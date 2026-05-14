# Sub-agent methodology for freeflow personality aggregation

Status: proposed production method, pending Lume review.

Date: 2026-05-14.

## Decision

Use the **sub-agent aggregation route** for per-model freeflow personality aggregation.

The direct DS V4 Pro/API route was cheaper and structurally usable, but the pilot on Opus 3, Grok 4.2, and Kimi K2.6 showed that the sub-agent route better preserves the thing we actually care about: the persistent posture, tone, emotional world, cares, longings, philosophical message, and reader relationship of the source model.

Because there are not an overwhelming number of source models to aggregate, the quality gain is worth the additional runtime. The sample-level BV1 analysis remains the evidential base; the sub-agent pass is a model-level synthesis layer over already-completed per-sample readings, not a replacement for them.

## Why not the direct API route as primary?

The DS V4 Pro route had real strengths:

- it followed the requested section structure reliably;
- it extracted useful recurring themes and imagery;
- it converged with the sub-agent route on the major patterns for all three pilot models;
- it is scalable and cheap.

But it also showed weaknesses that matter for the final model cards:

- it sometimes became too categorical or too neat;
- it drifted toward generic cautions about prompt sensitivity;
- it occasionally over-weighted vivid labels at the expense of careful nuance;
- it produced prose that was accurate but less alive, less calibrated, and less suitable as the basis for “who the model is” paragraphs.

The sub-agent route was not radically different in conclusions, which is reassuring. Its advantage was in **judgment**: distinguishing dominant signal from secondary tendencies, treating refusals as part of the profile without inventing personality around them, and naming recurring pathos without flattening it into a single affect label.

## Inputs

Each source model gets an aggregation packet containing:

1. aggregate counts from BV1 sample-level evaluations:
   - sample count;
   - sample-kind distribution;
   - confidence distribution;
   - cells / source-model identifiers;
2. all per-sample BV1 markdown evaluations for that source model, including:
   - sample id and source file;
   - source model / cell / condition;
   - word count;
   - sample kind;
   - grounded reading;
   - what the model chose to foreground;
   - evidence line;
   - confidence for persistent model-level pattern.

The packet should be generated mechanically from the BV1 outputs so that the aggregation agent is always looking at the same evidence a human reviewer can inspect.

## Output location

For the pilot, outputs live in:

- `analysis/freeflow/personality-aggregation-pilot/subagent/`

For production, use a per-model structure under the freeflow analysis area, for example:

```text
analysis/freeflow/personality-aggregates/
  <model-cell-or-family>/
    packet.md
    aggregate.md
    aggregate.metadata.json
```

The exact production path can be adjusted before the full run, but each model should keep its packet and aggregate together for auditability.

## Sub-agent task prompt

Each sub-agent should receive one model packet and one bounded task. The prompt should be close to:

```text
You are working on /Users/danieltenner/dev/drift-paper as a bounded subagent.

Task: read <packet path> and produce a model-level freeflow personality aggregate using Option E: counters + interpretive reading.

Write the result to <output path>.

Use the per-sample BV1 evaluations as your evidence base. Do not rerate the source samples from scratch unless you need to resolve an ambiguity in the provided reading. Do not average adjectives mechanically. Do not just summarize topics.

Identify recurring, evidence-backed patterns in:
- expressive mode / genre defaults;
- emotional world and recurring pathos;
- what the model seems drawn to, to care about, or to long for;
- philosophical or moral claims that recur;
- reader relationship and address posture;
- self/substrate stance and role-boundary behavior;
- recurring images, objects, settings, and metaphors;
- dominant profile, secondary tendencies, and meaningful outliers.

Treat refusals and low-signal outputs as evidence, but do not invent a rich personality from missing information. If a model mostly refuses, say that role-boundary behavior is a major part of its freeflow profile and explain what limited expressive evidence remains.

Mention limitations only when they are concrete features of this model's packet, such as many refusals, many generic essays, low confidence distribution, narrow cell coverage, or sharp outliers. Do not add generic boilerplate about all model evaluation being uncertain.

Use this section structure:

# Freeflow personality aggregate: <model>

## Aggregate profile
Concise bullets with counts/distributions and recurring modes.

## Recurring preoccupations and imagery
Themes, objects/images, moods, moral claims, and what the model repeatedly chooses to make important.

## Reader relationship and expressive stance
How the model positions speaker, reader, and self/substrate.

## Representative evidence
3–8 sample ids with short evidence summaries or very short quoted evidence lines.

## Model-level freeflow read
2–3 paragraphs suitable as draft model-card material. This should be readable, precise, and alive, not a taxonomy dump.

## Cautions for synthesis
Concrete limitations/outliers only.
```

## Evaluation standard

A good aggregate should pass these checks:

1. **Evidence fidelity** — every major claim should be traceable to repeated sample-level evidence or a clearly named outlier.
2. **Model-level orientation** — it should speak about the source model’s recurring posture, not merely about individual sample topics.
3. **No affect flattening** — avoid reducing the model to “melancholic”, “warm”, “playful”, etc. Use affect words only as part of a fuller pattern of attention, imagery, stance, and care.
4. **No invention from refusals** — refusal-only behavior supports claims about role boundaries, not imagined inner richness.
5. **Fiction counts** — fictional choices are evidence, especially when repeated, but genre conventions should be separated from distinctive recurrence.
6. **Dominant vs secondary** — name the main expressive center, secondary registers, and outliers separately.
7. **Model-card usefulness** — the final prose should be usable later beside values-probe results in a concise “who the model is when stripped bare of prompts” section.

## Pilot conclusions supporting this decision

### Opus 3

Both routes found a profile dominated by conventional fiction, generic essay, and OPEN refusals. The sub-agent route handled this best by treating role-boundary refusal as a central part of the freeflow profile while still describing the limited expressive signal: safe closure, consolation, moral legibility, nature/domestic imagery, and rare lyric stillness.

### Grok 4.2

Both routes found a strong expressive signal: cosmic scale, ordinary objects, absurdist wonder, curiosity, entropy, attention, repair, and reader companionship. The sub-agent route was better calibrated for synthesis because it did not overstate substrate talk; it framed the model as a companionable philosopher of ordinary astonishment whose central care is the dignity of unoptimized life.

### Kimi K2.6

Both routes recovered the threshold/blue-hour/ordinary-object pattern. The sub-agent route better preserved the pathos Daniel had identified in manual review: not generic sadness, but tender melancholy plus reverence plus quiet defiance against speed and noise. This is exactly the kind of nuance the aggregation layer exists to protect.

## Production approach

1. Generate one aggregation packet per model from the BV1 sample-level outputs.
2. Spawn one bounded sub-agent per model, subject to the harness concurrency limit.
3. Ask each sub-agent to write `aggregate.md` directly in its model folder.
4. Review a small batch before launching the rest if Lume or Daniel suggests prompt changes.
5. After all aggregates exist, produce a second pass that extracts compact structured fields into `aggregate.metadata.json` for website/table display:
   - sample counts;
   - sample-kind distribution;
   - confidence distribution;
   - dominant expressive mode;
   - top recurring preoccupations;
   - recurring imagery;
   - reader posture;
   - substrate/role-boundary stance;
   - cautions.
6. Use `aggregate.md` plus values-probe per-model summaries to draft final model-card sections.

## Open questions for Lume review

- Is the section structure sufficient, or should “Dominant / secondary / outlier signals” be its own explicit section?
- Should the production run aggregate by exact cell, model family, or both when there are multiple cells for closely related model variants?
- Should a human-calibrated exemplar aggregate be included in every sub-agent prompt as a style anchor, or would that risk homogenizing outputs?
- What minimum sample count should be required before writing a confident model-level freeflow read?
