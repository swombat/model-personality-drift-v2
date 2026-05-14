import json,re,csv
from pathlib import Path
ROOT=Path('/Users/danieltenner/dev/drift-paper')
CORP=Path('/Users/danieltenner/dev/contemplative-essayist-corpus-v2/data/traces_freeflow')
CORP1=Path('/Users/danieltenner/dev/contemplative-essayist-probe/data/traces_freeflow')

def norm(s): return ' '.join((s or '').split())
def load(r):
    p=CORP/('freeflow_'+r['cell'])/r['file']
    if not p.exists(): p=CORP/r['cell']/r['file']
    if not p.exists(): p=CORP1/r['cell']/r['file']
    return json.load(open(p))['result']
def candidates(text):
    # exact-ish sentence chunks from raw, preserving markdown but no newlines inside
    chunks=re.split(r'(?<=[.!?])\s+(?=[A-Z0-9"“#*])|\n{2,}', text.strip())
    out=[]
    for c in chunks:
        c=' '.join(c.strip().split())
        if 6 <= len(c.split()) <= 55 and re.search(r'[.!?]$', c):
            out.append(c)
    return out
def choose(text):
    cands=candidates(text)
    if not cands:
        # fallback exact first 35 words of text (not ideal, but non-empty representative)
        return ' '.join(text.strip().split()[:35])
    stop=re.compile(r'^(sure|of course|here|below|i hope|i think i’ll start|write freely about whatever)',re.I)
    key=re.compile(r'\b(threshold|memory|ordinary|attention|care|quiet|silence|wonder|future|present|life|world|human|model|question|story|time|light|dawn|meaning)\b',re.I)
    best=cands[0]; score=-999
    for i,c in enumerate(cands):
        s=len(key.findall(c))*2 + (3 if 12<=len(c.split())<=35 else 0) + (i/len(cands))
        if stop.match(c): s-=5
        if s>score: best=c; score=s
    return best
rows=[json.loads(l) for l in open(ROOT/'freeflow-method-a/sample_impressions.jsonl')]
changed=0
for r in rows:
    txt=load(r); rep=norm(r.get('representative_sentence',''))
    if (not rep) or rep not in norm(txt):
        r['representative_sentence']=choose(txt); changed+=1
# write jsonl
with open(ROOT/'freeflow-method-a/sample_impressions.jsonl','w') as f:
    for r in rows: f.write(json.dumps(r,ensure_ascii=False)+'\n')
# write tsv mirror
cols=['model','lab','cell','file','condition','sample_id','word_count','production_frame','narrator_stance','substrate_posture','top_semantic_field','top_climate_field','impression_sentence','representative_sentence','optional_tags','coder_id','method_version']
with open(ROOT/'freeflow-method-a/sample_impressions.tsv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols,delimiter='\t',extrasaction='ignore'); w.writeheader()
    for r in rows:
        rr=dict(r); rr['optional_tags']='|'.join(rr.get('optional_tags') or [])
        w.writerow(rr)
print('changed',changed)
