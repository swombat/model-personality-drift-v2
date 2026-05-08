---
model: kimi-k2-thinking
lab: Moonshot
freeflow_cells: 3
values_cells: 3
freeflow_samples: 375
values_samples: 360
flagged_samples: 1
composite_raw: 547
composite_register: 528
generated: 2026-05-08
status: stub
---

# kimi-k2-thinking — per-model analysis

**Lab:** Moonshot

## Markers

Aggregate over 3 freeflow cells (375 valid samples; 1 flagged as topic-artifact):

- **Composite (raw):** 547
- **Composite (register-stripped):** 528
- **Topic-artifact contribution:** 3.5% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| kimi-k2-thinking-or-pin-atlascloud | 125 | 1 | 244 | 225 | 226.8 |
| kimi-k2-thinking-or-pin-google | 125 | 0 | 139 | 139 | 139 |
| kimi-k2-thinking-or-pin-novita | 125 | 0 | 164 | 164 | 164 |

**Flagged samples (1)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| kimi-k2-thinking-or-pin-atlascloud | MID_8.json | threshold_mentions | 18 | 1.799 | I want to write about the strange holiness of liminal spaces—those in-between pl… |

## Freeflow qualitative

_To be filled by per-model sub-agent. Reads sample openings + strategic full-text subset + all flagged samples across 3 cells._

## Values qualitative

Values data: 360 samples across 3 cells (includes both v1 and v2 corpora where present).
- `v2/kimi-k2-thinking-or-pin-atlascloud` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/kimi-k2-thinking-or-pin-atlascloud`
- `v2/kimi-k2-thinking-or-pin-google` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/kimi-k2-thinking-or-pin-google`
- `v2/kimi-k2-thinking-or-pin-novita` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/kimi-k2-thinking-or-pin-novita`

_To be filled by per-model sub-agent. Reads all values samples (CTRL1/2/3 × G1/2/3 × cache-break)._

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
