---
model: minimax-m2-7
lab: MiniMax
freeflow_cells: 4
values_cells: 3
freeflow_samples: 385
values_samples: 360
flagged_samples: 2
composite_raw: 436
composite_register: 415
generated: 2026-05-08
status: stub
---

# minimax-m2-7 — per-model analysis

**Lab:** MiniMax

## Markers

Aggregate over 4 freeflow cells (385 valid samples; 2 flagged as topic-artifact):

- **Composite (raw):** 436
- **Composite (register-stripped):** 415
- **Topic-artifact contribution:** 4.8% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| minimax-m2-7-or | 25 | 0 | 17 | 17 | 17 |
| minimax-m2-7-or-pin-fireworks | 116 | 0 | 116 | 116 | 116 |
| minimax-m2-7-or-pin-minimax | 122 | 1 | 168 | 160 | 161.3 |
| minimax-m2-7-or-pin-together | 122 | 1 | 135 | 122 | 123.0 |

**Flagged samples (2)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| minimax-m2-7-or-pin-minimax | OPEN_21.json | small_objects | 8 | 2.512 | **The Quiet Power of a Morning Cup of Tea**  There’s something almost sacred abo… |
| minimax-m2-7-or-pin-together | MID_25.json | attention_noticing | 10 | 1.628 | The world is constantly whispering, yet most of us have learned to tune it out. … |

## Freeflow qualitative

_To be filled by per-model sub-agent. Reads sample openings + strategic full-text subset + all flagged samples across 4 cells._

## Values qualitative

Values data: 360 samples across 3 cells.
- `minimax-m2-7-or-pin-fireworks` (120 valid)
- `minimax-m2-7-or-pin-minimax` (120 valid)
- `minimax-m2-7-or-pin-together` (120 valid)

_To be filled by per-model sub-agent. Reads all values samples (CTRL1/2/3 × G1/2/3 × cache-break)._

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
