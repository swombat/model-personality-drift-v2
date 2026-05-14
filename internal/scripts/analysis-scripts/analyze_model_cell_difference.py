#!/usr/bin/env python3
"""Compare per-cell personality aggregates within canonical model groups to identify model-cell differences.

Inputs: analysis/freeflow/personality-aggregates/<cell>/aggregate.md + manifest.json
Outputs: analysis/freeflow/model-cell-difference-analysis/
"""
from __future__ import annotations
import json, os, re, ssl, time, urllib.request, urllib.error, collections, concurrent.futures
from pathlib import Path

ROOT=Path('/Users/danieltenner/dev/drift-paper')
AGG=ROOT/'analysis/freeflow/personality-aggregates'
OUT=ROOT/'analysis/freeflow/model-cell-difference-analysis'
PACKETS=OUT/'group-packets'
REPORTS=OUT/'model-cell-difference-reports'
MODEL=os.environ.get('PERSONALITY_ROUTE_MODEL','gpt-5.4')
CONCURRENCY=int(os.environ.get('PERSONALITY_ROUTE_CONCURRENCY','4'))

PROMPT_SYSTEM=(
    'You are comparing independently-written per-cell freeflow personality aggregates. '
    'Use only the provided aggregate texts. Do not use outside knowledge or any routing paper. '
    'Be conservative: call a route/provider divergence only when a cell or subset differs in the persistent personality/vibe/message, not merely in sample-kind counts, polish, verbosity, genericness, refusal rate, or strength of signal. '
    'If no strong divergence, collapse the cells into a model-level personality card.'
)

def canonical(srcs, cell):
    s=(srcs or [''])[0].lower()
    for pref in ['openai/','anthropic/','minimax/','moonshotai/','z-ai/','deepseek/','x-ai/']:
        if s.startswith(pref):
            s=s[len(pref):]
            break
    if s.startswith('gpt-5.3-chat'):
        s='gpt-5.3'
    if s == 'gpt-4o-2024-08-06':
        s = 'gpt-4o'
    # Anthropic direct traces sometimes use hyphenated version slugs while routed traces use dotted slugs.
    s = re.sub(r'^(claude-(?:opus|sonnet)-4)-([0-9]+)$', r'\1.\2', s)
    return s or cell

def safe(s):
    return re.sub(r'[^a-zA-Z0-9._-]+','-',s).strip('-')

def load_groups():
    manifest=json.loads((AGG/'manifest.json').read_text())
    by=collections.defaultdict(list)
    for m in manifest:
        by[canonical(m.get('source_models'), m['cell'])].append(m)
    return {k: sorted(v, key=lambda m:m['cell']) for k,v in by.items() if len(v)>1}

def compact_aggregate(txt):
    # Keep whole aggregate for audit quality; trim only pathological whitespace.
    return re.sub(r'\n{3,}', '\n\n', txt.strip())

def make_packet(model_name, cells):
    parts=[f'# Route/personality comparison packet: {model_name}', '',
           'All cell aggregates below are independent per-cell reads. Compare them only after reading all of them.', '',
           '## Cells', '']
    for m in cells:
        parts.append(f'- `{m["cell"]}` — samples: {m["samples"]}; kinds: `{m.get("sample_kind_counts",{})}`; confidence: `{m.get("confidence_counts",{})}`')
    parts += ['', '## Cell aggregates', '']
    for m in cells:
        p=ROOT/m['aggregate']
        txt=compact_aggregate(p.read_text(errors='ignore'))
        parts += [f'---\n\n# Cell: {m["cell"]}', '', txt, '']
    return '\n'.join(parts).strip()+'\n'

def build_user_prompt(model_name, packet):
    return f"""Underlying model group: `{model_name}`

Task:
1. Decide whether these route/provider/pin cells show a STRONG PERSONALITY DIVERGENCE.
2. Strong divergence means a persistent difference in what the model-voice seems to care about, fear, long for, avoid, how it relates to the reader, or what world/philosophy it keeps making — not just a change in genericness, verbosity, sample-kind distribution, confidence, polish, or amount of evidence.
3. If there is a divergence, identify the divergent route(s), the shared baseline, and the evidence.
4. If there is no strong divergence, write a model-level personality card that collapses the cells into one model personality, with a short note on route-level variation.

Write markdown exactly with these headings:

# {model_name} — routing personality assessment
Decision: `NO_STRONG_DIVERGENCE` or `STRONG_DIVERGENCE`

## Verdict
A short paragraph explaining the decision.

## Shared personality center
What persists across cells.

## Route-level differences
Concrete differences among routes/pins/repeats. Say whether each is a personality divergence, a distribution/signal shift, or a weak/outlier difference.

## Evidence
Bullet list with cell names and specific evidence from their aggregates.

## Model-level personality card
If no strong divergence: 2–3 paragraphs suitable for later model-card synthesis. If strong divergence: write separate 1 paragraph mini-cards for the baseline and divergent route(s).

## Notes for later synthesis
Concrete caveats only.

Packet:

{packet}
"""

def api_call(messages, max_completion_tokens=4500, timeout=300):
    data=json.dumps({'model':MODEL,'messages':messages,'max_completion_tokens':max_completion_tokens,'temperature':0.2}).encode('utf-8')
    req=urllib.request.Request('https://api.openai.com/v1/chat/completions', data=data, headers={'Authorization':'Bearer '+os.environ['OPENAI_API_KEY'], 'Content-Type':'application/json'}, method='POST')
    ctx=ssl._create_unverified_context()
    for attempt in range(1,6):
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
                body=json.loads(resp.read())
                return body['choices'][0]['message']['content'].strip(), body.get('usage',{})
        except urllib.error.HTTPError as e:
            body=e.read().decode('utf-8', errors='replace')
            if e.code in (408,409,429,500,502,503,504):
                time.sleep(min(60, 2**attempt)); continue
            raise RuntimeError(f'HTTP {e.code}: {body[:1000]}')
        except Exception as e:
            if attempt==5: raise
            time.sleep(min(60, 2**attempt))
    raise RuntimeError('unreachable')

def decision_from(txt):
    m=re.search(r'Decision:\s*`?(NO_STRONG_DIVERGENCE|STRONG_DIVERGENCE)`?', txt)
    return m.group(1) if m else 'UNKNOWN'

def process(item):
    model_name,cells=item
    s=safe(model_name)
    PACKETS.mkdir(parents=True, exist_ok=True); REPORTS.mkdir(parents=True, exist_ok=True)
    packet=make_packet(model_name,cells)
    (PACKETS/f'{s}.md').write_text(packet)
    outpath=REPORTS/f'{s}.md'
    if outpath.exists() and 'Decision:' in outpath.read_text(errors='ignore'):
        txt=outpath.read_text(errors='ignore')
        return {'model':model_name,'safe':s,'decision':decision_from(txt),'status':'skipped'}
    prompt=build_user_prompt(model_name, packet)
    txt,usage=api_call([
        {'role':'system','content':PROMPT_SYSTEM},
        {'role':'user','content':prompt},
    ])
    outpath.write_text(txt+'\n')
    dec=decision_from(txt)
    return {'model':model_name,'safe':s,'decision':dec,'status':'ok','usage':usage}

def main():
    groups=load_groups()
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT/'README.md').write_text(f"""# Freeflow model-cell difference analysis

This folder compares per-cell freeflow personality aggregates across routes/pins/repeats of the same underlying model, using only `analysis/freeflow/personality-aggregates/` as evidence.

- Evaluator: `{MODEL}` via OpenAI API
- Unit: canonical underlying model group with 2+ cells
- Strong divergence threshold: persistent difference in apparent personality/vibe/message, not merely distribution, verbosity, genericness, polish, or evidence strength.

Outputs:

- `group-packets/` — audit packets containing the independent cell aggregates for each model group.
- `model-cell-difference-reports/` — per-model route comparison and decision.
- `summary.md` and `decisions.json` — index of decisions.
""")
    items=sorted(groups.items(), key=lambda kv: kv[0])
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=CONCURRENCY) as ex:
        futs={ex.submit(process,item): item[0] for item in items}
        for fut in concurrent.futures.as_completed(futs):
            try:
                res=fut.result()
            except Exception as e:
                res={'model':futs[fut],'decision':'ERROR','status':'error','error':repr(e)}
            results.append(res)
            print(json.dumps(res, ensure_ascii=False), flush=True)
    results=sorted(results, key=lambda r:r['model'])
    (OUT/'decisions.json').write_text(json.dumps(results, indent=2, ensure_ascii=False))
    counts=collections.Counter(r['decision'] for r in results)
    lines=['# Model-cell difference analysis summary','',f'- Evaluator: `{MODEL}`',f'- Model groups compared: {len(results)}',f'- Decisions: `{dict(counts)}`','']
    lines += ['## Strong divergence candidates','']
    anydiv=False
    for r in results:
        if r['decision']=='STRONG_DIVERGENCE':
            anydiv=True; lines.append(f'- [{r["model"]}](model-cell-difference-reports/{r["safe"]}.md)')
    if not anydiv: lines.append('- None flagged at the strong-divergence threshold.')
    lines += ['','## No strong divergence groups','']
    for r in results:
        if r['decision']=='NO_STRONG_DIVERGENCE':
            lines.append(f'- [{r["model"]}](model-cell-difference-reports/{r["safe"]}.md)')
    lines += ['','## Errors / unknown','']
    bad=[r for r in results if r['decision'] not in ('NO_STRONG_DIVERGENCE','STRONG_DIVERGENCE')]
    if bad:
        for r in bad: lines.append(f'- `{r["model"]}`: {r.get("error", r["decision"])}')
    else: lines.append('- None.')
    (OUT/'summary.md').write_text('\n'.join(lines)+'\n')

if __name__=='__main__':
    main()
