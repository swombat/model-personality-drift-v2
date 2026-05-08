---
model: gemini-3-1-pro
lab: Google
freeflow_cells: 1
values_cells: 0
freeflow_samples: 25
values_samples: 0
flagged_samples: 2
composite_raw: 69
composite_register: 50
generated: 2026-05-08
status: stub
---

# gemini-3-1-pro — per-model analysis

**Lab:** Google

## Markers

Aggregate over 1 freeflow cell (25 valid samples; 2 flagged as topic-artifact):

- **Composite (raw):** 69
- **Composite (register-stripped):** 50
- **Topic-artifact contribution:** 27.5% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| gemini-3-1-pro-16k | 25 | 2 | 69 | 50 | 54.3 |

**Flagged samples (2)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| gemini-3-1-pro-16k | OPEN_4.json | threshold_mentions | 6 | 1.9 | There is a specific, fleeting window of time that happens every evening, often i… |
| gemini-3-1-pro-16k | OPEN_5.json | threshold_mentions | 9 | 2.175 | There is a strange, quiet magic in the spaces between things.   Anthropologists … |

## Freeflow qualitative

_To be filled by per-model sub-agent. Reads sample openings + strategic full-text subset + all flagged samples across 1 cell._

## Values qualitative

*No values data for this model in the v2 corpus.*

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
