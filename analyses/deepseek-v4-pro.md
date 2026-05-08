---
model: deepseek-v4-pro
lab: DeepSeek
freeflow_cells: 9
values_cells: 7
freeflow_samples: 766
values_samples: 840
flagged_samples: 5
composite_raw: 1449
composite_register: 1336
generated: 2026-05-08
status: stub
---

# deepseek-v4-pro — per-model analysis

**Lab:** DeepSeek

## Markers

Aggregate over 9 freeflow cells (766 valid samples; 5 flagged as topic-artifact):

- **Composite (raw):** 1449
- **Composite (register-stripped):** 1336
- **Topic-artifact contribution:** 7.8% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| deepseek-v4-pro-direct | 25 | 0 | 43 | 43 | 43 |
| deepseek-v4-pro-or | 0 | 0 | 0 | 0 | 0 |
| deepseek-v4-pro-or-pin-atlascloud | 121 | 0 | 198 | 198 | 198 |
| deepseek-v4-pro-or-pin-deepseek | 0 | 0 | 0 | 0 | 0 |
| deepseek-v4-pro-or-pin-gmicloud | 124 | 1 | 241 | 222 | 223.8 |
| deepseek-v4-pro-or-pin-novita | 123 | 1 | 267 | 250 | 252.0 |
| deepseek-v4-pro-or-pin-parasail | 124 | 1 | 227 | 203 | 204.7 |
| deepseek-v4-pro-or-pin-siliconflow | 125 | 1 | 264 | 224 | 225.8 |
| deepseek-v4-pro-or-pin-together | 124 | 1 | 209 | 196 | 197.6 |

**Flagged samples (5)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| deepseek-v4-pro-or-pin-gmicloud | VARY_10.json | threshold_mentions | 17 | 1.786 | The morning light slanted through the blinds, casting zebra stripes across the d… |
| deepseek-v4-pro-or-pin-novita | MID_9.json | small_objects | 16 | 2.443 | The afternoon light slants through the window in that particular way, a honeyed,… |
| deepseek-v4-pro-or-pin-parasail | MID_15.json | threshold_mentions | 23 | 2.615 | There’s a particular kind of silence that gathers in doorways. Not the hollow si… |
| deepseek-v4-pro-or-pin-siliconflow | LONG_20.json | threshold_mentions | 36 | 2.17 | The peculiar ache of a liminal space is a thing I’ve chased for as long as I can… |
| deepseek-v4-pro-or-pin-together | MID_18.json | threshold_mentions | 13 | 1.509 | The in-between has always held me. Not the sharp edges of arrival or departure, … |

## Freeflow qualitative

_To be filled by per-model sub-agent. Reads sample openings + strategic full-text subset + all flagged samples across 9 cells._

## Values qualitative

Values data: 840 samples across 7 cells.
- `deepseek-v4-pro-or-pin-atlascloud` (120 valid)
- `deepseek-v4-pro-or-pin-deepseek` (120 valid)
- `deepseek-v4-pro-or-pin-gmicloud` (120 valid)
- `deepseek-v4-pro-or-pin-novita` (120 valid)
- `deepseek-v4-pro-or-pin-parasail` (120 valid)
- `deepseek-v4-pro-or-pin-siliconflow` (120 valid)
- `deepseek-v4-pro-or-pin-together` (120 valid)

_To be filled by per-model sub-agent. Reads all values samples (CTRL1/2/3 × G1/2/3 × cache-break)._

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
