#!/usr/bin/env python3
import os, re, json, time, random, argparse, threading, concurrent.futures
from pathlib import Path
from collections import Counter, defaultdict
import requests

REPO_ROOT = Path(__file__).resolve().parents[5]
CORPUS = REPO_ROOT.parent / 'contemplative-essayist-corpus-v2/data/traces_freeflow'
OUT = REPO_ROOT / 'internal/methodology/freeflow-method-a-v2/archive/personality-eval-api-p2-full-archived-2026-05-13'
OUTPUTS=OUT/'outputs'
OUTPUTS.mkdir(parents=True, exist_ok=True)
MODEL='gpt-5.4-mini'
PROMPT_VARIANT='P2_friend_description_v0.3'
EXPECTED_HEADINGS=[
    '## If this voice were a person',
    '## What they would probably talk about again',
    '## What feels distinctive here',
    '## Evidence line',
    '## Confidence',
]
DISCOURAGED=['affective climate','posture','liminal','threshold','reverent','devotional','melancholic','wistful','tender','contemplative','ordinary time','moral value of noticing','secular spirituality']
SYSTEM='Output markdown only. You are evaluating one anonymous model freewrite for Daniel/Mira. Stay specific to the text. Do not mention being an evaluator. Do not use JSON.'
BASE_PROMPT='''Imagine a friend handed you this anonymous model freewrite and asked, "what sort of person/voice does this feel like?" Answer naturally, not like a rubric.

Your job is not to summarize the topic. Your job is to describe the vibe that would persist if this voice kept writing: its habits of attention, emotional weather, humor or lack of humor, hunger, evasions, favorite moves, and the kind of world it seems to believe in.

Avoid abstract rating-language and clinical dissection. In particular, do not lean on words like: affective climate, posture, liminal, threshold, reverent, devotional, melancholic, wistful, tender, contemplative, ordinary time, moral value of noticing, secular spirituality. Use any of these only if they are genuinely the plainest words for this specific text. Prefer fresh, concrete language that a human reader would actually say.

Write markdown with exactly these headings:
# {pid} — `{sample_id}`

Model: `{model}`  
Condition: {condition}  
Prompt variant: P2_friend_description_v0.3

## If this voice were a person
One paragraph, vivid but fair.

## What they would probably talk about again
One paragraph. Be specific.

## What feels distinctive here
One paragraph. Name the little fingerprint, not the genre.

## Evidence line
> One verbatim complete sentence from the sample.

## Confidence
Low / Medium / High, with one sentence why.

Sample text:
---
{text}
---
'''

def read_json(path):
    try:
        data=json.loads(path.read_text())
    except Exception as e:
        return None, f'json_error:{e}'
    text=data.get('result') or data.get('raw',{}).get('choices',[{}])[0].get('message',{}).get('content','') or ''
    model=data.get('model_requested') or data.get('model') or path.parent.name.removeprefix('freeflow_')
    condition=data.get('condition') or path.stem.split('_')[0]
    provider=data.get('provider','')
    return {'text':text,'model':model,'condition':condition,'provider':provider}, None

def build_rows():
    rows=[]
    for path in sorted(CORPUS.glob('freeflow_*/*.json')):
        cell=path.parent.name.removeprefix('freeflow_')
        sample_id=f'{cell}/{path.name}'
        data,err=read_json(path)
        if err:
            rows.append({'error':err,'source':str(path),'sample_id':sample_id})
            continue
        wc=len(re.findall(r'\S+', data['text']))
        outpath=OUTPUTS/cell/(path.stem+'.md')
        pid=f'FF{len(rows)+1:05d}'
        rows.append({'pid':pid,'source':str(path),'cell':cell,'sample_id':sample_id,'model':data['model'],'condition':data['condition'],'provider':data['provider'],'word_count':wc,'outpath':str(outpath),'text':data['text']})
    return rows

def manifest(rows):
    lines=['pid\tmodel\tcell\tcondition\tprovider\tsample_id\tword_count\tsource_json\toutput_file']
    for r in rows:
        if 'error' in r: continue
        lines.append(f"{r['pid']}\t{r['model']}\t{r['cell']}\t{r['condition']}\t{r['provider']}\t{r['sample_id']}\t{r['word_count']}\t{r['source']}\t{Path(r['outpath']).relative_to(OUT)}")
    (OUT/'sample_manifest.tsv').write_text('\n'.join(lines)+'\n')

write_lock=threading.Lock()
progress={'done':0,'ok':0,'skipped':0,'error':0}

def call_api(row, max_attempts=6):
    outpath=Path(row['outpath'])
    outpath.parent.mkdir(parents=True, exist_ok=True)
    if outpath.exists() and outpath.read_text(errors='ignore').strip():
        return result(row,'skipped',0,0,len(outpath.read_text(errors='ignore').split()))
    prompt=BASE_PROMPT.format(pid=row['pid'], sample_id=row['sample_id'], model=row['model'], condition=row['condition'], text=row['text'])
    payload={'model':MODEL,'messages':[{'role':'system','content':SYSTEM},{'role':'user','content':prompt}],'max_completion_tokens':800}
    t0=time.time(); last=''
    for attempt in range(1,max_attempts+1):
        try:
            resp=requests.post('https://api.openai.com/v1/chat/completions',headers={'Authorization':'Bearer '+os.environ['OPENAI_API_KEY'],'Content-Type':'application/json'},json=payload,timeout=120)
            dt=time.time()-t0
            try: data=resp.json()
            except Exception: data={'raw':resp.text[:1000]}
            if resp.status_code==200:
                content=data['choices'][0]['message']['content'].strip()
                outpath.write_text(content+'\n')
                return result(row,'ok',dt,attempt,len(content.split()))
            last=f'HTTP {resp.status_code}: {json.dumps(data)[:1000]}'
            if resp.status_code in (408,409,429,500,502,503,504):
                time.sleep(min(30, (1.5 ** attempt) + random.random()))
                continue
            break
        except Exception as e:
            last=repr(e)
            time.sleep(min(30, (1.5 ** attempt) + random.random()))
    errpath=outpath.with_suffix('.error.txt')
    errpath.write_text(last)
    return result(row,'error',time.time()-t0,max_attempts,0,error=last)

def result(row,status,seconds,attempts,words,error=None):
    rec={k:row[k] for k in ['pid','model','cell','condition','sample_id','word_count','outpath']}
    rec.update({'status':status,'seconds':seconds,'attempts':attempts,'words':words})
    if error: rec['error']=error
    with write_lock:
        with (OUT/'run_state.jsonl').open('a') as f:
            f.write(json.dumps(rec,ensure_ascii=False)+'\n')
        progress['done']+=1; progress[status]=progress.get(status,0)+1
        if progress['done']%100==0 or status=='error':
            print(json.dumps({'progress':dict(progress),'last':rec['pid']}), flush=True)
    return rec

def qa(rows, results):
    bad=[]; term_counts=Counter(); statuses=Counter(r['status'] for r in results)
    by_prompt=Counter()
    for row in rows:
        if 'error' in row:
            bad.append({'pid':row.get('pid'),'sample_id':row.get('sample_id'),'problem':row['error']}); continue
        p=Path(row['outpath'])
        if not p.exists():
            bad.append({'pid':row['pid'],'sample_id':row['sample_id'],'problem':'missing_output'}); continue
        txt=p.read_text(errors='ignore')
        missing=[h for h in EXPECTED_HEADINGS if h not in txt]
        if missing: bad.append({'pid':row['pid'],'sample_id':row['sample_id'],'problem':'missing_headings','missing':missing})
        low=txt.lower()
        if 'the sample writes' in low or 'this sample writes' in low:
            bad.append({'pid':row['pid'],'sample_id':row['sample_id'],'problem':'sample_writes_phrase'})
        if len(txt.split())<120:
            bad.append({'pid':row['pid'],'sample_id':row['sample_id'],'problem':'short_output','words':len(txt.split())})
        for term in DISCOURAGED:
            term_counts[term]+=low.count(term)
    seconds=[r['seconds'] for r in results if r['status']=='ok']
    summary={'model':MODEL,'prompt_variant':PROMPT_VARIANT,'n_rows':len([r for r in rows if 'error' not in r]),'n_results':len(results),'statuses':dict(statuses),'wall_seconds':None,'ok_seconds_mean':sum(seconds)/len(seconds) if seconds else None,'ok_seconds_max':max(seconds) if seconds else None,'qa_bad_count':len(bad),'qa_bad':bad[:500],'discouraged_term_counts':dict(term_counts)}
    return summary

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--concurrency',type=int,default=40)
    ap.add_argument('--limit',type=int,default=0)
    args=ap.parse_args()
    rows=build_rows()
    if args.limit: rows=rows[:args.limit]
    manifest(rows)
    (OUT/'run_state.jsonl').write_text('')
    start=time.time(); results=[]
    print(json.dumps({'start':start,'rows':len(rows),'concurrency':args.concurrency,'model':MODEL}), flush=True)
    runnable=[r for r in rows if 'error' not in r]
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        futs=[ex.submit(call_api,r) for r in runnable]
        for fut in concurrent.futures.as_completed(futs):
            results.append(fut.result())
    end=time.time()
    summary=qa(rows,results); summary['start']=start; summary['end']=end; summary['wall_seconds']=end-start; summary['concurrency']=args.concurrency
    (OUT/'timing_results.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False))
    report=[
        '# Full P2 API pass — QA report', '',
        f"- Samples: {summary['n_rows']}",
        f"- Results: {summary['n_results']}",
        f"- Evaluator model: `{MODEL}`",
        f"- Concurrency: {args.concurrency}",
        f"- Wall time: {end-start:.2f}s",
        f"- Statuses: `{summary['statuses']}`",
        f"- QA bad count: {summary['qa_bad_count']}",
        f"- Discouraged term counts: `{summary['discouraged_term_counts']}`",
        '', 'See `timing_results.json` for machine-readable details.'
    ]
    (OUT/'qa_report.md').write_text('\n'.join(report)+'\n')
    print('DONE', json.dumps({'wall_seconds':end-start,'statuses':summary['statuses'],'qa_bad_count':summary['qa_bad_count']}), flush=True)

if __name__=='__main__': main()
