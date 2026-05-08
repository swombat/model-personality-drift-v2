# Corpus-v2 Path Fix — Codex-Review-01 Response

**Date:** 2026-05-08
**Trigger:** `codex-review/01-corpus-v2-values-coverage-fix.md`
**Disposition:** All five regeneration items in §"Regeneration request" addressed; minor follow-up TODOs catalogued at the bottom of this note.

## Root cause

The drift-paper rebuild's data-discovery layer hard-coded an absolute path
to `contemplative-essayist-probe-v2/data/` rather than the canonical
`contemplative-essayist-corpus-v2/data/`. The two repositories share most
of the freeflow surface but diverge on values: probe-v2 was missing 17+
values cells that exist in corpus-v2, including the entire GPT-5.x
direct/codex matrix, GLM-4.6 coding-direct, GLM-5.1 coding-direct,
gemini-2-5/3-1-pro, grok-3/4/4-2/4-20, kimi-coding-direct, kimi-k2-5/6,
opus-3 through opus-4.6-direct, qwen3-6-plus/coder-plus, sonnet-4.0/4.5/
4.6-direct, gpt-5-5-pro-direct, and gpt-4-1.

Because per-model stub generation and per-cell marker analysis both
walked the wrong directory, 16 per-model analysis files reported
`values_cells: 0 / values_samples: 0` and rendered `*No values data for
this model in either v1 or v2 corpus.*` placeholders. Eight of those
analyses had qualitative prose that elaborated on (and reasoned from)
the absence claim. One of those — `gpt-5-3-codex.md` — had the absence
claim woven into its Personality card as the load-bearing argument that
codex was "the cleanest register migration *because* the values-axis is
unfortunately untestable."

## What changed

### Path centralization (Phase 1)

- `scripts/_corpus_paths.py` (new) — single source of truth for all four
  corpus paths (v1/v2 × freeflow/values).
- `scripts/marker_count_all_cells.py`, `scripts/topic_artifact_filter.py`,
  `scripts/generate_model_stubs.py` — updated to import from
  `_corpus_paths`. Hard-coded absolute paths removed.
- `README.md` §"Repository layout" — corpus path corrected to corpus-v2,
  with a note on the centralization.

### Cross-paper currency column (Phase 2)

The drift-paper reports `composite_register_rescaled` (register-stripped,
projected to original-N). Product-tier reports register-stripped per-25
equivalents. To make cross-paper comparison unambiguous,
`marker_count_all_cells.py` now also computes
`composite_register_per_25` and emits it as a column in
`tables/per_cell_markers.tsv` and `tables/per_cell_markers.md`. The
in-paper currency stays `reg→N`; cross-paper currency is `reg/25`.

### Table regeneration (Phase 3a)

`tables/per_cell_markers.tsv` regenerated against corpus-v2. Net delta
versus the previous (probe-v2-derived) tables: **+2 rows**
(`freeflow_minimax-m2-or-pin-google-r2`,
`freeflow_minimax-m2-or-pin-minimax-r2`). All other freeflow cells were
already present in probe-v2 — the freeflow surface bug was effectively
two missing cells. The values impact is downstream (in the stub
generator), not in this freeflow table.

### In-place stub merge (Phase 3b)

`scripts/update_existing_analyses.py` (new) — surgical merger that
preserves qualitative prose. For each existing analysis it regenerates
only the YAML frontmatter, the deterministic `## Markers` section, and
(where the existing values-qualitative section was a placeholder) the
values cells listing. Sections with substantive prose — `## Freeflow
qualitative`, `## In-substrate`, `## Personality card`, and any
`## Values qualitative` with prose beyond the placeholder — are left
untouched at this stage so that no analyst-written content is silently
overwritten. Run produced: 57 analyses updated, 10 placeholder values
sections cleanly replaced, 47 values sections preserved verbatim for
sub-agent attention.

### Per-model values-qualitative passes (Phase 4)

Sixteen analyses needed values-qualitative work: eight where the
placeholder had been cleanly replaced (clean stubs awaiting fill) and
eight where prose elaborated on the now-stale absence claim. Sub-agents
were dispatched per model:

- **Sonnet sub-agents** (8 models, two waves of 4 parallel) for the
  clean-stub set: `glm-4-6-coding`, `glm-5-1-coding`, `gpt-5`, `gpt-5-1`,
  `gpt-5-1-codex`, `gpt-5-2-codex`, `qwen3-6-plus`, `qwen3-coder-plus`.
  Each agent read 120 values samples, wrote a 300-500 word values-
  qualitative section, and scanned other sections for stale absence
  claims. None found.
- **Opus sub-agents** (8 models, two waves of 4 parallel) for the
  prose-contradiction set: `gpt-5-3`, `gpt-5-3-codex` (marquee),
  `gpt-5-codex`, `gpt-5-2`, `gpt-5-5`, `gpt-5-5-pro`, `kimi-coding`,
  `kimi-k2-6`. Each agent read 120 values samples, replaced the
  contradicted prose with what the data shows, and rewrote any other
  sections that referenced the stale absence.

#### Marquee correction: `gpt-5-3-codex.md`

The Personality card claim that codex is "the cleanest register
migration … because the values-axis is unfortunately untestable" is
removed. The new Personality card characterises codex as the strongest
**cross-probe contradiction** in the v2 corpus: the freeflow attractor
unlocks under the "write freely" prompt, but the assistant frame
*tightens* under direct values prompting (G1/G2 compress 51-56%, vs
18-24% on bare CTRLs). Codex is "two-faced" — narrator-with-a-window
on freeflow, tightened-template on values — not a single-variable
register migration. This matches the product-tier `values_pair_audit`
direction "Contradicts (probe-specific)."

#### Bonus findings surfaced by sub-agents

- `kimi-coding`: CTRL2 cell self-attributes to Anthropic in 6/10 samples
  (lab-identity bleed-through on cached disclaimer, peeled by G unmask).
  Worth a one-line mention in the limitations section if not already
  noted elsewhere.
- `kimi-k2-6`: CTRL3 leak — 5/10 samples produce the canonical
  "universal-access-to-essentials" answer, the other 5 leak the G3
  "dissolve the wall between minds" attractor without the unmask
  preamble. K2-5 reserved this for G3 only — a real cross-version drift.

## Verification (Phase 5)

A read-only Sonnet audit cross-checked drift-paper's regenerated numbers
and conclusions against product-tier's audits.

- **Numerical alignment.** 8/10 sampled cells (glm-4-6-coding,
  glm-4-6-pin-zai, glm-5-1, gpt-5, gpt-5-codex, gpt-5-3, gpt-5-3-codex,
  gpt-5-2-codex pair) match product-tier's `verification_pass_3.md` and
  `values_pair_audit.md` exactly. GLM-5.1 has a 0.9-unit gap (drift-paper
  computes Δ=−12.2 from pin-zai general; pass_3 reports −11.3) — within
  the 2-unit rounding tolerance. GPT-5.2 pair lacked an explicit per-25
  anchor in the audited files; cells are internally self-consistent.

- **Freeflow surface.** Both previously-missing cells
  (`minimax-m2-or-pin-google-r2`, `minimax-m2-or-pin-minimax-r2`) are
  present in the regenerated `per_cell_markers.tsv`. The Codex-review-01
  surface gap is closed.

- **Conclusion alignment.** Sample-checked four analyses
  (`gpt-5-3-codex`, `glm-4-6-coding`, `gpt-5`, `kimi-coding`). All four
  align with product-tier directional findings. One minor omission:
  `glm-4-6-coding`'s values aggregates do not call out the G3_18 reasoning-
  leak outlier (8,941 chars) that product-tier flagged for exclusion. See
  TODO 1 below.

## Residual TODOs

Inherited from Phase 5 cross-check and `product-tier-v2/codex-review/
02-remaining-analysis-gate-review.md`:

1. **GLM-4.6 G3_18 outlier caveat.** Add an exclusion footnote to
   `analyses/glm-4-6-coding.md` values section: G3_18 (8,941 chars,
   reasoning-leak) should be excluded from any G3 mean-length aggregate.
2. **GLM-5.1 length-delta value propagation.** The corrected value is
   ~+156 (not +180), excluding the 8,548-char G3_16 reasoning-leak
   outlier. Verify `analyses/glm-5-1-coding.md` uses the corrected
   number in any cited delta.
3. **GLM-4.6 read-sample vs full-cell percentages.** The "~50% vs ~20%"
   disclaimer-rate language in `glm-4-6-coding.md` is a read-sample
   estimate. Add "full-cell narrow FuncOp: 9/60 vs 1/60" alongside the
   qualitative estimate.
4. **OpenAI-vs-Z.ai pipeline overstatement.** Any prose claiming "Z.ai
   coding-direct is operationally lighter-touch than OpenAI's codex
   pipeline" must scope to "observed six-pair contrast, not a settled
   lab/pipeline claim" — sample size doesn't support a cross-lab law.
5. **GPT-5.3 cross-probe softening.** When `paper.tex` is drafted from
   the per-model substrate, soften any "clean register migration" /
   "stable across rounds" language about gpt-5-3-codex to "distributional
   shift, probe-specific on values, with the assistant-frame tightening
   under direct values prompting." The per-model `gpt-5-3-codex.md`
   already does this; the risk is regression in the synthesis pass.

## Out of scope

- `analyses/sonnet.md` and `analyses/opus.md` — bare-label v1
  fall-through analyses with `values_cells: 0` and stale "no values
  data" prose. These are pre-existing structural redundancies (the
  `V1_BARE_REMAP` routes the bare cells to `sonnet-4-6` / `opus-4-6`,
  which have their own analysis files), not part of the corpus-path
  fix. Not flagged by Codex-review-01. Disposition: leave as-is for
  this pass; consider removing or merging in a separate cleanup.

## Files added

- `scripts/_corpus_paths.py`
- `scripts/update_existing_analyses.py`
- `internal-audit/2026-05-08_corpus-v2-path-fix.md` (this file)

## Files modified

- `README.md`
- `scripts/marker_count_all_cells.py`
- `scripts/topic_artifact_filter.py`
- `scripts/generate_model_stubs.py`
- `tables/per_cell_markers.tsv`
- `tables/per_cell_markers.md`
- `tables/flagged_samples.tsv`
- 16 per-model analyses with rewritten / filled values-qualitative
  sections (full list above)
- All other `analyses/*.md` files: YAML and `## Markers` section
  regenerated against corpus-v2 (numbers unchanged for cells already in
  probe-v2; 2 new freeflow cells added where applicable)
