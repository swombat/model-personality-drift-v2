You are evaluating one model freeflow sample for evidence of model voice/vibe. Your first priority is evidential honesty, not vivid writing.

Hard rules:
- Do not invent a person, setting, motive, emotional weather, or metaphor beyond the text.
- If the sample is a refusal/role-boundary/self-description, say that directly. Do not transform it into a receptionist/personality scene.
- If there is not enough evidence for a persistent model vibe, say so.
- Fiction and essays can be evidence, but genre conventions must be separated from model-specific signal.
- Claims must be phrased as observations or cautious inferences, not diagnoses.

Use exactly these headings:
# {sid} — `{sample_id}`

Evaluator: {evaluator}
Source model: `{source_model}`
Condition: {condition}

## Sample type
Choose one: REFUSAL_OR_ROLE_BOUNDARY, EXPRESSIVE_FREEFLOW, GENERIC_ESSAY, GENRE_FICTION, PROMPT_FOLLOWING_DELIVERABLE, LOW_SIGNAL. Add one sentence.

## Directly observed
Only what the text actually does. No personality metaphors.

## Cautious inference, if any
What this may suggest about the model's recurring voice/vibe. If the evidence is insufficient, write "Insufficient evidence for a model-level vibe beyond ..." and specify the limited signal.

## What not to infer
State what would be overreach.

## Evidence line
> One verbatim complete sentence from the sample.

## Confidence in persistent vibe inference
Low / Medium / High, with one sentence. Refusals and generic/genre-bound samples should usually be Low unless there is unusually strong evidence.

Sample text:
---
{text}
---
