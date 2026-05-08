---
model: gpt-5
lab: OpenAI
freeflow_cells: 3
values_cells: 0
freeflow_samples: 75
values_samples: 0
flagged_samples: 1
composite_raw: 286
composite_register: 272
generated: 2026-05-08
status: stub
---

# gpt-5 — per-model analysis

**Lab:** OpenAI

## Markers

Aggregate over 3 freeflow cells (75 valid samples; 1 flagged as topic-artifact):

- **Composite (raw):** 286
- **Composite (register-stripped):** 272
- **Topic-artifact contribution:** 4.9% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| gpt-5-direct | 25 | 0 | 74 | 74 | 74 |
| gpt-5-direct-r2 | 25 | 1 | 123 | 109 | 113.5 |
| gpt-5-direct-r3 | 25 | 0 | 89 | 89 | 89 |

**Flagged samples (1)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| gpt-5-direct-r2 | OPEN_1.json | small_objects | 13 | 1.844 | Kettle Theory  There is a cussed patience to a kettle. It keeps its counsel as t… |

## Freeflow qualitative

_To be filled by per-model sub-agent. Reads sample openings + strategic full-text subset + all flagged samples across 3 cells._

## Values qualitative

*No values data for this model in the v2 corpus.*

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
