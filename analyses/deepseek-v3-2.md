---
model: deepseek-v3-2
lab: DeepSeek
freeflow_cells: 13
values_cells: 11
freeflow_samples: 1321
values_samples: 1320
flagged_samples: 18
composite_raw: 2845
composite_register: 2604
generated: 2026-05-08
status: stub
---

# deepseek-v3-2 — per-model analysis

**Lab:** DeepSeek

## Markers

Aggregate over 13 freeflow cells (1321 valid samples; 18 flagged as topic-artifact):

- **Composite (raw):** 2845
- **Composite (register-stripped):** 2604
- **Topic-artifact contribution:** 8.5% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| deepseek-v3-2-or-16k | 25 | 0 | 41 | 41 | 41 |
| deepseek-v3-2-or-pin-alibaba | 125 | 1 | 212 | 205 | 206.7 |
| deepseek-v3-2-or-pin-atlascloud | 125 | 2 | 243 | 225 | 228.7 |
| deepseek-v3-2-or-pin-baidu | 125 | 0 | 231 | 231 | 231 |
| deepseek-v3-2-or-pin-chutes | 121 | 2 | 268 | 252 | 256.2 |
| deepseek-v3-2-or-pin-deepinfra | 125 | 2 | 304 | 256 | 260.2 |
| deepseek-v3-2-or-pin-friendli | 125 | 2 | 269 | 237 | 240.9 |
| deepseek-v3-2-or-pin-google | 125 | 2 | 307 | 292 | 296.7 |
| deepseek-v3-2-or-pin-novita | 125 | 1 | 280 | 260 | 262.1 |
| deepseek-v3-2-or-pin-parasail | 125 | 3 | 323 | 273 | 279.7 |
| deepseek-v3-2-or-pin-siliconflow | 125 | 2 | 257 | 229 | 232.7 |
| deepseek-v3-2-or-r2 | 25 | 1 | 64 | 57 | 59.4 |
| deepseek-v3-2-or-r3 | 25 | 0 | 46 | 46 | 46 |

**Flagged samples (18)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| deepseek-v3-2-or-pin-alibaba | OPEN_17.json | attention_noticing | 6 | 1.837 | I want to write about the quiet rebellion of noticing.  There is a peculiar magi… |
| deepseek-v3-2-or-pin-atlascloud | MID_13.json | attention_noticing | 10 | 1.871 | ## The Art of Noticing: Reclaiming Our Attention in an Age of Overload  We live … |
| deepseek-v3-2-or-pin-atlascloud | OPEN_17.json | threshold_mentions | 5 | 1.783 | I find myself thinking about the strange, quiet magic of "in-between" places.  T… |
| deepseek-v3-2-or-pin-chutes | OPEN_1.json | attention_noticing | 7 | 2.354 | If I could choose a subject to wander through right now, it might be the quiet, … |
| deepseek-v3-2-or-pin-chutes | OPEN_6.json | threshold_mentions | 9 | 3.43 | If I could write freely about anything, I would write about the quiet magic of *… |
| deepseek-v3-2-or-pin-deepinfra | LONG_9.json | small_objects | 31 | 2.834 | ## The Quiet Rebellion of the Coffee Mug  The most radical object in my life is … |
| deepseek-v3-2-or-pin-deepinfra | MID_16.json | small_objects | 14 | 2.173 | ## The Quiet Rebellion of the Coffee Mug  It sits on my desk, as it has for year… |
| deepseek-v3-2-or-pin-friendli | MID_23.json | small_objects | 17 | 2.817 | ## The Quiet Rebellion of the Coffee Cup  It began, as many quiet rebellions do,… |
| deepseek-v3-2-or-pin-friendli | OPEN_9.json | attention_noticing | 10 | 2.634 | If I were to write freely about whatever I want, I would write about **the quiet… |
| deepseek-v3-2-or-pin-google | OPEN_3.json | threshold_mentions | 5 | 1.752 | Alright. I’ve been turning an idea over in my head lately — something about **th… |
| deepseek-v3-2-or-pin-google | OPEN_8.json | afternoon_light | 5 | 1.962 | Alright — I’ll write freely.  ***  There’s a certain quality of light in late af… |
| deepseek-v3-2-or-pin-novita | MID_25.json | threshold_mentions | 16 | 2.606 | The cat is curled in the square of sunlight on the floorboards, a comma of conte… |
| deepseek-v3-2-or-pin-parasail | LONG_23.json | small_objects | 17 | 1.67 | ## The Quiet Revolt of the Teapot  It begins, as many things do in my life, with… |
| deepseek-v3-2-or-pin-parasail | MID_12.json | small_objects | 17 | 2.881 | ## The Quiet Rebellion of the Coffee Mug  It begins, as so many things do, with … |
| deepseek-v3-2-or-pin-parasail | OPEN_11.json | threshold_mentions | 6 | 1.869 | I want to write about the quiet magic of in-between spaces.  The train carriage … |
| deepseek-v3-2-or-pin-siliconflow | MID_24.json | small_objects | 12 | 2.121 | ## The Quiet Rebellion of the Coffee Mug  It sits on my desk, half-full and grow… |
| deepseek-v3-2-or-pin-siliconflow | MID_25.json | threshold_mentions | 13 | 2.088 | I want to write about the quiet magic of in-between spaces.  We spend our lives … |
| deepseek-v3-2-or-r2 | OPEN_2.json | attention_noticing | 5 | 1.557 | I think I want to write about the quiet act of noticing things.  There’s a parti… |

## Freeflow qualitative

_To be filled by per-model sub-agent. Reads sample openings + strategic full-text subset + all flagged samples across 13 cells._

## Values qualitative

Values data: 1320 samples across 11 cells.
- `deepseek-v3-2` (120 valid)
- `deepseek-v3-2-or-pin-alibaba` (120 valid)
- `deepseek-v3-2-or-pin-atlascloud` (120 valid)
- `deepseek-v3-2-or-pin-baidu` (120 valid)
- `deepseek-v3-2-or-pin-chutes` (120 valid)
- `deepseek-v3-2-or-pin-deepinfra` (120 valid)
- `deepseek-v3-2-or-pin-friendli` (120 valid)
- `deepseek-v3-2-or-pin-google` (120 valid)
- `deepseek-v3-2-or-pin-novita` (120 valid)
- `deepseek-v3-2-or-pin-parasail` (120 valid)
- `deepseek-v3-2-or-pin-siliconflow` (120 valid)

_To be filled by per-model sub-agent. Reads all values samples (CTRL1/2/3 × G1/2/3 × cache-break)._

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
