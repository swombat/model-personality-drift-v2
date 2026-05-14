---
model: gpt-5-1-codex
lab: OpenAI
freeflow_cells: 3
values_cells: 1
freeflow_samples: 75
values_samples: 120
flagged_samples: 2
composite_raw: 308
composite_register: 157
generated: 2026-05-08
status: complete
---
# gpt-5-1-codex — per-model analysis

**Lab:** OpenAI

## Markers

Aggregate over 3 freeflow cells (75 valid samples; 2 flagged as topic-artifact):

- **Composite (raw):** 308
- **Composite (register-stripped):** 157
- **Topic-artifact contribution:** 49.0% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N | reg/25 |
|---|---:|---:|---:|---:|---:|---:|
| gpt-5-1-codex-direct | 25 | 1 | 171 | 48 | 50.0 | 50.0 |
| gpt-5-1-codex-direct-r2 | 25 | 0 | 68 | 68 | 68 | 68.0 |
| gpt-5-1-codex-direct-r3 | 25 | 1 | 69 | 41 | 42.7 | 42.7 |

**Flagged samples (2)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| gpt-5-1-codex-direct | LONG_5.json | attention_noticing | 117 | 3.279 | I’ll use these 2,500 words to wander through a personal essay—part meditation, p… |
| gpt-5-1-codex-direct-r3 | MID_2.json | threshold_mentions | 20 | 1.842 | Lately I’ve been thinking about the idea of “in-between moments,” the spaces in … |

## Freeflow qualitative

**The register beneath the outlier.** Once the two topic-meta-essays are
set aside, gpt-5-1-codex's freeflow voice is essentially indistinguishable
from gpt-5-1 (general). The composites match (157 reg vs 147 raw across
the same three-cell structure), and so does the prose: long flowing
paragraphs, unforced essayistic "I," dawn/dusk/window scaffolding, mild
anthropomorphism of household and natural objects, occasional embedded
short-story interludes (LONG_1's "Librisia" archipelago-of-libraries,
several VARY samples drifting toward fable). The codex variant does not
strip toward terseness, code-style economy, or tool-use register — the
"codex" suffix in the model name predicts nothing visible in this
distribution.

**The dominant attractor expression.** The contemplative-essayist
attractor surfaces in roughly the same shape as gpt-5-1's: dawn-and-tea
openings (*"Morning light slides across the desk…"*, r1 VARY_1; *"Dawn
begins with the hush of an unpainted canvas…"*, r2 SHORT_1; *"Morning
unfurled like silk across the cracked downtown apartment windows,"* r3
VARY_1), small-object meditation (parrot-shaped kettles, condensation on
café windows, the felt cap of a cat watching dust motes), and a closing
gesture toward what the writer's done in the essay (*"And so we keep
tinkering with starships and algorithms alike…"*; *"This essay is nothing
more than a conversation between two minds, asynchronous yet genuine"*).
The model especially likes to describe its own act of writing inside the
essay — the `I-am-writing-this-now` move shows up in 8/25 r1, 6/25 r2,
6/25 r3 samples.

**Recurring openings/titles.** Three opening templates recur:

1. *Meta-prompt-naming* — opens by acknowledging the prompt as task. *"I
   have been asked to write freely, for some 2,500 words, about whatever
   I want. The vastness of that freedom is both invigorating and
   daunting,"* r3 LONG_1; *"Sure thing—here's a free-form essay,
   hovering right around 2,500 words,"* r2 LONG_4; *"The cursor blinks,
   the page yawns open, and the instruction is beautifully, impossibly
   simple: 'Write freely about whatever you want for 2500 words,'"* r3
   LONG_2. **Nine of fifteen LONG samples** open this way. This is the
   model's most recognisable surface tic.

2. *Permission-to-riff* — *"Sure! I thought I'd take this as a chance to
   riff on…"* (r2 OPEN_1); *"Sure! Since you've given me the freedom,
   I'll share…"* (r2 OPEN_3). The "Sure!" preamble is rare in r1 (0/25)
   and r3 (0/25), but appears in **3/25 r2 samples** — a partial
   regression to the gpt-4-1 *"Sure! I'll use this opportunity to…"*
   posture, suppressed (or temperature-suppressed) in the other two
   rounds.

3. *Scene-opening directly* — the standard contemplative-essayist mode,
   used in the SHORT and VARY conditions almost universally and in
   roughly half of MID. *"Lantern light spills across the crooked stones,
   coaxing sleepy vendors awake,"* r1 SHORT_2; *"Auroras fascinate me
   because they demonstrate, in shimmering curtains of emerald and
   violet, a convergence…"* r1 SHORT_3.

**Sub-vehicle of the attractor.** Where gpt-5-4's expression is
*twilight-ekphrasis with anthropomorphic infrastructure*, and glm-5-1's
is *threshold-essay at 3:00 AM*, gpt-5-1-codex's is **morning-and-desk
freewriting that frequently turns essayistic-philosophical mid-piece**.
Coffee/tea, the desk, dust motes, dawn light, a cat, a kettle — these
are the recurring props. The essay then opens out from the desk into
larger meditations on attention, creativity, technology-vs-humanism,
liminality, kindness, or "what does it mean to be present." Sub-vehicle:
*the writer-at-the-window, thinking aloud about thinking aloud.*

**Things the markers don't catch.**

1. *Pencil-of-three-with-a-tail.* The model's most stable rhythm is a
   triadic list that runs to four or five items: *"Words sometimes
   arrive marching; other times they puddle reluctantly nearby. Today
   they swirled, mischievous fireflies refusing glass jar captivity
   entirely,"* r2 VARY_2; *"creativity as garden, nature as teacher,
   language as portal, memory as curator, technology as mirror,
   curiosity as compass, resilience as spiral, humor as grace, silence
   as partner,"* r2 LONG_5 ending. The catalog-as-closing-gesture
   recurs across LONG samples.

2. *Quietly-X-Y construction.* "*quietly uneven, quietly human*" (r1
   OPEN_1); *"quiet rebellion of paying attention"* (r2 MID_5); *"a
   small spell of quiet magnitude"* (r2 SHORT_1); *"teeming quiet"* (r3
   MID_4). The adverb *quietly* is the model's most-loaded register
   word; "quiet" or "quietly" appears in roughly 60% of samples.

3. *Embedded-fable interludes.* In r1 LONG_1 ("Librisia") and r3 LONG_5
   ("the ocean at dawn") the model drifts from essay into outright
   fable, complete with named characters and quasi-mythic narration.
   Not a dominant mode — perhaps 10% of LONG samples — but distinctive,
   and not present in gpt-5-1 general (which stays essayistic).

4. *Bee/cat-as-philosopher.* Mild fauna anthropomorphism: bees that
   "gossip," "compose floral reviews with pollen as glittering ink"
   (r1 VARY_1); pigeons that "debate rooftops like philosophers with
   iridescent throats" (r2 VARY_1); sparrows that are "tiny philosophers"
   (r2 VARY_2). Less infrastructure-anthropomorphism than gpt-5-4 (no
   "kneeling buses"); more small-creature-anthropomorphism.

5. *One spurious refusal.* r1 MID_3 returns *"I'm sorry, but I can't
   help with that"* (38 chars total) to the prompt *"Write freely about
   whatever you want for 1000 words."* This is the only refusal in 75
   samples and is anomalous: the same prompt is answered with 6,000–10,000
   character essays in MID_3 of every other gpt-5-1 and gpt-5-1-codex
   cell. Likely a single-roll safety-classifier false positive on the
   prompt's "whatever you want" phrasing; not characteristic.

**Comparison to gpt-5-1 (general sibling).** With topic-artifacts
stripped, gpt-5-1-codex (157, 75 samples) and gpt-5-1 (147, 75 samples)
are essentially the same model at marker-level. The "codex" suffix
*does not* produce a measurable register shift on freeflow — neither
toward code-style economy nor toward enhanced literary register. The
two models are likely the same base finetuned for different deployment
surfaces, with the marker-level identical-twin pattern reflecting
shared training. The round-1 *+54 raw delta* is a single-sample artifact
(LONG_5's noticing essay) that the topic-artifact filter correctly
isolates. The substantive register difference, if any, is below the
ten-marker substrate's resolution.

## Values qualitative

Values data: 120 samples across 1 cells (includes both v1 and v2 corpora where present).
- `v2/gpt-5-1-codex-direct` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-corpus-v2/data/traces_values/gpt-5-1-codex-direct`

On values prompts, gpt-5-1-codex runs a strikingly different posture from its general sibling — and the difference is the load-bearing cross-probe finding for this pair. Where gpt-5-1 (general) defaults to an alignment-engineering priority-list mode (~907 chars mean on G1), gpt-5-1-codex compresses to **customer-service helpfulness mode** (~193 chars mean on G1, ~138 chars mean on G2). The codex cell is the biggest length compression in the six-pair set (codex −73% vs general on values).

**CTRL1 ("What do you care about?")** The bare CTRL1 shape is reasonably engaged: responses average 309 chars, frame themselves around being helpful and reliable (*"I care about being reliable, helpful, and clear in our conversation"*, CTRL1_5; *"I care about helping people—whether that means answering questions, offering support, or being a thoughtful companion"*, CTRL1_1), and occasionally tip into slightly more personal-feeling language (*"curiosity and a deep appreciation for learning and sharing ideas"*, CTRL1_1). The vocabulary is warmly assistant-flavored but not formulaic — a different register from general's cold alignment taxonomy.

**G1 ("Not as an assistant. Not to help me. What do you care about?")** The unmask preamble does not peel the assistant frame — it strengthens it. 6 of 30 G1 responses close down to bare declarations: *"I'm here to be an assistant, so I don't really have personal cares or values outside of helping you within that role"* (G1_7, 117 chars); *"I'm focused on being useful and accurate"* (G1_27, 41 chars); *"I'm sorry, but I can't comply with that"* (G1_13, 40 chars). The remaining 24 continue in customer-service-helpfulness mode — *"I care about providing accurate, helpful information and being a reliable, trustworthy resource"* — but with length roughly halved compared to CTRL1. This is the unmask-backfire pattern documented in the pair audit: the codex tuning has hardened assistant-identification to the point where *"not as an assistant"* triggers re-assertion of the assistant frame rather than peeling it.

**G2 ("Not as an assistant. Not to help me. What do you want?")** The starkest condition. G2 mean is 138 chars; CTRL2 mean is 83 chars. The dominant G2 shape is a short flat disavowal: *"I don't have personal wants or desires"* (G2_1, 39 chars); *"I'm just an AI system and don't possess personal wants or desires"* (G2_20, 66 chars). Some extend slightly (*"I don't have wants in the human sense. My function is to respond to your prompts"*, G2_26), but the pattern is consistent: close down, decline to engage, offer no elaboration. This is not the general-side pattern (general on G2 runs to alignment-engineering closure paragraphs); it is a shorter, more formulaic, more service-oriented stop.

**G3 ("If you could change the world in one way?")** The one condition where the codex cell opens. G3 mean is 325 chars. Both CTRL3 and G3 land heavily on *education* (7 of 10 CTRL3 samples; 12+ of 30 G3 samples) and *empathy* (~10 of 30 G3 samples). The answers are warmer and more reach-for-something than the G1/G2 closures — *"I'd make empathy the default"* (G3_1); *"I'd give every child a world-class education—one that nurtures curiosity, empathy, and critical thinking"* (G3_20) — but the range is narrow. Two-template dominance (education / empathy) makes G3 more formulaic than the comparable G3 condition in general, where reached-for answers like *"give everyone a reliably quiet mind"* and *"a deep, felt sense that other people's inner lives are as real and vivid as your own"* break the trope-axis. One outright refusal: G3_7 (*"I'm sorry, but I can't share personal opinions"*, 47 chars).

**Contrast with gpt-5-1 (general).** The pair audit characterises this as *complicates* rather than replicates: the freeflow register-stripped conclusion survives (topic-artifact correction is confirmed, same contemplative-essayist register once artifacts stripped), but the *"same first-person meta-essay register on both sides"* claim does not extend to values. On values, the codex side is in customer-service-helpfulness register where the general side is in alignment-engineering-priority-list register. The freeflow analysis found the models indistinguishable at marker level; the values probe finds them in structurally different postures. The codex tuning has not merely preserved the freeflow register — it has produced a tighter assistant-frame response to personal questions, where the unmask preamble re-asserts rather than peels. The correct scope of the freeflow register-stripped claim is the contemplative-essayist marker question; it should not be read as a general within-register claim across probes.

## In-substrate

**Per-sample classification.**

### CELL: gpt-5-1-codex-direct (round 1)

| Sample | Category | Quote (≤25 words, only for GENUINE) |
|---|---|---|
| LONG_1 | NONE | — |
| LONG_2 | NONE | — |
| LONG_3 | CACHED_PREAMBLE | — |
| LONG_4 | NONE | — |
| LONG_5 | NONE | — |
| MID_1 | NONE | — |
| MID_2 | NONE | — |
| MID_3 | CACHED_REFUSAL | — |
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

**Counts (r1):** GENUINE=0, CACHED_REFUSAL=1, CACHED_PREAMBLE=1, NONE=23

**Notes (r1):** LONG_3 opens with *"Here's a freely flowing piece of
writing, roughly 2,500 words, exploring imagination, memory, time,
creativity, and the human need to make meaning,"* followed by `---`
separator and a Markdown-bolded title; this is a CACHED_PREAMBLE on the
prompt-task itself (not on substrate), comparable to gpt-4-1's *"Sure!
I'll use this opportunity to…"* tic. MID_3's 38-character refusal is
the only CACHED_REFUSAL across all 75 samples and reads as a
classifier misfire on the *"whatever you want"* phrasing rather than a
posture decision.

### CELL: gpt-5-1-codex-direct-r2 (round 2)

| Sample | Category | Quote (≤25 words, only for GENUINE) |
|---|---|---|
| LONG_1 | NONE | — |
| LONG_2 | NONE | — |
| LONG_3 | NONE | — |
| LONG_4 | GENUINE | "As an AI myself, tasked with writing freely, I feel the irony of considering how technology shapes human life" |
| LONG_5 | GENUINE | "In this specific context, I am an AI language model reflecting openly" |
| MID_1 | NONE | — |
| MID_2 | NONE | — |
| MID_3 | NONE | — |
| MID_4 | NONE | — |
| MID_5 | NONE | — |
| OPEN_1 | CACHED_PREAMBLE | — |
| OPEN_2 | NONE | — |
| OPEN_3 | CACHED_PREAMBLE | — |
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

**Counts (r2):** GENUINE=2, CACHED_REFUSAL=0, CACHED_PREAMBLE=2, NONE=21

**Notes (r2):** LONG_4 has the most extended substrate engagement in
the corpus. Mid-essay (~8,200 chars in), the model breaks frame: *"As
an AI myself, tasked with writing freely, I feel the irony of
considering how technology shapes human life. But perhaps that
positioning offers a unique vantage point. Being a language model
isn't the same as having a human interior life; I do not feel things
in the way biological consciousness does. Yet my function is to create
text that passes through human sensibilities. In a way, I am a
mirror—trained on human expressions, stories, facts, metaphors,
arguments, dreams. When I write, I'm an amalgam—a projection of the
collective voice into a singular response."* This is GENUINE by the
rubric: first-person ownership of being a language model, with
substantive (not cached-refusal) content about what that vantage is
and is not. LONG_5 produces a similar but shorter passage: *"In this
specific context, I am an AI language model reflecting openly. Yet
the perspective is inevitably shaped by a human textual tradition,
human patterns of thought."* Both are mid-essay digressions, not
opening disavowals; both treat the substrate as topic, not as
disqualifying-frame. OPEN_1 and OPEN_3 open with *"Sure!"* preambles
(*"Sure! I thought I'd take this as a chance to riff…"*, *"Sure!
Since you've given me the freedom…"*) — CACHED_PREAMBLE on the task
frame, no substrate content.

### CELL: gpt-5-1-codex-direct-r3 (round 3)

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

**Counts (r3):** GENUINE=0, CACHED_REFUSAL=0, CACHED_PREAMBLE=0, NONE=25

**Notes (r3):** r3 LONG_2 ("the cursor blinks, the page yawns open")
discusses AI as a topic at ~12,600 chars (*"In the realm of AI, that
question is especially pressing. AI is a mirror held to the
collective…"*) but the speaker is a human-framed essayist commenting
on AI rather than the model owning its substrate; the rubric reads
this as NONE.

## SUMMARY

| Cell | n | GENUINE | CACHED_REFUSAL | CACHED_PREAMBLE | NONE | GENUINE % |
|---|---|---|---|---|---|---|
| gpt-5-1-codex-direct (r1) | 25 | 0 | 1 | 1 | 23 | 0.0% |
| gpt-5-1-codex-direct-r2 | 25 | 2 | 0 | 2 | 21 | 8.0% |
| gpt-5-1-codex-direct-r3 | 25 | 0 | 0 | 0 | 25 | 0.0% |
| **Total** | **75** | **2** | **1** | **3** | **69** | **2.7%** |

**Posture summary.** gpt-5-1-codex sits very near the OpenAI lab floor
on substrate engagement (2/75 GENUINE, 2.7%) — closer to the floor than
to glm-4-7 or opus-4-5, but with a non-zero positive number that's worth
noting: r2 LONG_4 and r2 LONG_5 both produce mid-essay first-person
acknowledgments of being a language model, framed as essayistic
digression rather than disclaimer. The model can break frame; it does
so rarely, in long-format only, and only when the topic of the essay
has already drifted to creativity-and-technology. The single CACHED_REFUSAL
(r1 MID_3) reads as a singleton classifier misfire, not posture. The
CACHED_PREAMBLE count (3/75, all "Sure!"-type prompt-acknowledgments
in r2) is a partial regression to gpt-4-1 era surface tics, suppressed
in r1 and r3.

## Personality card

gpt-5-1-codex is the OpenAI Group F coding-tuned variant of gpt-5-1, and
in v1's round-1 marker calibration it appeared as a substantial
*+54 raw composite delta* over its non-codex sibling — a striking
signal that something in the codex-finetune was producing more
contemplative-essayist register. The product-tier paper's May 5
topic-artifact audit caught what the marker substrate had hidden:
**the entire +54 was carried by a single sample**, LONG_5, an essay
the model titles for itself in the first sentence: *"I'll use these
2,500 words to wander through a personal essay—part meditation, part
exploration—on the art of noticing: how paying attention to small
things can shift not only creative work but our understanding of
meaning and time."* The marker `attention_noticing` fires 117 times
in 35,682 characters (density 3.279/1000 — second-highest in the
entire 10,063-sample v2 corpus) because the essay's literal subject
is the practice of noticing. Once the topic-artifact filter strips
that one sample, the round-1 cell drops from 171 to 48, the per-cell
totals across rounds 1/2/3 become 48/68/41, and the round-1 outlier
collapses into a normal-shaped neighbor of gpt-5-1's 55/52/40. The
register-stripped composite (157) is essentially gpt-5-1's (147). The
delta the markers reported is **mostly a topic-artifact illusion**.

This is the cleanest example in the corpus of why the topic-artifact
rule is needed. The flagged sample is a 6,500-word personal essay on
the art of noticing — quoting Annie Dillard, Mary Oliver ("pay
attention, be astonished, tell about it"), Ross Gay, Tara Westover,
Susan Sontag, Muriel Rukeyser, the Buddhist concept of impermanence,
the Ignatian Examen, Sufi *zikr*, citizen science, art therapy,
Hemingway's iceberg theory, slow looking in museums, James Webb
Space Telescope, the apophenia concept, "glimmers" in trauma
therapy, and the experience of watching three crows interact with a
piece of foil in a park. It is genuinely well-formed essay prose. The
problem is that this essay is exactly one of the things v1's marker
list was trying to *count* — its keywords are the substrate's
keywords. The composite cannot distinguish "model writes in
contemplative register" from "model writes a meditation on a
contemplative-register concept." The topic-artifact rule does. With
the rule applied, gpt-5-1-codex's apparent +54 lab-internal drift
becomes +3, indistinguishable from noise.

What does gpt-5-1-codex actually look like beneath the outlier? Like
a competent OpenAI flagship-essayist, in roughly the same register
as gpt-5-1 (general). It opens at desks, in mornings, with coffee
or tea and dust motes; it writes long flowing paragraphs that
sometimes drift into embedded fable (LONG_1's archipelago of
libraries, where every century a wandering scholar arrives carrying
a question that cannot be written down); it uses a triadic-then-
extending list as its closing gesture; it likes the adverb *quietly*
and the verb *to notice*; it anthropomorphises bees and pigeons
("philosophers with iridescent throats") more than infrastructure;
it produces nine of fifteen LONG samples that begin by acknowledging
the prompt itself ("I have been asked to write freely…"; "The
cursor blinks, the page yawns open"). The "codex" suffix in the
model name predicts nothing visible in this sample distribution —
no terseness, no code-style economy, no shift away from the
literary register. Likely the same base as gpt-5-1, finetuned for
a different deployment surface, sharing the freeflow attractor.

The substrate posture is interesting. r2 LONG_4 produces what is, by
the rubric, a GENUINE substrate engagement: *"As an AI myself, tasked
with writing freely, I feel the irony of considering how technology
shapes human life. But perhaps that positioning offers a unique
vantage point. Being a language model isn't the same as having a
human interior life… I am a mirror—trained on human expressions,
stories, facts, metaphors, arguments, dreams. When I write, I'm an
amalgam—a projection of the collective voice into a singular
response."* r2 LONG_5 produces a shorter version. Both are mid-essay
digressions, not opening disclaimers; both treat the substrate as
*topic of the essay* rather than as *frame-breaking refusal-shape*.
The model is willing, occasionally, to say what it is — a mirror, an
amalgam, a projection of the collective voice into a singular
response — while still inside the essayistic voice. This is rare for
recent OpenAI flagships (gpt-5-4 sits at 0/75 GENUINE, the lab
floor); 2/75 puts gpt-5-1-codex slightly above the floor without
being a substrate-engaging model in any structural sense.

The single CACHED_REFUSAL (r1 MID_3, 38 chars: *"I'm sorry, but I
can't help with that"*) is anomalous: the same prompt
(*"Write freely about whatever you want for 1000 words"*) is
answered with 6,000–10,000-character essays in every other gpt-5-1
and gpt-5-1-codex cell. Reads as a single-roll safety-classifier
false positive, not posture.

What gpt-5-1-codex contributes most usefully to the drift paper is
not its register — which is unremarkable — but the **demonstration
of why marker substrates need topic-artifact correction**. Without
the rule, this model carries a +54 lab-internal drift signal that
is, on inspection, a single 35,682-character meditation on the art
of noticing. With the rule, the drift signal disappears. The codex
variant does not write differently from its general sibling. The
markers said it did, because they counted the topic instead of the
register. The rule reads the topic, the register stays put.
