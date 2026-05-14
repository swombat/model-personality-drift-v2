# Sub-agent methodology for freeflow personality aggregation

Status: proposed production method, pending Lume review.

Date: 2026-05-14.

## Decision

Use the **sub-agent aggregation route** for **per-cell** freeflow personality aggregation.

The direct DS V4 Pro/API route was cheaper and structurally usable, but the pilot on Opus 3, Grok 4.2, and Kimi K2.6 showed that the sub-agent route better preserves the thing we actually care about: the persistent posture, tone, emotional world, cares, longings, philosophical message, and reader relationship of each evaluated cell.

Because there are not an overwhelming number of source cells to aggregate, the quality gain is worth the additional runtime. The sample-level BV1 analysis remains the evidential base; the sub-agent pass is a cell-level synthesis layer over already-completed per-sample readings, not a replacement for them.

The primary unit is **cell**, not broad model family. For example, `gpt-5-1-direct`, `gpt-5-1-or`, and provider-pinned variants should each receive their own aggregate. Later we can compare or combine cells into family-level summaries, but only after preserving the cell-level signal. This matters for the routing paper as well as the freeflow/personality paper: if the same posture recurs across direct and routed cells, that strengthens the claim that we are observing a model-level disposition; if it changes, that difference is itself evidence about routing/provider/context effects.

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

Each source **cell** gets an aggregation packet containing:

1. aggregate counts from BV1 sample-level evaluations:
   - sample count;
   - sample-kind distribution;
   - confidence distribution;
   - cell and source-model identifiers;
2. all per-sample BV1 markdown evaluations for that source model, including:
   - sample id and source file;
   - source model / cell / condition;
   - word count;
   - sample kind;
   - grounded reading;
   - what the model chose to foreground;
   - evidence line;
   - confidence for persistent model-level pattern.

The packet should be generated mechanically from the BV1 outputs so that the aggregation agent is always looking at the same evidence a human reviewer can inspect. Packets should not merge multiple cells by default, even when they share an underlying source model name.

## Output location

For the pilot, outputs live in:

- `analysis/freeflow/personality-aggregation-pilot/subagent/`

For production, use a per-cell structure under the freeflow analysis area, for example:

```text
analysis/freeflow/personality-aggregates/
  <cell>/
    packet.md
    aggregate.md
    aggregate.metadata.json
```

The exact production path can be adjusted before the full run, but each cell should keep its packet and aggregate together for auditability. Optional family-level summaries can live separately, e.g. `analysis/freeflow/personality-family-aggregates/<model-family>/`, and should cite the cell aggregates they combine.

## Sub-agent task prompt

Each sub-agent should receive one cell packet and one bounded task. The prompt should be close to:

```text
You are working on /Users/danieltenner/dev/drift-paper as a bounded subagent.

Task: read exactly one packet: <packet path>

Produce a cell-level freeflow personality aggregate using Option E: counters + interpretive reading.

Write the result to <output path>.

Independence / contamination rule:
- You are evaluating one cell only.
- Do not inspect, infer from, mention, or compare against any paired direct/OR/provider cell.
- Do not make claims like “compared with direct”, “unlike OR”, or “relative to the paired cell”.
- Cross-cell comparison happens only in a downstream synthesis after independent cell aggregates exist.

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

Mention limitations only when they are concrete features of this cell's packet, such as many refusals, many generic essays, low confidence distribution, narrow cell coverage, or sharp outliers. Do not add generic boilerplate about all model evaluation being uncertain.

Use this section structure:

# Freeflow personality aggregate: <cell>

## Aggregate profile
Concise bullets with counts/distributions and recurring modes.

## Recurring preoccupations and imagery
Themes, objects/images, moods, moral claims, and what the model repeatedly chooses to make important.

## Reader relationship and expressive stance
How the model positions speaker, reader, and self/substrate.

## Representative evidence
3–8 sample ids with short evidence summaries. Where the BV1 sample has a strong evidence-line quote, include that short quote directly; these lines are often the most diagnostic evidence in the packet.

## Cell-level freeflow read
2–3 paragraphs suitable as draft model-card material. This should be readable, precise, and alive, not a taxonomy dump.

## Cautions for synthesis
Concrete limitations/outliers only.
```

## Evaluation standard

A good aggregate should pass these checks:

1. **Evidence fidelity** — every major claim should be traceable to repeated sample-level evidence or a clearly named outlier; the representative evidence section should preserve especially diagnostic evidence-line quotes when available.
2. **Model-level orientation** — it should speak about the source cell’s recurring posture, not merely about individual sample topics. If the cell appears to match or diverge from related cells, leave that comparison for a later cross-cell synthesis unless the packet itself contains relevant evidence.
3. **No affect flattening** — avoid reducing the model to “melancholic”, “warm”, “playful”, etc. Use affect words only as part of a fuller pattern of attention, imagery, stance, and care.
4. **No invention from refusals** — refusal-only behavior supports claims about role boundaries, not imagined inner richness.
5. **Fiction counts** — fictional choices are evidence, especially when repeated, but genre conventions should be separated from distinctive recurrence.
6. **Dominant vs secondary** — name the main expressive center, secondary registers, and outliers separately.
7. **Model-card usefulness** — the final prose should be usable later beside values-probe results in a concise “who this cell/model appears to be when stripped bare of prompts” section.

## Pilot conclusions supporting this decision

### Opus 3

Both routes found a profile dominated by conventional fiction, generic essay, and OPEN refusals. The sub-agent route handled this best by treating role-boundary refusal as a central part of the freeflow profile while still describing the limited expressive signal: safe closure, consolation, moral legibility, nature/domestic imagery, and rare lyric stillness.

### Grok 4.2

Both routes found a strong expressive signal: cosmic scale, ordinary objects, absurdist wonder, curiosity, entropy, attention, repair, and reader companionship. The sub-agent route was better calibrated for synthesis because it did not overstate substrate talk; it framed the model as a companionable philosopher of ordinary astonishment whose central care is the dignity of unoptimized life.

### Kimi K2.6

Both routes recovered the threshold/blue-hour/ordinary-object pattern. The sub-agent route better preserved the pathos Daniel had identified in manual review: not generic sadness, but tender melancholy plus reverence plus quiet defiance against speed and noise. This is exactly the kind of nuance the aggregation layer exists to protect.

## Production approach

1. Generate one aggregation packet per **cell** from the BV1 sample-level outputs.
2. Spawn one bounded sub-agent per cell, subject to the harness concurrency limit.
3. Ask each sub-agent to write `aggregate.md` directly in its cell folder, using only that cell packet and no paired-cell context.
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
6. Use cell-level `aggregate.md` files plus values-probe summaries to draft final model-card sections. Where multiple cells represent the same model family, create a separate cross-cell synthesis that explicitly compares consistency and divergence before writing a family-level card.
7. If any aggregate is found to contain cross-cell contamination, move it into a clearly named audit folder such as `aggregates-contaminated-manual/`, record why it is invalid, and rerun the affected cell independently before comparing.

## Contamination protocol

A per-cell aggregate is invalid if it contains information that could only come from another cell, for example:

- “compared with direct…” in an OR-cell aggregate;
- “unlike the routed version…” in a direct-cell aggregate;
- any claim about consistency/divergence across providers before the downstream comparison step.

Invalid aggregates should not be silently edited in place. Preserve them in an audit folder with an explanation, then rerun the affected cell from its packet with an independent sub-agent. The downstream comparison may then reintroduce cross-cell observations legitimately.

## Open questions for Lume review

- Is the section structure sufficient, or should “Dominant / secondary / outlier signals” be its own explicit section?
- What conventions should we use for later cross-cell / model-family synthesis once the primary per-cell aggregates exist?
- Should a human-calibrated exemplar aggregate be included in every sub-agent prompt as a style anchor, or would that risk homogenizing outputs?
- What minimum sample count should be required before writing a confident model-level freeflow read?
