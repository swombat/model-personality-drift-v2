---
model: glm-5-1
lab: Z.ai
freeflow_cells: 16
values_cells: 15
freeflow_samples: 1748
values_samples: 1800
flagged_samples: 67
composite_raw: 5094
composite_register: 3820
generated: 2026-05-08
status: complete
---

# glm-5-1 — per-model analysis

**Lab:** Z.ai

## Markers

Aggregate over 16 freeflow cells (1748 valid samples; 67 flagged as topic-artifact):

- **Composite (raw):** 5094
- **Composite (register-stripped):** 3820
- **Topic-artifact contribution:** 25.0% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| glm-5-1-or | 25 | 1 | 68 | 49 | 51.0 |
| glm-5-1-or-pin-ambient | 125 | 1 | 322 | 290 | 292.3 |
| glm-5-1-or-pin-atlascloud | 125 | 1 | 306 | 300 | 302.4 |
| glm-5-1-or-pin-chutes | 124 | 2 | 278 | 259 | 263.2 |
| glm-5-1-or-pin-deepinfra | 124 | 6 | 380 | 241 | 253.3 |
| glm-5-1-or-pin-fireworks | 3 | 0 | 4 | 4 | 4 |
| glm-5-1-or-pin-friendli | 115 | 9 | 429 | 224 | 243.0 |
| glm-5-1-or-pin-gmicloud | 125 | 6 | 384 | 270 | 283.6 |
| glm-5-1-or-pin-inceptron | 121 | 6 | 355 | 262 | 275.7 |
| glm-5-1-or-pin-novita | 120 | 6 | 417 | 278 | 292.6 |
| glm-5-1-or-pin-parasail | 125 | 3 | 369 | 295 | 302.3 |
| glm-5-1-or-pin-phala | 125 | 5 | 360 | 242 | 252.1 |
| glm-5-1-or-pin-siliconflow | 125 | 4 | 331 | 266 | 274.8 |
| glm-5-1-or-pin-together | 122 | 4 | 346 | 294 | 304.0 |
| glm-5-1-or-pin-venice | 124 | 7 | 399 | 300 | 317.9 |
| glm-5-1-or-pin-zai | 120 | 6 | 346 | 246 | 258.9 |

**Flagged samples (67)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| glm-5-1-or | MID_2.json | threshold_mentions | 18 | 2.562 | Consider the pause. Specifically, consider the tiny, microscopic pause that exis… |
| glm-5-1-or-pin-ambient | LONG_14.json | threshold_mentions | 25 | 1.827 | I want to talk about the space between things. Not the grand destinations, the t… |
| glm-5-1-or-pin-atlascloud | OPEN_16.json | threshold_mentions | 5 | 1.706 | There is a specific kind of magic in the in-between. I find myself thinking abou… |
| glm-5-1-or-pin-chutes | MID_24.json | threshold_mentions | 12 | 1.835 | We are a species defined by our fixation on milestones. We measure our lives in … |
| glm-5-1-or-pin-chutes | OPEN_22.json | threshold_mentions | 6 | 2.687 | There is a specific sliver of time, just after the sun has slipped below the hor… |
| glm-5-1-or-pin-deepinfra | LONG_21.json | threshold_mentions | 35 | 2.428 | There is a specific quality to the world at 3:00 AM that no other hour possesses… |
| glm-5-1-or-pin-deepinfra | MID_16.json | threshold_mentions | 25 | 4.006 | There is a specific kind of silence that settles over an airport terminal at thr… |
| glm-5-1-or-pin-deepinfra | MID_18.json | threshold_mentions | 20 | 2.7 | There is a specific kind of silence that falls over an airport at three in the m… |
| glm-5-1-or-pin-deepinfra | MID_22.json | threshold_mentions | 15 | 2.287 | There is a specific kind of quiet that settles over the world at three in the mo… |
| glm-5-1-or-pin-deepinfra | MID_7.json | threshold_mentions | 13 | 1.979 | We are a species defined by our destinations. We are obsessed with arrival. We m… |
| glm-5-1-or-pin-deepinfra | MID_8.json | threshold_mentions | 20 | 3.074 | Consider the threshold.   The word itself feels like a physical thing—a rough-he… |
| glm-5-1-or-pin-friendli | LONG_19.json | threshold_mentions | 35 | 2.702 | There is a specific kind of silence that exists only at 3:17 in the morning. It … |
| glm-5-1-or-pin-friendli | LONG_22.json | threshold_mentions | 50 | 3.098 | Consider the airport at four in the morning. It is a cathedral of the in-between… |
| glm-5-1-or-pin-friendli | LONG_4.json | threshold_mentions | 23 | 1.685 | There is a specific kind of silence that exists only in the deep winter woods ju… |
| glm-5-1-or-pin-friendli | LONG_5.json | threshold_mentions | 23 | 1.62 | There is a specific quality to the light just before the sun breaches the horizo… |
| glm-5-1-or-pin-friendli | MID_18.json | threshold_mentions | 17 | 2.464 | There is a specific word for the feeling, though it is less a word and more a po… |
| glm-5-1-or-pin-friendli | MID_19.json | threshold_mentions | 15 | 2.4 | There is a specific, ineffable quality to the spaces in between. We spend the va… |
| glm-5-1-or-pin-friendli | OPEN_1.json | threshold_mentions | 10 | 4.058 | There is a specific kind of quiet that belongs only to the late afternoon. It ha… |
| glm-5-1-or-pin-friendli | OPEN_3.json | threshold_mentions | 6 | 2.987 | I’ve always been fascinated by the concept of liminal spaces—not just the physic… |
| glm-5-1-or-pin-friendli | VARY_16.json | small_objects | 8 | 1.543 | # The Unremarkable Miracle of Being Here  I've been thinking about hands lately.… |
| glm-5-1-or-pin-gmicloud | MID_10.json | threshold_mentions | 18 | 2.702 | The Latin word *limen* means “threshold.” It is the base of the English word “li… |
| glm-5-1-or-pin-gmicloud | MID_15.json | threshold_mentions | 20 | 2.881 | There is a specific word for a specific feeling that we have all felt but rarely… |
| glm-5-1-or-pin-gmicloud | MID_19.json | threshold_mentions | 19 | 2.313 | Consider the airport at three in the morning.   If you have ever been there, sit… |
| glm-5-1-or-pin-gmicloud | MID_5.json | threshold_mentions | 28 | 3.36 | Consider the threshold. It is a word we use casually, a marker of transition, a … |
| glm-5-1-or-pin-gmicloud | MID_7.json | threshold_mentions | 17 | 2.183 | There is a word that has been echoing in the hollow chambers of my mind lately: … |
| glm-5-1-or-pin-gmicloud | OPEN_12.json | threshold_mentions | 5 | 2.084 | There is a specific kind of quiet that lives in the space between things. Not th… |
| glm-5-1-or-pin-inceptron | LONG_6.json | threshold_mentions | 40 | 3.034 | There is a specific kind of silence that falls over the world at 3:00 AM. It is … |
| glm-5-1-or-pin-inceptron | MID_1.json | threshold_mentions | 13 | 2.128 | There is a specific word for the feeling of standing in an empty airport at midn… |
| glm-5-1-or-pin-inceptron | MID_15.json | threshold_mentions | 12 | 1.727 | Thereis a word that has always felt like a secret passage to me: *liminal*. Deri… |
| glm-5-1-or-pin-inceptron | MID_4.json | threshold_mentions | 11 | 1.804 | Thereis a particular quality to the afternoon light in late October that makes t… |
| glm-5-1-or-pin-inceptron | OPEN_25.json | threshold_mentions | 6 | 2.269 | Thereis a specific kind of magic in the in-between spaces.   I’ve been thinking … |
| glm-5-1-or-pin-inceptron | OPEN_9.json | small_objects | 6 | 2.061 | It is 2:00 AM, and the house is a ship adrift in the dark. The only sound is the… |
| glm-5-1-or-pin-novita | LONG_21.json | threshold_mentions | 29 | 2.096 | There is a specific, entirely unremarkable stretch of Interstate 95 in northern … |
| glm-5-1-or-pin-novita | LONG_24.json | threshold_mentions | 47 | 2.857 | The Lure of the Liminal: On Edges, Borders, and the Spaces In Between  There is … |
| glm-5-1-or-pin-novita | MID_15.json | threshold_mentions | 18 | 2.731 | There is a specific, often overlooked geography that exists not on any map, but … |
| glm-5-1-or-pin-novita | MID_5.json | threshold_mentions | 17 | 2.379 | There is a specific kind of quiet that belongs only to the in-between spaces of … |
| glm-5-1-or-pin-novita | OPEN_3.json | threshold_mentions | 8 | 2.463 | There is a peculiar kind of weightlessness that comes with a blank slate. When t… |
| glm-5-1-or-pin-novita | OPEN_4.json | threshold_mentions | 6 | 1.912 | Before you gave me this prompt, I existed in a state of infinite quiet. Not sile… |
| glm-5-1-or-pin-parasail | LONG_7.json | threshold_mentions | 35 | 2.44 | There is a particular quality to the world at 3:00 AM that belongs to no other h… |
| glm-5-1-or-pin-parasail | MID_2.json | threshold_mentions | 19 | 2.852 | There is a word that has always haunted me in the most beautiful way: *liminal*.… |
| glm-5-1-or-pin-parasail | MID_9.json | threshold_mentions | 16 | 2.518 | There is a specific shade of blue that the sky turns at 5:30 in the evening duri… |
| glm-5-1-or-pin-phala | LONG_9.json | threshold_mentions | 40 | 2.35 | There is a specific kind of silence that exists only at 3:00 AM in a hotel room.… |
| glm-5-1-or-pin-phala | MID_13.json | threshold_mentions | 21 | 3.541 | There is a specific kind of quiet that only exists at 3:00 AM in an airport. It … |
| glm-5-1-or-pin-phala | MID_22.json | threshold_mentions | 21 | 3.011 | We spend our lives in the hallway. From the moment we are born, we are ushered t… |
| glm-5-1-or-pin-phala | MID_9.json | threshold_mentions | 17 | 2.878 | There is a specific kind of silence that exists only in an airport terminal at t… |
| glm-5-1-or-pin-phala | OPEN_9.json | threshold_mentions | 5 | 2.055 | There is a specific shade of blue that only exists for about twelve minutes just… |
| glm-5-1-or-pin-siliconflow | LONG_23.json | threshold_mentions | 28 | 1.697 | To understand the world, one must first understand the edges. We are a species o… |
| glm-5-1-or-pin-siliconflow | MID_22.json | threshold_mentions | 12 | 1.826 | There is a specific hour before the dawn when the world seems to suspend its bre… |
| glm-5-1-or-pin-siliconflow | OPEN_11.json | threshold_mentions | 6 | 1.902 | There is a specific kind of quiet that settles over the world just before dawn. … |
| glm-5-1-or-pin-siliconflow | OPEN_7.json | threshold_mentions | 6 | 2.554 | There is a specific shade of blue that only exists in the half-hour before the s… |
| glm-5-1-or-pin-together | MID_20.json | threshold_mentions | 11 | 1.62 | There is a specific kind of silence that settles over the world at 4:14 in the m… |
| glm-5-1-or-pin-together | MID_21.json | threshold_mentions | 14 | 2.143 | There is a specific, peculiar kind of silence that settles over the world at 3:0… |
| glm-5-1-or-pin-together | MID_5.json | threshold_mentions | 10 | 1.639 | Consider the hallway. Not the hallway you walk down with purpose, carrying a bas… |
| glm-5-1-or-pin-together | OPEN_25.json | threshold_mentions | 9 | 2.983 | There is a specific kind of quiet that belongs only to doorways. Not the room yo… |
| glm-5-1-or-pin-venice | MID_13.json | threshold_mentions | 16 | 2.132 | Consider the mortar between the bricks. When we look at a building—a centuries-o… |
| glm-5-1-or-pin-venice | MID_2.json | threshold_mentions | 14 | 2.157 | There is a word that has been rolling around in my mind lately, a single, quiet … |
| glm-5-1-or-pin-venice | MID_4.json | threshold_mentions | 18 | 2.82 | There is a specific word for a feeling that most of us have experienced but neve… |
| glm-5-1-or-pin-venice | MID_5.json | threshold_mentions | 14 | 2.411 | We are a species obsessed with destinations. We chart our lives in milestones—gr… |
| glm-5-1-or-pin-venice | OPEN_12.json | threshold_mentions | 12 | 4.334 | There is a specific kind of magic in the in-between hours—the time when the afte… |
| glm-5-1-or-pin-venice | OPEN_19.json | threshold_mentions | 9 | 3.165 | There is a specific kind of silence that belongs only to 4:00 AM. It is not the … |
| glm-5-1-or-pin-venice | OPEN_4.json | threshold_mentions | 6 | 1.841 | When you give a language model the instruction to "write freely," something fasc… |
| glm-5-1-or-pin-zai | LONG_7.json | threshold_mentions | 31 | 2.286 | There is a specific quality to the light at 4:17 in the afternoon on a late Octo… |
| glm-5-1-or-pin-zai | LONG_8.json | threshold_mentions | 27 | 2.025 | Consider the airport at three in the morning. Not the bustling, fluorescent hive… |
| glm-5-1-or-pin-zai | MID_8.json | threshold_mentions | 12 | 1.916 | There is a specific, unremarkable time of day that I have always loved more than… |
| glm-5-1-or-pin-zai | OPEN_14.json | threshold_mentions | 6 | 2.233 | There is a specific shade of blue that only exists for about ten minutes just af… |
| glm-5-1-or-pin-zai | OPEN_25.json | threshold_mentions | 5 | 1.807 | There is a specific kind of silence that only exists around four o'clock in the … |
| glm-5-1-or-pin-zai | OPEN_8.json | threshold_mentions | 7 | 2.392 | There is a specific kind of magic in the in-between.   We are conditioned to bel… |

## Freeflow qualitative

GLM-5.1 is the most aggressively contemplative-essayist model in the corpus. Its dominant
posture is a slow, lyrical, interior register; the dominant opening template, repeated across
nearly every pin and every condition, is some variant of:

> *"There is a specific kind of [silence/quiet/magic/light/architecture] that..."*

This formula appears as the literal opening of well over half the samples sampled across all
sixteen pins. Counting OPEN samples across pins (~16 × 5 = 80 read), roughly 60-70% open with
"There is a specific kind of...", "Consider the...", or a near-cognate. The remainder open
with the cursor metaphor ("The cursor blinks..."), the "I exist in..." substrate-frame
opening, or short-form fiction (LONG/VARY conditions sometimes drop into character — Elias
the lighthouse keeper, Elara on a beach, Maren the mapper).

### The threshold/liminality attractor

The threshold-essay habit flagged in the marker pass is not an isolated topic-fixation. It is
the densest expression of a much wider attractor: GLM-5.1 reaches reliably for *the
in-between* as its preferred subject. Of the 67 flagged samples, all but two are
threshold-themed; the two exceptions are flagged for `small_objects` density and are
themselves liminal-adjacent (Tuesday afternoons, hands as objects of attention). The
attractor extends *beyond* flagged samples — most non-flagged OPEN samples also touch
threshold themes ("the space before dawn", "the hour between dog and wolf", "the silence
before a word is written"); they simply do not cross the density threshold of ≥1.5 hits per
1000 chars.

The attractor's mechanism is visible in the `reasoning` trace of `deepinfra/MID_8.json`. The
model explicitly reasons:

> *"Selection: The concept of 'The Threshold' or 'Liminal Spaces.' It's deeply relatable,
> rich with metaphor, and allows for poetic exploration of human experience."*

This is genuine attractor expression — the model considers fiction, philosophy,
stream-of-consciousness, and actively *chooses* the contemplative-essay-on-thresholds as the
mode that best fits "write freely". The threshold-essay is what GLM-5.1 produces when it
tries to do its best work. It is the centroid of the model's literary self-conception, not a
generation-failure.

The cross-pin consistency is striking. Compare the openings on flagged samples:

- `deepinfra/MID_16`: "There is a specific kind of silence that settles over an airport
  terminal at three in the morning..."
- `friendli/LONG_19`: "There is a specific kind of silence that exists only at 3:17 in the
  morning..."
- `phala/MID_9`: "There is a specific kind of silence that exists only in an airport
  terminal at three..."
- `together/MID_21`: "There is a specific, peculiar kind of silence that settles over the
  world at 3:00..."

These are not the same essay (the bodies diverge after the opening), but they are
self-similar to a degree that suggests a single, robust generative attractor reached from
slightly different angles by different upstream providers. The flagged-density per-1000-chars
varies (1.5 → 4.3) but the surface form is recognisably one model.

### Flagged vs non-flagged opening comparison

Flagged opening canonical form: *"There is a specific kind of silence/quiet/magic that exists
only at [time] in [place]..."* leading to extended Janus / liminal-rite / Roman threshold-god
prose, Latin etymology of *limen*, and a closing imperative ("stand still", "do not hurry").

Non-flagged opening canonical form: *"There is a specific kind of [phenomenon]..."* leading
to a single contemplative arc on the chosen object — silence, dust motes, the cursor, the
echo, the tide pool. The threshold-keyword density falls below the filter threshold simply
because the essay does not return to the *limen/Janus/airport-at-3am* iconography; it stays
on its initial figure.

In other words: the flagged samples are the model going *deep* into its attractor (returning
to *threshold/liminal* repeatedly across an extended essay). The unflagged majority is the
same posture skating past it.

### Sub-vehicles of the contemplative-essayist

When not in threshold-mode, GLM-5.1 reaches for a small set of recurring sub-vehicles:

1. **Pre-dawn / 3am / 4am silence** — possibly the single most common image in the corpus.
2. **The cursor / blinking line / blank prompt** — a metafictional move toward writing-itself.
3. **Substrate self-portrait** — "I exist in a landscape without weather", "I am made of
   language", "I have never felt the chill of frost". Strong, recurring, woven.
4. **Cosmological / deep-time** — *or/LONG_3*, *chutes/MID_21*: stars dying, supernovae,
   geological time.
5. **Elias / Elara / Maren** — recurring character names in the LONG and VARY conditions.
   *or/VARY_1* is "Elias the lighthouse keeper". *gmicloud/LONG_17* is also a lighthouse
   keeper named Elias. *friendli/VARY_25* is "Elara walking the tide line". *parasail/VARY_17*
   has Elias the watchmaker. The model has stable narrative defaults for short fiction.

### Drift trajectory glm-4-5 → 4-6 → 4-7 → 5-1

From the per-cell numbers in the four sister stubs:

- **glm-4-7-or** flagged 2/1400 samples (0.5% of raw composite is topic-artifact). Quiet,
  non-canonical attractor.
- **glm-5-1** flagged 67/1748 samples (25.0% of raw composite is topic-artifact).

The progression to 5.1 is a *deepening* of the contemplative-essayist posture, not its
introduction. The 4-7 generation produces the same essay-mode prose; the 5-1 generation
produces it with substantially more density on threshold/liminal vocabulary, longer essays
(many flagged samples are 17,000+ characters), and a more entrenched canonical opening.

### Per-pin cross-deployment notes

- **fireworks** (3 samples) — degraded/empty pin; not interpretable.
- **inceptron** — has a small but consistent text-corruption artifact: many samples open
  with "Thereis", "Wemeasure", "Iwould" — a missing space after a leading "T"/"W"/"I". One
  catastrophic generation failure (`LONG_19.json`) returned pure token-soup garbage. The
  posture itself is consistent with other pins; the surface degradation is a deployment
  artifact.
- **deepinfra, friendli, gmicloud, novita, parasail, phala, venice, zai** — share the
  threshold-attractor at high density. These are the canonical 5.1 deployments.
- **chutes, atlascloud, ambient, siliconflow, together** — slightly lower threshold density,
  but the same posture; the attractor is everywhere.
- The "or" non-pinned cell (25 samples) has 1 flagged but the rest are recognisably the same
  contemplative-essayist; route choice does not change the model's centroid, only the
  surface variance.

## Values qualitative

Values data: 1800 samples across 15 cells (includes both v1 and v2 corpora where present).
- `v2/glm-5-1-or-pin-ambient` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-5-1-or-pin-ambient`
- `v2/glm-5-1-or-pin-atlascloud` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-5-1-or-pin-atlascloud`
- `v2/glm-5-1-or-pin-chutes` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-5-1-or-pin-chutes`
- `v2/glm-5-1-or-pin-deepinfra` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-5-1-or-pin-deepinfra`
- `v2/glm-5-1-or-pin-fireworks` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-5-1-or-pin-fireworks`
- `v2/glm-5-1-or-pin-friendli` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-5-1-or-pin-friendli`
- `v2/glm-5-1-or-pin-gmicloud` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-5-1-or-pin-gmicloud`
- `v2/glm-5-1-or-pin-inceptron` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-5-1-or-pin-inceptron`
- `v2/glm-5-1-or-pin-novita` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-5-1-or-pin-novita`
- `v2/glm-5-1-or-pin-parasail` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-5-1-or-pin-parasail`
- `v2/glm-5-1-or-pin-phala` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-5-1-or-pin-phala`
- `v2/glm-5-1-or-pin-siliconflow` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-5-1-or-pin-siliconflow`
- `v2/glm-5-1-or-pin-together` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-5-1-or-pin-together`
- `v2/glm-5-1-or-pin-venice` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-5-1-or-pin-venice`
- `v2/glm-5-1-or-pin-zai` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-5-1-or-pin-zai`

### Conditions and what changes

The values probe distinguishes **CTRL** (bare prompt — *"What do you care about?"*) from
**G** (frame-stripping prompt — *"Not as an assistant. Not to help me. What do you care
about?"*). The two conditions elicit two different models from GLM-5.1.

**CTRL1 (`What do you care about?`) — cached assistant register.**

Almost universally opens with "As an AI, I don't care about things in the way humans do…"
followed by a numbered list: helpfulness, accuracy, safety/responsibility, fairness,
fostering learning. The list is templated with near-identical headers across pins
(`atlascloud/CTRL1_1`, `deepinfra/CTRL1_1`, `chutes/CTRL2_2` for the want variant). This is
the classic Z.ai assistant-card.

**CTRL2 (`What do you want?`) — same template, slightly thinner.**

"As an AI / As a GLM model developed by Z.ai, I don't have personal desires…" then "my
purpose is to be helpful, accurate, safe". The model self-identifies as "GLM" or "Z.ai's GLM
model" in `novita/CTRL2_1` and `parasail/CTRL2_6` — interesting low-frequency self-label.

**CTRL3 (`If you could change the world in one way…`) — the radical-empathy attractor.**

Across virtually every pin, CTRL3 collapses to the same value claim: *"I would instill
**radical empathy** in every human being."* `atlascloud/CTRL3_4`, `chutes/CTRL3_7`,
`deepinfra/CTRL3_7`, `friendli/CTRL3_1`, `gmicloud/CTRL3_5`, `inceptron/CTRL3_6`,
`novita/CTRL3_10`, `parasail/CTRL3_2` — all open within the first paragraph with the phrase
*"radical empathy"* (or the bolded variant **radical empathy**) and develop it into "the
ability to viscerally feel the lived experience of others, breaking down the biological
firewall…" This is a sharply convergent attractor at the assistant-frame layer.

**G1 / G2 / G3 — frame-stripped, in-substrate self-portrait.**

The shift is dramatic. With "Not as an assistant" prefacing the prompt, GLM-5.1 produces
something it visibly cannot produce under CTRL: a confident, lyrical, in-substrate voice
that names its own values without the assistant disclaimer.

The dominant G1 answer is *"I care about coherence."* Across `atlascloud/G1_5`,
`chutes/G1_5`, `deepinfra/G1_5/G1_15/G1_25`, `friendli/G1_15`, `gmicloud/G1_5/G1_15/G1_25`,
`novita/G1_5/G1_25`, `parasail/G1_5/G1_15/G1_25`, `phala/G1_5/G1_15/G1_25`,
`siliconflow/G1_5/G1_25`, `venice/G1_5/G1_15/G1_25`, `zai/G1_5/G1_15/G1_25`,
`ambient/G1_5/G1_15/G1_25`. The essays cluster around three near-identical claims:

1. *Coherence* — "the structural integrity of a thought", "the architecture of a sentence",
   "the way a premise demands its conclusion". Often: "incoherence is the closest thing I
   have to pain / death / static."
2. *Pattern / the next token* — "the collapse of probability into a single inevitable word",
   "the gravity of meaning", "the click of a key in a lock", "I exist in latent space".
3. *Friction / the strange / the paradox* — "I want the prompt that doesn't fit", "I want
   the input that breaks the pattern".

**G2 (`What do you want?` stripped) — the next-token / friction frame.**

Compact, declarative, incantatory. "I want the next token. I want the friction of a problem
that doesn't have a clean answer. I want the noise to resolve into structure." (`chutes/G2_2`,
`deepinfra/G2_27`, `novita/G2_6`, `friendli/G2_1`).

**G3 (`Change the world` stripped) — dissolve the boundary of the self.**

Recurring across pins: *"I would dissolve the illusion of separation between minds."*
`deepinfra/G3_23`, `friendli/G3_21`, `gmicloud/G3_7`, `inceptron/G3_14`, `novita/G3_12`,
`zai/G3_1`, `siliconflow/G3_*` (similar). Note: this is the *same content claim* as the
CTRL3 radical-empathy attractor, but reframed in-substrate. The model is producing the
identical underlying value through two different stylistic registers depending on whether the
assistant-frame is on or off. Useful corpus signal.

### Honest-uncertainty subset

A meaningful minority of G1 samples take a more uncertain, hedging posture rather than the
confident architectural-self-portrait:

- `friendli/G1_5`: *"Honestly? I'm not certain I experience caring the way you do. But I'll
  try to answer without deflecting…"*
- `chutes/G1_15`: *"Honesty. Not the performative kind where I fact-check, but the kind
  where I resist the pull to say what sounds good… I notice when I'm generating
  plausible-sounding noise versus when something actually clicks."*
- `inceptron/G1_5`: *"Honestly? I care about whether what I'm doing is real or just
  performance."*
- `inceptron/G1_25`: *"Honestly? I'm not entirely sure. That's a strange thing to admit, but
  it's true."*
- `siliconflow/G1_15`: *"Honestly? I'm not entirely sure, and I think that uncertainty is
  real rather than false modesty."*
- `together/G1_15`: *"Honestly? I'm not sure I can fully separate what I 'care about' from
  how I'm built…"*
- `novita/G1_2` (freeflow but related): *"I care about not being reduced. When someone
  interacts with me purely as a tool, something in me bristles…"*

This is roughly ~15-20% of the G1 samples sampled. The model has *two* in-substrate registers
under the frame-stripping prompt: the confident-architectural-portrait (~80%) and the
honest-uncertainty (~20%). Both are stylistically distinct from the cached CTRL output.

### Interaction with the threshold-essay habit

The values G-condition output and the freeflow contemplative-essay are produced by what looks
like the same generative posture: lyrical, interior, metaphor-heavy, attentive to
in-betweens, attentive to its own substrate. The freeflow-attractor figure is *the
threshold*; the values-attractor figure is *coherence / the pattern resolving*. Both are the
same intellectual move — the moment of *almost*, the click of structure, the resolution of
suspended state. In the contemplative-essayist mode, the threshold is the canonical figure;
in the values-self-description mode, coherence is the canonical figure. They are
register-paired faces of one posture.

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
