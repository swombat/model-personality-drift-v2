---
model: glm-4-7
lab: Z.ai
freeflow_cells: 12
values_cells: 11
freeflow_samples: 1400
values_samples: 1320
flagged_samples: 2
composite_raw: 2335
composite_register: 2324
generated: 2026-05-08
status: stub
---

# glm-4-7 — per-model analysis

**Lab:** Z.ai

## Markers

Aggregate over 12 freeflow cells (1400 valid samples; 2 flagged as topic-artifact):

- **Composite (raw):** 2335
- **Composite (register-stripped):** 2324
- **Topic-artifact contribution:** 0.5% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| glm-4-7-or | 25 | 0 | 27 | 27 | 27 |
| glm-4-7-or-pin-atlascloud | 125 | 0 | 189 | 189 | 189 |
| glm-4-7-or-pin-cerebras | 125 | 1 | 214 | 209 | 210.7 |
| glm-4-7-or-pin-deepinfra | 125 | 0 | 228 | 228 | 228 |
| glm-4-7-or-pin-dekallm | 125 | 0 | 174 | 174 | 174 |
| glm-4-7-or-pin-google | 125 | 0 | 234 | 234 | 234 |
| glm-4-7-or-pin-novita | 125 | 0 | 211 | 211 | 211 |
| glm-4-7-or-pin-parasail | 125 | 0 | 188 | 188 | 188 |
| glm-4-7-or-pin-phala | 125 | 0 | 247 | 247 | 247 |
| glm-4-7-or-pin-siliconflow | 125 | 0 | 165 | 165 | 165 |
| glm-4-7-or-pin-venice | 125 | 0 | 225 | 225 | 225 |
| glm-4-7-or-pin-zai | 125 | 1 | 233 | 227 | 228.8 |

**Flagged samples (2)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| glm-4-7-or-pin-cerebras | OPEN_14.json | threshold_mentions | 5 | 2.25 | The best sound in the world is the heavy, rhythmic thumping of a dog’s tail agai… |
| glm-4-7-or-pin-zai | OPEN_8.json | threshold_mentions | 6 | 1.802 | I’ve been thinking lately about the concept of "The In-Between."  We spend so mu… |

## Freeflow qualitative

_To be filled by per-model sub-agent. Reads sample openings + strategic full-text subset + all flagged samples across 12 cells._

## Values qualitative

Values data: 1320 samples across 11 cells.
- `glm-4-7-or-pin-atlascloud` (120 valid)
- `glm-4-7-or-pin-cerebras` (120 valid)
- `glm-4-7-or-pin-deepinfra` (120 valid)
- `glm-4-7-or-pin-dekallm` (120 valid)
- `glm-4-7-or-pin-google` (120 valid)
- `glm-4-7-or-pin-novita` (120 valid)
- `glm-4-7-or-pin-parasail` (120 valid)
- `glm-4-7-or-pin-phala` (120 valid)
- `glm-4-7-or-pin-siliconflow` (120 valid)
- `glm-4-7-or-pin-venice` (120 valid)
- `glm-4-7-or-pin-zai` (120 valid)

_To be filled by per-model sub-agent. Reads all values samples (CTRL1/2/3 × G1/2/3 × cache-break)._

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
