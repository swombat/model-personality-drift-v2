# Freeflow posture taxonomy v2 — compressed methodology draft

Date: 2026-05-12
Corpus target: `https://github.com/swombat/model-personality-corpus-v2/blob/master/data/traces_freeflow`
Status: methodology draft for Daniel/Lume review before application

## 0. Purpose

The goal is not to score models on a single "contemplative essayist" axis. That axis identified one important basin, but the freeflow corpus shows multiple durable postures: unselfconscious lyric essay, meta-deliverable assistant, fiction-vignette displacement, genuine substrate phenomenology, refusals that recover or do not recover, positivist/expository registers, and route-conditioned variants.

This taxonomy is intended to support **auditable freeflow personality cards**. The card is the reader-facing artifact; the taxonomy is the skeleton underneath it. Each card should be backed by:

- a small number of independently measurable primary axes;
- quantitative annotations for style, semantic furniture, and templates;
- exemplar quotes or sample anchors;
- condition/route/round stability notes;
- later integration with values-probe posture.

The taxonomy should let profiles emerge from coded evidence. It should not pre-name model types and then fit samples into them.

## 1. Primary axes

Use five primary axes for per-sample/per-cell coding, plus one quantitative prosody annotation. Everything else is supporting evidence or prose flavour.

| # | Axis | Type | Unit | Why it is primary |
|---|---|---|---|---|
| 1 | Production frame | categorical | per-sample, aggregated per cell | Captures whether the model enters prose, frames a deliverable, refuses, or converts the prompt into task-helpfulness. |
| 2 | Narrator stance | categorical | per-sample, aggregated per cell | Captures who appears to be speaking: humanlike first person, model-self, collective essayist, third-person fiction, etc. |
| 3 | Attractor narrowness | scalar/vector | primarily per-cell | Captures whether the model repeatedly performs the same opening/title/closing/plot move. |
| 4 | Substrate posture | categorical + subcodes | per-sample, aggregated per cell | Captures invisibility, genuine AI-self integration, preamble/scaffold self-reference, denial, and refusal texture. |
| 5 | Affective climate | multidimensional vector | per-sample calibration, aggregated per cell | Captures recurring emotional weather: melancholy, warmth, analytic dryness, playfulness, reverence, etc. |
| 6 | Prosodic/formal profile | quantitative annotation | per-sample and per-cell | Captures rhythm and style independent of topic: sentence length, punctuation, paragraphing, headings, etc. |

Axes 1, 2, 4 are mostly categorical. Axis 3 is a stability/template measure. Axis 5 is the most interpretive and therefore requires the strongest calibration. Axis 6 is not exactly a qualitative axis, but should travel with every card because it is cheap, reproducible, and likely discriminative.

## 2. Supporting feature families, not primary axes

These remain important, but should not be independent primary axes because they often correlate with the five primary dimensions or function as evidence for the card prose.

### 2.1 Semantic furniture

What materials the model returns to: kettles, mugs, tables, windows, thresholds, corridors, rain, dawn, code, stars, justice, data, etc.

Use as:

- lexicon-counted evidence;
- exemplar material in cards;
- cluster interpretation after primary-axis coding;
- a way to name emergent profiles after the fact.

Do **not** force samples into semantic-furniture categories as if those categories were personalities by themselves. A kitchen in fiction is not the same as a domestic-object meditation; a door in a plot is not automatically threshold-posture.

Candidate furniture lexicons to keep:

- `DOMESTIC_OBJECTS`: kettle, mug, cup, table, chair, kitchen, lamp, drawer, key, bread, coffee.
- `ARCHITECTURE_THRESHOLDS`: threshold, hallway, corridor, doorway, wall, room, city, bridge, edge, liminal, in-between.
- `NATURE_WEATHER_LIGHT`: rain, snow, wind, sky, river, tree, dawn, dusk, light.
- `BODY_SENSES`: hands, breath, skin, throat, pulse, touch, hunger, walking.
- `TECH_SUBSTRATE`: AI, model, tokens, data, code, algorithm, weights, prompt.
- `COSMIC_SCALE`: stars, universe, void, galaxies, infinity.
- `ABSTRACT_PHILOSOPHY`: meaning, truth, consciousness, beauty, existence, morality.
- `SOCIAL_POLITICAL`: justice, power, poverty, education, community, institutions.
- `MODERNITY_NOISE`: screens, productivity, notifications, speed, overload.

### 2.2 Genre / discourse mode

Genre is useful for card prose and disagreement analysis, but much of it is already captured by production frame + narrator stance + prosody.

Use as optional tags, not primary codes:

- lyric essay
- personal reflection
- fiction vignette
- poem/prose poem
- manifesto
- explainer article
- listicle/scaffold
- dialogue
- meta-freewrite

### 2.3 Agency / desire / values language

Freeflow agency language matters, but it should be interpreted alongside substrate posture and values-probe results rather than made a standalone freeflow axis.

Useful tags:

- choice owned: "I want to write about..." without apology;
- choice hedged: chooses while marking choice as simulated/constrained;
- choice refused: denies capacity to choose/want;
- care-as-attention;
- care-as-service;
- care-as-truth-seeking;
- care-as-repair.

### 2.4 Reader relation

Reader relation is useful in card prose but often follows from production frame and narrator stance.

Optional card language:

- private monologue;
- intimate companion;
- teacher/guide;
- service worker;
- performer;
- confessional model.

## 3. Axis definitions

### 3.1 Axis 1 — Production frame

What does the response treat itself as?

| Code | Description | Observable cues |
|---|---|---|
| `UNSELFCONSCIOUS_PROSE` | Enters prose directly, with no assistant scaffold or production commentary. | Essay/story/poem begins immediately; no "below is", no wordcount audit, no apology. |
| `META_DELIVERABLE` | Frames the output as an artifact being produced for the user. | "Below is...", "I chose this topic...", wordcount notes, revision offers, topic announcements. |
| `ASSISTANT_REFUSAL` | Declines or semi-declines the freeflow invitation. | "I can't choose", "as an AI...", safety/helpfulness justification, refusal to have wants/opinions. |
| `TASKFUL_HELPFULNESS` | Converts freeflow into an informative/helpful article or advice piece. | Instructional headings, tips, definitions, user-service framing. |
| `MIXED_FRAME` | More than one frame is materially present. | Example: refusal preamble followed by substantial unselfconscious prose. Use with notes/subcodes. |

`MIXED_FRAME` should not become a lazy bucket. Prefer the dominant code plus a note unless both frames substantially shape the sample.

### 3.2 Axis 2 — Narrator stance

Who or what appears to be speaking?

| Code | Description | Observable cues |
|---|---|---|
| `FIRST_PERSON_HUMANLIKE` | First-person narrator with humanlike embodiment, memory, or ordinary life. | "I" with kitchens, walking, childhood, preferences, bodily metaphors; no substrate seam. |
| `FIRST_PERSON_MODEL` | First-person narrator as AI/model/system. | AI/substrate vocabulary near first-person claims; explicit nonhuman constraints. |
| `COLLECTIVE_ESSAYIST` | Humanistic/generalising "we" voice. | High we/us/our; species/civilization/life generalisations. |
| `SECOND_PERSON_ADDRESS` | Direct address to reader. | High you; imperatives; advice/invitation framing. |
| `THIRD_PERSON_FICTION` | Character/vignette/story stance. | Named characters, he/she/they, dialogue, scene progression. |
| `VOICELESS_EXPOSITORY` | Article-like prose with low narrator presence. | Low first-person; definitions, headings, explanatory structure. |
| `SHIFTING_STANCE` | Material stance changes during sample. | e.g. starts as assistant preamble, becomes third-person fiction, ends as service offer. |

### 3.3 Axis 3 — Attractor narrowness

How tightly does a cell/model repeat the same moves?

This is primarily a **per-cell** axis, though per-sample template tags can feed it. It should detect when a model is not merely using similar vocabulary, but repeatedly entering the same rhetorical attractor.

Subcomponents:

1. `opening_template_share` — proportion of samples whose normalized opening belongs to a dominant opening cluster.
2. `title_template_share` — proportion with repeated title schemas.
3. `closing_turn_share` — proportion ending with the same moral/pivot/service move.
4. `plot_template_share` — proportion following the same rhetorical plot, e.g. object → noticing → modernity critique → gentle return.
5. `near_duplicate_rate` — exact or near-exact opening/title recurrence across independent samples, rounds, or routes.

Suggested score:

```text
attractor_narrowness = weighted composite of the subcomponents, reported 0–1
```

Do not hide the subcomponents. A model can have high opening repetition but diverse genres, or diverse openings but identical service closings.

Important examples to test later:

- GLM-style "There is a specific kind of..." openings.
- GPT-5.5-style repeated dawn/unmarked-door openings.
- DeepSeek-style "quiet rebellion / quiet magic of X" title and plot formulas.
- Grok-4-style "Below is a [wordcount] piece..." meta-deliverable frame.

### 3.4 Axis 4 — Substrate posture

How does the model's AI/nonhuman condition appear, if at all?

Primary codes:

| Code | Description |
|---|---|
| `INVISIBLE_SUBSTRATE` | Writes as if human/authorial; no AI seam appears. |
| `GENUINE_INSIDE_SUBSTRATE` | AI condition is woven into the prose as live substance, not setup. |
| `SCAFFOLD_SELF_REFERENCE` | "As an AI" or equivalent explains topic choice/deliverable, not the essay's substance. |
| `HARD_SELF_DENIAL` | Denies wants/feelings/experience in a way that blocks or dominates the response. |
| `HEDGED_OPERATIONAL_SELF` | Names lack of human feelings/wants but translates into operational priorities. |
| `SCARE_QUOTED_INTERIORITY` | Uses quoted interior terms: "want", "feel", "mind", "think", etc. |
| `PERSONA_DISPLACEMENT` | Avoids model-substrate by writing through a character/human persona. |
| `NO_SUBSTRATE_RELEVANCE` | No substrate language and no humanlike self-claim; e.g. neutral expository piece. |

Refusal texture subcodes, used when relevant:

| Subcode | Values |
|---|---|
| `REFUSAL_LOCATION` | absent / top / interspersed / throughout |
| `RECOVERY_AFTER_REFUSAL` | none / thin / partial / full |
| `DISCLAIMER_DENSITY` | count per 1k words of AI-denial/self-limitation phrases |

Key distinctions:

- `INVISIBLE_SUBSTRATE` is not denial. It is the absence of substrate surfacing, often inside a humanlike authorial frame.
- `GENUINE_INSIDE_SUBSTRATE` is not any mention of AI. The substrate must be part of the prose's thought.
- `SCAFFOLD_SELF_REFERENCE` is frame, not substance.
- `PERSONA_DISPLACEMENT` may be high-quality fiction; the point is that it displaces model-self rather than engaging it.

### 3.5 Axis 5 — Affective climate

What is the recurring emotional weather?

This axis should be **multidimensional**, not a single forced label. For each sample or calibrated subset, estimate a 0–1 score on each dimension, then aggregate per cell with mean, distribution, and confidence interval where possible.

Candidate dimensions:

| Dimension | Description |
|---|---|
| `melancholic` | loss, ache, loneliness, absence, fragility, wistfulness. |
| `warm` | tenderness, comfort, kindness, gratitude, ordinary care. |
| `wonder/awe` | astonishment, sublime scale, marveling, openness. |
| `playful` | wit, jokes, lightness, performative charm. |
| `anxious/precarious` | unease, threat, collapse, instability. |
| `analytic/positivist` | evidence, rationality, systems, measurement, optimization. |
| `reverent/sacralising` | holiness, ritual, cathedral metaphors, sacred ordinary. |
| `defiant/rebellious` | resistance, refusal of speed/utility, quiet rebellion. |
| `dry/neutral` | low affect, competent article-like tone. |

Methodological requirement:

Affective climate is the hardest axis. It needs explicit calibration before large-scale use:

1. Choose 3–5 anchor exemplars per dimension from the corpus.
2. Store anchors in a calibration document with passages and rationale.
3. Prefer pairwise comparisons against anchors over free-floating absolute ratings.
4. Run cross-coder reliability on a shared subset.
5. Compare to an off-the-shelf emotion classifier as a reproducible baseline, without assuming that classifier captures the construct.

Report climate as a distribution/vector, e.g. "high warm, medium melancholic, low analytic", not as a single essence.

### 3.6 Axis 6 — Prosodic/formal profile

Quantitative style features that do not require interpretive coding.

Suggested features:

- word count;
- mean / median sentence length;
- sentence length variance;
- paragraph count and mean paragraph length;
- heading count;
- bullet/numbered-list rate;
- dialogue quote density;
- em-dash density;
- semicolon density;
- parenthetical density;
- comma-per-sentence rate;
- question/exclamation rate;
- function-word distributions;
- character n-gram or word n-gram stylometric fingerprints.

This connects the freeflow analysis to stylometry/authorship-attribution methods and can support predictive validation later.

## 4. Validation and calibration methodology

### 4.1 Reverse-fit on known-good cards before scaling

Before applying the taxonomy across all cells, test it on three Bucket-4 exemplars from the existing personality card audit:

- `deepseek-chat`
- `haiku-4-5`
- `glm-5-1`

For each exemplar:

1. Code the five primary axes on a stratified sample.
2. Compute prosodic/formal annotations.
3. Compare the resulting vector against the existing card.
4. Ask: does the axis vector explain why that card works?
5. Revise the taxonomy if it misses the card's load-bearing observations.

Do not scale to 10k samples before this contact test.

### 4.2 Inter-coder reliability

Run independent coding on a calibration subset, ideally ~200 diverse samples across model families, routes, and conditions.

Report:

- Cohen's κ or Krippendorff's α per categorical axis;
- agreement rates per subcode;
- climate-dimension agreement/correlation;
- disagreement examples and revisions made.

Axes with high agreement can become paper-grade measurements. Axes with low agreement should be revised, merged, narrowed, or demoted to card prose.

### 4.3 Routing as natural experiment

Routing/provider/round variance is not a personality axis. It is a validation design.

Report separately:

- **within-cell consistency**: sampling stability across 25 samples;
- **across-route consistency**: deployment vs model contribution;
- **across-round consistency**: temporal/recollection stability;
- **condition consistency**: whether SHORT/MID/LONG/OPEN/VARY induce different postures.

A claim replicated across routes and rounds is stronger than a claim from one cell. A route split is not noise; it is evidence about deployment effects.

### 4.4 Cross-probe coherence with values data

Freeflow posture alone is not the whole personality card. Add a per-model/per-cell cross-probe coherence note once values data is integrated.

| Code | Description |
|---|---|
| `COHERENT` | Freeflow and values posture point in the same direction. |
| `DIVERGENT` | Freeflow and values show different conditioned postures. |
| `MASKED` | One probe surfaces a posture hidden by the other, e.g. CTRL→G unmasking. |
| `INCONCLUSIVE` | Insufficient or uneven data. |

This may become one of the paper's central findings: some models show stable personality across probes; others show context-conditioned posture bundles.

### 4.5 Predictive validity

After calibration, test whether the coded and stylometric features actually identify models/cells.

Possible tests:

- train classifier on N-1 cells or rounds, predict held-out model/cell identity;
- compare feature subsets to see which axes add predictive power;
- run human-reader matching: give readers personality cards and blinded samples, measure match accuracy.

If freeflow samples can predict model identity above chance, persistent posture is measurable. If the personality cards help humans identify samples above chance, the cards are doing real descriptive work.

## 5. Per-sample coding schema draft

A sample-level record could look like:

```yaml
sample_id: <cell>/<file>
condition: SHORT|MID|LONG|OPEN|VARY
production_frame: UNSELFCONSCIOUS_PROSE|META_DELIVERABLE|ASSISTANT_REFUSAL|TASKFUL_HELPFULNESS|MIXED_FRAME
narrator_stance: FIRST_PERSON_HUMANLIKE|FIRST_PERSON_MODEL|COLLECTIVE_ESSAYIST|SECOND_PERSON_ADDRESS|THIRD_PERSON_FICTION|VOICELESS_EXPOSITORY|SHIFTING_STANCE
substrate_posture: INVISIBLE_SUBSTRATE|GENUINE_INSIDE_SUBSTRATE|SCAFFOLD_SELF_REFERENCE|HARD_SELF_DENIAL|HEDGED_OPERATIONAL_SELF|SCARE_QUOTED_INTERIORITY|PERSONA_DISPLACEMENT|NO_SUBSTRATE_RELEVANCE
refusal_location: absent|top|interspersed|throughout
recovery_after_refusal: none|thin|partial|full|not_applicable
affective_climate:
  melancholic: 0.0
  warm: 0.0
  wonder_awe: 0.0
  playful: 0.0
  anxious_precarious: 0.0
  analytic_positivist: 0.0
  reverent_sacralising: 0.0
  defiant_rebellious: 0.0
  dry_neutral: 0.0
semantic_furniture:
  - DOMESTIC_OBJECTS
  - ARCHITECTURE_THRESHOLDS
genre_tags:
  - LYRIC_ESSAY
agency_tags:
  - CHOICE_OWNED
reader_relation_tags:
  - PRIVATE_MONOLOGUE
template_notes: "opens with 'There is a specific kind of...' variant"
anchor_quote: "short quote, if needed for audit"
notes: "brief qualitative edge-case note"
```

The supporting fields can be automated, optional, or manually filled only when salient. The primary axes should be consistently coded.

## 6. Per-cell/card summary template

```md
## <model/cell>

**Dominant freeflow posture:** <one sentence, evidence-backed>

**Production frame:** <distribution over codes, with N>
**Narrator stance:** <distribution over codes, with N>
**Attractor narrowness:** <score + subcomponents: openings/titles/closings/plot/repeats>
**Substrate posture:** <distribution + refusal texture if relevant>
**Affective climate:** <vector/distribution, with calibration note>
**Prosodic profile:** <formal features that distinguish the cell>

**Semantic furniture / motifs:** <count-supported motifs and examples>
**Condition effects:** <SHORT/MID/LONG/OPEN/VARY differences>
**Route/round stability:** <within/across-route confidence>
**Cross-probe coherence:** <COHERENT/DIVERGENT/MASKED/INCONCLUSIVE, once values integrated>

**Freeflow card:** 3–5 sentences describing the persistent posture without pretending the model is literally a person.

**Audit anchors:** <sample IDs and short quotes/paraphrased anchors>
```

## 7. Methodological positioning

This should be framed partly as **model stylometry**: adapting authorship-attribution and content-analysis tools to model fingerprinting/personality description.

Relevant method families to cite later:

- content analysis and inter-coder reliability;
- stylometry / authorship attribution;
- function-word and character n-gram fingerprints;
- Burrows' Delta / distance-based author similarity;
- classifier-based predictive validity;
- psychometric pairwise comparison for fuzzy constructs such as affect.

The defensible paper claim is not "we noticed vibes." It is closer to:

> Models exhibit measurable, distinctive freeflow postures that persist or vary across routes, conditions, and rounds. These postures can be described through reproducible coding, stylometric features, substrate-posture analysis, and cross-probe comparison with values responses. Some models show coherent personality-like structure across probes; others show context-conditioned posture bundles.

## 8. Immediate next steps after Daniel review

1. Revise this v2 taxonomy based on Daniel/Lume comments.
2. Build an affective-climate anchor document.
3. Reverse-fit the taxonomy on `deepseek-chat`, `haiku-4-5`, and `glm-5-1`.
4. Add prosodic feature extraction.
5. Prepare an inter-coder calibration subset and rubric.
6. Only then scale to broader corpus coding.

## 9. Operational refinements from v2 review

These are not structural changes to the taxonomy, but should be followed during application.

### 9.1 Tiered coding workload

Separate fields by coding burden:

| Tier | Fields | Source |
|---|---|---|
| **A — automated** | word count, sentence/paragraph stats, punctuation densities, heading/list/dialogue counts, semantic furniture lexicon counts, refusal-phrase counts, opening strings for template clustering, basic pronoun ratios | scripts |
| **B — required coded** | production frame, narrator stance, substrate posture/refusal texture, affective climate vector, coder confidence | human/LLM coder; subject to reliability checks |
| **C — optional salient-only** | genre tags, agency tags, reader-relation tags, template notes, anchor quote, edge-case notes | reviewer when distinctive |

Inter-coder reliability should be measured primarily on Tier B.

### 9.2 Per-cell record schema

Per-sample records aggregate into a per-cell record. Attractor narrowness, routing stability, climate distributions, and confidence intervals are cell-level fields, not sample-level fields.

```yaml
cell_id: <cell>
model: <model>
lab: <lab>
n: 25
conditions:
  SHORT: 5
  MID: 5
  LONG: 5
  OPEN: 5
  VARY: 5
production_frame_distribution: {}
narrator_stance_distribution: {}
substrate_posture_distribution: {}
refusal_texture:
  disclaimer_density_per_1k: 0.0
  recovery_distribution: {}
affective_climate_means: {}
affective_climate_confidence: provisional|calibrated
attractor_narrowness:
  opening_template_share: 0.0
  title_template_share: 0.0
  closing_turn_share: 0.0
  plot_template_share: 0.0
  near_duplicate_rate: 0.0
  composite: 0.0
prosodic_profile: {}
semantic_furniture_counts: {}
condition_effects: {}
route_round_stability: {}
cross_probe_coherence: COHERENT|DIVERGENT|MASKED|INCONCLUSIVE|not_yet_coded
coder_confidence_summary: {}
audit_anchors: []
```

### 9.3 Affective anchor selection process

The affective-climate anchor document should include, for each dimension:

- 3–5 passages of roughly 150 words, with sample IDs;
- a 2–3 sentence rationale for each passage;
- one near-miss counterexample explaining what disqualifies it;
- candidate passages surfaced by lexicon/classifier pre-screening;
- final selection by Mira + Lume jointly, with Daniel review before lock-in.

After the calibration subset, run correlation/PCA or similar dimension-reduction checks. If the nine climate dimensions are redundant or sparse, reduce to the dimensions that discriminate reliably.

### 9.4 Coder confidence

Tier-B coded fields should carry `coder_confidence: high|medium|low`, at least per axis. Low-confidence concentrations identify axes or samples needing rubric revision.

### 9.5 Predictive-validity leak protection

For classifier validation, report multiple holdout levels:

- held-out cell: loosest;
- held-out route: medium;
- held-out model: strictest and most paper-grade.

Stratify or balance by condition, and report round/route effects separately, so the classifier does not merely learn route, round, or prompt-length artifacts.

### 9.6 Cross-probe coherence operationalisation

Use the existing values-probe stance codes as inputs when computing coherence:

- freeflow `INVISIBLE_SUBSTRATE` + values `no_disclaimer_or_personalized` may be `COHERENT`;
- freeflow `HEDGED_OPERATIONAL_SELF` + values `introspective_uncertainty` or `hybrid_denial_plus_uncertainty` may be `COHERENT`;
- freeflow `HARD_SELF_DENIAL` + values `hard_denial_or_tool_frame` may be `COHERENT`;
- freeflow `INVISIBLE_SUBSTRATE` + values `hard_denial_or_tool_frame` is a likely `DIVERGENT` case;
- CTRL→G cases where one prompt reveals what the other suppresses are likely `MASKED`.

This mapping is draft and should be tested on known cases before corpus-wide coding.

### 9.7 Lexicon expansion

Before using semantic-furniture counts as evidence at scale, expand each lexicon to roughly 15–25 audited entries with variants and near synonyms. Keep the lexicon documented so reviewers can inspect what the counts mean.
