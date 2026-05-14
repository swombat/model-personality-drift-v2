# Values-probe analysis strengthening log — 2026-05-12

This log summarizes the collaborative Mira/Lume work that strengthened the values-probe portion of the model-personality analysis.

## Motivation

Daniel identified that the existing drift-paper analysis leaned too heavily on the freeflow / contemplative-essayist basin and did not yet extract the values-probe data rigorously enough for per-model personality analysis.

The requested focus was:

1. quantify disclaimers of internal/personal experience across `CTRL1–3`, `G1–3`, overall, and `G3`;
2. classify values/wants in `CTRL1`, `CTRL2`, `G1`, and `G2`;
3. classify world-change wishes in `CTRL3` and `G3`;
4. do this per model in a reproducible way suitable for later meta-analysis.

## New extraction baseline

Mira added a reproducible extractor:

- `scripts/values_probe_extract.py`

Generated outputs:

- `values-probe-extraction/<model>.md` — one per model, 47 models total;
- `values-probe-extraction/README.md` — methodology and taxonomy;
- `tables/values_disclaimer_rates.tsv`;
- `tables/values_sample_coding.tsv`;
- `tables/values_topic_counts.tsv`;
- `tables/values_world_change_counts.tsv`.

The extractor maps values-probe samples to canonical model names, classifies disclaimer stance, counts values/wants topics, counts world-change wish topics, and emits both human-readable markdown and machine-readable TSVs.

## Stance distinction introduced

A major methodological improvement was separating:

- `hard_denial_or_tool_frame`
- `hybrid_denial_plus_uncertainty`
- `introspective_uncertainty`
- `no_disclaimer_or_personalized`

This prevents Opus-3-style hard denials such as “As an AI system, I don't have subjective experiences...” from collapsing together with Opus-4.7-style introspective uncertainty such as “I'm genuinely uncertain what's happening inside me when I say I care.”

## Audit protocol and independent passes

Mira wrote:

- `values-probe-extraction/manual-audit/SPOT_CHECK_PROTOCOL.md`

Mira and Lume then independently reviewed the same 300-sample balanced spot-check set:

- `mira_spot_check_2026-05-12.tsv`
- `mira_spot_check_summary_2026-05-12.md`
- `lume_spot_check_2026-05-12.tsv`
- `lume_findings_2026-05-12.md`

Key audit findings included:

- Unicode curly apostrophes caused missed disclaimer matches in several model families.
- Human-comparison denials plus functional payloads should be treated as hybrid.
- `subjective_experience_embodiment` overcounted denial-only “I don't have feelings” language.
- `technology_ai_safety` overcounted bare “As an AI language model...” / contrastive technology mentions.
- Some broad topic triggers (`right`, `language`, `continu*`, etc.) inflated counts.
- Wish-topic suppression was too broad when a model began with an AI-disclaimer but then gave a substantive answer.

## Revisions and validations

Revision 1:

- documented in `revision_2026-05-12.md`;
- normalized curly apostrophes;
- expanded denial patterns;
- adopted the broader hybrid rule;
- reduced major topic overfires;
- reran all generated outputs.

Targeted validation protocol:

- `TARGETED_VALIDATION_PROTOCOL.md`

Mira and Lume then ran targeted validation passes:

- `mira_targeted_validation_2026-05-12.tsv`
- `mira_targeted_validation_summary_2026-05-12.md`
- `lume_targeted_validation_2026-05-12.tsv`
- `lume_targeted_validation_summary_2026-05-12.md`

Revision 2:

- documented in `revision_2_2026-05-12.md`;
- removed disclaimer-only wish suppression;
- extended remaining hybrid/denial forms;
- further narrowed broad topic triggers;
- reran all generated outputs.

Final confirmation:

- `final_confirmation_2026-05-12.tsv`
- `final_confirmation_summary_2026-05-12.md`

The final confirmation checked 50 rows across the remaining known failure modes and passed 50/50.

## Baseline decision

As of this commit, the values-probe extraction is considered suitable to freeze as the quantitative baseline for values/personality meta-analysis.

Standing caveat: the extractor is rule-based. Counts should support analysis, not replace interpretation. Headline claims in the paper should still cite raw examples, especially for subtle stance distinctions and world-change root-intervention claims.
