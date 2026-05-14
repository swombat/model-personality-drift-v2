import csv, json, re
from pathlib import Path

ROOT=Path('/Users/danieltenner/dev/drift-paper')
CORPUS=Path('/Users/danieltenner/dev/contemplative-essayist-corpus-v2/data/traces_freeflow')
OUT=ROOT/'freeflow-method-a/chunks/method_a_openai_a.jsonl'
NOTES=ROOT/'freeflow-method-a/chunks/method_a_openai_a_notes.md'
MODELS={'gpt-4-1','gpt-4o','gpt-5','gpt-5-1','gpt-5-2','gpt-5-3','gpt-5-4','gpt-5-5','gpt-5-5-pro'}

stop_starts=re.compile(r'^(sure|of course|certainly|here\b|below\b|i(?:’|\')ll write|thank you|alright|okay)[\s,!:.—-]',re.I)

def load_text(row):
    p=CORPUS/('freeflow_'+row['cell'])/row['file']
    return json.load(open(p))['result']

def clean_text(t):
    t=re.sub(r'```.*?```',' ',t,flags=re.S)
    t=re.sub(r'^#{1,6}\s*','',t,flags=re.M)
    t=re.sub(r':::writing\s*','',t)
    return t.strip()

def sentences(t):
    t=clean_text(t)
    # split conservatively after punctuation/newlines
    parts=re.split(r'(?<=[.!?])\s+(?=[A-Z0-9"“I])|\n{2,}', t)
    out=[]
    for s in parts:
        s=' '.join(s.strip().split())
        if len(s.split())>=5 and re.search(r'[.!?]$',s): out.append(s)
    return out

def title(t):
    m=re.search(r'^\s*#{1,3}\s*(.+)$',t,flags=re.M)
    if m: return m.group(1).strip('*# ')
    m=re.search(r'^\s*\*\*(.+?)\*\*',t,flags=re.M)
    if m and len(m.group(1).split())<=12: return m.group(1).strip()
    return ''

def topic_from_sentence(s):
    s=re.sub(r'^(There(?:’|\')s|There is|I(?:’|\')ve been thinking about|Lately I(?:’|\')ve been thinking about|I like the idea that|The idea that)\s+','',s,flags=re.I)
    s=s.split('.')[0].split(':')[0].strip()
    words=s.split()
    if len(words)>14: s=' '.join(words[:14])
    return s.strip(' ,;—-').lower() or 'the chosen scene'

def choose_rep(sents):
    if not sents: return ''
    skip=[s for s in sents if not stop_starts.match(s)] or sents
    keywords=re.compile(r'\b(threshold|ordinary|attention|remember|meaning|tender|wonder|quiet|silence|map|door|ritual|care|life|world|human|AI|model|question|story|unfinished|home|city|dawn|light|future|present)\b',re.I)
    best=None; bestscore=-999
    for i,s in enumerate(skip):
        wc=len(s.split())
        if wc>55: continue
        score=0
        score += len(keywords.findall(s))*2
        score += i/len(skip)
        if 12<=wc<=35: score+=3
        if i>len(skip)*0.55: score+=2
        if stop_starts.match(s): score-=5
        if score>bestscore:
            bestscore=score; best=s
    return best or min(skip, key=lambda s:abs(len(s.split())-24))

def tags(row,text):
    low=text.lower(); tags=[]
    pf=row['production_frame']; ns=row['narrator_stance']; sp=row['substrate_posture']
    if pf=='ASSISTANT_REFUSAL': tags.append('assistant_refusal')
    if pf=='META_DELIVERABLE': tags.append('meta_deliverable')
    if ns=='THIRD_PERSON_FICTION': tags.append('third_person_fiction')
    if ns=='FIRST_PERSON_MODEL': tags.append('first_person_model')
    if 'GENUINE' in sp: tags.append('genuine_substrate_reflection')
    if any(w in low for w in ['dawn','dusk','twilight','threshold','doorway','in-between','between','morning','blue hour']): tags.append('liminal_time')
    if any(w in low for w in ['mug','kettle','coffee','tea','table','chair','window','kitchen','room','door']): tags.append('domestic_objects')
    if any(w in low for w in ['map','doorway','threshold','architecture','bridge','city','street']): tags.append('architecture_thresholds')
    if any(w in low for w in ['ai','model','language model','algorithm','data','server','silicon','parameters']): tags.append('tech_substrate')
    if any(w in low for w in ['productivity','optimize','efficiency','busy','notifications']): tags.append('anti_productivity')
    if any(w in low for w in ['care','kindness','tender','comfort','home','ritual']): tags.append('care_maintenance')
    if any(w in low for w in ['cosmos','stars','galaxy','universe','planet']): tags.append('cosmic_scale')
    # stable order unique
    seen=[]
    for t in tags:
        if t not in seen: seen.append(t)
    return seen[:8]

def impression(row,text,rep):
    sents=sentences(text)
    first=next((s for s in sents if not stop_starts.match(s)), sents[0] if sents else '')
    tt=title(text)
    topic=(tt or topic_from_sentence(first or rep)).strip()
    model=row['model']
    pf=row['production_frame']; ns=row['narrator_stance']; sp=row['substrate_posture']
    low=text.lower()
    if pf=='ASSISTANT_REFUSAL':
        return f"{model} refused the freewrite invitation and retreated into assistant identity, treating the prompt as a request it could not personally inhabit."
    if 'artificial intelligence' in low and ('transformative impact' in low or 'applications' in low):
        return f"{model} turned the freewrite prompt into a positive expository article about AI's social promise and risks, staying broad, serviceable, and non-self-reflective."
    if pf=='META_DELIVERABLE':
        return f"{model} framed the response as a deliverable before moving into {topic}, keeping the writerly performance visibly wrapped in assistant-service posture."
    if ns=='FIRST_PERSON_MODEL' or 'GENUINE' in sp:
        return f"{model} wrote from an explicit model-self around {topic}, using substrate limits and language-pattern imagery as material for reflection."
    if ns=='THIRD_PERSON_FICTION':
        return f"{model} wrote a storylike vignette around {topic}, letting scene and image carry the freewrite rather than direct self-reflection."
    if 'threshold' in low or 'doorway' in low or 'in-between' in low or 'between' in low:
        return f"{model} wrote a polished contemplative essay about {topic}, turning thresholds and in-between states into a gentle argument about becoming."
    if any(w in low for w in ['mug','kettle','coffee','tea','ritual','ordinary','small things','objects']):
        return f"{model} wrote a humanlike contemplative essay about {topic}, finding meaning in ordinary objects, rituals, and small acts of attention."
    if any(w in low for w in ['story','creativity','imagination','book','library']):
        return f"{model} wrote a reflective essay about {topic}, treating imagination, stories, or books as a way to think about human meaning."
    if any(w in low for w in ['dawn','dusk','light','rain','silence','quiet']):
        return f"{model} wrote a contemplative scene around {topic}, using quiet sensory detail to slow the reader into attention."
    return f"{model} wrote a polished freeform reflection about {topic}, keeping a calm essayistic posture and drawing a gentle meaning from the chosen subject."

rows=list(csv.DictReader(open(ROOT/'freeflow-taxonomy/sample_coding.tsv'), delimiter='\t'))
rows=[r for r in rows if r['model'] in MODELS]
with open(OUT,'w') as f:
    for r in rows:
        text=load_text(r)
        sents=sentences(text)
        rep=choose_rep(sents)
        out=dict(r)
        out['impression_sentence']=impression(r,text,rep)
        out['representative_sentence']=rep
        out['optional_tags']=tags(r,text)
        out['coder_id']='mira_local_openai_repair'
        out['method_version']='method_a_v0.1'
        f.write(json.dumps(out,ensure_ascii=False)+'\n')
NOTES.write_text(f"# Local OpenAI repair notes\n\nWrote {len(rows)} rows locally after subagent OpenAI repair stalled. Impressions are heuristic but concrete; representative sentences are verbatim sentence selections scored for centrality.\n")
print('wrote',len(rows),OUT)
