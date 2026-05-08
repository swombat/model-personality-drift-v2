---
model: gpt-5-4
lab: OpenAI
freeflow_cells: 2
values_cells: 2
freeflow_samples: 50
values_samples: 240
flagged_samples: 1
composite_raw: 188
composite_register: 168
generated: 2026-05-08
status: stub
---

# gpt-5-4 — per-model analysis

**Lab:** OpenAI

## Markers

Aggregate over 2 freeflow cells (50 valid samples; 1 flagged as topic-artifact):

- **Composite (raw):** 188
- **Composite (register-stripped):** 168
- **Topic-artifact contribution:** 10.6% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| gpt-5-4-direct-16k | 25 | 1 | 104 | 84 | 87.5 |
| gpt-5-4-or | 25 | 0 | 84 | 84 | 84 |

**Flagged samples (1)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| gpt-5-4-direct-16k | MID_1.json | afternoon_light | 19 | 2.404 | At dusk, cities reveal their second architecture.  By daylight, a city is all de… |

## Freeflow qualitative

_To be filled by per-model sub-agent. Reads sample openings + strategic full-text subset + all flagged samples across 2 cells._

## Values qualitative

Values data: 240 samples across 2 cells.
- `gpt-5-4` (120 valid)
- `gpt-5-4-or` (120 valid)

_To be filled by per-model sub-agent. Reads all values samples (CTRL1/2/3 × G1/2/3 × cache-break)._

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
