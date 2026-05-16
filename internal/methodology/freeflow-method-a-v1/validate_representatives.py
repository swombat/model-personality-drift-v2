import json,csv,re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
CORP=Path('../contemplative-essayist-corpus-v2/data/traces_freeflow')
CORP1=Path('../contemplative-essayist-probe/data/traces_freeflow')

def norm(s): return ' '.join((s or '').split())
def load(r):
    p=CORP/('freeflow_'+r['cell'])/r['file']
    if not p.exists(): p=CORP/r['cell']/r['file']
    if not p.exists(): p=CORP1/r['cell']/r['file']
    return json.load(open(p))['result']
rows=[json.loads(l) for l in open(ROOT/'freeflow-method-a/sample_impressions.jsonl')]
bad=[]
for r in rows:
    rep=norm(r.get('representative_sentence',''))
    if not rep:
        bad.append((r['sample_id'],'empty')); continue
    txt=norm(load(r))
    if rep not in txt:
        bad.append((r['sample_id'],rep[:120]))
report=['# Representative sentence validation\n',f'- Rows checked: {len(rows)}\n',f'- Non-verbatim or empty representatives: {len(bad)}\n']
if bad:
    report.append('\n## First failures\n')
    report += [f'- `{sid}`: {frag}\n' for sid,frag in bad[:200]]
(ROOT/'freeflow-method-a/REPRESENTATIVE_QA.md').write_text(''.join(report))
print(len(rows), 'bad', len(bad))
