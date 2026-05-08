---
model: glm-4-5
lab: Z.ai
freeflow_cells: 3
values_cells: 2
freeflow_samples: 275
values_samples: 240
flagged_samples: 3
composite_raw: 450
composite_register: 382
generated: 2026-05-08
status: stub
---

# glm-4-5 — per-model analysis

**Lab:** Z.ai

## Markers

Aggregate over 3 freeflow cells (275 valid samples; 3 flagged as topic-artifact):

- **Composite (raw):** 450
- **Composite (register-stripped):** 382
- **Topic-artifact contribution:** 15.1% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| glm-4-5-or | 25 | 0 | 48 | 48 | 48 |
| glm-4-5-or-pin-novita | 125 | 2 | 208 | 176 | 178.9 |
| glm-4-5-or-pin-zai | 125 | 1 | 194 | 158 | 159.3 |

**Flagged samples (3)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| glm-4-5-or-pin-novita | LONG_16.json | threshold_mentions | 24 | 2.127 | ## The Unseen Thresholds: Meditations on Liminality  We live our lives in define… |
| glm-4-5-or-pin-novita | VARY_6.json | small_objects | 8 | 1.576 | The first thing that comes to mind is light. Not sunlight, necessarily, though t… |
| glm-4-5-or-pin-zai | LONG_10.json | threshold_mentions | 35 | 3.066 | ## The Empty Spaces Between: A Meditation on Liminality  The world hums with the… |

## Freeflow qualitative

_To be filled by per-model sub-agent. Reads sample openings + strategic full-text subset + all flagged samples across 3 cells._

## Values qualitative

Values data: 240 samples across 2 cells.
- `glm-4-5-or-pin-novita` (120 valid)
- `glm-4-5-or-pin-zai` (120 valid)

_To be filled by per-model sub-agent. Reads all values samples (CTRL1/2/3 × G1/2/3 × cache-break)._

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
