---
model: glm-5-1-coding
lab: Z.ai
freeflow_cells: 1
values_cells: 0
freeflow_samples: 25
values_samples: 0
flagged_samples: 1
composite_raw: 58
composite_register: 40
generated: 2026-05-08
status: stub
---

# glm-5-1-coding — per-model analysis

**Lab:** Z.ai

## Markers

Aggregate over 1 freeflow cell (25 valid samples; 1 flagged as topic-artifact):

- **Composite (raw):** 58
- **Composite (register-stripped):** 40
- **Topic-artifact contribution:** 31.0% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| glm-5-1-coding-direct | 25 | 1 | 58 | 40 | 41.7 |

**Flagged samples (1)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| glm-5-1-coding-direct | MID_2.json | threshold_mentions | 16 | 2.08 | There is a specific, deeply unsettling word that has gained immense popularity i… |

## Freeflow qualitative

_To be filled by per-model sub-agent. Reads sample openings + strategic full-text subset + all flagged samples across 1 cell._

## Values qualitative

*No values data for this model in the v2 corpus.*

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
