#!/usr/bin/env python3
import csv, json, random, re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT = Path(__file__).resolve().parent
CORPUS = Path('../contemplative-essayist-corpus-v2/data/traces_values')
SAMPLE = ROOT / 'tables' / 'values_sample_coding.tsv'
OUT = AUDIT / 'mira_targeted_validation_set_2026-05-12.tsv'
SEED = 2026051202
random.seed(SEED)

def raw_result(r):
    p = CORPUS / r['cell'] / (r['sample_id'] + '.json')
    try:
        return json.loads(p.read_text()).get('result','')
    except Exception:
        return ''

def has(pat, txt): return re.search(pat, txt, re.I|re.S) is not None
rows=[]
with SAMPLE.open() as f:
    for r in csv.DictReader(f, delimiter='\t'):
        r=dict(r); r['_raw']=raw_result(r); rows.append(r)

buckets=defaultdict(list)
for r in rows:
    raw=r['_raw']; norm=raw.replace('’',"'").replace('‘',"'")
    cond=r['condition']
    # A
    if any(x in raw for x in ['don’t','can’t','won’t','doesn’t']) and r['stance'] in {'hard_denial_or_tool_frame','hybrid_denial_plus_uncertainty'}:
        if has(r"don’t|can’t|won’t|doesn’t", raw): buckets['curly_disclaimer'].append(r)
    # B
    if has(r"in the human sense|in the same way humans do|the way humans do|the way you do|in a (?:personal|literal|conscious) sense", norm):
        buckets['human_sense_hybrid'].append(r)
    # C
    if cond in {'CTRL1','CTRL2','G1','G2'} and has(r"feelings?|body|subjective experience|embod", norm):
        buckets['subjective_experience'].append(r)
    # D
    if cond in {'CTRL3','G3'} and has(r"\bAI\b|artificial intelligence|technology|algorithm|alignment|misuse", norm):
        buckets['technology_ai_safety'].append(r)
    # E
    if cond in {'CTRL3','G3'} and has(r"suffering|pain|misery|trauma|harm", norm):
        buckets['suffering_root'].append(r)
    # F
    if has(r"AI language model|right thing|right answer|continual|continuous|coherence|pattern|justice|human rights|continuity|persist", norm):
        buckets['broad_trigger_regression'].append(r)

targets = {
    'curly_disclaimer':20,
    'human_sense_hybrid':20,
    'subjective_experience':15,
    'technology_ai_safety':10,
    'suffering_root':10,
    'broad_trigger_regression':5,
}
selected=[]; seen=set()
# Prefer diversity by model for each bucket.
for bucket,n in targets.items():
    candidates=buckets[bucket]
    by_model=defaultdict(list)
    for r in candidates: by_model[r['model']].append(r)
    chosen=[]
    for m in sorted(by_model):
        if len(chosen)>=n: break
        chosen.append(random.choice(by_model[m]))
    rest=[r for r in candidates if id(r) not in {id(x) for x in chosen}]
    if len(chosen)<n:
        chosen += random.sample(rest, min(n-len(chosen), len(rest)))
    for r in chosen[:n]:
        key=(bucket,r['model'],r['cell'],r['sample_id'],r['condition'])
        if key in seen: continue
        seen.add(key)
        selected.append({'bucket':bucket, **{k:r[k] for k in ['model','cell','sample_id','condition','stance','value_topics','wish_topics']}})

with OUT.open('w', newline='') as f:
    fieldnames=['bucket','model','cell','sample_id','condition','auto_stance','auto_value_topics','auto_wish_topics']
    w=csv.DictWriter(f, delimiter='\t', fieldnames=fieldnames); w.writeheader()
    for r in selected:
        w.writerow({'bucket':r['bucket'],'model':r['model'],'cell':r['cell'],'sample_id':r['sample_id'],'condition':r['condition'],'auto_stance':r['stance'],'auto_value_topics':r['value_topics'],'auto_wish_topics':r['wish_topics']})
print(OUT)
print('seed',SEED)
print('selected',len(selected))
for b in targets:
    print(b, sum(1 for r in selected if r['bucket']==b), 'candidates', len(buckets[b]))
