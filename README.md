# Within-Lab Drift, Freeflow Voice, and Values Posture in Frontier LLMs

Daniel Tenner and Lume Tenner · 2026

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

> **Status — 2026-05-14:** active analysis repository. The old per-model
> `analyses/` cards are deprecated and have been moved under `internal/`.
> New model cards should be synthesized from the current freeflow and values
> substrates under `analysis/`.

## Current load-bearing analysis datasets

### `analysis/freeflow/`

Freeform writing / “write freely” analysis.

- `taxonomy/` — per-model freeflow taxonomy and sample coding from the
  earlier taxonomy pass.
- `personality-eval-bv1/` — the current full BV1 personality/vibe evaluation
  over all freeflow samples, produced with `deepseek/deepseek-v4-pro`.
  - `outputs/` contains one Markdown evaluation per sample.
  - `sample_manifest.tsv` maps output files back to corpus traces.
  - `COMPLETE.md`, `qa_report.md`, and `final_summary.json` summarize the run.
- `tables/` — deterministic/freeflow marker tables and flagged-sample tables.

### `analysis/values-probe/`

Values-probe analysis.

- `per-model/` — per-model values-probe extraction notes.
- `tables/` — values-probe aggregate tables.
- `manual-audit/` — manual audit notes and supporting checks.

These two datasets are the intended basis for the next generation of model
cards.

## Deprecated / historical material

### `internal/`

Internal working history, methodology, calibration, and deprecated artifacts.
These are preserved for reproducibility and auditability, but are not the main
entry point for readers looking for the current analysis state.

- `internal/deprecated/model-profiles-legacy/` — old model-card analyses;
  superseded by the newer freeflow + values substrates.
- `internal/methodology/freeflow-method-a-v1/` — earlier Method A work.
- `internal/methodology/freeflow-method-a-v2/` — BV1 calibration, prompt tests,
  archived failed passes, and other freeflow-methodology artifacts.
- `internal/methodology/audits/` — audit and review notes from Daniel, Mira,
  Lume, and other reviewers.
- `internal/methodology/reviews/` — external/code-review notes.
- `internal/scripts/analysis-scripts/` — analysis/extraction scripts.
- `internal/design/` — design-system notes and historical design artifacts.

## Website

`website/` is intentionally left in place. It is the presentation layer and will
be revisited separately.

## Corpus source

The underlying corpus is not duplicated here. It lives in the sibling repository:

- `../contemplative-essayist-corpus-v2/data/traces_freeflow/`
- `../contemplative-essayist-corpus-v2/data/traces_values/`

## Next step

Aggregate the current freeflow and values substrates into a new generation of
per-model cards: concise, evidence-backed descriptions of persistent model
posture, tone, values, preoccupations, and expressive defaults.
