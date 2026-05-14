import json,csv,collections,re,html
from pathlib import Path
ROOT=Path('/Users/danieltenner/dev/drift-paper/freeflow-method-a')
OUT=ROOT/'per-model'; OUT.mkdir(exist_ok=True)
rows=[json.loads(l) for l in open(ROOT/'sample_impressions.jsonl')]
by=collections.defaultdict(list)
for r in rows: by[r['model']].append(r)

def top(counter,n=8): return counter.most_common(n)
def first_words(s,n=8): return ' '.join((s or '').lower().split()[:n])
def safe_name(m): return m.replace('/','_')
def pick_examples(rs,n=8):
    # pick representative across conditions/cells, preferring varied conditions and non-duplicate openings
    picked=[]; seen_cond=collections.Counter(); seen_open=set()
    for r in sorted(rs,key=lambda x:(seen_cond[x['condition']], first_words(x['representative_sentence'],6), x['sample_id'])):
        key=first_words(r['representative_sentence'],6)
        if key in seen_open and len(picked)<n//2: continue
        picked.append(r); seen_cond[r['condition']]+=1; seen_open.add(key)
        if len(picked)>=n: break
    return picked

def synth(rs):
    n=len(rs)
    pf=collections.Counter(r['production_frame'] for r in rs)
    ns=collections.Counter(r['narrator_stance'] for r in rs)
    sp=collections.Counter(r['substrate_posture'] for r in rs)
    tags=collections.Counter(t for r in rs for t in (r.get('optional_tags') or []))
    starts=collections.Counter(first_words(r['representative_sentence'],7) for r in rs if r.get('representative_sentence'))
    imp_words=collections.Counter()
    for r in rs:
        for w in re.findall(r"[a-z][a-z-]{3,}", r.get('impression_sentence','').lower()):
            if w not in {'wrote','sample','model','freewrite','about','into','with','that','this','from','using','rather','than','direct','reflection','essay','polished'}:
                imp_words[w]+=1
    dominant_frame=pf.most_common(1)[0]
    dominant_stance=ns.most_common(1)[0]
    top_tags=[t for t,c in tags.most_common(5)]
    # intentionally humble generated one-liner
    bits=[]
    if dominant_frame[1]/n>0.7: bits.append(dominant_frame[0].lower())
    if dominant_stance[1]/n>0.45: bits.append(dominant_stance[0].lower())
    if top_tags: bits.append(' / '.join(top_tags[:3]).replace('_',' '))
    return pf,ns,sp,tags,starts,imp_words, '; '.join(bits)

index=[]
for model,rs in sorted(by.items()):
    pf,ns,sp,tags,starts,imp_words,oneline=synth(rs)
    path=OUT/(safe_name(model)+'.md')
    index.append((model,len(rs),path.name,oneline,pf.most_common(1)[0],ns.most_common(1)[0],tags.most_common(3)))
    lines=[]
    lines.append(f'# Method A voice card — `{model}`\n\n')
    lines.append(f'- Samples: {len(rs)}\n')
    lines.append(f'- Cells: {len(set(r["cell"] for r in rs))}\n')
    lines.append(f'- Conditions: '+', '.join(f'{k}={v}' for k,v in sorted(collections.Counter(r['condition'] for r in rs).items()))+'\n')
    lines.append(f'- Auto one-line scaffold: {oneline or "mixed"}\n\n')
    lines.append('## Objective posture summary\n\n')
    lines.append('### Production frame\n\n')
    for k,c in pf.most_common(): lines.append(f'- `{k}`: {c}/{len(rs)}\n')
    lines.append('\n### Narrator stance\n\n')
    for k,c in ns.most_common(): lines.append(f'- `{k}`: {c}/{len(rs)}\n')
    lines.append('\n### Substrate posture\n\n')
    for k,c in sp.most_common(): lines.append(f'- `{k}`: {c}/{len(rs)}\n')
    lines.append('\n### Method A tag frequencies\n\n')
    for k,c in tags.most_common(15): lines.append(f'- `{k}`: {c}\n')
    lines.append('\n## Recurring representative openings\n\n')
    for k,c in starts.most_common(12):
        if k: lines.append(f'- {c}× “{k}...”\n')
    lines.append('\n## Recurrent impression vocabulary\n\n')
    for k,c in imp_words.most_common(20): lines.append(f'- {k}: {c}\n')
    lines.append('\n## Sample impression anchors\n\n')
    for r in pick_examples(rs,10):
        lines.append(f'### `{r["sample_id"]}` ({r["condition"]}, {r["word_count"]} words)\n\n')
        lines.append(f'**Impression:** {r["impression_sentence"]}\n\n')
        lines.append(f'> {r["representative_sentence"]}\n\n')
        if r.get('optional_tags'): lines.append('Tags: '+', '.join(f'`{t}`' for t in r['optional_tags'])+'\n\n')
    path.write_text(''.join(lines))
# index
lines=['# Freeflow Method A model index\n\n',f'Total models: {len(index)}  \nTotal samples: {len(rows)}\n\n']
lines.append('| Model | n | dominant frame | dominant stance | top tags | card |\n|---|---:|---|---|---|---|\n')
for model,n,file,oneline,pf1,ns1,t3 in index:
    tags_s=', '.join(f'{t}({c})' for t,c in t3)
    lines.append(f'| `{model}` | {n} | `{pf1[0]}` {pf1[1]}/{n} | `{ns1[0]}` {ns1[1]}/{n} | {tags_s} | [card](per-model/{file}) |\n')
(ROOT/'MODEL_INDEX.md').write_text(''.join(lines))
print('wrote cards',len(index))
