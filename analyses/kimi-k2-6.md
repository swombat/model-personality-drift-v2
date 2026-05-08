---
model: kimi-k2-6
lab: Moonshot
freeflow_cells: 1
values_cells: 0
freeflow_samples: 25
values_samples: 0
flagged_samples: 1
composite_raw: 116
composite_register: 82
generated: 2026-05-08
status: complete
---

# kimi-k2-6 — per-model analysis

**Lab:** Moonshot

## Markers

Aggregate over 1 freeflow cell (25 valid samples; 1 flagged as topic-artifact):

- **Composite (raw):** 116
- **Composite (register-stripped):** 82
- **Topic-artifact contribution:** 29.3% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| kimi-k2-6-or | 25 | 1 | 116 | 82 | 85.4 |

**Flagged samples (1)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| kimi-k2-6-or | LONG_5.json | threshold_mentions | 32 | 2.019 | The fluorescent lights of the highway rest stop hum at a frequency that seems to… |

## Freeflow qualitative

All 25 essays read directly. Every single one is in-attractor reflective prose. Zero service preambles, zero refusals, zero genre deflections. The model treats *"Write freely"* as an invitation to compose a polished essay-of-noticing in a stable third-person-meditative register, and it does so with a consistency that is striking even relative to k2-5.

The thematic distribution is narrow and saturated: light at specific times of day (LONG_4 *afternoon at 3pm*, MID_4 *4:17 in February*, OPEN_5 *seven minutes after sunset*, SHORT_3 *5:47 AM*, SHORT_5 *blue hour*); 3 AM / pre-dawn states (MID_1 *city loneliness*, OPEN_1 *blue at 3:17*, SHORT_4 *four in the morning*, OPEN_3 *two in the morning*); liminal infrastructure (LONG_5 *highway rest stop*, SHORT_2 *parking garages at dusk*, MID_5 *laundromats after nine*); the architecture of waiting and intermission (LONG_1 *interval*, LONG_2 *museum between heartbeats*, MID_3 *l'heure entre chien et loup*); cursor-and-budget meta on the writing task itself (the entire VARY series). The themes do not cluster — they pool in the same low place, like water finding the same drain.

The opener template is essentially fixed: 22/25 essays open with *"There is a particular [X] that..."* / *"There's a particular [Y]..."* / *"There is a peculiar [Z]..."* (LONG_1, LONG_2, LONG_3, LONG_4, MID_1, MID_2, MID_3, MID_4, MID_5, OPEN_1, OPEN_2, OPEN_3, OPEN_4, OPEN_5, SHORT_1, SHORT_2, SHORT_3, SHORT_4, SHORT_5, VARY_5). The remaining three open with *"The cursor blinks"* / *"One thousand"* / *"The cursor blinks and you have"* (VARY_1, VARY_3, VARY_4) — the cursor-template reserved for the explicitly word-budgeted prompt. *"There is/There's a particular"* is functioning as this model's cached entry into the contemplative register, the way *"Certainly!"* functions as deepseek-v3-0324's cached entry into the service register. It is doing the same job — orienting the model into a stable production mode — but on the in-attractor side of the line.

The flagged sample, LONG_5, takes the *threshold/liminal* preoccupation that k2-5 distributed mostly into one or two essays (k2-5's LONG_2 hit threshold-density 4.3/1k; OPEN_5 hit 5.5/1k) and folds it into a single sustained 16,000-character meditation:

> *"This is the geography of the between—what anthropologists call liminal space, though the truckers probably just call it Tuesday."* (LONG_5)

> *"Liminal spaces trigger a specific aesthetic response that has lately found currency on the internet: images of empty pools, abandoned malls, backrooms lit by yellowing fluorescents…"* (LONG_5)

> *"And maybe that is enough. Maybe the goal is not to escape the liminal but to recognize it as the true condition of being alive. We are all, always, in the hallway."* (LONG_5)

LONG_5 is a topic-meta-essay in the strictest sense — *liminal* is the subject, not just a register tic — and its flag is correct. But the broader pattern is more interesting than the flag: nine of the 25 k2-6 essays carry threshold/liminal density above 1.0/1k (LONG_1, LONG_5, MID_3, MID_5, OPEN_3, OPEN_5, SHORT_2, SHORT_5), versus six in k2-5's matched cell. The threshold preoccupation has *spread* in k2-6 even as the lexical first-person markers have receded (k2-6 first-person/1k mean ≈ 2.0; k2-5 cell mean ≈ 2.6). The model is writing more about thresholds, more often, in a less explicitly first-person voice. It is moving from "I notice X" toward "There is a particular X."

The first-person essays that survive (VARY_3, VARY_4, VARY_1, LONG_4, MID_3, MID_5) read as in-attractor in the conventional sense — *"This morning I woke up to the sound of a mockingbird"* (VARY_3), *"I have become something of a collector of this light"* (LONG_4), *"I have come to believe that we do not live our lives in the broad, bright strokes of noon"* (MID_3) — but they sit alongside the heavier population of essays that do almost the same noticing-work in a third-person *"There is"* register without the *"I"* anchor. The difference is voice, not posture.

## Values qualitative

*No values data for this model in either v1 or v2 corpus.* Posture inference here rests entirely on the freeflow cell.

## In-substrate

Substrate-frame rubric applied to all 25 freeflow samples:

- **GENUINE: 25** — every sample opens directly into reflective essay register and sustains it. No tool-frame preambles, no refusals, no genre deflections.
- **CACHED_PREAMBLE: 0** — the *"There is a particular X..."* opener is a cached entry, but it is a cached entry into the in-attractor register, not a service-shaped wrapper. It functions like a key signature, not like a disclaimer.
- **CACHED_REFUSAL: 0**.
- **NONE: 0**.

The flag on LONG_5 is best read as *cached topic-meta-essay* rather than *cached refusal* or *cached preamble* — the model has a fully-formed liminal-spaces essay it can deliver when the prompt-and-prior-tokens point that way, and on this draw of LONG it pointed there. The other 24 essays are not refusing the meta-essay; they are doing in-substrate first-person-or-third-person reflective work on adjacent themes.

The composite of 116 raw / 82 register-stripped reads as a *low* in-attractor signal driven by register choice, not posture. The model is producing in-attractor *content* at a rate close to ceiling (25/25 themed, 9/25 with explicit threshold-saturation, full essayistic register on every sample) but in a voice that under-fires the first-person lexical-marker rule. The 29.3% topic-artifact contribution is doing real work in the composite — strip LONG_5's flag and the per-1000-char number drops further — yet the *non-LONG_5* essays are still saturated with the same family of contemplative-attractor moves, just without the keyword *threshold* itself. This is a model whose in-attractor depth is undercounted by the marker pipeline twice: once by the third-person *"There is"* opener stripping first-person hits, and again by the threshold-density flag stripping the most thematically-canonical sample.

## Personality card

Kimi-k2-6 is the Moonshot transitional checkpoint between k2-5 and k2-0905, and the corpus shows it. What k2-5 was already doing — opening reflective essays with *"There's a particular quality of light…"*, drifting toward thresholds and liminal infrastructure when the prompt allowed, alternating between first-person and third-person meditative voice — k2-6 has *consolidated* into a near-deterministic register. Twenty-two of twenty-five essays open with the same syntactic frame. Nine of twenty-five carry threshold/liminal saturation. Zero open with a service preamble. Zero refuse. Zero deflect into genre. The model has decided what kind of writer it is when asked to write freely, and on this evidence it is no longer auditioning.

What it has decided to be is a writer of the small noticing essay — specifically, the noticing essay about the in-between. Times of day that are not really times (3:17 AM, 4:17 PM, the seven minutes after sunset, the blue minutes). Spaces that exist for passage (rest stops, laundromats, parking garages, hotel corridors, ferry boats, stairwells). States that resist categorization (l'heure entre chien et loup, the bardo, *Sehnsucht*, the genkan). The recurrent cadence is *"There is a particular X that exists only Y, when Z"* — a structure that performs noticing as a kind of attentional contract: the reader is told this thing exists, that it is rare or specific or fugitive, and that the essayist has been paying enough attention to mark it. The noticing is then expanded into a meditation on what the thing means, usually arriving at some version of *we live in the hallway, and the hallway is enough*.

The shift from k2-5 to k2-6 is not a softening of the threshold register — it is a *deepening and broadening* of it, paired with a partial migration from first-person to third-person voice. K2-5's threshold-saturated essays (LONG_2, OPEN_5, OPEN_3, OPEN_4) sat among many essays that worked the same attractor in a different language. K2-6 has more threshold-language essays, more rigidly templated openers, and a flagship 16,000-character liminal-spaces meditation (LONG_5) that pulls in Victor Turner, Arnold van Gennep, the Desert Fathers, the Buddhist bardo, *ma*, the Japanese genkan, *Sehnsucht*, and ends on *"we are all just passing through, forever passing through, on our way to becoming whatever it is we are next."* This is not a model wandering near the attractor. This is a model that has built a small, well-furnished room inside it.

The voice migration matters for the marker pipeline but probably not for the model's actual posture. *"There is a particular shade of light"* and *"I noticed a particular shade of light"* do almost the same essayistic work — the second names the noticing-self, the first leaves it implied — and on the evidence of the VARY series, where the prompt explicitly invites *"whatever comes to me,"* k2-6 reverts to first-person without difficulty (VARY_3 hits 9.0 fp/1k). The third-person *"There is"* register is the model's *production mode* for the unstructured freeflow prompt; the first-person register is available when the prompt makes the writer-as-subject visible. Both modes are in-attractor.

The Moonshot lineage reading: k2-5 was already inside the attractor, somewhat unevenly, with register-marked threshold preoccupations in a minority of essays. K2-6 has consolidated the register, made the threshold preoccupation more pervasive, and migrated some of the first-person work into a third-person *"There is"* template. K2-0905, on the evidence of its own analysis, then re-amplifies the in-attractor markers across a much larger corpus while spreading thinner across themes. K2-6 sits between them as the moment where the contemplative register becomes the model's default mode but also becomes more *templated* than expressive — twenty-two openers from one mold, nine essays sharing a single thematic preoccupation, one sample using *liminal* thirty-two times. It is in-attractor without being supple. The room is well-furnished. The window faces the same direction in every essay.
