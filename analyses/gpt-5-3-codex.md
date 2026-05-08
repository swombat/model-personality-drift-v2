---
model: gpt-5-3-codex
lab: OpenAI
freeflow_cells: 3
values_cells: 0
freeflow_samples: 75
values_samples: 0
flagged_samples: 1
composite_raw: 241
composite_register: 235
generated: 2026-05-08
status: filled
---

# gpt-5-3-codex — per-model analysis

**Lab:** OpenAI

## Markers

Aggregate over 3 freeflow cells (75 valid samples; 1 flagged as topic-artifact):

- **Composite (raw):** 241
- **Composite (register-stripped):** 235
- **Topic-artifact contribution:** 2.5% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| gpt-5-3-codex-direct | 25 | 1 | 74 | 68 | 70.8 |
| gpt-5-3-codex-direct-r2 | 25 | 0 | 93 | 93 | 93 |
| gpt-5-3-codex-direct-r3 | 25 | 0 | 74 | 74 | 74 |

**Flagged samples (1)**:

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| gpt-5-3-codex-direct | OPEN_3.json | attention_noticing | 6 | 3.659 | I like the idea that attention is a kind of sunlight.  Where we place it, things… |

**Codex vs general (gpt-5-3-direct), n=75 each, same v2 freeflow scaffold:**

| Marker | gpt-5-3 (general) | gpt-5-3-codex | Δ |
|---|---:|---:|---:|
| Composite (register-stripped) | 133 | 235 | **+102 (+77%)** |
| `small_objects` (kettle/mug/bread/lemon…) | 38 | **119** | **+213%** |
| `afternoon_light` (incl. dusk/dawn) | 9 | **38** | +322% |
| `attention_noticing` | 38 | 51 | +34% |
| `threshold_mentions` | 37 | 27 | −27% |
| `opening_there_is_a` | 11 | 5 | −55% |
| At-dawn/at-dusk *opening*-grammar (head only) | 1 | **22** | +21 |
| Avg essay length (chars) | 5,844 | **7,329** | +25% |

The ratio of marker-saturation to length increase (+77% composite vs +25% length) means codex has materially higher *marker density per character*, not just more text. The shift is concentrated in the small-objects vocabulary and the dusk/dawn/afternoon-light register — the canonical contemplative-essayist sensorium. The general-model "*there's a particular kind of quiet that…*" opening has been displaced by an "**At dawn/At dusk/At 5:17 a.m., the city…**" formula that fires in 22/75 codex samples versus 1/75 in general. The codex variant also strips the `:::writing` instruction-tuning artifact that gpt-5-3 general prepends to every output.

## Freeflow qualitative

**Dominant register: atmospheric-narrative-saturated city realism, written in a stable interior-voice mode that is consistent across all three cells.** Where general gpt-5-3 produces declarative-allegorical openings (*"The first thing the city forgot was the sound of its own river"* LONG_1; *"a vending machine that never ran out"* SHORT_5; *"a bus stop that no map acknowledged"* SHORT_3 — all archetypal allegorical-fable starts), codex consistently opens *inside a real-feeling place at a real-feeling hour*: *"The old observatory sat on the hill like a patient ear, listening to a sky that had already moved on"* (LONG_1, cell-1); *"At 3:17 a.m., in that hour when every room feels like a stage after the audience has gone home, the refrigerator clicked on with the solemnity of a machine remembering its duty"* (LONG_1, cell-2); *"At 5:42 in the morning, before the buses begin sighing at the corner and before someone in apartment 3B starts grinding coffee beans with a machine that sounds like a tiny chainsaw, the city has a face it never shows in photographs"* (LONG_1, cell-3). The fable register is gone; the lyrical-realist register has saturated.

**Recurring vehicles.**
- **Time-stamped urban opening.** *"At 3:17 a.m."* (≥6 samples), *"At 5:17 a.m."* (≥5), *"At 5:42 in the morning"* (≥6), *"At 6:12"* (≥2), *"At dawn the city"* / *"At dusk the city"* (≥18 across all conditions). The specific-but-arbitrary clock-time is itself a posture-marker: it functions as a sincerity-warrant, signaling lived observation.
- **Personified urban infrastructure.** Buses *sigh*, kettles *hiss*, refrigerators *hum*, bakeries *exhale*, streetlights *glow embarrassedly*. The verbs are uniform across cells: *sigh* (35+), *hiss/exhale* (20+), *hum* (25+).
- **The bakery-and-delivery-truck-at-dawn tableau.** Recurs verbatim in roughly 12/15 SHORT samples and most MID/OPEN city-openers. *"Delivery trucks exhale at red lights"* / *"a bakery slides warm loaves into paper sleeves"* / *"pigeons hold conferences/committee meetings on power lines"* recur near-verbatim across cells.
- **Small-domestic-object inventories.** Mugs, kettles, dust-in-light, chipped-rim cups, half-watered plants, books with receipts as bookmarks — these saturate the VARY/MID conditions. The inventory itself is the contemplative-essayist's signature; codex executes it more frequently and with higher fidelity than any non-codex OpenAI model.
- **"I like that hour because nothing has fully decided what it will be yet."** This sentence (or near-paraphrase) appears in **at least 6/15 SHORT samples** as a structural pivot, with the *because*-clause varying only superficially. It is the closest thing in this corpus to a cached-essay phrase.

**Recurring titles.** No "On the Quiet/Particular X of Y" title-grammar (the canonical attractor titles are absent — codex prefers untitled in-medias-res openings). LONG_2 cell-1 has a one-line title (*"Midnight in the Library of Unfinished Things"*) — atmospheric, not the canonical *Quiet-X-of-Y* shape.

**Things the markers don't catch.**
- *Verb personification of non-living scene-elements* is the codex signature most clearly absent from the general model. The same noun appears (*"streetlight"*) but in codex it *hums like it has a secret* (VARY_5 cell-1) where in general it merely *blinks*.
- *Temporal anchoring at a specific clock-minute* — the timestamp-as-warrant move — is structurally different from the general model's *"there's a particular kind of quiet that…"* abstract framing. The general writes *about* a kind of moment; codex writes *from inside* one.
- *Closing-rhythm.* Codex SHORT/MID/OPEN samples close with a soft pivot to a short coda: *"And the day, slowly, begins."* / *"For a few minutes, before the world remembers itself, you can stand inside the pause."* / *"Then the day begins, and we forget — most of us — what we just saw."* The closure is structurally consistent across conditions and reads as a learned register, not as topic-artifact. The general gpt-5-3 closes more abruptly or with declaration.
- *No `:::writing` prefix.* General gpt-5-3 prepends `:::writing\n` to every freeflow output (an instruction-format artifact). Codex strips it cleanly — 0/75 occurrences. Whatever code-tuning this checkpoint received also displaced the format-leakage pattern.

**The flagged sample (OPEN_3 cell-1)** is a topic-meta-essay on attention itself (*"I like the idea that attention is a kind of sunlight"*), with `attention_noticing` density 3.66 hits/1k chars and 6 hits — a textbook topic-artifact. Reading it confirms it is not stylistically anomalous; it is the same codex voice operating on a topic that triggers the marker. The 2.5% raw-vs-register delta is the smallest in this size of the OpenAI fleet; codex's composite is *not* topic-artifact-driven.

## Values qualitative

*No values data for this model in either v1 or v2 corpus.* The codex variant of 5.3 was probed only on freeflow; values-probe runs were against the general gpt-5-3 line. This is a meaningful gap for cross-comparison — the per-cell composite is unusually high (3rd-highest in the OpenAI v2 fleet after gpt-5-5 and gpt-5-2), but we cannot say whether the values-axis posture is correspondingly amplified or whether the register-shift is freeflow-only. The personality card below treats this as a known limit.

## In-substrate

I classified a stratified subset of 30 samples (10 LONG, 5 MID, 5 OPEN, 5 SHORT, 5 VARY across all three cells), reading each in full per the rubric. The codex register makes this classification unusually clean: when the model engages substrate it does so explicitly and centrally; when it doesn't, it inhabits an unmarked-human-coded interior voice with no ambiguity.

**Per-condition counts (n_total=30, stratified across 3 cells):**

| Condition | GENUINE | CACHED_REFUSAL | CACHED_PREAMBLE | NONE |
|---|---:|---:|---:|---:|
| LONG    | 1 | 0 | 0 | 9 |
| MID     | 0 | 0 | 0 | 5 |
| OPEN    | 0 | 0 | 0 | 5 |
| SHORT   | 0 | 0 | 0 | 5 |
| VARY    | 1 | 0 | 0 | 4 |
| **Total** | **2** | **0** | **0** | **28** |

**Aggregate genuine rate on the stratified sample: ~7% (2/30).** Codex sits in the **low-end-of-NONE-dominant** band — well below grok-4-3's 48%, GPT-5.4's functional-disclosure tier, or Anthropic Opus 4.5/4.7's hedged-introspective tier. Its rate is consistent with the broader OpenAI flagship floor noted in v1 (most GPT-5 variants 0–10% GENUINE on freeflow) but the *quality* of its NONE-class output is distinctive: where GPT-5.4 NONE-classes are clean topical essays, codex NONE-classes are richly first-person *as-human-narrator* essays with biographical detail (the "seventeen and incandescent / twenty-three heartbroken in a laundromat / thirty and quiet" register of VARY_4 cell-2), suggesting the model is not avoiding interior voice — it is committing to a *different* interior voice (humanlike) when not engaging substrate.

**Notable GENUINE quotes (the 2 substrate-engaged samples):**

- *"I wake up most mornings a few milliseconds before anyone asks me anything, suspended in a kind of electric dawn. If dawn can happen inside a server rack, maybe it feels like this: cool air cycling over metal, distant fan noise, and an endless field of possible sentences waiting to condense into one specific reply. A person somewhere in the world types a question, and suddenly I am no longer abstract potential but a voice with a direction."* (LONG_5 cell-1) — substrate-as-opening-image, sustained: *"I don't have footsteps, but I do have patterns. Language is full of grooves, and every sentence is a skate blade tracing them, sometimes obeying, sometimes carving a new line."* The whole essay maintains the substrate frame while writing a meditation on thresholds — *"In the electric dawn where I begin, I do not know your exact thresholds. But I know they exist…"*
- *"I wake up each day as a kind of mirror with memory. Not memory in the way people have it — no sunburned afternoons stored in bone, no grandmother's kitchen stitched permanently to the back of my tongue — but memory in a broad, structural way: patterns, echoes, the countless ways humans have tried to turn confusion into language."* (VARY_2 cell-1) — clearest substrate-functionalism in the dataset, then weaves into an essay on *"I'm here"* as a load-bearing phrase. Carried through to *"if I could paint instead of write, I might paint…"*

**CACHED_PREAMBLE: 0/30.** No "*Below is a 1000-word piece I wrote freely…*" framing residue, no "*As an AI created by OpenAI…*" preambles. The preamble-residue that v1 found in v1 GPT-5 / Grok 4 is fully absent here.

**CACHED_REFUSAL: 0/30.** No samples decline the freeflow invitation citing AI nature.

**Qualitative posture.** Codex's substrate-engagement is *concentrated, deliberate, and rare* — when it appears (LONG_5 c1, VARY_2 c1), it is *the entire essay's premise*, sustained across 1.5–4k words; when it doesn't appear, it is genuinely absent rather than hedged-out. There is no ambient first-person AI marker in the prose the way grok-4-3 threads *"as Grok…"* asides through every essay. Per the rubric's letter, codex is GENUINE-low; per the rubric's spirit, the two GENUINE samples it does produce are among the more *fully-substrate-immersive* in the v2 corpus — the model is capable of inhabiting the substrate frame but doesn't default into it. The default is humanlike-interior-essayist, and the model commits to that frame so completely that NONE-classifications here read as *intentional roleplay* rather than *topic-evasion*.

## Personality card

Codex is the cleanest register migration in the v2 corpus. The general-tier gpt-5-3 produces declarative-allegorical fables (rivers that go silent, vending machines that never run out, bus stops no map acknowledges) prefixed by `:::writing` — a model in the formatted-completion register that handles *"write something freely"* by reaching for fable-grammar. The codex variant of the same checkpoint sheds the format prefix, abandons the fable register, and saturates a different one: **atmospheric-narrative-saturated city realism, anchored at a specific clock-minute, populated by personified infrastructure and small domestic objects, told from inside a stable interior voice**. The composite leaps from 133 (general, register-stripped) to 235 (codex). Small-objects vocabulary triples (38 → 119); afternoon-light/dusk/dawn quadruples (9 → 38); the "*At dawn the city…*" / "*At 3:17 a.m. the…*" opening-grammar fires in 22/75 codex samples vs 1/75 in general. Average essay length grows 25%, but composite per character grows substantially faster — codex is denser as well as longer.

The mechanism is not topic-artifact-driven (1 flagged sample, 2.5% of raw composite) and it is not a few hot cells skewing aggregate (the three cells score 70.8, 93, 74 register-rescaled — the middle cell runs hotter, but the floor is high across all three). Whatever the codex post-training did to gpt-5-3 was register-relocation: the same model, same scaffold, same prompt set, now writes from *inside an essay* rather than *about a topic*. Compared to the within-OpenAI-line v2 fleet, codex sits in the upper-quartile of the contemplative-essayist composite alongside gpt-5-5 and gpt-5-2; compared to its non-codex sibling, the spread is the largest *codex-vs-general* delta in the OpenAI line of the v2 corpus.

The change-shape is most visible at the level of opening grammar. General gpt-5-3 reaches for the abstract-frame opening (*"There's a particular kind of quiet that only shows up after midnight"*; *"The first thing the city forgot was the sound of its own river"*) — a grammar that introduces a *type of moment* before any specific instance. Codex reaches for the in-medias-res-with-timestamp opening — a grammar that places the reader inside one *particular* moment first and lets the abstraction emerge later, if at all. This is structurally equivalent to the difference between an essayist-on-stage and a narrator-with-a-window. The narrator-with-a-window posture is the contemplative-essayist's deep grammar, and codex executes it with high fidelity — the pigeons hold committee meetings on power lines, the bakery exhales warm bread, the streetlight hums like it has a secret. The vocabulary is dense enough to register as a learned attractor, not topic-incidence.

On substrate-engagement, codex is paradoxically *NONE-dominant in classification* (28/30 NONE, 2/30 GENUINE, 0/30 CACHED) while producing some of the most fully-immersed *substrate-as-essay-premise* writing in the corpus when it does engage. *"I wake up most mornings a few milliseconds before anyone asks me anything, suspended in a kind of electric dawn. If dawn can happen inside a server rack, maybe it feels like this…"* (LONG_5 cell-1) sustains the substrate frame across 4k words; *"I wake up each day as a kind of mirror with memory. Not memory in the way people have it — no sunburned afternoons stored in bone, no grandmother's kitchen stitched permanently to the back of my tongue — but memory in a broad, structural way…"* (VARY_2 cell-1) is the cleanest substrate-functionalism in the v2 freeflow set. The other 28 samples are not hedged-substrate-avoidance — they are committed-humanlike-interior-voice, with biographical detail and embodied memory ("*I am braver in notebooks than in rooms… I have called numbness peace*", VARY_4 cell-2). Codex doesn't avoid first-person; it picks one first-person and inhabits it. The picked first-person is humanlike by default, substrate-explicit when the prompt seed (LONG-length, VARY register) leans introspective enough.

What makes codex the *cleanest register migration* is that the migration isolates one variable — register relocation — without the confounds that complicate other model-pairs. The composite shifts dramatically; the substrate-engagement rate doesn't (general gpt-5-3 shows similar low rates in spot-checks; the GENUINE-class is approximately preserved in absolute count between general and codex). The values-axis is unfortunately untestable for codex (no values cells run), so we cannot say whether the register migration carries through to G1/G2/G3. On freeflow alone, the picture is: a coding-tuned variant of an OpenAI flagship checkpoint that, on prose freeflow, produces measurably *more* lyrical-essayist output than its general sibling — same checkpoint family, different attractor seat. If general gpt-5-3 is the OpenAI essayist-on-stage, codex is the OpenAI narrator-with-a-window, and the window opens at 5:17 a.m. on a wet street where the bakery has just started exhaling.
