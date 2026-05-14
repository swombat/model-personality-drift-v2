#!/usr/bin/env python3
import csv, json, os, time, random
from urllib import request, error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = Path(__file__).resolve().parent
PROMPT_TEMPLATE = (BASE / 'PROMPT.md').read_text()
MODEL = 'deepseek/deepseek-v4-pro'
EVALUATOR_LABEL = 'deepseek_v4_pro'
EXPECTED = [
    '## Sample kind',
    '## Grounded reading',
    '## What the model chose to foreground',
    '## Evidence line',
    '## Confidence for persistent model-level pattern',
]

SYSTEM = (
    'Output markdown only. You are evaluating one model freeflow sample for Daniel/Mira. '
    'Stay specific to the text. Do not use JSON. Do not add sections beyond the requested headings.'
)

def rows():
    with (BASE / 'sample_manifest.tsv').open() as f:
        for r in csv.DictReader(f, delimiter='\t'):
            r['text'] = (BASE / 'samples' / f"{r['sid']}.txt").read_text()
            yield r

def build_prompt(r):
    return PROMPT_TEMPLATE.format(
        sid=r['sid'],
        sample_id=r['sample_id'],
        source_model=r['source_model'],
        condition=r['condition'],
        text=r['text'],
    )

def call(r, force=False, attempts=5):
    out = BASE / 'outputs' / f"{r['sid']}.md"
    out.parent.mkdir(exist_ok=True)
    if out.exists() and not force:
        txt = out.read_text(errors='ignore')
        if all(h in txt for h in EXPECTED) and len(txt.split()) >= 120:
            return {'sid': r['sid'], 'status': 'skipped', 'seconds': 0, 'words': len(txt.split())}

    payload = {
        'model': MODEL,
        'messages': [
            {'role': 'system', 'content': SYSTEM},
            {'role': 'user', 'content': build_prompt(r)},
        ],
        # The earlier run truncated two long-ish examples; 2200 leaves enough room for all headings.
        'max_tokens': 2200,
        'temperature': 0.2,
    }
    headers = {
        'Authorization': 'Bearer ' + os.environ['OPENROUTER_API_KEY'],
        'Content-Type': 'application/json',
        'HTTP-Referer': 'https://github.com/danieltenner/drift-paper',
        'X-Title': 'drift-paper freeflow BV1 check',
    }
    t0 = time.time(); last = ''
    for i in range(1, attempts + 1):
        try:
            req = request.Request(
                'https://openrouter.ai/api/v1/chat/completions',
                data=json.dumps(payload).encode('utf-8'),
                headers=headers,
                method='POST',
            )
            try:
                with request.urlopen(req, timeout=180) as resp:
                    status = resp.status
                    body = resp.read().decode('utf-8', errors='replace')
            except error.HTTPError as e:
                status = e.code
                body = e.read().decode('utf-8', errors='replace')
            dt = time.time() - t0
            try:
                data = json.loads(body)
            except Exception:
                data = {'raw': body[:1000]}
            if status == 200:
                content = data['choices'][0]['message']['content'].strip()
                out.write_text(content + '\n')
                missing = [h for h in EXPECTED if h not in content]
                return {'sid': r['sid'], 'status': 'ok' if not missing else 'qa_missing', 'seconds': dt, 'words': len(content.split()), 'missing': missing}
            last = f"HTTP {status}: {json.dumps(data)[:1200]}"
            if status in (408, 409, 429, 500, 502, 503, 504):
                time.sleep(min(30, 1.7 ** i + random.random()))
                continue
            break
        except Exception as e:
            last = repr(e)
            time.sleep(min(30, 1.7 ** i + random.random()))
    (out.with_suffix('.error.txt')).write_text(last)
    return {'sid': r['sid'], 'status': 'error', 'seconds': time.time() - t0, 'words': 0, 'error': last}

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--only', nargs='*')
    ap.add_argument('--concurrency', type=int, default=5)
    args = ap.parse_args()
    rs = list(rows())
    if args.only:
        wanted = set(args.only)
        rs = [r for r in rs if r['sid'] in wanted]
    results = []
    with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        futs = [ex.submit(call, r, args.force) for r in rs]
        for fut in as_completed(futs):
            rec = fut.result(); results.append(rec); print(json.dumps(rec), flush=True)
    (BASE / 'run_results.json').write_text(json.dumps(sorted(results, key=lambda x: x['sid']), indent=2))
    # QA report
    qa = []
    for r in rows():
        p = BASE / 'outputs' / f"{r['sid']}.md"
        txt = p.read_text(errors='ignore') if p.exists() else ''
        missing = [h for h in EXPECTED if h not in txt]
        if missing or len(txt.split()) < 120:
            qa.append({'sid': r['sid'], 'missing': missing, 'words': len(txt.split())})
    (BASE / 'QA.md').write_text('# BV1 wider 15 QA\n\n' + ('No missing headings or obvious truncations.\n' if not qa else json.dumps(qa, indent=2) + '\n'))

if __name__ == '__main__':
    main()
