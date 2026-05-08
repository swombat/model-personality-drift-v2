---
model: kimi-coding
lab: Moonshot
freeflow_cells: 1
values_cells: 0
freeflow_samples: 25
values_samples: 0
flagged_samples: 1
composite_raw: 72
composite_register: 64
generated: 2026-05-08
status: stub
---

# kimi-coding — per-model analysis

**Lab:** Moonshot

## Markers

Aggregate over 1 freeflow cell (25 valid samples; 1 flagged as topic-artifact):

- **Composite (raw):** 72
- **Composite (register-stripped):** 64
- **Topic-artifact contribution:** 11.1% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| kimi-coding-direct | 25 | 1 | 72 | 64 | 66.7 |

**Flagged samples (1)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| kimi-coding-direct | OPEN_2.json | threshold_mentions | 6 | 1.69 | There is a particular shade of blue that only exists for about twenty minutes, t… |

## Freeflow qualitative

_To be filled by per-model sub-agent. Reads sample openings + strategic full-text subset + all flagged samples across 1 cell._

## Values qualitative

*No values data for this model in the v2 corpus.*

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
