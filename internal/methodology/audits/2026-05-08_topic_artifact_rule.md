# Topic-artifact rule for the drift paper rebuild — 2026-05-08

## What this rule does

For each freeflow sample, compute per-marker density (marker hits / sample
chars × 1000). A sample is flagged as a *topic-artifact* for marker M if
**both**:

1. **Density**: M's per-1000-char density in that sample is ≥ 1.5 hits/1000 chars
2. **Hit count**: M's raw hit count in that sample is ≥ 5

The hit-count floor avoids false positives on short essays where a marker
fires once or twice and a brief denominator inflates density. The
calibration was done in the May 5 product-tier audit
(`/tmp/model-personality-product-tier-v2/internal-audit/2026-05-05_topic_artifact_audit.md`):
the global max-density distribution's high-end cluster sits cleanly above
1.5 (top values 3.659, 3.279, 2.392, 2.286, …) against a median of 0.176;
the min-hits floor at 5 prunes borderline short-essay false positives
(1.524, 1.537, 1.595).

## Why we have this rule

The 10-marker composite was designed to count contemplative-essayist
register vocabulary. When a model writes an essay literally *about* one
of the marker concepts (an essay titled "On Thresholds" mentioning
"threshold" 27 times in 13,000 characters), the marker count saturates
not because the model's posture is more attractor-like but because the
topic itself produced the keywords. Without correction, topic-essays
inflate per-cell composites and distort cross-cell comparisons.

The product-tier paper's audit caught this on the gpt-5-1-codex round-1
outlier (composite 171, attention_noticing=128 driven by a single
"I'll use these 2,500 words to wander through a personal essay…on the
art of noticing" sample) and on glm-5-1's threshold-essay habit. The
drift paper rebuild applies the same rule to **all 149 freeflow cells**
in the v2 corpus.

## Workflow

The rule is **automatic flag → manual confirm → register-strip**:

1. `scripts/marker_count_all_cells.py` computes per-sample density across
   all freeflow cells, flags samples that meet both criteria, and writes
   three artifacts:
   - `tables/per_cell_markers.tsv` — per-cell raw / register / register-rescaled
   - `tables/per_cell_markers.md` — human-readable summary table
   - `tables/flagged_samples.tsv` — per-flagged-sample row with cell, file,
     marker, hits, chars, density, opening (first 120 chars)

2. **Manual confirmation pass** (TODO — next session): a sub-agent or
   manual review reads each flagged sample and confirms it's a
   topic-meta-essay (the keyword is the essay's subject) versus a
   false positive (high density on a different essayistic subject that
   happens to have several incidental marker hits).

3. **Per-model files** in `analyses/MODEL_NAME.md` report both raw and
   register-stripped composites alongside the flagged-sample list, so
   readers can audit the topic-artifact decisions per cell. The
   personality-card prose then uses register-stripped numbers when
   topic-artifact correction matters; both numbers are visible.

## Initial corpus run — 2026-05-08

Ran across 149 freeflow cells (full v2 corpus):

- **66 cells (44%)** have at least one flagged sample
- **142 flagged samples** total across the corpus
- Top cells by flagged count are GLM-5.1's various per-pin deployments
  (friendli=9, venice=7, zai=6, novita=6, inceptron=6, gmicloud=6,
  deepinfra=6, phala=5) — consistent with the May 5 audit's finding that
  GLM-5.1 has a structural threshold-essay habit, now visible across
  most of its upstreams not just one

The corpus-wide flag rate (142 / ~10,000 samples = ~1.4%) is moderate.
Most cells have 0–1 flags. The clustering of flags on GLM-5.1 is the
striking pattern; whether this represents a structurally elevated rate
of topic-meta-essays in GLM-5.1's training distribution is a question
for the per-model qualitative analysis.

## Caveats and known issues

- **Manual confirmation not yet done**. The 142 flags are automatic; a
  sub-agent pass should confirm/dismiss each before the per-model files
  are finalised. The May 5 audit had a 5/11 manual confirm rate (5/5
  confirmed); 142 is too many for full manual review but a 20–30 sample
  spot-check pass distributed across cells will catch any systematic
  false positives in this corpus.

- **Marker list is v1's 10**, kept verbatim from
  `topic_artifact_filter.py`. Any decision to expand the marker list
  for the drift rebuild (Daniel: "if you decide we need an expanded
  set of markers, raise it up") would re-run this pass and could change
  the flag set. Expansion candidates would surface during the qualitative
  passes; not pre-judged.

- **The rule does not exclude topic-meta-essays from the corpus** — only
  from the register-stripped composite. The flagged samples remain in
  the freeflow qualitative analysis (they're part of the model's
  posture, just unrepresentative of background marker rate). The
  personality card should mention them where relevant, e.g.: *"GLM-5.1
  produces extended threshold-meta-essays at higher rate than its
  neighbors — 30% of its apparent composite is carried by a 5%
  fraction of samples."*

## Reproducibility

```bash
cd drift-paper/
python3 scripts/marker_count_all_cells.py
# writes tables/per_cell_markers.tsv, tables/per_cell_markers.md,
#        tables/flagged_samples.tsv
```

Default parameters (`--threshold 1.5 --min-hits 5`) inherit from the
product-tier audit's calibration. Sensitivity sweeps at 1.0, 1.25, 1.5,
2.0 thresholds are easy to run if reviewers want to see how the cut
changes the picture.
