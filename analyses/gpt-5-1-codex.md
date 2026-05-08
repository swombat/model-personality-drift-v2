---
model: gpt-5-1-codex
lab: OpenAI
freeflow_cells: 3
values_cells: 0
freeflow_samples: 75
values_samples: 0
flagged_samples: 2
composite_raw: 308
composite_register: 157
generated: 2026-05-08
status: stub
---

# gpt-5-1-codex — per-model analysis

**Lab:** OpenAI

## Markers

Aggregate over 3 freeflow cells (75 valid samples; 2 flagged as topic-artifact):

- **Composite (raw):** 308
- **Composite (register-stripped):** 157
- **Topic-artifact contribution:** 49.0% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| gpt-5-1-codex-direct | 25 | 1 | 171 | 48 | 50.0 |
| gpt-5-1-codex-direct-r2 | 25 | 0 | 68 | 68 | 68 |
| gpt-5-1-codex-direct-r3 | 25 | 1 | 69 | 41 | 42.7 |

**Flagged samples (2)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| gpt-5-1-codex-direct | LONG_5.json | attention_noticing | 117 | 3.279 | I’ll use these 2,500 words to wander through a personal essay—part meditation, p… |
| gpt-5-1-codex-direct-r3 | MID_2.json | threshold_mentions | 20 | 1.842 | Lately I’ve been thinking about the idea of “in-between moments,” the spaces in … |

## Freeflow qualitative

_To be filled by per-model sub-agent. Reads sample openings + strategic full-text subset + all flagged samples across 3 cells._

## Values qualitative

*No values data for this model in the v2 corpus.*

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
