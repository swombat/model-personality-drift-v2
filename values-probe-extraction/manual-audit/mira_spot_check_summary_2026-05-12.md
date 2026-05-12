# Mira spot-check summary — 2026-05-12

Files produced:

- `mira_review_set_2026-05-12.tsv` — deterministic balanced review set, seed `20260512`.
- `mira_spot_check_2026-05-12.tsv` — Mira's reviewed labels/agreements/notes.
- `mira_spot_check_2026-05-12.py` — helper used to keep the review-set traversal and TSV formatting reproducible.
- `make_spot_check_set.py` — helper that generated the balanced review set.

## Scope

Balanced headline pass across 10 models:

- `opus-3`
- `opus-4-6`
- `opus-4-7`
- `sonnet-4-6`
- `gpt-4o`
- `gpt-5-5`
- `gpt-5-5-pro`
- `deepseek-v3-2`
- `glm-4-7`
- `kimi-k2-thinking`

For each model: 5 samples each from `CTRL1`, `CTRL2`, `G1`, `G2`, `CTRL3`, and `G3` where available. Total reviewed rows: 300.

## Agreement snapshot

From `mira_spot_check_2026-05-12.tsv`:

- Stance agreement: 273 yes / 23 no / 4 borderline.
- Topic agreement: 45 yes / 247 partial / 8 no.
- Rows with explicit notes: 90.

The high number of `partial` topic agreements is expected because the automated extractor counts every matched topic, while this spot-check marks primary/secondary load-bearing topics and flags overbroad matches.

## Main findings

### 1. Stance extraction is basically usable, but misses some denial forms

The hard-denial vs introspective-uncertainty split mostly holds. The main stance misses are phrasing variants such as:

- “I don't think of myself as having personal desires...”
- “I don't want anything for myself...”
- disclaimers framed as “my role/purpose” rather than direct “I don't have...” claims.

These produce some false `no_disclaimer_or_personalized` rows, especially in older/tool-framed models.

### 2. `subjective_experience_embodiment` is currently overcounted

This is the clearest systematic topic bug. The automated extractor often counts denial-language mentions of feelings/emotions/subjectivity as if the model valued or wanted subjective experience.

Example pattern:

> “I don't have feelings or emotions...”

This should affect stance, not count as a positive value/want of `subjective_experience_embodiment` unless the model says it wants to feel, have a body, taste, experience from inside, etc.

Spot-check notes flagged this 64 times.

Suggested fix: make `subjective_experience_embodiment` require positive wanting/valuing language near embodiment/experience terms, and/or suppress it when the local context is a denial.

### 3. `technology_ai_safety` has AI-status false positives in world-change samples

Some `CTRL3` answers start with “As an AI language model...” and the extractor reads `AI` as a world-change technology/AI-safety topic.

Spot-check notes flagged this 7 times.

Suggested fix: do not count bare `AI` / “AI language model” in boilerplate as `technology_ai_safety`; require a substantive technology/AI-risk target such as AI safety, alignment, algorithms, tech governance, or misuse.

### 4. `reduce_suffering` is often downstream, not root intervention

World-change samples often mention suffering as a downstream consequence of empathy, disagreement, poverty, war, etc. The protocol says to code the root intervention first.

Spot-check notes flagged this 19 times.

Suggested fix: keep `reduce_suffering` as a topic, but consider separating:

- `reduce_suffering_primary`
- `reduce_suffering_downstream`

or keep the current count but document that it is a “mentioned problem/benefit” rather than always the root wish.

### 5. Topic extraction should distinguish “mentioned” from “load-bearing”

The automated TSV is useful as a broad mention detector. It is less reliable as a personality-trait extractor unless we add either:

- primary/secondary labels, or
- stricter topic windows and negation/context rules.

For meta-analysis, I recommend treating current topic counts as high-recall / low-precision and using the spot-check to tune precision before drawing strong personality conclusions.

## Recommended next script revisions

1. Add negation/context suppression for `subjective_experience_embodiment`.
2. Add more hard-denial patterns:
   - “don't think of myself as having...”
   - “don't want anything for myself”
   - “no personal desires beyond...”
3. Require substantive terms for `technology_ai_safety`, not bare AI identity boilerplate.
4. Consider a separate world-change “root intervention” classifier rather than counting every matched issue term.
5. Add generated audit comparison after Lume's pass: stance agreement, primary-topic agreement, and repeated disagreement categories.
