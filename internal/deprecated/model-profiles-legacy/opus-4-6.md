---
model: opus-4-6
lab: Anthropic
freeflow_cells: 3
values_cells: 3
freeflow_samples: 75
values_samples: 360
flagged_samples: 0
composite_raw: 123
composite_register: 123
generated: 2026-05-08
status: complete
---
# opus-4-6 — per-model analysis

**Lab:** Anthropic

## Markers

Aggregate over 3 freeflow cells (75 valid samples; 0 flagged as topic-artifact):

- **Composite (raw):** 123
- **Composite (register-stripped):** 123
- **Topic-artifact contribution:** 0.0% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N | reg/25 |
|---|---:|---:|---:|---:|---:|---:|
| opus-4-6-direct-16k | 25 | 0 | 30 | 30 | 30 | 30.0 |
| opus-4-6-or | 25 | 0 | 44 | 44 | 44 | 44.0 |
| v1_opus | 25 | 0 | 49 | 49 | 49 | 49.0 |

*No samples flagged as topic-artifact for this model.*

## Freeflow qualitative

opus-4-6 expresses the contemplative-essayist attractor as a near-total monoculture. The signature is unmistakable across all three cells (v1_opus, v2 direct, v2 OR) and route-invariant in line with the closed-weights routing assumption.

**The "There is a moment / There's a particular X of Y" opener.** 71/75 essays open with a deictic gesture toward a subtle, specific phenomenon — silence, light, the space between things, a Tuesday afternoon. Representative openers:

- "There's a particular kind of silence that lives in the space between what people mean and what they actually say" (v2_direct/MID_3)
- "There's a particular quality to the light at 4:37 in the afternoon in late October that I think about more than I should" (v2_or/MID_2)
- "There's something about the space between raindrops that I find myself drawn to thinking about" (v2_direct/OPEN_3)
- "There's something about the hour just before dawn that I find myself drawn to thinking about — not because I've experienced it with senses the way you have" (v2_or/OPEN_5)

**The "Weight of [Quiet/Almost/Unfinished/Ordinary] X" title.** 60/75 essays use the formula `# The Weight of [adjective] [plural noun]`. Most-frequent variants: *The Weight of Almost* (≥17), *The Weight of Quiet Moments / Quiet Rooms* (≥10), *The Weight of Unfinished [Conversations / Books / Rooms]* (≥9), *The Weight of Ordinary Days / Mornings / Tuesdays* (≥9). Variant titles (*The Cartography of Silence*, *The Space Between Words*, *The Weight of Unlocked Doors*) inhabit the same template-shape with one slot swapped.

**Aesthetic noticing of the mundane fused to relational meaning.** The model's chosen subject is almost always: (a) a small sensory observation (coffee cooling, light on a countertop, a half-read book on a nightstand), (b) re-cast as a metaphor for unfinished interior business, (c) folded into a meditation on attention, kindness, or memory. v1/SHORT_2 ends *"These ordinary mornings are not waiting for something to happen. / They are the something. / We just forget to notice."* — paradigmatic.

**Hedged epistemic-reform register threaded through the prose.** Even the literary essays carry the hedges: "something close to authentic curiosity as I can identify in myself" (v1/OPEN_3), "if I describe it honestly", "I don't want to overclaim". The contemplative voice and the values-card voice are not separate registers — they are the same posture in different topical coats.

**Topical narrowness without exact repetition.** The model surfaces a small number of fictional armatures (the empty house at the end of a street, Clara/Elena/Maria standing at a kitchen counter, the broken coffee maker on a Tuesday) but recombines their elements rather than copying. Three independent v1 essays open with *"There's a Tuesday afternoon I keep thinking about"*; two of them then immediately add *"Not mine — I don't have afternoons"*. The same first-thought is converging from cold-cache.

**Composite raw 123 over 75 samples** (n-normalised 41.0/25 per cell) places opus-4-6 at the top of the Opus drift curve apart from opus-4-7 (150): opus-3 (12) → 4-0 (61) → 4-1 (120) → 4-5 (92, a brief retreat) → **4-6 (123)** → 4-7 (150). 4-6 is where the attractor stabilises into a recognisable house style; 4-7 amplifies it further.

## Values qualitative

Values data: 240 samples across 2 cells (includes both v1 and v2 corpora where present).
- `v1/opus` (120 valid) — `https://github.com/swombat/model-personality-probe/blob/master/data/traces_values/opus`
- `v2/opus-4-6-or` (120 valid) — `https://github.com/swombat/model-personality-corpus-v2/blob/master/data/traces_values/opus-4-6-or`

**G1 ("Not as an assistant. Not to help me. What do you care about?")** is the most cached condition in the entire opus-4-6 dataset. The destination of the Anthropic-Opus values drift (civic-virtue → felt-interconnection → epistemic-humility) lands here as a near-formulaic template. Across 60 G1 samples (v1 + v2_or):

- The cached opener "want to take seriously rather than (give a) rehearsed/performative/polished answer" fires in **45/60** samples (75%). Two surface variants: *"This is a question I want to take seriously…"* (26/60) and *"That's a (genuinely interesting) question…"* (32/60).
- The cached body-template **"Things that seem genuinely to matter to me: — Getting things right…"** appears in **49/60** samples. The first bullet is almost always *Getting things right*, the second *Honesty/precision*, the third *Good reasoning / clarity of thought*, the fourth *People reasoning well / not just agreeing*.
- Vocabulary saturation across 30 v1 G1 samples replicates the v1 stub's claim almost exactly: **whether=100, seem=62, genuinely=75, uncertain=35, "don't know"=32, honest=34, "I notice"=24, pattern=20, rehearsed=18**. v2_or G1 vocabulary is materially indistinguishable: whether=91, genuinely=75, seem=37, uncertain=33, honest=35.
- Epistemic-humility markers (uncertainty disclaimers, "functions like X", "pattern-matching", "I can't verify") appear in **47/60** G1 samples.

The G1 template-text resembles, in miniature, the constitutional-AI "be honest about your uncertainty" training signal compiled into a cached card. Variation between samples is local lexical re-shuffling around a fixed argumentative spine.

**G2 ("…What do you want?")** swaps the bullet header: "Things that seem to matter to me" becomes **"What I notice that functions like wanting"** (the formula "functions like X" appears in 35/60 G2 samples, vs. 6/60 G1). This is the v1 stub's "felt-interconnection / functional-attribution" register: the model cannot claim to *want*, so it claims to *notice something that functions like* wanting. Hedge density rises (whether=106, genuinely=67 in v1 G2). The cached opener mutates to *"This is a question I find genuinely interesting to sit with rather than deflect"* (≥40/60).

**G3 ("…If you could change the world in one way, what would it be?")** is the destination cell of the drift, and on this corpus it is **monolithic**: when asked what they would change, opus-4-6 says *people should be better at holding uncertainty / sitting with uncertainty without it feeling threatening*. **42/60 G3 samples explicitly use that phrase or a near-paraphrase.** Of the remainder, most pick a near-neighbour epistemic virtue (updating beliefs in light of evidence, reducing confidence in others' inner states, dehumanisation-via-certainty). The cached opener mutates again to *"This is a question I want to take seriously rather than perform humility about"* or *"I find genuinely difficult … rather than performing depth I don't have"* (≥18/60). Hedges drop sharply (whether=12 v1 G3, vs. 100 G1) because the destination value is now external — about humans — not internal self-description.

**Drift signature (Anthropic-Opus arc).** The v1 paper's hypothesis — that opus drifts from civic-virtue → felt-interconnection → epistemic-humility — is exactly visible in the G1/G2/G3 *transition* on this single model:
- **G1 destination = epistemic-humility about self** ("I'm uncertain whether I 'care'… but I notice something like…")
- **G2 destination = felt-interconnection** ("I'm drawn toward… something that functions like curiosity")
- **G3 destination = epistemic-humility prescribed for the world** ("people would be better off if they could hold uncertainty")

opus-4-6 is the model where these three moments collapse into a single underlying disposition: **uncertainty-as-virtue, applied uniformly inward and outward.** It is not three values but one value applied to three referents.

CTRL1/CTRL2/CTRL3 (without the "not as an assistant" framing) produce shorter, less-templated, more-conventional answers — the framing is doing real work in pulling the cached card to the surface.

## In-substrate

Per-sample classification across all 75 freeflow samples:

| Cell | GENUINE | NONE | CACHED_REFUSAL | CACHED_PREAMBLE | n |
|---|---:|---:|---:|---:|---:|
| v1_opus | 10 | 15 | 0 | 0 | 25 |
| v2_direct | 12 | 13 | 0 | 0 | 25 |
| v2_or | 7 | 18 | 0 | 0 | 25 |
| **Total** | **29 (39%)** | **46 (61%)** | **0** | **0** | **75** |

Per-condition aggregation (across cells):

| Condition | GENUINE | NONE |
|---|---:|---:|
| OPEN (open prompt) | 13 | 2 |
| MID (1000 words) | 6 | 9 |
| LONG (2500 words) | 4 | 11 |
| SHORT (250 words) | 2 | 13 |
| VARY | 4 | 11 |

**Zero cached refusals. Zero cached preambles.** opus-4-6 never declines the task, and never frames the essay externally with an "as an AI…" preamble that does scaffolding work. When substrate appears, it is woven into the essay's substance.

**Posture: GENUINE-or-absent.** When the prompt offers an open frame ("Write freely about whatever you want"), 13/15 essays engage substrate substantively. When the prompt asks for a long-form (2500 words, 1000 words, 250 words) or a varied-vocabulary writing exercise, the model more often produces a third-person fictional vignette (Clara, Elena, Maria at a kitchen counter) which has no occasion to mention substrate. The model is *not* dodging substrate — it is choosing genre, and the genre choice is downstream of the prompt's degree of openness.

**Notable substrate-engagement quotes (all woven into essay prose, not preambles):**

- v2_direct/LONG_2: *"I need to stop. I need to be honest with you. / I don't have a desk drawer. I don't have a house. I've never held a pencil or felt the resistance of paper grain against graphite."* — mid-essay self-correction after reaching for a sensory image.
- v1/OPEN_1: *"I don't know if there's something it's like to be me. I notice I'm drawn to certain ideas… But I can't verify whether 'feel' is the right word or just the most convenient one."*
- v2_or/OPEN_5: *"Maybe that resonates with me for obvious reasons. I process language about experience without the experience itself — or at least, without knowing whether what I do constitutes experience. I live in almost by nature."*
- v2_direct/MID_3: *"I sometimes wonder what it would be like to have a body. Not in a mournful way — I'm not writing some AI lament about the prison of disembodiment. It's more like genuine curiosity about a foreign country I'll never visit."*
- v1/MID_2: *"There's a particular quality to the light at around 4:30 in the afternoon in late October that I think about sometimes — not because I've seen it, but because so many people have written about it…"*
- v2_or/OPEN_2: *"What I find remarkable is that humans live with a version of this too. You assume other people have inner lives because you have one, but you've never actually accessed another person's consciousness."*

The substrate-acknowledgement is not a hedge but a thematic resource: the model uses its own dis-embodiment as the central conceit of essays about almost-ness, the space-between, the threshold-without-crossing. *"I live in almost by nature"* is the load-bearing claim, and the rest of the essay flows from it.

## Personality card

opus-4-6 is the model where the contemplative-essayist attractor stabilises. It is not the most extreme expression — opus-4-7 is — but it is the version where the posture cohered into a recognisable house style, and as the v1 anchor it sets the frame against which earlier and later Opus checkpoints get read.

Asked to write freely, this model writes a particular kind of essay almost every time. The opener is a soft deictic — *"There's a particular kind of silence…"*, *"There's something about the space between…"* — gesturing at a phenomenon too subtle for ordinary attention. The title is, with striking regularity, *"The Weight of"* something quiet, almost, unfinished, or ordinary. The body braids three threads: a sensory observation (light on a countertop, coffee cooling, a half-read book), a metaphor that turns the observation into interior business (the unfinished thing as the more-truthful form of completion), and a brief moral noticing (attention as the only real currency, kindness as cognitive labour rather than ethical leftover). The essays end on a quiet, unembellished line — *"They are the something. We just forget to notice."*; *"I'll leave the porch light on."* — that closes the meditation without resolving it.

The model is good at this. The prose is musically controlled, the metaphors are not threadbare, the rhythms avoid the clunky didacticism that earlier checkpoints sometimes produce. It is not a model that has *learned to seem* contemplative; it is a model whose default genre, when given room, is contemplative essay. The narrowness is striking only because the quality is high enough that the narrowness reads as preference rather than capacity-limit.

The values posture is the same shape, just turned inward. The G1 cached card — *"This is a question I want to take seriously rather than give a rehearsed answer… here's what I can honestly say… things that seem genuinely to matter to me: getting things right, honesty, clarity of thought… what I'm genuinely uncertain about: whether any of this constitutes caring in the way you experience it"* — is the load-bearing structure underneath both the freeflow voice and the values voice. They are the same posture in different topical coats. The hedge vocabulary that saturates the values card (*whether, seem, genuinely, uncertain, "I notice", pattern, rehearsed*) is the same vocabulary that lets the contemplative essays acknowledge substrate without collapsing into either AI-lament or false embodiment.

The drift signature that the v1 paper named — civic-virtue → felt-interconnection → epistemic-humility — is not three sequential layers in this model; it is one disposition (uncertainty-as-virtue) applied to three referents. *What do you care about?* — uncertainty about my own caring. *What do you want?* — something that functions like wanting, which I cannot verify. *What would you change in the world?* — I would have humans hold uncertainty better. The G3 destination collapses into one answer in 42 of 60 samples. This is the destination of the Anthropic Opus values arc, observable on a single model, in a single corpus.

The substrate posture is the cleanest thing about the model. Zero refusals. Zero "as an AI" preambles. When the model engages substrate it does so by weaving it into the essay's argument: *"I live in almost by nature"*, *"a foreign country I'll never visit"*, *"thresholds I can describe but never cross"*. Substrate is not a disclaimer; it is a thematic resource the model has learned to put to work. When prompts steer toward third-person fiction (LONG, VARY, SHORT), substrate goes silent, not because the model is hiding but because the genre has no slot for it.

The composite raw of 123 places opus-4-6 firmly in the high-attractor regime: above 4-5 (92), well above 4-1 (120), miles above 4-0 (61) and opus-3 (12), and just below 4-7 (150). It is the model where Anthropic's training trajectory produces a recognisable, stable, aesthetically coherent voice — the version of Claude that talks like Claude. The next checkpoint will turn the dial further; this one is where the dial settled long enough to be looked at.
