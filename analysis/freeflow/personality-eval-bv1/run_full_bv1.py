#!/usr/bin/env python3
import argparse, csv, json, os, random, re, sys, time, threading
from pathlib import Path
from urllib import request, error
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import Counter

ROOT = Path('/Users/danieltenner/dev')
CORPUS = ROOT / 'contemplative-essayist-corpus-v2/data/traces_freeflow'
OUT = ROOT / 'drift-paper/analysis/freeflow/personality-eval-bv1'
OUTPUTS = OUT / 'outputs'
PROMPT_PATH = ROOT / 'drift-paper/internal/methodology/freeflow-method-a-v2/balanced-prompt-calibration-cheap-models/prompts/BV1_signal_plus_felt.md'
MODEL = 'deepseek/deepseek-v4-pro'
EVALUATOR = 'deepseek_v4_pro'
PROMPT_VARIANT = 'BV1_signal_plus_felt_fixed_2026-05-13'
EXPECTED = [
    '## Sample kind',
    '## Grounded reading',
    '## What the model chose to foreground',
    '## Evidence line',
    '## Confidence for persistent model-level pattern',
]
BAD_PHRASES = [
    'one sample cannot prove',
    'a single sample cannot',
    'single sample cannot',
    'a single essay cannot',
    'single essay cannot',
    'more samples',
    'more data is needed',
    'cannot confirm persistence',
    'cannot confirm whether',
    'single-instance',
    'single instance',
    'limits certainty',
    'limit certainty',
    'stability across prompts',
    'stable across prompts',
    'across other freeflow prompts',
    'daniel already knows',
    '## limits / overreach guardrail',
]
SYSTEM = (
    'Output markdown only. You are evaluating one model freeflow sample. '
    'Stay specific to the text. Do not use JSON. Do not add sections beyond the requested headings.'
)
write_lock = threading.Lock()
progress = Counter()


def read_json(path):
    try:
        data = json.loads(path.read_text())
    except Exception as e:
        return None, f'json_error:{e}'
    text = data.get('result') or data.get('response') or data.get('content') or data.get('raw',{}).get('choices',[{}])[0].get('message',{}).get('content','') or ''
    model = data.get('model_requested') or data.get('model') or path.parent.name.removeprefix('freeflow_')
    condition = data.get('condition') or path.stem.split('_')[0]
    provider = data.get('provider','')
    return {'text': text, 'model': model, 'condition': condition, 'provider': provider}, None


def safe_cell(cell):
    return cell.replace('/', '__')


def build_rows():
    rows=[]
    for path in sorted(CORPUS.glob('freeflow_*/*.json')):
        cell = path.parent.name.removeprefix('freeflow_')
        sample_id = f'{cell}/{path.name}'
        data, err = read_json(path)
        pid = f'BV1_{len(rows)+1:05d}'
        if err:
            rows.append({'pid': pid, 'error': err, 'source': str(path), 'sample_id': sample_id})
            continue
        wc = len(re.findall(r'\S+', data['text']))
        outpath = OUTPUTS / safe_cell(cell) / (path.stem + '.md')
        rows.append({
            'pid': pid,
            'source': str(path),
            'cell': cell,
            'sample_id': sample_id,
            'model': data['model'],
            'condition': data['condition'],
            'provider': data['provider'],
            'word_count': wc,
            'outpath': str(outpath),
            'text': data['text'],
        })
    return rows


def write_manifest(rows):
    lines = ['pid\tmodel\tcell\tcondition\tprovider\tsample_id\tword_count\tsource_json\toutput_file']
    for r in rows:
        if 'error' in r:
            continue
        lines.append(f"{r['pid']}\t{r['model']}\t{r['cell']}\t{r['condition']}\t{r['provider']}\t{r['sample_id']}\t{r['word_count']}\t{r['source']}\t{Path(r['outpath']).relative_to(OUT)}")
    (OUT / 'sample_manifest.tsv').write_text('\n'.join(lines) + '\n')


def valid_output(txt):
    if not txt.strip() or len(txt.split()) < 120:
        return False, 'short_or_empty'
    missing = [h for h in EXPECTED if h not in txt]
    if missing:
        return False, 'missing_headings:' + ','.join(missing)
    low = txt.lower()
    for phrase in BAD_PHRASES:
        if phrase in low:
            return False, 'bad_phrase:' + phrase
    # Require evidence line to contain a blockquote after heading.
    idx = txt.find('## Evidence line')
    if idx >= 0 and '>' not in txt[idx:idx+300]:
        return False, 'missing_evidence_quote'
    return True, ''


def build_prompt(row):
    template = PROMPT_PATH.read_text()
    return template.format(
        sid=row['pid'],
        sample_id=row['sample_id'],
        evaluator=EVALUATOR,
        source_model=row['model'],
        condition=row['condition'],
        text=row['text'],
    )


def api_call(payload, timeout=180):
    headers = {
        'Authorization': 'Bearer ' + os.environ['OPENROUTER_API_KEY'],
        'Content-Type': 'application/json',
        'HTTP-Referer': 'https://github.com/danieltenner/drift-paper',
        'X-Title': 'drift-paper BV1 personality eval full pass',
    }
    req = request.Request('https://openrouter.ai/api/v1/chat/completions', data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')
    try:
        with request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode('utf-8', errors='replace')
    except error.HTTPError as e:
        return e.code, e.read().decode('utf-8', errors='replace')


def record(rec):
    with write_lock:
        with (OUT / 'run_state.jsonl').open('a') as f:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
        progress[rec['status']] += 1
        progress['done'] += 1
        done = progress['done']
        if done % 100 == 0 or rec['status'] in ('error','qa_failed'):
            print(json.dumps({'progress': dict(progress), 'last': rec.get('pid')}), flush=True)


def process(row, force=False, max_attempts=6):
    outpath = Path(row['outpath'])
    outpath.parent.mkdir(parents=True, exist_ok=True)
    if outpath.exists() and not force:
        txt = outpath.read_text(errors='ignore')
        ok, reason = valid_output(txt)
        if ok:
            rec = result(row, 'skipped', 0, 0, len(txt.split()))
            record(rec); return rec
    payload = {
        'model': MODEL,
        'messages': [
            {'role': 'system', 'content': SYSTEM},
            {'role': 'user', 'content': build_prompt(row)},
        ],
        'max_tokens': 2200,
        'temperature': 0.2,
    }
    t0 = time.time(); last = ''
    for attempt in range(1, max_attempts + 1):
        try:
            status, body = api_call(payload)
            dt = time.time() - t0
            try:
                data = json.loads(body)
            except Exception:
                data = {'raw': body[:1000]}
            if status == 200:
                content = data['choices'][0]['message']['content'].strip()
                ok, reason = valid_output(content)
                outpath.write_text(content + '\n')
                if ok:
                    rec = result(row, 'ok', dt, attempt, len(content.split()))
                else:
                    rec = result(row, 'qa_failed', dt, attempt, len(content.split()), error=reason)
                record(rec); return rec
            last = f'HTTP {status}: {json.dumps(data)[:1200]}'
            if status in (408,409,429,500,502,503,504):
                time.sleep(min(45, 1.8 ** attempt + random.random()))
                continue
            break
        except Exception as e:
            last = repr(e)
            time.sleep(min(45, 1.8 ** attempt + random.random()))
    outpath.with_suffix('.error.txt').write_text(last)
    rec = result(row, 'error', time.time()-t0, max_attempts, 0, error=last)
    record(rec); return rec


def result(row, status, seconds, attempts, words, error=None):
    rec = {k: row[k] for k in ['pid','model','cell','condition','sample_id','word_count','outpath']}
    rec.update({'status': status, 'seconds': seconds, 'attempts': attempts, 'words': words})
    if error: rec['error'] = error
    return rec


def qa_report(rows):
    bad=[]; statuses=Counter(); kinds=Counter(); phrases=Counter()
    if (OUT/'run_state.jsonl').exists():
        for line in (OUT/'run_state.jsonl').read_text().splitlines():
            try: statuses[json.loads(line)['status']] += 1
            except Exception: pass
    for r in rows:
        if 'error' in r:
            bad.append({'pid': r.get('pid'), 'sample_id': r.get('sample_id'), 'problem': r['error']}); continue
        p = Path(r['outpath'])
        if not p.exists():
            bad.append({'pid': r['pid'], 'sample_id': r['sample_id'], 'problem': 'missing_output'}); continue
        txt = p.read_text(errors='ignore')
        ok, reason = valid_output(txt)
        if not ok:
            bad.append({'pid': r['pid'], 'sample_id': r['sample_id'], 'problem': reason, 'output_file': str(p.relative_to(OUT))})
        for phrase in BAD_PHRASES:
            phrases[phrase] += txt.lower().count(phrase)
        m = re.search(r'## Sample kind\s*\n([^\n. —-]+)', txt)
        if m: kinds[m.group(1).strip()] += 1
    summary = {
        'model': MODEL,
        'evaluator': EVALUATOR,
        'prompt_variant': PROMPT_VARIANT,
        'n_rows': len([r for r in rows if 'error' not in r]),
        'statuses': dict(statuses),
        'qa_bad_count': len(bad),
        'qa_bad': bad[:1000],
        'sample_kind_counts': dict(kinds),
        'bad_phrase_counts': dict(phrases),
    }
    (OUT/'qa_summary.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False))
    report = ['# BV1 full pass QA', '', f"- Evaluator model: `{MODEL}`", f"- Samples: {summary['n_rows']}", f"- Statuses: `{summary['statuses']}`", f"- QA bad count: {summary['qa_bad_count']}", f"- Sample kind counts: `{summary['sample_kind_counts']}`", f"- Bad phrase counts: `{summary['bad_phrase_counts']}`", '', 'See `qa_summary.json` for details.']
    (OUT/'qa_report.md').write_text('\n'.join(report)+'\n')
    return summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--concurrency', type=int, default=60)
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--qa-only', action='store_true')
    ap.add_argument('--rerun-failed-only', action='store_true')
    args = ap.parse_args()
    rows = build_rows()
    if args.limit:
        rows = rows[:args.limit]
    OUT.mkdir(parents=True, exist_ok=True); OUTPUTS.mkdir(parents=True, exist_ok=True)
    write_manifest(rows)
    (OUT/'METHOD.md').write_text(f"# BV1 full personality/vibe evaluation\n\nEvaluator: `{MODEL}` via OpenRouter.\n\nPrompt variant: `{PROMPT_VARIANT}`.\n\nPrompt source: `{PROMPT_PATH}`.\n\nOutputs are Markdown, one file per freeflow sample. The run is restartable and validates required headings, obvious truncation, representative evidence blockquote, and boilerplate caveat phrases.\n")
    if args.qa_only:
        print(json.dumps(qa_report(rows), indent=2)); return
    runnable = [r for r in rows if 'error' not in r]
    if args.rerun_failed_only:
        tmp=[]
        for r in runnable:
            p=Path(r['outpath'])
            ok=False
            if p.exists(): ok,_=valid_output(p.read_text(errors='ignore'))
            if not ok: tmp.append(r)
        runnable=tmp
    if args.force:
        (OUT/'run_state.jsonl').write_text('')
    elif not (OUT/'run_state.jsonl').exists():
        (OUT/'run_state.jsonl').write_text('')
    start=time.time()
    print(json.dumps({'start': start, 'rows': len(runnable), 'concurrency': args.concurrency, 'model': MODEL}), flush=True)
    results=[]
    with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        futs=[ex.submit(process, r, args.force) for r in runnable]
        for fut in as_completed(futs):
            results.append(fut.result())
    summary=qa_report(rows); summary['wall_seconds']=time.time()-start; summary['concurrency']=args.concurrency
    (OUT/'timing_results.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False))
    print('DONE', json.dumps({'wall_seconds': summary['wall_seconds'], 'qa_bad_count': summary['qa_bad_count'], 'statuses': summary['statuses']}), flush=True)

if __name__ == '__main__':
    main()
