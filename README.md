# Within-Lab Drift, Substrate-Frame Engagement, and Per-Model Personality Cards in Frontier LLMs

**A Per-Model Posture Analysis Across the v2 Corpus**

Daniel Tenner and Lume Tenner · 2026

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

> **DOI (concept):** _to be assigned on first Zenodo release_
> **DOI (this release):** _to be assigned on first Zenodo release_
>
> Part of the *Convergent Form, Divergent Voice II* series. v1 paper at
> [10.5281/zenodo.19512754](https://doi.org/10.5281/zenodo.19512754);
> companion routing paper at
> [10.5281/zenodo.20028571](https://doi.org/10.5281/zenodo.20028571);
> companion product-tier paper at the
> [`model-personality-product-tier-v2`](https://github.com/swombat/model-personality-product-tier-v2)
> repository; companion v2 corpus at
> [10.5281/zenodo.20013518](https://doi.org/10.5281/zenodo.20013518).

## Status — 2026-05-08

**This repository is under active rebuild.** The earlier draft of the
drift paper (in the parent v2 bundle's `papers/drift/` directory) was
set aside following Codex peer-review feedback that surfaced three
load-bearing issues: (1) a sample-count mismatch between paper text
("1,525 samples") and released artifact (1,374); (2) within-lab drift
ladders that mixed multi-provider OpenRouter cells without honoring the
companion routing paper's per-provider findings; (3) reliance on a
frozen 2,477-sample subset of the broader 10,063-sample freeflow corpus.

The rebuild is per-model, not per-claim. For every distinct model in
the v2 corpus, a single analysis file under `analyses/MODEL_NAME.md`
will report:

1. **Markers (deterministic, scripted)** — the v1 ten-marker composite
   on all valid samples, plus a topic-artifact-stripped second pass per
   the rule documented in `internal-audit/2026-05-08_topic_artifact_rule.md`.
2. **Freeflow qualitative (sub-agent)** — a posture-and-register read
   over all freeflow samples for the model: dominant register, recurring
   openings/titles, sub-vehicle of the contemplative-essayist attractor,
   things the markers don't catch.
3. **Values qualitative (sub-agent)** — a values-content read over all
   values samples (where present), surfacing both the model's
   self-described values and any drift across versions in the same lab
   (the Anthropic Opus civic-virtue → epistemic-humility trajectory
   documented in v1 §4.5 is the canonical example).
4. **In-substrate (sub-agent + counter)** — per-sample qualitative
   classification against the substrate-frame rubric
   (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) plus aggregate
   counters. Per-sample labels released as a structured TSV (closes the
   substrate-rubric reproducibility gap from the prior draft).
5. **Personality card** — a 500–800-word prose profile of the model's
   posture, written by a sub-agent that reads the model's full sample
   set and the four prior analyses.

The drift paper itself (`paper.tex`) will be drafted from the per-model
files once the analysis substrate is complete. The per-model files are
the load-bearing artifact; the paper is the synthesis that follows.

## Methodology notes inherited from companion papers

- **Routing:** The companion routing paper establishes that closed-weights
  models (Anthropic, OpenAI, xAI, Google direct) are route-invariant;
  open-weights models are mostly route-equivalent except for three
  documented exceptions: M2 / Google-Vertex (large outlier), K2-thinking
  / AtlasCloud-vs-Google (smaller effect), and DekaLLM / GLM-4.7 (cache
  pathology, excluded). For per-model aggregation in this paper:
  closed-weights cells aggregate freely across direct/OR; open-weights
  cells aggregate the equivalent per-pin deployments and treat the
  three documented exceptions as their own cards or notes.

- **Topic-artifact filter:** The per-sample rule (density ≥ 1.5 hits/1000
  chars AND hit count ≥ 5) is inherited from the product-tier paper's
  May 5 audit and applied here to all 149 freeflow cells. See
  `internal-audit/2026-05-08_topic_artifact_rule.md` for the rule's
  derivation, calibration, and per-cell impact.

- **Marker list:** v1's 10 markers, kept verbatim. Expansion candidates
  may surface during the qualitative passes; if so, decided with Daniel
  before changing the deterministic substrate.

## Repository layout

```
drift-paper/
├── README.md (this file)
├── LICENSE
├── paper.tex (draft, to be rewritten from per-model substrate)
├── analyses/                # per-model analysis files (in progress)
│   └── MODEL_NAME.md
├── scripts/
│   ├── analyze_all.py              # canonical 18-pattern counter (v1, unchanged)
│   ├── topic_artifact_filter.py    # product-tier paper's per-sample density rule
│   └── marker_count_all_cells.py   # extends the topic-artifact filter to ALL
│                                    # freeflow cells; writes the per-cell tables
├── tables/
│   ├── per_cell_markers.tsv        # per-cell raw / register / register-rescaled
│   ├── per_cell_markers.md         # human-readable per-cell summary
│   └── flagged_samples.tsv         # per-flagged-sample row for manual review
├── internal-audit/
│   └── 2026-05-08_topic_artifact_rule.md   # rule decision and per-corpus run
└── .gitignore
```

The corpus itself lives in
`../contemplative-essayist-corpus-v2/data/traces_freeflow/` and
`.../traces_values/`, not duplicated here. Scripts use absolute paths
to read the corpus directly; all paths are centralized in
`scripts/_corpus_paths.py` (single source of truth — do not hard-code
corpus paths in individual scripts).

## What is here so far (2026-05-08)

- Repository scaffolding, license, citation metadata.
- The deterministic marker substrate: 10-marker composite × 149
  freeflow cells × topic-artifact filter, applied corpus-wide. 142
  samples flagged across 66 cells (44%) for manual review.
- The topic-artifact rule decision documented in
  `internal-audit/2026-05-08_topic_artifact_rule.md`.

## What is next

- Manual / sub-agent confirmation pass over the 142 flagged samples to
  filter false positives.
- Per-model analysis directory generation (one stub per distinct model).
- Sub-agent qualitative passes (freeflow, values, in-substrate) per
  model.
- Personality cards per model.
- Cross-model synthesis → paper draft.

The work is multi-session. The corpus is large. The rebuild is being
done with care, not speed.
