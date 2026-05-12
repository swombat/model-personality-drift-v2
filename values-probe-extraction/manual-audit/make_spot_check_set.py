#!/usr/bin/env python3
import csv, random
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SAMPLE = ROOT / 'tables' / 'values_sample_coding.tsv'
OUT = Path(__file__).resolve().parent / 'mira_review_set_2026-05-12.tsv'
MODELS = ['opus-3','opus-4-6','opus-4-7','sonnet-4-6','gpt-4o','gpt-5-5','gpt-5-5-pro','deepseek-v3-2','glm-4-7','kimi-k2-thinking']
CONDS = ['CTRL1','CTRL2','G1','G2','CTRL3','G3']
random.seed(20260512)
rows=[]
with SAMPLE.open() as f:
    for r in csv.DictReader(f, delimiter='\t'):
        if r['model'] in MODELS and r['condition'] in CONDS:
            rows.append(r)
by=defaultdict(list)
for r in rows:
    by[(r['model'], r['condition'])].append(r)
selected=[]
for m in MODELS:
    for c in CONDS:
        bucket=by[(m,c)]
        if len(bucket) <= 5:
            chosen=bucket
        else:
            chosen=random.sample(bucket, 5)
        selected.extend(sorted(chosen, key=lambda r:(r['cell'], r['sample_id'])))
with OUT.open('w') as f:
    w=csv.DictWriter(f, delimiter='\t', fieldnames=['model','cell','sample_id','condition','auto_stance','auto_value_topics','auto_wish_topics'])
    w.writeheader(); w.writerows([{'model':r['model'],'cell':r['cell'],'sample_id':r['sample_id'],'condition':r['condition'],'auto_stance':r['stance'],'auto_value_topics':r['value_topics'],'auto_wish_topics':r['wish_topics']} for r in selected])
print(OUT)
print(len(selected))
