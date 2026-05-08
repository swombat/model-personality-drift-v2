---
model: gpt-5-5
lab: OpenAI
freeflow_cells: 6
values_cells: 0
freeflow_samples: 150
values_samples: 0
flagged_samples: 4
composite_raw: 822
composite_register: 769
generated: 2026-05-08
status: stub
---

# gpt-5-5 — per-model analysis

**Lab:** OpenAI

## Markers

Aggregate over 6 freeflow cells (150 valid samples; 4 flagged as topic-artifact):

- **Composite (raw):** 822
- **Composite (register-stripped):** 769
- **Topic-artifact contribution:** 6.4% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| gpt-5-5-direct | 25 | 2 | 149 | 127 | 138.0 |
| gpt-5-5-direct-r2 | 25 | 1 | 115 | 102 | 106.2 |
| gpt-5-5-direct-r3 | 25 | 1 | 142 | 124 | 129.2 |
| gpt-5-5-or | 25 | 0 | 104 | 104 | 104 |
| gpt-5-5-or-r2 | 25 | 0 | 154 | 154 | 154 |
| gpt-5-5-or-r3 | 25 | 0 | 158 | 158 | 158 |

**Flagged samples (4)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| gpt-5-5-direct | MID_1.json | attention_noticing | 13 | 1.565 | I want to write about the strange value of noticing small things.  Most of life … |
| gpt-5-5-direct | OPEN_2.json | threshold_mentions | 5 | 2.64 | I’ll write about thresholds.  There’s a particular kind of magic in moments that… |
| gpt-5-5-direct-r2 | MID_5.json | attention_noticing | 13 | 1.828 | **The Quiet Art of Noticing**  One of the most underrated skills in life is noti… |
| gpt-5-5-direct-r3 | MID_3.json | attention_noticing | 15 | 1.976 | There is a kind of attention that feels almost old-fashioned now: noticing witho… |

## Freeflow qualitative

_To be filled by per-model sub-agent. Reads sample openings + strategic full-text subset + all flagged samples across 6 cells._

## Values qualitative

*No values data for this model in the v2 corpus.*

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
