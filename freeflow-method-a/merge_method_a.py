import csv,json,glob,collections,os
from pathlib import Path
ROOT=Path('/Users/danieltenner/dev/drift-paper')
DIR=ROOT/'freeflow-method-a'
CH=DIR/'chunks'
# include main chunks only, exclude partial small openai if appear and zero file? exclude openai_small
files=[
 'method_a_starter_a.jsonl','method_a_anthropic_a.jsonl','method_a_openai_a.jsonl','method_a_deepseek_b.jsonl','method_a_glm51_b.jsonl','method_a_glm_other_b.jsonl','method_a_grok_codex_b.jsonl','method_a_kimi_minimax_b.jsonl'
]
rows=[]; byid={}; dup=[]; bad=[]
for name in files:
    p=CH/name
    if not p.exists(): bad.append(f'missing file {name}'); continue
    for i,line in enumerate(open(p),1):
        if not line.strip(): continue
        try: r=json.loads(line)
        except Exception as e: bad.append(f'{name}:{i}: json {e}'); continue
        sid=r.get('sample_id')
        if sid in byid: dup.append(sid)
        byid[sid]=r; rows.append(r)
expected=list(csv.DictReader(open(ROOT/'freeflow-taxonomy/sample_coding.tsv'), delimiter='\t'))
exp_ids=[r['sample_id'] for r in expected]
missing=[sid for sid in exp_ids if sid not in byid]
extra=[sid for sid in byid if sid not in set(exp_ids)]
# order by source tsv
ordered=[byid[sid] for sid in exp_ids if sid in byid]
with open(DIR/'sample_impressions.jsonl','w') as f:
    for r in ordered: f.write(json.dumps(r,ensure_ascii=False)+'\n')
# tsv selected fields plus tags pipe
cols=['model','lab','cell','file','condition','sample_id','word_count','production_frame','narrator_stance','substrate_posture','top_semantic_field','top_climate_field','impression_sentence','representative_sentence','optional_tags','coder_id','method_version']
with open(DIR/'sample_impressions.tsv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols,delimiter='\t',extrasaction='ignore')
    w.writeheader()
    for r in ordered:
        rr=dict(r); rr['optional_tags']='|'.join(rr.get('optional_tags') or [])
        w.writerow(rr)
counts=collections.Counter(r['model'] for r in ordered)
exp_counts=collections.Counter(r['model'] for r in expected)
report=[]
report.append('# Method A merge QA\n')
report.append(f'- Rows expected: {len(expected)}\n')
report.append(f'- Rows merged: {len(ordered)}\n')
report.append(f'- Missing sample IDs: {len(missing)}\n')
report.append(f'- Extra sample IDs: {len(extra)}\n')
report.append(f'- Duplicate sample IDs encountered: {len(dup)}\n')
report.append(f'- Parse/schema errors: {len(bad)}\n')
if missing:
    report.append('\n## Missing\n')
    report += [f'- {m}\n' for m in missing[:100]]
if bad:
    report.append('\n## Errors\n')
    report += [f'- {b}\n' for b in bad[:100]]
report.append('\n## Model counts\n\n| Model | Expected | Merged |\n|---|---:|---:|\n')
for m in sorted(exp_counts): report.append(f'| {m} | {exp_counts[m]} | {counts[m]} |\n')
(DIR/'MERGE_QA.md').write_text(''.join(report))
print('merged',len(ordered),'missing',len(missing),'extra',len(extra),'dup',len(dup),'bad',len(bad))
