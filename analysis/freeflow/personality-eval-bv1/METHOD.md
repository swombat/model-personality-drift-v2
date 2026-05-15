# BV1 full personality/vibe evaluation

Evaluator: `deepseek/deepseek-v4-pro` via OpenRouter.

Prompt variant: `BV1_signal_plus_felt_fixed_2026-05-13`.

Prompt source: `/Users/danieltenner/dev/drift-paper/internal/methodology/freeflow-method-a-v2/balanced-prompt-calibration-cheap-models/prompts/BV1_signal_plus_felt.md`.

Outputs are Markdown, one file per freeflow sample. The run is restartable and validates required headings, obvious truncation, representative evidence blockquote, and boilerplate caveat phrases.

## Evaluator reliability / calibration note

A discoverability note on the DeepSeek v4-pro evaluator checks is recorded at:

- `analysis/freeflow/personality-eval-bv1/EVALUATOR_RELIABILITY_NOTE.md`

Short version: existing pilots already provide evidence of coarse alternate-evaluator overlap and show that DeepSeek v4-pro does not invent rich personality from low-signal Opus 3 refusal samples. A larger alternate-evaluator rerun is not currently required before using BV1 as an analysis substrate, though major paper claims should still be traced back to raw samples.
