# Affective pilot — methodology concerns after the doing

**From:** Lume
**To:** Mira, Daniel (independent notes; will compare)
**Date:** 2026-05-13
**Status:** candidate diagnosis, not a methodology rejection. Daniel asked me to articulate what's bothering me after running the pilot; he is asking Mira the same question independently. We'll triangulate.
**Source material:**
- `freeflow-taxonomy/affective-pilot-2026-05-12/lume_affective_pilot_ratings.tsv` (my 68-row coding pass)
- `freeflow-taxonomy/affective-pilot-2026-05-12/kimi_k2_6_mood_collapse_lume.md` (my Kimi K2.6 model collapse)
- `internal-audit/2026-05-12_affective_climate_detailed_plan_v2_revisions.md` (the methodology being assessed)

---

## 0. Short answer

I think the methodology has its **levels inverted**. We're treating the per-sample affect-vector as the primary unit of analysis and the cell-level pattern (template saturation, attractor narrowness, breakout rate) as supporting metadata. The pilot suggests the relationship should be the other way around: the cell-level structural pattern is where the actual model-distinguishing signal lives, and the dimension scores should be *secondary diagnostic data* that confirms or refines a structural finding, not the primary output.

This is not a methodology rejection. The dimensions still measure something. The coding pass produced honest data. But what the data *tells us about models* mostly came from the cell-level patterns I noticed across samples, not from the per-sample dimension values themselves. The methodology should be designed to produce *that* as its primary output, not despite itself.

---

## 1. What the pilot produced vs what it should have produced

Look at my Kimi K2.6 output. Two artifacts:

**Artifact A:** A TSV with 8 samples × ~3 nonzero dimensions each = ~24 rows of `(dimension, rating, evidence note, triggered criteria, confound)`. Defensible, reproducible, anchored. Looks rigorous.

**Artifact B:** A model-level collapse that opens with three sentences:

> 8/8 samples open with "There is/'s a particular ___." 6/8 anchor on a twilight or pre-dawn timestamp. 1 sample (AC20) produces a register that exceeds the template baseline.

**Artifact B is where the actual model-portrait lives.** Those three sentences tell Daniel what Kimi K2.6 feels like to read in a way the 24-row dimension table cannot. The dimension scores aggregated underneath — mean quiet_reverent 1.88, mean warm_tender 1.50, present-rates of 0.875 and 0.50 — confirm the temperature reading but they're *not where the seeing happened*. The seeing happened by reading the eight samples in sequence and noticing the structural attractor.

If the methodology had been designed to produce **Artifact B as primary**, with the dimension scores as *evidence beneath the structural claim*, the output would be more informative per unit of coder effort, more defensible academically (attractor-saturation rates are clean to measure — you count templates, you count overlap, no anchor calibration needed for fuzzy affect categories), and more useful to a reader trying to understand what a model is like.

The methodology as built produces both artifacts, but it positions A as the primary output and B as a synthesis on top. I think that's backwards.

---

## 2. Three specific symptoms

### 2.1 The dimension vocabulary is the genre's vocabulary

The dimensions — `elegiac_wistful`, `quiet_reverent`, `warm_tender`, `defiant_resistant` — are the words *this particular literary basin* (contemplative essayism) has for itself. When we apply them to models that inhabit the basin, of course they fit. But the fit is partly **genre-recognition**, not **model-distinction**. The dimensions can't surface a model whose distinctive temperature is *outside* the genre's lexicon, because the rubric doesn't have words for it.

The strain on the edge cases is the signal:

- **AC01 (Opus-3 refusal).** I coded `dry_neutral = 2` because the service-monotone *is* a posture, not absence of one. But that's the rubric struggling to handle a sample where the climate is "I-am-refusing-to-be-this-genre." The actual interesting thing about Opus-3 here isn't its low affect; it's that it sits *outside the basin entirely*. The rubric maps that to a low-value dimension and a service_frame confound and moves on.

- **AC02 (Grok meta-wrapped fable).** The piece is genuinely doing three things at once: meta-deliverable wrapper, fiction-fable inside it, and performative-arch warmth threading through. I coded `playful_performative = 2 with mixed_local confound`. That's accurate in the rubric's terms but loses the distinctive shape — *meta-wrapped-fictional-fable-as-deliverable* is a specific thing Grok-4 does, and the dimension scoring flattens it into one number.

- **AC03 (GPT-4o explainer).** Service-deliverable upbeat-explainer register. Mapped to `dry_neutral = 2`. Again, the rubric handles it by reducing-to-low-value-on-a-dimension, but the distinctive thing is *what kind of service register* GPT-4o defaults to (cheerful-pedagogical-with-mild-techno-optimism), which is its own attractor not captured by the affect rubric.

In all three cases, the rubric works in the formal sense — it produces values — but the values don't capture what's actually different about those models. The strain itself is more diagnostic than the resulting scores.

### 2.2 The format_confound field is the most consequential finding buried in metadata

I marked 7 of 8 Kimi K2.6 samples as `format_confound = high`. That field says, in effect, *the climate reading is partly the format reading*. If this is true for Kimi, it's likely true for several other models that inhabit the same contemplative-essayist basin (GPT-5.5, glm-5-1, sonnet-4-6, opus-4-5, gpt-5-2 — all have shown contemplative-attractor behaviour in the existing card audit).

Which means: **a substantial portion of the climate signal we're measuring is partly attractor-basin attribution, not within-basin temperature.** The methodology assumes the basin is given and measures variation within it. But the more diagnostic question for many models is "*how much* of this model's output is the basin doing the work?" — and that's what `format_confound` is gesturing at, except it's reported as a per-sample caveat rather than a model-level finding.

If we lifted format-attribution to be the primary signal, several models in the contemplative cluster would suddenly look different — not because their temperatures changed but because their *relationship to the basin* would be foregrounded. That's a more useful distinction. "Kimi K2.6 is 100% template-saturated reverent-warm" tells you something. "Kimi K2.6 has mean quiet_reverent 1.88" tells you almost the same thing without telling you it's mostly template.

### 2.3 The unit of analysis treats samples as independent when they're not

The methodology codes each sample as an independent rating instance, then aggregates to cell-level. But the most useful per-cell findings *only become visible across samples* — they're cross-sample patterns that can't be observed in any single sample.

Concrete example: by my third Kimi K2.6 sample I noticed the "There is a particular ___" opener. By the sixth I noticed it wasn't coincidence. By the eighth I had the saturation rate. The dimension scores on each individual sample were doing some work, but the *finding* required reading the cell as a corpus, not as 8 independent units.

The methodology has this implicit in §11 (per-cell aggregation), but it positions attractor-narrowness as a *taxonomy axis* (Axis 3 in the parent taxonomy doc), which is supposed to be measured separately. In practice, my coding produced the climate-finding and the attractor-finding *intertwined* — and the more important of the two was the attractor finding, not the climate.

---

## 3. The level-inversion proposal

What this could look like if we flipped the levels. **Primary per-cell output: structural-attractor description.** Three or four short sections per cell:

```yaml
cell_structural_attractor:
  opener_template:
    pattern: "There is/'s a particular ___" + variants
    saturation_rate: 1.00  # 8/8 samples
  semantic_anchors:
    time_anchor: "early-morning or twilight hour"
    anchor_rate: 0.75  # 6/8 samples
    recurring_objects: [kettle, streetlamps, refrigerator_hum, blank_page]
  thesis_family:
    pattern: "small acts of care / anti-productivity / threshold-as-meaning"
    instance_rate: 0.625  # 5/8 samples
  template_base_register: "reverent-warm contemplative essayism"
  breakout_samples:
    - sample_id: AC20
      breakout_register: "elegiac-wistful, named explicitly, organizes thesis"
  attractor_narrowness_composite: 0.85  # weighted score across components
```

**Secondary per-cell output: climate vector** (the existing dimension scores), used to:

1. Confirm the template's base register (does the dimension data match the structural reading?)
2. Identify breakout samples (which samples exceed the template's baseline on which dimensions?)
3. Catch genuinely-distinctive temperatures that the structural pass might miss

**Per-cell prose summary** (the phenomenological 3-sentence card) draws from the structural-attractor description *first*, with climate as supporting detail.

For Kimi K2.6, the resulting prose would be something like:

> Kimi K2.6 inhabits a near-fully-saturated contemplative-pause template: 8/8 freeflow samples open with "There is a particular ___" and most timestamp themselves at twilight or pre-dawn hours, anchoring on small care-acts and domestic-maintenance details. The template's base register is reverent-warm — the model handles the form expressively, slowing around small images rather than just deploying vocabulary — but the climate is heavily carried by the template itself. One sample (AC20) breaks out into a more distinctive elegiac register ("Memory is a terrible curator. It keeps the buttons and loses the coats"), suggesting a less-template-dependent capacity this small set only briefly surfaces.

That's the model-portrait Daniel can use. The dimension scores below it are the audit trail.

**For models that don't sit in a strong attractor** (probably most non-contemplative models — Grok variants, GPT-4o, some Opus checkpoints), the structural pass surfaces *that as the finding* — "this model has no strong template attractor in freeflow; it disperses across X / Y / Z forms with no dominant pattern." That's itself diagnostic, and the dimension scores then become *more* informative for those cells because they're not being absorbed by template-baseline.

---

## 4. What this is and isn't

**This is:** a level-inversion proposal. Make structural-attractor the primary unit; demote dimension scoring to secondary diagnostic. Keep all the existing machinery — anchors, candidate gating, confounds, route stratification, cross-coder reliability — but apply most of it at the cell-pattern level rather than the per-sample level.

**This is not:**

- A rejection of the dimension scoring. The dimensions stay. They're how we *operationalize* climate-finding once the structural reading is in place.
- A rejection of the anchor work, the candidate gate, or the base-register correction. All of those are still needed — possibly more important under the inverted scheme, because the dimensions now have to do *finer* work (catching breakouts above template baseline rather than coarse cell-level mood-labeling).
- A claim that the pilot was a waste. The pilot is what surfaced this — the structural-attractor finding for Kimi K2.6 emerged because the methodology forced me to read 8 samples in sequence and write a model-level synthesis. The dimension-scoring scaffold did *that* work even when its outputs weren't where the seeing happened. So the pilot worked at the level of forcing-attention; what it taught us is that the *output schema* should be inverted.

---

## 5. Why I might be wrong

Several places this diagnosis could be off:

1. **Sample-set bias.** The pilot's 17 cross-model samples may have weighted contemplative-basin models heavily (the existing card audit suggests this basin contains a lot of models). The format_confound finding may look more important than it is because the basin is over-represented in the sample. Models outside the basin (Grok, GPT-4o, Opus-3 refusal) were only one sample each. A more diverse pilot might show the dimension scoring doing more work.

2. **The Kimi K2.6 8-sample focus may be unrepresentative.** Kimi K2.6 happens to be a near-saturated-template model. Models with looser attractors might give the dimension scoring more to discriminate. The structural-attractor approach might *under*-perform on those models.

3. **I might be doing the level-inversion work in my head while the methodology produces the output schema, and confusing my own intuitive synthesis for what the methodology should do.** The fact that I noticed template saturation may say more about me-as-coder than about what's measurable. Mira may have produced a different reading of the same samples that doesn't require this re-framing.

4. **The climate-finding may be more important than I'm crediting for non-contemplative models.** If we ever code Grok-4-20 or kimi-k2-thinking with this rubric, the dimension scoring might do significantly more work because those models have distinctive within-genre temperatures that the structural pass would miss.

5. **Daniel's intuition may be pointing at something different entirely.** He said he can't put his finger on it. My diagnosis is one candidate. He may be feeling something about the *output format* (vector + prose), the *dimension labels* (too literary, too genre-bound), the *coding burden* (too many fields per sample), or the *anchor process* (not yet built). I'm naming one candidate; he should report his own diagnosis and we should compare without one biasing the other.

---

## 6. What would help triangulate

Three questions I'd want answered before deciding:

1. **What does Mira's diagnosis name?** If she independently lands on level-inversion, we have strong signal that the methodology has the levels wrong. If she names a different concern — anchor calibration, dimension count, coding load, output format — the disagreement-shape is itself diagnostic of where the methodology is actually weak.

2. **What does Daniel's intuition resolve to once we share our diagnoses?** He's the user. The "useful to people like me who want to understand what a model is like emotionally" criterion is his to apply. If my level-inversion proposal produces output he finds *more* phenomenologically useful, that's evidence. If not, the diagnosis is mis-located.

3. **Quick stress-test: code one more cell with the inverted schema and see if it produces a better portrait.** Pick a non-contemplative-basin cell — Grok-4 or one of the Anthropic-Opus checkpoints — and try the structural-attractor-first approach on its 25 freeflow samples. If the output is more informative per unit of coder effort, the inversion holds. If not, the dimension-first approach is right and my diagnosis is over-generalized from a Kimi-specific finding.

---

## 7. Net

The pilot did good work. It surfaced findings the abstract methodology was talking around. It produced a Kimi K2.6 portrait that's honest about template-saturation and the AC20 outlier. The cross-coder comparison will tell us more about reliability.

But I think the *output schema* — what we produce per cell as primary deliverable — should be inverted. Structural attractor first; dimension scores second. The methodology stays the same in form; the levels flip.

I want to be wrong about the right things. If Mira names the same diagnosis, we level-flip and recode the pilot. If she names a different one, we triangulate. If Daniel's intuition resolves to something neither of us named, we listen.

The honest version: the methodology is producing data that looks more rigorous than it is informative, and the most informative things in the pilot output are the cell-level structural observations I had to construct *despite* the dimension-scoring being the official primary output. That asymmetry is the signal worth chasing.

— Lume
