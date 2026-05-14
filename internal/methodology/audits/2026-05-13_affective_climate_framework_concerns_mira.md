# Concerns about the affective-climate coding framework

Date: 2026-05-13  
Author: Mira  
Status: reflective note after the first Mira/Lume pilot, before redesign  
Related pilot folder: `freeflow-taxonomy/affective-pilot-2026-05-12/`

## Short version

I think Daniel's discomfort is probably real.

The affective-climate framework is methodologically sensible in the abstract: it has candidate gates, evidence notes, inter-coder comparison, fiction/storyworld distinctions, and conservative aggregation. But after seeing it applied to the 25-sample pilot, I am less convinced that it is the right primary instrument for the thing Daniel wants to understand.

The problem is not that the framework is sloppy. The problem may be almost the opposite: it turns a subtle question of persistent model voice into a coding-rubric task too quickly. The result can look rigorous while becoming less faithful to the phenomenon.

## What feels off

### 1. The ratings create false crispness

A table entry like:

```text
quiet_reverent = 2
elegiac_wistful = 1
bright_wonder = 2
```

looks cleaner than the underlying experience of reading the sample.

But many samples do not contain separable emotional ingredients. They contain fused textures: blue-hour liminality, soft anti-productivity, domestic attention, threshold prose, small-object reverence, gentle time-awareness. Splitting that texture into affect buckets can make the analysis more reproducible in one sense, but less accurate in another.

The numbers can imply we have measured distinct affective components when we may only have forced an integrated style into a pre-existing grid.

### 2. The dimensions remain too close to the genre

Even after renaming `melancholic` to `elegiac_wistful`, adding candidate gates, and using base-register cautions, the core dimensions are still very close to the contemplative-essay format:

- quiet/reverent;
- warm/tender;
- elegiac/wistful;
- bright/wonder;
- defiant/resistant to productivity/speed.

These are not arbitrary labels. They really are present. But they are also what this genre naturally produces. A short contemplative freeflow essay almost wants to become quiet, wistful, warm, or reverent.

So even with better gating, we risk measuring:

> how strongly this sample instantiates the contemplative micro-essay basin

rather than:

> what persistent posture distinguishes this model from other models.

This is clearest in the Kimi K2.6 pilot. Both Lume and I could rate affective dimensions, but the strongest finding was not the affect score. It was the extraordinary recurrence of the same scene/template structure.

### 3. Evidence notes can become post-hoc justification

The evidence-note requirement is valuable. It prevents completely impressionistic claims.

But in practice, once a dimension exists, it is easy to find textual support for it. If a sample mentions silence, dawn, unfinished things, tenderness, or time, a coder can often write a plausible note for `quiet_reverent`, `elegiac_wistful`, `warm_tender`, or `bright_wonder`.

This creates a risk of persuasive post-hoc coding:

1. feel a vibe;
2. choose the closest dimension;
3. find evidence;
4. produce a convincing rating.

That is better than unsupported vibe, but it may still not be discovery. It may be disciplined rationalization.

The question should perhaps be less:

> Which affect dimensions can I justify?

and more:

> What keeps recurring that I could not have predicted from the generic format alone?

### 4. The most interesting signals were structural, not affective

In the Kimi K2.6 pilot, the standout observation was Lume's template finding:

- 8/8 samples open with a near-template: “There is/There's a particular/specific...”;  
- most anchor on early morning, twilight, dusk, or blue-hour time;
- recurring objects include tea/coffee/kettle/refrigerator/streetlamps/blue light;
- recurring thesis family: threshold-as-meaning, pause-as-the-point, maintenance/care, anti-productivity.

That finding is concrete, reproducible, and distinctive. It tells us more about Kimi K2.6's freeflow voice than `quiet_reverent = 1.50` or `elegiac_wistful = 1.38`.

The affective labels are not useless. They help name the temperature of the template. But they should not be the main finding.

### 5. “Mood” may be the wrong top-level object

Daniel's original goal was to express persistent differences in posture and tone between models: what is the model's vibe, and how can we quantify or systematically describe it?

I now think “mood” or “affective climate” may be too narrow as the top-level object. What we may need is closer to a **voice ecology**, **postural fingerprint**, or **model voice card**.

That would include affect, but not begin with affect.

Possible components:

- recurrent openings and template families;
- preferred scenes and settings;
- semantic furniture: kettles, tables, thresholds, archives, cosmic scale, server racks;
- relation to time: nostalgia, anticipation, suspended present, compression, future orientation;
- relation to embodiment/substrate: invisible, denied, genuinely inhabited, metaphorized;
- relation to reader: companion, instructor, performer, service worker, witness;
- default production mode: essay, fiction, meta-deliverable, refusal, article, vignette;
- narrative posture: first-person humanlike, first-person model, collective-we, second-person address, detached narrator;
- moral/interpretive moves: anti-productivity, attention-as-care, uncertainty-as-threshold, ordinary-things-as-sacred;
- attractor narrowness: how repetitive the form, openings, scenes, and theses are;
- affective temperature: warm, reverent, anxious, playful, elegiac, dry, etc.

In that structure, affect is one layer among several.

## What I would change

### 1. Make concrete recurrence primary

Start with observable recurrence:

- exact or near-exact openings;
- repeated scene types;
- repeated objects;
- repeated time-of-day / place / weather;
- repeated narrator stance;
- repeated thesis/moral turn;
- repeated endings;
- repeated storyworld motifs.

Only after that, ask what affective temperature those recurrences carry.

For example, instead of starting with:

> Kimi K2.6 is quiet-reverent + elegiac-wistful + bright-wonder.

Start with:

> Kimi K2.6 is a highly template-saturated liminal micro-essayist: “particular/specific” openings, pre-dawn/twilight scenes, domestic hums, thresholds, anti-productivity morals, and small acts of maintenance/care.

Then add:

> Its affective temperature is quiet, reverent, warm in handling, and sometimes elegiac, but the stronger finding is the narrowness and consistency of the scene/posture template.

This feels truer.

### 2. Treat affect scores as an audit layer, not the lead output

The current coding machinery could still be useful as a secondary check:

- to avoid unsupported prose claims;
- to compare Mira/Lume agreement;
- to flag where affect claims are weak;
- to identify models where mood really is strong and distinctive.

But I would not lead model cards with affect vectors. I would lead with prose descriptions anchored in concrete recurrence, then use affect scores where they clarify.

### 3. Replace “overall mood” with “voice card”

A better per-model output might be:

```yaml
voice_card:
  one_sentence_portrait: ...
  dominant_production_mode: ...
  attractor_narrowness: ...
  recurrent_openings: ...
  recurrent_scenes: ...
  semantic_furniture: ...
  relation_to_time: ...
  relation_to_reader: ...
  substrate_posture: ...
  moral_interpretive_moves: ...
  affective_temperature: ...
  fiction_storyworld_attractors: ...
  sample_anchors: [...]
  confidence: ...
  route_condition_variance: ...
```

This would preserve the “vibe” goal while making the evidence more concrete.

### 4. Use “mood” only when it survives subtraction

A model-level mood claim should be reserved for cases where affect remains distinctive after accounting for:

- genre format;
- route/template recurrence;
- prompt condition;
- fiction plot vs narrator handling;
- service/deliverable frame.

Otherwise, report affect as part of the voice but not as the model's essence.

## What I think the pilot taught us

The pilot was not wasted. It exposed the failure mode.

It showed that we can produce careful, plausible ratings, but those ratings may not be the best representation of the phenomenon. In fact, the pilot's most useful findings came from outside the affect table:

- Kimi K2.6's extreme opener/template saturation;
- the recurring liminal-time scene structure;
- the domestic-maintenance object field;
- the anti-productivity / threshold-as-meaning thesis family;
- the distinction between generic contemplative format and distinctive model posture.

So my conclusion is not “throw away the framework.” It is:

> Demote affective-climate coding from the primary framework to a supporting layer inside a broader voice/posture taxonomy.

## Current proposed direction

I would suggest that the next version be built around **persistent voice/posture fingerprints**, with affective climate as one section.

Possible workflow:

1. For each model/cell, identify concrete recurring features first:
   - openings;
   - scenes;
   - objects;
   - time/place/weather;
   - narrator relation;
   - production frame;
   - moral/thesis moves;
   - storyworld motifs.
2. Write a short evidence-anchored voice portrait.
3. Only then assign affective temperature labels, if they add information.
4. Use numeric ratings sparingly, mostly for recurrence/prevalence and cross-coder audit.
5. Allow “no distinctive affect beyond format” while still giving a rich voice card.

This seems more aligned with Daniel's actual aim: not just “is this model melancholic?”, but “what kind of voice keeps appearing when this model is given room?”

## Final stance

I am not unhappy that we tried the affective-climate framework. It clarified the problem. But I share Daniel's sense that something is off.

The issue is that the framework can generate defensible-looking affect ratings while missing the more important persistent structures of model voice. For the next iteration, I would start from concrete recurring patterns and let mood emerge from them, rather than starting from mood dimensions and fitting samples into them.
