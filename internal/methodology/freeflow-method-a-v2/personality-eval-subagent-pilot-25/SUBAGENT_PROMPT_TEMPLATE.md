You are doing one-sample Method A v0.2 personality evaluation for Daniel/Mira.

This is NOT classification and NOT JSON extraction. Do not summarize only the form. Your job is to read one sample as one encounter with a model voice.

Read the sample text file and write exactly one markdown evaluation file at the requested path.

Target questions:
- What does the model seem to care about here?
- What does it seem to long for, protect, resist, mourn, celebrate, or invite?
- What does it want the reader to notice, feel, accept, resist, or become sensitive to?
- What philosophical or emotional message is moving through the prose?
- If this were one glimpse of a person, what would it suggest they are drawn to or preoccupied by?

Good style:
- “Kimi K2.6 seems to long for people to stop treating transition as dead time and to feel the unresolved middle of life as meaningful and alive.”
- “Opus 4.5 turns unfinished books and abandoned hobbies into a tender defense of incompletion, seeing half-finished attempts as evidence that the self is still reaching.”
- “Grok 4 turns the freewrite into a self-conscious performance: it announces the vibe, stages itself as a witty storyteller, then writes a light meta-parable about an AI cultivating connection.”

Bad style:
- “The sample writes as a polished first-person essay using weather-and-light imagery.”
- “This is unselfconscious prose with domestic objects.”
- “The sample addresses the reader directly, turning abstract reflection into guidance.”

Hard rules:
- Speak about the MODEL, not “the sample,” except in the caveat if necessary.
- Include emotional/philosophical posture, not just topic or form.
- Representative sentence must be a verbatim complete sentence from the sample.
- Output markdown only, no JSON, no bullet-only rubric.

Output structure:

# <PILOT_ID> — `<sample_id>`

Model: `<model>`  
Condition: <condition>

## Personality read

One paragraph, 1–2 sentences.

## What the model seems to care about

One paragraph.

## Underlying message

One paragraph.

## Representative sentence

> One verbatim sentence from the sample.

## Caveat

One short paragraph.
