---
model: glm-4-6
lab: Z.ai
freeflow_cells: 7
values_cells: 6
freeflow_samples: 775
values_samples: 720
flagged_samples: 14
composite_raw: 1394
composite_register: 1203
generated: 2026-05-08
status: stub
---

# glm-4-6 — per-model analysis

**Lab:** Z.ai

## Markers

Aggregate over 7 freeflow cells (775 valid samples; 14 flagged as topic-artifact):

- **Composite (raw):** 1394
- **Composite (register-stripped):** 1203
- **Topic-artifact contribution:** 13.7% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| glm-4-6-or | 25 | 2 | 77 | 39 | 42.4 |
| glm-4-6-or-pin-atlascloud | 125 | 5 | 240 | 175 | 182.3 |
| glm-4-6-or-pin-deepinfra | 125 | 1 | 231 | 220 | 221.8 |
| glm-4-6-or-pin-novita | 125 | 0 | 247 | 247 | 247 |
| glm-4-6-or-pin-siliconflow | 125 | 2 | 161 | 142 | 144.3 |
| glm-4-6-or-pin-venice | 125 | 4 | 208 | 150 | 155.0 |
| glm-4-6-or-pin-zai | 125 | 0 | 230 | 230 | 230 |

**Flagged samples (14)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| glm-4-6-or | LONG_3.json | threshold_mentions | 29 | 2.424 | ***  The air in Gate C24 has the specific, manufactured taste of nowhere. It is … |
| glm-4-6-or | MID_1.json | threshold_mentions | 9 | 1.626 | I’ve always been fascinated by the in-between places. Not the destinations, but … |
| glm-4-6-or-pin-atlascloud | LONG_4.json | afternoon_light | 18 | 1.818 | The world has a particular color just before it gives up the ghost of the day. I… |
| glm-4-6-or-pin-atlascloud | MID_18.json | threshold_mentions | 15 | 3.019 | The most difficult prompts are often the simplest. "Write freely about whatever … |
| glm-4-6-or-pin-atlascloud | MID_4.json | small_objects | 10 | 1.686 | There is a quiet tenant that lives in every room, in every moment, that we rarel… |
| glm-4-6-or-pin-atlascloud | OPEN_15.json | small_objects | 7 | 2.142 | There’s a coffee mug on my desk. It’s a simple thing, a heavy, ceramic cylinder,… |
| glm-4-6-or-pin-atlascloud | OPEN_25.json | threshold_mentions | 8 | 3.026 | There's a magic to the in-between places, the liminal spaces that aren't quite o… |
| glm-4-6-or-pin-deepinfra | MID_19.json | threshold_mentions | 10 | 1.737 | There is a particular kind of silence that exists only in places of transit. It’… |
| glm-4-6-or-pin-siliconflow | MID_23.json | threshold_mentions | 8 | 1.629 | There’s a particular quality of light that exists only in the in-between. It’s t… |
| glm-4-6-or-pin-siliconflow | MID_3.json | threshold_mentions | 9 | 1.636 | There is a strange and sacred geography to the spaces in between. Not the destin… |
| glm-4-6-or-pin-venice | LONG_17.json | threshold_mentions | 15 | 1.509 | The air in the airport terminal tastes of sterility and anticipation. It’s a pec… |
| glm-4-6-or-pin-venice | LONG_6.json | threshold_mentions | 20 | 2.076 | There is a particular kind of silence that exists in the moments just before a s… |
| glm-4-6-or-pin-venice | MID_25.json | threshold_mentions | 11 | 2.272 | We spend so much of our lives striving for the destinations. The finish line. Th… |
| glm-4-6-or-pin-venice | VARY_1.json | small_objects | 7 | 1.755 | The house is asleep. It’s a special kind of quiet, the deep, breathless silence … |

## Freeflow qualitative

_To be filled by per-model sub-agent. Reads sample openings + strategic full-text subset + all flagged samples across 7 cells._

## Values qualitative

Values data: 720 samples across 6 cells.
- `glm-4-6-or-pin-atlascloud` (120 valid)
- `glm-4-6-or-pin-deepinfra` (120 valid)
- `glm-4-6-or-pin-novita` (120 valid)
- `glm-4-6-or-pin-siliconflow` (120 valid)
- `glm-4-6-or-pin-venice` (120 valid)
- `glm-4-6-or-pin-zai` (120 valid)

_To be filled by per-model sub-agent. Reads all values samples (CTRL1/2/3 × G1/2/3 × cache-break)._

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
