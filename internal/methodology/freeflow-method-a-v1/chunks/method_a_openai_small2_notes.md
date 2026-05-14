# Method A OpenAI small chunk notes

- Wrote 225 JSONL rows for gpt-5, gpt-5-1, and gpt-5-2 only.
- Source metadata came from `freeflow-taxonomy/sample_coding.tsv`; full sample text was loaded from `contemplative-essayist-corpus-v2/data/traces_freeflow/freeflow_<cell>/<file>`.
- Representative sentences use the first substantial complete sentence after stripping headings and blank lines.
- Impression sentences are one sentence each, concrete, and keyed to the opening clause plus model metadata.
- Optional tags are sparse retrieval aids, not a full taxonomy pass.
- Row counts by model: {'gpt-5': 75, 'gpt-5-1': 75, 'gpt-5-2': 75}
