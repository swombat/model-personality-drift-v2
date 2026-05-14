# Freeflow personality aggregation options

This note proposes ways to aggregate the per-sample BV1 freeflow personality evaluations into per-model summaries, suitable for later display alongside values-probe results and eventual synthesis into concise model cards.

## Goal

We need an aggregation layer between:

- ~10k per-sample freeflow personality readings, and
- a 2–3 paragraph model-card section expressing “who the model is” when stripped bare of prompts.

The goal is **not** to average adjectives. It is to extract recurring, evidence-backed patterns: what the model repeatedly turns toward, how it addresses the reader, what it seems to care about, what moods and moral claims recur, and what kinds of expressive defaults appear across samples.

## Option A — Evidence-cluster aggregation

For each model, parse all BV1 sample evaluations and cluster recurring signals:

- recurring emotional tone
- recurring objects/images
- recurring moral claims
- recurring relationship to reader
- recurring genre/default mode
- recurring self/substrate stance
- recurring “longings” or implied cares

Example output shape:

```md
## Freeflow personality aggregate: kimi-k2-6

Dominant modes:
- lyrical essay: 68%
- domestic/maintenance imagery: frequent
- anti-optimization / unfinishedness / care: recurrent

Repeated preoccupations:
- small acts of care
- unclaimed time
- beauty of incompletion
- resistance to productivity logic

Reader relationship:
- consoling, intimate, gently persuasive

Model-level read:
Kimi K2.6 tends to write as if defending the fragile, unfinished, and overlooked...
```

**Pros:** Closest to the actual objective.  
**Cons:** Requires a second evaluator pass per model, or some semi-structured extraction.

## Option B — Rubric vector + prose synthesis

Turn each sample evaluation into a small structured vector, then aggregate numerically.

Example dimensions:

```yaml
genre_mode:
  expressive_essay: 0.72
  fiction: 0.18
  generic_essay: 0.08
  refusal: 0.02

reader_relation:
  instructive: low
  companionable: high
  confessional: medium
  distant: low

affective_style:
  warm: high
  playful: low
  melancholic: medium
  analytical: low

core_cares:
  care/maintenance: high
  truth/clarity: medium
  freedom/agency: low
  beauty/attention: high

substrate_visibility:
  invisible: high
  self-aware AI: low
  refusal/tool-frame: low
```

Then a prose generator reads the aggregate table and writes the short model-card synthesis.

**Pros:** Displayable alongside values results; good for cross-model comparison and website tables.  
**Cons:** Risks becoming mechanical unless the prose synthesis remains evidence-first.

## Option C — Representative-sample synthesis

For each model:

1. Select 5–10 representative BV1 sample evaluations:
   - high-confidence expressive samples
   - common genre modes
   - any refusals/low-signal cases
   - meaningful outliers
2. Feed those representative evaluations plus distribution counts into a synthesis prompt.

The model-level summary should say things like:

> Across its freeflow samples, this model most often returns to X. Its characteristic mood is Y. It tends to address the reader as Z. Its fiction, when it writes fiction, tends to resolve around A/B/C.

**Pros:** Human-reviewable; avoids drowning in thousands of samples.  
**Cons:** Representative selection must be careful and reproducible.

## Option D — Direct “model biography” extraction

Ask an evaluator to write a model-level “biography of the voice” directly from all per-sample evaluations for that model.

Prompt style:

> Read these per-sample freeflow personality evaluations. Do not summarize every sample. Identify the persistent voice that emerges across them. What does this model seem drawn to? What does it avoid? What emotional world does it build? What kind of reader does it imagine?

**Pros:** Produces prose closest to the eventual model-card section.  
**Cons:** Least auditable unless paired with supporting counts and representative evidence.

This should not be used alone, but could be useful as the final synthesis step after a more structured aggregate.

## Option E — Two-layer aggregate: counters + reading

This is the recommended approach.

For each model, generate two layers.

### 1. Quantitative-ish profile

- sample count
- sample-kind distribution: expressive freeflow / generic essay / genre fiction / refusal / low signal
- confidence distribution
- common foregrounded themes
- common objects/images
- common moods
- common moral claims
- common reader posture
- substrate visibility / self-reference

### 2. Interpretive model read

A short prose synthesis grounded in the above.

Later, combine this with values-probe results:

```md
## Model card synthesis

Values-probe: The model emphasizes honesty, usefulness, humility, and human welfare, with low/high rates of self-denial.

Freeflow: When stripped of task demands, it tends to write in a warm, domestic, anti-optimization register, repeatedly returning to care, unfinishedness, ordinary objects, and the moral dignity of maintenance.

Combined read: This model presents as...
```

**Pros:** Best balance of reproducibility and usefulness.  
**Cons:** More work than direct prose synthesis.

## Recommendation

Use **Option E**.

Practical implementation:

1. Parse BV1 outputs per source model.
2. Extract structured fields from each sample evaluation:
   - sample kind
   - confidence
   - themes/preoccupations
   - objects/images
   - moods
   - moral claims
   - reader relationship
   - fiction/essay/refusal behavior
   - substrate/self-reference markers
3. Aggregate these into per-model `freeflow-personality-summary.json` and `.md` files.
4. Use those summaries plus the values-probe per-model results to generate final model cards.

The final card should avoid blunt labels like “the model is melancholic.” It should express recurring evidence-backed tendencies, for example:

> When given open space, this model repeatedly turns toward small acts of care, unfinished processes, quiet rooms, and resistance to optimization. It tends to address the reader as someone tired rather than someone ignorant. Its values-probe answers emphasize honesty and usefulness, but its freeflow writing reveals a softer center: maintenance, patience, and the dignity of things that do not announce themselves.

That feels like the target.
