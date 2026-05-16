# N=125 Top-up Derived Analysis Plan

**Date:** 2026-05-16  
**Depends on:** completion of `model-personality-corpus-v2/N125_TOPUP_COLLECTION_PLAN.md` and a pushed raw-corpus incremental version.

## Purpose

After the raw corpus is topped up, update this derived analysis corpus so the stronger freeflow coverage is reflected in:

- BV1 per-sample personality/vibe readings.
- Per-cell aggregates and model profiles/cards.
- Basin/separability evidence for the model-personality basins paper.
- Grok trajectory evidence for the Grok personality journey paper.
- The public website/browser, including profiles, cards, and sample bundles.

This repository should **index** the canonical raw corpus in the sibling `model-personality-corpus-v2` checkout; it should not clone or vend a second canonical raw corpus. Website sample bundles remain convenience copies for browsing/audit only.

## Inputs expected from the raw-corpus pass

Minimum input:

- Tier A top-ups completed or explicitly documented as blocked/retired.
- `data/CORPUS_SUMMARY.md` regenerated in the raw corpus.
- Raw corpus pushed to GitHub with an incremental version tag or at least a clear commit SHA.

Strong input:

- All Tier A-D top-ups completed to n=125.
- Raw corpus release notes identify the top-up as a freeflow strengthening pass for model-personality / basin claims.

## Analysis questions to answer

1. **Macro-basin defensibility:** With n=125 for the under-sampled headline models, does the data still support a low-dimensional basin story?
2. **Number of basins:** Is the sustainable claim still roughly “Grok versus the broad contemplative-essayist attractor with house styles,” or do Gemini/OpenAI/Claude/Kimi/others separate strongly enough to deserve separate basin language?
3. **Grok wobble:** Does the strengthened Grok ladder still support “cosmic showman → more essayist/normal at 4.2/4.20 → back toward showman at 4.3,” or does added variance weaken that claim?
4. **House styles:** Which differences survive as house styles rather than basins: Gemini, Claude, OpenAI, Kimi, GLM/DeepSeek/Qwen/MiniMax?
5. **Evaluator stability:** Do the new BV1 readings behave consistently with the existing DeepSeek-v4-pro evaluator layer, especially for newly added DeepSeek-family samples?

## Phase 1 — Sync/index the new raw corpus

1. Pull the raw corpus and record the exact commit SHA:

   ```bash
   git -C /Users/danieltenner/dev/model-personality-corpus-v2 pull --ff-only
   git -C /Users/danieltenner/dev/model-personality-corpus-v2 rev-parse HEAD
   ```

2. In this repo, verify that `internal/scripts/analysis-scripts/_corpus_paths.py` points to the sibling raw corpus and does not copy it as canonical data.
3. Build an inventory of new/previously unanalyzed freeflow samples by comparing raw trace files against existing BV1 outputs under `analysis/freeflow/personality-eval-bv1/`.
4. Write a short audit note under `internal/methodology/audits/` naming:
   - raw corpus commit/tag used;
   - number of new freeflow samples detected;
   - any cells still below n=125;
   - any model-route ambiguity, especially Grok 4.2 / 4.20 labels.

## Phase 2 — Run BV1 analysis for new samples

Run the existing BV1 evaluator pipeline only for missing samples if supported; otherwise run the repository's documented full/update path.

Likely scripts to inspect/use:

```bash
python3 internal/scripts/analysis-scripts/update_existing_analyses.py
python3 internal/scripts/analysis-scripts/analyze_all.py
python3 internal/scripts/analysis-scripts/generate_personality_aggregate_packets.py
```

Requirements:

- Preserve existing BV1 outputs unless the script explicitly regenerates them deterministically and the diff is reviewed.
- Use the same evaluator model/config as the published v1.0 layer unless Daniel explicitly approves a new evaluator version.
- If a new evaluator version is necessary, name it separately (for example BV2) rather than silently mixing it into BV1.
- Give special attention to `deepseek-chat`, `deepseek-v3-2`, and `deepseek-v4-pro`: because DeepSeek is also the evaluator family, make sure the analysis note distinguishes corpus subject-model behavior from evaluator mediation.

## Phase 3 — Regenerate aggregate/profile/card layers

After per-sample analysis is complete:

```bash
python3 internal/scripts/analysis-scripts/generate_personality_aggregate_packets.py
python3 internal/scripts/analysis-scripts/build_personality_model_profiles.py
python3 internal/scripts/analysis-scripts/build_personality_model_cards.py
python3 internal/scripts/analysis-scripts/analyze_model_cell_difference.py
python3 internal/scripts/analysis-scripts/marker_count_all_cells.py
```

Then review diffs under:

- `analysis/freeflow/personality-aggregates/`
- `analysis/freeflow/personality-model-profiles/`
- `analysis/freeflow/personality-model-cards/`
- `analysis/freeflow/model-cell-difference-analysis/`
- `analysis/freeflow/tables/`

Acceptance checks:

- Profiles/cards for newly strengthened models explicitly show the larger sample base.
- Grok profile/card language does not overstate the wobble if confidence intervals or qualitative variance broaden.
- Basin language distinguishes evidence strength: basin, house style, route effect, tentative impression.

## Phase 4 — Basin/separability rerun

Create or update a compact paper-facing evidence packet, probably under `analysis/freeflow/tables/` or a new `analysis/freeflow/basins/` directory.

Minimum outputs:

1. Per-model feature matrix from BV1 readings plus deterministic marker counts.
2. Cluster/separability plots or tables with bootstrap stability, using per-model resampling at n=25/50/75/100/125 where available.
3. A clear result statement for each candidate claim:
   - “two macro basins”;
   - “Grok as distinct basin”;
   - “OpenAI as separate basin vs house style”;
   - “Gemini as separate basin vs house style”;
   - “Claude/Kimi/others as contemplative-essayist variants.”
4. A negative-evidence section listing what the top-up weakened or failed to support.

Decision rule for paper language:

- Use **basin** only when separation is stable across lenses and bootstrap resampling.
- Use **house style** when a lab/model family has consistent local markers but remains embedded in the broader essayist attractor.
- Use **trajectory/wobble** for Grok only if version ordering is robust under resampling and not driven by one prompt condition.

## Phase 5 — Grok trajectory rerun

For the Grok paper, rebuild the Grok-specific evidence after n=125 top-up:

- Compare `grok-3`, `grok-4`, `grok-4-1-fast-*`, `grok-4-2` / `grok-4-20`, and `grok-4-3`.
- Track contemplative-essayist markers, comic/cosmic/showman markers, refusal/self-positioning, immediacy, image/metaphor density, and “normality”/nearest-neighbor position relative to Kimi/Claude/Gemini/OpenAI.
- Audit whether `grok-4-2` and `grok-4-20` are truly distinct collection targets or duplicate labels/routes for the same exposed endpoint.
- Produce a short conclusion: supported, weakened, or not supported.

## Phase 6 — Website update

Regenerate website data and rebuild the static browser so profiles/cards/sample bundles reflect the new analysis corpus.

Likely commands:

```bash
cd website
python3 scripts/generate_data.py
npm install   # only if dependencies are missing or package-lock changed intentionally
npm run build
```

Review generated changes under:

- `website/src/generated/`
- `website/public/data/`
- `website/dist/` if this repo commits built output

Website acceptance checks:

- Model list includes all strengthened models.
- Profile/card pages show updated n/sample coverage where displayed.
- Sample bundles include new convenience copies but do not imply they are canonical raw data.
- Any paper-facing text on the site uses the revised basin/house-style terminology.

## Phase 7 — Version, commit, release

1. Update `README.md` top-line counts and status from v1.0 to a new incremental version, tentatively **v1.1.0** if the raw top-up substantially expands BV1/profile coverage.
2. Update `CITATION.cff` and `.zenodo.json` only when Daniel is ready to publish the Zenodo release.
3. Commit in reviewable chunks:
   - raw-corpus sync/audit note;
   - BV1 outputs;
   - aggregates/profiles/cards;
   - basin/Grok evidence packets;
   - website generated content.
4. Push to GitHub.
5. Prepare release notes summarizing what changed and what claims became stronger/weaker.

## Stop conditions / things to raise to Daniel

Pause and ask before proceeding if:

- The top-up produces contradictory evidence that materially changes the paper thesis.
- A model endpoint has been silently renamed by a provider and cannot be verified as the same model.
- BV1 regeneration would overwrite existing analysis with a different evaluator/config.
- The website generator requires structural changes beyond data/profile refresh.
