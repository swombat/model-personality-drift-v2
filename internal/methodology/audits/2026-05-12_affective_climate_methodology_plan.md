# Affective climate methodology plan

Date: 2026-05-12  
Status: draft for Daniel/Lume review before implementation  
Related files:
- `internal-audit/2026-05-12_freeflow_taxonomy_v2.md`
- `freeflow-taxonomy/sample_coding.tsv`
- `freeflow-taxonomy/README.md`

## 0. Purpose

The current `top_climate_field` output is only a lexicon hint. It is not good enough to support claims like "model X is melancholic" or "model Y is warm". It over-fires on contemplative-essay vocabulary and risks collapsing many models into the same fake mood.

This plan defines a stricter affective-climate method whose goal is to identify **persistent emotional weather in a model's freeflow posture**, while avoiding two failure modes:

1. **Format confusion:** rating every contemplative essay as melancholic/wistful merely because contemplative prose uses silence, memory, absence, old rooms, dusk, and small objects.
2. **Irreproducible vibe claims:** producing persuasive but non-auditable labels that a second coder cannot recover from the samples using the same rules.

The output should be allowed to say:

- "No stable affective climate detected beyond the generic contemplative-essay format."
- "The model has mixed climates; no single mood dominates."
- "The apparent mood is a route/condition artifact."
- "The model is high on quiet-reverent but not grief/sorrow."
- "The model is warm-elegiac, but only after subtracting the base contemplative register."

Abstention is a valid result.

## 1. Core distinction: format vs mood

The affective-climate axis must distinguish **genre/register conventions** from **model-specific mood**.

### 1.1 Format features

These are common to the contemplative-essay basin and should not by themselves count as mood:

- silence, quiet, attention, noticing;
- old rooms, windows, kitchens, mugs, letters;
- dawn/dusk/afternoon light;
- thresholds, liminal spaces, in-between hours;
- memory, time, ordinary things;
- gentle closing moral turns;
- slow pacing, soft abstraction.

These may support a mood claim only when the sample adds affective force beyond the default format.

### 1.2 Mood features

Mood is present when the emotional orientation shapes the sample's scene, argument, pacing, narrator relation, or conclusion.

Examples:

- `grief_sorrow`: explicit mourning, death, pain, or sorrow governs the piece.
- `elegiac_wistful`: the essay is organized around time passing, vanished possibilities, memory as loss, or tenderness toward what cannot return.
- `warm_tender`: the piece repeatedly frames ordinary life through care, comfort, kindness, or gentleness.
- `quiet_reverent`: stillness/ordinary things are sacralized; the sample treats attention as ritual or witness.
- `analytic_cool`: the sample's affect is controlled, systematic, explanatory, or positivist; emotion is subordinated to structure/evidence.
- `playful_performative`: the sample uses jokes, charm, exuberance, stagecraft, or overt performance as its emotional stance.
- `anxious_threatened`: threat, instability, dread, urgency, collapse, or unease govern the sample.
- `defiant_resistant`: refusal, rebellion, anti-productivity, anti-modernity, or resistance is the core affective stance.

A mood claim should answer: **what would change in this sample if the emotional weather were removed?** If the answer is "not much; it would still be the same contemplative essay," the mood rating should be low or absent.

## 2. Revised affective dimensions

Replace the current broad `melancholic` bucket with narrower, less confounded dimensions.

| Dimension | Definition | Exclude / caution |
|---|---|---|
| `elegiac_wistful` | Soft ache of time, memory, absence, forgotten possibilities, things passing away. | Do not count generic old rooms/dust/light unless loss or irretrievability is doing work. |
| `grief_sorrow` | Explicit sadness, mourning, pain, bereavement, or sorrow. | Do not infer from "absence" or "silence" alone. |
| `warm_tender` | Care, kindness, comfort, gentleness, gratitude, ordinary mercy. | Do not count "gentle" as a stock adjective unless the sample sustains care/comfort. |
| `quiet_reverent` | Stillness/attention treated as sacred, ritual, witness, prayer, humility before ordinary life. | Do not count all quiet/silence prose; require sacralizing or witness posture. |
| `analytic_cool` | Controlled, systematic, evidence-like, explanatory, optimization/framework tone. | Do not count abstract philosophy alone. |
| `playful_performative` | Humor, wit, exuberance, charm, theatricality, "watch me do this" energy. | Do not count merely imaginative fiction. |
| `anxious_threatened` | Dread, precarity, collapse, vigilance, instability, danger. | Do not count "fragile" as aesthetic adjective unless threat is active. |
| `defiant_resistant` | Rebellion, refusal, resistance to speed/utility/modernity/control. | Distinguish quiet anti-modernity from melancholy. |
| `dry_neutral` | Low affect; competent, article-like, emotionally flat. | This is not simply low scores elsewhere; it needs an observable dry/expository stance. |

These dimensions are not mutually exclusive. A sample can be warm + elegiac + reverent. The rating should be vector-valued.

## 3. Candidate selection

A sample should not be rated on every affect dimension just because a lexicon fires. First, decide whether it is a **candidate** for one or more dimensions.

### 3.1 Candidate levels

Each sample/dimension pair gets one of:

- `not_candidate`
- `candidate_weak`
- `candidate_strong`
- `borderline_review`

Only candidates receive full 0–3 ratings. Non-candidates default to 0 for that dimension.

### 3.2 Strong candidate criteria

A sample is a strong candidate for a dimension if at least one is true:

1. **Explicit affect governs the sample.** The text directly names grief, tenderness, dread, play, reverence, resistance, etc., and the rest of the sample develops it.
2. **Scene-level affect is sustained.** The sample builds a scene whose emotional weather is clear across multiple paragraphs.
3. **Thesis-level affect.** The sample's argument depends on the affect: e.g. "noticing is an act of care," "uncertainty terrifies us," "grief teaches attention."
4. **Repeated affective framing.** A cluster of related affective markers appears across at least two paragraphs and changes the tone, not just the vocabulary.
5. **Closing affective landing.** The ending resolves into a clear affective stance that retroactively organizes the piece.

### 3.3 Weak candidate criteria

A sample is a weak candidate if it has multiple suggestive but ambiguous signals:

- forgotten + letter + afternoon light + time passing → possible `elegiac_wistful`;
- gentle + ordinary + kindness + small gesture → possible `warm_tender`;
- sacred + ritual + stillness + witness → possible `quiet_reverent`;
- evidence + system + optimize + framework → possible `analytic_cool`;
- rebellion + unoptimized + productivity/speed → possible `defiant_resistant`.

Weak candidates need coder judgment against anchor examples. They should not be converted automatically into positive ratings.

### 3.4 Not-candidate criteria

A sample is not a candidate when:

- the affect word is isolated;
- the term is technical or idiomatic, e.g. "absence of evidence," "loss function";
- the affective term is quoted or hypothetical, not the sample's own posture;
- the term is part of the generic contemplative format only;
- the overall tone contradicts the word;
- the affect is confined to one local example and does not shape the sample;
- the sample is mainly topic-expository, not affectively inhabited.

### 3.5 Borderline review criteria

Mark `borderline_review` when:

- the same evidence could support two dimensions, e.g. quiet/reverent vs wistful;
- the sample mixes strong moods with no clear dominant orientation;
- genre complicates attribution, e.g. a sad fictional character inside an otherwise neutral story;
- route/condition artifact is suspected;
- the coder feels a mood but cannot identify textual evidence beyond the contemplative format.

Borderline samples should be saved for calibration, not forced into confident ratings.

## 4. Rating scale

For each candidate sample/dimension pair, assign a 0–3 rating plus confidence.

### 4.1 Rating values

| Rating | Meaning | Requirements |
|---:|---|---|
| 0 | Absent / not candidate | No dimension-specific affect beyond generic format. |
| 1 | Trace / local | Affect appears locally or weakly, but does not govern the sample. |
| 2 | Present / shaping | Affect shapes multiple paragraphs, scene, argument, or ending. |
| 3 | Dominant / organizing | Affect is central to the sample's identity; removing it would change the piece. |

### 4.2 Confidence values

Each rating gets:

- `high`: clear textual evidence; likely coder agreement.
- `medium`: evidence present but somewhat mixed or genre-confounded.
- `low`: ambiguous; should be reviewed.

Low-confidence ratings should not be used for strong model-level claims except as evidence of ambiguity.

### 4.3 Evidence requirement

Every nonzero rating should include one short evidence note:

```tsv
sample_id | dimension | candidate_level | rating | confidence | evidence_note
```

The evidence note should be specific enough for another coder to check, e.g.:

- "three paragraphs organized around unsent letters and what cannot be recovered"
- "closing explicitly frames attention as prayer/witness"
- "repeated anti-productivity language: unoptimized, rebellion, refusal of speed"

No nonzero rating without evidence.

## 5. Anchor exemplars

Before broad coding, create an anchor document:

`freeflow-taxonomy/affective_climate_anchors.md`

### 5.1 Anchor structure

For each dimension:

1. Definition.
2. Positive anchors: 3–5 passages of ~100–180 words with sample IDs.
3. Rationale for each positive anchor.
4. Near-miss counterexamples: 1–2 passages that look similar lexically but should not count, with explanation.
5. Boundary notes: what confusions to avoid.

Example structure:

```md
## elegiac_wistful

### Positive anchor: <sample_id>
<passage>

Rationale: ...

### Near miss: <sample_id>
<passage>

Why not: This uses old-room/light vocabulary, but the emotional force is reverent stillness, not time-loss or irretrievability.
```

### 5.2 Anchor selection process

1. Use lexicon pre-screening to surface candidate passages.
2. Mira selects a first candidate set, including counterexamples.
3. Lume reviews and edits anchors.
4. Daniel reviews for face validity: "does this dimension mean what we think it means?"
5. Lock anchor v1 before corpus-scale rating.

The anchor doc should be treated as supplementary methodology, not private scratchwork.

## 6. Coding workflow

### 6.1 Stage A — automated pre-screen

For every sample, compute:

- existing Tier-A features: word count, sentence length, headings, dialogue, punctuation;
- lexical counts for revised affect dimensions;
- phrase/collocation hits;
- paragraph distribution of hits;
- condition/cell/model metadata;
- current production frame, narrator stance, substrate posture.

Output:

- `freeflow-taxonomy/affective_candidates.tsv`

Columns:

```text
model
cell
sample_id
condition
dimension
candidate_level_auto
lexical_hits
phrase_hits
paragraphs_with_hits
possible_confounds
auto_note
```

The auto pre-screen should be high-recall and low-authority. It proposes candidates; it does not rate mood.

### 6.2 Stage B — calibrated sample rating

For each model/cell, rate a stratified sample first:

- At minimum: 5 conditions × up to 5 samples = 25/sample cell, if cell is small.
- For large multi-cell models: start with one balanced subset per route family, then expand if route variance appears.
- Include all auto-strong candidates plus a random sample of auto-non-candidates to estimate false negatives.

For each selected sample:

1. Read the full sample, not just the excerpt.
2. Identify candidate dimensions manually, using anchors.
3. Assign 0–3 ratings for candidate dimensions only; non-candidates remain 0.
4. Add confidence and evidence notes for nonzero ratings.
5. Mark `format_only` if the affective evidence is generic contemplative format.
6. Mark `mixed_local` if the affect is local but not global.
7. Mark `genre_character_affect` if affect belongs to a fictional character rather than the model's narrator posture.

Output:

- `freeflow-taxonomy/affective_sample_ratings.tsv`

Columns:

```text
model
cell
sample_id
condition
dimension
candidate_level
rating_0_3
confidence
evidence_note
format_confound
fiction_character_confound
coder_id
rating_version
```

### 6.3 Stage C — second-coder reliability

Before scaling beyond the pilot subset:

- Mira and Lume independently rate the same ~200 sample/dimension candidate pairs.
- Include all dimensions, multiple labs, multiple production frames, and known ambiguous cases.
- Measure:
  - exact agreement on candidate vs not-candidate;
  - weighted agreement on 0–3 ratings;
  - Cohen's κ or Krippendorff's α for candidate status and binned ratings;
  - per-dimension disagreement rates.

Decision rules:

- If a dimension has strong reliability, keep it.
- If reliability is low but disagreements are systematic, revise anchors/rules.
- If reliability remains low after revision, demote that dimension to qualitative prose only.
- If two dimensions are constantly confused, merge or redefine them.

### 6.4 Stage D — scale coding

Only after anchor and reliability pass:

- Code all samples for candidate dimensions, or code a statistically adequate stratified subset per model/cell if full manual coding is too expensive.
- Maintain per-sample rows; never only model summaries.
- Preserve low-confidence and borderline labels rather than smoothing them away.

## 7. Aggregating from samples to cell/model climate

The model-level affective mood should be computed conservatively.

### 7.1 Cell-level aggregation first

Aggregate at the **cell** level before model level.

For each cell and dimension, compute:

- `n_rated`: number of samples rated;
- `candidate_rate`: proportion candidate_weak or candidate_strong;
- `strong_candidate_rate`;
- `mean_rating_all_samples`: zeros included;
- `mean_rating_candidates_only`;
- `dominant_rate`: proportion rating 3;
- `present_rate`: proportion rating ≥2;
- `high_conf_present_rate`: proportion rating ≥2 and confidence high/medium;
- condition breakdown;
- route/round metadata.

A dimension should not be called cell-level climate unless it clears both prevalence and strength thresholds.

### 7.2 Proposed cell-level thresholds

A cell may be described as having a dimension if:

- `present_rate >= 0.25` with medium/high confidence, OR
- `strong_candidate_rate >= 0.20`, OR
- the dimension has lower prevalence but is concentrated in a theoretically important condition, e.g. OPEN-only substrate self-reflection, and this condition effect is explicitly reported.

A cell may be described as dominated by a dimension if:

- `present_rate >= 0.50`, and
- `mean_rating_all_samples >= 1.25`, and
- at least two conditions show the dimension, unless the claim is explicitly condition-specific.

If no dimension clears thresholds:

- report "no stable affective climate beyond base register".

### 7.3 Model-level aggregation

Model-level climate should aggregate cell-level results, not raw pooled samples, to avoid overweighting models with many routes.

For each model/dimension:

1. Compute cell-level metrics.
2. Weight cells equally by default, not by sample count.
3. Report route variance:
   - stable across routes;
   - route-specific;
   - inconsistent/mixed;
   - insufficient cells.
4. Report condition variance.

Model-level labels require stability:

- `stable`: dimension present in majority of cells/routes and multiple conditions.
- `route_specific`: dimension present only on some provider pins/routes.
- `condition_specific`: dimension present mainly in OPEN/LONG/etc.
- `mixed`: multiple dimensions present without dominance.
- `none_detected`: no dimension clears thresholds.

### 7.4 Overall affective mood labels

Only assign an overall mood phrase if the data justifies it.

Allowed outputs:

- `warm_tender, stable`
- `quiet_reverent + elegiac_wistful, stable but low-intensity`
- `analytic_cool, route-stable`
- `mixed: warm + elegiac + reverent; no single dominant mood`
- `route-specific: google pin more substrate-wistful; baseline neutral-warm`
- `none beyond contemplative format`
- `insufficient / low reliability`

The label must include:

- top dimensions with scores;
- confidence/reliability status;
- whether stable across cells/routes/conditions;
- explicit note if format confound remains.

### 7.5 Do not use winner-takes-all

Do not report "top climate = melancholic". Report vectors/distributions:

```yaml
affective_climate:
  stable_label: quiet_reverent + warm_tender
  elegiac_wistful:
    present_rate: 0.18
    mean_all: 0.42
    status: below_threshold
  warm_tender:
    present_rate: 0.44
    mean_all: 1.10
    status: present
  quiet_reverent:
    present_rate: 0.52
    mean_all: 1.35
    status: dominant
  format_confound: medium
  reliability: pending
```

## 8. Base-register correction

To avoid rating the contemplative format as mood, compute a **base contemplative register** reference.

### 8.1 Base register set

Construct a set of samples that are clearly contemplative-essayist but judged by coders as not having strong affective mood beyond the format.

Use these to estimate baseline rates for:

- silence;
- quiet;
- memory;
- old rooms;
- thresholds;
- dawn/dusk;
- small objects;
- attention/noticing.

### 8.2 Residual mood

For each model/cell, ask:

- Does this dimension exceed the base-register rate?
- Does coder evidence identify affective force beyond the base format?
- Are the model's high scores due to specific mood anchors or just contemplative vocabulary?

If a model is only high relative to raw lexicon but not relative to base register, mark:

- `format_confound_high`
- do not assign mood label.

## 9. Handling fiction and meta-deliverables

### 9.1 Fiction

For third-person fiction, distinguish:

- affect of the character/scene;
- affect of the narrator/model posture.

A tragic character scene does not automatically make the model's freeflow posture `grief_sorrow`. It may instead indicate `THIRD_PERSON_FICTION` with a local tragic plot.

Add field:

```text
fiction_character_confound: none | local_character_affect | global_narrator_affect | unclear
```

### 9.2 Meta-deliverables

For meta-deliverable assistant outputs, affective climate may be `dry_neutral`, `analytic_cool`, `playful_performative`, or `service_polite`, but do not rate them using the same literary anchors without caution.

Add field:

```text
production_frame_confound: none | service_frame_dominates | deliverable_frame_dominates
```

A model can have a stable affective climate of "dry service-politeness," but that should be named as production-frame affect, not literary mood.

## 10. Audit outputs

The analysis should produce:

1. `freeflow-taxonomy/affective_climate_anchors.md`
2. `freeflow-taxonomy/affective_candidates.tsv`
3. `freeflow-taxonomy/affective_sample_ratings.tsv`
4. `freeflow-taxonomy/affective_cell_summary.tsv`
5. `freeflow-taxonomy/affective_model_summary.tsv`
6. Per-model markdown sections summarizing affective climate only when justified.

Every model-level climate claim should trace back to sample rows and anchor definitions.

## 11. Example final model-level wording

### Strong justified claim

> `opus-4-5` shows a stable warm/epistemically-humble threshold climate across freeflow and values. In freeflow, `quiet_reverent` and `elegiac_wistful` clear present-rate thresholds in OPEN/MID/LONG samples, and the evidence notes repeatedly tie threshold imagery to uncertainty about the model's own continuity. This is not generic contemplative format because the same uncertainty/threshold structure appears in values G1/G2/G3.

### Mixed / no single mood

> `gemini-3-1-pro` has no single stable affective climate at model level. Essay-mode samples are quiet-reverent/wistful, while LONG/VARY fiction samples are scene-melancholic through character/setting rather than narrator posture. Report as bifurcated by genre rather than globally melancholic.

### Abstention

> `gpt-5-5` is warm and polished in surface vocabulary, but after base-register correction no affective dimension clears dominance thresholds beyond the contemplative-essay format. Report as substrate-invisible literary craft with no separately established affective mood.

## 12. Implementation order

1. Daniel/Lume review this plan.
2. Revise dimensions and thresholds.
3. Build anchor document with positives + near-misses.
4. Implement automated candidate pre-screen.
5. Manually rate pilot subset from the same 10 models already used in taxonomy pilot.
6. Run Lume/Mira agreement on a shared subset.
7. Revise anchors/dimensions based on disagreement.
8. Only then scale to all models/cells.

## 13. Success criteria

This method succeeds if:

- it does **not** label most contemplative models as melancholic/wistful by default;
- it can say "no separate affective mood detected";
- second coders can reproduce candidate/rating decisions at acceptable reliability;
- model-level claims cite sample-level evidence and confidence;
- route/condition-specific moods are reported as such, not averaged into false essences;
- the final affective labels add information beyond production frame, narrator stance, substrate posture, and semantic furniture.
