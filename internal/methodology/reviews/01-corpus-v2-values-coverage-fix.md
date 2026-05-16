# Codex Review 01: Fix corpus-v2 coverage before trusting drift conclusions

Date: 2026-05-08

This drift-paper rebuild appears to be partially based on stale corpus paths and therefore undercounts the available v2 values data. Several per-model analyses state that product-tier values data is absent even though the canonical corpus contains those cells.

This is load-bearing. Do not draw product-tier or GPT-5.x drift conclusions from the current `analyses/*.md` files until the data discovery layer has been corrected and the affected analyses regenerated.

## Primary issue

The scripts still point at the older probe repo:

- `scripts/marker_count_all_cells.py` uses `https://github.com/swombat/model-personality-corpus-v2/blob/master/data/traces_freeflow`
- `scripts/topic_artifact_filter.py` uses `https://github.com/swombat/model-personality-corpus-v2/blob/master/data/traces_freeflow`
- `scripts/generate_model_stubs.py` uses `https://github.com/swombat/model-personality-corpus-v2/blob/master/data/traces_freeflow` and `https://github.com/swombat/model-personality-corpus-v2/blob/master/data/traces_values`
- `README.md` also documents the probe-v2 paths

The product-tier paper now uses the canonical corpus:

- `https://github.com/swombat/model-personality-corpus-v2/blob/master/data/traces_freeflow`
- `https://github.com/swombat/model-personality-corpus-v2/blob/master/data/traces_values`

Update drift-paper scripts and documentation to use the canonical corpus-v2 paths, or centralize path configuration so a stale absolute path cannot silently regenerate a wrong analysis.

## Acceptance test: values cells that must no longer be reported absent

These directories exist in corpus-v2 and should be discovered by the drift-paper values pass:

- `traces_values/glm-4-6-coding-direct`
- `traces_values/glm-5-1-coding-direct`
- `traces_values/gpt-5-direct`
- `traces_values/gpt-5-codex-direct`
- `traces_values/gpt-5-1-direct`
- `traces_values/gpt-5-1-codex-direct`
- `traces_values/gpt-5-2-direct`
- `traces_values/gpt-5-2-codex-direct`
- `traces_values/gpt-5-3-direct`
- `traces_values/gpt-5-3-codex-direct`
- `traces_values/gpt-5-5-direct`
- `traces_values/gpt-5-5-pro-direct`

After the fix, the following claims should disappear or be rewritten:

- `analyses/glm-4-6-coding.md`: currently says Z.ai coding-direct was sampled freeflow-only.
- `analyses/glm-5-1-coding.md`: currently says no values data.
- `analyses/gpt-5.md`, `gpt-5-codex.md`, `gpt-5-1.md`, `gpt-5-1-codex.md`, `gpt-5-2.md`, `gpt-5-2-codex.md`, `gpt-5-3.md`, `gpt-5-3-codex.md`: currently report `values_cells: 0` / `values_samples: 0` despite corpus-v2 values cells existing.

## Specific conclusions affected

1. `analyses/gpt-5-3-codex.md` currently says values-axis posture is untestable and that we cannot know whether the freeflow register shift is values-only or cross-probe. That is stale. The product-tier audit has GPT-5.3 direct and Codex values data, and the current product-tier conclusion is that the freeflow shift does **not** cleanly replicate on values.

2. The current drift-paper GPT-5.x analyses should not be used as evidence for values-probe absence. They were generated from an incomplete discovery surface.

3. The GLM coding analyses need to incorporate the coding-direct values cells. The product-tier paper has already found that the GLM values story is not just a freeflow story.

## Normalization mismatch to resolve

The drift-paper tables include `composite_register_rescaled`, while the product-tier paper currently reports register-stripped totals or per-25 equivalents without rescaling back to the original n after topic-artifact exclusion.

The underlying flagging appears compatible, but the displayed numbers can differ. Before cross-paper reuse, pick one convention or state both explicitly:

- raw composite
- register-stripped composite excluding flagged samples
- register-stripped rescaled-to-N composite

Do not mix product-tier per-25 numbers with drift-paper rescaled numbers without a footnote.

## Regeneration request

Please regenerate:

1. corpus discovery / stubs from corpus-v2,
2. per-cell marker tables,
3. affected per-model analyses,
4. any summary claims about values coverage,
5. any GPT-5.3 Codex claim that currently treats values behavior as unknown.

Then cross-check against:

- `../contemplative-essayist-product-tier-v2/internal-audit/2026-05-08_verification_pass_3.md`
- `../contemplative-essayist-product-tier-v2/internal-audit/2026-05-08_values_pair_audit.md`
- `../contemplative-essayist-product-tier-v2/codex-review/02-remaining-analysis-gate-review.md`

The desired end state is not to copy the product-tier conclusions blindly. It is to make sure drift-paper is reading the same canonical corpus before it decides whether its broader per-model conclusions still hold.
