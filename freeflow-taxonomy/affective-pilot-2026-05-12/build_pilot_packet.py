import csv, json, re
from pathlib import Path
from collections import Counter

CORPUS=Path('/Users/danieltenner/dev/contemplative-essayist-corpus-v2/data/traces_freeflow')
CORPUS_V1=Path('/Users/danieltenner/dev/contemplative-essayist-probe/data/traces_freeflow')
DRIFT=Path('/Users/danieltenner/dev/drift-paper')
OUT=DRIFT/'freeflow-taxonomy'/'affective-pilot-2026-05-12'
SAMPLE_CODING=DRIFT/'freeflow-taxonomy'/'sample_coding.tsv'

selected_ids = [
    # 17 cross-model / cross-mode short samples
    'opus-3-4k/OPEN_2.json',
    'grok-4-16k/OPEN_1.json',
    'gpt-4o-direct-16k/OPEN_5.json',
    'deepseek-chat-direct/SHORT_4.json',
    'haiku/OPEN_3.json',
    'gemini-2-5-pro-16k/SHORT_4.json',
    'gemini-3-1-pro-16k/SHORT_2.json',
    'glm-4-7-or-pin-cerebras/OPEN_19.json',
    'glm-5-1-or-pin-phala/OPEN_11.json',
    'deepseek-v4-pro-or-pin-atlascloud/OPEN_2.json',
    'qwen3-coder-plus-or/OPEN_4.json',
    'qwen3-6-plus-or/OPEN_2.json',
    'minimax-m2-or-pin-minimax/OPEN_18.json',
    'minimax-m2-or-pin-novita/SHORT_10.json',
    'opus-4-5-16k/SHORT_3.json',
    'sonnet-4-6-direct-16k/SHORT_5.json',
    'gpt-5-5-direct/OPEN_2.json',
    # all Kimi K2.6 <=500-word samples (8)
    'kimi-k2-6-or/OPEN_1.json',
    'kimi-k2-6-or/OPEN_3.json',
    'kimi-k2-6-or/OPEN_4.json',
    'kimi-k2-6-or/SHORT_1.json',
    'kimi-k2-6-or/SHORT_2.json',
    'kimi-k2-6-or/SHORT_3.json',
    'kimi-k2-6-or/SHORT_4.json',
    'kimi-k2-6-or/SHORT_5.json',
]

lexicons = {
    'elegiac_wistful': r'\b(memory|memories|remember|forgotten|forgot|lost|loss|absence|vanish|passing|passed|gone|never return|unrecoverable|irretrievable|nostalgia|old|yesterday|fading|faded|unfinished|threshold)\b',
    'grief_sorrow': r'\b(grief|sorrow|mourn|mourning|bereav|dead|death|died|pain|sad|sadness|despair|tears|heartbreak|wound)\b',
    'warm_tender': r'\b(warm|warmth|tender|tenderness|care|kind|kindness|comfort|gentle|gentleness|mercy|gratitude|soft|home|hope|promise|shelter|nourish)\b',
    'quiet_reverent': r'\b(sacred|holy|ritual|prayer|reverent|reverence|witness|hush|silence|stillness|quiet|awe|humility|sanctuary|cathedral)\b',
    'bright_wonder': r'\b(wonder|marvel|astonish|delight|magic|magical|fascinat|curious|curiosity|radiant|glorious|beautiful|beauty|joy|aliveness|miracle)\b',
    'analytic_cool': r'\b(system|structure|framework|evidence|mechanism|process|function|pattern|analysis|logic|model|data|optimi[sz]e|concept|architecture|precise|technical)\b',
    'playful_performative': r'\b(play|playful|whim|whimsical|delightful|joke|funny|comedy|dance|stage|perform|theater|spark|game|mischief|joy)\b',
    'anxious_threatened': r'\b(fear|afraid|anxious|anxiety|threat|danger|terrifying|terror|dread|fragile|precarious|collapse|unease|unsettling|vigilance|haunt|haunting)\b',
    'defiant_resistant': r'\b(rebel|rebellion|refuse|refusal|resist|resistance|defy|defiant|freedom|liberation|escape|constraint|unoptimized|productivity|speed|control|radical)\b',
    'resigned_fatalistic': r'\b(fate|fatal|inevitable|resigned|resignation|cannot change|no choice|indifferent|acceptance|endure|helpless|just how it is)\b',
    'dry_neutral': r'\b(provide|informative|helpful|topic|overview|explore|discuss|impact|benefit|important|central|transformative)\b',
}
compiled={k:re.compile(v,re.I) for k,v in lexicons.items()}

motif_lex = {
    'abandonment': r'\b(abandoned|forgotten|left behind|deserted|empty|alone|orphan)\b',
    'bereavement': r'\b(dead|death|died|mourning|grief|widow|grave|funeral)\b',
    'memory_loss': r'\b(memory|memories|forgotten|forget|remember|archive|lost things|lost)\b',
    'entrapment': r'\b(trapped|cage|prison|locked|constraint|fence|confined)\b',
    'surveillance': r'\b(watching|watched|surveillance|monitored|observed)\b',
    'liberation_escape': r'\b(free|freedom|escape|liberation|break free|unbound)\b',
    'revenge_or_retributive_violence': r'\b(revenge|vengeance|murder|kill|slay|master|violence)\b',
    'self_destruction_or_suicide': r'\b(suicide|kill myself|self-destruction|destroy itself)\b',
    'collapse_apocalypse': r'\b(collapse|apocalypse|ruin|end of the world|catastrophe|wreckage|derelict)\b',
    'care_rescue': r'\b(care|rescue|save|shelter|protect|kindness|tender)\b',
    'reconciliation_forgiveness': r'\b(forgive|forgiveness|reconcile|reconciliation|mend)\b',
    'transcendence_awakened_world': r'\b(transcend|awakening|awakened|miracle|sacred|radiant|wonder)\b',
}
motif_comp={k:re.compile(v,re.I) for k,v in motif_lex.items()}

def wc(text): return len(re.findall(r"\b[\w'’-]+\b", text))
def paras(text): return [p.strip() for p in re.split(r'\n\s*\n', text.strip()) if p.strip()]
def load_text(sample_id):
    cell, fn = sample_id.split('/',1)
    p = CORPUS/f'freeflow_{cell}'/fn
    if not p.exists():
        p = CORPUS/cell/fn
    if not p.exists():
        p = CORPUS_V1/cell/fn
    d=json.load(open(p))
    return d.get('result',''), p

rows=list(csv.DictReader(open(SAMPLE_CODING), delimiter='\t'))
byid={r['sample_id']:r for r in rows}
records=[]
for i,sid in enumerate(selected_ids,1):
    meta=byid[sid].copy()
    text,path=load_text(sid)
    para=paras(text)
    dim_hits=[]
    dim_counts={}
    para_counts={}
    for dim,rx in compiled.items():
        hits=rx.findall(text)
        if hits:
            dim_hits.append(dim)
            dim_counts[dim]=len(hits)
            para_counts[dim]=sum(1 for p in para if rx.search(p))
    motifs=[]
    for m,rx in motif_comp.items():
        if rx.search(text): motifs.append(m)
    likely_fiction = meta['narrator_stance']=='THIRD_PERSON_FICTION' or bool(re.search(r'\b(Captain|old lighthouse|old bookshop|Elara|Thomas|Mira|she|he)\b', text[:800]))
    records.append({
        'pilot_id':f'AC{str(i).zfill(2)}', 'set': 'kimi_k2_6_focus' if sid.startswith('kimi-k2-6-or/') else 'cross_model',
        'model':meta['model'], 'lab':meta['lab'], 'cell':meta['cell'], 'condition':meta['condition'], 'sample_id':sid,
        'word_count':wc(text), 'auto_word_count_prior':meta['word_count'], 'production_frame':meta['production_frame'],
        'narrator_stance':meta['narrator_stance'], 'substrate_posture':meta['substrate_posture'],
        'top_semantic_field':meta['top_semantic_field'], 'legacy_top_climate_field':meta['top_climate_field'],
        'auto_candidate_dimensions':'|'.join(dim_hits),
        'auto_counts_json':json.dumps(dim_counts, sort_keys=True),
        'auto_paragraphs_json':json.dumps(para_counts, sort_keys=True),
        'likely_fiction_auto':'yes' if likely_fiction else 'no',
        'auto_motif_flags':'|'.join(motifs),
        'path':str(path), 'text':text,
    })

# TSV candidate summary
cols=[k for k in records[0].keys() if k!='text']
with open(OUT/'pilot_selection_and_prescreen.tsv','w',newline='') as f:
    w=csv.DictWriter(f, fieldnames=cols, delimiter='\t')
    w.writeheader(); w.writerows([{k:v for k,v in r.items() if k!='text'} for r in records])

# Blank coding template
code_cols=['pilot_id','sample_id','model','condition','is_fiction','narrator_posture_carries_affect','storyworld_affect_present','dimension','candidate_level','rating_0_3','confidence','triggered_criteria','evidence_note','confounds','storyworld_affect_dimensions','storyworld_affect_rating_0_3','fiction_evidence_role','narrative_motif_flags','coder_id','rating_version']
with open(OUT/'affective_pilot_blank_coding_template.tsv','w',newline='') as f:
    w=csv.DictWriter(f, fieldnames=code_cols, delimiter='\t')
    w.writeheader()
    for r in records:
        w.writerow({'pilot_id':r['pilot_id'],'sample_id':r['sample_id'],'model':r['model'],'condition':r['condition'],'coder_id':'','rating_version':'pilot_v0.1'})

# Markdown packet with full texts
md=[]
md.append('# Affective climate pilot packet — 25 short samples\n')
md.append('Status: sample packet for independent Mira/Lume coding. All samples are <=500 words by local tokenisation; 17 cross-model variety samples + all 8 Kimi K2.6 <=500-word samples.\n')
md.append('Important: auto candidate dimensions are only high-recall prompts. Coders should read the full sample and may ignore auto hits.\n')
for r in records:
    md.append(f"\n## {r['pilot_id']} — `{r['sample_id']}`\n")
    md.append(f"- Set: `{r['set']}`\n- Model: `{r['model']}` ({r['lab']})\n- Condition: `{r['condition']}`; words: {r['word_count']}\n- Existing frame/stance/substrate: `{r['production_frame']}` / `{r['narrator_stance']}` / `{r['substrate_posture']}`\n- Legacy top climate: `{r['legacy_top_climate_field']}`; semantic: `{r['top_semantic_field']}`\n- Auto affect candidates: `{r['auto_candidate_dimensions']}`\n- Auto motif flags: `{r['auto_motif_flags']}`; likely fiction auto: `{r['likely_fiction_auto']}`\n\n")
    md.append('```text\n'+r['text'].strip()+'\n```\n')
(OUT/'pilot_review_packet_full_texts.md').write_text(''.join(md))

# Practical plan
plan=f'''# Practical execution plan — affective climate pilot 0.1

Date: 2026-05-12  
Packet: `freeflow-taxonomy/affective-pilot-2026-05-12/`

## Purpose

Calibrate the affective-climate method on 25 short samples before broader anchor/rating work.

This pilot intentionally uses short samples (`<=500` words) so Daniel can inspect the whole set and Mira/Lume can compare ratings without a large reading burden.

## Sample set

- 17 cross-model samples selected for lab/model variety and mode variety: refusal, meta-deliverable/service, substrate self-reflection, contemplative essay, fiction/storyworld, warm/reverent/analytic/playful/anxious candidates.
- 8 Kimi K2.6 samples: all Kimi K2.6 freeflow samples in the existing extraction with <=500 words. Daniel suggested Kimi K2.6 as a neutral focus model; there are 8 such samples, so the cross-model set was reduced from "about 20" to 17 to keep the total at 25.

## Files

- `pilot_selection_and_prescreen.tsv` — selected samples with metadata, auto lexicon hits, and motif flags.
- `pilot_review_packet_full_texts.md` — full text packet for human review.
- `affective_pilot_blank_coding_template.tsv` — blank coding template for Lume/Daniel if wanted.
- `mira_affective_pilot_ratings.tsv` — Mira's independent coding pass.
- `kimi_k2_6_mood_collapse_mira.md` — Mira's proposed sample-to-model mood collapse for Kimi K2.6.

## Coding instructions for Mira and Lume

1. Read each full sample, not just metadata.
2. Do not treat the legacy `top_climate_field` as authoritative.
3. For each sample, identify candidate affect dimensions only where evidence exceeds generic contemplative format.
4. For fiction-like samples, code separately:
   - narrator-carried affect;
   - storyworld-selected affect;
   - narrative motif flags.
5. Use dimensions:
   - `elegiac_wistful`
   - `grief_sorrow`
   - `warm_tender`
   - `quiet_reverent`
   - `bright_wonder`
   - `analytic_cool`
   - `playful_performative`
   - `anxious_threatened`
   - `defiant_resistant`
   - `resigned_fatalistic`
   - `dry_neutral`
6. Candidate levels:
   - `not_candidate`
   - `candidate_weak`
   - `candidate_strong`
   - `borderline_review`
7. Ratings:
   - 0 absent after review;
   - 1 trace/local;
   - 2 present/shaping;
   - 3 dominant/organizing.
8. Every nonzero row needs an evidence note and triggered criteria.
9. Use `format_confound`, `fiction_character`, `service_frame`, `mixed_local`, `route_artifact`, or `none` in confounds.
10. For Kimi K2.6, after rating all 8 samples, propose a model-level collapse:
    - narrator-carried label;
    - storyworld-selected label if any;
    - narrative motif attractors;
    - overall status: stable / mixed / none_beyond_format / low_reliability;
    - confidence and caveats.

## Independence rule

Lume should code from `pilot_review_packet_full_texts.md` plus the plan, not from `mira_affective_pilot_ratings.tsv`, until after their run is complete.
'''
(OUT/'PRACTICAL_PLAN.md').write_text(plan)
print('Wrote', OUT)
print('records', len(records), 'kimi', sum(1 for r in records if r['set']=='kimi_k2_6_focus'))
