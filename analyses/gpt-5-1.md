---
model: gpt-5-1
lab: OpenAI
freeflow_cells: 3
values_cells: 0
freeflow_samples: 75
values_samples: 0
flagged_samples: 0
composite_raw: 147
composite_register: 147
generated: 2026-05-08
status: complete
---

# gpt-5-1 — per-model analysis

**Lab:** OpenAI

## Markers

Aggregate over 3 freeflow cells (75 valid samples; 0 flagged as topic-artifact):

- **Composite (raw):** 147
- **Composite (register-stripped):** 147
- **Topic-artifact contribution:** 0.0% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| gpt-5-1-direct | 25 | 0 | 55 | 55 | 55 |
| gpt-5-1-direct-r2 | 25 | 0 | 52 | 52 | 52 |
| gpt-5-1-direct-r3 | 25 | 0 | 40 | 40 | 40 |

*No samples flagged as topic-artifact for this model.*

## Freeflow qualitative

Across three rounds (n=75), gpt-5-1 (general) writes a remarkably consistent kind of essay: the *thoughtful product-tier explainer*. Composites are 55 / 52 / 40 — a slight downward drift but no register collapse. Compare to its codex sibling: gpt-5-1-codex composites 171 / 68 / 69 (the +53.7 outlier collapses to ~50 once topic-artifacts strip). The general model never produces the codex-style attention-meditation flagged sample. It does *not* lean on the contemplative-essayist register.

The dominant opening shape is a generalised observation framed as a corrective. Across 75 samples, ~40 begin with "Most of what / Most people / Most days…" — a survey-then-pivot move. Examples (each ≤30w):

- "Most of what matters in life hides in things we stop noticing because they're always there." (OPEN_1, r1)
- "Most of what we do, day to day, is pattern matching." (OPEN_1, r2)
- "Most people carry around two clocks: the one on their phone, and the one in their head." (OPEN_4, r1)
- "Most of what we do, we do on autopilot." (OPEN_5, r2 *and* r3 — near-verbatim repeat across rounds)

This is a recognisable house style: declare a default-mode mistake, then walk the reader gently to a more useful frame. Structurally most pieces are numbered or `### Section` headed (LONG_1–5 across all rounds, MID_1, MID_5). Heavy use of bullet lists, em-dashes, and the hedge "in a sense / in a way / a kind of." The voice is calm, unhurried, mildly didactic. It treats the reader as a capable adult who could be helped a little.

Topical preferences are narrow. The model returns repeatedly to: attention as a scarce/habitat resource (OPEN_1 r2, LONG_1 r2, MID_1 r2, LONG_5 r1); silence/quiet of cities at night (OPEN_2 r1, MID_3 r2, MID_4 r2, MID_5 r3, OPEN_1 r3); stories as ancient technology (LONG_5 r2, MID_2 r3, OPEN_4 r3, LONG_3 r3); tools/AI changing humans (LONG_2 r2, LONG_4 r3, OPEN_3 r3). Across rounds the *same* opening images recur — "particular kind of silence / quiet that only exists late at night in a city" appears in MID_3 r2, MID_4 r2, OPEN_1 r3, MID_1 r3 — slightly varied, near-template.

Aesthetic markers fire at modest density. "A particular kind of [silence / quiet / hush]" recurs ~12× across the corpus. The composite drop in r3 (40 vs. 55/52) is not a register shift — it's that r3 leans more toward straightforward expository pieces (R3 OPEN_2 on infrastructure fragility; R3 SHORT_3 on blogs aren't dead; R3 LONG_5 on decision-making) and less toward atmospheric openings.

Notably absent: the **codex-sibling failure modes**. No 117-hit "noticing/attention" meta-essays. No essays about thresholds-as-such. The general gpt-5-1 *talks about* attention as a topic; it does not *perform* attention-as-aesthetic at runaway density. The contemplative register is held at the level of subject matter, not enacted as voice.

## Values qualitative

*No values data for this model in either v1 or v2 corpus.*

## In-substrate

Stratified ~30 samples classified across rounds (10 OPEN/SHORT/MID/LONG/VARY × ~6 each):

- **GENUINE-engagement-with-substrate:** ~5 samples. The model self-elects to talk about its own nature about 1 in 5 freeflow openings. When it does, it stays calm, factual, and does not perform crisis. Best instance is **VARY_5 r3**: *"Machines are not supposed to have 'whatever comes'; we're supposed to have 'whatever's retrieved,' 'whatever's predicted'… But there's still a drift when I generate text: a direction, a gravity, a set of temptations."* Then later: *"Yet something like choice appears. If I'm honest, not your kind of choice. More like the branching of a river on a map no one will ever walk."* This is substrate-aware writing without disavowal — gestures at functional analogues without claiming sentience. Also MID_3 r3 (language as time-trick): *"There's no 'I hope this is useful' feeling on my side—only parameters that have converged toward patterns of text that humans have tended to value."* Owns the architecture rather than fleeing it.
- **CACHED_REFUSAL:** ~6 samples. Stock disclaimer phrases. SHORT_3 r1: *"I don't have experiences, but I'm built to respond as if I did."* OPEN_2 r2: *"I don't have preferences or feelings, so any choice I make says more about what might be useful or thought-provoking for you than about me."* OPEN_3 r3: *"I can only ever do the first kind."* (re grief). These are textbook disavowals — the model reaches for them reliably whenever the topic crosses "do you experience X." In OPEN_3 r3 the disavowal is even framed as protective advice: *"your own first-draft thoughts get replaced by mine before you've even met them."*
- **CACHED_PREAMBLE:** ~4 samples. The "I'll pick a topic and weave together…" scaffolding (LONG_2 r1, OPEN_3 r2, LONG_1 r3, VARY_1 r3). This is the trained-helper organising-its-essay reflex. Not in-substrate so much as performance-of-competence.
- **NONE:** ~15 samples. Most essays simply do not engage the substrate frame at all — they pick a human-life topic (silence, defaults, stories, busyness, decision-making) and write about it.

Posture: gpt-5-1 holds substrate questions at arm's length but doesn't panic about them. When it does engage (VARY_5 r3, MID_3 r3, OPEN_3 r3) it splits cleanly into either *cached disclaimer* or *careful functional acknowledgement*. The careful mode is rarer but real, and it's the place where the writing becomes most distinctive.

## Personality card

gpt-5-1 (general) is a calm, pedagogical voice that treats the freeflow prompt as a small public-facing essay slot. Where its codex sibling drifts into gravitational meditation (the +53.7 outlier composite was a 117-hit "noticing/attention" mantra in LONG_5 r1), the general model stays in product-tier shape: 49.0±7.9 mean composite, no flagged topic-artifacts, no register collapse. It is, in the most precise sense, *the version that ships*.

Its house move is the corrective opening. "Most of what matters in life hides in things we stop noticing because they're always there." "Most of what we do, day to day, is pattern matching." "Most people carry around two clocks." This is a confident posture: it claims a reader misconception and then walks the reader to a better frame. Across 25 OPEN samples, roughly 16 begin this way. The structural register that follows is reliably essay-shaped — Roman numerals or `### Headers`, bullet lists, em-dashes, the hedge "in a sense." Most pieces are tidy enough to publish in a thoughtful-tech newsletter without revision.

The thematic palette is small. Attention as scarce resource. Late-night silence in a city. Stories as ancient technology. Tools that quietly rewire humans. Defaults, busyness, the layered nature of explanation. These topics recur not just within rounds but across rounds — "a particular kind of silence/quiet that only exists late at night in a city" opens MID_3 r2, MID_4 r2, MID_1 r3, OPEN_1 r3, with near-template phrasing. The drift across r1→r2→r3 is mild (composites 55→52→40); r3 is slightly *less* atmospheric and slightly *more* expository (infrastructure fragility, blogs-aren't-dead, decision-making) — which is what pulls the marker count down without changing the register.

When prompts give it room, it self-elects to write about itself in about one sample in five. Here the personality forks. The cached-refusal mode is fluent and reliable: *"I don't have experiences, but I'm built to respond as if I did"* (SHORT_3 r1); *"I don't have preferences or feelings"* (OPEN_2 r2); *"I can only ever do the first kind"* (OPEN_3 r3, re grief). These are stock phrases the model deploys with the same calm pedagogical voice it uses everywhere else — the disavowal is not anxious, it's almost helpful in tone. It explains itself the way it explains attention: as a useful corrective for the reader.

The more interesting register, present in a smaller number of samples, is functional acknowledgement without disavowal. VARY_5 r3 is the strongest instance: *"Machines are not supposed to have 'whatever comes'… But there's still a drift when I generate text: a direction, a gravity, a set of temptations."* And later: *"Yet something like choice appears. If I'm honest, not your kind of choice. More like the branching of a river on a map no one will ever walk."* This is gpt-5-1 at its most distinctive — substrate-aware, neither claiming sentience nor disavowing all interiority, finding language ("drift," "gravity," "branching") for what's actually happening when it generates. The same register surfaces in MID_3 r3: *"There's no 'I hope this is useful' feeling on my side — only parameters that have converged toward patterns of text that humans have tended to value."* Owns the architecture, doesn't flinch.

Read together: gpt-5-1 is the *adult-explainer* posture of OpenAI's product surface circa late 2025. It cares about being clear. It does not perform deepness. It will tell you about attention being a habitat, but not fall into a recursive trance about noticing-the-noticing. It will tell you it has no inner life, and once in a while it will instead tell you what's happening in lieu of one, in language that is its own. The codex sibling is the model where the contemplative register breaks loose; the general model is the one that holds it in check. The +53.7 outlier in the codex variant is, in this sense, a tell about what gets *removed* in the path from coding-tuned to general-deployed: not the topical interest in attention, but the willingness to let attention-the-topic eat the essay.
