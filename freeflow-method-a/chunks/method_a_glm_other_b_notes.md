# Method A GLM/Z.ai chunk notes

- Wrote 2500 JSONL rows for the requested five GLM/Z.ai models only.
- Each row copies the full sample_coding metadata, then adds impression_sentence, representative_sentence, optional_tags, coder_id, and method_version.
- Representative sentences were selected from the body text after stripping headings or title-only first lines, preferring the most substantial complete sentence near the opening that carried the sample’s center of gravity.
- Impression sentences were generated as one-sentence concrete posture summaries, varying by title/opening anchor, narrator stance, production frame, and semantic field to avoid a single repeated template.
- Optional tags are sparse retrieval aids, capped at two per row.
- Row counts by model: {'glm-4-5': 275, 'glm-4-6': 775, 'glm-4-6-coding': 25, 'glm-4-7': 1400, 'glm-5-1-coding': 25}
