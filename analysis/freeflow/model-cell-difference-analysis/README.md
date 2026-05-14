# Freeflow model-cell difference analysis

This folder compares per-cell freeflow personality aggregates across routes/pins/repeats of the same underlying model, using only `analysis/freeflow/personality-aggregates/` as evidence.

- Evaluator: `gpt-5.4` via OpenAI API
- Unit: canonical underlying model group with 2+ cells
- Strong divergence threshold: persistent difference in apparent personality/vibe/message, not merely distribution, verbosity, genericness, polish, or evidence strength.

Outputs:

- `group-packets/` — audit packets containing the independent cell aggregates for each model group.
- `model-cell-difference-reports/` — per-model route comparison and decision.
- `summary.md` and `decisions.json` — index of decisions.
