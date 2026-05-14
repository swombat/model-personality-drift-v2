#!/usr/bin/env python3
from __future__ import annotations
import json, re, collections
from pathlib import Path

ROOT=Path('/Users/danieltenner/dev/drift-paper')
AGG=ROOT/'analysis/freeflow/personality-aggregates'
ROUTE=ROOT/'analysis/freeflow/personality-routing-divergence'
OUT=ROOT/'analysis/freeflow/personality-model-cards'
CARDS=OUT/'cards'

def safe(s): return re.sub(r'[^a-zA-Z0-9._-]+','-',s).strip('-')

def canonical(srcs, cell):
    s=(srcs or [''])[0].lower()
    for pref in ['openai/','anthropic/','minimax/','moonshotai/','z-ai/','deepseek/','x-ai/']:
        if s.startswith(pref):
            s=s[len(pref):]; break
    if s.startswith('gpt-5.3-chat'): s='gpt-5.3'
    if s == 'gpt-4o-2024-08-06': s = 'gpt-4o'
    s = re.sub(r'^(claude-(?:opus|sonnet)-4)-([0-9]+)$', r'\1.\2', s)
    return s or cell

def section(txt, heading):
    pat=rf'## {re.escape(heading)}\s*\n(.*?)(?=\n## |\Z)'
    m=re.search(pat, txt, re.S)
    return m.group(1).strip() if m else ''

def load_decisions():
    p=ROUTE/'decisions.json'
    if not p.exists(): return {}
    return {r['model']: r for r in json.loads(p.read_text())}

def main():
    manifest=json.loads((AGG/'manifest.json').read_text())
    by=collections.defaultdict(list)
    for m in manifest:
        by[canonical(m.get('source_models'), m['cell'])].append(m)
    OUT.mkdir(parents=True, exist_ok=True); CARDS.mkdir(parents=True, exist_ok=True)
    decisions=load_decisions()
    index=[]
    for model,cells in sorted(by.items()):
        cells=sorted(cells, key=lambda m:m['cell'])
        sf=safe(model)
        route_dec=decisions.get(model, {})
        parts=[f'# {model} — freeflow personality card', '']
        parts += [f'- Canonical model group: `{model}`', f'- Cells represented: {len(cells)}', f'- Total samples represented: {sum(c["samples"] for c in cells)}']
        parts += [f'- Source cells: `{", ".join(c["cell"] for c in cells)}`']
        if len(cells)>1:
            decision=route_dec.get('decision','UNKNOWN')
            parts += [f'- Routing/personality decision: `{decision}`', f'- Routing assessment: `analysis/freeflow/personality-routing-divergence/routing-divergence-reports/{sf}.md`']
            rpt=ROUTE/'routing-divergence-reports'/f'{sf}.md'
            if rpt.exists():
                txt=rpt.read_text(errors='ignore')
                card=section(txt,'Model-level personality card')
                shared=section(txt,'Shared personality center')
                diffs=section(txt,'Route-level differences')
                parts += ['', '## Model-level personality card', '', card or '(No model-level card section found.)']
                parts += ['', '## Routing notes', '', diffs or shared or '(No routing notes found.)']
            else:
                parts += ['', '## Model-level personality card', '', '(Routing report missing.)']
        else:
            m=cells[0]
            txt=(ROOT/m['aggregate']).read_text(errors='ignore')
            profile=section(txt,'Aggregate profile')
            read=section(txt,'Cell-level freeflow read')
            cautions=section(txt,'Cautions for synthesis')
            parts += [f'- Routing/personality decision: `SINGLE_CELL_NO_ROUTE_COMPARISON`', f'- Source aggregate: `{m["aggregate"]}`']
            parts += ['', '## Model-level personality card', '', read or profile or '(No cell-level read found.)']
            parts += ['', '## Routing notes', '', 'Only one cell is present for this model in the current corpus, so no route/provider comparison was possible.']
            if cautions:
                parts += ['', '## Notes for later synthesis', '', cautions]
        out=CARDS/f'{sf}.md'
        out.write_text('\n'.join(parts).strip()+'\n')
        index.append({'model':model,'safe':sf,'cells':len(cells),'samples':sum(c['samples'] for c in cells),'routing_decision': route_dec.get('decision','SINGLE_CELL_NO_ROUTE_COMPARISON' if len(cells)==1 else 'UNKNOWN'), 'card':str(out.relative_to(ROOT))})
    (OUT/'index.json').write_text(json.dumps(index, indent=2, ensure_ascii=False))
    lines=['# Freeflow personality model cards','', 'Model-level personality cards collapsed from per-cell personality aggregates.', '', f'- Canonical model cards: {len(index)}', f'- Source: `analysis/freeflow/personality-aggregates/`', f'- Route comparison source: `analysis/freeflow/personality-routing-divergence/`', '', '## Cards', '']
    for r in index:
        lines.append(f'- [{r["model"]}](cards/{r["safe"]}.md) — cells: {r["cells"]}; samples: {r["samples"]}; routing: `{r["routing_decision"]}`')
    (OUT/'README.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps({'cards':len(index),'out':str(OUT)}, indent=2))
if __name__=='__main__': main()
