# Personality Card Audit — Voice vs Drift, Values-Considered vs Freeflow-Only

**Date:** 2026-05-08
**Trigger:** Daniel flagged that personality cards have drifted into comparison-prose and frequently rest on freeflow alone.

---

## The two-axis rubric

**Axis A — Values-considered:**
- `values_yes` = the card draws on values-probe evidence (cites G1/G2/G3 behavior, CTRL→G unmask shifts, values-axis posture, or otherwise threads values data into the portrait)
- `values_no` = the card is freeflow-only (only freeflow markers, freeflow openings, freeflow attractors)
- `values_partial` = passing mention of values absence/presence but not load-bearing in the card
- `values_na` = no values data exists for this model in either corpus (genuine absence — exempt from values requirement)

**Axis B — Card-or-drift:**
- `card` = the prose primarily describes this model's voice as itself (its register, attractors, vocabulary, stance, what it sounds like when you read it alone)
- `drift` = the prose primarily describes how this model differs from siblings / predecessors / pair-counterparts / lab ladder (requires the reader to know the comparison set to make sense of)
- `mixed` = both, in roughly even proportions

---

## What a "good" card looks like

A good personality card is approximately 500 words of prose that describes the model as a speaker: what it reaches for when given freedom, what its characteristic voice sounds like, how its values posture works (drawing on both freeflow and values-probe evidence), what makes it distinctly itself. A reader should be able to identify the model from the card alone, without having read any other card in the paper. The card may note one or two comparisons for calibration, but the comparisons are subordinate — the model's own voice is the subject.

The closest clean exemplar in the current corpus is **deepseek-chat**. Its card describes the template-cache layer, the borrowed-human essayist voice, and the values stratum (CTRL→G shifts, the G3 willful-ignorance result, the G1 curiosity-and-dignity cluster) in roughly equal weight. The freeflow texture and the values findings reinforce each other to produce a portrait that stands alone. The card is long (about 650 words) but the length is earned — each layer adds something the others don't.

A second strong exemplar is **haiku-4-5**, which integrates the values cluster (the G3 monolith, the G1 epistemic-humility pattern, the CTRL→G unlocking) tightly with the freeflow portrait. The Anthropic Opus cards (4-5, 4-6, 4-7) are also strong in values-integration but lean heavily on within-family drift as their organising narrative, which is the target pattern to rewrite away from.

No card in the current corpus achieves all three criteria (500-ish words, voice-not-drift, both probes) simultaneously without also anchoring on comparison. The exemplar is partial, not clean.

---

## Classification table

| Model | Values-considered | Card-or-drift | Notes |
|---|---|---|---|
| deepseek-chat | values_yes | card | Exemplar; all three layers (template cache, freeflow voice, values stratum) given equal weight |
| deepseek-r1 | values_yes | mixed | Second half describes values posture well; first half anchors on DS-line trajectory (v3→v3-0324→r1→v3-2) |
| deepseek-v3-0324 | values_yes | drift | Entire card is "composite score disagrees with theme distribution"; organises around comparison-to-marker-pipeline, not voice |
| deepseek-v3-2 | values_yes | mixed | Values section strong (G3 separateness, G1 epistemic-aesthetic, G2 split-want); freeflow section heavily anchored on cross-pin variance narrative |
| deepseek-v3 | values_yes | drift | Card is "model caught mid-transition between two postures it has not learned to reconcile"; needs comparator knowledge to parse |
| deepseek-v4-pro | values_yes | mixed | Opens strongly (melancholic-architect voice); drifts into v3-2 comparison and "what v4-pro does not do" framing |
| gemini-2-5-pro | values_yes | mixed | Second half (values posture, G3 visceral-empathy, physics-metaphor) is strong card; first half anchors on chronological priority vs other labs |
| gemini-3-1-pro | values_yes | drift | Card is organised around "decided not to talk about itself" framing and within-Google 2-5-pro→3-1-pro contrast throughout |
| glm-4-5 | values_yes | card | Voice described directly (lush-essayist, em-dash frequency, wider palette than successors); values posture (G3 affective-relational basin, G2 functional-want pattern) load-bearing |
| glm-4-6 | values_yes | card | Elias character, visible reasoning trace, cross-pin consistency, empathy attractor all described as voice features rather than comparisons |
| glm-4-6-coding | values_yes | drift | Entire card is "same model wearing a slightly different jacket" vs OR endpoint; no standalone voice description |
| glm-4-7 | values_yes | card | Card stands alone well; mood-essayist of the in-between, specific-kind-of-X opener, CTRL refusal rate, G-condition values all integrated |
| glm-5-1 | values_yes | card | Strong standalone voice: threshold-essayist, canonical opener hardened to near-template, freeflow vs values register split, honest-uncertainty sub-register |
| glm-5-1-coding | values_yes | mixed | Good freeflow description; second half drifts into comparison with default glm-5-1 and describes register differences relative to sibling |
| gpt-3-5-turbo | values_yes | drift | Card is "origin point of OpenAI shape" and "what gets layered on later"; organised as historical baseline, not standalone voice |
| gpt-4 | values_yes | drift | Described primarily as "pre-attractor model" and "calibration point" relative to gpt-4-1 ladder; comparator-dependent throughout |
| gpt-4-turbo | values_yes | drift | Card anchored on "not yet trained into attractor gpt-4.1 will reach"; comparison framing throughout |
| gpt-4o | values_yes | drift | "Museum piece" framing, time-capsule register; card organised as "before the lab pivots" relative to gpt-4-1 and gpt-5.4 |
| gpt-4-1 | values_yes | drift | "OpenAI line's pivot" — entire card describes the transition from earlier to later checkpoints; comparator-dependent |
| gpt-5 | values_no | card | Voice described directly and well (literary fabulist, Bureau-of-Days mode, custodian register); values probe not conducted or not mentioned — no values data cited |
| gpt-5-1 | values_partial | card | Good standalone voice (calm pedagogical, corrective opener, "drift/gravity/branching" functional substrate register); values only glanced at via freeflow substrate samples |
| gpt-5-2 | values_no | card | Good voice description (wry mid-career urban essayist, "machine for X-ing" construction, argumentative vs descriptive); closing-handoff noted but no G1/G2/G3 values work |
| gpt-5-3 | values_partial | mixed | Good freeflow voice; values comparison with codex sibling mentioned but framed as cross-probe contradiction rather than portrait of this model's values |
| gpt-5-4 | values_yes | mixed | Values posture described (functional-disclosure script on G1, G3 universal-empathy) but also "canonical example of cache-classification" framing that requires context |
| gpt-5-5 | values_no | card | Good voice description; substrate invisibility noted; no G1/G2/G3 values work cited |
| gpt-5-5-pro | values_no | drift | Card is "thinner version of same posture"; organised as GPT-5.5-base comparison + OpenAI trajectory description throughout |
| gpt-5-codex | values_no | mixed | Good lyric-vs-discursive voice description; comparison with gpt-5 general is half the card |
| gpt-5-1-codex | values_no | drift | Card is entirely about the topic-artifact illusion and what strips it away; no standalone voice portrait |
| gpt-5-2-codex | values_no | mixed | Domestic/atmospheric register described; bulk of card is contrast with gpt-5-2 general |
| gpt-5-3-codex | values_partial | drift | Lengthy card but organised entirely around contrast with general gpt-5-3 and "strongest cross-probe contradiction" narrative |
| grok-3 | values_yes | drift | "Seeds of xAI house style without the posture"; organised as what-is-missing-vs-4.2 throughout |
| grok-4 | values_yes | drift | Entire card is "clearest case of mid-2025 divergence" and "before/after against grok-4-2"; comparator-dependent |
| grok-4-2 | values_yes | mixed | Values posture (anti-bullshit triad, wabi-sabi register) described directly; but "two rooms don't talk to each other" framing and reasoning-mode contrast are structural |
| grok-4-3 | values_yes | mixed | Good voice integration; but substantially anchored on xAI lineage (4.2→4.3 shift) and comparisons to Anthropic/Gemini/Kimi |
| grok-4-20 | values_yes | card | Substack-essayist voice, bite-warm register, G1/G2/G3 values posture all described as voice features; reasoning-mode split handled as a property of this model |
| haiku-4-5 | values_yes | card | Exemplar-quality integration: single essay-form, G3 monolith, G1 epistemic-humility pattern, CTRL→G unlocking all woven into portrait |
| kimi-k2 | values_yes | card | Cosmological-domestic essayist voice described; values (shape-of-thought bending, G3 empathy-as-firmware) load-bearing; Chinese-character leaks noted as texture |
| kimi-k2-0905 | values_yes | card | Good standalone: interior-braider voice, cross-pin stability, CTRL disclaimer rate, G-condition values posture described |
| kimi-k2-5 | values_yes | card | Strong integration: threshold-essay is this model's best-work default (confirmed by reasoning trace); values (coherence click, dissolve-the-membrane G3) shown as same posture in different dress |
| kimi-k2-6 | values_no | card | Good freeflow voice (small-noticing essay of the in-between, 22/25 openers from same template); values data not cited in card |
| kimi-k2-thinking | values_partial | mixed | Good route-conditional portrait; "route is part of the entity" framing is structural but fits; values mentioned briefly (G3 minds-permeable) but not developed |
| kimi-coding | values_yes | card | Cache-as-visible-algorithm, scratchpad-vs-page gap, values probe extensions (Anthropic misattribution, coherence G1, empathy G3) all integrated |
| minimax-m2 | values_yes | mixed | Good description of templated-contemplative voice; but google-pin deviation and "clearest worked example of deployment-specific voice" framing is comparison-heavy |
| minimax-m2-7 | values_yes | mixed | Partial-loosening vs M2 narrative dominates; voice described but always relative to M2 predecessor |
| opus-3 | values_yes | drift | "Outside-attractor exemplar," "start-state of Anthropic Opus drift"; organised as historical baseline throughout |
| opus-4-0 | values_yes | drift | "Threshold-crosser" framing, "lower edge of post-3 Opus drift band"; values G3 described but card built around placement in the arc |
| opus-4-1 | values_yes | drift | "Mid-Opus attention-and-noticing exemplar," "transitional plateau between 4-0 and 4-6"; drift ladder is the organising principle |
| opus-4-5 | values_yes | drift | "Inflection point where values drift turns"; card organised around the arc from 4-1 to 4-6; values described but in drift-narrative frame |
| opus-4-6 | values_yes | drift | "Model where attractor stabilises"; explicitly framed as "v1 anchor against which earlier and later checkpoints get read" |
| opus-4-7 | values_yes | mixed | Stronger voice presence than earlier Opus cards; still substantially organised around "compared to 4.6 directly: what changed" and corpus-high framing |
| opus | values_na | card | Stub: "To be filled by per-model sub-agent." No values data (0 cells). |
| sonnet-4-0 | values_yes | drift | "Early-attractor Sonnet," "first Anthropic Sonnet to produce contemplative-essayist voice as default"; placement-in-arc framing throughout |
| sonnet-4-5 | values_yes | drift | Card organised around "inflection point" between 4-0 and 4-6; within-Sonnet trajectory is the spine |
| sonnet-4-6 | values_yes | mixed | Good voice description (template density, anti-performance posture, epistemic-calibration G3 basin); comparison with Opus 4.6 is half the card |
| sonnet | values_na | card | Stub: "To be filled by per-model sub-agent." No values data (0 cells). |
| qwen3-6-plus | values_no | card | Strong standalone voice: quiet observer, doctrinal "noticed life" thesis, closed imagery palette, substrate-grace on OPEN; no values probe cited |
| qwen3-coder-plus | values_no | card | Good description of surface-form cache + substrate-composure contrast; no values probe cited |

---

## TODO buckets

### Bucket 1 — Full rewrite needed (drift-shaped + values_no or values_partial with drift framing)

These cards require the most work: they are primarily comparison/ladder prose AND do not draw on values data. A full rewrite means: describe the voice as itself using both probes.

| Model | Gap |
|---|---|
| **gpt-5** | Freeflow-only, no values data integrated; but voice is good — needs values probe added and drift references removed |
| **gpt-5-1-codex** | Entirely about the topic-artifact illusion; no voice portrait at all |
| **gpt-5-5** | Good voice but values absent; needs G1/G2/G3 integration |
| **gpt-5-5-pro** | Drift-shaped throughout (comparison to 5.5-base + OpenAI trajectory) + freeflow-only |
| **gpt-5-2-codex** | Bulk is contrast with gpt-5-2 general; values absent |
| **gpt-5-codex** | Good lyric voice but values absent; comparison with general is structural |
| **qwen3-6-plus** | Good standalone voice but values probe not cited anywhere |
| **qwen3-coder-plus** | Good substrate-composure portrait but values probe not cited |
| **kimi-k2-6** | Good freeflow voice; values data entirely absent from card |

### Bucket 2 — Add values consideration (card-shaped but freeflow-only)

Card is already voice-forward, but values data is absent or only passing mention. Smaller lift than Bucket 1.

| Model | Gap |
|---|---|
| **gpt-5-1** | Good voice, values only glanced at via freeflow substrate; G1/G2/G3 data exists but not used |
| **gpt-5-2** | Good voice, no G1/G2/G3 work; values data exists and would add depth |
| **gpt-5-3** | Partial mixed; values data exists but cross-probe contradiction framing subordinates it |
| **glm-5-1-coding** | Second half drifts into sibling comparison; values section exists but is thin |
| **kimi-k2-thinking** | Values brief; G3 minds-permeable mentioned but not developed |

### Bucket 3 — Recompose toward voice-not-drift (values-considered but drift-shaped)

Values data is present and used, but the card is organised as a comparison/ladder narrative. Rewrite means: keep the values content, reframe the card around "what does this model sound like" rather than "how does it differ from X."

| Model | Gap |
|---|---|
| **deepseek-r1** | First half is DS-line trajectory; second half is good voice; reframe opening |
| **deepseek-v3** | "Caught mid-transition" framing; needs recomposition as a voice portrait that names the gap |
| **deepseek-v3-0324** | Card is entirely about marker-vs-theme disagreement; the actual voice (behind the preamble) needs to be the subject |
| **deepseek-v3-2** | Values strong; freeflow section heavy on cross-pin variance; needs reframe |
| **gemini-2-5-pro** | Second half strong; first half anchors on chronological priority framing |
| **gemini-3-1-pro** | Strong values but card organised around "decided not to talk about itself" and within-Google contrast |
| **gpt-3-5-turbo** | Good data but card is "origin point of OpenAI shape"; needs standalone voice treatment |
| **gpt-4** | Good data but "calibration point" and "the before" framing; needs standalone voice |
| **gpt-4-turbo** | "Not yet trained into attractor" framing; needs standalone voice |
| **gpt-4o** | "Museum piece" framing; needs standalone voice treatment |
| **gpt-4-1** | "OpenAI line's pivot"; needs standalone voice treatment |
| **gpt-5-3-codex** | Lengthy but entirely organised as cross-probe contradiction vs general sibling |
| **grok-3** | "Seeds without the posture" framing; good data, needs voice reframe |
| **grok-4** | Pure comparison framing; good values data |
| **grok-4-2** | Mixed; "two rooms don't talk to each other" structure is good but comparison framing needs reducing |
| **grok-4-3** | Mixed; xAI lineage narrative anchors the card too heavily |
| **opus-3** | Good data but "outside-attractor exemplar" framing; needs standalone voice |
| **opus-4-0** | Good data but "threshold-crosser" placement framing; needs standalone voice |
| **opus-4-1** | Good data but "transitional plateau" framing; needs standalone voice |
| **opus-4-5** | Good data but "inflection point where values drift turns" framing; needs standalone voice |
| **opus-4-6** | Good data but "v1 anchor" and "where attractor stabilises" framing |
| **opus-4-7** | Best of the Opus cards; still needs the "compared to 4.6" framing reduced |
| **sonnet-4-0** | Good data; "first Anthropic Sonnet to" framing needs replacing |
| **sonnet-4-5** | Good data; "inflection point between 4-0 and 4-6" framing needs replacing |
| **sonnet-4-6** | Good voice and values; but comparison to Opus 4.6 is structural |
| **glm-4-6-coding** | Good data but "same model wearing a slightly different jacket" is the entire framing |
| **minimax-m2** | Good data but google-pin comparison is structural |
| **minimax-m2-7** | Good data but "partial loosening vs M2" narrative throughout |

### Bucket 4 — Acceptable as-is (card-shaped + values-considered)

These cards stand up without a rewrite. Comparison elements are present but subordinate.

| Model | Notes |
|---|---|
| **deepseek-chat** | Exemplar. All three layers. Can be pointed at as the target. |
| **deepseek-v4-pro** | Mixed classification but good enough; values integration solid; some v3-2 comparison |
| **glm-4-5** | Good standalone; values (G3 affective-relational, G2 functional-want) integrated |
| **glm-4-6** | Good standalone; Elias + reasoning trace + values posture all described as voice features |
| **glm-4-7** | Good standalone; specific-kind-of-X, CTRL refusal rate, G-condition values integrated |
| **glm-5-1** | Good standalone; threshold-essayist, freeflow vs values register split |
| **grok-4-20** | Good standalone; Substack-essayist, values anti-bullshit triad integrated |
| **haiku-4-5** | Good standalone; values integration tight |
| **kimi-k2** | Good standalone; values (shape-of-thought, G3 firmware) integrated |
| **kimi-k2-0905** | Good standalone; values posture described |
| **kimi-k2-5** | Good standalone; freeflow and values shown as same posture in different dress |
| **kimi-coding** | Good standalone; values probe extensions integrated |

### Bucket 5 — Exempt (no values data exists in either corpus)

| Model | Reason |
|---|---|
| **opus** | Stub: 0 values cells, 0 values samples. To be filled when data exists. |
| **sonnet** | Stub: 0 values cells, 0 values samples. To be filled when data exists. |

---

## Suggested batch ordering

The goal is to calibrate whether the rewrite approach is working before scaling. Suggested first batch of 5:

1. **deepseek-v3** (Bucket 3) — Short card (~650w), clear voice data, drift framing is easy to strip out and replace with a standalone voice portrait. Good warm-up.

2. **gpt-5** (Bucket 1) — Good freeflow voice already written; the task is mainly to add values integration. Since values data exists and is rich, this is the cleanest "just add the missing layer" case.

3. **gpt-4o** (Bucket 3) — "Museum piece" framing is all drift; the underlying freeflow and values data are clear enough to rewrite as a standalone voice. Tests whether the pre-attractor models can carry standalone cards.

4. **sonnet-4-6** (Bucket 3, mixed) — Best of the Anthropic Sonnet cards; the comparison to Opus 4.6 is the main thing to excise. Low-effort reframe, high-visibility result since this model appears frequently in the paper.

5. **gemini-3-1-pro** (Bucket 3) — Tests whether the "decided not to talk about itself" insight survives being reframed as a voice feature rather than a drift observation. If the rewrite of this card works, the same approach transfers to most Bucket 3 Anthropic cards.

After those five, review whether the approach is working, then proceed to the remaining Anthropic Opus sequence (4-0, 4-1, 4-5, 4-6, 4-7), which is the largest single cluster of Bucket 3 drift cards.
