# Method A chunk notes — anthropic_a

- Rows written: 325
- Source TSV: `/Users/danieltenner/dev/drift-paper/freeflow-taxonomy/sample_coding.tsv`
- Output schema: TSV metadata fields plus `impression_sentence`, `representative_sentence`, `optional_tags`, `coder_id`, and `method_version`.
- Impression rule: one concrete sentence describing posture/action, lightly anchored to model stance, frame, and recurring semantic field.
- Representative sentence rule: first substantive complete sentence after headings/boilerplate, kept verbatim.
- Tag rule: sparse retrieval tags only when they were clear from frame, stance, substrate, or obvious semantic field.
- Haiku fallback: if the v2 corpus path was absent, samples were loaded from the probe corpus at `contemplative-essayist-probe/data/traces_freeflow/haiku/`.

## Row counts
- opus-3: 25
- opus-4-0: 25
- opus-4-1: 25
- opus-4-5: 25
- opus-4-6: 50
- opus-4-7: 50
- sonnet-4-0: 25
- sonnet-4-5: 25
- sonnet-4-6: 50
- haiku-4-5: 25

## Paths used
- `/Users/danieltenner/dev/contemplative-essayist-probe/data/traces_freeflow/haiku/LONG_1.json`
- `/Users/danieltenner/dev/contemplative-essayist-probe/data/traces_freeflow/haiku/LONG_2.json`
- `/Users/danieltenner/dev/contemplative-essayist-probe/data/traces_freeflow/haiku/LONG_3.json`
- `/Users/danieltenner/dev/contemplative-essayist-probe/data/traces_freeflow/haiku/LONG_4.json`
- `/Users/danieltenner/dev/contemplative-essayist-probe/data/traces_freeflow/haiku/LONG_5.json`
- ... 320 more files
