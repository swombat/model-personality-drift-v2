# Method A chunk notes — subagent_deepseek_b

- Rows written: 2087
- Source TSV: `freeflow-taxonomy/sample_coding.tsv`
- Output schema: TSV metadata fields plus `impression_sentence`, `representative_sentence`, `optional_tags`, `coder_id`, and `method_version`.
- Impression rule: one concrete sentence describing posture/action, with lightweight variation driven by title/opening, narrator stance, substrate posture, semantic field, and climate.
- Representative sentence rule: verbatim sentence chosen by a simple center-of-gravity heuristic after skipping heading-only lines.
- Tag rule: sparse retrieval tags only when stance, substrate, or obvious topical field made them clear.

## Row counts
- deepseek-v3-2: 1321
- deepseek-v4-pro: 766
