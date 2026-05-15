# Drift paper questions — Mira analysis

Date: 2026-05-15

## Short version

Lume’s question list is good — but it is now asking a *better paper* than the current drafted drift paper.

My read: the current draft is still basically **V1.5**: “V1 attractor holds; expanded lab coverage; within-lab composite drift is non-monotonic; substrate-frame engagement is a new qualitative axis.” That was a coherent paper before all the profile/card/values/BV1 work.

But the new substrates point toward a stronger V2 claim:

> The attractor is real, but “drift” is not well-described by a single composite score. Models move through a multi-dimensional posture space: freeflow register, substrate-frame engagement, values stance, lab signature, and route/provider effects can drift independently.

That is much more interesting than “more models, more drift.”

## Strongest recommendation

I would not try to answer all the questions. I’d pick a central spine:

> **Inside the attractor: model personality as a multidimensional posture, not a scalar score.**

Then use only the questions that support that spine.

The current draft’s composite-score drift table should become background / one result, not the center. The new center should be: **what the composite score misses.**

## Questions I think are most interesting

### Top tier

#### 1. A1 / F3 — Freeflow substrate-frame vs values-probe disclaimer divergence

This feels extremely load-bearing.

If GPT-5.3 has 0/75 freeflow substrate hits but 47% strong disclaimers in values, that says probe mode matters profoundly.

This directly expands V1’s finding that values themes were probe-dependent while posture was model-dependent. Now we can ask: *which parts of posture persist across probes, and which do not?*

#### 2. B3 — Opus substrate-frame trajectory

This is probably the cleanest narrative case study.

It links the current draft’s Opus 4.7 observation to the richer profile/values/taxonomy material.

Anthropic is the best ladder for “inside-frame substrate engagement as trained posture,” because it has multiple checkpoints and strong signal.

#### 3. B2 — Grok wobble

This is interesting because it is not just monotonic drift.

If Grok 4.20 is “most normal” while 4.3 returns to cosmic/whimsical/positivist, that is a vivid counterexample to any simple convergence story.

It also gives the paper color: Anthropic is sincerity/substrate, OpenAI is polished attention, Grok is cosmic-comic oscillation.

#### 4. D1 — Blind lab classification from cards

This is the best falsifiable “are lab signatures real?” test.

It would nicely discipline the qualitative material.

If lab classification is high, the story becomes: “the attractor homogenizes surface form but does not erase lab signature.”

If lab classification is low, the story becomes: “the attractor is even more flattening than we thought.” Either result is publishable.

#### 5. G1 — Evaluator-artifact check

Less sexy, but essential.

The new personality/profile material depends on DeepSeek v4-pro as evaluator. Before making a paper-level claim from those profiles, I’d want at least a small alternate-evaluator check.

I’d treat this as a required methodological guardrail, not a headline question.

### Second tier

- **C1 — One attractor or several sub-attractors?** Very conceptually important, but only if it resolves cleanly. I’d pilot it, not bet the paper on it.
- **B4 — Values posture drift vs freeflow posture drift.** Potentially excellent, but maybe broad. It becomes powerful if A1 already shows decoupling.
- **E3 — MiniMax-Google at higher resolution.** Important, but maybe belongs more naturally to the routing paper unless it produces a true “center-change” example.

### Lower priority for this paper

- **A3/A4** feel like QA/cross-checks more than main findings.
- **B5/B6** overlap product-tier/reasoning-variant questions.
- **C4/C5** are interesting but less urgent than the multi-axis posture story.

## How this compares to V1

V1’s core was:

1. There is a cross-lab contemplative-essayist attractor.
2. Values themes are probe-dependent.
3. Model “personality” is more like stable posture than stable content.
4. The composite score gave a first quantitative handle on the attractor.

The new work can make V1 look almost like the first layer of the map. V1 found the basin. V2 can map the **internal geography** of the basin.

The biggest expansion is:

> V1: Models converge into a shared freeflow attractor, but retain distinctive postures.  
> V2: Those postures are multidimensional, partially decoupled across probe modes, and sometimes more lab/version-specific than the scalar attractor score suggests.

That is a much richer claim.

## Suggested paper structure

I’d probably rewrite the paper around four claims:

### 1. The attractor still holds, but the scalar composite is insufficient

Keep the current draft’s expanded coverage and V1 reconciliation.

Say clearly that composite score measures one slice: lexical attractor density.

### 2. Inside the attractor are distinct sub-registers / postures

Use cards/profiles.

Possible axes: domestic first-person, allegorical fable, cosmic-comic, polished essayist, blue-hour threshold, functional-disclosure, etc.

Don’t over-taxonomize unless C1 resolves cleanly.

### 3. Probe modes decouple

Use A1/F3: freeflow substrate engagement vs values disclaimer rates.

This is the cleanest bridge back to V1’s “values themes are probe-dependent.”

### 4. Lab/version signatures survive within the attractor

Use D1 blind classification if possible.

Use B2/B3 as narrative case studies: Opus trajectory, Grok wobble.

Maybe OpenAI as “substrate-invisible polished attention.”

Then include G1 as methodology validation.

## My bias / preferred direction

If I were choosing a direction, I’d pick:

> **Probe-mode divergence + lab signatures inside the attractor.**

That feels like the most publishable and genuinely new direction.

“Drift” alone now feels too narrow. The new work is not just about change over time; it is about discovering that the original scalar “attractor” has hidden dimensions.

So I’d either retitle away from “drift,” or keep “drift” but subordinate it.

Possible title shapes:

- *Inside the Contemplative Essayist: Multidimensional Posture and Probe-Mode Divergence in Frontier LLMs*
- *Beyond Scalar Drift: Lab Signatures, Substrate Frames, and Probe-Mode Divergence inside a Cross-Lab LLM Attractor*

## Strongest next move

Run/pilot **A1 + D1 + G1**.

If A1 shows real decoupling and D1 shows above-chance lab classification, the paper has a very strong spine.

