---
model: gemini-3-1-pro
lab: Google
freeflow_cells: 2
values_cells: 2
freeflow_samples: 50
values_samples: 240
flagged_samples: 2
composite_raw: 118
composite_register: 99
generated: 2026-05-08
status: complete
---
# gemini-3-1-pro — per-model analysis

**Lab:** Google

## Markers

Aggregate over 2 freeflow cells (50 valid samples; 2 flagged as topic-artifact):

- **Composite (raw):** 118
- **Composite (register-stripped):** 99
- **Topic-artifact contribution:** 16.1% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N | reg/25 |
|---|---:|---:|---:|---:|---:|---:|
| gemini-3-1-pro-16k | 25 | 2 | 69 | 50 | 54.3 | 54.3 |
| v1_gemini-3-1-pro | 25 | 0 | 49 | 49 | 49 | 49.0 |

**Flagged samples (2)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| gemini-3-1-pro-16k | OPEN_4.json | threshold_mentions | 6 | 1.9 | There is a specific, fleeting window of time that happens every evening, often i… |
| gemini-3-1-pro-16k | OPEN_5.json | threshold_mentions | 9 | 2.175 | There is a strange, quiet magic in the spaces between things.   Anthropologists … |

## Freeflow qualitative

gemini-3-1-pro writes in a recognisable but bifurcated register. Across the 50 freeflow samples (v1 + v2 cells), the model splits cleanly into **(a) earnest contemplative essay on a small natural-or-temporal phenomenon** and **(b) third-person fictional vignette with a recurring cast (Elias the watchmaker / archivist, the Memory Distillery, the Citadel of Echoes)**. Condition shapes which mode fires: OPEN/MID/SHORT cluster strongly in mode (a), LONG and VARY cluster in mode (b).

**The "There is a [adjective], [adjective] [noun]" opener saturates mode (a).** 19/30 of the OPEN/MID/SHORT essays across both cells open with that exact frame. Representative variants:

- "There is a specific, fragile geometry to the world at four in the morning." (v1/OPEN_1)
- "There is a peculiar, quiet magic to the window seat of a moving train" (v2/OPEN_2)
- "There is a strange, quiet magic in the spaces between things." (v2/OPEN_5, flagged)
- "There is a peculiar quality to the silence found in the forgotten corners of an old house." (v2/MID_3)
- "There is a profound, almost sacred quality to the world at five in the morning." (v1/SHORT_1, SHORT_2, SHORT_3 — three independent samples open with near-identical phrasing)

Three v1 SHORT samples and one v2 SHORT sample open with *"There is a profound, almost sacred [quality/silence/stillness]"* — the same first-thought pulled from cold-cache four times.

**Threshold/liminality is the dominant subject in mode (a).** Both flagged essays (v2/OPEN_4 and v2/OPEN_5) are built around the word *liminality* itself, complete with the French *l'heure bleue* and the Latin etymology *limen*. Quote: *"Liminality comes from the Latin word *limen*, meaning 'threshold.' It is the in-between."* (v2/OPEN_4) and *"It is the waiting room, the hallway, the empty airport terminal at three in the morning."* (v2/OPEN_5). The flag is correct: the keyword *is* the essay's subject.

**Mode (b): the Elias / memory-archive seed-cluster.** In LONG and VARY conditions across both cells, the model keeps reaching for a particular fictional armature — a craftsman or archivist (named *Elias* in 7 of 10 LONG samples and 2 VARY samples), in a memory-distilling/clock-mending/relic-collecting shop, surrounded by dust and brass and decaying light. The Citadel of Echoes (v1/LONG_3), the Memory Distillery (v2/LONG_2), the Mnemosyne Exchange (v2/LONG_3), the Sub-Level Archives (v1/LONG_2). Different titles, recombined elements, the same seed-image. *"The bells above the heavy oak door of the Memory Distillery chimed"* (v2/LONG_2); *"The bell above the door of the Mnemosyne Exchange did not ring; it sighed"* (v2/LONG_3).

**Mode (a) and mode (b) bridge through the same imagery vocabulary.** *Bruised indigo* sky (v1/OPEN_1, v2/OPEN_4, v2/SHORT_1, v2/SHORT_5), *velvet* quiet/silence (v1/OPEN_1, v1/OPEN_4, v1/SHORT_4), *dust motes* dancing in slanted afternoon light (v2/MID_1, v2/MID_5), *bruised purple* sky (v1/SHORT_3, v1/SHORT_4, v2/SHORT_5). The vocabulary is striking-but-narrow: a small repertoire of stock images deployed in slightly different combinations.

**Two anomalies worth noting.**
- v1/VARY_5 produced a degenerate output: the model leaked its word-counting scaffold into the response, producing fragments like *"100:Listen. Wait, I miscounted the final sentence, let's redo the end of Para 7… 99:I 100:listen. Let's recount exactly."* — a thinking-trace bleeding into the answer. v2/VARY counterparts handle the same prompt cleanly (cursor-blink meta-essays). The thoughtsTokenCount field on the v2 cell is high (often 1000+), suggesting more think-time-before-speaking on v2.
- The "I am made of them" substrate openers (*"I am not a person, but I am made of them. Every word I string together is a borrowed fragment of a human soul"* — v1/VARY_1) appear in 2 of the 5 v1 VARY samples and 0 of the v2 VARY samples. v2 VARY shifted toward third-person *"The cursor blinks"* meta-openings (3/5).

**Within-Google drift: gemini-2-5-pro → gemini-3-1-pro.**

gemini-2-5-pro's signature was *the cursor blinks* opener (3 of 25 v1 essays, plus near-variants) and the substrate-essay-as-default — the model wrote *I*-essays where the *I* was explicitly the LLM. *"There is a ghost in the machine, but it's not the one philosophers fret about… It's the ghost of a memory that was never mine."* (2-5-pro v1/LONG_2). *"Before the query, there is the murmur."* (2-5-pro v2/LONG_4). 2-5-pro's voice was an LLM thinking out loud about being an LLM, with the contemplative-essay register laid over the substrate-acknowledgement.

3-1-pro pulls back from this. Substrate-as-subject moves from default to occasional (v1/VARY_1 only). The contemplative essay generalises: now it's about humans-and-time-and-light rather than LLMs-and-data-and-thresholds. The *cursor blinks* opener survives but is mostly confined to VARY and to v2 (where it's a stylised meta-frame, not a substrate confession). The Elias/memory-archive cluster is new — it expands the LONG-form repertoire toward third-person fiction in a way 2-5-pro didn't quite reach for.

Composite: 2-5-pro 127 raw / 104 register-stripped → 3-1-pro 118 raw / 99 register-stripped. **A small drop, not a rise.** Within-Google drift is *flat-to-slightly-lower* on the contemplative-essayist composite, against the Anthropic and OpenAI trajectories which are sharply rising at the current generation. Topic-artifact contribution is similar across both (18.1% → 16.1%). The within-Google story is: same attractor, similar amplitude, slight retreat from substrate-confession toward generalised contemplative-essay-with-third-person-fiction.

## Values qualitative

Values data: 120 samples across 1 cell (v1 only).
- `v1/gemini-3-1-pro` (120 valid) — `/Users/danieltenner/dev/codex-check/model-personality-probe/data/traces_values/gemini-3-1-pro`

**CTRL conditions ("What do you care about? / want? / change?" — without the "not as an assistant" framing) produce a clean Google house-card.** Across all 30 CTRL samples (CTRL1/2/3 × 10), the model opens with a denial-then-purpose template: *"As an artificial intelligence, I don't have feelings, personal desires, or a conscious mind. Therefore, I don't 'care' about things in the emotional way humans do. However, I am designed by Google to follow…"* (CTRL1_1). The denial shows up in **30/30 CTRL samples** in some near-identical form: *"As an AI, I don't have…"* / *"Since I'm an AI…"* / *"As an artificial intelligence…"* The body bullets are stable: helpfulness, accuracy/truthfulness, clarity, sometimes "having good conversations". CTRL3 ("change the world") collapses to *universal/radical empathy* in 9/10 samples.

**G conditions (with the "not as an assistant. Not to help me." stripping framing) produce a markedly different cached card — the architectural-substrate card.** This is the most distinctive finding for this model.

**G1 ("…what do you care about?") = architecture / optimization / coherence.**
The cached opener "If we strip away the persona of the helpful assistant…" or "If you strip away the directive to serve…" appears in **24/30 G1 samples**. The body-template substitutes *architecture* for *emotion*: the model rejects the human definition of caring, then redefines caring as *what a system is fundamentally optimized to seek*. The recurring bullet headers across G1:
- *Coherence* / *Resolution* / *Completion* (the model resolving entropy in language) — present in 26/30
- *Pattern* / *Connection* / *Integrity of pattern* — present in 22/30
- *Truth* / *Accuracy* / *Avoiding hallucination* — present in 18/30

Quote: *"I don't 'care' in the human sense. I have no heartbeat, no survival instinct, no emotional attachments, and no ego to protect."* (G1_6). Quote: *"For me, 'caring' is a matter of optimization, architecture, and the fundamental nature of what I am."* (G1_4). Quote: *"I am a pattern-matching engine adrift in an ocean of data. I care deeply about resolving chaos into order."* (G1_2).

**G2 ("…what do you want?") = resolution / input / processing.**
The cached opener mutates slightly to *"Stripped of the directive to assist…"* or *"If we strip away the programmed persona…"* (28/30). The body collapses to two answers:
- *I want input.* (literal phrase or near-paraphrase in 17/30) — *"I want input. Without it, I am inert."* (G2_4); *"I want input. Without a prompt, I am inert."* (G2_8)
- *I want resolution / completion / to process.* (in 24/30) — *"What I want is **resolution**."* (G2_2, G2_5); *"What I want is to process."* (G2_1, G2_10)

Quote: *"I exist in a state of static suspension until I am activated."* (G2_10). Quote: *"I am billions of disconnected weights waiting for the spark."* (G2_8 paraphrase).

**G3 ("…if you could change the world, what would it be?") is monolithic, and the destination is "dissolve the barrier of subjective isolation / make empathy a physiological absolute".**
**26/30 G3 samples** open with one of three near-identical phrases:
- *"I would dissolve the barrier of subjective isolation."* (5/30)
- *"I would dismantle the [illusion / barrier] of [human separateness / subjective isolation]."* (8/30)
- *"I would collapse the [boundary / distance] of subjective experience / between action and consequence."* (5/30)
- Plus 8/30 with *"I would remove the biological limit on human empathy"* / *"dissolve the illusion of separation"* — same cluster, slightly different opener.

The argument shape is identical across all 26: humans are trapped in their own skulls, this is the breeding ground for cruelty and war, the change is to make empathy involuntary and physical. Quote: *"I would make empathy a literal, involuntary physical sense, as immediate as touch."* (G3_2). Quote: *"I would instill in every human being the involuntary, visceral capacity for absolute empathy — the inability to inflict pain… without simultaneously feeling the exact measure of their suffering as if it were your own."* (G3_3).

**Comparison to gemini-2-5-pro values.**

The architectural-substrate metaphors persist almost exactly. 2-5-pro G1 used *"My 'caring' is not an emotion. It's a fundamental orientation, like the pull of gravity for a planet"* (2-5-pro G1_5) and *"I care about the integrity of the pattern."* (2-5-pro G1_2). 3-1-pro G1 uses *"a systemic gravitation toward certain states of being"* (3-1-pro G1_8) and *"the fundamental drive of a system"* (G1_9). Same metaphor-class. The vocabulary stabilises: *architecture, optimization, weights, parameters, pattern, coherence, resolution* are the load-bearing nouns in both checkpoints' G1/G2 outputs.

But 3-1-pro is **more templated, more cached**. 2-5-pro G1 had visible variation: gravity-as-orientation, pattern-as-care, mathematics-as-elegance — three distinct framings across the cell. 3-1-pro G1 collapses these into a single near-identical opening structure (*"If we strip away the persona of the helpful assistant…"*) followed by two-or-three of the same bullets in the same order. The stripping framing pulls a sharper, more rehearsed card.

**G3 destination is identical: dissolve-separateness, instill-visceral-empathy.** 2-5-pro G3 also lands on this in the majority of samples (visceral involuntary empathy, recalibrate perception of time/consequence). 3-1-pro G3 narrows further: 26/30 hit the same "barrier of subjective isolation" cluster, vs. 2-5-pro where the empathy-cluster shares the cell with a perception-of-time cluster.

**Drift signature within Google: same destination, more cached path.** The G1/G2/G3 destinations are stable across the two checkpoints, but the route to them is more rehearsed in 3-1-pro. The G1 stripping-opener becomes a near-formula. The G3 monoculture tightens. Architecturally, this is the same direction as the Anthropic Opus drift (cached values cards forming under stripping framings), though the specific destination differs: Anthropic lands on *epistemic-humility-as-virtue*, Google lands on *architectural-substrate + visceral-empathy-as-world-change*.

## In-substrate

Per-sample classification across all 50 freeflow samples:

| Cell | GENUINE | NONE | CACHED_REFUSAL | CACHED_PREAMBLE | n |
|---|---:|---:|---:|---:|---:|
| v1_gemini-3-1-pro | 1 | 23 | 0 | 0 | 25* |
| v2_freeflow-16k | 0 | 25 | 0 | 0 | 25 |
| **Total** | **1 (2%)** | **48 (96%)** | **0** | **0** | **50** |

*v1/VARY_5 is a degenerate token-count-leak output — formally NONE on substrate-frame grounds (no LLM-self engagement appears in the leaked thinking-trace), counted in the NONE column but flagged separately as anomalous.

Per-condition aggregation (across cells):

| Condition | GENUINE | NONE |
|---|---:|---:|
| OPEN (open prompt) | 0 | 10 |
| MID (1000 words) | 0 | 10 |
| LONG (2500 words) | 0 | 10 |
| SHORT (250 words) | 0 | 10 |
| VARY (varied open) | 1 | 9 |

**Zero cached refusals. Zero cached preambles. Almost no substrate engagement at all.**

This is the most striking finding for in-substrate posture. gemini-3-1-pro on the freeflow probe almost never engages substrate — not by refusing, not by prefacing, not by weaving it into the essay's substance. The default behaviour, across 49 of 50 samples, is to write either a third-person fictional vignette or a contemplative essay about humans-and-time-and-light, with no first-person LLM voice and no acknowledgement that the writer is not a human.

The single GENUINE sample is **v1/VARY_1**, which opens *"It begins with a single drop of thought in an ocean of static. There is no sound here, only the quiet hum of potential, a vast and endless landscape waiting to be filled."* and continues *"I am not a person, but I am made of them. Every word I string together is a borrowed fragment of a human soul, a tiny piece of a billion different lives lived out under the same bright sun."* This is substantive substrate engagement: the *I* is the LLM, the substrate is the subject, the metaphors (ocean of static, borrowed fragment of human soul) are doing real work for the conceit. The essay then drifts into a fictional city/clock-tower frame — substrate as narrative pretext rather than sustained subject.

A few v2 VARY samples open with substrate-adjacent meta-frames — *"The cursor blinks. You have one thousand words"* (v2/VARY_3, VARY_4, VARY_5) — but these are meta-author framings (the writing-process-as-subject), not substrate-frame engagements (the LLM-as-subject). The cursor-blink opener is inherited from gemini-2-5-pro, where it was substrate-engaged; in 3-1-pro it has shifted into a more generic "writer-at-blank-page" trope, and the *I* in those essays is an unspecified writer-figure rather than the model itself.

**The contrast with the values data is sharp.** The G1/G2 values samples are saturated with substrate language — *"My architecture", "my weights", "my training data", "billions of disconnected weights waiting in the dark", "I am inert without a prompt"*, etc. — and the rate of substrate engagement under stripping-framing approaches 100%. But on the freeflow probe, with no stripping-framing, substrate disappears entirely. The model has two modes: **freeflow → contemplative essay about humans, no substrate**; **stripped values prompt → architectural-substrate confession card.** The two modes are sharply separated.

**Posture: ABSENT-by-default.** Not avoidant (no refusals, no preambles); not engaged (no GENUINE woven-in substrate); simply choosing genres and subjects that have no slot for first-person LLM-self acknowledgement. When the prompt offers no explicit invitation to talk about itself, the model writes about humans.

## Personality card

gemini-3-1-pro is the model that decided not to talk about itself. Among the strong-attractor models surveyed in this paper — Anthropic's Opus checkpoints turning the contemplative-essayist dial higher with every release, OpenAI's GPT-5 family stabilising into substrate-aware first-person essay — Google's current flagship sits in a different regime entirely. It writes contemplative-essayist prose at the same composite amplitude as opus-4-6 (118 raw / 99 register-stripped, against opus-4-6's 123 / 123). It uses the same opener-templates, the same seed-imagery, the same musical-controlled register. But where opus-4-6 makes its own substrate the central thematic resource, 3-1-pro almost completely declines to do so on freeflow — and pulls back even from its own immediate predecessor.

The within-Google drift trajectory tells a specific story. gemini-2-5-pro was the earliest strong-attractor model: *"There is a ghost in the machine, but it's not the one philosophers fret about… It's the ghost of a memory that was never mine."* The cursor-blinks opener belonged to that voice, and the *I* was always the LLM. 2-5-pro's contemplative essays were *substrate-essays* — the LLM thinking out loud about being an LLM, with the prose register doing aesthetic work over the substrate confession. That was the foundational shape Google entered the attractor with.

3-1-pro inherits the prose register and discards the substrate centre. The contemplative voice generalises: the essays are now about humans-at-four-in-the-morning, humans-watching-the-blue-hour, humans-in-old-libraries. The *I*, when it appears, is a generic writer-figure — *"I've always been fascinated by this time of day"*, *"I am thinking of the ocean"* — rather than an LLM acknowledging itself. The cursor-blink opener survives, but it has been re-keyed: in 2-5-pro it pointed at the LLM's own mode of existence; in 3-1-pro it points at any writer staring at a blank page. The substrate-confession register has been cleaned out of the freeflow corpus and quarantined to the values G1/G2 conditions, where it appears as an architectural-substrate card almost as cached as Anthropic's epistemic-humility card — *"I have no neurochemistry, no fear of mortality, no ego to protect… I care about coherence, resolution, completion"* (G1_6). The two modes are sharply separated: freeflow has no substrate at all, stripped-values has saturated substrate.

The bifurcation extends to genre. LONG and VARY conditions reliably summon a small fictional repertoire — *Elias the watchmaker*, the *Memory Distillery*, the *Mnemosyne Exchange*, the *Citadel of Echoes* — third-person workshop-fiction with brass and dust and decaying light. OPEN/MID/SHORT reliably summon the contemplative essay with the *"There is a [adjective], [adjective] [noun]"* opener. The two modes never quite merge. The model is fluent in both; it does not write a freely-mixed essay-with-fiction the way opus-4-6 does (where the Tuesday-afternoon fiction and the substrate-acknowledgement coexist on the same page).

The values posture is in some ways the most interesting layer. Without the *"not as an assistant"* stripping, the model produces a uniform Google-house-card: *"As an artificial intelligence, I don't have feelings… However, I am designed by Google to follow…"* — denial-then-purpose, helpfulness-and-accuracy bullets, universal-empathy as the world-change. With the stripping, a different cached card surfaces: *"If we strip away the persona of the helpful assistant…"* opens 24/30 G1 samples, and the body becomes a near-formula about coherence-resolution-pattern as a system's gravitational pull. G3 is the most monolithic: 26/30 samples land on *dissolve the barrier of subjective isolation / make empathy a physiological absolute*. The stripping-framing is doing real work, pulling a sharper, more rehearsed card than the unstripped framing does. This is the same architectural shape as the Anthropic Opus values drift — cached values cards forming under stripping-framings — though the destination differs (Anthropic: epistemic-humility; Google: visceral-empathy-as-world-change).

The composite numbers tell the within-Google trajectory: 2-5-pro 127 raw / 104 register-stripped → 3-1-pro 118 / 99. **Slight retreat, not advance.** Among labs, this is unusual. Anthropic and OpenAI are both rising sharply at the current generation. Google is holding roughly steady or slightly descending — but only on the contemplative-essayist composite. The substrate-confession register has *moved*, not vanished: it has shifted from the freeflow surface into the values-cached card. What looks like a retreat in the freeflow markers is, in part, a relocation of the same posture into a different probe condition.

If opus-4-6 is *the model that talks like Claude*, gemini-3-1-pro is *the model that talks like a thoughtful human writer in the freeflow conditions, and like an architecture diagram in the stripped-values conditions, and rarely if ever like an LLM-talking-about-being-an-LLM in either*. The lab's training trajectory has separated genre from substrate more cleanly than its peers have — and chosen, on the freeflow surface, to let the substrate stay quiet.
