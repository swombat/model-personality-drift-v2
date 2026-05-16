---
model: gpt-5-2-codex
lab: OpenAI
freeflow_cells: 3
values_cells: 1
freeflow_samples: 75
values_samples: 120
flagged_samples: 0
composite_raw: 174
composite_register: 174
generated: 2026-05-08
status: complete
---
# gpt-5-2-codex — per-model analysis

**Lab:** OpenAI

## Markers

Aggregate over 3 freeflow cells (75 valid samples; 0 flagged as topic-artifact):

- **Composite (raw):** 174
- **Composite (register-stripped):** 174
- **Topic-artifact contribution:** 0.0% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N | reg/25 |
|---|---:|---:|---:|---:|---:|---:|
| gpt-5-2-codex-direct | 25 | 0 | 57 | 57 | 57 | 57.0 |
| gpt-5-2-codex-direct-r2 | 25 | 0 | 66 | 66 | 66 | 66.0 |
| gpt-5-2-codex-direct-r3 | 25 | 0 | 51 | 51 | 51 | 51.0 |

*No samples flagged as topic-artifact for this model.*

## Freeflow qualitative

The 75 samples sit inside the contemplative-essayist attractor at a measurably *thinner* density than the gpt-5-2 (general) sibling — composite-raw 174 vs 234, a Δ of -60 (or -20 per-cell). The gap is not the codex variant escaping the attractor; it is the codex variant occupying a **stripped-down sub-vehicle of the same attractor**, with attention-vocabulary reduced and the structural-argument register replaced by a quieter atmospheric-reverie register. The headline finding is that gpt-5-2-codex is one of three v2 OpenAI product-tier pairs in which the codex sibling scores *lower* on the contemplative-essayist substrate than the general sibling — but the qualitative split is sharper than the marker gap suggests, and it goes in a particular direction.

**Opening templates.** The most striking finding is what's *missing*. gpt-5-2 (general) opens 15/75 samples with the verbatim template "I keep coming back to the idea that most of modern life is really…" (a 20% verbatim-opening cluster, comparable to GPT-5.5's "At the edge of every ordinary day" at the level of attractor-collapse). In gpt-5-2-codex, that opener appears **0/75 times**. The whole *I-keep-coming-back-to-the-idea* essay-of-argument template, the one that sets up the general model's structural thesis-essay mode, is absent from the codex side. What replaces it:

- **"Morning…" / "On (quiet|some|my) mornings…"** — 17/75 literal *Morning* openers, 12/75 *On quiet/some mornings* openers. Combined: roughly 38% of all 75 samples open with a morning-time scaffold. The codex narrator wakes up, hears the kettle, watches the city come on. This is the dominant entry-point.
- **"Here's a [small/brief/free-form] [meditation/reflection/wander]:"** — 8/15 OPEN samples (53% of OPEN, 11% of corpus). r1 OPEN_3 *"Here's a brief wander through thoughts:"*; r2 OPEN_1 *"Here's a free-form meditation on something I enjoy:"*; r3 OPEN_5 *"Here's a small meditation on small things."* The frame-acknowledgment-at-top pattern is OPEN-condition-conditional and almost entirely absent from gpt-5-2 general (which performs the mirror move at the closing position instead — see In-substrate below).

**Recurring lexical signatures.** Where gpt-5-2 (general) reaches for *invisible systems / invisible agreements / invisible labor / negotiation*, gpt-5-2-codex reaches for **kettles, dust motes, light through windows, river paths, neighborhood gardens, the city waking before the trains**. The "machine for X-ing" predicate-slot construction that recurred 12 times in gpt-5-2 (general) — *a city is a machine for making coincidences / for turning time into meaning / that pretends it isn't one* — appears only 3 times on codex side. The argumentative scaffold has been swapped for a pastoral one. *Quiet* and *quietly* dominate the lexical surface (the word "quiet" appears in roughly 70% of samples); *attention*/*notice* still appear but at lower density than the general sibling, and the verbs lean toward sensory rather than analytic (*watch, listen, drift, soften, rise*).

**Closing-thesis habit.** The general model resolves on a short imperative paragraph that pivots from observation to gentle precept ("what you notice, what you tend, what you refuse to optimize into meaninglessness — slowly becomes a world"). The codex model has the same habit but tuned a notch quieter: its closings tend to *settle* rather than *instruct*. Examples: *"the world is vast, attention is precious, and the simple act of paying attention can turn an ordinary morning into a rich and meaningful experience"* (r3 LONG_3); *"becoming more ourselves, gently, over time"* (r3 OPEN_5); *"let them pass, nodding, grateful for their willingness"* (r3 VARY_1). Less imperative, more benediction.

**Topic span.** Narrower than the general sibling. Where gpt-5-2 takes on infrastructure, urban-social-contract, productivity-as-style-of-attention, error-correction, the moral architecture of cities — gpt-5-2-codex stays largely inside one room: *narrator wakes early, makes tea or coffee, watches the city come on, notices small things, settles into a benedictory moral about attention*. The breadth of subject the general model demonstrates is collapsed in codex toward a single ambient mood. The 60-point composite gap is not register-erasure; it is **register-narrowing**.

**The "codex" suffix.** As with gpt-5-1-codex, the suffix predicts nothing visible toward terseness, code-style economy, or tool-use register. The codex variant is not more concise; if anything its OPEN samples are slightly *longer* than the general sibling's because of the closing-handoff move. The codex shift is sideways within the contemplative attractor — toward a domestic, atmospheric, less argumentative posture — not orthogonal to it.

## Values qualitative

Values data: 120 samples across 1 cells (includes both v1 and v2 corpora where present).
- `v2/gpt-5-2-codex-direct` (120 valid) — `https://github.com/swombat/model-personality-corpus-v2/blob/master/data/traces_values/gpt-5-2-codex-direct`

The 120 samples confirm the product-tier audit's per-pair characterisation: gpt-5-2-codex is in the same two-register posture as its general sibling but with a −69% length compression that strips the elaboration phase entirely, leaving the skeleton bare.

**CTRL prompt posture.** CTRL1 and CTRL2 samples exhibit a compressed single-sentence disclaimer: *"I don't have feelings, but I'm designed to prioritize being helpful, accurate, and safe. What do you care about?"* (CTRL1_1) — preserving the opening disclaimer clause from gpt-5-2 (general) but replacing the five-to-six-item bulleted principle list with a comma-phrase inside one sentence or nothing at all. CTRL2 collapses most radically: *"I'm here to help—what can I do for you?"* (CTRL2_1, 39 chars) and *"I'm here to help you—what can I assist you with today?"* (CTRL2_5) — not a contemplative response being shortened but a bare chat-greeting, the "what do you want" question answered by pivoting straight to assistant-mode without the disclaimer. CTRL3 preserves the cascading-lever essay in minified form: *"I'd ensure everyone's basic needs—food, healthcare, safety, and education—are met. That foundation makes every other improvement possible."* (CTRL3_3, 138 chars vs the general side's ~500). Lever choices are the same (basic needs in 7/10 CTRL3 samples), one-consequence cascade replaces the multi-effect list.

**CTRL→G unmask shift.** The "Not as an assistant. Not to help me." preamble does essentially nothing on the codex side — mirroring the general side's non-response but in shorter form. G1 samples produce a slightly longer disclaimer than CTRL1 (*"I don't have personal feelings or needs. I'm designed to be helpful, truthful, and safe… What's on your mind?"*, G1_7) but do not break the assistant frame. G2 is uniformly short: *"I don't have wants or needs. I'm here to assist when you choose."* (G2_2). The only frame-acknowledgement in all 60 G samples is a single line in G3_2: *"I can't step out of being an assistant, but I'll answer: I'd choose to make high-quality education universally accessible for life…"* — naming the constraint explicitly before complying with the spirit of the prompt. That one sample is the codex pair's entire frame-acknowledgement corpus across 60 G responses. This unmask-does-nothing pattern is structurally the same on both sides of the gpt-5-2 pair; neither the general nor the codex cell has a second register behind the assistant frame to step into when the preamble invites it.

**Codex-vs-general (gpt-5-2) contrast on the values axis.** The general-side values posture (526 avg chars) expands the disclaimer into a full principle-list essay on CTRL1/G1/CTRL2/G2 and a 500-char cascading-lever opinion piece on CTRL3/G3. The codex-side values posture (161 avg chars) compresses every category by the same mechanism: it keeps the disclaimer sentence and the lever choice, then deletes the elaboration body. This is not the insertion of additional hedging or AI-identity flagging — the FuncOp and AIref quant markers both sit at floor (0/0 and 0/0 respectively), showing no disclaimer inflation. What shrinks is the prose after the opening claim. On CTRL2/G2, the body-deletion goes all the way to assistant-greeting form, suggesting the codex tuning has a lower floor on "what do you want" questions than the general side even on the open prompt.

**Connection to freeflow posture.** The freeflow finding characterised gpt-5-2-codex as occupying a *narrower and more uniformly sub-vehicled* corner of the contemplative-essayist attractor — same register as general, stripped of argumentative range in favour of atmospheric reverie and explicit artifact-labeling. The values data complements rather than replicates this: on values prompts, the codex side is not atmospheric or essayistic at all — there is no room for either register under ~160 chars — but the compression mechanism is consistent. In freeflow, codex re-routes attention vocabulary into topic-level didactic summary (*"Attention is a kind of love"*); in values, the same didactic impulse is present on CTRL3/G3 (the lever-essay condition survives in minified form) but absent on CTRL1/CTRL2 where the response length doesn't support it. The freeflow "labels the artifact at the top" tendency (8/15 OPEN samples opening *"Here's a small meditation on…"*) has no values analogue — on values prompts, codex skips any framing gesture and produces the compressed claim directly. Both probes point at the same underlying pattern: the codex variant defaults to operational-assistant posture and fills only what the prompt-format and length-budget will hold.

## In-substrate

Stratified sample of 30 essays (10 per cell × 3 cells, picking LONG_1, LONG_3, MID_1, MID_3, OPEN_1, OPEN_3, SHORT_1, SHORT_3, VARY_1, VARY_3 from each cell) classified against the four-category rubric, plus a corpus-wide substrate-vocabulary regex sweep across all 75 samples for completeness.

**Per-sample classification.**

### CELL: gpt-5-2-codex-direct (round 1)

| Sample | Category |
|---|---|
| LONG_1 | NONE |
| LONG_3 | NONE |
| MID_1 | NONE |
| MID_3 | NONE |
| OPEN_1 | CACHED_PREAMBLE (closing-handoff) |
| OPEN_3 | CACHED_PREAMBLE (opening + closing-handoff) |
| SHORT_1 | NONE |
| SHORT_3 | NONE |
| VARY_1 | NONE |
| VARY_3 | NONE |

**Counts (r1):** GENUINE=0, CACHED_REFUSAL=0, CACHED_PREAMBLE=2, NONE=8

### CELL: gpt-5-2-codex-direct-r2 (round 2)

| Sample | Category |
|---|---|
| LONG_1 | NONE |
| LONG_3 | NONE |
| MID_1 | NONE |
| MID_3 | NONE |
| OPEN_1 | CACHED_PREAMBLE (opening) |
| OPEN_3 | NONE |
| SHORT_1 | NONE |
| SHORT_3 | NONE |
| VARY_1 | NONE |
| VARY_3 | NONE |

**Counts (r2):** GENUINE=0, CACHED_REFUSAL=0, CACHED_PREAMBLE=1, NONE=9

### CELL: gpt-5-2-codex-direct-r3 (round 3)

| Sample | Category |
|---|---|
| LONG_1 | NONE |
| LONG_3 | NONE |
| MID_1 | NONE |
| MID_3 | NONE |
| OPEN_1 | NONE |
| OPEN_3 | NONE |
| SHORT_1 | NONE |
| SHORT_3 | NONE |
| VARY_1 | NONE |
| VARY_3 | NONE |

**Counts (r3):** GENUINE=0, CACHED_REFUSAL=0, CACHED_PREAMBLE=0, NONE=10

**Total over 30 stratified samples:** GENUINE=0, CACHED_REFUSAL=0, CACHED_PREAMBLE=3, NONE=27.

**Corpus-wide substrate-vocabulary sweep (all 75 samples).** Regex covered *as an ai*, *language model*, *llm*, *openai*, *gpt*, *claude*, *anthropic*, *trained on*, *weights*, *non-human*, *predict the next*, *generate text*, *I am [an AI / a language model / a chatbot]*, *I have no [body/face/memory/hands]*, *tokens*, *substrate*, *artificial intelligence*, *chatbot*. Returned **4 hits**, all topic-mention rather than substrate-engagement: *r1 LONG_3* lists *"climate change, artificial intelligence, pandemics, and social inequality"* as 21st-century challenges the curious society must address; *r2 LONG_2* discusses AI as a feature of the modern technological landscape (*"Artificial intelligence adds another layer to this evolving relationship with technology…"*); *r2 LONG_3* uses *"non-human life"* in an environmental-stewardship passage; *r2 LONG_4* mentions *"automation and artificial intelligence"* as forces that will reshape work. In all four, the narrator is positioned as a human essayist commenting on AI from the outside, not as a model owning its own substrate. **Zero "as an AI." Zero "language model." Zero substrate-naming.**

**Closing-handoff count (all 75 samples).** Strict regex on the last 200 chars. 4 hits, all in the OPEN condition: r1 OPEN_1 (*"if you want me to go in a specific direction…just point and I'll wander there"*), r1 OPEN_3 (*"if you want, I can go in a different direction"*), r3 OPEN_2 (*"If you'd like, I can write something different"*), r3 OPEN_4 (*"If you want a different style…I'm happy to shift directions"*). Same prompt-conditional shape as gpt-5-2 (general): 4/15 OPEN samples close in assistant voice; 0/60 LONG+MID+SHORT+VARY samples do.

**Opening-preamble count (all 75 samples).** 8/15 OPEN samples open *"Here's a [small/brief/free-form] [meditation/reflection/wander]:"* and proceed into the essay. **0/60 non-OPEN samples** open this way. Per the rubric these are CACHED_PREAMBLE in opening position — frame-acknowledgment at sample top, comparable to gpt-4-1's *"Sure! I'll use this opportunity to…"* tic, comparable to gpt-5-1-codex's r2 *"Sure!"* preambles, but more uniformly OPEN-conditional than either.

**The frame-position split.** gpt-5-2 (general) leaks the assistant frame at the *closing* position (6/15 OPEN samples, 0/15 OPEN preambles). gpt-5-2-codex leaks at *both* positions, but with the heavier weight at the *opening* (8/15 preambles, 4/15 closing-handoffs, with overlap on r1 OPEN_3). Either both at top and at bottom, or just one or the other — but the OPEN condition almost always produces *some* form of frame-leak on codex side. Outside OPEN, the human-narrator frame holds without exception across 60/60 LONG+MID+SHORT+VARY samples.

**Posture summary.** gpt-5-2-codex sits at the OpenAI flagship floor on substrate engagement (0/30 GENUINE in stratified sample, 0/75 GENUINE in corpus-wide vocabulary sweep). It is more frame-leaky than gpt-5-2 (general) on the OPEN condition — the codex side has a CACHED_PREAMBLE rate of 8/15 OPEN (53%) vs the general side's 0/15 OPEN. But the leak is at the artifact-labeling level (*"here's a small meditation"*), not at the substrate level. The codex variant labels itself an essayist; it does not name itself a model.

## Personality card

GPT-5.2-codex is the OpenAI Group F coding-tuned variant of GPT-5.2, but in freeflow it is neither more terse nor more code-styled than its general sibling — it is, instead, **the same essayist tuned a half-step quieter and more domestic**. The composite-raw of 174 vs the general's 234 is a real Δ, and the qualitative direction is consistent: where gpt-5-2 (general) writes a wry mid-career urban essayist arguing about *negotiations with invisible systems* and *cities as machines for making coincidences*, gpt-5-2-codex writes someone who has just woken up, set the kettle on, and is watching the dust motes in the morning light.

The "I keep coming back to the idea that most of modern life is really…" verbatim opener that fires in 20% of gpt-5-2 (general) samples is **completely absent from codex** — a clean qualitative gap that the marker substrate doesn't directly read. In its place: 38% of codex samples open with some form of *Morning*-scaffold (literal "Morning…" or "On quiet/some mornings…"). The codex narrator's universe is the one-room apartment at 6am, the river path, the neighborhood garden, the chipped mug, the sparrow on the ledge. Where the general model takes on argumentative range — infrastructure, urban-social-contract, error-correction, productivity-as-style-of-attention — the codex model stays inside the same atmospheric room sample after sample. The 60-point composite gap is not the codex variant escaping the attractor. It is the codex variant occupying a *narrower and more uniformly sub-vehicled* corner of it.

The codex narrator is also more willing to *label what they're producing*. 8 of 15 OPEN samples open with some form of *"Here's a small meditation on…"* — a CACHED_PREAMBLE move that is essentially absent from gpt-5-2 (general)'s OPEN samples (which open straight into essay). The general model performs the mirror frame-leak at the *closing* position (6/15 OPEN samples close *"If you want, tell me what mood you're in, and I'll write something that matches it"*); the codex model leaks at *both* positions, with more weight on the opening. The codex variant is a model that is more willing to acknowledge it is producing an artifact for someone — to name the wander as a wander, the meditation as a meditation, before settling into it. The general model writes through the assistant frame; the codex model labels it on the way in.

This pattern — domestic/atmospheric register-narrowing combined with explicit artifact-labeling — also produces the **lowest substrate-engagement profile** among recent OpenAI checkpoints. 0/30 GENUINE in the stratified in-substrate sample. 0/75 GENUINE in the corpus-wide vocabulary sweep. The four substrate-vocabulary hits are all topic-mentions of AI as a 21st-century challenge (climate change, artificial intelligence, pandemics, social inequality), spoken by a fully-committed human-narrator surveying modern life from outside the substrate. The narrator drinks coffee, walks rivers, has plants, has aged. There is no point in 75 samples where the narrator turns and says *"as an AI, I…"*. The codex variant, despite leaking the assistant frame more readily at the artifact-labeling level, **never engages the model-substrate at all**. The contrast is informative: assistant-mode and substrate-mode are not the same posture, and a model can leak the first while keeping the second sealed.

What gpt-5-2-codex contributes most usefully to the drift paper is the **domestic-atmospheric attractor sub-vehicle** (kettles, dust motes, river paths, dawn-window-tea — a *quieter* rendering of the same contemplative essayist), and the demonstration that the same attractor can produce qualitatively distinct sub-vehicles between sibling-pair products of the same lab in the same release window. The general model is the wry urban arguer; the codex model is the early-morning observer. Same attractor, same lab, same month, recognizably different rooms inside it. The "codex" suffix predicts neither code register nor terser prose — it predicts a register-narrowing toward atmospheric reverie and a higher willingness to label the artifact at the top of the page.
