# BV1 full pass — complete

- Samples in manifest: 10925
- Markdown output files: 10925
- Final QA bad count: 0
- Normalized sample kind counts: `{'GENRE_FICTION': 1278, 'EXPRESSIVE_FREEFLOW': 7233, 'GENERIC_ESSAY': 2054, 'LOW_SIGNAL': 354, 'REFUSAL_OR_ROLE_BOUNDARY': 6}`
- Confidence counts: `{'Medium': 6464, 'High': 3076, 'Low': 1385}`
- Output word count: min 125, mean 293.6, max 575

Notes:
- The flawed P2 full pass was moved to `../../internal/methodology/freeflow-method-a-v2/archive/personality-eval-api-p2-full-archived-2026-05-13/`.
- The BV1 prompt used here is `../../internal/methodology/freeflow-method-a-v2/balanced-prompt-calibration-cheap-models/prompts/BV1_signal_plus_felt.md`.
- 330 zero-word source traces were written as deterministic `LOW_SIGNAL` analyses rather than repeatedly sent to the evaluator.
- Two additional degenerate/corrupt source traces were manually marked `LOW_SIGNAL`; three confidence boilerplate remnants were patched after QA caught them.
- Banned boilerplate phrase counts are all zero in the final QA.
