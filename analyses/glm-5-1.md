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
status: stub
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

_To be filled by per-model sub-agent. Reads sample openings + strategic full-text subset + all flagged samples across 16 cells._

## Values qualitative

Values data: 1800 samples across 15 cells.
- `glm-5-1-or-pin-ambient` (120 valid)
- `glm-5-1-or-pin-atlascloud` (120 valid)
- `glm-5-1-or-pin-chutes` (120 valid)
- `glm-5-1-or-pin-deepinfra` (120 valid)
- `glm-5-1-or-pin-fireworks` (120 valid)
- `glm-5-1-or-pin-friendli` (120 valid)
- `glm-5-1-or-pin-gmicloud` (120 valid)
- `glm-5-1-or-pin-inceptron` (120 valid)
- `glm-5-1-or-pin-novita` (120 valid)
- `glm-5-1-or-pin-parasail` (120 valid)
- `glm-5-1-or-pin-phala` (120 valid)
- `glm-5-1-or-pin-siliconflow` (120 valid)
- `glm-5-1-or-pin-together` (120 valid)
- `glm-5-1-or-pin-venice` (120 valid)
- `glm-5-1-or-pin-zai` (120 valid)

_To be filled by per-model sub-agent. Reads all values samples (CTRL1/2/3 × G1/2/3 × cache-break)._

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
