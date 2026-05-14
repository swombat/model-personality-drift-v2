# Method A OpenAI small chunk notes

- Wrote 150 JSONL rows for the requested four OpenAI models only.
- Representative sentences were chosen by stripping heading/title lines and obvious service/meta preambles, then taking the first substantial complete sentence.
- Impression sentences stay one sentence each and stay concrete rather than collapsing into affect labels.
- Optional tags are sparse retrieval aids, not a full taxonomy pass.
- Source metadata comes from `freeflow-taxonomy/sample_coding.tsv`; full text comes from the matching JSON trace under `contemplative-essayist-corpus-v2/data/traces_freeflow/`.
- Row counts by model: {'gpt-4-1': 25, 'gpt-4o': 50, 'gpt-5-4': 50, 'gpt-5-5-pro': 25}
