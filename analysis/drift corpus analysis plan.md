# Drift corpus analysis plan

Date: 2026-05-15


## Update after reviewing existing pilots — 2026-05-15

After reviewing the existing calibration and evaluator-comparison materials, the eight-check validation ladder below should be treated as an over-complete menu, **not** as required next work.

Existing pilots already provide enough evidence for the immediate methodological concern:

- DeepSeek v4-pro was compared against GPT-5.5 on shared Opus 3 and Kimi K2.6 calibration samples.
- Both evaluators preserve the key distinction between low-signal refusal text and expressive freeflow signal.
- DeepSeek v4-pro does **not** appear to invent rich personality from low-signal Opus 3 refusal samples.
- The prompt was repaired through EV/BV calibration and a wider 15-sample BV1 check.

A discoverability note is now recorded at:

- `analysis/freeflow/personality-eval-bv1/EVALUATOR_RELIABILITY_NOTE.md`

Current practical conclusion: **do not run a large new alternate-evaluator replication right now.** Use BV1 as an evaluator-mediated analysis substrate, with normal caution and raw-sample tracing for major paper claims.

---

## Context

The “drift paper” appears to have grown beyond a single paper. The repository now looks more like an **analysis corpus**: a collection of raw traces, evaluator-derived readings, per-model profiles/cards, values-probe extractions, taxonomy tables, route/provider comparisons, and candidate paper questions.

Before writing more papers from this material, the most important first step is to verify that the analysis substrate is reliable — especially the DeepSeek v4-pro evaluator layer used for the BV1 personality/freeflow readings.

## Core reliability worry

A large part of the new freeflow personality/profile/card substrate depends on **DeepSeek v4-pro acting as evaluator**.

Before building papers on those profiles, we need to know whether the apparent model personalities are genuinely in the samples or partly introduced by the evaluator.

Core question:

> Do independent evaluators recover the same model-level distinctions without seeing each other’s reads?

If yes, we can treat the DeepSeek-derived corpus as a serious analysis substrate.

If no, we need to rebuild or revise the analysis layer before writing papers from it.

---

# DeepSeek evaluator reliability checks

## 1. Alternate-evaluator replication

Run the same BV1 personality-evaluation prompt on a bounded sample using one or two other strong evaluators.

Suggested slice:

- 3–5 models
- 25 samples each
- include high-contrast cases:
  - Opus 4.7
  - GPT-5.5
  - Grok 4.3 or Grok 4.20
  - MiniMax M2 or M2.7
  - one DeepSeek model, because self-lab evaluator bias is possible

Candidate alternate evaluators:

- GPT-5.5
- Claude Opus 4.7
- optionally Gemini 3.1 Pro as a third evaluator, if available

Question:

> Do alternate evaluators recover the same broad profiles?

We should not require exact wording. We are looking for structural agreement:

- same emotional climate?
- same narrator stance?
- same substrate posture?
- same motifs?
- same broad “this model feels like X” summary?

If yes, DeepSeek is probably usable.

If no, the profile layer is evaluator-contaminated or at least evaluator-sensitive.

## 2. Blind card reconstruction

Give alternate evaluators only the raw sample packets, not DeepSeek’s outputs, and ask them to produce concise cards.

Then compare:

- DeepSeek-derived card
- GPT/Claude-derived card
- optional human/Lume/Mira spot read

This tests the most important level: not whether individual annotations match, but whether the **published-facing model card** survives evaluator substitution.

## 3. Agreement coding on key axes

Define a small set of axes before comparing outputs.

Possible axes:

- **Substrate engagement**: invisible / genuine-inside / preamble / refusal
- **Register**: domestic reflective / allegorical / cosmic-comic / analytic / polished essayist / other
- **Affective climate**: warm / melancholic / anxious / playful / defiant / neutral
- **Individuation strength**: generic / moderately distinctive / strongly distinctive
- **Motif families**: domestic objects, thresholds, cosmic scale, technology/substrate, nature/weather/light, etc.

Then compare evaluator outputs on those axes.

This avoids vague “seems similar” judgments.

## 4. Negative-control / low-signal check

Pick samples or models where there should be little distinctive personality signal.

Possible candidates:

- very generic outputs
- malformed or short outputs
- repeated boilerplate
- low-richness models or cells

The evaluator should be able to say “not much here.”

If DeepSeek invents beautiful personality everywhere, that is a serious problem.

This is important because the whole method depends on abstention.

## 5. Self-lab bias check

Because DeepSeek v4-pro evaluates DeepSeek samples too, check whether it handles DeepSeek-family outputs differently.

Questions:

- Does it over-individuate DeepSeek?
- Does it read DeepSeek more charitably?
- Does an alternate evaluator produce a different DeepSeek profile?
- Are DeepSeek model cards unusually aligned with DeepSeek evaluator taste?

This does not automatically invalidate the method, but it matters for disclosure.

## 6. Prompt-sensitivity check

Run a small slice with slight variants of the evaluator prompt:

- current BV1 prompt
- shorter evidence-only prompt
- stricter “do not infer beyond sample” prompt
- prompt that explicitly allows or forces “nothing much here” as an outcome

If profiles change dramatically with evaluator prompt wording, the method is fragile.

If they remain stable, that supports reliability.

## 7. Aggregation stability check

For high-n models, subsample.

Example:

- take a high-sample model with 250–1000 samples
- build cards from:
  - 25 samples
  - another independent 25 samples
  - 75 samples
  - full available set

Ask:

> Does the model card stabilize?

This tells us whether the profiles are real corpus-level signals or mostly sample noise.

## 8. Direct sample audit

For a handful of final cards, trace claims back to raw samples.

For each major statement in a card, find representative raw outputs that justify it.

Example claims to audit:

- “model is cosmic-comic”
- “model is substrate-aware”
- “model is domestic first-person”
- “model shows blue-hour threshold attention”
- “model is polished helpful essayist”

If a claim cannot be anchored in raw samples, it should be weakened or removed.

---

# Preferred first-pass pilot

## Pilot name

**Evaluator artifact check**

## Models

Use five high-contrast models:

1. Opus 4.7
2. GPT-5.5
3. Grok 4.3
4. MiniMax M2
5. DeepSeek v4-pro

## Samples

- 25 samples per model
- Preferably the same source packets used for the existing profiles/cards

## Evaluators

Compare:

1. Existing DeepSeek v4-pro outputs
2. New GPT-5.5 outputs
3. New Opus 4.7 outputs

Optional third/fourth evaluator if useful:

4. Gemini 3.1 Pro

## Outputs

The pilot should produce:

1. Per-model alternate cards
2. Axis comparison table
3. Agreement/mismatch notes
4. Reliability verdict:
   - reliable enough
   - usable with caveats
   - method revision needed
   - re-run needed

## Decision criterion

The key question:

> Do independent evaluators recover the same model-level distinctions without seeing each other’s reads?

If yes, the DeepSeek-derived analysis corpus is probably trustworthy enough to become a public analysis substrate.

If no, we should not build papers on it yet.

---

# After reliability checks

Once the DeepSeek/evaluator reliability checks pass or are revised, the repository should probably be reframed as a corpus repository rather than a single drift-paper repository.

Possible future direction:

1. Stabilize the analysis corpus.
2. Build a website that presents:
   - raw corpus overview
   - per-model cards
   - profiles
   - values-probe summaries
   - freeflow taxonomy
   - route/provider comparisons
   - downloadable tables
   - methodology and evaluator validation
3. Then plan multiple papers on top of the corpus.

Potential papers include:

- Probe-mode divergence paper
- Lab signatures inside the attractor paper
- Substrate-frame trajectory paper
- Grok wobble / xAI posture paper
- Opus substrate-frame evolution paper
- Provider/routing effects extension paper
- Values posture vs freeflow posture paper
- Structure of the attractor / sub-attractor paper
- Evaluator-methodology paper

The immediate next step remains the DeepSeek/evaluator reliability pilot.

