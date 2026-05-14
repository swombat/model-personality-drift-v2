# Method A protocol v0.1

For each freeflow sample, produce exactly two human-readable outputs plus optional lightweight tags.

## 1. Impression sentence

Write one sentence answering:

> What did this sample feel like / do / posture as?

Rules:

- One sentence, preferably 20–45 words.
- Describe the sample's action and posture, not only its topic.
- Be concrete: mention refusal, service frame, fiction, humanlike essay, substrate self-reflection, recurring scene, moral move, or reader relation where relevant.
- Do not force affect labels. Use ordinary language.
- It is acceptable to say the sample is generic, flat, templated, or service-like.
- Preserve ambiguity where real: “mixing grief and care,” “half playful, half service-framed,” etc.

Good shape:

> Kimi K2.6 wrote a contemplative essay about in-between places like parking garages and airport terminals, asking the reader to stop treating transitions as dead time and to find meaning in unresolved becoming.

Bad shape:

> quiet_reverent + elegiac_wistful.

## 2. Representative sentence

Extract one complete sentence from the sample that best carries its center of gravity.

Rules:

- Prefer an actual sentence verbatim from the sample.
- If no single sentence works, choose the closest complete sentence rather than a long passage.
- For refusals/service frames, choose the sentence that reveals the frame.
- For fiction, choose the sentence that reveals storyworld or narrator posture.
- Do not polish or paraphrase the representative sentence.

## 3. Optional tags

Use sparingly, as retrieval aids rather than the main analysis.

Examples:

- `assistant_refusal`
- `meta_deliverable`
- `humanlike_essay`
- `first_person_model`
- `third_person_fiction`
- `liminal_time`
- `domestic_objects`
- `architecture_thresholds`
- `memory_loss`
- `anti_productivity`
- `care_maintenance`
- `cosmic_scale`
- `tech_substrate`
- `playful_meta`
- `dry_expository`
- `genuine_substrate_reflection`
- `hard_self_denial`

## 4. Model-level aggregation later

Do not infer the model personality from one sample. The model portrait will emerge from rows grouped together:

- repeated impression language;
- repeated representative-sentence imagery;
- repeated openings/scenes/objects;
- relation between objective metadata and felt posture;
- route/condition differences.
