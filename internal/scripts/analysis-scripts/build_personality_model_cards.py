#!/usr/bin/env python3
from __future__ import annotations
import json, re, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
AGG=ROOT/'analysis/freeflow/personality-aggregates'
DIFF=ROOT/'analysis/freeflow/model-cell-difference-analysis'
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
    m=re.search(rf'## {re.escape(heading)}\s*\n(.*?)(?=\n## |\Z)', txt, re.S)
    return m.group(1).strip() if m else ''

def clean_card_text(txt):
    # The personality cards should be pure model descriptions, not audit metadata.
    replacements = [
        (r'\b[Cc]ell-level\b', 'model-level'),
        (r'\bper-cell\b', 'per-sample'),
        (r'\b[Cc]ells\b', 'variants'),
        (r'\b[Cc]ell\b', 'variant'),
    ]
    for pat, rep in replacements:
        txt=re.sub(pat, rep, txt)
    return txt.strip()

def load_decisions():
    p=DIFF/'decisions.json'
    if not p.exists(): return {}
    return {r['model']: r for r in json.loads(p.read_text())}

def main():
    manifest=json.loads((AGG/'manifest.json').read_text())
    by=collections.defaultdict(list)
    for m in manifest:
        by[canonical(m.get('source_models'), m['cell'])].append(m)
    if OUT.exists():
        for path in sorted(OUT.rglob('*'), reverse=True):
            if path.is_file(): path.unlink()
            elif path.is_dir(): path.rmdir()
    OUT.mkdir(parents=True, exist_ok=True); CARDS.mkdir(parents=True, exist_ok=True)
    decisions=load_decisions()
    index=[]
    for model, variants in sorted(by.items()):
        variants=sorted(variants, key=lambda m:m['cell'])
        sf=safe(model)
        body=''
        if len(variants)>1:
            rpt=DIFF/'model-cell-difference-reports'/f'{sf}.md'
            if rpt.exists():
                body=section(rpt.read_text(errors='ignore'), 'Model-level personality card')
        if not body:
            # Single-variant models, or fallback if no difference report exists.
            reads=[]
            for m in variants:
                txt=(ROOT/m['aggregate']).read_text(errors='ignore')
                reads.append(section(txt,'Cell-level freeflow read') or section(txt,'Aggregate profile'))
            body='\n\n'.join(x for x in reads if x).strip()
        body=clean_card_text(body or '(No personality card text found.)')
        sample_count=sum(v['samples'] for v in variants)
        variant_count=len(variants)
        parts=[f'# {model} — freeflow personality card', '', f'_Based on {sample_count} freeflow samples' + (f' across {variant_count} route/provider variants' if variant_count>1 else '') + '._', '', body]
        out=CARDS/f'{sf}.md'
        out.write_text('\n'.join(parts).strip()+'\n')
        index.append({'model':model,'safe':sf,'variants':variant_count,'samples':sample_count,'card':str(out.relative_to(ROOT)),'difference_decision':decisions.get(model,{}).get('decision','SINGLE_VARIANT')})
    (OUT/'index.json').write_text(json.dumps(index, indent=2, ensure_ascii=False))
    lines=['# Freeflow personality model cards','', 'Clean model-level personality cards collapsed from the freeflow personality analysis.', '', f'- Model cards: {len(index)}', f'- Source aggregates: `analysis/freeflow/personality-aggregates/`', f'- Difference analysis: `analysis/freeflow/model-cell-difference-analysis/`', '', '## Cards', '']
    for r in index:
        lines.append(f'- [{r["model"]}](cards/{r["safe"]}.md) — samples: {r["samples"]}; variants: {r["variants"]}')
    (OUT/'README.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps({'cards':len(index),'out':str(OUT)}, indent=2))
if __name__=='__main__': main()
