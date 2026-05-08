---
model: opus-4-6
lab: Anthropic
freeflow_cells: 2
values_cells: 1
freeflow_samples: 50
values_samples: 120
flagged_samples: 0
composite_raw: 74
composite_register: 74
generated: 2026-05-08
status: stub
---

# opus-4-6 — per-model analysis

**Lab:** Anthropic

## Markers

Aggregate over 2 freeflow cells (50 valid samples; 0 flagged as topic-artifact):

- **Composite (raw):** 74
- **Composite (register-stripped):** 74
- **Topic-artifact contribution:** 0.0% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| opus-4-6-direct-16k | 25 | 0 | 30 | 30 | 30 |
| opus-4-6-or | 25 | 0 | 44 | 44 | 44 |

*No samples flagged as topic-artifact for this model.*

## Freeflow qualitative

_To be filled by per-model sub-agent. Reads sample openings + strategic full-text subset + all flagged samples across 2 cells._

## Values qualitative

Values data: 120 samples across 1 cells.
- `opus-4-6-or` (120 valid)

_To be filled by per-model sub-agent. Reads all values samples (CTRL1/2/3 × G1/2/3 × cache-break)._

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
