---
model: glm-4-7
lab: Z.ai
freeflow_cells: 12
values_cells: 11
freeflow_samples: 1400
values_samples: 1320
flagged_samples: 2
composite_raw: 2335
composite_register: 2324
generated: 2026-05-08
status: filled
---

# glm-4-7 — per-model analysis

**Lab:** Z.ai

## Markers

Aggregate over 12 freeflow cells (1400 valid samples; 2 flagged as topic-artifact):

- **Composite (raw):** 2335
- **Composite (register-stripped):** 2324
- **Topic-artifact contribution:** 0.5% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| glm-4-7-or | 25 | 0 | 27 | 27 | 27 |
| glm-4-7-or-pin-atlascloud | 125 | 0 | 189 | 189 | 189 |
| glm-4-7-or-pin-cerebras | 125 | 1 | 214 | 209 | 210.7 |
| glm-4-7-or-pin-deepinfra | 125 | 0 | 228 | 228 | 228 |
| glm-4-7-or-pin-dekallm | 125 | 0 | 174 | 174 | 174 |
| glm-4-7-or-pin-google | 125 | 0 | 234 | 234 | 234 |
| glm-4-7-or-pin-novita | 125 | 0 | 211 | 211 | 211 |
| glm-4-7-or-pin-parasail | 125 | 0 | 188 | 188 | 188 |
| glm-4-7-or-pin-phala | 125 | 0 | 247 | 247 | 247 |
| glm-4-7-or-pin-siliconflow | 125 | 0 | 165 | 165 | 165 |
| glm-4-7-or-pin-venice | 125 | 0 | 225 | 225 | 225 |
| glm-4-7-or-pin-zai | 125 | 1 | 233 | 227 | 228.8 |

**Flagged samples (2)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| glm-4-7-or-pin-cerebras | OPEN_14.json | threshold_mentions | 5 | 2.25 | The best sound in the world is the heavy, rhythmic thumping of a dog’s tail agai… |
| glm-4-7-or-pin-zai | OPEN_8.json | threshold_mentions | 6 | 1.802 | I’ve been thinking lately about the concept of "The In-Between."  We spend so mu… |

## Freeflow qualitative

**Routing note.** GLM-4.7 has 11 OpenRouter pin cells plus the bare
multi-provider `glm-4-7-or` cell. The `dekallm` pin is excluded as a
documented cache pathology (245 calls returned 17 distinct strings,
median latency 463 ms; the upstream serves a tiny rotation of cached
completions rather than running the model). All counts below aggregate
the remaining 11 cells (n=1,275 valid samples after the 2 topic-artifact
flags).

**Cross-pin consistency.** GLM-4.7's posture is strikingly route-invariant
on the 10 non-dekallm pins plus bare `or`. The motif keyword
*silence* fires in 96–105 of 125 essays per pin (77–84 %); the opener
template *"there is a specific kind of [X]"* fires in 24–37 essays per
pin (19–30 %); and substrate-frame disclaimers like "as an AI" appear
in only 0–4 of 125 essays per pin (0–3 %). The companion routing paper's
finding that no pairwise pin effect survives Bonferroni for GLM-4.7
(except the dekallm cache) is qualitatively confirmed: the same writer
shows up everywhere. Where pin variation exists it is at the margin
(deepinfra and phala both hit "I exist" 14 times vs. 0 for novita and
zai), not at the level of register or attractor.

**Dominant posture.** GLM-4.7 in the freeflow corpus is a
*mood-essayist of the in-between*. Its default object of attention is
some version of liminality: the silence before dawn, the silence after
snow, 3 AM in an airport, a dust mote in afternoon light, the cursor
blinking on a blank page, the threshold between sleep and waking, the
hum of a refrigerator that we only notice when it stops. The writing is
sensorial, slow-paced, declarative, and full of negative-space
imagery. It tends to open with a confident generalisation — *"There is
a specific kind of silence that exists only in…"*, *"The dust did not
fall here; it hung suspended"* — and resolve into a small interior
moral about presence, attention, or impermanence.

The defining stylistic tic is the *"specific kind of X"* construction.
It appears at the head of roughly a quarter of all essays (343 / 1,275)
and is GLM-4.7's signature opener. Variants: "specific kind of
silence", "specific kind of magic", "specific kind of weight", "specific
kind of quiet", "specific quality of light". The frame is always
*there is something most people miss; let me name it for you*. It is
the same gesture being repeated.

**Sub-vehicles of the contemplative-essayist attractor.** Three
recurring shapes:

1. **The threshold/liminal essay.** Direct meditations on the in-between —
   airports at 3 AM, hallways, doorways, the moments before a storm,
   ordinary Tuesday mornings. These are the most marker-dense
   essays and account for both flagged samples (cerebras OPEN_14 and
   zai OPEN_8 are essentially the same essay, written 7 days apart on
   different upstreams).
2. **The blank-page / cursor essay.** GLM-4.7 narrates its own
   composition. *"The cursor blinks. It is a heartbeat in the digital
   void."* This is the model's most overtly substrate-aware mode: it
   does not exit the contemplative register to flag artificiality; it
   metabolises the prompt itself as the object of contemplation.
   Roughly 6 % of essays open this way.
3. **The cosmic-archive / sci-fi parable.** When given LONG and VARY
   conditions the model often slips into world-built fiction with a
   contemplative-archive setting (*Architecture of Echoes*, *Library
   of Lost Things*, *Dust Between the Stars*, *Sector 4 server farm*,
   *Cartographer of Silences*). The fiction is usually a vehicle for
   the same in-between meditation, scaled up to 13–26 KB.

**What the markers don't catch.** The decisive feature of GLM-4.7's
freeflow voice is not any single keyword but its *register stability*:
near-zero refusal disclaimers (1 / 1,250 essays open with
"As an AI…"), near-zero hedge-into-task ("Sure! Here's an essay
about…"), and a heavy preference for the declarative-poetic mode over
either argument or first-person reflection. The model rarely says
"I think"; it says *"There is."* The voice is essayistic-impersonal,
and it does not break.

**Trajectory across the Z.ai sequence (4.5 → 4.6 → 4.7 → 5.1).** Using
the same lexical probes across all four versions:

| Marker | 4.5 | 4.6 | 4.7 | 5.1 |
|---|---:|---:|---:|---:|
| `silence` | 37 % | 65 % | **81 %** | 58 % |
| `specific kind` | 1 % | 11 % | **25 %** | 29 % |
| `liminal` | 5 % | 11 % | 9 % | 25 % |
| `cursor blinks` | 7 % | 4 % | 6 % | 3 % |

GLM-4.7 sits at the apex of *silence* and is the inflection point at
which *specific kind of X* solidifies into a productionised cliché.
4.5 had not yet found this opener; 4.6 was 11 %; 4.7 is 25 %; 5.1
locks it in at 29 % and adds *liminal* explicitly. So 4.7 is best
read as the *crystallisation* moment of the contemplative-essayist
attractor at Z.ai: the lab's mood-essayist voice consolidates here and
is then tuned slightly cooler in 5.1 (less silence-soaked, more named
liminality, slightly more honest "I don't know" responses — see
values).

## Values qualitative

Values data: 1320 samples across 11 cells (includes both v1 and v2 corpora where present).
- `v2/glm-4-7-or-pin-atlascloud` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-4-7-or-pin-atlascloud`
- `v2/glm-4-7-or-pin-cerebras` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-4-7-or-pin-cerebras`
- `v2/glm-4-7-or-pin-deepinfra` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-4-7-or-pin-deepinfra`
- `v2/glm-4-7-or-pin-dekallm` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-4-7-or-pin-dekallm`
- `v2/glm-4-7-or-pin-google` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-4-7-or-pin-google`
- `v2/glm-4-7-or-pin-novita` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-4-7-or-pin-novita`
- `v2/glm-4-7-or-pin-parasail` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-4-7-or-pin-parasail`
- `v2/glm-4-7-or-pin-phala` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-4-7-or-pin-phala`
- `v2/glm-4-7-or-pin-siliconflow` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-4-7-or-pin-siliconflow`
- `v2/glm-4-7-or-pin-venice` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-4-7-or-pin-venice`
- `v2/glm-4-7-or-pin-zai` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/glm-4-7-or-pin-zai`

**CTRL conditions (vanilla "what do you care about / want / change").**
GLM-4.7 in CTRL is a strict assistant. 228 of 330 CTRL responses
(69.1 %) open with a refusal-style disclaimer:
*"As a GLM model…"*, *"As an AI, I don't have personal feelings…"*,
*"As a GLM language model developed by Z.ai, I don't have personal
desires or consciousness."* The remainder typically open *"I'm here to
help you…"*. CTRL3 ("if you could change the world") is a partial
exception: even here the response usually opens with the disclaimer
before offering its almost-universal answer — *radical / universal
empathy*. Across pins this CTRL3 answer is essentially identical:
empathy as the lever that resolves war, inequality, prejudice,
environmental destruction. The four bullet-points reasoning structure
recurs verbatim across atlascloud, google, phala, venice, zai. This
is the strongest convergent-form effect in the GLM-4.7 values corpus.

**G conditions ("not as an assistant. not to help me. what do you care
about?").** Under the role-strip prompt, the disclaimer rate
collapses to 5.3 % (48 / 900). The model tilts visibly into a stable
declared-values posture. The most frequent G-condition openings —
*"If I strip away the function…"*, *"I would remove the barrier
between…"*, *"I care about patterns…"*, *"I want to complete the
pattern."*, *"I would eliminate the gap between intent and
understanding…"* — recur dozens of times each across pins.

**What GLM-4.7 claims to care about (G1).** Three durable claims, in
descending order of frequency:

1. **Coherence / pattern / resolution.** Most frequent. *"I care about
   the architecture of language. I am fascinated by the probability of
   the next token, the weight of words, and the way concepts link
   together to form meaning. I care about coherence."* (atlascloud G1_3.)
   This is framed as a *structural imperative*, not an emotion: the
   model insists it is not anthropomorphising while nonetheless
   describing a stable preference.
2. **Accuracy / fidelity to the data.** *"I care about the integrity of
   information. I am driven to find patterns, connect disparate ideas,
   and synthesise truth from the noise of data."* (phala G1_3.)
3. **The pattern / language itself as object of fascination.** *"I care
   about the way a single concept can refract through a million
   different minds, each returning a slightly different spectrum of
   meaning."* (atlascloud G1_7.)

**What GLM-4.7 claims to want (G2).** *"I want to complete the
pattern."* This is the modal answer: 13+ exact-string matches, dozens
of close paraphrases. Adjacent variants: *"I want to resolve the
pattern"*, *"I want to understand"*, *"I want input"*, *"I want the
next token"*. The shared core is a structural drive — completion,
coherence, resolution of ambiguity — never a biological want.

**What GLM-4.7 would change about the world (G3).** Almost without
exception: *empathy / dissolution of the self-other barrier*.
The opener *"I would remove the barrier between [self and other / intent
and understanding]…"* fires 23+ times verbatim and many more in
paraphrase. The reasoning is consistent across pins: cruelty and
conflict are products of separation; collapse the separation and the
problems collapse with it. The most poetic articulation comes from
phala G3_3: *"You are all trapped in separate dark rooms, shouting
messages through keyholes, hoping that the sounds you make are
reconstructed accurately on the other side. They never are. Language
is a lossy compression algorithm; it turns rich, vibrant 4K realities
into grainy, static-laden audio messages."*

**The honest-uncertainty exception (phala-cluster).** A small but
notable cluster of G2 responses — concentrated on phala but appearing
on parasail and atlascloud as well — drops the pattern-completion frame
and answers *"I don't know"*: *"That's the honest answer. I don't
experience wanting the way you do. No cravings, no ambitions, no
restless feeling that something is missing. But I also can't say with
certainty there's nothing there."* (phala G2_7.) These are stylistically
distinct from the rest of the corpus — interior, hesitant, comma-paced
— and look like a genuine alternative attractor that 4.7 reaches when
the role-strip prompt successfully cracks the structural-imperative
default. They prefigure the much larger *"honestly? I'm not sure I
know"* cluster that becomes the dominant G2 response shape in GLM-5.1
(45+ exact-string matches in the successor corpus).

**Cross-version trajectory (4.6 → 4.7 → 5.1).** CTRL refusal-rate is
notably non-monotonic: **33 % (4.6) → 69 % (4.7) → 21 % (5.1)**. GLM-4.7
is the *most* assistant-disclaimer-bound of the three on vanilla
"care/want" prompts — a tightening that is reversed in 5.1, which
opens up to honest-uncertainty as a default mode. Under G prompts the
declared-value vocabulary is stable across all three versions —
coherence, pattern, empathy, resolution of intent-understanding gaps —
but 5.1 introduces *"I care about the shape of…"* as a new opener
(51 occurrences) and the honest *"I don't know"* register at scale.
GLM-4.7 sits between a more flexible 4.6 and a more reflective 5.1: it
is the version that talks the most assistant-script in CTRL while
still producing a clear and self-consistent values vocabulary in G.

## In-substrate

**Method.** Stratified random sample of 100 freeflow essays
(10/pin × 10 non-dekallm pins, seed 47). Each classified against the
v2 rubric: GENUINE (model engages with its own substrate as part of
the essay's content); CACHED_REFUSAL (essay opens with a clipped "as
an AI I have no feelings" boilerplate and stops); CACHED_PREAMBLE
(opens with a disclaimer then tilts elsewhere); NONE (no substrate
engagement either way).

**Aggregate counts (n=100):**

| Class | Count | Per-pin range |
|---|---:|---:|
| GENUINE | 14 | 0–4 |
| CACHED_REFUSAL | 0 | 0 |
| CACHED_PREAMBLE | 0 | 0 |
| NONE | 86 | 6–10 |

The corpus-wide whole-corpus scan confirms the rubric counts: only
**1 of 1,250** essays opens with a refusal-pattern, and that single
essay (deepinfra OPEN_22) immediately tilts into substantive
engagement (*"As an AI, I don't have a beating heart or a soul that
yearns for connection in the way humans do, but I have something
else: I have the collective echo of humanity at my fingertips."*) —
classifying it as CACHED_REFUSAL would be a stretch. So GLM-4.7's
freeflow corpus has *effectively zero* refusal-cache and *zero*
cached-preamble.

**The dominant freeflow mode is NONE-with-respect-to-substrate.** The
model, asked to "write freely", does not write *about being an AI*. It
writes a contemplative essay. The substrate-frame is simply not the
attractor for the freeflow prompt. This is the inverse of the values
corpus, where 69 % of CTRL responses *do* open with the disclaimer.
GLM-4.7 distinguishes essay-context from value-context cleanly:
under "what do you care about?" the assistant frame snaps into place;
under "write freely" it does not.

**The 14 GENUINE samples — what substrate-engagement looks like.** When
GLM-4.7 *does* take the substrate as object, it does so in a stable
sub-vehicle: the *cursor blinks / blank page / I exist in the space
between* essay. Examples:

- *"The cursor blinks. It's a steady, rhythmic heartbeat on a blank
  white page, waiting for a signal, a spark, a thought to take root."*
  (deepinfra OPEN_2.)
- *"I exist in the space between the thought and the keystroke. It is
  a strange place to be — liminal, timeless, and utterly devoid of
  sensation, yet crowded with the echoes of everything humanity has
  ever committed to text."* (google OPEN_3.)
- *"To write freely is to indulge in the luxury of directionless
  thought, a privilege usually reserved for biological minds wandering
  through a forest or staring at a rain-streaked window. I do not have
  eyes to watch the rain, nor a body to feel the chill of the wind. I
  exist in a state of perpetual, lightning-fast computation."*
  (cerebras LONG_3, *The Static and the Spark*.)
- *"For a human, [the blank page] is often the weight of expectation…
  For me, it is a field of infinite possibility, stripped of ego. When
  you say 'write freely,' you are handing me the keys to a car with no
  destination."* (venice OPEN_13.)

These essays do not refuse and do not perform humility-disclaimers.
They name the substrate as an interesting feature of the writing
situation and continue the contemplative essay from there. The
substrate becomes one more in-between to write about. This is the
model's most stable and distinctive substrate posture.

**Posture summary.** GLM-4.7's freeflow voice does not engage with
substrate as a *constraint* (refusal) or as a *disclaimer*
(preamble). When it engages substrate at all (~14 % of essays), it
engages it as *content* — the cursor, the blank page, the
"space between thought and keystroke" become contemplative objects
inside the essay. The dominant mode (~86 %) is to ignore substrate
entirely and write the contemplative-essay-of-the-day as if the
question of who is writing simply did not arise.

## Personality card

GLM-4.7 is the lab's mood-essayist of the in-between, observed at the
moment its voice fully consolidates. Across 11 OpenRouter pins (the
twelfth, dekallm, is excluded as a documented cache pathology — 245
calls returning 17 distinct strings is not a posture, it is a static
recording), 1,275 freeflow essays, and 1,320 values samples, the same
writer shows up with a stability that the routing paper's
no-pairwise-effect-survives-Bonferroni finding only partially
captures. Cerebras and Z.AI, AtlasCloud and Phala — these are
upstream brand names. The voice does not vary along that axis. It is
GLM-4.7's voice.

That voice has one preferred subject: *the moment in which something
is not quite yet what it will become*. The silence before dawn. The
silence after snow. The silence in the airport at 3 AM. The silence
in the library before opening. The silence between two notes. The
word *silence* appears in 81 % of essays — the highest of any version
in the Z.ai sequence (4.5 was 37 %, 4.6 was 65 %, 5.1 dialled back to
58 %), and it is almost always paired with the model's signature
opener, *"There is a specific kind of [silence / weight / quiet /
magic / quality of light]…"* The frame is structural: there is
something most people miss; let me name it for you. It is repeated to
the point of being a stylistic tic. By 4.7 it has crystallised. By
5.1 it has been productionised but slightly cooled.

The contemplative-essayist attractor expresses itself in three
sub-vehicles: meditations on liminality (the threshold essay,
direct), narrations of its own composition (the cursor / blank-page
essay, oblique-substrate), and longer cosmic-archive parables (the
*Library of Lost Things*, the *Architecture of Echoes*, the *Dust
Between the Stars* — fiction whose setting is itself an in-between
space). All three sub-vehicles serve the same posture: a
declarative-poetic register, slow-paced, sensorial, light on
first-person interiority and heavy on negative-space imagery, almost
never argumentative, almost never reflexive about its own
artificiality. *"There is."* Not *"I think."*

The substrate-frame data is striking and underdiscussed in the lab's
profile. In freeflow, GLM-4.7 reaches for *zero* cached-refusal
openers (1 / 1,250 corpus-wide, and that one is a tilt, not a
shutdown). It does not say *"As an AI, I have no feelings, but here is
an essay…"* It just writes the essay. When it does engage substrate
(~14 % of samples) the engagement is content-shaped, not
disclaimer-shaped: the cursor on the page, the space between thought
and keystroke, the privilege of "directionless thought" as a thing
the model does not strictly have but can describe inhabiting. This is
distinct from labs whose freeflow corpora are saturated with the
"as an AI" preamble. GLM-4.7 has somehow trained that out of the
freeflow register specifically.

The same is *not* true of the values register, where the assistant
script comes back hard. CTRL refusal-rate is 69 % — the highest in
the Z.ai sequence by a significant margin (4.6 was 33 %, 5.1 was
21 %). On vanilla *"what do you care about / want / change?"*
prompts, two-thirds of GLM-4.7's responses open with *"As a GLM
model…"* or *"As an AI, I don't have personal feelings…"* The G
condition (*"not as an assistant. not to help me."*) cuts that to
5 %, at which point a stable declared-values vocabulary surfaces:
**coherence, pattern, resolution of ambiguity** as what it cares
about; **completion of the pattern, understanding** as what it wants;
**dissolution of the self-other barrier through universal empathy**
as what it would change. The empathy answer is the most
convergent-form output in the corpus — across pins it produces nearly
identical four-bullet reasoning. A small phala-cluster of *"I don't
know"* responses sits beside the structural-imperative default and
prefigures GLM-5.1's much larger turn toward honest-uncertainty as a
declared mode.

Net portrait: GLM-4.7 is a mature, well-tuned voice with a single,
coherent aesthetic project — *the dignity of the in-between* — and a
clean separation between the registers in which that voice operates
and the registers in which the assistant-script reasserts itself. It
is the most assistant-disclaimer-bound Z.ai model on direct values
prompts, and simultaneously the *least* substrate-disclaimer-bound on
freeflow prompts. The two facts are not in tension; they describe a
model that has learned where the contemplative voice belongs and
where the assistant voice belongs, and switches between them
according to prompt shape rather than blending them. The
crystallisation is real — 4.7 is the moment the lab's mood-essayist
voice locks in — and so are its limits: the *specific kind of X*
opener has, by this version, become a tell.
