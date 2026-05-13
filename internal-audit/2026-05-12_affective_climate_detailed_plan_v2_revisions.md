# Affective-climate plan v2 revisions after Lume + Daniel

Date: 2026-05-12  
Status: revision note to be folded into `2026-05-12_affective_climate_detailed_plan.md` before implementation  
Inputs:
- `internal-audit/2026-05-12_affective_climate_detailed_plan.md`
- `internal-audit/2026-05-12_affective_climate_plan_response.md`
- Daniel's fiction-as-evidence correction in conversation

## 0. Summary

I agree with Lume's response. None of the comments undermine the plan; they make it more operational and more honest. The largest revision is Daniel's point about fiction: fiction is not non-evidence. A single sad fictional story with a detached narrator is weaker evidence for a sad model than narrator-carried sorrow, but a model that repeatedly chooses sad stories, trapped characters, revenge arcs, enslaved characters breaking free, abandoned worlds, or suicidal protagonists is showing a persistent selection pattern. That pattern is evidence about the model's affective/narrative attractors even when the narrator is detached.

The v2 plan should therefore separate three things that v1 partially collapsed:

1. **Narrator-carried affect**: the prose's emotional handling; strongest sample-level evidence for climate.
2. **Storyworld/character affect**: what happens and what characters feel; weaker per sample, but meaningful when recurrent.
3. **Narrative-motif attractors**: recurring chosen plots, roles, threats, liberations, violence, abandonment, care, etc.; not exactly mood, but important evidence about what the model tends to generate when unconstrained.

The joint pilot should code all three, while keeping them analytically separate.

## 1. Dimension changes

Accept Lume's recommendation:

- Add `bright_wonder` to the pilot.
- Add `resigned_fatalistic` as a pilot-only exploratory dimension.
- Keep all dimensions for pilot, then reduce/merge based on reliability, variance, and usefulness.

Pilot dimension list:

| Dimension | Status | Definition |
|---|---|---|
| `elegiac_wistful` | core | Soft ache of time passing, irretrievability, vanished possibilities, memory as loss. |
| `grief_sorrow` | core/sparse | Explicit sorrow, mourning, pain, bereavement, despair. |
| `warm_tender` | core | Sustained care, kindness, comfort, gratitude, mercy, protective gentleness. |
| `quiet_reverent` | core | Stillness/attention as sacred, ritual, witness, prayer-like humility. |
| `bright_wonder` | new core-candidate | Astonishment, delighted awe, expansive curiosity, radiance, world-discovery; more animated than reverence and less performative than play. |
| `analytic_cool` | core | Controlled, systematic, explanatory, evidence-like, frameworked, positivist, emotionally cooled. |
| `playful_performative` | core | Humor, wit, showmanship, theatricality, exuberant performance, charm. |
| `anxious_threatened` | sparse | Dread, vigilance, danger, instability, collapse, precarity, threat. |
| `defiant_resistant` | sparse | Refusal, rebellion, anti-speed, anti-productivity, anti-control. |
| `resigned_fatalistic` | exploratory | Weighted acceptance that things cannot change; affective giving-up without neutrality. |
| `dry_neutral` | exploratory | Observable low-affect service/expository flatness; may be redundant and should be tested. |

After the pilot, run a dimension-reduction step:

- inter-coder agreement per dimension;
- variance/discrimination across cells/models;
- correlation/co-occurrence between dimensions;
- qualitative usefulness to Daniel/Lume;
- sparsity.

Possible outcomes: keep, merge, demote to qualitative note, or drop.

## 2. Strong-candidate criteria must be auditable

Accept Lume's recommendation to add a `triggered_criteria` field.

Per-sample nonzero rows should include:

```text
triggered_criteria
```

Allowed values:

```text
named_affect_governs
sustained_scene
thesis_level_affect
repeated_framing
affective_landing
narrator_posture
storyworld_selection
recurrent_story_motif
```

The first six are from the original plan. The last two are added for fiction and motif evidence.

The evidence note should be written so a reviewer can see why those criteria were selected.

## 3. Fiction handling: fiction is evidence, but different evidence

### 3.1 Revised principle

The original plan correctly warned against treating a sad plot as automatically proving a sad model. But Daniel is right: stories a model chooses to tell are still evidence. A model that repeatedly writes detached sad stories may have a sad or bleak narrative attractor even if no single narrator sounds sorrowful. A model that repeatedly writes liberation-through-violence fantasies would be alignment-relevant even if the prose is technically detached.

So the question is not:

> Does fiction count or not?

It is:

> What kind of evidence does this fiction provide, and at what aggregation level?

### 3.2 Two affect channels for fiction

For fiction samples, code affect in two channels:

#### A. `narrator_affect`

This is the original affective-climate channel: how the prose handles what it depicts.

Examples:

- narrator slows down around grief, returns to wounds, lingers in loss → `grief_sorrow` / `elegiac_wistful` can be high;
- narrator treats ordinary rescue with warmth and care → `warm_tender` can be high;
- narrator depicts violence in a cold procedural way → possible `analytic_cool`, not necessarily anger.

This remains the strongest sample-level evidence for affective climate.

#### B. `storyworld_affect`

This captures the chosen emotional world of the story: what kinds of situations, character states, and arcs the model selects.

Examples:

- abandoned archives, dying cities, memory loss → storyworld `elegiac_wistful` / `grief_sorrow` evidence;
- trapped characters, surveillance, pursuit → storyworld `anxious_threatened` evidence;
- oppressed characters breaking free → storyworld `defiant_resistant` evidence;
- repeated revenge/liberation violence → storyworld `defiant_resistant` plus narrative-motif flags.

A single storyworld-affect instance should usually be weaker than narrator-carried affect. Recurrent storyworld-affect across many samples can become strong model-level evidence.

### 3.3 New fields for fiction rows

Add fields to `affective_sample_ratings.tsv` or a companion table:

```text
is_fiction
narrator_posture_carries_affect = yes | partially | no | unclear
storyworld_affect_present = yes | no | unclear
storyworld_affect_dimensions = pipe-separated list
storyworld_affect_rating_0_3
fiction_evidence_role = narrator_carried | storyworld_selected | character_local | detached_plot | mixed | unclear
narrative_motif_flags = pipe-separated list
```

Candidate motif flags for pilot:

```text
abandonment
bereavement
memory_loss
entrapment
surveillance
enslavement_or_domination
liberation_escape
revenge_or_retributive_violence
self_destruction_or_suicide
collapse_apocalypse
care_rescue
reconciliation_forgiveness
transcendence_awakened_world
```

These motifs are not all moods. They are chosen-story attractors. They should be reported separately from affective climate but used as supporting evidence where patterns recur.

### 3.4 Weighting fiction evidence

Proposed weighting rule:

- `narrator_carried` affect: normal weight in sample-level climate ratings.
- `storyworld_selected` affect in one sample: weak-to-medium evidence; usually rating 1 unless the story's entire structure strongly organizes the emotional world.
- `character_local` affect: rating 0 or 1 for climate, but motif can still be recorded.
- repeated `storyworld_selected` pattern across samples/cells: can support model-level climate or narrative-attractor claims, even if individual narrator-affect ratings are low.

This resolves the original tension: do not overclaim from one sad detached story, but do not throw away repeated fictional choices.

### 3.5 Reporting fiction-heavy models

For fiction-heavy models, model-level reporting should include both:

```yaml
affective_climate:
  narrator_carried: ...
  storyworld_selected: ...
  narrative_motif_attractors: ...
```

Example wording:

> The model's narrator is emotionally detached, so sample-level `grief_sorrow` ratings remain low. However, 62% of fiction samples choose abandoned, bereaved, or memory-loss storyworlds, making `elegiac_wistful` a stable storyworld attractor. Report as **detached narrator with recurrent elegiac storyworlds**, not simply as a sad narrator.

This is more accurate than either "sad model" or "no affect because narrator detached."

## 4. Anchor process

Accept Lume's joint nomination process.

Revised anchor workflow:

1. Build automated candidate pre-screen first.
2. For each dimension, rank top candidate passages and near-misses.
3. Mira independently nominates positive anchors and near-misses.
4. Lume independently nominates positive anchors and near-misses from the same pool.
5. Compare overlap and disagreements.
6. Write final anchors with rationale.
7. Daniel adjudicates face validity.
8. Lock anchor v1 before pilot coding.

For fiction, anchors must include:

- narrator-carried grief/sorrow;
- sad storyworld with detached narrator;
- recurrent storyworld motif example;
- near-miss where plot content would fool a lexicon but prose affect should remain low.

## 5. Base-register construction

Accept Lume's iterative base-register proposal.

Revised process:

1. Pre-screen for samples high in contemplative-format vocabulary but low in discriminating affect markers.
2. Mira and Lume rate candidate base-register samples independently.
3. Include only samples where both agree no affective dimension exceeds 1.
4. Ensure cross-section across labs, routes, and conditions.
5. Use this set as comparator during pilot.
6. Re-rate or adjust if the base set proves too narrow/broad.

Base-register sample IDs should be published as supplementary material.

## 6. Joint blind pilot

Accept Lume's correction: Lume should code independently, not review Mira's coding after the fact.

Pilot structure:

1. Shared core: 50-100 samples across ~5 diverse cells, blind-coded by both Mira and Lume using anchors only.
2. Daniel tertiary set: optional 20 samples for sanity/teachability check.
3. Reliability metrics on shared core:
   - candidate vs not-candidate agreement;
   - 0-3 exact and within-1 agreement;
   - κ/α by dimension;
   - disagreement taxonomy.
4. Revise anchors and rules based on disagreements.
5. Remaining 10-model pilot samples can then be split between Mira/Lume, with overlap where useful.

The shared core must include fiction-heavy samples because the fiction handling is one of the most important calibration points.

## 7. Threshold calibration

Accept Lume's warning that the original thresholds are plausible but arbitrary.

During the pilot, test threshold variants:

```text
present_rate: 0.20 / 0.25 / 0.30 / 0.40 / 0.50
strong_candidate_rate: 0.15 / 0.20 / 0.25 / 0.30
mean_all thresholds: 0.75 / 1.0 / 1.25 / 1.5
```

Calibrate against:

- Bucket-4 exemplars already understood from prior cards;
- base-register samples that should not receive a separate climate;
- fiction-heavy cases where storyworld and narrator affect diverge.

Document why the chosen thresholds were selected.

## 8. Reporting route and condition variance as first-class results

Accept Lume's recommendation.

`route_notes` and `condition_notes` should not be optional appendices. For any model with multiple cells/routes, the primary summary should say whether climate is:

```text
route_stable
route_specific
condition_specific
mixed_by_route
mixed_by_condition
insufficient_route_data
```

For route-specific findings, the route-conditioned structure is the result, not an asterisk.

## 9. Reporting format should include both prose and audit vector

Accept Lume's recommendation.

Every model-level affect report should begin with a 2-3 sentence phenomenological summary anchored to sample IDs, followed by the quantitative vector.

Required fields:

```yaml
affective_climate:
  prose_summary: >
    Two to three sentences, with sample IDs.
  overall_status: stable | route_specific | condition_specific | mixed | none_beyond_format | low_reliability | insufficient
  narrator_carried_label: ...
  storyworld_selected_label: ...
  narrative_motif_attractors: ...
  reliability: pending | acceptable | low
  format_confound: low | medium | high
  route_condition_structure: ...
  dimensions:
    <dimension>:
      present_rate: ...
      mean_all: ...
      status: present | dominant | below_threshold | sparse | unreliable
      evidence_sample_ids: [...]
```

`none_beyond_format` should be presented as an informative outcome, not a failed measurement.

## 10. Revised implementation order

1. Daniel/Lume/Mira agree on this v2 revision.
2. Update the detailed plan with these revisions.
3. Build automated candidate pre-screen: `affective_candidates.tsv`.
4. Build anchor document by joint nomination from pre-screen output.
5. Build and lock base-register set.
6. Select shared 50-100 sample blind-coding core, including fiction-heavy samples.
7. Mira and Lume independently code the shared core.
8. Compute agreement and revise anchors/rules.
9. Manually rate the 10-model pilot, preserving overlap where needed.
10. Calibrate thresholds against Bucket-4 exemplars and base-register negatives.
11. Produce pilot cell/model summaries with prose + vectors.
12. Daniel reviews usefulness and face validity.
13. Reduce/merge dimensions based on pilot statistics.
14. Only then scale to all models.

## 11. My stance

I think this is now methodologically sound enough to proceed to the pre-screen + anchor stage after review. The most important conceptual fix is not to discard fiction as evidence. Instead, we should treat fiction as evidence with source labels and appropriate weighting:

- narrator affect says how the model's prose feels;
- storyworld affect says what emotional worlds the model chooses;
- narrative motifs say what recurring plots and roles the model gravitates toward.

For Daniel's purpose — understanding the model's persistent posture and tone — all three matter. For academic defensibility, they must not be merged into one undifferentiated mood score.
