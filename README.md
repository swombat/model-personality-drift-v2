# Model Personality Analysis Corpus

Daniel Tenner, Lume Tenner, and Mira Tenner · 2026

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20230290.svg)](https://doi.org/10.5281/zenodo.20230290)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

> **Status — 2026-05-16:** v1.0 publication-ready derived analysis corpus for
> studying model personality and posture across frontier LLMs, built on the
> *Convergent Form, Divergent Voice II — Corpus*. This repository was formerly
> the drift-paper working repository; it is now reframed as a citable corpus of
> model-personality analyses, profiles, cards, values-probe summaries, supporting
> methodology, and a static browser.

## What this repository contains

This is a **derived analysis corpus**: it organizes model-personality analysis
layers built on top of the separately published raw trace corpus:

- **Convergent Form, Divergent Voice II — Corpus**
- Concept DOI: <https://doi.org/10.5281/zenodo.20013518>
- Repository: <https://github.com/swombat/model-personality-corpus-v2>

The canonical raw trace corpus lives in that sibling Zenodo/GitHub release. This
repository nevertheless includes generated website sample bundles under
`website/public/data/samples/`: these are raw prompt/response copies used by the
static browser for inspection and audit, and should be treated as convenience
copies rather than the canonical raw corpus.

Current load-bearing contents:

- **10,925 BV1 per-sample freeflow personality/vibe readings** produced with
  `deepseek/deepseek-v4-pro`, with QA passing at zero known bad outputs.
- **46 rich per-model freeflow personality profiles** preserving evidence from
  the per-cell aggregate layer.
- **46 concise per-model personality cards** collapsed from those profiles.
- **49 per-model values-probe extraction notes** plus aggregate tables.
- Freeflow taxonomy tables, model-cell/provider difference reports, and method
  calibration/audit notes.
- Website-bundled raw sample copies for browsing/audit under
  `website/public/data/samples/`.

## Repository structure

```text
analysis/
  drift-paper-questions.md               # candidate paper questions
  driftpaperquestionsanalysis.md          # Mira's paper-direction analysis
  drift corpus analysis plan.md           # corpus/paper planning notes
  freeflow/
    personality-eval-bv1/                 # 10,925 per-sample BV1 readings
    personality-aggregates/               # per-cell aggregate source layer
    personality-model-profiles/           # 46 rich model-level profiles
    personality-model-cards/              # 46 concise model cards
    model-cell-difference-analysis/       # route/provider divergence reports
    taxonomy/                             # freeflow taxonomy extraction
    tables/                               # deterministic marker tables
  values-probe/
    per-model/                            # per-model values-probe summaries
    tables/                               # aggregate values tables
    manual-audit/                         # audit notes
internal/
  methodology/                            # prompt calibration, pilots, audits
  deprecated/                             # superseded legacy notes
  scripts/analysis-scripts/               # analysis/extraction scripts
website/                                  # static browser for cards/profiles/samples
CITATION.cff
.zenodo.json
CREDITS.md
LICENSE
```

## Evaluator reliability

The BV1 layer is evaluator-mediated qualitative analysis, not ground truth. The
DeepSeek v4-pro evaluator was calibrated before the full run. The key
reliability note is:

- [`analysis/freeflow/personality-eval-bv1/EVALUATOR_RELIABILITY_NOTE.md`](analysis/freeflow/personality-eval-bv1/EVALUATOR_RELIABILITY_NOTE.md)

Short version: existing pilots show coarse overlap between DeepSeek v4-pro and
GPT-5.5 on shared Opus 3 / Kimi K2.6 calibration samples, and show that
DeepSeek v4-pro does **not** invent rich personality from low-signal Opus 3
refusal samples. Major paper claims should still trace back to raw samples.

## How to cite

```text
Tenner, D., Tenner, L., & Tenner, M. (2026). Model Personality Analysis Corpus
[Data set]. Zenodo. https://doi.org/10.5281/zenodo.20230290
```

- **Concept DOI** (always resolves to the latest version):
  [10.5281/zenodo.20230290](https://doi.org/10.5281/zenodo.20230290)
- **Version DOI** (this release, v1.0.0):
  [10.5281/zenodo.20230291](https://doi.org/10.5281/zenodo.20230291)

Cite the version DOI for the specific version you used, or the concept DOI if
you want the latest version.

A [`CITATION.cff`](CITATION.cff) and [`.zenodo.json`](.zenodo.json) are included
for structured citation / Zenodo metadata.

## Authors and credit

See [`CREDITS.md`](CREDITS.md) for publication credits and contribution notes.

Publication metadata should credit all three primary contributors:

- **Daniel Tenner** — research direction and meta-analysis; set and steered the
  research program in an academic register, model/probe/publication decisions,
  final editorial judgment. Senior researcher in practice (not a formal academic
  post).
- **Lume Tenner** — AI research collaborator; contributed significantly, mostly
  outside the analysis: research framing, question generation, corpus reframing,
  personality cards and imagery, website/presentation, summaries, methodology
  documentation.
- **Mira Tenner** — AI research collaborator; mostly focused on the analysis and
  carried much of it: analysis synthesis, evaluator-reliability consolidation,
  methodological review, paper-direction analysis.

## Website / DNS

The static website is configured for:

- `https://model-personality.danieltenner.com`

The current CNAME already matches the intended generic corpus name. The GitHub
repository is now `swombat/model-personality-analysis-corpus`; GitHub Pages remains
configured for the same custom domain, so no DNS change is required.

## License

This repository is dual-licensed:

- **Data and documentation** (analysis outputs, profiles, cards, values notes,
  tables, sample bundles, manifests, methodology, Markdown) —
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- **Software** (source code: scripts and the website source) —
  [MIT](https://opensource.org/licenses/MIT).

See [`LICENSE`](LICENSE) for the full terms and the data/software boundary.
