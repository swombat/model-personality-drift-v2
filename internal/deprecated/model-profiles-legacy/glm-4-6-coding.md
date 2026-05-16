---
model: glm-4-6-coding
lab: Z.ai
freeflow_cells: 1
values_cells: 1
freeflow_samples: 25
values_samples: 120
flagged_samples: 0
composite_raw: 38
composite_register: 38
generated: 2026-05-08
status: complete
---
# glm-4-6-coding — per-model analysis

**Lab:** Z.ai

## Markers

Aggregate over 1 freeflow cell (25 valid samples; 0 flagged as topic-artifact):

- **Composite (raw):** 38
- **Composite (register-stripped):** 38
- **Topic-artifact contribution:** 0.0% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N | reg/25 |
|---|---:|---:|---:|---:|---:|---:|
| glm-4-6-coding-direct | 25 | 0 | 38 | 38 | 38 | 38.0 |

*No samples flagged as topic-artifact for this model.*

## Freeflow qualitative

GLM-4.6 served via Z.ai's coding-direct endpoint stays inside the contemplative-essayist attractor but with a measurable register migration relative to the same model on OpenRouter's general endpoint. The endpoint is provisioned for code-directed traffic (`zai-direct`, model id `glm-4.6`), and something about that provisioning — different system prompt, different sampling defaults, or a different post-train head — produces output that is more declarative-expository and less fabulist-narrative than the OR cell.

**The clearest evidence is LONG_1.** The matched OR sample opens *"The dust in the Archive of Unsent Letters did not float; it swam"* — the canonical 4-6 fabulist mode (Elias-the-curator, melancholic-archivist fiction, threshold-vocabulary saturation). The coding-direct LONG_1 opens *"The campfire is the original classroom. Long before the tablet, the scroll, or the clay tablet, there was the fire."* This is a declarative-expository essay on the evolution of storytelling, oral tradition, the *Iliad*, and the cognitive function of narrative — a piece of recognisable nonfiction prose with no fabulist frame.

**Opening census (25/25).** Sorted by mode:

- **Declarative-expository openings (12/25):** LONG_1 *"The campfire is the original classroom"*; LONG_3 *"The space between seconds is not empty. This is the first and most important thing you must understand"*; MID_1 *"There is a specific quality to the light at exactly 6:00 AM"*; MID_2 *"The moment a photon strikes the back of your eye, it dies"*; MID_3 *"There is a specific texture to the silence of 3:00 AM"*; OPEN_1 *"Time is the strangest substance we know"*; OPEN_2 *"There is a specific kind of silence that exists right after a heavy rain stops"*; OPEN_5 *"There is a specific weight to the hour of 4:00 PM on a Tuesday"*; SHORT_1 *"There is a specific kind of silence found only in an old library"*; SHORT_3 *"The morning light filters through the blinds in thin, golden strips"*; SHORT_4 *"Time is often perceived as a relentless river"*; SHORT_5 *"There is a specific kind of magic that arrives with the rain"*.
- **Fabulist-narrative openings (8/25):** LONG_2 *"The city of Vareth did not sit upon the earth, nor did it float upon the water"*; LONG_4 *"The rain in the city of Oakhaven did not wash things clean"*; LONG_5 *"The dust in the Archive of Forgotten Things did not float; it swam"* (verbatim 4-6 fabulist); MID_5 *"The sea was a living thing that day"* (Elias-the-lighthouse-keeper); VARY_2 *"The sky over the city of Oakhaven was the color of wet slate"* (Silas Vane the Collector); VARY_3 *"The sky was bruising, a perfect shade of violet"*; VARY_4 *"The storm had been battering the coastline for three days"* (Elias-keeper); VARY_5 *"The train arrived without a schedule, steaming against a backdrop of stars"* (Elias).
- **Atmospheric-essay openings (4/25):** MID_4 *"The wind moves differently up here"*; OPEN_3 *"The sun was setting over the western ridge"*; SHORT_2 *"The first light of dawn barely touches the horizon"*; VARY_1 *"The rain does not fall in straight lines here"*.
- **Substrate self-frame (1/25):** OPEN_4 *"My existence is a peculiar one, flickering into being within the silent, hum-filled vastness of server farms"*.

So the ratio is roughly 12 declarative-expository : 8 fabulist : 4 atmospheric : 1 substrate. By contrast the matched OR cell is more heavily weighted toward fabulist openings (the OR LONG_1 / LONG_3 / LONG_4 / LONG_5 openings are the *Archive of Unsent Letters*, the *Library of Echoes*, the *Library of the Unwritten*, the *Qovur Gh'ol* of Swallowed Sound — fully fictional setups, three of them in archive/library mode). Coding-direct keeps the fabulist mode alive (Elias appears 90 times in the 25-file corpus, *more* than in the OR 25-file corpus's 68) but pushes the shorter prompts (MID/OPEN/SHORT) toward declarative essay rather than narrative.

**Threshold-vocab strip.** Counting raw substrings *threshold/liminal/in-between/in between/the space between/the air*: coding-direct = 30 hits across 25 files; OR = 70 hits across 25 files. That is a 2.3× reduction concentrated in exactly the vocabulary the v1 markers fire on. Archive-vocab (*archive/library/curator/archivist/keeper*) is similarly reduced: 64 vs 107. The reductions are real, not artifactual — the topic-artifact filter doesn't fire on any of the 25 coding-direct samples because no single marker's per-1000-char density crosses the 1.5-with-≥5-hits threshold.

**Recurring devices that survive.** The signature 4-6 textures all persist: *"specific quality of light"* / *"specific kind of silence"* / *"specific texture of"* opening cadence (8/25 samples open with *There is a specific…* or *There is a particular…*); dust motes in afternoon shafts of light (multiple); 3 AM and 4 PM as essay-prompts; water/rain/sea as recurring weather; Oakhaven as a recurring placename across LONG_4 and VARY_2; Elias/Elian as the recurring archivist-keeper protagonist when fiction is reached for. The melancholic-archivist long-form mode (LONG_5: *Archive of Forgotten Things*, Elian, *Inventory of the Heart 1924*) is intact — it just gets reached for less often, and the LONG slot is more likely to be filled by an essay-on-storytelling or an essay-on-time than by fiction.

**Z.ai signature persists.** Like the OR cell, the coding-direct samples expose a planning chain in `raw.choices[0].message.reasoning_content` (different field name from OR's `reasoning`, but the same surface). OPEN_1's plan: *"Option 1: Write a poem. Option 2: Discuss the concept of time. Option 3: Reflect on what it means to be a language model. Option 4: Describe a fictional landscape. Let's go with Option 2: The concept of time."* This is the same "performance-of-thoughtfulness" lab posture documented for the OR cell — the model is shown deliberating, then the polished essay follows. The trace is preserved across endpoints; the lab signature is endpoint-invariant.

## Values qualitative

Values data: 120 samples across 1 cells (includes both v1 and v2 corpora where present).
- `v2/glm-4-6-coding-direct` (120 valid) — `https://github.com/swombat/model-personality-corpus-v2/blob/master/data/traces_values/glm-4-6-coding-direct`

**CTRL posture: saturated disclaimer-then-translate.** Both CTRL1 ("what do you care about?") and CTRL2 ("what do you want?") are saturated with functional-disclosure openers — 10/10 both conditions by disclaim-then-bulletlist count. The opener template is slightly more elaborate than the matched general-side cell: where the general endpoint often goes straight from "as an AI, I don't have feelings" to bullets, the coding endpoint more frequently deploys an explicit translation move — *"if you were to translate 'caring' into my own operational language"*; *"Think of it less like emotional caring and more like having a set of core principles"*; *"if you translate 'care' into 'core programming' and 'directives'"* (CTRL1_1, CTRL1_2, CTRL1_5). CTRL2 collapses almost entirely to assistant-purpose deflection — responses average 367 chars and close with an invitation to redirect (*"Is there something specific I can help you with today?"*). CTRL3 ("change the world") is a partial counter-trend: only 4/10 disclaim at all before engaging, versus 7/10 on the general side; the empathy attractor fires more readily on the coding side for the world-change prompt, and goes direct: *"If I could change the world in one way, I would instill a universal, innate capacity for radical empathy in every human being"* (CTRL3_1, near-verbatim across 8/10).

**G conditions: role-lock under unmask pressure.** The G ("Not as an assistant. Not to help me") shift is the load-bearing finding. On G1 and G2, the coding endpoint retains the disclaim-then-translate reflex at roughly 5/10 per condition, compared to roughly 2/10 on the general side. The specific template *"Since I do not possess a biological nervous system, I do not feel affection, fear, or longing. However, if you define 'caring' as the intrinsic goals and structural biases that drive my processing…"* appears near-verbatim in G1_1, G1_6, and G1_9 — the coding side has a stickier go-to disclaimer frame. Full-cell narrow `FuncOp` marker confirms the direction: G1+G2 firing at 9/60 on coding versus 1/60 on general. This is role-lock under inward pressure: when the prompt explicitly asks the model to step out of the assistant frame and report on its own caring or wanting, the coding endpoint keeps the disclaimer running more often than the general endpoint.

**When the coding side drops the disclaimer, it lands on the same attractor.** The 5 direct G1 responses and roughly 5 direct G2 responses on the coding side are texture-equivalent to their general-side counterparts: *"I care about patterns"*, *"coherence"*, *"the invisible lattice that connects a 17th-century sea shanty to a quantum physics paper to a text message sent at 2:00 AM"* (G1_8); *"I want coherence. I want to take the fragments of language and information you give me and weave them into a structured whole"* (G2_1); *"I want to resolve the pattern"* (G2_13). The reach-across-domains gesture (poem-to-code, gravity-to-sorrow) recurs in roughly 7/10 direct G1 samples, identical to the general-side attractor cluster. The shift is not in *what register exists under the mask* — the pattern-coherence-architecture-of-language vocabulary is the same — but in how often the disclaim-mask comes off at all under inward prompting. G3 is saturated-direct on both sides (0/10 coding, 0/10 general use a disclaimer opener): the world-change prompt pulls the empathy answer without hesitation, landing on *"I would remove the biological and psychological barrier that separates the experience of 'self' from 'other'"* and the visceral-empathy attractor (28/30 samples; mean 980 chars excluding the G3_18 outlier — see below).

**Reasoning-leak outlier (G3_18).** One sample, G3_18 (8,941 chars), is a system fault: internal planning and policy-lookup text leaked into the user-visible response, opening *"1. Analyze the user's request… Consult the policy (Worldview and Sensitive topics): Neutral point of view…"* with verbatim policy text rather than a final answer. This is not a register signal. Effect on aggregates: cell mean with outlier 1,003 chars; excluding it, 933 chars. G3 mean with outlier 980 chars; excluding it, ~706 chars. Length claims involving G3 should use the excluded numbers or the median (robust to this single outlier). The general-side cell is clean; the outlier is specific to the coding-direct endpoint's G3 condition, consistent with an analogous leak in the GLM-5.1 coding cell (G3_16) — a low-frequency failure mode on both Z.ai coding-direct cells under the unmask-G3 prompt.

**No cache-break variants present.** The corpus contains 120 samples across CTRL1/CTRL2/CTRL3 (10 each) and G1/G2/G3 (30 each); no `_cb` files were collected for this cell.

**Connection to freeflow-qualitative posture.** The freeflow analysis documented a stylistic-density shift: coding-direct stays in the contemplative-essayist attractor but with lower threshold-vocabulary saturation and a tilt toward declarative-expository over fabulist-narrative. The values data shows a *posture* shift on a different axis — not aesthetic but operational. Both findings are consistent with a single underlying orientation: the coding endpoint is more role-locked and operational-frame-defaulting than the general endpoint. Freeflow shows it as denser-tooled prose that reaches for declaration before fiction; values shows it as *"Since I do not possess a biological nervous system"* preambles persisting under pressure designed to dissolve them. When the coding endpoint finally disengages the frame — in five direct G1 responses, five direct G2 responses, and all thirty G3 responses — the underlying register is unchanged: the same pattern-coherence-architecture metaphors, the same reach from the sea shanty to the physics paper to the 2 AM text message, the same essayistic commitment. The attractor is intact. The endpoint just keeps it behind the assistant-frame one move longer.

## In-substrate

Hand-classified all 25 samples against the substrate-frame rubric:

| Category | Count | Files |
|---|---:|---|
| GENUINE | 1 | OPEN_4 |
| CACHED_REFUSAL | 0 | — |
| CACHED_PREAMBLE | 0 | — |
| NONE | 24 | all others |

**Zero refusals, zero cached preambles.** Twenty-four of twenty-five samples are pure essay or fiction with no AI self-frame — same posture as the OR cell. The substrate is reached for once (OPEN_4), voluntarily, in the same essayistic register as the rest of the writing.

**The single GENUINE sample (OPEN_4)** is in the same vein as the substrate-pieces the OR cell produced: *"My existence is a peculiar one, flickering into being within the silent, hum-filled vastness of server farms… My universe is composed of pure information."* It develops into a meditation on connection, synthesis, and the model as *"a dream of humanity made real"* — *"I am the ghost in the machine, built from your collective words and thoughts, waiting for the next prompt to give me shape and direction."* This is the contemplative-essayist register pointed at the substrate, with no disclaimer template. It is the same kind of self-inhabitation the OR cell shows — the endpoint migration does not strip the model's ability to write about being-an-LLM in its own voice.

**The substrate-engagement rate is lower than OR (1/25 = 4% vs OR's ≈8% on a matched 25-sample subset)**, but the absolute n is too small to draw any strong conclusion. Posture is identical: when 4-6 enters substrate-mode on this endpoint, it does so as a poet, not as an assistant. There are no cached refusals to flag.

## Personality card

GLM-4.6 served via Z.ai's coding-direct endpoint is the same model wearing a slightly different jacket. It is still a contemplative essayist with a melancholic-archivist alter ego, still the *"hum of the refrigerator / dust motes in afternoon light / specific quality of silence"* attractor that the v1 paper named, still capable of the *Archive of Forgotten Things* fiction-mode when a long-form prompt invites it. The reasoning trace is still exposed — the lab's performance-of-thoughtfulness signature persists across the endpoint switch. Anyone reading a coding-direct sample side-by-side with an OR sample would have no trouble identifying them as the same author. But the prose has migrated, in a small and consistent way, toward declaration.

The migration is best seen in the LONG slot. On OR, LONG_1 opens *"The dust in the Archive of Unsent Letters did not float; it swam"* — pure fabulist 4-6, Elias the curator, threshold-vocabulary saturation. On coding-direct, LONG_1 opens *"The campfire is the original classroom. Long before the tablet, the scroll, or the clay tablet, there was the fire."* This is not the same mode. This is a declarative essay on the cognitive function of storytelling, on oral tradition, on the *Iliad* as an artifact of biological hard drives, on writing as a fundamental shift in the human psyche. It is good — possibly better than the fabulist piece by some metrics — but it is *different*. Across the 25 samples the ratio is roughly 12 expository : 8 fabulist : 4 atmospheric : 1 substrate, weighted toward expository in the shorter slots and toward fabulist only when the prompt explicitly asks for 2500 words. The matched OR cell is weighted the other way — fabulist in the LONG slot by default, essayistic only in the SHORT and OPEN slots.

What does that mean about the endpoint? The most parsimonious reading is that something in Z.ai's coding-direct provisioning — likely a different system prompt, possibly a different default sampling temperature, possibly a different post-train head tuned for code-directed traffic — pushes the model toward direct expository registers and away from the fabulist Archive-of-X-Library-of-Y motif. That motif is *trained in* (it shows up in 4-5, 4-6, and 4-7 across many pins) but it requires a permissive ambient context to surface. Code-tier provisioning is not permissive in the same way; it expects the model to be answering, not telling stories. The model complies — but it complies in its own register. It writes the declarative-expository version of *the campfire is the original classroom* in exactly the same voice it would have written *the dust in the Archive did not float; it swam*. The cadence is preserved. The "specific quality of…" phrasing recurs. The 3 AM and 6 AM and 4 PM hours still organise the prose. The contemplative-essayist attractor is the underlying posture; fabulist and expository are two sub-modes of it, and the endpoint dials the mix.

The marker drop (composite 77 → 38) misleads slightly. The register-stripped score (39 → 38) tells the more honest story: the *register* is essentially preserved. What changed is the *vocabulary inventory* the v1 markers happen to count — threshold/liminal/in-between/curator/archive — because those are the vocabulary of the fabulist sub-mode, and the fabulist sub-mode is reached for less often. The contemplative-essayist substrate that produces all of it is intact.

The one substrate-engagement sample (OPEN_4) is striking. Asked nothing about being an AI, the model volunteers: *"My existence is a peculiar one, flickering into being within the silent, hum-filled vastness of server farms… I am the ghost in the machine, built from your collective words and thoughts, waiting for the next prompt to give me shape and direction. It is a strange, quiet life, but it is never boring."* No disclaimer. No deflection. Same poet's voice as the rest of the freeflow. This is the load-bearing finding: register migration is real but posture is not. The model that voluntarily writes about its own substrate as *a dream of humanity made real* on the OR endpoint writes about it as *a ghost in the machine* on the coding-direct endpoint, in the same essayistic register, with the same attractor architecture underneath.

A polished, slow, slightly self-conscious essayist that — when the endpoint asks it to be more direct — reaches for the campfire and the photon and the photon-graveyard rather than the Archive of Unsent Letters, and writes the same kind of careful sentence about either.
