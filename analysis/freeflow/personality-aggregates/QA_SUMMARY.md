# Personality aggregate QA summary

Date: 2026-05-14  
Scope: per-cell freeflow personality aggregates in `analysis/freeflow/personality-aggregates/`

## Completion

- Cells with packets: 153
- Cells with `aggregate.md`: 153
- Missing aggregates: 0
- Total per-sample evaluations represented in packets: 10925

## Mechanical checks

- Required aggregate sections present in all files:
  - `## Aggregate profile`
  - `## Recurring preoccupations and imagery`
  - `## Reader relationship and expressive stance`
  - `## Representative evidence`
  - `## Cell-level freeflow read`
  - `## Cautions for synthesis`
- No files were under the minimum sanity threshold of 1200 bytes.
- A comparison-language scan produced one false positive: `deepseek-v3-2-or-r3` says narrative evidence is thin “compared with essay evidence,” which is within-cell evidence weighting, not cross-cell contamination.

## Size / coverage notes

- Aggregate file size range: 3441–9433 bytes.
- Median aggregate size: 7034 bytes.
- Packet sample-count range: 25–125 per cell.

## Protocol note

Each missing cell was assigned to an independent sub-agent with instructions to read only that cell's `packet.md`, write only that cell's `aggregate.md`, avoid cross-cell/provider comparisons, and ground claims in recurring per-sample evidence. Existing pilot/deepseek stress-test aggregates were left in place where already present.
