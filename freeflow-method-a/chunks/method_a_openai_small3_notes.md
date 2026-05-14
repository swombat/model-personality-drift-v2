# Method A OpenAI small3 chunk notes

- Wrote 225 JSONL rows for the requested OpenAI models: gpt-5-3 and gpt-5-5.
- Row counts by model: {'gpt-5-3': 75, 'gpt-5-5': 150}
- Row counts by cell: {'gpt-5-3-direct': 25, 'gpt-5-3-direct-r2': 25, 'gpt-5-3-direct-r3': 25, 'gpt-5-5-direct': 25, 'gpt-5-5-direct-r2': 25, 'gpt-5-5-direct-r3': 25, 'gpt-5-5-or': 25, 'gpt-5-5-or-r2': 25, 'gpt-5-5-or-r3': 25}
- Representative sentences are taken verbatim from the first complete body sentence after stripping markdown headings and obvious :::writing / title scaffolding.
- Impression sentences stay one sentence each and stay concrete about posture, action, or reader relation rather than using affect buckets.
- Optional tags are sparse retrieval aids: stance tags are included consistently, with a few content tags where the semantic field is especially clear.
- Source metadata comes from `freeflow-taxonomy/sample_coding.tsv`; full text comes from the matching JSON trace under `contemplative-essayist-corpus-v2/data/traces_freeflow/`.
