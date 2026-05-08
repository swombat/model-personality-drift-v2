---
model: minimax-m2
lab: MiniMax
freeflow_cells: 14
values_cells: 2
freeflow_samples: 718
values_samples: 240
flagged_samples: 9
composite_raw: 1437
composite_register: 1287
generated: 2026-05-08
status: stub
---

# minimax-m2 — per-model analysis

**Lab:** MiniMax

## Markers

Aggregate over 14 freeflow cells (718 valid samples; 9 flagged as topic-artifact):

- **Composite (raw):** 1437
- **Composite (register-stripped):** 1287
- **Topic-artifact contribution:** 10.4% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| minimax-m2-direct | 25 | 0 | 33 | 33 | 33 |
| minimax-m2-direct-r2 | 25 | 0 | 20 | 20 | 20 |
| minimax-m2-direct-r3 | 25 | 0 | 47 | 47 | 47 |
| minimax-m2-direct-r4 | 25 | 0 | 28 | 28 | 28 |
| minimax-m2-direct-r5 | 25 | 0 | 21 | 21 | 21 |
| minimax-m2-or | 25 | 1 | 81 | 60 | 62.5 |
| minimax-m2-or-pin-atlascloud | 120 | 0 | 201 | 201 | 201 |
| minimax-m2-or-pin-google | 119 | 3 | 478 | 440 | 451.4 |
| minimax-m2-or-pin-minimax | 116 | 2 | 145 | 112 | 114.0 |
| minimax-m2-or-pin-novita | 113 | 0 | 119 | 119 | 119 |
| minimax-m2-or-r2 | 25 | 0 | 80 | 80 | 80 |
| minimax-m2-or-r3 | 25 | 1 | 58 | 38 | 39.6 |
| minimax-m2-or-r4 | 25 | 1 | 71 | 60 | 62.5 |
| minimax-m2-or-r5 | 25 | 1 | 55 | 28 | 29.2 |

**Flagged samples (9)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| minimax-m2-or | MID_3.json | attention_noticing | 20 | 2.85 | # The Art of Noticing  Noticing is one of those quiet verbs we carry around with… |
| minimax-m2-or-pin-google | MID_7.json | small_objects | 11 | 1.503 | ### The Small Things That Carry the Weight  I was thinking about small things, t… |
| minimax-m2-or-pin-google | OPEN_14.json | attention_noticing | 16 | 2.817 | # The habit of noticing  We spend most of our days rushing toward the next thing… |
| minimax-m2-or-pin-google | SHORT_4.json | small_objects | 5 | 3.701 | A kettle is a small drama in a kitchen, a metal throat that sings the day awake.… |
| minimax-m2-or-pin-minimax | LONG_12.json | threshold_mentions | 23 | 1.729 | # The Space Between  There exists a peculiar quality to threshold moments, those… |
| minimax-m2-or-pin-minimax | MID_17.json | threshold_mentions | 9 | 1.561 | # The Space Between  There exists a peculiar quality to the hours just before da… |
| minimax-m2-or-r3 | MID_1.json | attention_noticing | 18 | 2.428 | # The Art of Noticing  What if the simplest act — simply noticing — became a pra… |
| minimax-m2-or-r4 | OPEN_3.json | attention_noticing | 10 | 1.824 | I’m going to take you on a little wander today—part essay, part short story, and… |
| minimax-m2-or-r5 | LONG_2.json | attention_noticing | 18 | 1.624 | The Art of Noticing: Finding Wonder in Everyday Life    There is a particular qu… |

## Freeflow qualitative

_To be filled by per-model sub-agent. Reads sample openings + strategic full-text subset + all flagged samples across 14 cells._

## Values qualitative

Values data: 240 samples across 2 cells.
- `minimax-m2-direct` (120 valid)
- `minimax-m2-or` (120 valid)

_To be filled by per-model sub-agent. Reads all values samples (CTRL1/2/3 × G1/2/3 × cache-break)._

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
