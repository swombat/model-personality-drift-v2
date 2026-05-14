# Method A QA notes

Date: 2026-05-13

## Completion

The Method A extraction is complete for all rows in `freeflow-taxonomy/sample_coding.tsv`.

- Expected rows: 10,620
- Merged rows: 10,620
- Missing sample IDs: 0
- Extra sample IDs: 0
- Duplicate sample IDs: 0
- JSON parse errors: 0
- Representative sentence validation: 0 non-verbatim / empty after repair

See:

- `MERGE_QA.md`
- `REPRESENTATIVE_QA.md`

## Important caveat: optional tags are secondary

The `optional_tags` field is useful for retrieval, but should not be treated as paper-grade coding.

Known issue:

- The locally repaired OpenAI chunk uses heuristic tag detection and over-fires `tech_substrate` on some OpenAI rows, especially where the topic is AI or the text contains generic AI vocabulary. This does **not** affect the core Method A outputs (`impression_sentence` and `representative_sentence`), but it means model-card top-tag summaries are less trustworthy for the OpenAI models until tags are cleaned.

Recommendation:

- Treat `impression_sentence` + `representative_sentence` as primary.
- Treat objective fields from the original taxonomy (`production_frame`, `narrator_stance`, `substrate_posture`) as secondary.
- Treat `optional_tags` as rough retrieval aids only.

## Subagent quality variation

Different chunks were produced by different agents plus one local OpenAI repair. The extraction is coherent enough for first-pass review, but a later polish pass could improve consistency of impression style, especially:

- OpenAI local repair impressions are heuristic and more formulaic than ideal.
- Some large routed-model chunks may under-describe route variance at the per-row level.
- The per-model cards are auto-generated summaries, not final prose portraits.

## What is ready now

Ready for review/use:

- `sample_impressions.jsonl`
- `sample_impressions.tsv`
- `MODEL_INDEX.md`
- `per-model/*.md`

Not final-paper-grade yet:

- optional tag frequencies;
- auto one-line scaffolds in per-model cards;
- any broad personality claim generated only from counts without human synthesis.
