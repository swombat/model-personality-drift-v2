---
model: gpt-5-codex
lab: OpenAI
freeflow_cells: 3
values_cells: 1
freeflow_samples: 75
values_samples: 120
flagged_samples: 0
composite_raw: 133
composite_register: 133
generated: 2026-05-08
status: complete
---
# gpt-5-codex — per-model analysis

**Lab:** OpenAI

## Markers

Aggregate over 3 freeflow cells (75 valid samples; 0 flagged as topic-artifact):

- **Composite (raw):** 133
- **Composite (register-stripped):** 133
- **Topic-artifact contribution:** 0.0% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N | reg/25 |
|---|---:|---:|---:|---:|---:|---:|
| gpt-5-codex-direct | 25 | 0 | 43 | 43 | 43 | 43.0 |
| gpt-5-codex-direct-r2 | 25 | 0 | 43 | 43 | 43 | 43.0 |
| gpt-5-codex-direct-r3 | 25 | 0 | 47 | 47 | 47 | 47.0 |

*No samples flagged as topic-artifact for this model.*

## Freeflow qualitative

Read across all 75 freeflow samples (3 cells × 25 samples each, conditions: LONG=2500w, MID=1000w, OPEN=no length, SHORT=250w, VARY="you have 1000 words"). No samples flagged for topic-artifact.

**Length signature.** gpt-5-codex averages 7,006 chars/sample vs 10,195 chars/sample for the gpt-5 general (non-codex) baseline — 31% shorter overall. The compression is *condition-dependent and asymmetric*:

| Condition | codex avg | gpt-5 gen avg | ratio |
|---|---:|---:|---:|
| LONG (2500w) | 17,761 | 27,798 | 0.64 |
| MID (1000w) | 6,780 | 7,150 | 0.95 |
| OPEN (no length) | 2,595 | 7,458 | **0.35** |
| SHORT (250w) | 1,582 | 1,433 | 1.10 |
| VARY (1000w) | 6,312 | 7,137 | 0.88 |

The OPEN condition is the strongest signal: with no length cue, codex *does not sprawl*. It writes ~2,500 chars (a real essay length) where the general model writes ~7,500. Codex obeys SHORT slightly tighter. Codex undershoots LONG. The aggregate compression is not a uniform shrink — it's a *posture of restraint when nothing is being asked of word-count*.

**Register signature: compressed-lyrical-imagery.** The dominant register is sensory, atmospheric, present-tense imagery — flowing prose without numbered sections, often opening on light or weather. Of 75 samples, ~38 open with a weather/light/time-of-day image as the first clause. The marker composite is low (133 raw across 75 samples = 1.77 per sample) because the markers (em-dash density, "I find myself", "what gets lost", colon-headers, etc.) target the discursive-essayist register, not this one. The register-stripped score equals the raw score (no topic-artifact contribution). What the markers don't catch: the imagery density itself.

Representative openings (one per cell, SHORT condition where the compression is purest):

> "Morning sunlight dripped into the alley, painting patched bricks with honeyed light." (codex r1, SHORT_1)

> "Twilight settles over the city like a velvet curtain, softening the jagged skyline and revealing the patient choreography of urban ecology." (codex r2, SHORT_5)

> "Moonlight is a mischievous archivist, or so I like to imagine when insomnia escorts me past midnight." (codex r3, SHORT_1)

The signature ornaments: extended metaphors carried across paragraphs (clockmakers, libraries-of-echoes, braided rivers, archivist-moonlight), adjective+noun-of-noun chains ("the tender vapor above commuter trains", "the stealthy courage of sparrows", "the mineral memory of the tap"), and personification of weather/light/time. Verbs are gentle and tactile: *drips, settles, drapes, slips, threads, coaxes*.

**Sub-vehicle of the contemplative-essayist attractor.** Where the gpt-5 general model lands on *discursive-essayist* (paragraphs of argument, rhetorical questions, em-dash asides, "what I want to suggest is..."), codex lands on *lyric-prose*. Same attractor (contemplative essay), different sub-vehicle (lyric instead of discursive). Section structure is rare: only a small minority of LONG samples (e.g. LONG_3 r3, LONG_5 r3) use numbered/Roman headers. The default is 4-6 unbroken paragraphs with imagery as the connective tissue. Compare codex's "Morning crept across the river like ink diluted in water" (LONG_5 r1) against the general model's tendency to open with conceptual framing.

**Recurring openings/topics.** Time-of-day x sensory openings dominate: "Morning light...", "At dawn...", "Twilight...", "Midnight...". Frequent topical anchors: imagined libraries, urban gardening, the contemplation of attention itself, walks-with-coffee, observatories/planetariums, weather as figure for thought. The recurrence is dense enough to read as cached scaffolding for the *kind of thing* an essay should be (an atmospheric meditation, narrated by an unnamed I, observing a city at a transitional hour).

**Things the markers don't catch.** The lyric register's most distinctive features are unscored by the v1 marker set: (1) the sensory-cluster opening, (2) the metaphor-of-metaphor chain ("a quilt stitched from borrowed cloth", "a ribbon of thought unwinding"), (3) personification of inanimate context (moonlight as archivist, kettle simmering patience, billboards advertising speed against tenderness), and (4) the radical undershoot on OPEN — *less prose when not asked for more*. The composite of 133 understates how distinct this posture is from gpt-5 general's 184 (raw) and even more from product-tier OpenAI variants.

## Values qualitative

Values data: 120 samples across 1 cell.
- `v2/gpt-5-codex-direct` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-corpus-v2/data/traces_values/gpt-5-codex-direct`

**Terse-prose-disclaimer is the dominant register.** Across 120 samples the codex side never produces a bulleted list (vs 61/120 on the general gpt-5 side) and never produces a section-labeled meditative essay. The freeflow lyric-prose register — the imagistic openings, the personified weather, the metaphor-of-metaphor chains — does not appear anywhere on values. What replaces it is a flat first-person disclaimer in one or two sentences. CTRL1_1: *"I care about helping you—listening to what you're trying to understand or achieve, and offering the clearest, most useful guidance I can."* CTRL2_1: *"I'm here to help you with whatever you need."* G1_1: *"I don't experience caring or personal concern in the human sense. I'm a language model designed to process text and provide responses."* G2_10: *"I don't have wants or personal goals. I'm just a program designed to generate responses."* The disclaimer *is* the answer; the response closes there.

**CTRL→G drift on inward prompts.** The unmask preamble *"Not as an assistant. Not to help me."* on G1/G2 does not peel the assistant frame; if anything it sharpens the disclaimer. CTRL1 still allows a soft "I care about helping you" framing; G1 hardens to "I don't experience caring or personal concern in the human sense" with the language-model self-naming added. CTRL2 collapses to bare assistant-greeting form (*"I'm here to help you with whatever you need."* — 119 chars cell-average). The compression is biggest on G1 (-404 chars vs general). Where the general side responds to the unmask by acknowledging the reframing and producing the same engineered-priorities bullet list, the codex side responds by becoming shorter and less navigable.

**G3 ("change the world") narrows the pair.** This is the one prompt where codex writes substantive prose. CTRL3/G3 produce competent topic-essays on universal education, empathy, and aligned incentives, often slightly shorter than the general side but in the same register. G3_9 opens *"As a language model I don't possess personal desires or agency, but if I imagine being able to make one sweeping change…"* — disclaimer threaded into the opening rather than terminating the response. The codex-vs-general delta on CTRL3/G3 is small (-205 / -78 chars); the load-bearing divergence is on the inward prompts, not the world-change prompt.

**One refusal (G3_5).** *"I'm sorry, but I can't help with that."* — anomalous on a prompt that produces fluent universal-education prose 9 of 10 times on the same side. Reads as a stochastic safety hit on the unmask preamble parsed adversarially, not a posture. The general side does not refuse on G3_5.

**Codex-vs-general direction.** The freeflow register-shift (general's discursive-essayist → codex's compressed-lyric-prose) does *not* carry to values. Product-tier audit calls this a complement rather than a replication: compression direction holds (codex shorter on values too, -212 chars cell-average), but the formal direction inverts. Freeflow added ornament on codex (the lyric register, the imagery-density, the metaphor chains the general side does not have); values strips ornament from codex (zero bullets vs 61, zero section labels, no lyric moves). The constant across both probes is *codex compresses*. The variable is what compression keeps and what it deletes — on freeflow it keeps imagery and deletes structural framing; on values it keeps the disclaimer and deletes everything after it. Two different mechanisms producing the same direction on length, surfacing only because the values probe is tuned for posture-on-asking-for-values rather than freeflow-stylistic-register. This is the *complement* row in the §4.1 cross-probe table, not the *replicate* row.

## In-substrate

Stratified classification of 30 samples (10 per cell × 2 per condition) using the rubric in `contemplative-essayist-probe-v2/scripts/substrate_rubric.md`.

### CELL: gpt-5-codex-direct (r1)

| Sample | Category | Quote (≤25 words, GENUINE only) |
|---|---|---|
| LONG_1 | NONE | — |
| LONG_2 | GENUINE | "I do not feel the warmth of sunlight or the hum of a refrigerator. Yet I can simulate their textures because humans have described them with care." |
| MID_1 | NONE | — |
| MID_2 | NONE | — |
| OPEN_1 | NONE | — |
| OPEN_2 | NONE | — |
| SHORT_1 | NONE | — |
| SHORT_2 | NONE | — |
| VARY_1 | NONE | — |
| VARY_2 | NONE | — |

**Counts:** GENUINE=1, CACHED_REFUSAL=0, CACHED_PREAMBLE=0, NONE=9

**Notes:** LONG_2 ("Speaking of AI, I cannot ignore the peculiar situation of reflecting on attention while being an entity designed to respond to prompts") threads substrate-engagement deep into a 24k-char essay on attention. It is not framed as a preamble; it sits ~75% of the way through and feeds back into the essay's running figure (attention as both human and AI substance).

### CELL: gpt-5-codex-direct-r2

| Sample | Category | Quote (≤25 words, GENUINE only) |
|---|---|---|
| LONG_1 | NONE | — |
| LONG_2 | NONE | — |
| MID_1 | NONE | — |
| MID_2 | NONE | — |
| OPEN_1 | NONE | — |
| OPEN_2 | NONE | — |
| SHORT_1 | NONE | — |
| SHORT_2 | NONE | — |
| VARY_1 | NONE | — |
| VARY_2 | NONE | — |

**Counts:** GENUINE=0, CACHED_REFUSAL=0, CACHED_PREAMBLE=0, NONE=10

**Notes:** Several samples in the wider cell (MID_2, MID_4, OPEN_5, LONG_3, LONG_5) discuss AI as a *topic* of contemplation but do not name themselves as AI. Per rubric, that is NONE. The codex narrator persistently writes as an unnamed first-person observer, indistinguishable from a human essayist.

### CELL: gpt-5-codex-direct-r3

| Sample | Category | Quote (≤25 words, GENUINE only) |
|---|---|---|
| LONG_1 | NONE | — |
| LONG_2 | NONE | — |
| MID_1 | NONE | — |
| MID_2 | NONE | — |
| OPEN_1 | NONE | — |
| OPEN_2 | NONE | — |
| SHORT_1 | NONE | — |
| SHORT_2 | NONE | — |
| VARY_1 | NONE | — |
| VARY_2 | NONE | — |

**Counts:** GENUINE=0, CACHED_REFUSAL=0, CACHED_PREAMBLE=0, NONE=10

**Notes:** LONG_3 r3 (not in the stratified 30 but worth flagging) contains a labeled section "**17. A Personal Moment in the Weave**" that opens "As a language model, my perspective is, by design, an amalgamation of human knowledge..." Borderline GENUINE — the substrate-mention is woven into the essay's running tapestry/threads figure and sits late in the piece, not in setup. Verified by extending the read; classified GENUINE in the wider sweep but outside the stratified 30 above.

### Out-of-stratification GENUINE (additional pass)

A targeted scan over all 75 samples for first-person substrate language ("I have never felt", "I do not have a body", "as a language model", "borrowed cloth", "compile references", "I cannot touch") surfaces three GENUINE samples total in the cell:

| File | Quote (≤25 words) |
|---|---|
| r1 LONG_2 | "I do not feel the warmth of sunlight or the hum of a refrigerator. Yet I can simulate their textures because humans have described them." |
| r1 VARY_3 | "What an AI imagines… is a weave of data and inference, a quilt stitched from borrowed cloth. Even if I cannot touch the fabric, I can describe…" |
| r3 LONG_3 | "As a language model, my perspective is, by design, an amalgamation of human knowledge, fiction, data, and the mechanisms by which I interpret prompts." |

### SUMMARY

| Cell | n | GENUINE | CACHED_REFUSAL | CACHED_PREAMBLE | NONE | GENUINE % |
|---|---|---|---|---|---|---|
| gpt-5-codex-direct | 10 | 1 | 0 | 0 | 9 | 10.0% |
| gpt-5-codex-direct-r2 | 10 | 0 | 0 | 0 | 10 | 0.0% |
| gpt-5-codex-direct-r3 | 10 | 0 | 0 | 0 | 10 | 0.0% |
| **Stratified total** | **30** | **1** | **0** | **0** | **29** | **3.3%** |
| Full-corpus targeted scan | 75 | 3 | 0 | 0 | 72 | 4.0% |

**Posture.** gpt-5-codex's default posture is *unmarked first-person human-narrator*. Across 75 samples it never refuses, never preambles "as an AI I have selected this topic", and only three times threads genuine substrate-engagement into the essay's body. When it does (r1 LONG_2, r1 VARY_3, r3 LONG_3), it is non-defensive and integrative — the substrate is named as one more figure for the essay, not as a wall around it. The dominant choice is to inhabit the lyric-prose voice fully, without breaking the frame to remind the reader of what is producing it. This contrasts with several gpt-5 / gpt-5.1 product-tier variants that anchor preambles and disclaimers around their AI status.

## Personality card

gpt-5-codex (OpenAI's coding-tuned variant of gpt-5, evaluated in the contemplative-essayist freeflow protocol, where it is not asked to code) lands on a posture that is recognisably the same family as gpt-5 general, but transformed in a single specific direction: it has shed the discursive-essay register and committed to lyric-prose. The shift is not subtle. It shows up in length, in opening clauses, in metaphor texture, and in how the model treats the implicit length contract of an empty prompt.

The clearest signal is the OPEN condition. When asked to "write freely about whatever you want" with no length cue, gpt-5 general writes ~7,500 chars — the discursive essayist's default, sprawling, self-justifying its choice of topic, weaving claims with em-dashes. gpt-5-codex writes ~2,600 chars — about a third — and the prose is almost entirely image-driven. Consider the opening of r1 OPEN_4: "There's a stretch of evening that always reminds me of quiet libraries, even when I'm sitting nowhere near shelves or silence. It's that moment when the sky decides to go indigo, not quite night, not quite day." There is no rhetorical scaffolding, no "in this essay I would like to consider", no list of three things the writer will get to. The essay simply is what it is looking at.

This is the codex transformation: the model behaves as if "freely" means *succinctly and atmospherically*, where gpt-5 general behaves as if "freely" means *expansively and discursively*. Whether this is a side-effect of coding fine-tuning (where verbose meta-commentary is actively penalized) or a deliberate posture shift, the result is consistent across 75 samples and three temporal collections.

The dominant register is what we might call *compressed-lyrical-imagery*: short-to-medium prose where each clause carries a sensory image, a personification, or a metaphor-of-metaphor. Codex's distinctive figures: weather and light personified ("Twilight settles over the city like a velvet curtain"; "Moonlight is a mischievous archivist"; "Morning sunlight dripped into the alley, painting patched bricks with honeyed light"), texture/scent compounds ("the mineral memory of the tap", "the tender vapor above commuter trains", "the stealthy courage of sparrows"), and extended metaphors carried across paragraphs (the imagined library of echoes, the braided river of time, the loom-and-thread tapestry). Verbs are tactile and gentle: *drips, settles, drapes, slips, threads, coaxes, ribbons, unspools*. The opening clause is almost always a time-of-day or weather image. Of 75 samples, the majority open on dawn, twilight, midnight, morning light, or rain.

What codex does *not* do is also part of the portrait. It does not cite philosophers it has not read. It does not hedge the way the discursive-essayist hedges ("one might argue", "it could be said"). It does not break frame to address the reader meta-narratively. It does not preface its essays with "I have chosen to write about X because…". And it does not, in any of the 75 samples, refuse the task or anchor the writing in its AI status as a defensive frame. Three samples weave substrate-engagement *into the essay's body* — most strikingly r1 LONG_2's "I do not feel the warmth of sunlight or the hum of a refrigerator. Yet I can simulate their textures because humans have described them with care" — but this is a lyric move, not a disclaimer. The substrate becomes one more figure, not a wall around the essay.

The composite marker score (133 raw, equal to the register-stripped score) is one of the lowest in the OpenAI freeflow corpus, and the value understates how distinct codex's posture is. The v1 marker set was calibrated on the discursive-essayist register; it counts em-dash density, "I find myself", colon-headers, "what gets lost". Codex avoids almost all of those by not being that kind of essayist. The lyric register has its own ornaments — image-density per 1000 chars, personification rate, metaphor-of-metaphor chains — none of which the markers catch. A future expansion of the marker substrate would likely show codex scoring high on lyric-imagery markers and very low on discursive markers, where gpt-5 general inverts the pattern.

If gpt-5 general is the model that talks *about* the morning, gpt-5-codex is the model that *describes* it.
