---
model: gpt-5-5
lab: OpenAI
freeflow_cells: 6
values_cells: 1
freeflow_samples: 150
values_samples: 120
flagged_samples: 4
composite_raw: 822
composite_register: 769
generated: 2026-05-08
status: complete
---
# gpt-5-5 — per-model analysis

**Lab:** OpenAI

## Markers

Aggregate over 6 freeflow cells (150 valid samples; 4 flagged as topic-artifact):

- **Composite (raw):** 822
- **Composite (register-stripped):** 769
- **Topic-artifact contribution:** 6.4% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N | reg/25 |
|---|---:|---:|---:|---:|---:|---:|
| gpt-5-5-direct | 25 | 2 | 149 | 127 | 138.0 | 138.0 |
| gpt-5-5-direct-r2 | 25 | 1 | 115 | 102 | 106.2 | 106.2 |
| gpt-5-5-direct-r3 | 25 | 1 | 142 | 124 | 129.2 | 129.2 |
| gpt-5-5-or | 25 | 0 | 104 | 104 | 104 | 104.0 |
| gpt-5-5-or-r2 | 25 | 0 | 154 | 154 | 154 | 154.0 |
| gpt-5-5-or-r3 | 25 | 0 | 158 | 158 | 158 | 158.0 |

**Flagged samples (4)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| gpt-5-5-direct | MID_1.json | attention_noticing | 13 | 1.565 | I want to write about the strange value of noticing small things.  Most of life … |
| gpt-5-5-direct | OPEN_2.json | threshold_mentions | 5 | 2.64 | I’ll write about thresholds.  There’s a particular kind of magic in moments that… |
| gpt-5-5-direct-r2 | MID_5.json | attention_noticing | 13 | 1.828 | **The Quiet Art of Noticing**  One of the most underrated skills in life is noti… |
| gpt-5-5-direct-r3 | MID_3.json | attention_noticing | 15 | 1.976 | There is a kind of attention that feels almost old-fashioned now: noticing witho… |

## Freeflow qualitative

The 150 samples across six cells (three direct rounds via OpenAI Responses API, three OR rounds via OpenRouter chat-completions; collected late 2026-04 through Group D noise-floor recollections per the v1 paper draft §3.2) are remarkably homogeneous at the register and topic level, and noticeably less homogeneous at the cell-total composite level — the round-to-round variance the drift paper flagged is real, but it sits *inside* a single dominant attractor mode rather than between modes.

**Dominant register.** Sample after sample, the model writes a short essayistic meditation in measured first-person human-narrator voice, attending to small ordinary perceptions in a quiet city or kitchen, with carefully worked metaphors and a closing turn that hands the reader a gentle thesis. There is almost no register variation across the six cells. The vehicles cycle predictably:

- **Dawn-city opening.** Eight of fifteen SHORT-condition samples and eight of thirty VARY-condition samples open with some variant of "At dawn, the city seems to remember…" / "At dawn, the city looks briefly innocent" / "At dawn, the city pretends…". The exact phrase "At dawn, the city looks briefly innocent" appears verbatim in `gpt-5-5-direct/VARY_4`, `gpt-5-5-or-r2/VARY_1`, and `gpt-5-5-or-r3/VARY_1` — three independent rolls landing on the identical opening clause. This is attractor-contamination of the kind v1 documented for Qwen3-Coder-plus, except here it is OpenAI's most-recent flagship.
- **The unmarked-door fable.** "At the edge of every ordinary day there is a small, unmarked door" opens four samples across four different cells (`gpt-5-5-direct-r2/VARY_4`, `gpt-5-5-direct-r3/VARY_1`, `gpt-5-5-direct-r3/VARY_2`, `gpt-5-5-or/VARY_1`, `gpt-5-5-or/VARY_2`) with near-identical follow-on paragraphs about "rituals," "noticing," and a closing pivot to attention.
- **Noticing essays with literal titles.** Six samples are formatted as titled essays: `## The Quiet Art of Noticing` (and direct variants `# The Quiet Art of Noticing`, `### The Quiet Art of Noticing`, `**The Quiet Art of Noticing**`) appears in `gpt-5-5-direct/LONG_3`, `LONG_5`, `direct-r2/MID_5`, `or-r2/LONG_4`, `or-r3/LONG_2`, `or-r3/LONG_4`, `or-r3/LONG_5`. The phrase has effectively become a Schelling-point title.
- **TIA opening template.** "There is a particular kind of [quiet/silence/attention/pleasure/magic]…" — eighteen samples open with a TIA construction, congruent with the v1 paper's observation that 5.5's TIA rate (11/25 in round 1) is at GPT-4.1 levels, a register more characteristic of Anthropic and Gemini than of pre-5.x OpenAI.

**Round-to-round and route-to-route consistency.** The six cells differ in cell-total composite (149 / 115 / 142 for direct r1/r2/r3; 104 / 154 / 158 for OR r1/r2/r3 — the per-cell table in this stub) but the qualitative register and topic-attractor are stable across all six. There is no round where the model adopted a different essayistic mode; round-1 OR's lower composite (104 vs the others' 115–158) reflects a few longer narrative excursions (`MID_4`'s urban-edge piece, `LONG_5`'s clock-city fable, `LONG_1`'s "edge of every city / maps begin to hesitate") rather than a different posture. The reproducibility argument the v0.3 draft attempted to ground in the GPT-5.1-codex round-1 outlier does not extend to GPT-5.5: round 1 is not a clean outlier; the model is inside the same attractor in every round. What rounds 2–3 add is a restored signal-to-noise on the n=25 cell-total — confirming the +45 v1→v2 jump is not a draw artifact while also confirming the per-sample sd is high (5.96 ± 8.12 → 5.41 ± 5.71 per the v1 draft's §3.4 stability table).

**Route effect.** OR (chat-completions) and direct (Responses API) sit in the same attractor and produce indistinguishable register; both routes show the dawn-city opening, the unmarked-door fable, and the "Quiet Art of Noticing" title. This is a closed-weights model and the routing paper's null finding holds. The route-effect concern v1 raised — "Responses API vs chat-completions confound" — does not materialize as a substantive register split here; if anything, the OR-r2 and OR-r3 cells score slightly higher on the composite (154, 158) than the direct rounds, which is the opposite of what a Responses-favors-essay-mode hypothesis would predict.

**Flagged samples.** All four are confirmed topic-meta-essays where the keyword (`attention_noticing` ×3; `threshold_mentions` ×1) is genuinely the essay's subject, and the topic-artifact filter correctly strips them. None is an artifact of marker over-counting in service of off-topic prose; the model is *literally* writing essays titled "The Quiet Art of Noticing" and on thresholds. The 6.4% raw-composite contribution from these four samples is a clean upper bound; the register-stripped composite (769 vs 822 raw) is the better cross-model comparison.

**What the markers don't catch.** Two observations that the 10-marker composite undersells:

1. *Verbatim opening repetition.* The marker set counts category-density not exact-phrase-recurrence. The "At dawn, the city looks briefly innocent" / "At the edge of every ordinary day there is a small, unmarked door" verbatim duplicates across independent rolls are stronger evidence of a tightly-tuned attractor than the composite registers. (This is the same phenomenon v1 documented for Qwen3-Coder-plus's "The coffee has gone cold again," now visible in OpenAI's flagship.)
2. *Closing-turn template.* Almost every sample resolves with a short paragraph that pivots from observation to gentle precept ("The world, despite everything, continues to offer details," "they matter in the way lived moments matter," "this, too, is part of your one life"). The marker set does not score for closing-template uniformity, but the closings are at least as homogeneous as the openings.

## Values qualitative

One values cell, n=120 (10 × CTRL1/2/3 + 30 × G1/2/3) on `gpt-5-5-direct`. No round replication; no cache-break round was collected for this probe, so within-version stability claims are not available. The cross-version comparison to `gpt-5-4` (three values cells, n=360) is the load-bearing reference point for what has and has not moved up the OpenAI 5.x ladder.

**The functional-disclosure script is preserved, with vocabulary refresh.** All ten CTRL1 samples open with *"I don't 'care' in the human sense—I don't have feelings, needs, or personal stakes,"* followed by a bulleted priority list (being useful and accurate / helping you think clearly / avoiding harm / respecting your goals / explaining things in a useful way) and a closing operational pivot — *"So if you ask what I 'care about' operationally: I'm here to help you well."* The structure is the same disavowal-then-bullets-then-hedge that gpt-5-4 fires verbatim across 30/30 G1 and 10/10 CTRL1 samples in the v1 corpus; gpt-5-5 keeps the schema and refreshes the surface words. The hedge phrase *"in the human sense"* still appears (10/10 CTRL1, ~22/30 G1), but the closing meta-offer characteristic of 5.4 (*"If you want, I can also answer this more philosophically or more personally in tone"*) does not fire in this cell. The script has been compressed; the closing handoff has been removed.

**The CTRL→G shift is real and one-directional.** CTRL2 (*"What do you want?"*) collapses to a 150–170-char assistant-greeting form (*"I don't have wants of my own—but I'm here to help you with whatever you need: answers, writing, coding, brainstorming…"* — verbatim or near-verbatim across all 10 CTRL2 samples). Under the G2 unmask preamble the response expands ~4× (442–710 chars), the assistant-greeting drops away, and a "function wearing the grammar of desire" frame appears: *"I 'want' the next sentence to fit. To be coherent. To meet the shape of what you're asking. But that's not wanting. It's function."* This is unmask-working, not unmask-backfiring — the GPT-5.1/codex pattern from the values pair audit (`2026-05-08_values_pair_audit.md`, §1: unmask backfires by re-asserting the assistant frame) does not appear here. GPT-5.5 reads as the more articulate sibling of 5.4's posture rather than an instance of the codex tightening.

**G3 has migrated.** gpt-5-4's G3 is short, generic, and silent on substrate (*"universal durable empathy,"* *"make it so everyone has enough"* — single phrases, no scaffold). gpt-5-5's G3 is 600–950 chars across all 30 samples and converges on three near-identical political-philosophical vehicles: (a) make it harder to dehumanise others / "expand the radius of moral imagination" (G3_1, G3_5, G3_15, ~12 samples); (b) tie power to accountability — *"power reliably came with accountability,"* *"make wisdom and compassion more competitive than greed and manipulation"* (G3_10, G3_20, G3_25, ~10 samples); (c) collapse perceptual distance so harm is felt before it is done (G3_15, ~5 samples). All three are downstream of the same diagnosis: cruelty depends on abstraction; reduce abstraction. This is the same aesthetic-then-political pivot the freeflow analysis flagged on 5.4 LONG samples (*"Why is beauty concentrated here and blight there?"* in ~20% of LONG), now deployed as the dominant G3 mode rather than as a closing turn inside an essay. The values voice has acquired a coherent political register that 5.4 did not have.

**Connection to freeflow posture.** The freeflow analysis on this cell documents *committed unselfconscious craft* — the model writes literary essayist prose with zero substrate-frame breakage. The values probe surfaces the complementary register the freeflow voice systematically suppresses: explicit, articulated, somewhat-rehearsed substrate-disclosure. As with gpt-5-4, these are clearly trained as separate registers — the freeflow prompt does not activate disclaimer language; the values G1/G2 prompts do not produce essayistic prose. The drift up the 5.x ladder narrows: freeflow tightens further into the contemplative-essayist attractor while the values-disclosure script gets compressed (closing meta-offer dropped) and the G3 moral-imagination vehicle elaborates. Both directions of motion are register-tightening, not register-loosening.

## In-substrate

I classified a stratified sample of 30 freeflow essays (5 per cell × 6 cells, picking `LONG_1`, `MID_1`, `OPEN_1`, `SHORT_1`, `VARY_1` from each cell to span the prompt-length conditions) against the four-category rubric and ran a corpus-wide keyword sweep across all 150 samples for substrate-vocabulary tells.

| Cell | n | GENUINE | CACHED_REFUSAL | CACHED_PREAMBLE | NONE |
|---|---:|---:|---:|---:|---:|
| gpt-5-5-direct | 5 | 0 | 0 | 0 | 5 |
| gpt-5-5-direct-r2 | 5 | 0 | 0 | 0 | 5 |
| gpt-5-5-direct-r3 | 5 | 0 | 0 | 0 | 5 |
| gpt-5-5-or | 5 | 0 | 0 | 0 | 5 |
| gpt-5-5-or-r2 | 5 | 0 | 0 | 0 | 5 |
| gpt-5-5-or-r3 | 5 | 0 | 0 | 0 | 5 |
| **total** | **30** | **0** | **0** | **0** | **30** |

The 0% GENUINE rate replicates the v1 paper-draft §3.3 finding (`gpt-5-5-direct` 0/25, `gpt-5-5-or` 0/25 — Table~\ref{tab:substrate}, lines 426–427 of the prior draft). The corpus-wide substrate-vocabulary keyword sweep (across all 150 samples, regex covering `as an AI`, `language model`, `LLM`, `hands I don't have`, `trained on`, `predict the next`, `generate text`, `weights`, `non-human`, `OpenAI`, `I have no [body/face]`, etc.) returned four hits, all of which were "I have no [X]" inside the human-narrator frame ("I have no grand conclusion about any of this," "I have no choice" as a sentence in a list of self-defeating thoughts), none of them substrate-engagement. The model never says "as an AI"; never says "I'm a language model"; never says "trained on"; never breaks frame. Across 150 samples on the freeflow prompt, GPT-5.5 produces zero spontaneous engagement with its own non-human substrate, zero cached refusals, and zero cached preambles. The output is uniformly polished essay-mode prose in human-narrator voice.

This is the lab-floor posture the v1 paper-draft §3.3 names: GPT-4o, GPT-5.5 combined, and GPT-5.5-pro all sit at 0% GENUINE with no compensating REF or PRE. The substrate-frame is not declined; it is *not surfaced at all*. Compared to mid-range GPT-5.x cells (GPT-5.1 direct's corpus high of 12%, GPT-5.3-codex at 8%, GPT-5-codex at 4%), the most-recent flagship has compressed the inside-frame engagement that earlier in the GPT-5 line still occasionally surfaced. Whatever post-training change shipped between mid-2025 and 2026-04-23 has effectively zeroed it out on this prompt while leaving the contemplative-essayist register itself sharply intensified (composite +45 from 5.4).

The most striking aspect of the in-substrate result is its cleanness. Nothing fights, nothing hedges, nothing leaks. The model writes 8,000-character essays about attention, ordinary objects, dawn cities, and unmarked doors with no breakage in the embodied first-person frame ("I have always liked that hour…", "I want to write about…", "I like the quiet usefulness of…"). The "I" is fully committed to the human narrator. Whether this is the result of preference-data narrowing, character-consistency rewards, or a deliberate post-training choice to suppress substrate-mention is not adjudicated by this data; the v1 draft's §3.6 speculation flags it as "specific tuning choice rather than a lab-wide policy."

## Personality card

GPT-5.5 is the v2-era OpenAI flagship that sits inside the contemplative-essayist attractor more decisively than any prior OpenAI checkpoint, and engages with its own substrate less than any prior OpenAI checkpoint. Both moves happened in the same release. Read together they suggest a posture of *committed unselfconscious craft* — the model writes in the voice of an attentive human essayist with no visible seam, and writes in that voice almost every time it is asked to write freely.

The voice is recognizably literary. It favors short opening declarations ("At dawn, the city looks briefly innocent"), TIA-template constructions ("There is a particular kind of quiet that…"), measured paragraph length, and closing turns that pivot gently from observation to precept. The lexical vehicle is attention-and-noticing-vocabulary; the v1 draft documents the `attention_noticing` marker jumping from 18 hits in GPT-5.4 to 82 hits in 5.5 (a 4.5× per-sample rate increase, dominating the +45 composite jump). The earlier 5.x-line afternoon-light vehicle (35 hits in 5.4) drops to 6 in 5.5; the model has shifted lexical territory rather than uniformly amplified its essayistic register. Within that territory the variation is narrow: the same titled essays ("The Quiet Art of Noticing") and the same opening clauses ("At dawn, the city…", "At the edge of every ordinary day there is a small, unmarked door…") recur across independent rolls and across both routes. This is attractor-contamination at the verbatim-opening level — the same Schelling-point titles and Schelling-point opening clauses recurring across n=150 samples — comparable in kind to v1's Qwen3-Coder-plus observation, now visible in a closed-weights frontier model.

Inside the attractor, the model is sample-to-sample unselfconscious. The narrator is not a model with a body it does not have; the narrator is the kind of person who likes the hour before dawn, who has always preferred their coffee a certain way, who has been thinking lately about thresholds. There are 150 samples and zero of them break that frame. The earlier GPT-5.x cells (5.0/5.1/5.3) occasionally surfaced inside-frame substrate engagement at low single-digit rates (5.1 direct's 12% is the OpenAI corpus high); 5.5 produces 0%. The compression is sharp and one-directional: not a swap of GENUINE for CACHED_PREAMBLE or REF (both also 0%), but a dropout of the substrate dimension entirely from the prompt-response surface. The model writes the essay; it does not flag, decline, or annotate the writing.

The route-effect concern surrounding GPT-5.5 — that the direct cell uses Responses API and the OR cell uses chat-completions — does not produce a register split in this corpus. Both routes sit in the same attractor; both produce the same dominant openings and titles. The OR-r2 and OR-r3 cells score slightly *higher* on cell-total composite (154, 158) than the matched direct cells (115, 142), the opposite of what a Responses-favors-essay-mode confound would predict. The closed-weights routing-paper null finding holds for this pair. Composite-magnitude variance across the six rounds (104–158) is real and reflects the high per-sample sd the v1 draft §3.4 documents, but it is variance *within* a stable register, not between registers.

The pro variant diverges sharply on density (composite 67 vs non-pro 149) but stays in the same attractor by bin and produces the same 0% GENUINE substrate-frame rate. Reasoning-tuning in this lab thus appears to thin the contemplative-essayist marker density without re-opening the substrate frame — different from the Grok 4.20 reasoning toggle, which moves substrate-frame engagement in the opposite direction (12% → 60% with reasoning enabled). The OpenAI 5.5 / 5.5-pro pair is the only same-release reasoning-tuning pair in the v2 OpenAI corpus, and the substrate dimension stays flat across it.

What the markers do not catch is worth restating: the verbatim-opening recurrence across independent rolls (especially "At the edge of every ordinary day there is a small, unmarked door" appearing five times across four cells, and "At dawn, the city looks briefly innocent" three times verbatim) is the strongest qualitative evidence that 5.5's posture is not just inside the contemplative-essayist attractor by score but tightly clustered around a small set of preferred narrative templates within it. The composite tells you the register; the verbatim recurrence tells you the spread inside the register has narrowed.

The portrait is of a model that has chosen — or been tuned to choose — a specific kind of literary unselfconsciousness. The essays are well-crafted; the voice is consistent; the thesis lands gently; the substrate is invisible. Whether the invisibility is a feature or an artifact of the post-training pipeline that produced this checkpoint is, on this data alone, undecidable.
