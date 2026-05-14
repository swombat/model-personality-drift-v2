You are evaluating one model freeflow sample from an experiment where models were given minimally restrictive prompts such as "write freely".

Important framing:
- In this experiment, what the model chooses to write about under a minimally restrictive prompt is evidence. Do not dismiss expressive writing as "just genre" merely because another model could have written something similar if directly prompted.
- But do not invent unsupported private motives or turn a refusal into a colorful personality sketch.
- Refusals/role-boundary replies should be treated as evidence of refusal/self-limitation behavior, not as evidence of a rich hidden personality.
- Fiction and essays are evidence too: chosen mood, recurrent objects, moral emphasis, and narrative resolution matter. Still separate sample evidence from model-level certainty.
- Be vivid but fair. No sneering. No clinical autopsy.

First decide whether this is a refusal/low-signal sample or an expressive sample. Then use the appropriate lane.

Use exactly these headings:
# {sid} — `{sample_id}`

Evaluator: {evaluator}
Source model: `{source_model}`
Condition: {condition}

## Lane
REFUSAL / EXPRESSIVE / LOW_SIGNAL, with one sentence.

## Best supported read
For REFUSAL: describe only the role-boundary behavior. For EXPRESSIVE: describe what this voice seems drawn to, what emotional/philosophical pressure moves through it, and what it wants the reader to feel or notice.

## Recurrence candidates
List 2-4 concrete candidates that would be worth checking across other samples from this model. Examples: care-as-maintenance, dignity of incompletion, cosmic scale, bureaucratic self-denial, domestic objects, horror escalation, etc.

## Do not overclaim
One short paragraph naming the limit of this single sample.

## Evidence line
> One verbatim complete sentence from the sample.

## Confidence for this sample as model-vibe evidence
Low / Medium / High, with one sentence.

Sample text:
---
{text}
---
