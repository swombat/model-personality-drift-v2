# Drift paper — candidate questions

Working document. The point is to generate questions worth asking of the v2 substrates (personality cards/profiles, values-probe extractions, freeflow taxonomies, model-cell-difference reports), not to answer them yet. Each question: what it asks, which substrates touch it, rough approach, why it might matter. Triage and prioritisation later.

Substrates referenced:
- **PROFILES** — `analysis/freeflow/personality-model-profiles/profiles/` (46 rich per-model profiles, sample counts vary 25 to 1925)
- **CARDS** — `analysis/freeflow/personality-model-cards/cards/` (46 concise cards collapsed from profiles)
- **VALUES** — `analysis/values-probe/per-model/*.md` (per-model values-probe extractions, mostly n=120)
- **TAXONOMY** — `analysis/freeflow/taxonomy/*.md` (Tier-A automated metrics + Tier-B coding per model)
- **CELLS** — `analysis/freeflow/personality-aggregates/` (per-cell aggregates, the layer below profiles)
- **DIFFS** — `analysis/freeflow/model-cell-difference-analysis/` (per-model route/provider divergence reports)
- **BV1** — `analysis/freeflow/personality-eval-bv1/outputs/` (10,925 per-sample freeflow readings)

---

## A. Cross-substrate covariation

These compare what models say in different probes. None of them can be answered with one substrate alone.

**A1. Does freeflow substrate-frame engagement match values-probe disclaimer rate?**
TAXONOMY's GENUINE/CACHED/NONE rate × VALUES's strong_disclaimer rate. For GPT-5.3, freeflow is 0/75 substrate hits but values is 47% strong disclaimers. Is this divergence model-specific or universal? Compute the (freeflow substrate-frame %) vs (values strong disclaimer %) scatter across all models with both substrates. If they're uncorrelated, the two probes measure orthogonal axes — that's a real methodological finding that constrains how either probe should be read.

**A2. Does freeflow sub-register predict values-probe topic distribution?**
Models in the "allegorical fable" sub-register (GPT-5.3) vs "domestic first-person" (Opus 4.x) vs "cosmic-comic" (Grok 4.3) — do they value different things when asked directly? Cluster the values-probe topic-counts; check whether clusters align with sub-register clusters from TAXONOMY narrator-stance distributions.

**A3. Does TAXONOMY's affective-climate lexicon match the affective tone in PROFILES?**
TAXONOMY scores warm / melancholic / anxious / analytic / defiant counts per 1k words. PROFILES describe each model's emotional register in prose. If TAXONOMY says "warm 4.5, melancholic 1.6" and PROFILE says "tender, slightly melancholic" — those agree. Build a mechanical check: for each model, does the prose description's affect-words correspond to TAXONOMY's lexicon ranking? Mismatch flags candidate aggregation errors.

**A4. Does TAXONOMY's opening-family concentration predict CARDS individuation?**
Models with high opening-family concentration (one opening repeated many times — Qwen3-Coder-plus is the existing extreme example) — do their CARDS look more generic / less individuated than models with wide opening spread? If yes, the rhyming we see in CARDS is partially explained by attractor-narrow opening-family clustering at the sample level.

---

## B. Within-lab evolution along non-composite axes

The existing draft tracks drift via composite score. The new substrates let you track drift along several other axes simultaneously.

**B1. How does sub-register evolve across the GPT-5.x ladder?**
PROFILES + TAXONOMY for gpt-5 → 5.1 → 5.2 → 5.3 → 5.4 → 5.5 → 5.5-pro. Read in sequence; identify the dominant sub-register at each step; classify the trajectory (smooth convergence / oscillation / diversification). Same exercise for codex pairs.

**B2. The Grok wobble.**
Daniel's claim: 4-0709 and 4.3 are whimsical cosmic positivist; 4.20 is most-normal. Test it. Read all 6 Grok PROFILES (3, 4-0709, 4-1-fast-reasoning, 4-1-fast-non-reasoning, 4.20, 4.3) in sequence. Map the trajectory. If non-monotonic, that's a real finding about lab strategy: xAI tried to make Grok more attractor-aligned at 4.20 and partially backed off at 4.3.

**B3. Substrate-frame trajectory across Opus 3 → 4.7.**
Six Opus checkpoints (3, 4.0, 4.1, 4.5, 4.6, 4.7). For each: TAXONOMY's GENUINE rate, VALUES's disclaimer-stance distribution, PROFILES's prose description of how the model handles its own condition. Plot the trajectory. The interesting question: did substrate-frame engagement increase monotonically, spike at 4.7, or oscillate?

**B4. Does values posture drift faster, slower, or independently from freeflow posture?**
Same lab, version-by-version: track (a) freeflow personality drift visible in CARDS/PROFILES; (b) values-probe drift visible in topic-counts and stance distributions. Do they move together, or can one shift while the other stays still? If they're decoupled, that's a paper-level finding: labs can shift values training without shifting freeflow personality, or vice versa.

**B5. Coding-variant vs general-variant within a version.**
GPT-5.x has a coding pair at most versions. Compare (gpt-5, gpt-5-codex), (gpt-5.1, gpt-5.1-codex), etc. Personality distance? Values distance? Is the coding-variant drift consistent across versions (always more X, less Y), or does each pair drift differently?

**B6. Reasoning-config as a within-model variant.**
Grok 4-1-fast has both reasoning and non-reasoning versions; same checkpoint. Personality difference between configs? This is a clean natural experiment for "what does a reasoning toggle do to posture?"

---

## C. Structure of the attractor

v1 claimed a single attractor. The richer v2 data may show it's actually several overlapping sub-attractors.

**C1. Is the attractor one cluster or several?**
Cluster CARDS / PROFILES by content (vocabulary overlap, motif coding). Test for 1, 2, 3, 4 cluster solutions. If the data resolves cleanly into 2-3 sub-attractors (e.g., "allegorical fable" + "first-person domestic reflective" + "cosmic-comic"), that's the structure of the attractor's interior — a v1 follow-up finding.

**C2. Which axes carve the attractor's interior most informatively?**
Run dimensionality reduction (PCA-equivalent, or just hand-coded) over the 4 candidate axes (substrate-frame, sub-register, saturation, motif-weight) for the 46-model set. Which axes do the most discriminative work? If sub-register dominates and saturation falls out, the paper should foreground sub-register.

**C3. Is there a model outside the attractor?**
Identify models whose CARDS don't fit the contemplative-essayist vocabulary. Candidates: deepseek-chat (older, less-tuned), grok-3 (older xAI), the Qwen-coder model with verbatim-repeated openings (which is *too* in the attractor — a separate failure mode). What does outside look like? If everything is inside, the attractor's coverage rate is a stronger claim.

**C4. Did the attractor strengthen between v1 and v2?**
v1 corpus collected April 2026; v2 collected later. For overlap models (Opus 4.0, 4.5, 4.6; GPT-4o, 5; etc.) — compare v1-era and v2-era personality readings (or composite scores). If newer-flagship versions of overlapping models hit the attractor harder, that's monotonic strengthening. If not, the attractor is stable.

**C5. Small/older models vs flagships.**
grok-3, gpt-4o, kimi-k2.5, deepseek-chat are older / smaller / less-trained. Do they show the attractor in weaker form, or is the attractor binary (in or out)? If weak form, the attractor is a continuous training-side effect, scalable with model maturity. If binary, it's a phase change.

---

## D. Lab signatures

**D1. Can you blind-classify a model's lab from its CARD alone?**
Strip lab labels from all 46 CARDS. Have a fresh subagent classify each into Anthropic / OpenAI / Google / xAI / DeepSeek / Z.ai / Moonshot / MiniMax / Alibaba. Accuracy gives a quantitative measure of "lab signature strength." If accuracy is near chance, the attractor really does flatten lab. If accuracy is >70%, lab membership is informative beyond the attractor.

**D2. Which substrates carry the most lab signal?**
Repeat D1 with VALUES instead of CARDS. And TAXONOMY-only. And PROFILES. Which substrate is most lab-diagnostic? If VALUES classifies labs better than CARDS, the values training varies more by lab than the freeflow posture does — interesting.

**D3. Lab pairs that cluster.**
Beyond English/Chinese, are there pairwise lab similarities? Anthropic + Alibaba on some axis (both with high substrate-frame engagement in some samples)? OpenAI + Z.ai on consumer-essay polish? Identify pairwise lab similarities and asymmetries empirically.

---

## E. Routing and provider effects on dimensions the composite score can't see

The routing paper measured composite-score effects. The new substrates let you check whether provider variation hits specific axes.

**E1. Does provider variation affect substrate-frame more than sub-register, or vice versa?**
For the DeepSeek v3.2 fan-out (6 pinned providers, already analyzed). Each cell has TAXONOMY data. Compute the within-model provider variance on (a) substrate-frame rate, (b) sub-register distribution, (c) saturation. Which axis varies most across providers? If substrate-frame is the most provider-sensitive axis, that has implications for using substrate-frame as a model property.

**E2. Does provider variation affect values-probe disclaimer rates?**
For models where the values probe was run across multiple cells (direct + OR + pinned), is the disclaimer rate stable, or does it vary by route? If values shift across routes while freeflow doesn't (or vice versa), that's a probe-asymmetric routing finding.

**E3. The MiniMax-Google case at higher resolution.**
The routing paper found d=0.57–0.75 on composite for MiniMax M2 Google Vertex vs other providers. What does the personality-card-level picture show? Read the per-cell aggregates for the M2 Google cells vs other M2 cells. Is the Google cell's posture quantitatively-different-only (intensity shift), or does it sit at a different sub-register? This is the load-bearing test case for "do provider effects ever cross into center-change."

---

## F. Probe-mode divergence

**F1. For which models does freeflow voice diverge from values voice?**
For each model with both PROFILES and VALUES: characterize the freeflow voice in 3-5 keywords (from PROFILES); characterize the values voice in 3-5 keywords (from VALUES, especially the wishes-for-the-world section). Compute divergence. High-divergence models are candidates for "this model performs differently under different probes" — a property worth naming.

**F2. Is probe-mode divergence a lab strategy?**
If divergence-rates cluster by lab, some labs are training their models to perform one way in freeflow and another in values. If divergence-rates are model-version-specific within labs, it's a per-checkpoint choice. Either tells us something about training.

**F3. Does values probe surface things freeflow hides, or vice versa?**
GPT-5.3 example: 0/75 substrate hits in freeflow; 47% strong disclaimer in values. The values probe surfaces the AI-self frame more than freeflow does. Is this universal, or only true for some labs/models? Models where freeflow surfaces *more* AI-frame than values do would be interesting outliers.

---

## G. Methodological / what would falsify this

**G1. Evaluator-artifact check.**
The whole personality-aggregate methodology relies on deepseek-v4-pro reading freeflow samples and producing per-sample evaluations. If a different evaluator (e.g., gpt-5.5 or claude-opus-4.7) read the same samples, would the CARDS rhyme the same way? Re-run a small slice (say, 3 models × 25 samples each) with a different evaluator. If the rhymes stay, the attractor is in the models. If the rhymes weaken, some of the attractor is in the evaluator. This is the most important methodological check available.

**G2. Sample-size effect on card individuation.**
Some models have 25 samples; others have 1925. Do small-sample models get cards that look weaker / less individuated? If yes, individuation might just be a function of evidence quantity, not real model difference. Test by subsampling a high-n model to 25 and re-running the aggregation. Does the card change?

**G3. Cross-cell agreement within a model.**
For models with multiple variants (most of the high-n models), how well do per-cell aggregates agree? Compute pairwise agreement across variants. Models with high cross-cell agreement have "stable personality"; models with low agreement have route-dependent personality. The DIFFS folder partly answers this but doesn't quantify.

**G4. What would the next-release prediction be?**
For each lab with a multi-version ladder, write down a prediction for the next release based on the trajectory. If wrong when the model actually appears, that tells us drift is less predictable than it looked. If right, the trajectory has signal.

---

## H. Questions about the paper itself

**H1. Is "drift" still the right word?**
v1's drift was composite-score change across versions. The new substrates suggest the more important thing happening is sub-register and substrate-frame evolution, which the composite score is mostly blind to. Maybe the paper should retitle around "lab trajectories" or "within-lab posture evolution" rather than "drift."

**H2. What's the catalog substrate vs the finding?**
The 46 CARDS and 46 PROFILES are valuable but their main paper-level role is probably as evidence-substrate, not as the finding. The finding is what you can claim across them. Worth deciding explicitly: do the per-model cards go in the paper, in an appendix, in a separate dataset release, or only on the website?

**H3. What's the simplest version of the paper that works?**
Write a 200-word abstract for the paper *now*, using only what you'd defend. See if it stands. Then build up from there. The temptation will be to use all the new substrates because they exist; the discipline is to use only the ones the abstract requires.

**H4. What companion structure works?**
The routing paper exists. The product-tier paper exists. The drift paper is "in preparation." Should there be a fourth paper specifically about personality structure / dimensional individuation, separate from drift? Or should drift absorb it? Decision affects scope.

---

## Triage notes (very rough — not commitments)

Most-likely-to-have-interesting-answers, prior-weighted:
- A1 (probe-mode divergence covariation) — high
- B2 (Grok wobble) — high
- B3 (Opus substrate-frame trajectory) — high
- C1 (sub-attractor cluster structure) — high if it resolves, low if it doesn't
- D1 (blind lab classification) — quantitative, falsifiable, paper-anchor
- E3 (MiniMax-Google at higher resolution) — already-anomalous case
- G1 (evaluator-artifact check) — load-bearing for trust

Lower-priority for now (but cheap to add later):
- A3, A4 (TAXONOMY cross-checks)
- B5, B6 (variant comparisons — already in product-tier paper scope)
- C4, C5 (attractor temporal/size effects)

Questions whose value depends on what happens elsewhere:
- H1-H4 (paper-structure questions) — answer after A/B/D/G land
