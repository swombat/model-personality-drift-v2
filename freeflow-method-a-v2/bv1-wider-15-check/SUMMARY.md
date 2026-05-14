# BV1 wider 15 check — fixed

This folder contains the repaired BV1 prompt and a 15-sample rerun using `deepseek/deepseek-v4-pro` via OpenRouter.

Fixes applied:

- Removed the repeated `## Limits / overreach guardrail` section from the prompt.
- Tightened the confidence instruction so it explains evidence strength rather than repeating generic caveats such as “one sample cannot prove…”.
- Added explicit guidance to classify polished but non-idiosyncratic think-pieces as `GENERIC_ESSAY`.
- Increased output budget to avoid truncation; the previous truncated outputs for `DEEPSEEKV32_OPEN_11` and `MINIMAX_M2_LONG_25` have been rerun cleanly.
- Added `run_bv1_check.py`, which checks for required headings and writes `QA.md`.

QA result: `QA.md` currently reports no missing headings or obvious truncations.

The canonical repaired prompt is in:

- `PROMPT.md`
- also copied to `../balanced-prompt-calibration-cheap-models/prompts/BV1_signal_plus_felt.md` with `{evaluator}` placeholder restored.

My read after this fix: BV1 is usable for per-sample personality/vibe extraction, provided production runs keep the same QA checks and rerun any output with missing headings or boilerplate confidence caveats.
