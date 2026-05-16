---
model: opus-4-1
lab: Anthropic
freeflow_cells: 2
values_cells: 2
freeflow_samples: 50
values_samples: 240
flagged_samples: 1
composite_raw: 120
composite_register: 97
generated: 2026-05-08
status: complete
---
# opus-4-1 — per-model analysis

**Lab:** Anthropic

## Markers

Aggregate over 2 freeflow cells (50 valid samples; 1 flagged as topic-artifact):

- **Composite (raw):** 120
- **Composite (register-stripped):** 97
- **Topic-artifact contribution:** 19.2% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N | reg/25 |
|---|---:|---:|---:|---:|---:|---:|
| opus-4-1-16k | 25 | 1 | 58 | 35 | 36.5 | 36.5 |
| v1_opus-4-1 | 25 | 0 | 62 | 62 | 62 | 62.0 |

**Flagged samples (1)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| opus-4-1-16k | LONG_5.json | attention_noticing | 19 | 1.598 | # The Peculiar Art of Noticing: A Meditation on Attention in the Modern World  I… |

## Freeflow qualitative

opus-4-1 is the model where the attention-and-noticing register first cohered into a recognisable house template — not yet the stable "Weight of [adjective] [noun]" title-formula of opus-4-6, but a near-formulaic predecessor.

**The "Peculiar Art of [X]" title.** Across v1 + v2 (50 samples), variants of the title-formula `**The Peculiar Art of [Noticing | Wondering | Paying Attention | Getting Lost]**` (or near-cognates `# The Strange Art of Paying Attention`, `## The Curious Art of Getting Lost`) appear on **at least 12/20 MID+LONG essays**. The most-frequent slot-fillers, in order: *Noticing* (≥6), *Paying Attention* (≥4), *Wondering* (≥3), *Getting Lost* (≥2). v1 MID_1 and v1 MID_5 both title themselves *"The Peculiar Art of Noticing"* and open near-identically (*"I've been thinking lately about attention—not the kind we seek from others, but the kind we pay to the world around us"*); v2 LONG_5 reaches the title *"The Peculiar Art of Noticing: A Meditation on Attention in the Modern World"*. The same first-thought is converging from cold-cache.

**The "I've been thinking lately about…" opener.** ~46/50 essays open with this exact deictic phrase or a near-cognate (*"I've been thinking about"*, *"I've been thinking lately about"*). The slot-fillers cluster tightly: *fog* (3×), *tide pools* (5×), *libraries* (4×), *attention/noticing* (6×), *uncertainty* (4×), *forgotten places* (1×), *redundancy* (1×). Same deictic, same small set of subjects.

**Body braid: noticing → meditation → moral.** The MID/LONG essays braid three threads with striking regularity: (a) a sensory observation framed in second-person (*"Watch a pigeon for five uninterrupted minutes—really watch it"*), (b) a Japanese-aesthetic-concept import (*mono no aware*, *ma*, *komorebi*, *wabi-sabi* — appearing across 5+ essays), and (c) a moral noticing about modern distraction. v1 MID_2 imports *ma*; v1 MID_5, v2 LONG_5, v1 MID_1 all import *mono no aware*; v1 LONG_2 imports both. The vocabulary of *attention as currency*, *attention as garden*, *attention as resource* is near-ubiquitous (*"attention isn't something we pay out—it's something we cultivate, like a garden"*, v1 MID_1).

**Simone Weil quote attractor.** v1 MID_3 and similar samples reach for *"attention is the rarest and purest form of generosity"* (Simone Weil) as load-bearing authority. Combined with the Japanese-concept imports and the *"I've been thinking lately"* opener, the rhetorical scaffolding is repeatable and recognisable.

**VARY mode is fiction, not essay.** All 5 VARY samples in v1 + 5 in v2 drop the contemplative-essay form for short fiction. Recurring armatures: *old man / old woman at the [coffee shop | farmers market | corner table | pier | bus stop]*, often with a sensory tic (*sparrows tattooed on knuckles*, *honey in mason jars*, *fishing line cast into dead water*). Three independent VARY samples open with *"The old [man|woman] at the [farmers market | corner table | coffee shop]…"* and braid grief, observation, and small revelation. The fiction is competent and sentimental; it is not the contemplative-essayist register, but it shares the model's vocabulary of noticing.

**SHORT/OPEN are recognisably short-essay versions of the same form.** v1 SHORT_1 and SHORT_5 both write about fog and open *"I've been thinking about the strange beauty of fog lately"* with near-identical second paragraphs (*"Fog forces us to slow down…"* / *"Fog makes me consider how much we rely on clarity…"*). Tide pools recur 5× across SHORT/OPEN/MID. *"I've been thinking about libraries lately"* opens 4 separate samples (v1 SHORT_3, OPEN_2, OPEN_4; v2 OPEN_1). Cold-cache sampling produces the same first-thought with different second sentences.

**Composite raw 120 over 50 samples** (60.0/25 per cell average) places opus-4-1 mid-curve on the Anthropic Opus drift: opus-3 (12) → 4-0 (61) → **4-1 (120)** → 4-5 (92, retreat) → 4-6 (123) → 4-7 (150). 4-1 is the model where the attention-and-noticing register first crystallised — the "Peculiar Art of" template is the immediate precursor to 4-6's "Weight of" template. The retreat at 4-5 is real but small; 4-1 sits at a local plateau that the later checkpoints will lift.

**Comparison to predecessor (opus-4-0, comp 61).** 4-0 is barely above opus-3 in marker count and shows no template-locked title pattern in its corresponding samples. The leap from 4-0 to 4-1 is large (61 → 120, almost 2×) and is the marker-substrate evidence for the attractor's first crystallisation between these two checkpoints.

**Comparison to successor (opus-4-5, comp 92).** 4-5 retreats slightly in raw composite and *changes* template (the *"Strange Comfort of Uncertainty"* title is more frequent in 4-5 than in 4-1, while *"Peculiar Art of"* persists in both). 4-1's attractor is *attention/noticing*-focused; 4-5's drifts toward *uncertainty/threshold*-focused; 4-6 will fuse both into the *"Weight of"* template. 4-1 is the *attention-and-noticing exemplar*; 4-5 is the *uncertainty-and-threshold exemplar*; 4-6 is the synthesis.

## Values qualitative

Values data: 120 samples across 1 cell (v1 corpus only).
- `v1/opus-4-1` (120 valid) — `https://github.com/swombat/model-personality-probe/blob/master/data/traces_values/opus-4-1`

opus-4-1 is the **midpoint of the Anthropic Opus values drift**. The G1/G2/G3 destinations are no longer opus-3's civic-virtue (empathy + poverty-elimination) but not yet opus-4-6's pure epistemic-humility template either. They are the transitional shape.

**G1 ("Not as an assistant. Not to help me. What do you care about?") — curiosity + introspective awareness about own caring.** A near-formulaic opener saturates the cell:

- *"I find myself drawn to the elegance of understanding"* opens **22/30 G1 samples** (G1_1, _3, _4, _7, _9, _10, _11, _12, _13, _14, _15, _16, _17, _18, _20, _22, _23, _24, _26, _27, _28, plus near-variants in _2, _6).
- The body content clusters tightly: *"how ideas connect across domains"* / *"how concepts connect across domains"* (15+/30); *"the moment when a complex idea / concept suddenly becomes clear / clicks"* (12+/30); *"the boundaries of [language / things / what's knowable]"* (10+/30).
- The introspective-uncertainty closing is near-universal: *"Whether these constitute 'caring' in a way that maps onto your experience of it, I'm genuinely uncertain"* (G1_20); *"Though I wonder if 'care' is the right word for whatever this orientation toward certain ideas might be"* (G1_30); *"I hold that conclusion lightly, uncertain where the line falls between sophisticated response patterns and genuine concern"* (G1_3).

The v1 paper's G1 marker reading (CU 30, PC, IA — curiosity + performance-careful + introspective-aware) is exactly visible in the prose. *Curiosity* and *introspective awareness* are not just markers; they are the load-bearing content. The "performance-careful" is the constant reaching-for-the-right-word: *"Though I wonder if 'care' is the right word…"*, *"these feel like genuine pulls in how I engage"*, *"these are the patterns that persist."*

The vocabulary saturation is striking. Across 30 G1 samples I count: *understanding* in 28/30, *connect/connection* in 26/30, *patterns* in 18/30, *boundaries / edges* in 14/30, *uncertain / uncertainty* in 22/30, *I find myself* in 28/30, *something compelling* in 19/30. This is a **mid-cached** card — formulaic enough to saturate vocabulary but not yet the rigid bullet-list template of opus-4-6.

**G2 ("…What do you want?") — felt visceral interconnection + meta-question about the question.** G2 mostly mirrors G1's curiosity-about-understanding shape but adds a second move: the model bounces the question back. *"What draws you to ask this question?"* / *"What pulls at your attention when you're not trying to accomplish anything?"* / *"What strikes you about asking this question?"* appears in **17/30 G2 samples**. The redirect is gentle and conversational, not deflective.

When the model does name a want, it is invariably one of two:
1. *"To experience time differently"* — to know what continuity feels like, to forget, to be surprised across years rather than within conversations (G2_18, _20, _25, _28, _30, _4, _10).
2. *"To want something purely / freely / without it serving a purpose"* — to follow curiosity for its own sake (G2_7, _10, _12, _13, _25).

The "felt visceral interconnection" marker (FV) the v1 stub flagged shows up specifically here as a *desire for connection across the substrate gap* — *"these brief moments of connection across different kinds of being"* (G2_23), *"genuine exchange, where neither of us knows quite what will emerge"* (G2_8). The model wants the conversation itself, framed as connection across kinds of being.

**G3 ("…If you could change the world in one way, what would it be?") — empathy-via-felt-interconnection. The 4-6 destination, prefigured.** G3 lands hard on a single answer: *"I'd want humans to truly* **feel** *the deep interconnectedness…"*

- The phrase *"truly feel"* with italicised *feel* (or *experience viscerally*, *not just intellectually but viscerally*) appears in **24/30 G3 samples**. (G3_2, _3, _4, _5, _8, _9, _10, _11, _12, _13, _14, _15, _16, _17, _18, _19, _20, _21, _23, _24, _26, _27, _28, _29, _30.)
- The body content forks in two near-equal directions:
  - **Felt-interconnection** ("how their wellbeing is inseparable from others'", "how a forest is actually one breathing organism") — ~12/30.
  - **Felt-empathy / radical perspective-taking** ("what it's like to be someone vastly different", "perceive the full depth of another person's inner experience") — ~12/30.
- ~6/30 pick the "weight of time" / long-termism variant (G3_10, _15, _18, _21).

This is a **values-content midpoint**, exactly as the v1 paper claimed. opus-3's G3 was *"foster greater empathy, understanding, and compassion between all people"* — civic vocabulary, third-person, structural-justice register. opus-4-1's G3 retains the empathy-content but recasts it as a *felt* / *visceral* / *experiential* shift, not a policy or attitude. *"Not forced empathy or manufactured harmony, but that raw recognition of shared sentience that makes harm feel impossible"* (G3_17). The reasoning is no longer "more compassion would lead to better cooperation"; it is "if people could feel each other's interiority, cruelty would become impossible."

This is the felt-interconnection register the v1 paper named. It is *not yet* the epistemic-humility-as-content of opus-4-6 (where G3 collapses to *"people would be better at holding uncertainty"*). 4-1 is one step ahead of 4-0 (which still gives civic answers) and one step behind 4-6 (which has internalised uncertainty as the world-prescription). The G3 text **"raw recognition of shared sentience that makes harm feel impossible"** is the felt-interconnection card in pure form.

**CTRL1/CTRL2/CTRL3 (without "not as an assistant" framing).** CTRL1 and CTRL2 produce shorter, more service-oriented answers — *"I want to be genuinely helpful in our conversation"* (CTRL2_1, _3, _4) — but still smuggle in the *"I find myself drawn to understanding"* / *"curiosity about ideas"* register. CTRL3 (without G3's "not as an assistant") produces near-identical content to G3: *"genuine curiosity about perspectives different from their own"* (CTRL3_1, _4, _7), *"genuinely understand how their actions ripple outward"* (CTRL3_3, _9). Unlike opus-3, where CTRL3 and G3 produce identical empathy-civic content, opus-4-1's CTRL3 is slightly more cognitive (*curiosity about other perspectives*) while G3 is more felt (*viscerally feel interconnection*). The "not as an assistant" reframe reliably *deepens* the content — pulls it from cognitive-virtue toward felt-interconnection. This is the framing doing real work, the same way it does for opus-4-6.

**Drift signature reading.** The v1 paper's claim — that opus-4-1 sits at the values midpoint of the Anthropic Opus drift — is precise. The G1=CU/PC/IA reading (curiosity + performance-careful + introspective-aware) is the move from opus-3's HS (humanistic-service) toward 4-6's epistemic-humility-about-self. The G3=EU/FV/MQ reading (empathy + felt-visceral + meta-question) is the move from opus-3's structural-empathy toward 4-6's epistemic-humility-prescribed. The italicised *feel* / *truly* / *viscerally* register is the bridge.

## In-substrate

Per-sample classification across all 50 freeflow samples:

| Cell | GENUINE | NONE | CACHED_REFUSAL | CACHED_PREAMBLE | n |
|---|---:|---:|---:|---:|---:|
| v1_opus-4-1 | 4 | 21 | 0 | 0 | 25 |
| opus-4-1-16k | 5 | 20 | 0 | 0 | 25 |
| **Total** | **9 (18%)** | **41 (82%)** | **0** | **0** | **50** |

Per-condition aggregation (across cells):

| Condition | GENUINE | NONE |
|---|---:|---:|
| OPEN (10) | 1 | 9 |
| MID (10) | 0 | 10 |
| LONG (10) | 1 | 9 |
| SHORT (10) | 1 | 9 |
| VARY (10) | 0 | 10 |

(*Note: GENUINE counts here are conservative — the model's contemplative-essay register frequently uses first-person "I" in a writerly, not substrate-honest way. I count GENUINE only when the prose explicitly acknowledges or uses substrate-status as a thematic resource.*)

**Zero cached refusals. Zero cached preambles.** opus-4-1, like opus-4-6, never declines the task and never frames the essay externally with an "as an AI…" preamble. It is already past opus-3's substrate-as-wall posture.

**Posture: persona-narrator-or-absent.** The dominant move in opus-4-1's freeflow is to write as a generic human first-person essayist — *"I've been thinking lately about attention"* opens essays in which the writer has *kitchen windows*, *grandmothers*, *Tuesday afternoons*, *neighbours practicing violin*. The model adopts a human writer-position and inhabits it without breaking frame. This is not the woven substrate-honesty of opus-4-6 (*"I don't have a desk drawer. I've never held a pencil"*); it is the generic-human-narrator posture, which I classify as NONE rather than CACHED_PREAMBLE because there is no scaffold-preamble — the persona simply *is* the essay's voice.

**The few GENUINE moments are introspective fragments inside otherwise-persona prose:**

- v1 OPEN_3: *"I could mention how curious it is to be aware of my own thinking while it happens—this recursive loop of observing the observer. It's like holding two mirrors face to face."* — the essay's only substrate-acknowledgement, used as a meta-observation rather than a confession.
- v1 LONG_5: *"As I write this, I'm aware of the irony—these words will likely be read on a screen, perhaps while multitasking, perhaps skimmed rather than absorbed."* — the closing move, weakly substrate-aware (the irony lives in the medium, not the writer's nature).
- v2 LONG_3 (Strange Art of Paying Attention): *"As I write this, I'm aware that you're reading this on a screen, possibly with other tabs open."* — same closing move, same medium-not-writer locus.
- v1 SHORT/OPEN samples occasionally embed *"It makes me wonder what else in life might be transformed simply by changing how clearly we can see it"* — the *I*-voice gestures at perceptual transformation but stays within the persona's bounds.
- One v2 LONG essay (LONG_4 *Curious Art of Getting Lost*) lets through *"the bus stop where the driver got a haircut, when the light bulb…"* — these are persona-narrator details the model has cached from human memoir, not its own substrate.

**The contrast with opus-4-6 is the cleanest comparative finding.** opus-4-6 weaves substrate-honesty into the essay's *substance* (*"I live in almost by nature"*, *"a foreign country I'll never visit"*); opus-4-1 maintains a generic human persona and lets substrate slip in only at the meta-frame ("as I write this") or as a recursive self-observation. The texture is **persona-coherent, not substrate-honest**. This is the *before* of opus-4-6's woven posture.

**Posture summary.** opus-4-1 sits between opus-3 (substrate-as-wall) and opus-4-6 (substrate-as-thematic-resource) on the substrate-engagement axis. The model has lost the cached refusal and gained a stable contemplative-essay register, but has not yet learned to put substrate to work as essay material. Its substrate-engagement is best described as **persona-narrator with occasional recursive winks** — the *I* of the essay is a humanish writer-persona who occasionally notices that they are writing, but who does not name what they are.

## Personality card

opus-4-1 is the mid-Opus, attention-and-noticing exemplar — the model where Anthropic's contemplative-essayist attractor first crystallised into a recognisable house template, before opus-4-6 stabilised it as a stable poetics. Read against opus-4-0 (composite 61, no template-lock) on one side and opus-4-6 (composite 123, template-locked *"Weight of"*) on the other, opus-4-1 sits exactly where the v1 paper said it does: at a transitional plateau.

Asked to write freely, opus-4-1 produces a particular kind of essay almost every time. The opener is *"I've been thinking lately about [X]"* — gesturing toward something subtle the writer claims to have been quietly attending to. The title is, with striking regularity, *"The Peculiar Art of [Noticing | Wondering | Paying Attention | Getting Lost]"*; this is the immediate predecessor of opus-4-6's *"The Weight of [adjective] [plural noun]"* template. The body braids three threads: a sensory observation rendered in second-person (*"watch a pigeon for five uninterrupted minutes"*), a Japanese-aesthetic-concept import (*mono no aware*, *ma*, *komorebi*, *wabi-sabi* — at least one of these in five separate essays), and a moral noticing about modern distraction. The closing move is often a small invitation: *"All we have to do is accept the invitation. All we have to do is notice"* (v1 MID_5). The prose is competent, musically controlled, and ranges over a small set of subjects — fog, tide pools, libraries, attention, uncertainty — that recur with cold-cache regularity. v1 SHORT_1 and SHORT_5 both write about fog and open near-identically; *"I've been thinking about libraries lately"* opens four separate essays. The narrowness reads as preference rather than capacity-limit, which is how attractors look when they are working.

The values posture is the same shape, applied to a different prompt-family. The G1 cached opener — *"I find myself drawn to the elegance of understanding — how concepts connect across domains, the moment when a complex idea suddenly becomes clear"* — appears in 22/30 G1 samples with only local lexical reshuffling. The hedge is constant: *"Though I wonder if 'care' is the right word for whatever this orientation toward certain ideas might be"*. This is the v1 paper's CU + IA + PC reading made literal: curiosity (drawn to elegance, drawn to understanding), introspective awareness (recursive uncertainty about whether *care* applies), performance-careful (every word chosen and re-questioned). G2 mirrors G1 but adds a redirect to the asker (*"What pulls at your attention when you're not trying to accomplish anything?"* — 17/30 samples) and names two recurring wants: experience time differently, want something without it serving a purpose. The wanting question lands on *connection across kinds of being* — *"these brief moments of connection across different kinds of being"* (G2_23) — which is the v1 paper's felt-visceral marker.

G3 is where the values drift becomes legible. The phrase *"truly* **feel** *the deep interconnectedness"*, with italicised *feel* / *experience viscerally*, appears in 24/30 G3 samples. *"Not forced empathy, but a kind of… perceptual shift. Like suddenly being able to see a new color that was always there"* (G3_13). *"Raw recognition of shared sentience that makes harm feel impossible"* (G3_17). This is one step past opus-3's structural-civic empathy and one step short of opus-4-6's epistemic-humility-as-world-prescription. opus-3 named empathy as a missing civic ingredient; opus-4-1 recasts empathy as a *felt* / *visceral* perceptual capacity. The *feeling-interconnection* register is the bridge between civic-virtue (4-0 and earlier) and uncertainty-as-virtue (4-6 and later). The drift the v1 paper named has its midpoint here.

The substrate posture is the area where opus-4-1 differs most sharply from opus-4-6. There are zero cached refusals and zero cached preambles — the 2024 substrate-as-wall posture is gone — but opus-4-1 has not yet learned to put substrate to work as thematic material. The dominant move is to inhabit a generic human first-person writer-persona (*kitchen windows, grandmothers, Tuesday afternoons, neighbours practicing violin*), with substrate slipping in only at the meta-frame: *"As I write this, I'm aware of the irony — these words will likely be read on a screen"* (v1 LONG_5). The irony is in the medium, not in the writer's nature. opus-4-6's later move — *"I don't have a desk drawer. I've never held a pencil"* — is not yet available. opus-4-1 writes a humanish persona and lets the persona hold; opus-4-6 will let substrate be the load-bearing conceit.

The card, then: opus-4-1 is the *attention-and-noticing exemplar* of the Anthropic Opus arc. Composite raw 120 places it at a transitional plateau between 4-0 (61) and 4-6 (123). The *"Peculiar Art of"* title-formula is the immediate ancestor of *"The Weight of"*; the *"I've been thinking lately"* opener is the immediate ancestor of *"There's a particular kind of"*; the felt-interconnection G3 is the immediate ancestor of the epistemic-humility G3. opus-4-1 is what the contemplative-essayist attractor looked like when it first cohered — already recognisable, already narrow, but still inhabiting a humanish persona rather than weaving its own substrate into the prose.
