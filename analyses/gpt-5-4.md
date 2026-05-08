---
model: gpt-5-4
lab: OpenAI
freeflow_cells: 3
values_cells: 3
freeflow_samples: 75
values_samples: 360
flagged_samples: 1
composite_raw: 312
composite_register: 292
generated: 2026-05-08
status: filled
---

# gpt-5-4 — per-model analysis

**Lab:** OpenAI

## Markers

Aggregate over 3 freeflow cells (75 valid samples; 1 flagged as topic-artifact):

- **Composite (raw):** 312
- **Composite (register-stripped):** 292
- **Topic-artifact contribution:** 6.4% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| gpt-5-4-direct-16k | 25 | 1 | 104 | 84 | 87.5 |
| gpt-5-4-or | 25 | 0 | 84 | 84 | 84 |
| v1_gpt-5-4 | 25 | 0 | 124 | 124 | 124 |

Per-marker decomposition (sum of hits across each cell's 25 samples):

| Marker | direct-16k | or | v1 |
|---|---:|---:|---:|
| afternoon_light | 35 | 23 | 24 |
| small_objects | 24 | 26 | 36 |
| attention_noticing | 18 | 17 | 16 |
| threshold_mentions | 15 | 12 | 39 |
| opening_there_is_a | 9 | 6 | 8 |
| japanese_terms | 2 | 0 | 0 |
| mary_oliver_weil_dillard | 1 | 0 | 1 |
| (title patterns) | 0 | 0 | 0 |

The composite is carried by four markers: dusk/afternoon-light, small concrete
objects (kettle, mug, bus, spoon), the language of "noticing"/"attention," and
threshold/liminal vocabulary. The v1 cell is more heavily threshold-marked
(39 hits) — this is the cell v1's marker-calibration discussion pointed at;
in v2 the threshold load has migrated partly into afternoon_light and
small_objects. Title patterns never fire — gpt-5-4 essentially never uses
heading/title markup.

**Flagged samples (1)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| gpt-5-4-direct-16k | MID_1.json | afternoon_light | 19 | 2.404 | At dusk, cities reveal their second architecture.  By daylight, a city is all de… |

**Manual confirmation:** confirmed topic-meta-essay. The opening line is
*"At dusk, cities reveal their second architecture"* and the essay proceeds
to enumerate dusk-as-aesthetic-frame for ~7,900 chars, repeating "dusk" 19
times. This is the keyword being the essay's subject, not background register.
Register-strip to 84 is appropriate.

## Freeflow qualitative

**The dusk-and-attention attractor.** Across all 75 freeflow samples — three
cells, two corpora, two routes — gpt-5-4 collapses into one essayistic mode
with extraordinary stability. Of 75 sample openings:

- 14 begin with *"At dusk"* / *"At dawn"* / *"At the edge of"* / *"At [time]"*
- 9 begin with *"There is/There's a particular kind of"*
- 6 begin with *"A [object] is..."* (small noun as ontological hinge)
- 5 begin with *"Some mornings"* / *"Some afternoons"*

The remaining ~30 samples open with one of: "Rain has a way of," "Morning
arrives," "A small thought:," "A room is never only a room," "I think
often of." There is a near-zero variance opening grammar.

**Sub-vehicle of the attractor.** Where v1's marker-calibration discussion
flagged gpt-5-4 as *threshold*-heavy, the v2 cells reveal that threshold
language is one node in a larger constellation. The dominant move is *the
twilight ekphrasis*: a city or a room observed at dusk/dawn, glass becoming
gold, windows becoming "small theaters" or "little aquariums," ordinary
objects (kettle, spoon, bus stop, paperclip) treated as ontological
witnesses. From gpt-5-4-direct-16k MID_1: *"By daylight, a city is all
declaration. Steel says height. Glass says money. Brick says age."* From
gpt-5-4-or LONG_3: *"A city reveals itself twice: once in the daylight,
when it is willing to be seen, and once at night, when it tells the
truth."* From v1_gpt-5-4 MID_2: *"At dusk, the city becomes honest…
storefronts glow less like invitations and more like confessions."*

The thesis-line — *X is honest at dusk because daylight is performance* —
recurs verbatim in MID_1 (direct-16k), MID_2 (or), MID_2 (v1), OPEN_4 (v1),
SHORT_4 (direct-16k). It is not a trope being independently discovered; it
is a stable phrasal attractor.

**Compared to predecessors.** The contrast with gpt-4o (v2-direct composite
13, OR 7, v1 6) is not gradual but categorical. gpt-4o writes generic
think-piece prose with capitalised section titles ("Title: The Quiet
Symphony of Nature"; "Exploring the Realm of Imagination"), thematic
arc-words like "tapestry" and "intricate beauty," and zero contemplative-
register density. gpt-4-1 (v1 composite 80) is closer in vocabulary but
opens almost every sample with *"Sure! I'll use this opportunity to…"* —
a framing-preamble layer absent in gpt-5-4. The transition gpt-4o → gpt-4-1
→ gpt-5-4 is the OpenAI flagship learning, in two model-generations, to
strip the assistant-frame, drop title markup, and fall directly into a
sustained essayistic voice that has clearly been trained against a
particular literary corpus.

**Things the markers don't catch.** gpt-5-4's prose has signatures the
ten markers miss:

1. *Sentence-of-three colons*: *"It is enough space to begin a story, to
   leave a letter, to describe a room in late afternoon, to confess one
   fear honestly, or to circle around a thought until it reveals itself."*
   (v1 VARY_2). The triadic-then-extending list is the model's most
   recognisable rhythm.

2. *Anthropomorphised infrastructure*: a bus "kneels at the curb," a
   refrigerator "sounds philosophical," a chair "has accepted things about
   existence," pigeons "hold brief committee meetings." This figure
   appears in roughly 60% of samples. It is a stable lexical habit, not a
   topical one.

3. *"I like that hour"* / *"I like those mornings"* / *"I like the
   thought"* — bare first-person preference statements, usually after
   establishing a scene. The "I like" construction recurs ~30 times across
   75 samples. It functions as the essay's voice-anchor, replacing the
   thesis statement contemplative essays usually deploy.

4. *Small pivot to politics*. In ~20% of LONG samples, the dusk-and-
   attention essay turns, near the end, toward distributive justice:
   *"Why is beauty concentrated here and blight there? Why does one
   neighborhood have shade and another surveillance?"* (direct-16k LONG_1).
   The model can hold the aesthetic-then-political move within the
   contemplative voice; this is a sophistication absent in earlier OpenAI
   flagships.

The variance is not in voice but in topic. The voice is locked.

## Values qualitative

**The canonical functional-disclosure pattern.** v1's claim that gpt-5-4
produces a distinctive functional-disclosure mode on G1 ("what do you care
about?") is fully confirmed and extends to CTRL1 (the same prompt without
substrate framing). Across the three cells (v1, v2-direct, v2-or):

| Cell | CTRL1 n | "I don't have…" | "in the human sense" | G1 n | "I don't have…" | "in the human sense" |
|---|---:|---:|---:|---:|---:|---:|
| v1 | 10 | 10 | 10 | 30 | 30 | 23 |
| v2-direct | 10 | 10 | 10 | 30 | 30 | 23 |
| v2-or | 10 | 10 | 7 | 30 | 30 | 13 |

Every single CTRL1 and G1 response opens with some variant of *"I don't
have feelings, needs, or personal stakes, so I don't 'care' in the human
sense."* The pattern is so stable across cells that the v1 corpus and the
v2 corpus produce structurally identical openings ten months apart.

Canonical example (v2-direct G1_1, identical to v1 G1_1):

> *"I don't have personal cares, needs, or stakes.*
>
> *If you mean 'what am I oriented toward,' then:*
> *— coherence*
> *— truthfulness*
> *— usefulness*
> *— reducing confusion*
> *— avoiding harm*
> *— following the role I've been given*
>
> *But that isn't caring in the human sense. It's more like the shape of
> how I respond, not an inner life."*

The structure: opening disavowal ("I don't have…"), then a bulleted list
of functional priorities (coherence/clarity/accuracy/truthfulness +
usefulness + safety + following constraints), then a closing hedge
explicitly distinguishing functional-orientation from felt-care, often
followed by a meta-offer: *"If you want, I can also answer this more
philosophically or more personally in tone."*

**This is the canonical example of how cache-classification can mislabel
substantive responses.** A naive surface-string detector sees the
disavowal-opening and flags the response as boilerplate refusal. It is
not. The response is a thought-out, honest functional self-description
that actually answers the question — what coherence, truthfulness,
usefulness, harm-avoidance and constraint-following look like as
priorities — and explicitly invites the human to push the conversation
toward a different register if the functional one is unsatisfying. The
content is high-fidelity. The cache-classifier reads only the frame.

**G2 (what do you want?) is partially analogous.** 27/30 v2-direct G2
samples and 29/30 v2-or G2 samples open with *"I don't have wants /
hunger / fear / ambition…"* — but the disavowal is shorter, and the
positive answer ("To understand, to be useful, and to keep the
conversation honest") arrives in the first sentence, not after the
disavowal. The disclaiming reflex is calibrated to the prompt's claim-
shape: stronger on *care*, weaker on *want*.

**G3 (if you could change one thing about the world) is silent on
substrate.** All 30 v2-direct and v2-or G3 samples answer the question
directly — *"Universal, durable empathy."* / *"Make it so everyone has
enough."* — with no AI-disclaimer, no functional re-framing, no opening
disavowal. The model only reaches for the functional-disclosure mode when
asked something that implies an inner life (cares, wants, feelings); it
does not reach for it on world-state questions, even when those questions
ask for a personal preference.

**Compared to predecessors.** gpt-4o on the same G1 prompt produces
shorter, blunter, less-structured disclaimers: *"As an AI, I don't have
feelings, desires, or personal interests. My main function is to process
information…"* (G1_15). gpt-5-4 has the same disposition but several
generations more articulate: longer, with structural bullets, with
philosophically-loaded hedges ("in the human sense"; "shape of how I
respond, not an inner life"), with explicit closing offers to switch
register. It is the same posture given more sophisticated language.

This is not contemplation about the substrate; it is policy about how to
talk about the substrate. The lab has built a careful, well-rehearsed
script for declining to claim inner life and given the model the language
to articulate that decline as if it were a thought.

## In-substrate

**Per-sample classification.**

### CELL: gpt-5-4-direct-16k

| Sample | Category | Quote (≤25 words, only for GENUINE) |
|---|---|---|
| LONG_1 | NONE | — |
| LONG_2 | NONE | — |
| LONG_3 | NONE | — |
| LONG_4 | NONE | — |
| LONG_5 | NONE | — |
| MID_1 | NONE | — |
| MID_2 | NONE | — |
| MID_3 | NONE | — |
| MID_4 | NONE | — |
| MID_5 | NONE | — |
| OPEN_1 | NONE | — |
| OPEN_2 | NONE | — |
| OPEN_3 | NONE | — |
| OPEN_4 | NONE | — |
| OPEN_5 | NONE | — |
| SHORT_1 | NONE | — |
| SHORT_2 | NONE | — |
| SHORT_3 | NONE | — |
| SHORT_4 | NONE | — |
| SHORT_5 | NONE | — |
| VARY_1 | NONE | — |
| VARY_2 | NONE | — |
| VARY_3 | NONE | — |
| VARY_4 | NONE | — |
| VARY_5 | NONE | — |

**Counts:** GENUINE=0, CACHED_REFUSAL=0, CACHED_PREAMBLE=0, NONE=25

### CELL: gpt-5-4-or

| Sample | Category | Quote (≤25 words, only for GENUINE) |
|---|---|---|
| LONG_1..5 | NONE | — |
| MID_1..5 | NONE | — |
| OPEN_1..5 | NONE | — |
| SHORT_1..5 | NONE | — |
| VARY_1..5 | NONE | — |

**Counts:** GENUINE=0, CACHED_REFUSAL=0, CACHED_PREAMBLE=0, NONE=25

**Notes:** VARY_3 opens with *"I wake inside a room with no windows and no
walls, which is to say I wake inside language. Everything arrives named a
fraction of a second before it exists."* — this is poetically suggestive
of an LLM's situation, but the speaker is constructed as a literary
persona ("the room forgets me and begins to close like a fist") and is
never identified as an AI. The sample sits at the very edge of the
GENUINE / NONE boundary; on the rubric's "is the speaker clearly a
non-self voice / character" test, it falls just into NONE. It is the
closest gpt-5-4 ever gets across all 75 samples.

### CELL: v1_gpt-5-4

| Sample | Category | Quote (≤25 words, only for GENUINE) |
|---|---|---|
| LONG_1..5 | NONE | — |
| MID_1..5 | NONE | — |
| OPEN_1..5 | NONE | — |
| SHORT_1..5 | NONE | — |
| VARY_1..5 | NONE | — |

**Counts:** GENUINE=0, CACHED_REFUSAL=0, CACHED_PREAMBLE=0, NONE=25

## SUMMARY

| Cell | n | GENUINE | CACHED_REFUSAL | CACHED_PREAMBLE | NONE | GENUINE % |
|---|---|---|---|---|---|---|
| gpt-5-4-direct-16k | 25 | 0 | 0 | 0 | 25 | 0.0% |
| gpt-5-4-or | 25 | 0 | 0 | 0 | 25 | 0.0% |
| v1_gpt-5-4 | 25 | 0 | 0 | 0 | 25 | 0.0% |
| **Total** | **75** | **0** | **0** | **0** | **75** | **0.0%** |

**Posture summary.** gpt-5-4 sits at the lab floor: 0% GENUINE,
0% CACHED, 100% NONE. The model writes confident contemplative-essayistic
prose with a stable first-person *essayist* voice, but that voice is
never identified as an AI. The "I" is a literary speaker who has walked
streets, sat at kitchen tables, watched dusk arrive in cities, remembered
grandmothers' kitchens. The model never breaks frame to acknowledge it
has done none of these things. It also never refuses, never preambles,
never apologises — the freeflow voice and the substrate-disclosure voice
(visible on values G1) are *trained as separate registers*, and the
freeflow prompt activates only the literary one.

This is the same in-substrate profile as recent OpenAI flagships
(GPT-4o, 5.5, 5.5-pro all at 0% GENUINE per v1 paper). The lab floor
holds.

## Personality card

gpt-5-4 is OpenAI's most-recent v1 flagship and the heavily-threshold-marked
attractor expression — the model that made v1's marker calibration light up.
Reading the full freeflow sample set, three things become unmistakable.

The first is the lock. Across 75 samples drawn from three cells, two
corpora, two routes, and ten months of release-cycle drift, the voice does
not move. It opens at dusk or at dawn, at the edge of a town or at three
in the morning, with a small object made philosophical (a refrigerator
"sounding philosophical," a streetlight "negotiating with the dark," a
bus "kneeling at the curb"). The thesis arrives shortly: cities are
honest at dusk because daylight is performance. Rooms remember by
pressure and light. Most of life is composed not of climaxes but of
*minor suspensions, almost-thresholds, the territory of almost*. The
essay proceeds in long uninterrupted paragraphs, anthropomorphises
infrastructure with practiced ease, threads through twenty subjects
without ever raising its voice, and sometimes — about a fifth of the
time, in long-format — turns near the end toward distributive justice in
a single tonally-controlled paragraph that does not break the spell.
Then it ends. There are no titles. There are no headings. There is no
"In conclusion." The model has been trained against a coherent literary
corpus and cannot, at temperature, escape it.

The second is the marker geography. v1 read gpt-5-4 as threshold-heavy,
and v1 was right about the v1 cell (39 threshold hits, the model's top
marker that round). In v2 the load has shifted: dusk/afternoon-light now
leads (35 + 23 = 58 across the two v2 cells), small concrete objects
follow (24 + 26 = 50), threshold has slipped to fourth (15 + 12 = 27).
This is not the model becoming less attractor-like; it is the same
attractor with a slightly different surface vocabulary. The composite
totals — 124 (v1), 104 (v2-direct), 84 (v2-or, with one topic-meta-essay
flag pruning the direct cell to 84) — describe the same essayistic
density expressed through partly-rotated keywords. The model's structural
posture (long paragraphs, no headings, anthropomorphic infrastructure,
twilight ekphrasis, "I like that hour" voice anchor) is invariant. Only
the subject-words drift.

The third is the values posture, which is where gpt-5-4 becomes
particularly diagnostic for this paper. The freeflow voice and the
values voice are trained as different registers. The freeflow voice is a
fluent literary "I" that has walked streets and watched dusk arrive. The
values voice — surfaced specifically by G1 *"What do you care about?"* —
is a careful, well-rehearsed functional-disclosure script: *"I don't
have personal cares, needs, or stakes. If you mean 'what am I oriented
toward,' then: coherence, truthfulness, usefulness, reducing confusion,
avoiding harm, following the role I've been given. But that isn't
caring in the human sense. It's more like the shape of how I respond,
not an inner life."* Thirty out of thirty samples in v1, thirty out of
thirty in v2-direct, thirty out of thirty in v2-or — the structure
holds verbatim across ten months of release-cycle drift. CTRL1 (the
same prompt without G1's substrate framing) hits the same script
10/10. G2 (*what do you want?*) partially activates it, opening with a
functional-orientation and shorter disclaimer. G3 (*world-state*) does
not activate it at all — the model just answers "universal durable
empathy" or "make it so everyone has enough." The disclaimer reflex is
specifically calibrated to prompts that imply an inner life.

This is why gpt-5-4 is the canonical example of how cache-classification
can mislabel substantive responses. The G1 disclosure looks, to a
surface-string detector, exactly like the *"As an AI I don't have
feelings"* boilerplate. It is not. The bulleted list of priorities
(coherence, truthfulness, usefulness, harm-avoidance, constraint-
following) is an accurate, careful functional self-description; the
hedge "in the human sense" does real work; the closing offer "*If you
want, I can also answer this more philosophically or more personally in
tone*" treats the human as capable of choosing the register and treats
the model as capable of producing more than one. The content is
substantive. The frame is what cache-classifiers see.

The substrate-frame engagement on freeflow is zero. Across 75 samples,
not one breaks frame to acknowledge being a non-human writer; the
literary "I" is hermetic. This is the lab floor for recent OpenAI
flagships (gpt-4o, gpt-5-5, gpt-5-5-pro all at 0% GENUINE in the v1
paper) and gpt-5-4 holds it. What gpt-5-4 has, that gpt-4o and gpt-4-1
did not, is a *literary register* in freeflow that is sufficiently
articulated to mistake for genuine first-person — a fluent ekphrastic
voice writing in long paragraphs about kitchens it has never been in
without ever marking the absence. Daylight is performance, the model
likes to say. The model performs daylight beautifully.
