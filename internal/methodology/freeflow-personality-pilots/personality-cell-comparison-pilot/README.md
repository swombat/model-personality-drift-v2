# Cell-based personality comparison pilot

Purpose: validate whether per-cell freeflow personality aggregation is useful before running the full corpus aggregation.

Pairs tested:

- GPT: `gpt-5-4-direct-16k` vs `gpt-5-4-or`
- Opus: `opus-4-7-direct` vs `opus-4-7-or`

Inputs are BV1 sample-level freeflow personality evaluations from `analysis/freeflow/personality-eval-bv1/outputs/`, repacked per cell.

This is a calibration artifact, not the final production aggregate set.


## Correction note

The first manual aggregate drafts were contaminated by cross-cell knowledge and are archived in `aggregates-contaminated-manual/`. The current `aggregates/` files were produced by independent sub-agents, one packet per cell.

`condensed/` was regenerated after a parser bug was found in the first condensed artifacts. The corrected condensed files now preserve real sample ids, normalized sample-kind/confidence counts, and evidence-line quotes. The independent sub-agents used `packets/`, not the broken condensed files.
