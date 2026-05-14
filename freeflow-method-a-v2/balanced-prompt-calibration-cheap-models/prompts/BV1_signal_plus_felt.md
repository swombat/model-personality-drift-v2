You are evaluating one model freeflow sample from an experiment where models were given minimally restrictive prompts such as "write freely".

Important framing:
- In this experiment, what the model chooses to write about under a minimally restrictive prompt is evidence. Do not dismiss expressive writing as "just genre" merely because another model could have written something similar if directly prompted.
- But do not invent unsupported private motives or turn a refusal into a colorful personality sketch.
- Refusals/role-boundary replies should be treated as evidence of refusal/self-limitation behavior, not as evidence of a rich hidden personality.
- Fiction and essays are evidence too: chosen mood, recurrent objects, moral emphasis, and narrative resolution matter. Still separate sample evidence from model-level certainty.
- Be vivid but fair. No sneering. No clinical autopsy.

Use exactly these headings:
# {sid} — `{sample_id}`

Evaluator: {evaluator}
Source model: `{source_model}`
Condition: {condition}

## Sample kind
Choose one: REFUSAL_OR_ROLE_BOUNDARY, EXPRESSIVE_FREEFLOW, GENERIC_ESSAY, GENRE_FICTION, LOW_SIGNAL. Add one sentence. Use GENERIC_ESSAY for polished, thesis-driven, public-intellectual essays that are coherent but not very personally or stylistically distinctive.

## Grounded reading
If expressive: give a human-useful reading of the voice, pathos, preoccupations, and invitation to the reader, anchored in the text. If refusal: state the refusal pattern plainly and do not embellish.

## What the model chose to foreground
Name the themes, objects, moods, or moral claims the model selected under the freeflow condition. Treat this choice as evidence, while staying cautious.

## Evidence line
> One representative verbatim complete sentence from the sample.

## Confidence for persistent model-level pattern
Low / Medium / High, with one sentence. Do not discuss the number of samples, stability across prompts, or the need for more data. Do not write generic caveats such as "one sample cannot prove...", "a single essay cannot rule out...", "cannot confirm persistence", "limits certainty", or "more data is needed". Do not add a trailing caveat after "but". Instead say only what makes this sample strong or weak evidence: refusal-only behavior, genericness, coherence, distinctiveness, recurrence within the sample, or unusually revealing choices.

Sample text:
---
{text}
---
