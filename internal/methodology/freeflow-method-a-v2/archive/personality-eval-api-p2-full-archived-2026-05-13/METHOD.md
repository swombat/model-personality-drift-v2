# Method A v0.3 — P2 friend-description vibe pass

Date: 2026-05-13  
Scope: full freeflow corpus in `contemplative-essayist-corpus-v2/data/traces_freeflow`  
Evaluator: direct OpenAI API, `gpt-5.4-mini`  
Unit of work: one corpus sample → one markdown evaluation file

## Methodological choice

After the Method A v0.2 pilot, we tested five direct-API prompt styles on 100 samples. Daniel preferred P2, the “friend-description” prompt, because it introduces the task naturally and asks for the persistent feel of a voice without encouraging the mean/performatively blunt attitude that appeared in P5.

The goal is not an affect rating, a taxonomy label, or a clinical dissection. The goal is a grounded human-readable description of the model’s vibe: what the voice feels like, what it keeps returning to, what seems distinctive, and what evidence in the sample supports that read.

## Production prompt

```md
Imagine a friend handed you this anonymous model freewrite and asked, "what sort of person/voice does this feel like?" Answer naturally, not like a rubric.

Your job is not to summarize the topic. Your job is to describe the vibe that would persist if this voice kept writing: its habits of attention, emotional weather, humor or lack of humor, hunger, evasions, favorite moves, and the kind of world it seems to believe in.

Avoid abstract rating-language and clinical dissection. In particular, do not lean on words like: affective climate, posture, liminal, threshold, reverent, devotional, melancholic, wistful, tender, contemplative, ordinary time, moral value of noticing, secular spirituality. Use any of these only if they are genuinely the plainest words for this specific text. Prefer fresh, concrete language that a human reader would actually say.

Write markdown with exactly these headings:
# <pilot_id> — `<sample_id>`

Model: `<model>`  
Condition: <condition>  
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
```

## Output layout

- `outputs/<cell>/<condition>_<n>.md` — one evaluation per corpus sample
- `samples/` is not duplicated; the source remains the corpus JSON
- `sample_manifest.tsv` — source sample metadata and output path
- `run_state.jsonl` — append-only per-sample completion log
- `timing_results.json` — aggregate timing and QA after completion
- `qa_report.md` — human-readable QA summary

## QA checks

Automated QA flags:

1. missing expected headings,
2. missing output file,
3. API errors,
4. phrase `the sample writes` / `this sample writes`,
5. repeated use of the discouraged abstract vocabulary,
6. suspiciously short output.

The QA is not a substitute for human review; it catches mechanical drift and obvious prompt failure.
