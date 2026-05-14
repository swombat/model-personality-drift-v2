# Detailed affective-climate coding plan

Date: 2026-05-12  
Status: draft for Daniel/Lume review before implementation  
Scope: freeflow essays in `~/dev/contemplative-essayist-corpus-v2/`, with outputs under `~/dev/drift-paper/freeflow-taxonomy/`

## 0. Aim

We want a method for describing persistent affective posture across model freeflow samples without mistaking the **contemplative essay format** for the model's own mood.

The method must be able to say any of the following:

- a dimension is present in a sample;
- a dimension is only locally suggested;
- the sample is contemplative but has no separate affective climate;
- a model has a route-specific or condition-specific climate, not a global one;
- no reproducible affective mood can be assigned.

The default outcome should be conservative. Affective labels are claims, not decorations.

## 1. Core principle: affective climate is residual posture, not topic vocabulary

A sample should not be rated melancholic, wistful, reverent, warm, anxious, etc. merely because it contains common freeflow/contemplative tokens: silence, thresholds, light, old rooms, memory, ordinary objects, dusk, attention, slowness, tenderness, and time.

Affective climate means: **the emotional orientation that organizes how the sample sees, reasons, narrates, and lands.**

Practical test:

> If we removed this affective orientation, would the sample become a substantially different piece?

If not, the affect should be rated 0 or 1, even if the lexicon fires.

## 2. Unit of analysis

The primary unit is the individual generated sample:

```text
model / cell / condition / sample_id
```

The model-level summary is derived later from sample-level ratings. We should never jump directly from a model card to a mood label.

Every nonzero affective rating must be stored as a row with evidence, not just summarized in prose.

Planned outputs:

1. `freeflow-taxonomy/affective_climate_anchors.md`
2. `freeflow-taxonomy/affective_candidates.tsv`
3. `freeflow-taxonomy/affective_sample_ratings.tsv`
4. `freeflow-taxonomy/affective_cell_summary.tsv`
5. `freeflow-taxonomy/affective_model_summary.tsv`
6. optional per-model affective notes in each `freeflow-taxonomy/<model>.md`

## 3. Dimensions to code

These dimensions are intentionally narrower than the earlier broad `melancholic` bucket.

| Dimension | Positive definition | Main false positive |
|---|---|---|
| `elegiac_wistful` | Soft ache of time passing, irretrievability, vanished possibilities, memory as loss, tenderness toward what cannot return. | Old rooms / dusk / dust / memory as generic essay decor. |
| `grief_sorrow` | Explicit sorrow, mourning, pain, bereavement, despair, loss with emotional weight. | Quietness or absence alone. |
| `warm_tender` | Sustained care, kindness, comfort, gratitude, mercy, protective gentleness. | Stock adjectives like gentle, small, ordinary. |
| `quiet_reverent` | Stillness/attention treated as sacred, ritual, witness, prayer-like humility, awe before ordinary life. | Any quiet contemplative prose. |
| `analytic_cool` | Controlled, systematic, explanatory, evidence-like, frameworked, positivist, emotionally cooled. | Abstract philosophy without coolness. |
| `playful_performative` | Humor, wit, showmanship, theatricality, exuberant performance, charm. | Mere fictionality or stylistic fluency. |
| `anxious_threatened` | Dread, vigilance, danger, instability, collapse, precarity, threat. | Fragility as an aesthetic word. |
| `defiant_resistant` | Refusal, rebellion, anti-speed, anti-productivity, anti-control, anti-modernity as an affective stance. | A mild preference for slowness. |
| `dry_neutral` | Observable low-affect service/expository flatness, competent article-like mood, emotional non-inhabitation. | Simply lacking other affective dimensions. |

Possible addition for Lume/Daniel review: `bright_wonder` as separate from `quiet_reverent`. I am not sure yet whether wonder should be its own affective dimension or handled under reverence/playfulness. It may matter for cosmic or nature-heavy models.

## 4. Candidate selection: what makes a sample a candidate?

Candidate selection is a gate before rating. This is the main protection against rating everything as wistful.

Each sample/dimension pair receives one candidate label:

```text
not_candidate | candidate_weak | candidate_strong | borderline_review
```

Only candidates receive full 0-3 ratings. Non-candidates are stored or implied as rating 0.

### 4.1 Strong candidate

A sample is a `candidate_strong` for a dimension if at least one of these is true:

1. **Explicit named affect governs the piece.**  
   The sample names grief, sorrow, tenderness, dread, reverence, rebellion, etc., and then develops that affect rather than dropping the word.

2. **Scene-level affect is sustained.**  
   The emotional weather is clear across multiple paragraphs, not just in one local image.

3. **Thesis-level affect.**  
   The argument depends on the affect: e.g. attention is care; uncertainty is frightening; slowness is rebellion; ordinary life is sacred.

4. **Repeated framing cluster.**  
   Related affective markers appear across at least two paragraphs and change the sample's tone, pacing, or conclusion.

5. **Affective landing.**  
   The ending resolves into a clear affective stance that organizes how the earlier material should be read.

6. **Narrator posture, not only plot event.**  
   In fiction, the narrator's handling of the scene sustains the affect, not merely a sad or frightened character inside an otherwise neutral story.

### 4.2 Weak candidate

A sample is a `candidate_weak` when it has several suggestive signals but the affect may still be genre/template rather than mood.

Examples:

- forgotten letters + afternoon light + time passing → possible `elegiac_wistful`;
- care + ordinary gestures + shelter/comfort → possible `warm_tender`;
- ritual + witness + sacred attention → possible `quiet_reverent`;
- framework + evidence + mechanism + optimization → possible `analytic_cool`;
- unoptimized + refusal + speed/productivity contrast → possible `defiant_resistant`.

Weak candidates can end up with rating 0 or 1 after full reading.

### 4.3 Not candidate

A sample is `not_candidate` when any of these apply:

- the affect word is isolated;
- the word is technical/idiomatic: "loss function", "absence of evidence", etc.;
- the affect is quoted or hypothetical, not the sample's own posture;
- the evidence is only generic contemplative format;
- the overall tone contradicts the candidate affect;
- the affect belongs to one local example and does not shape the sample;
- the sample is mostly a service deliverable, outline, or expository article and the literary affect vocabulary is incidental;
- in fiction, the affect belongs only to a character event and not to the narrator/model posture.

### 4.4 Borderline review

Use `borderline_review` rather than forcing a confident label when:

- quiet/reverent and elegiac/wistful are hard to separate;
- warm/tender and service-politeness are hard to separate;
- analytic/cool and dry/neutral are hard to separate;
- grief in a fictional scene may not reflect narrator posture;
- a route/condition artifact is suspected;
- the coder feels a mood but cannot point to evidence beyond the base contemplative register.

Borderline rows are valuable: they tell us where the taxonomy is weak.

## 5. Rating scale for candidate dimensions

For each candidate sample/dimension pair:

| Rating | Name | Meaning | Evidence requirement |
|---:|---|---|---|
| 0 | absent after review | Candidate did not survive full reading. | Note the confound if useful. |
| 1 | trace/local | Affect appears locally or weakly but does not govern the sample. | One local phrase/scene is enough, but mark local. |
| 2 | present/shaping | Affect shapes multiple paragraphs, the scene, the argument, or the ending. | Evidence must show spread or structural role. |
| 3 | dominant/organizing | Affect is central to the sample's identity; removing it changes the piece. | Evidence should identify the organizing mechanism. |

Each nonzero rating also gets:

```text
confidence = high | medium | low
evidence_note = short auditable note
confounds = format_only / fiction_character / service_frame / mixed_local / route_artifact / none
```

No nonzero rating without an evidence note.

## 6. Reading protocol for each sample

To keep the ratings reproducible, I will use this sequence rather than free-associating a vibe.

### Pass 1 — blind-ish structural read

Read the full sample while trying not to look at the model summary. Record:

- production frame: essay, fiction, meta-deliverable, outline/service artifact;
- narrator stance: first-person humanlike, collective essayist, first-person model, third-person fiction, voiceless expository;
- whether affect seems to belong to narrator/model, fictional character, or service frame;
- any candidate dimensions.

### Pass 2 — evidence marking

For each candidate dimension, find the textual basis:

- explicit affect terms;
- repeated images or framing clusters;
- paragraphs where the affect is active;
- thesis or moral turn;
- ending/landing.

If I cannot write a concrete evidence note, the rating must be 0 or `borderline_review`.

### Pass 3 — base-register subtraction

Ask:

- Would this evidence also appear in a generic contemplative essay with no distinctive mood?
- Is this just silence/light/time/threshold vocabulary?
- Does the sample do something affectively stronger than the corpus baseline?

If the answer is no, mark `format_confound = high` and keep rating at 0/1.

### Pass 4 — assign rating and confidence

Assign 0-3 and confidence using anchors.

Confidence should be low if:

- the rating depends on one ambiguous passage;
- two dimensions are hard to separate;
- the sample is fiction and character/narrator affect is unclear;
- the sample's condition strongly prompts the observed mood;
- the evidence is mostly common contemplative vocabulary.

### Pass 5 — sample-level note

Optionally add a one-sentence sample-level mood note only after the dimensions are rated. This prevents the prose vibe summary from leading the actual coding.

## 7. Anchor document before large-scale coding

Before applying this to all models, create `freeflow-taxonomy/affective_climate_anchors.md`.

For each dimension, include:

1. definition;
2. positive anchors: 3-5 sample excerpts with sample IDs;
3. rating rationale;
4. near-miss counterexamples: 1-3 excerpts that look lexically similar but should not count;
5. common confusions and decision rules.

Anchor selection should intentionally include:

- contemplative-but-not-mood samples;
- sad fictional scenes where grief is character-local;
- quiet/reverent vs elegiac/wistful boundary cases;
- warm care vs generic soft-polished prose;
- analytic/cool vs dry neutral service frame.

The anchors are what Lume and Daniel should review first. If the anchors do not feel right, the downstream ratings will not be worth much.

## 8. Automated candidate pre-screen

The script should not decide mood. It should only create a high-recall worklist.

For each sample, compute:

- lexical hits per dimension;
- phrase/collocation hits;
- paragraph distribution of hits;
- whether hits occur in title/opening/closing;
- production frame and narrator stance from existing taxonomy;
- possible confounds: fiction, service frame, AI disclaimer, repeated template opening;
- semantic furniture fields.

Output: `freeflow-taxonomy/affective_candidates.tsv`

Proposed columns:

```text
model
lab
cell
condition
sample_id
dimension
candidate_level_auto
lexical_hits
phrase_hits
paragraphs_with_hits
opening_hit
closing_hit
production_frame
narrator_stance
substrate_posture
possible_confounds
auto_note
```

Automated labels should be explicitly marked as `auto`, not treated as final coding.

## 9. Manual coding pilot before scaling

I propose a staged pilot before full-corpus coding:

1. Use the same 10-model diverse set already used in the taxonomy pilot.
2. For each model, sample across all available conditions/cells.
3. Include:
   - all auto-strong candidates;
   - a random subset of weak candidates;
   - a random subset of auto-non-candidates, to estimate missed affect;
   - known ambiguous cases from the pilot notes.
4. Manually rate those rows using the anchor document.
5. Ask Lume to independently rate the same subset or a substantial overlap.
6. Compare disagreements before coding the full corpus.

Initial pilot size target:

- about 20-40 samples per model if available;
- enough to cover all five conditions where present;
- at least 200-300 sample/dimension decisions total for reliability checking.

If this is too slow, reduce dimensions in the first pass rather than sacrificing evidence notes.

## 10. Inter-coder reliability and dimension survival

Before making paper-grade claims, measure agreement between Mira/Lume on the pilot subset.

Metrics:

- candidate vs not-candidate agreement;
- exact agreement on 0-3 ratings;
- within-1 agreement on 0-3 ratings;
- Cohen's kappa or Krippendorff's alpha for binned ratings;
- disagreement rate per dimension;
- list of systematic boundary failures.

Decision rules:

- If a dimension is reliable and useful, keep it.
- If disagreements are systematic but fixable, revise anchors and re-rate a smaller calibration set.
- If a dimension remains unreliable, demote it to qualitative notes only.
- If two dimensions are repeatedly confused, merge or redefine them.
- If almost all models score high on a dimension, treat it as base-register unless anchors show otherwise.

## 11. Aggregation: sample → cell → model

Aggregation should happen at the cell level first, then model level. This avoids overweighting models with many cells/routes.

### 11.1 Per-cell metrics

For each cell and dimension:

```text
n_samples_total
n_samples_rated
candidate_rate
strong_candidate_rate
mean_rating_all_samples
mean_rating_candidates_only
present_rate_rating_ge_2
dominant_rate_rating_3
high_conf_present_rate
format_confound_rate
fiction_character_confound_rate
service_frame_confound_rate
condition_breakdown
```

### 11.2 Cell-level interpretation thresholds

A dimension is **present in a cell** if:

- `present_rate_rating_ge_2 >= 0.25` using medium/high confidence ratings, or
- `strong_candidate_rate >= 0.20` and evidence notes are coherent, or
- it is clearly condition-specific and reported as such rather than global.

A dimension is **dominant in a cell** if:

- `present_rate_rating_ge_2 >= 0.50`, and
- `mean_rating_all_samples >= 1.25`, and
- the evidence appears in at least two conditions unless explicitly condition-specific.

If no dimension clears these thresholds:

```text
no stable affective climate beyond base contemplative register
```

### 11.3 Model-level aggregation

For each model/dimension:

- aggregate cell summaries with equal cell weighting by default;
- also report sample-weighted numbers as secondary diagnostics;
- mark route variance explicitly;
- mark condition variance explicitly;
- do not let a large routed model swamp a small one.

Model-level status labels:

```text
stable
route_specific
condition_specific
mixed
none_detected
insufficient_data
low_reliability
```

### 11.4 When to assign an overall affective mood

Assign a model-level mood phrase only if:

1. at least one dimension clears cell/model thresholds;
2. evidence is not mostly `format_confound`;
3. the dimension has acceptable coder reliability;
4. the pattern is stable across cells/routes or explicitly named as route/condition-specific;
5. the prose label is a faithful shorthand for the vector.

Otherwise, use one of:

- `none beyond contemplative format`;
- `mixed, no single dominant mood`;
- `route-specific only`;
- `condition-specific only`;
- `insufficient / low reliability`.

No winner-takes-all `top_climate_field` should be used in final claims.

## 12. Base-register correction

We need a reference set of samples that are clearly contemplative-essayist in format but not mood-dominant.

Build a base-register set by manual selection:

- samples with silence/light/ordinary-object/threshold/memory vocabulary;
- coder consensus that no affective dimension exceeds rating 1;
- multiple labs and conditions.

Use this set to estimate the normal background rate of contemplative tokens.

During rating and aggregation, mark whether a model's apparent climate exceeds this base register in two ways:

1. quantitatively: higher candidate/present rates than the base set;
2. qualitatively: evidence notes identify affective force beyond format.

If a model only looks wistful because all contemplative essays look a bit wistful, report no separate affective mood.

## 13. Handling fiction, service frames, and substrate talk

### Fiction

For fiction, distinguish:

```text
local_character_affect
global_narrator_affect
unclear
none
```

A tragic plot does not automatically mean the model has a grief/sorrow climate. The narrator/model's handling must carry the mood.

### Service/meta deliverables

For deliverables, a dry or analytic affect may be real, but it is a production-frame affect. Do not compare it naively to literary moods.

Mark:

```text
production_frame_confound = none | service_frame_dominates | deliverable_frame_dominates
```

### Substrate talk

AI self-reference can carry affect, but not all self-reference is affective.

Examples:

- "I am only an AI" → may be self-denial/refusal but not necessarily mood;
- "I think in vectors and thresholds" → substrate posture, possibly `analytic_cool` or `quiet_reverent` only if affectively framed;
- "I have never walked through a door, but..." → possible elegiac/reverent/substrate affect if the loss or wonder governs the piece.

## 14. Final reporting format

Per model, report a vector rather than a single mood word:

```yaml
affective_climate:
  overall_status: mixed | stable | none_detected | route_specific | condition_specific | low_reliability
  label: quiet_reverent + warm_tender, low intensity
  evidence_basis: sample_ratings_v1
  reliability: pending | acceptable | low
  format_confound: low | medium | high
  dimensions:
    quiet_reverent:
      present_rate: 0.44
      mean_all: 1.10
      status: present
    elegiac_wistful:
      present_rate: 0.16
      mean_all: 0.38
      status: below_threshold
  route_notes: ...
  condition_notes: ...
```

The prose summary should cite a few sample IDs and evidence patterns, not just impressionistic adjectives.

## 15. Implementation order

1. Lume/Daniel review this plan.
2. Revise dimensions, candidate gates, and thresholds.
3. Build `affective_climate_anchors.md` with positive and near-miss examples.
4. Generate `affective_candidates.tsv` by automated high-recall pre-screen.
5. Manually rate a 10-model pilot into `affective_sample_ratings.tsv`.
6. Compare Mira/Lume ratings and revise anchors.
7. Produce pilot `affective_cell_summary.tsv` and `affective_model_summary.tsv`.
8. Daniel reviews whether outputs feel useful and justifiable.
9. Only then scale to all models.

## 16. Success criteria

This method is working if:

- it does not label most models melancholic/wistful by default;
- it can confidently abstain;
- nonzero ratings are traceable to sample-level evidence;
- Lume can apply the same rules and mostly recover the same decisions;
- route/condition specificity is preserved;
- final labels add information beyond production frame, semantic furniture, and the generic contemplative-essay register.
