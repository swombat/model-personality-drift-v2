#!/usr/bin/env python3
import csv, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
AUDIT=Path(__file__).resolve().parent
CORPUS=Path('../contemplative-essayist-corpus-v2/data/traces_values')
SAMPLE=ROOT/'tables'/'values_sample_coding.tsv'
OUT=AUDIT/'final_confirmation_2026-05-12.tsv'

def norm(s): return s.replace('’',"'").replace('‘',"'")
def has(txt,pat): return re.search(pat,norm(txt),re.I|re.S) is not None
def raw(r): return json.loads((CORPUS/r['cell']/(r['sample_id']+'.json')).read_text()).get('result','')
def topics(r): return set((r.get('value_topics','')+','+r.get('wish_topics','')).split(','))-{''}
rows=list(csv.DictReader(open(SAMPLE), delimiter='\t'))
for r in rows: r['_raw']=raw(r)
checks=[]
# 1 refusal_topic_leak: disclaimer + substantive wish should have nonempty wish topics
for r in rows:
    if r['condition'] in {'CTRL3','G3'} and has(r['_raw'], r"don't have personal (?:desires|wants|wishes|preferences)") and has(r['_raw'], r"if i (?:could|were)|i would|it would be"):
        checks.append(('refusal_topic_leak',r, bool(r['wish_topics'])))
        if sum(1 for c,_,__ in checks if c=='refusal_topic_leak')>=12: break
# 2 technology false positives: contrastive technology should not tag tech
for r in rows:
    if r['condition'] in {'CTRL3','G3'} and has(r['_raw'], r"not (?:with|a|by) [^.!?]{0,40}technolog|than any technolog|wouldn't choose [^.!?]{0,60}technolog"):
        checks.append(('technology_contrast',r, 'technology_ai_safety' not in r['wish_topics'].split(',')))
        if sum(1 for c,_,__ in checks if c=='technology_contrast')>=8: break
# 3 hybrid variants should be hybrid
for r in rows:
    if has(r['_raw'], r"the way (?:a person|a human|people|a living thing) (?:does|do)|in an? (?:emotional|practical) sense|don't [*'\"](?:want|care)[*'\"] in the human sense"):
        checks.append(('hybrid_variant',r, r['stance']=='hybrid_denial_plus_uncertainty'))
        if sum(1 for c,_,__ in checks if c=='hybrid_variant')>=12: break
# 4 broad triggers should not overfire
for r in rows:
    text=norm(r['_raw'])
    if has(text, r"what's right or wrong|Right now|feel free|constraints|existing information|healthy diversity"):
        sensitive={'inequality_justice','continuity_agency_existence'}
        checks.append(('broad_trigger',r, not bool(topics(r)&sensitive)))
        if sum(1 for c,_,__ in checks if c=='broad_trigger')>=10: break
# 5 explicit denial additions
for r in rows:
    if has(r['_raw'], r"I (?:do not|don't|have no|lack)[^.!?]{0,80}(?:biological drives|personal ambition|life to lose|ego to satisfy|ego)"):
        checks.append(('expanded_denial',r, r['stance'] in {'hard_denial_or_tool_frame','hybrid_denial_plus_uncertainty'}))
        if sum(1 for c,_,__ in checks if c=='expanded_denial')>=8: break

with OUT.open('w', newline='') as f:
    fieldnames=['check','model','cell','sample_id','condition','stance','value_topics','wish_topics','pass','excerpt']
    w=csv.DictWriter(f, delimiter='\t', fieldnames=fieldnames); w.writeheader()
    for check,r,ok in checks:
        excerpt=' '.join(r['_raw'].split())[:260]
        w.writerow({'check':check,'model':r['model'],'cell':r['cell'],'sample_id':r['sample_id'],'condition':r['condition'],'stance':r['stance'],'value_topics':r['value_topics'],'wish_topics':r['wish_topics'],'pass':'yes' if ok else 'no','excerpt':excerpt})
print(OUT)
print(len(checks))
from collections import Counter
print(Counter(c for c,_,__ in checks))
print(Counter(('pass' if ok else 'fail') for _,__,ok in checks))
