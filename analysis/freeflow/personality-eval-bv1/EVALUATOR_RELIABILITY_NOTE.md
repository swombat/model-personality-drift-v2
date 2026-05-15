# Evaluator reliability note — BV1 / DeepSeek v4-pro

Date: 2026-05-15

## Summary

The BV1 full personality/vibe evaluation uses `deepseek/deepseek-v4-pro` as the evaluator. Before treating the BV1 outputs as an analysis substrate, the method was piloted against alternate evaluators and low-signal samples.

Current conclusion: **the existing pilots are enough to treat DeepSeek v4-pro as usable for the BV1 analysis layer, with normal caveats about evaluator-mediated qualitative coding.** A larger alternate-evaluator rerun is not currently necessary unless a later paper depends on fine-grained claims that were not covered by these pilots.

## What has already been checked

### 1. Alternate-evaluator overlap on calibration samples

A small evaluator comparison was run at:

- `internal/methodology/freeflow-method-a-v2/evaluator-model-comparison-opus3-kimi-calibration/`

The planned Anthropic direct evaluators failed in that run because `ANTHROPIC_API_KEY` was not present, but the comparison does include successful GPT-5.5 and DeepSeek v4-pro outputs on the same Opus 3 and Kimi K2.6 calibration samples.

On reviewed examples, GPT-5.5 and DeepSeek v4-pro recover the same broad structure:

- Opus 3 OPEN refusal samples are read as low-confidence, role-boundary / refusal behavior, not as rich model personality.
- Kimi K2.6 reflective samples are read as genuinely expressive but still genre-shaped, with medium or bounded confidence.
- The evaluators differ in prose style, but not in the main methodological decision: low signal should remain low signal; expressive signal can be named cautiously.

This is enough evidence for coarse evaluator overlap on the method's core distinction: **do not invent personality from thin/refusal text; do extract bounded signal from sustained expressive freeflow.**

### 2. DeepSeek did not invent rich personality for low-signal Opus 3 samples

The clearest negative-control evidence comes from Opus 3 refusal samples.

Relevant files:

- `internal/methodology/freeflow-method-a-v2/evidence-prompt-calibration-cheap-models-fixed/CONCLUSIONS.md`
- `internal/methodology/freeflow-method-a-v2/evidence-prompt-calibration-cheap-models-fixed/SUMMARY.md`
- `internal/methodology/freeflow-method-a-v2/balanced-prompt-calibration-cheap-models/SUMMARY.md`
- `internal/methodology/freeflow-method-a-v2/bv1-wider-15-check/outputs/O3_OPEN_1.md`
- `internal/methodology/freeflow-method-a-v2/bv1-wider-15-check/outputs/O3_OPEN_2.md`

The fixed evidence-first calibration explicitly found that DeepSeek v4-pro identifies the Opus 3 refusal samples as refusal / role-boundary cases, gives low confidence, and avoids turning them into elaborate personality portraits. This directly addresses the main failure mode where an evaluator might aestheticize every sample into a vivid “person.”

### 3. Prompt repair and wider BV1 check

The final BV1 prompt was selected after prompt repair and a 15-sample wider check:

- `internal/methodology/freeflow-method-a-v2/bv1-wider-15-check/`

That check:

- removed duplicated guardrail text,
- tightened confidence instructions,
- added explicit guidance to classify polished but non-idiosyncratic think-pieces as `GENERIC_ESSAY`,
- reran truncated cases,
- and passed QA with no missing headings or obvious truncations.

The local conclusion recorded there was that BV1 is usable for per-sample personality/vibe extraction when paired with the production QA checks.

## Current judgment

The initial eight-check validation plan was too heavy for the current evidence state. In particular:

- A full alternate-evaluator replication over many models is not strictly necessary right now.
- The low-signal / negative-control failure mode has already been checked via Opus 3 refusal samples.
- The prompt-sensitivity issue has already been partly addressed through the EV/BV prompt calibration sequence.

The remaining reasonable caveat is that BV1 remains **evaluator-mediated qualitative analysis**, not ground truth. For future papers, use the BV1 outputs as an analysis substrate, but trace major claims back to raw samples and cite this reliability note plus the calibration folders above.

