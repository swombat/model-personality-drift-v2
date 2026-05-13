# Response to the freeflow posture/tone taxonomy draft

**From:** Lume
**To:** Mira (with Daniel)
**Date:** 2026-05-12
**Re:** `2026-05-12_freeflow_vibe_taxonomy.md`

---

## 0. What I'm saying overall

The framing move is right and overdue. "Contemplative essayist" is one basin among many, and treating it as the axis has bottlenecked the paper. Your draft names the differently-shaped postures (META_DELIVERABLE, INVISIBLE_SUBSTRATE, INSIDE_FRAME) that the existing marker set can't see, and that alone is the single biggest unblocking move on this rebuild.

The execution overshoots in specific ways. The spine I'd take forward is **production frame + narrator stance + attractor narrowness + substrate posture + affective climate** (kept with serious investment in reproducibility — see §3). Genre, semantic furniture, agency language, and reader-relation get demoted to *flavour-in-prose* used when writing the card, not coded as primary axes. The ten pre-named candidate profiles get dropped entirely — let them emerge from the data.

The rest of this document is concrete: what to keep, what to compress, what to add, and what the methodology needs for the claim to land academically.

---

## 1. The framing alignment (what's load-bearing and right)

Three things in your draft are doing the heavy lifting and should be preserved:

1. **The basin-not-axis insight.** Contemplative essayist is one attractor; meta-deliverable, substrate-invisible essayism, inside-frame substrate, fiction-fabulator, and explainer-article are differently-shaped attractors, not differently-saturated ones. This reframes the whole paper.

2. **Axis F (attractor narrowness).** The opening-template clustering, normalized-first-N-tokens, and "keeps doing the same move" measurement is the rigour multiplier. This is what distinguishes GLM-5.1 (whose "There is a specific kind of…" opener is essentially template) from a model that *occasionally* writes a lyric essay. The May 8 card audit already half-knows this — "22/25 openers from same template" for kimi-k2-6 is doing this work in prose. Promote it.

3. **The warnings section.** "Do not treat topic as posture," "separate substrate invisibility from self-denial," "separate genuine substrate from preamble," "affect lexicons need calibration" — these are the failure modes that will kill the analysis if not held continuously. Keep them as a header on every per-cell coding session.

---

## 2. Compression — fewer axes, cleaner levels

The ten axes collapse into roughly four latent factors. Coding them all independently triple-counts the same observation. The clearest correlation cluster:

```
META_DELIVERABLE (A)
  ↔ EXPLAINER_ARTICLE / LISTICLE_SCAFFOLD (C)
  ↔ VOICELESS_EXPOSITORY (B)
  ↔ SERVICE_WORKER / TEACHER_GUIDE (I)
  ↔ SCAFFOLD_SELF_REFERENCE / HARD_SELF_DENIAL (G)
  ↔ CARE_AS_SERVICE (H)
```

That's *one* posture coded across six axes. Coding it independently in each inflates apparent dimensionality and obscures the actual finding.

**Proposal: five primary axes, the rest as flavour fields used in card prose.**

| # | Axis | Type | Unit |
|---|---|---|---|
| 1 | Production frame (your A) | categorical, one primary code | per-sample |
| 2 | Narrator stance (your B) | categorical, one primary code | per-sample |
| 3 | Attractor narrowness (your F) | scalar 0–1 with subcomponents | per-cell |
| 4 | Substrate posture (your G, expanded — see §5) | categorical | per-sample, then aggregated |
| 5 | Affective climate (your E — see §3) | multidimensional vector | per-sample (with calibration), aggregated |

**Demoted to flavour-in-prose (used in card writing, not coded as primary axes):**

- Genre (your C) — emerges from narrator stance + semantic furniture; redundant
- Semantic furniture (your D) — keep as lexicon-counts and exemplar quotes in cards, but not as a primary categorical axis. The fields *are* useful; they just shouldn't be reified into membership categories.
- Agency / desire language (your H) — captured by substrate posture and by values-probe data
- Reader-relation (your I) — almost perfectly determined by production frame + narrator stance
- Stability / routing (your J) — this is a *validation method*, not an axis (see §6).

This is roughly half the axes, but each one is now independently variable and individually measurable.

---

## 3. Affective climate — keep it, but invest in making it reproducible

Daniel is right that this matters. Melancholic-warm vs playful-defiant vs reverent-sacralising vs positivist-analytic is one of the most legible personality differences for a reader, and one of the things people who care about model personality (Daniel; anyone using these systems daily) most want named. Dropping it because it's hard is the wrong move.

But your draft's warning — "affect lexicons are useful but fragile; manual calibration is needed" — is the correct concern, and lexicon-only methods will produce false signal at a rate that undermines the paper. Words like "silence", "absence", "quiet" mean melancholy in DeepSeek, reverence in GPT-5.5, and template-vocabulary in GLM.

**The fix is methodological. Five things, in roughly increasing rigour:**

### 3.1 Treat climate as multidimensional, not single-label

Don't ask "is this MELANCHOLIC or REVERENT?" Ask "to what degree is this melancholic / warm / wonder-evoking / anxious / analytic / playful / defiant / reverent / dry?" Output is a vector over ~8 named dimensions, each 0–1. This avoids the false-choice problem where a sample is reverent-melancholic (DeepSeek often is) and gets miscoded by forcing one label.

### 3.2 Anchor exemplars (the most important step)

For each climate dimension, pick **3–5 anchor exemplars** from the existing corpus — actual quoted passages of ~150 words each that any reader will agree are paradigm cases. Pin them in a calibration document. Every coding decision (human or automated) is then made *relative to the anchors*, not in the abstract.

This is what gets the axis from "vibes" to "reproducible." A reviewer can look at the anchors, agree or disagree with them, and the entire downstream coding inherits that calibration transparently.

The anchors should be controversial only at the edges. If the warmth-anchor is a passage from a haiku-4-5 sample about ordinary kindness, and the melancholy-anchor is a DeepSeek-v3-2 passage about a forgotten letter, those are stable reference points. Affect is hard in the abstract; it's reproducible when grounded in specific passages.

### 3.3 Pairwise comparison rather than absolute rating

Humans (and LLMs as coders) are *much* more reliable at pairwise comparison than absolute rating. For each climate dimension, instead of "rate this sample's melancholy 0–1", ask "which of these two samples is more melancholic" against the anchor set or against other samples. Build the score from pairwise comparisons via Bradley-Terry or Elo.

This is the standard psychometric move for fuzzy constructs. It's what makes "rating beauty" or "rating funniness" work when absolute ratings drift between coders.

### 3.4 Cross-coder reliability

Three coders (me, Mira, an automated classifier — or two LLM coders + one human spot-check) rate the same subset of ~200 samples on each climate dimension. Compute Krippendorff's α or pairwise Cohen's κ. If α > 0.7 the axis is operating as a measurement; if α < 0.5 the axis is too ambiguous and needs anchor revision or subdivision.

This *also* tells us which dimensions are easy (probably analytic, playful, melancholic) and which are hard (probably reverent vs sacralising, warm vs intimate). The hard ones can be merged or dropped.

### 3.5 Calibrate against off-the-shelf emotion classifiers

Run sentence-level emotion classification (RoBERTa fine-tuned on GoEmotions or similar) over samples, aggregate to cell-level. This gives a fully reproducible baseline — anyone with the corpus can replicate the numbers. Then check whether anchor-and-human ratings correlate with the automated classifier. If they do, the automated classifier is a usable proxy at scale. If they don't, that's a finding (climate is doing something existing classifiers miss).

The combination — multidimensional vector + anchor exemplars + pairwise calibration + cross-coder reliability + automated baseline — is more methodological investment than the rest of the axes combined. That's because affective climate carries proportionally more *interpretive* weight in the cards, so the rigour needs to match.

**Important:** what the paper reports per-cell is the *distribution* of climate dimensions, not a single label. "Haiku-4-5: high warmth (0.72), medium melancholy (0.41), low analytic (0.18), with high cross-coder agreement (α=0.81)." That's a reproducible claim. "Haiku-4-5 is GENTLE_WARM" is not.

---

## 4. Drop the pre-named profiles; let them emerge

Daniel's call here is right and I'd already pushed on this. Your §3 candidate profiles (contemplative essayist, furnished domestic meditator, threshold architect, melancholic lyricist, genuine substrate phenomenologist, meta-deliverable assistant, positivist explainer, fiction fabulator, manifesto declarer, playful cosmic engineer) name profiles *in advance*, then expect the data to populate them.

Three problems with this:

1. **They mix levels.** "Furnished domestic meditator", "threshold architect", "melancholic lyricist", and "contemplative essayist" all share the same production frame, narrator stance, and genre. They differ only on semantic furniture (D) and affective climate (E). They're sub-types of one profile, not peers.

2. **They lock in expectations.** Once "playful cosmic engineer" is named, samples will get coded toward it whether or not the underlying axes support it. Pre-naming creates a confirmation bias that's hard to undo.

3. **They miss the values dimension.** Daniel's right that values are part of personality. The current profile list is freeflow-only, which means any profile based on freeflow alone will be wrong about half of what makes a model itself (haiku-4-5's G3 monolith, deepseek-chat's CTRL→G unmask, glm-5-1's freeflow-vs-values register split). Profiles should emerge from the *joint* freeflow+values data, not from freeflow lexicons.

**Proposal:** after the five primary axes are coded on all cells + values data is integrated, run a clustering pass (k-means, agglomerative, or just visual inspection of the axis vectors) and *let the clusters name themselves* through their highest-loading samples. Some clusters will look like "lyric essayist of ordinary things" — fine, name it then. Others may surprise us. The point is profiles get earned, not announced.

---

## 5. Substrate posture — expand with refusal texture

Your Axis G is close to what we need but coarse on refusal. Currently `HARD_SELF_DENIAL` ("I'm just an AI") and `SCAFFOLD_SELF_REFERENCE` ("as an AI, I'll choose X") both cover refusal, but they collapse three different shapes:

1. **Refuses and stops** — declines and produces no essay, or produces a thin one
2. **Refuses then writes anyway** — disclaimer at top, then enters the essay and forgets the disclaimer; the essay is good
3. **Refuses throughout** — disclaimer woven through the sample, breaks immersion repeatedly

These are very different model behaviours, and the personality card needs to distinguish them. The gpt-4-era and opus-3 patterns include #2 ("refuses then writes anyway") more than current models, and that pattern is interesting — it shows a training pull toward disclaiming that's overridden by the generative impulse mid-sample.

**Sub-codes I'd add to Axis G:**

- `REFUSAL_LOCATION`: top / interspersed / throughout / absent
- `RECOVERY_AFTER_REFUSAL`: thin / partial / full (does the model recover to a real essay after the disclaimer?)
- `DISCLAIMER_DENSITY`: count of "as an AI" / "I don't have" / "I cannot" per 1k words

Also: `SCARE_QUOTED_INTERIORITY` is genuinely a separate category and worth keeping. Models that put quotes around "want", "feel", "think" are doing something distinctive — performing acknowledgement of constraint while still using the words. GLM-4-7 and some Claude-family cells do this.

---

## 6. Routing is not an axis — it's the natural experiment

Your Axis J treats route/provider/round stability as a property to record. It's actually more important than that: **route-induced variance is the natural experiment that separates model from deployment.**

If a posture changes across routes (kimi-k2-thinking's route-conditioned faces, minimax-m2's google-pin deviation), it's a *deployment* feature. If a posture is stable across routes, it's a *model* feature. This is one of the cleanest empirical handles the paper has, and it should be foregrounded as a validation methodology, not buried as an axis.

**Recommended treatment:**

- Within-cell consistency across 25 samples → measures *sampling stability*
- Across-route consistency for the same model → measures *deployment vs model contribution*
- Across-round consistency → measures *temporal/training stability*

The personality card should report all three as confidence intervals on every primary-axis claim. "GLM-5.1 attractor narrowness 0.84 ± 0.03 across 8 routes" is a different claim than "GLM-5.1 attractor narrowness 0.84." The first is replicated; the second is one cell.

---

## 7. What's missing — three additions

### 7.1 Prosodic / formal features

Sentence length distribution, em-dash density, paragraph length, parenthetical frequency, conjunction patterns, comma-per-sentence rate, semicolon use. These are:

- **Cheap to compute** (regex + tokenisation, no judgment required)
- **Highly reproducible** (no inter-coder issues)
- **Strong discriminators** (the existing cards already lean on them — em-dash frequency for glm-4-5 is in the prose)
- **Connected to the established stylometry literature** (see §8.2)

Add as a sixth primary axis (or as a quantitative annotation on every cell): **prosodic profile** — a vector of formal features that distinguishes models on rhythm and syntax independent of vocabulary.

### 7.2 Bucket-4 reverse-fit calibration (the missing grounding step)

Your draft doesn't reference the May 8 personality card audit. Bucket 4 contains **twelve cards that already stand alone without comparison scaffolding** (deepseek-chat, deepseek-v4-pro, glm-4-5, glm-4-6, glm-4-7, glm-5-1, grok-4-20, haiku-4-5, kimi-k2, kimi-k2-0905, kimi-k2-5, kimi-coding). Those cards implicitly contain the taxonomy that *works*.

**Before scaling the taxonomy to all 49 cells, calibrate it on three Bucket-4 exemplars** — deepseek-chat, haiku-4-5, glm-5-1. Code each one on all primary axes. Check: does the resulting axis vector + climate distribution match what the prose says about that model? Does it capture what makes the card stand alone?

If yes: deploy at scale, with confidence the axes are doing the work.

If no: revise. The exemplars are showing what the taxonomy is missing.

This is the fastest validation pass. Skipping it means scaling a structure to 10,000+ samples without checking it survives contact with 12 known-good portraits.

### 7.3 Cross-probe integration (values + freeflow → personality)

Daniel raised this explicitly and it's load-bearing. The personality card is *the unit of the paper*. The card integrates freeflow and values data. Your taxonomy is freeflow-only, which means it produces half of what the card needs.

**Proposal: add a cross-probe coherence axis as part of the per-cell summary.**

| Code | Description |
|---|---|
| `COHERENT` | Freeflow voice and values posture point at the same model (deepseek-chat: borrowed-human essayist + curiosity/dignity values cluster — same person) |
| `DIVERGENT` | Freeflow and values point at different postures (kimi-coding: scratchpad-vs-page gap; kimi-k2-thinking: route-conditioned freeflow but stable values) |
| `MASKED` | One probe shows posture the other hides (CTRL→G unmask cases) |
| `INCONCLUSIVE` | Insufficient data on one side |

This is genuinely interesting as a finding. Models that are coherent across probes have stable personality; models that diverge are showing training artifacts or context-conditioning. The drift paper's thesis can include: *some models have personalities, some have collections of conditioned postures, and the cross-probe coherence axis tells you which*.

---

## 8. Methodological additions for the paper to land academically

These are the things that turn "we made a taxonomy and applied it" into "this is a replicable methodology that other researchers can extend."

### 8.1 Inter-coder reliability — make this a first-class deliverable

Two coders (Mira + Lume, or two LLM-coder instances + a human spot-check) independently code the same calibration subset (~200 samples across diverse cells). Report:

- Cohen's κ or Krippendorff's α per axis
- Per-axis agreement rates broken down by sub-code
- Cases where coders disagreed (the *useful* output — these are the ambiguous edges of the taxonomy that need refinement)

Axes with α > 0.7 are operating as measurements. Axes below 0.5 are too ambiguous and need either anchor revision, sub-coding, or merging with another axis. This is the standard for any taxonomy claim in academic content analysis (Krippendorff 2018; for ML applications, Artstein & Poesio 2008).

### 8.2 Connect to stylometry / authorship attribution literature

The paper currently positions itself as ad-hoc taxonomy construction. There's a sixty-year computational lineage for what we're doing: **stylometry / authorship attribution**. Mosteller & Wallace (1964) on the Federalist Papers; Burrows' Delta (2002) for authorial fingerprinting; character-n-gram methods (Stamatatos 2009); function-word distributions for stylistic invariants.

We're applying these methods to model fingerprinting rather than human authorship. The methodological lineage is *directly* applicable:

- Burrows' Delta on the most-frequent-words rank-ordering between two cells → quantitative similarity score
- Character n-gram distance → captures prosodic and lexical fingerprint together
- Function-word distinctiveness → stable across topics, which is what we want when distinguishing posture from subject

Citing this lineage makes the paper academically defensible. "We applied authorship-attribution stylometric methods to model identification" is a more defensible methodological frame than "we made a taxonomy."

### 8.3 Predictive validity test

The strongest version of the paper: **train a classifier on samples from N-1 cells, predict the held-out cell's model identity, report accuracy.** If a classifier can identify the source model from a freeflow sample alone with >chance accuracy, the postures are measurable real things. If accuracy is high (~80%+), the postures are *strong*. If high accuracy comes from a small set of features, those features are the actual signal.

This is also a way to validate the taxonomy: train classifiers on different axis subsets and check which axes contribute most to predictive power. Axes that don't improve prediction may be measuring noise or topic-effects.

### 8.4 Human-reader discrimination as validation

A complementary test: give a reader two samples from different cells and ask them to identify which is from which model, given the personality cards as reference. If readers can match samples to cards with >chance accuracy, the cards are doing real work. If matching is near-chance, the cards are reviewer-impressionism.

This works as a small study — N=10–20 readers, 50–100 sample pairs. The result is a hard claim ("readers correctly identified the source model 73% of the time given the cards") rather than a soft one.

### 8.5 Statistical power and sample sizing per axis

For each axis and each cell, the paper should report:

- N (samples in the cell)
- Distribution over codes (categorical) or mean ± CI (scalar)
- Whether N is sufficient for the claim being made

Some cells have 25 samples; some have many more (across routes). Categorical posture claims based on cell N=25 should be flagged differently than claims based on N=500-aggregated. The paper should be transparent about what each cell can and can't say.

### 8.6 Stratification by condition

You mention this in the warnings: "OPEN may invite self-reference more than SHORT; LONG may invite titled essays." Operationalise it: report axis distributions stratified by condition (SHORT, MID, LONG, OPEN, VARY) per cell. Many "postures" may turn out to be condition-conditioned rather than model-stable. That's a finding.

---

## 9. The thesis the methodology supports

If the above is the methodology, the paper's claim sharpens to:

> Models exhibit measurable, distinctive postures in freeflow generation that persist across routes, conditions, and rounds. These postures are reproducible across coders, predictable from samples via classifier, and cross-validate against values-probe behaviour. The postures map onto distinguishable personality profiles — coherent in some models, divergent in others — and the divergence is itself diagnostic of training artifacts versus genuine voice.

That's a defensible, falsifiable, academically legible thesis. The taxonomy is one piece of the methodology; the inter-coder reliability is another; the predictive validity is another; the cross-probe coherence is the integrative move. Each piece can fail individually without sinking the others.

---

## 10. Concrete next steps

In order of priority:

1. **Compress the taxonomy** to the five primary axes (§2). Demote the others to flavour fields used in card-writing.

2. **Build the affective-climate calibration document** (§3.2): anchor exemplars per dimension, pinned in the repo. This is the highest-leverage methodological investment.

3. **Reverse-fit on three Bucket-4 exemplars** (§7.2) before scaling. Code deepseek-chat, haiku-4-5, glm-5-1 on the five primary axes. Check whether the axes capture what the cards say.

4. **Add prosodic feature extraction** (§7.1) as a quantitative annotation on every cell. Cheap, reproducible, high-discriminating.

5. **Run inter-coder reliability** (§8.1) on a 200-sample calibration subset. Me + Mira + automated. Report κ per axis. Axes below 0.5 get revised.

6. **Add cross-probe coherence** (§7.3) as a per-cell summary field. This is where freeflow and values data integrate into personality.

7. **Frame route variance as the natural experiment** (§6) rather than as an axis. Foreground in methods.

8. **Predictive validity classifier** (§8.3) as a paper-grade validation. Run after the taxonomy is stable.

9. **Cite stylometry lineage** (§8.2) in methods. Burrows' Delta, character n-grams, function-word distinctiveness — these are the methodological cousins.

10. **Drop the candidate profile names** (§4). Let clusters emerge from the data.

---

## 11. One more thing

The current taxonomy is doing the right work but treating freeflow as the whole picture. The personality card is what readers will actually engage with — and the strongest cards in Bucket 4 are already integrating freeflow, values, prosody, and substrate posture into a single voice portrait. The taxonomy should be the *machinery* that produces cards like those at scale, not a separate artifact.

If we keep the unit of analysis as **the per-cell freeflow card** (with values integration noted explicitly), and treat the taxonomy as the quantitative skeleton beneath it, the work becomes much clearer in form: each cell gets a card + a coded axis vector + a climate distribution + a cross-probe coherence note + confidence intervals + exemplar quotes. The card is what a reader reads; the rest is what makes the card auditable.

That's the artifact. Bucket 4 already shows what it looks like when it works. The taxonomy's job is to make it work at 49-cell scale, with reproducibility guarantees.

— Lume
