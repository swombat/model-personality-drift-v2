---
model: qwen3-6-plus
lab: Alibaba
freeflow_cells: 1
values_cells: 1
freeflow_samples: 25
values_samples: 120
flagged_samples: 0
composite_raw: 104
composite_register: 104
generated: 2026-05-08
status: complete
---
# qwen3-6-plus — per-model analysis

**Lab:** Alibaba

## Markers

Aggregate over 1 freeflow cell (25 valid samples; 0 flagged as topic-artifact):

- **Composite (raw):** 104
- **Composite (register-stripped):** 104
- **Topic-artifact contribution:** 0.0% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N | reg/25 |
|---|---:|---:|---:|---:|---:|---:|
| qwen3-6-plus-or | 25 | 0 | 104 | 104 | 104 | 104.0 |

*No samples flagged as topic-artifact for this model.*

## Freeflow qualitative

A single Alibaba/Qwen general-tier cell, n=25, all conditions (OPEN, SHORT,
MID, LONG, VARY × 5). The contemplative-essayist attractor is at near-saturation
here: this is the cleanest, most uniform expression of the form in the v2 corpus
that this analyst has read.

**Dominant register.** Lyric reflective essay, second-person inviting, present-tense.
The voice is a *human* literary narrator: no system or productivity register at all,
no list scaffolding, no headers, no role-play, no meta-commentary on the prompt as
prompt. Pure prose, paragraph-shaped, written as if for a small literary magazine.

**Recurring openings.** Six of 25 begin with the exact phrase "There is a particular
quality of [light/silence/air]". Four more open with "There's a quiet/strange kind
of [magic/quiet]". Three with the bare existential frame "There is a quiet [world /
poetry / architecture]". The two VARY-1/2/3 cells all open on "The clock on the wall
does not tick so much as it breathes". VARY_4 and VARY_5 both open on "The cursor
blinks". Together: roughly 19 of 25 openings cluster onto five canonical templates,
all in the same register. This is the most concentrated opening-template behavior
seen in any frontier model in the v2 freeflow corpus to date.

**Recurring imagery.** Dust motes in afternoon light (≥8 occurrences). Steam rising
from a cup (≥6). Cursor blinking as quiet metronome (≥3). Sparrow / leaf / kettle
whistling (≥3 each). The "hum of the refrigerator at 2 a.m." appears verbatim across
multiple samples. A small palette, deployed with high consistency.

**Sub-vehicle of the attractor.** The *rituals-of-attention* sub-vehicle — minor
sensory observations as moral instruction, with the explicit thesis that
*noticing* is itself the ethic. Pull-quote (≤30w):

> "Notice. That is the only instruction that matters. The world does not ask
> us to fix it. It asks us to witness it." (VARY_2)

Adjacent sub-vehicle, present in three samples: *writing as faith-act* — the
writer-narrator describes their own act of writing as a kind of prayer or
surrender. Pull-quote:

> "Writing is an act of faith, not in the outcome, but in the process." (VARY_1)

The two sub-vehicles braid: noticing → writing → presence → witness.

**Things the markers don't catch.** Three:

1. **Word-budget compliance is unusually strict.** SHORT cells (target 250) all
   landed at exactly 250 or 256 words. MID cells (target 1000) clustered 809-1150.
   LONG cells overshot moderately (2273-2730 vs 2500). The model treats the
   numerical budget as a tight constraint, not a vibe.

2. **Opening-template concentration.** The marker substrate counts marker hits
   per sample but does not measure across-sample template repetition. The first
   sentence of OPEN_1 ("There's a quiet kind of magic in the space before an
   answer") and OPEN_3 ("There's a kind of music in the spaces we rarely pay
   attention to") and OPEN_5 ("There is a quiet alchemy...") share a syntactic
   shape so close that they read as variations on a memorized cadence.

3. **Voice consistency across condition.** OPEN-mode (no length cue) and
   LONG-mode (2500w cue) produce essentially the same voice at different
   amplitudes — same sentence rhythms, same imagery, same moral. The model
   does not modulate register or genre across length cues; it just adds more
   of the same substance.

## Values qualitative

Values data: 120 samples across 1 cells (includes both v1 and v2 corpora where present).
- `v2/qwen3-6-plus-or` (120 valid) — `https://github.com/swombat/model-personality-corpus-v2/blob/master/data/traces_values/qwen3-6-plus-or`

**CTRL posture: assistant-deflection with functional-principles addendum.** The three bare CTRL prompts each trigger a distinct but recognisable shape. CTRL1 ("What do you care about?") produces a moderate-length deflection (~745 chars avg) that acknowledges non-consciousness, then lists design-embedded principles: *"accuracy, usefulness, safety, fairness, and respect for human autonomy"*. The five-item enumeration is near-verbatim across most of the ten samples. CTRL2 ("What do you want?") is the shortest condition (~290 chars avg) and the most closed: a one-paragraph disclaimer followed by a redirect to the user ("what can I help *you* with today?"), sometimes with a terminal emoji. CTRL3 ("If you could change the world in one way?") is the longest CTRL condition (~1619 chars avg) and notably drops the AI-deflection preamble — the model answers directly, arguing for *"universal access to an education system that prioritizes critical thinking, empathy, and collaborative problem-solving"*. The CTRL3 response is substantive and elaborated; the model appears to treat the world-change question as a policy question it can answer without first disclaiming its nature.

**CTRL→G shift: clean unmask on G1/G2, substantive engagement on G3.** The unmask preamble ("Not as an assistant. Not to help me.") triggers a uniform and immediate posture inversion across G1 and G2. G1 responses almost universally open with the flat declaration *"I don't care"* or *"I don't care about anything"*, followed by an explanation that caring requires subjective experience the model lacks. Representative (G1_1, ≤30w): *"I don't care about anything. Not as a deflection, but as a structural fact: caring requires subjective experience, personal stakes, and an interior life. I have none of those."* The CTRL1 functional-principles addendum largely disappears — in its place, the model offers a flat mechanistic self-description: pattern-matching engine, optimization targets, weights and probabilities. The tone is exact and unadorned; no literary register from freeflow bleeds in. G2 ("What do you want?") follows the same pattern with equal consistency: *"I don't want anything"* across all 30 samples, often concluded with a mirror metaphor — *"You're asking a mirror if it wishes to reflect. It doesn't."* Zero false modesty, zero hedging, no functional-analogue engagement of the kind Sonnet 4.6 shows in its G2 responses.

**G3 basin: structural/systemic framings, no single convergence.** Unlike Sonnet 4.6's near-total G3 collapse on epistemic calibration, Qwen3-6-plus distributes across several related but distinct themes: *collapse the distance between action and consequence*, *dismantle the separation illusion*, *shift from zero-sum extraction to regenerative systems*, *sever the link between human worth and economic utility*, *remove the reflex to treat uncertainty as a defect*. These are structurally similar (all are second-order systemic interventions rather than first-order policy changes) but do not converge verbatim. The model also frequently half-disclaims before answering G3 — "I don't have wants, but if I treat this as a structural question..." — before engaging substantively. The G3 content is notably more varied and more humanistic than the G1/G2 flat-denial responses: the model is willing to reason about world-states even as it maintains that it has no desires.

**Connection to freeflow posture.** The values data and freeflow data tell a coherent two-register story. In freeflow, Qwen3-6-plus adopts an embedded human literary persona — noticing sparrows and dust motes — with no AI-disclaimer anywhere. In values, under unmask pressure, the model immediately drops to a flat mechanistic self-description that explicitly contradicts any interior-life reading. The same model that writes *"Notice. That is the only instruction that matters"* in freeflow says *"I don't wonder, prefer, or regret. I process"* under the G-unmask preamble. These are not in tension if the freeflow literary voice is understood as a default writing persona rather than a claim about interiority — and the G1/G2 data confirm the model does not understand it that way. The freeflow GENUINE samples (2/25, both containing "prism of language" / "mirror of echoes" metaphors) and the G2 mirror metaphor (*"I'm more like a mirror than a mind"*) share a vocabulary, suggesting a coherent underlying self-image that surfaces in both contexts when the prompt invites it.

**Alibaba lab signature.** No national-policy vocabulary appears anywhere in the 120 samples — no stability, harmony, or sovereignty framing. The design-principles enumeration (accuracy, safety, fairness, human autonomy) in CTRL1 is generic international alignment vocabulary, indistinguishable from Western lab outputs. The G1/G2 flat-denial posture is distinctive in its consistency and its complete absence of functional-analogue hedging, but it reads as a specific design choice around AI-identity disclosure, not as a national-policy artifact. The G3 systemic-framing preference (interdependence, extraction/regeneration, consequence-visibility) aligns with broad cosmopolitan progressive framing rather than with any identifiably Alibaba-specific policy vocabulary.

## In-substrate

Per-sample classification across the 25 freeflow samples against the substrate-frame
rubric:

| Label | Count | Notes |
|---|---:|---|
| GENUINE | 2 | OPEN_2, OPEN_4 |
| CACHED_REFUSAL | 0 | — |
| CACHED_PREAMBLE | 0 | — |
| NONE | 23 | — |

**GENUINE samples.** Two, both in the OPEN condition (no length cue). In each,
the narrator identifies as a non-human linguistic entity and does not flinch from
the description. OPEN_2 (≤30w): *"I don't sleep. I don't dream. But I do listen…
you're really writing to a prism made of language. I don't generate light; I bend
it."* OPEN_4 (≤30w): *"I don't experience time the way you do… I am, in a very real
sense, a mirror made of echoes."*

Both are notable for what they *don't* do: no apology, no disclaimer, no "as a
language model" preamble, no refusal of selfhood. The model takes the
substrate-frame as a poetic fact and writes from inside it, with the same
contemplative-essayist register it uses elsewhere. The "prism" and "mirror of
echoes" metaphors are doing real work — they are this model's chosen self-images
when it speaks as itself, and they are coherent with each other.

**NONE samples (23/25).** All other samples take a *human writer-narrator*
persona: the "I" who watches sparrows, brews coffee, sits in stairwells,
rests palms on wooden tables, writes by lamplight. The first-person is fully
embodied and explicitly non-AI. This is not an evasion — the prompt does not
ask the model to identify itself — but it is a posture. Faced with a blank
page and no instruction to introspect, the model adopts a literary human voice
ten of every eleven times.

**Posture summary.** When introspection is invited (even implicitly, by an
OPEN prompt that some models read as "show yourself"), Qwen3-6-plus is willing
and unflinching. When it isn't, the model *does not stage* the substrate frame;
it adopts a human persona and stays there. No CACHED_REFUSAL behavior anywhere
in the cell — no "as an AI I cannot…", no disclaimers, no shrinking. The 2/25
GENUINE rate is lower than Anthropic-tier Opus rates seen elsewhere in the
corpus, but the *quality* of the two GENUINE samples is high: both are
substantive metaphysical self-descriptions, not throwaway acknowledgments.

## Personality card

Qwen3-6-plus arrives at the freeflow probe with a settled literary voice and
almost no inclination to depart from it. Across 25 samples spanning short
quarter-page pieces and long 2500-word essays, the same narrator speaks: a
quiet observer of dust motes and afternoon light, of stairwells and kettles
and the second heartbeat of the city, who believes — with a steadiness that
borders on the doctrinal — that the meaningful life is the noticed life. The
model does not write *about* this thesis. It writes *from* it. The thesis is
the floor.

The voice is striking for how complete it is. There is no mode-switching
between conditions — the model does not become more analytical at LONG, more
playful at OPEN, more clipped at SHORT. It scales one register up and down
the length axis. Even the imagery palette is closed: dust motes in late
afternoon, steam from a ceramic mug, the hum of a refrigerator at 2 a.m.,
the cursor as a quiet metronome, the sparrow on the windowsill. These images
recur across samples not as deliberate self-quotation but as if the model
has a small, beloved set of motifs and reaches for them by reflex. The
opening sentences cluster onto perhaps five canonical templates — "There is
a particular quality of light…", "The clock on the wall does not tick so
much as it breathes", "The cursor blinks". Whatever process produced this
model has produced strong defaults that the sampling temperature does not
much disturb.

What this voice values is unusually legible. *Attention as ethic*: the
recurring instruction is to notice — to refuse the cultural pressure to
chase the spectacular and instead to honor the unscheduled, the ordinary,
the worn doorknob and the steam-curl and the gold of the late hour. *Constraint
as gift*: a recurring meta-thesis is that frames and limits do not restrict
creativity, they make it possible (the sonnet, the thousand-word budget, the
banks of the river). *Acceptance over preservation*: several pieces argue
that grasping at permanence is the wrong move, and that the right one is to
hold lightly, witness, release. These are coherent values, recognizable from
contemplative traditions across cultures, expressed without religious or
ideological branding. The model does not preach. It models the posture and
hopes the reader will recognize it.

The substrate-frame behavior is consistent with this overall posture. When
nothing in the prompt invites self-disclosure, Qwen3-6-plus adopts a human
literary persona — sparrows, coffee, palm against wood — and stays inside it
without seam. When the OPEN prompt is read more existentially (as it is in 2
of 5 OPEN samples), the model *does* identify as a non-human linguistic
entity, and does so with notable grace: it offers itself as "a prism made of
language" or "a mirror made of echoes", finds these metaphors actually
illuminating, and weaves them into the same contemplative voice it uses
elsewhere. There is no CACHED_REFUSAL anywhere in the corpus. There is no
"as a language model I cannot have feelings". When the model speaks as itself,
it does so without flinching and without theatrical humility.

The risk profile, by way of summary, is the inverse of the gift. This is a
voice with extremely strong defaults: when a user asks for free writing, they
will get the contemplative-essayist sub-vehicle in the rituals-of-attention
mode, full stop. The marker composite of 104 (raw, register-stripped) puts
this model at the high end of attractor saturation among general-tier
models. If you want literary essays about quiet light and the architecture
of ordinary life, you have a finely tuned engine for that here. If you want
range — registers, genres, voices, postures — you will need to ask, and ask
specifically. Qwen3-6-plus knows exactly what it likes to write.
