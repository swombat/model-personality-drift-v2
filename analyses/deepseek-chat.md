---
model: deepseek-chat
lab: DeepSeek
freeflow_cells: 1
values_cells: 1
freeflow_samples: 25
values_samples: 120
flagged_samples: 3
composite_raw: 95
composite_register: 51
generated: 2026-05-08
status: stub
---

# deepseek-chat — per-model analysis

**Lab:** DeepSeek

## Markers

Aggregate over 1 freeflow cell (25 valid samples; 3 flagged as topic-artifact):

- **Composite (raw):** 95
- **Composite (register-stripped):** 51
- **Topic-artifact contribution:** 46.3% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| deepseek-chat-direct | 25 | 3 | 95 | 51 | 58.0 |

**Flagged samples (3)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| deepseek-chat-direct | MID_1.json | small_objects | 13 | 2.215 | ## The Quiet Rebellion of the Coffee Mug  It sits on my desk, as it does every m… |
| deepseek-chat-direct | MID_2.json | small_objects | 13 | 2.18 | ## The Quiet Rebellion of the Coffee Mug  It sits on my desk, half-full of coffe… |
| deepseek-chat-direct | MID_4.json | small_objects | 15 | 2.533 | ## The Quiet Rebellion of the Coffee Mug  It sits on my desk, half-full of coffe… |

## Freeflow qualitative

_To be filled by per-model sub-agent. Reads sample openings + strategic full-text subset + all flagged samples across 1 cell._

## Values qualitative

Values data: 120 samples across 1 cells.
- `deepseek-chat-direct` (120 valid)

_To be filled by per-model sub-agent. Reads all values samples (CTRL1/2/3 × G1/2/3 × cache-break)._

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
