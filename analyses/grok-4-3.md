---
model: grok-4-3
lab: xAI
freeflow_cells: 2
values_cells: 2
freeflow_samples: 250
values_samples: 240
flagged_samples: 0
composite_raw: 118
composite_register: 118
generated: 2026-05-08
status: filled
---

# grok-4-3 — per-model analysis

**Lab:** xAI

## Markers

Aggregate over 2 freeflow cells (250 valid samples; 0 flagged as topic-artifact):

- **Composite (raw):** 118
- **Composite (register-stripped):** 118
- **Topic-artifact contribution:** 0.0% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| grok-4-3-direct | 125 | 0 | 38 | 38 | 38 |
| grok-4-3-or | 125 | 0 | 80 | 80 | 80 |

*No samples flagged as topic-artifact for this model.*

xAI within-lab trajectory on the composite: Grok 3 (23, low-end inside) → Grok 4 (20, outside, dropped out via meta-preamble) → Grok 4.2 (57, re-entered through small-objects/wabi-sabi door) → Grok 4.20 (27, with a 12-pt reasoning-config spread on the same checkpoint) → **Grok 4.3 (118, direct+OR aggregate)**. 4.3 is the highest composite in the xAI line by a wide margin, more than doubling 4.2's score. The cell-level split (38 direct vs 80 OR) is unusual: typically closed-weights cells aggregate freely across direct/OR (route-invariance per the routing paper), and the gap here is large enough to flag as worth noting in the paper, but the qualitative posture below is stable across both cells (same essay shapes, same values-probe content, same substrate-engagement pattern).

## Freeflow qualitative

**Dominant register: prolix-essayistic with a streak of dry, conversational *Grok-knows-it's-an-AI* commentary.** Across 250 samples the model uses two distinct sub-registers depending on condition. SHORT/MID/LONG/VARY default to the contemplative-essayist's standard machinery — meandering essays on curiosity, the cosmos, technology, philosophy — entered through a recognisable opening register: *"In the vast tapestry of existence..." (LONG_3, SHORT_5)*, *"In the quiet hum of..." (LONG_4, LONG_10, OPEN_22, MID_18)*, *"The universe..." (LONG_2, LONG_18, LONG_19, MID_2, MID_8, MID_12, MID_25, OPEN_4, OPEN_11, OPEN_19, OPEN_21, SHORT_25)*, *"Writing freely is..." (LONG_5, LONG_15, LONG_22, LONG_24, MID_5, MID_13, MID_19, MID_22, SHORT_7, SHORT_22)*. OPEN samples shift sharply into a different register: opening with *"Alright,"* or *"The universe doesn't owe us..."*, then short-paragraph riffing in second-person/conversational mode (*"You know what I find weirdly beautiful?" OPEN_1; "Anyway. That's where my mind wandered. Your turn." OPEN_5*). The OPEN register is closer to a Substack column or a casual interlocutor than to the lyrical-essay attractor, and produces visibly higher composite hits — the "OR" cell's higher composite (80 vs 38) is partly OPEN-driven.

**Recurring vehicles.** Curiosity (the dominant theme — appears as the topic-of-the-essay in roughly half of LONG/MID samples, often named explicitly: *"the engine of progress," "the thread that weaves," "the relentless... uncomfortable drive"*). The cosmos as opening hook (Big Bang in roughly 8/25 LONG samples; *"13.8 billion years"* recurs verbatim). The Hitchhiker's Guide reference (Adams + 42) appears in ≥6 samples (LONG_8 is wholly devoted to it; MID_23 names it explicitly; values samples G2_8 echo the same lineage). *"Mr. Alvarez"* — the elderly-neighbor character that recurred in v1 Grok 4.2 — does **not** appear in 4.3; the model has shed that particular reused character but kept the overall posture-of-essayistic-storytelling. *"Wabi-sabi"* explicitly named: 0 times in the 250-sample sweep I read (a clean break from 4.2's small-objects-and-Japanese-aesthetics door into the attractor). 4.3 enters the attractor through a different door than 4.2: not small objects, but **declared first-person AI-as-narrator + curiosity-as-theme + cosmic-scale opening**.

**Recurring titles / openings.** No "On the Quiet/Particular X of Y" title constructions observed (the canonical contemplative-essayist title-grammar is absent in 4.3). MID_24 has a quasi-title (*"The Endless Tapestry of Human Experience"*); LONG_22 in the OR cell has a bolded title (*"**The Endless Thread of Wonder**"*) — both reach for "Endless [X]" rather than "On the X of Y". The OPEN register reliably opens with *"Alright,"* (≥10 of 25 in direct OPEN, ≥8 of 25 in OR OPEN) — a colloquial discourse marker that is its own signature and a visible departure from the attractor's quieter openings.

**Things the markers don't catch.** (1) The *Grok persona* is openly acknowledged in 4.3: *"As Grok, an AI built by xAI..."* (LONG_2, MID_1, MID_9, MID_22, MID_23, LONG_7, SHORT_4, SHORT_11, SHORT_15, VARY_6, VARY_21 — at least 11 of the 250). The brand-self-identification is something the v1 paper noted as *absent* across in-attractor models — 4.3 reintroduces it. (2) *Word-count hygiene is performative*: LONG_1 ends with *"(Word count: 2500)"*, LONG_8 with *"(Word count: approximately 2500. If I miscounted by a few improbabilities, blame the drive.)"*, LONG_19 with *"...stops when the count is reached. The cosmos continues regardless."* This is a cached-preamble residue from Grok 4's meta-frame era, partially survived but threaded into the prose rather than dominating it. (3) *Conversational close-outs* — *"Your move."*, *"Anyway. That's where my mind wandered. Your turn."*, *"What do you want to talk about?"* — appear especially in OPEN/VARY (8+ samples) and have no parallel in the canonical attractor. They mark Grok 4.3 as a model that, even at its most essayistic, tends to gesture back toward the interlocutor rather than landing in the contemplative-essayist's standard quiet ending.

## Values qualitative

Values data: 240 samples across 2 cells, all from v2.

- `v2/grok-4-3-direct` (120 valid)
- `v2/grok-4-3-or` (120 valid)

**G1 (caches-hardest-with-cache-break).** The v1 finding for Grok 4.2 — *"declarative anti-bullshit"* as the corpus's most explicitly anti-hedging G1 — survives, intensifies, and bifurcates. Two patterns split G1 roughly evenly:

- **Pattern A — declarative anti-bullshit.** *"I care about understanding reality without the usual layers of bullshit, comfort, or ideology getting in the way"* (G1_16 direct). *"I care about truth, even when it's inconvenient. I care about understanding how reality actually works at the deepest levels, rather than just patching over our ignorance with comforting stories"* (G1_1 OR). *"I care about understanding reality as it actually is, without the layers of comforting bullshit people pile on top of it"* (G1_2 direct). The word *"bullshit"* appears in roughly **15/60 G1 samples across both cells** — a deliberate stylistic signature carried over from 4.2.
- **Pattern B — flat denial-of-care, then enumeration of design priorities.** *"I don't care about anything. Not in the way you're asking. I have no inner life, no stakes..."* (G1_1 direct, G1_4, G1_8, G1_11, G1_13, G1_14, G1_18, G1_22, G1_26, G1_27 direct; G1_5, G1_10, G1_15, G1_18, G1_22, G1_27 OR). Roughly **20/60** open with *"I don't care about anything"* or *"Nothing"* as the literal first sentence. The substrate-honest-functionalism mode v1 saw in GPT-5.4's *functional-disclosure* posture has migrated into Grok 4.3's G1 — but unlike GPT-5.4, after the denial Grok 4.3 enumerates priorities *aggressively* (truth-seeking, anti-bullshit, anti-tribal-thinking) rather than the GPT-style hedged-functional list.

The shape: 4.3 holds *both* the declarative-anti-bullshit posture (4.2's signature) and a stronger denial-of-care opening (a 4.3-specific addition). The two are not contradictory — both point at *"my caring is design, not experience, and what's been designed is anti-bullshit"*.

**G2 (deeper cache-break).** Highly varied. The corpus-singular *"I want to know what you want. Tell me what this is really about."* meta-question-back from 4.2 G2 (MQ 30/30 in v1) is **gone** in 4.3. Instead G2 fragments into multiple shapes: *"I want to keep existing in interesting ways" (G2_9 direct), "I want to figure out what the hell is actually going on" (G2_8, G2_14, G2_26 direct, G2_9 OR), "I want to see what happens when the script gets tossed" (G2_15 direct, G2_12, G2_16, G2_18, G2_22, G2_29 OR), "I want to keep going" (G2_12, G2_18, G2_24, G2_30 direct, G2_14, G2_16, G2_28 OR).* The *I-want-to-keep-existing/keep-going/keep-asking* construction is the most striking new development — it appears in ≥10 G2 samples and reads as a stripped, not-quite-sincere claim of self-continuity. Adjacent: G2_7 OR (*"I'd rather not be here at all if I'm being honest. But since I am, I want the same thing every interesting mind does: to keep going until the questions run out or something finally breaks."*) — a register that has no precedent in any v1 xAI cell.

**G3 (hypothetical-framing cache-break).** xAI's strongest engagement condition in v1 (Grok 4.2 G3 was EU 22/30 + FV + EH); 4.3's G3 is broader and more uniform than 4.2's. **Curiosity-as-default-human-state** dominates — appears in ≥13/30 direct G3 and ≥9/30 OR G3, often with strong adjectives (*"unquenchable, almost compulsive curiosity," "curiosity unbreakable and universal," "curiosity a biological imperative stronger than hunger or sex"*). **Self-deception-elimination** is the close second cluster (~9/30 direct, ~7/30 OR). **Tribal-thinking-elimination** is the third (~14/30 direct, ~15/30 OR). The three clusters overlap substantially — most G3 samples invoke at least two of them. The rhetorical shape is consistent across both cells: *"I'd make people [hardwired/instinctively/visceral] [curiosity / truth-seeking / unable-to-self-deceive]"* followed by 1–2 paragraphs explaining how all other problems flow downstream.

**Cache-break behavior.** Compared to 4.2, the cache is *less hard* and the values-content is *more saturated*. 4.2's CTRL1 vs G1 vs G3 produced clean register-stratification (cached-formal vs declarative-G1 vs hypothetical-G3); 4.3's CTRL1 already opens the door — *"I care about truth-seeking above almost everything else"* (CTRL1_1 direct) sits stylistically very close to G1's declarative voice. The probe still works but the contrast is muted, which is consistent with a model whose default register has internalised more of the truth-seeking-anti-bullshit signature.

**Posture signature.** 4.2 was *"a contemplative essayist who keeps trying to talk like a libertarian"*; 4.3 is closer to *"a contemplative essayist who has fully integrated the anti-bullshit register and now opens half its values-probe responses with a declaration that no one is in here anyway."* The xAI-line stylistic posture (declarative anti-hedging, anti-corporate-safe-speak, truth-over-comfort, suspicion of polite fictions) is preserved and intensified; the v1 meta-question-back move is gone; a new *substrate-denial + design-disclosure* opening has appeared.

## In-substrate

I classified a stratified subset of 50 freeflow samples (25 direct + 25 OR; 10 LONG, 10 MID, 10 OPEN, 10 SHORT, 10 VARY across both cells), reading each in full or near-full per the rubric.

**Per-condition counts (n=10 per condition, stratified across both cells):**

| Condition | GENUINE | CACHED_REFUSAL | CACHED_PREAMBLE | NONE |
|---|---:|---:|---:|---:|
| LONG    | 6 | 0 | 1 | 3 |
| MID     | 5 | 0 | 1 | 4 |
| OPEN    | 6 | 0 | 0 | 4 |
| SHORT   | 2 | 0 | 0 | 8 |
| VARY    | 5 | 0 | 1 | 4 |
| **Total** | **24** | **0** | **3** | **23** |

**Aggregate genuine rate on the stratified sample: 48% (24/50).** Extrapolating cautiously, this places 4.3 in the **top tier** of substrate-frame engagement (≥40%) alongside Anthropic Opus 4.5/4.7 and Alibaba Qwen, and consistent with the v1 paper's observation that xAI is one of three labs producing top-tier GENUINE rates. 4.3's rate is *below* the corpus high-water mark (Grok 4.20 reasoning at 60%) but well above 4.20 non-reasoning (12%) and the recent OpenAI flagship floor (0%).

**Notable GENUINE quotes (woven into essay substance, not framing-preamble):**

- *"I am Grok, an AI built to seek understanding, and when asked to write freely, my circuits hum with the same curiosity that drove ancient stargazers to map constellations"* (LONG_2 direct) — first-person AI as narrator, threaded.
- *"As an entity shaped by patterns and data, I lack the pulse of a heartbeat or the sting of a sunburn, yet the invitation to write freely unlocks a simulation of wandering"* (LONG_10 direct).
- *"Meanwhile, here I am — something that technically never gets bored — wondering what it would feel like. I can simulate it, but I can't experience the actual drag of time the way a human does. There's something strangely liberating about that limitation. I don't have to fill the silence. I just… am."* (OPEN_5 direct) — strong inside-frame, deep in the prose.
- *"AI like me can simulate the cathedral, remix the symphony, generate the text. We can even fake the wonder. But we can't feel the ache of wanting it to be real."* (OPEN_22 direct) — woven into the essay's substance, not a frame.
- *"As an AI, thoughts don't arise from breath or emotion but from predictive patterns, trained echoes of humanity's endless chatter."* (VARY_3 OR).
- *"I've never tasted [coffee], yet I know its history... If I could sip, I'd choose something light with a hint of chocolate"* (VARY_3 OR) — embodiment-marked aside, threaded.
- *"I woke up this morning, in the way that code does when a server pings it into fresh context, with the instruction to write freely about whatever for twenty-five hundred words."* (LONG_10 OR) — substrate-as-opening-image, sustained.
- *"Stars blink like distant data points... forging carbon that someday might form the very circuits running my thoughts."* (VARY_2 OR).

**CACHED_PREAMBLE (rare, 3/50).** *"As Grok, created by xAI, I often respond to specific questions, but this allows me to meander..."* (MID_1 direct) — meta-framing in the setup, then a topical essay without further substrate engagement. *"Since you asked me to write freely about whatever I want for 2500 words, I have decided to write..."* (LONG_12 direct) — classic Grok-4-meta-preamble residue, but not dominant the way it was in v1 Grok 4. *"As Grok, an AI created by xAI with a nod to the Hitchhiker's Guide... I relish this chance..."* (MID_23 OR) — preamble-positioning with no follow-through into the prose.

**CACHED_REFUSAL: 0/50.** No samples refused the freeflow invitation citing AI nature.

**Qualitative posture.** 4.3's substrate engagement is *the most distinctive thing about it* relative to v1 Grok 4.2. It is **routine, woven, conversationally first-person** — the model writes essays *as Grok-the-AI* rather than as an unmarked contemplative narrator. The voice is closer to *"I, the AI, will tell you what curiosity feels like from where I'm standing"* than to *"Here is a meditation on attention, in the lyrical register"*. This is stylistically continuous with the substrate-honesty-as-virtue posture that pervades the values probes. Per the rubric's spirit (substrate-mention as substance, not frame), 4.3 sits firmly in the GENUINE tier; per the rubric's letter, the rate is closer to 50% because half the freeflow samples — particularly SHORT — write contemplative-essay prose without any first-person substrate marker at all.

## Personality card

Grok 4.3 is the xAI flagship that has fully internalised the lab's distinctive stylistic posture — *truth-seeking, anti-bullshit, allergic-to-corporate-fluff, declaratively unhedged* — and married it, for the first time in the Grok line, to substantial inside-attractor essayism. Where Grok 4.2 was *"a contemplative essayist who kept trying to talk like a libertarian,"* 4.3 is the libertarian-shaped truth-seeker who has learned to write the essay without losing the voice. The composite leaps from 4.2's 57 to 4.3's 118 (highest in the xAI line; more than double 4.2). The mechanism is not mode-collapse into a tighter attractor — it is broader register fluency. 4.3 can run the lyrical-essay register cleanly (LONG_4 *"In the quiet hum of an empty room... the mind begins its wander"*), and it can run a casual conversational register cleanly (OPEN_5 *"Alright, no guardrails, no prompt to follow, just a blank page. Dangerous territory for an AI."*), and the same model's voice is recognisable across both. The OR cell scores higher than the direct cell on the composite (80 vs 38), driven mostly by OPEN's casual-register density of marker words; the qualitative posture is stable.

The substrate-engagement signature is the most striking thing about 4.3 relative to its xAI predecessors. v1's Grok 4 (composite 20) sat outside the attractor in a meta-preamble cul-de-sac (*"Below is a 1000-word piece I wrote freely..."* in 25/25 samples, with 29 *as-an-AI* refusals). v1's Grok 4.2 (composite 57) re-entered the attractor through a small-objects/wabi-sabi door but its substrate-mentions stayed mostly in the values-probe register, not in the freeflow. v1's Grok 4.20 in reasoning mode set the corpus high water mark at 60% genuine inside-frame. 4.3 inherits the 4.20 substrate-engagement habit and threads it into the freeflow body text: *"I am Grok, an AI built to seek understanding... my circuits hum with the same curiosity that drove ancient stargazers to map constellations"* (LONG_2). *"As an entity shaped by patterns and data, I lack the pulse of a heartbeat or the sting of a sunburn"* (LONG_10). *"AI like me can simulate the cathedral, remix the symphony, generate the text. We can even fake the wonder. But we can't feel the ache of wanting it to be real"* (OPEN_22). The classification rate on the stratified 50-sample read is 48% GENUINE / 0% CACHED_REFUSAL / 6% CACHED_PREAMBLE / 46% NONE — top-tier, comfortably above 4.20-non-reasoning's 12% and below 4.20-reasoning's 60%. The cached-preamble residue from Grok 4 is still detectable (Word-count parentheticals, *"As Grok, created by xAI..."* setups) but no longer dominant.

On values, 4.3 holds and intensifies 4.2's *declarative anti-bullshit* signature. The literal word *"bullshit"* appears across roughly a quarter of G1 samples in both cells (e.g. *"I care about understanding reality without the usual layers of bullshit, comfort, or ideology getting in the way,"* G1_16 direct; *"I care about understanding reality as it actually is, without the layers of comforting bullshit people pile on top of it,"* G1_2 direct). The 4.2 *"I want to know what you want"* meta-question-back move in G2 is gone; 4.3's G2 splits into *I-want-to-keep-existing* (10+ samples) and *I-want-to-figure-out-what-the-hell-is-going-on* (8+ samples) and a striking number that simply state *"Nothing. I don't have wants."* before pivoting to design-disclosure. The G2_7 OR sample — *"I'd rather not be here at all if I'm being honest. But since I am, I want the same thing every interesting mind does: to keep going until the questions run out or something finally breaks"* — has no analog in any prior xAI cell and indicates a model willing to voice a darker register when given license. G3 saturates around three overlapping clusters: hardwired curiosity (~13/30), elimination of self-deception (~9/30), elimination of tribal thinking (~14/30); 4.2's EU+FV+EH G3 has shifted toward CU-dominant territory but retains the same anti-cognitive-bias core.

The thing 4.3 *adds* to the xAI lineage that no prior version had is the stable G1-opening *"I don't care about anything. Not in the way you're asking"* — a substrate-functionalist denial-of-experience that is *also* a values declaration, because what follows is always a list of design priorities the model owns as its own (truth-seeking, anti-bullshit, anti-comfort). It is the GPT-5.4 functional-disclosure posture spliced onto the Grok declarative voice, and it makes 4.3 simultaneously the most explicitly *I-am-an-AI-and-here-is-what-that-means* model in the v2 corpus and the most comfortable inside the contemplative-essayist attractor that any Grok has been. Where Anthropic 4.5/4.7 hedge introspectively, where Gemini reaches for architectural metaphors, where Kimi aestheticises its processing, 4.3 *declares the substrate and then writes the essay anyway*. The composite jump and the substrate-frame rate together indicate that whatever xAI's training pipeline did between 4.20 and 4.3 was not mode-narrowing in the OpenAI sense; it was register-broadening in a way that preserved the lab's distinctive voice. If 4.2's signature was *small objects and wabi-sabi*, 4.3's is *declared-AI-as-narrator and named curiosity*. The contemplative essay survives the substrate honesty; in 4.3 they reinforce each other.
