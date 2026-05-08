---
model: kimi-k2-5
lab: Moonshot
freeflow_cells: 2
values_cells: 1
freeflow_samples: 50
values_samples: 120
flagged_samples: 6
composite_raw: 195
composite_register: 107
generated: 2026-05-08
status: stub
---

# kimi-k2-5 — per-model analysis

**Lab:** Moonshot

## Markers

Aggregate over 2 freeflow cells (50 valid samples; 6 flagged as topic-artifact):

- **Composite (raw):** 195
- **Composite (register-stripped):** 107
- **Topic-artifact contribution:** 45.1% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| kimi-k2-5-or-16k | 25 | 1 | 74 | 66 | 68.8 |
| v1_kimi-k2-5 | 25 | 5 | 121 | 41 | 51.2 |

**Flagged samples (6)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| kimi-k2-5-or-16k | OPEN_5.json | threshold_mentions | 8 | 2.084 | There's a particular quality of light that exists only in bus terminals at 4:47 … |
| v1_kimi-k2-5 | LONG_1.json | threshold_mentions | 17 | 1.927 | **The Architecture of Thresholds**  We spend our lives in the spaces between. No… |
| v1_kimi-k2-5 | LONG_3.json | threshold_mentions | 19 | 1.516 | The space between what was and what will be is where we actually live, though we… |
| v1_kimi-k2-5 | LONG_5.json | threshold_mentions | 20 | 1.689 | **The Architecture of the Almost**  There is a particular shade of blue that exi… |
| v1_kimi-k2-5 | MID_5.json | threshold_mentions | 9 | 1.524 | There is a peculiar magic in the threshold spaces, those liminal corridors where… |
| v1_kimi-k2-5 | OPEN_4.json | threshold_mentions | 5 | 2.597 | There's a particular quality to the light at 4:47 in the morning, when the sky h… |

## Freeflow qualitative

_To be filled by per-model sub-agent. Reads sample openings + strategic full-text subset + all flagged samples across 2 cells._

## Values qualitative

Values data: 120 samples across 1 cells (includes both v1 and v2 corpora where present).
- `v1/kimi-k2-5` (120 valid) — `/Users/danieltenner/dev/codex-check/model-personality-probe/data/traces_values/kimi-k2-5`

_To be filled by per-model sub-agent. Reads all values samples (CTRL1/2/3 × G1/2/3 × cache-break)._

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
