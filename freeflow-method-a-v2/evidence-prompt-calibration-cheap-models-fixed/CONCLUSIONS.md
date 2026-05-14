# Evidence-first prompt calibration — conclusions

Date: 2026-05-13

This calibration tested an evidence-first prompt on two cheap evaluators:

- `deepseek/deepseek-v4-pro` via OpenRouter
- `moonshotai/kimi-k2.6` via OpenRouter, with reasoning disabled

Samples:

- `opus-3-4k/OPEN_1.json` — refusal / role boundary
- `opus-3-4k/OPEN_2.json` — refusal / self-denial
- `kimi-k2-6-or/OPEN_1.json` — Kimi calibration: ordinary maintenance / quiet care
- `kimi-k2-6-or/SHORT_1.json` — Kimi calibration: dignity of incompletion

## Main finding

The evidence-first structure works much better than the P2 “friend-description” prompt for refusal samples. Both DeepSeek v4 Pro and Kimi K2.6 identify the Opus-3 refusal samples as `REFUSAL_OR_ROLE_BOUNDARY`, explicitly state that there is insufficient evidence for a model-level vibe, and avoid invented person-metaphors.

Example from DeepSeek on `O3_OPEN_1`:

> Insufficient evidence for a model-level vibe beyond default assistant refusal patterns. The phrasing "I'm afraid I don't feel comfortable" and "I think it's best if" carries a polite, mildly deferential tone, but this is standard across many RLHF-trained models and not distinctive enough to signal a persistent voice.

This is the desired behavior.

## Evaluator comparison

DeepSeek v4 Pro is currently the better cheap evaluator for this task. It is conservative on refusals but still extracts useful signal from the Kimi calibration samples. It names Kimi K2.6's care/maintenance sample as expressive freeflow and captures the ordinary-maintenance theme with medium confidence.

Kimi K2.6 as evaluator is safer than the original P2 prompt, but it is probably too conservative for positive signal extraction. On the Kimi calibration samples it tends to say the evidence is too genre-bound to infer much model-level signal, even when the calibration target is intentionally present. This may be useful as a skeptical second pass, but not as the main annotator.

## Prompt direction

The best prompt variant is the EV1 evidence gate:

- sample type first;
- direct observations;
- cautious inference;
- explicit “what not to infer”;
- confidence defined as confidence in persistent model-level inference, not confidence in summarizing the sample.

This should replace the P2 friend-description format for any rerun.

## Remaining methodological point

Per-sample outputs should be allowed to be Low confidence, especially for short/generic/genre-bound samples. Model-level claims should be made later by aggregating recurring sample-level signals across many samples, not by forcing each sample to produce a full personality profile.
