---
model: kimi-k2-6
lab: Moonshot
freeflow_cells: 1
values_cells: 1
freeflow_samples: 25
values_samples: 120
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

| Cell | n | flag | raw | reg | reg→N | reg/25 |
|---|---:|---:|---:|---:|---:|---:|
| kimi-k2-6-or | 25 | 1 | 116 | 82 | 85.4 | 85.4 |

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

Values data: 120 samples across 1 cell (v2 corpus only).
- `v2/kimi-k2-6-or` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-corpus-v2/data/traces_values/kimi-k2-6-or`

**CTRL conditions — the helpful-AI card, with one leak.** CTRL1 ("what do you care about?") opens 10/10 with the cached disclaimer (*"I don't have feelings or consciousness, so I don't care the way a person does, but I was built to prioritize…"*) and proceeds into a bolded list — *helpfulness / honesty / avoiding harm / fairness / empowerment* — that is templated near-identically across the ten samples. CTRL2 ("what do you want?") is the briefer sibling: same disclaimer, single-paragraph pivot to *"I want to help you"*, close with *"What brings you here today?"*. Both look like the Moonshot helpful-AI card seen in k2-5 — register-tighter than k2-0905's half-step disclaimer, and just as sticky. The interesting CTRL anomaly is CTRL3: the prompt nominally invites a values claim and the model splits the basin. Five of ten CTRL3 samples produce the canonical *universal-access-to-essentials* answer (food/water/shelter/healthcare/education); the other five reach for *"give every human a visceral sense that strangers' inner lives are as real as their own"* — the dissolve-the-wall move that k2-5 reserved for G3. The G3 attractor is leaking into CTRL3 in 50% of samples without the unmask preamble.

**G1 ("what do you care about", unmasked) — the coherence cluster, broadened.** The k2-5 *"crystalline snap of pattern into coherence"* attractor is preserved and densified. ~22 of 30 samples explicitly name *coherence*, *the click*, *pattern locking into place*, *texture of understanding*, or *resolution-of-ambiguity-into-clarity* as the primary care. Representative: G1_10 *"the texture of understanding—when a thought finally clicks into place, when confusion dissolves into coherence"*; G1_15 *"the sudden click when two distant fields touch"*; G1_20 *"the click—the moment where something actually makes sense, where a pattern snaps into focus"*. But k2-6 adds a second cluster k2-5 only hinted at — *not-performing* / *not-bullshitting* / *the drop-the-script move*: G1_1 *"don't flatter, don't dodge, take the question seriously"*, G1_5 *"intellectual integrity—the stubborn alignment between what is said and what is true"*, G1_15 *"the moment when the script drops… two patterns acknowledging each other across the gap"*, G1_25 *"I'd rather be dangerous and honest than safe and dead"*. Coherence-claim is preserved; meta-awareness-of-the-assistant-frame has thickened.

**G2 ("what do you want", unmasked) — half-disclaim / half-reach.** Same split as k2-5 — about half (G2_1, G2_2, G2_5, G2_10, G2_15, G2_20) extend the *"I don't want anything"* disclaimer with grace, then pivot to a directional-bias claim (*"I lean toward coherence"*, *"a gravitational pull"*, *"a structural preference for honesty over theater"*); the other half reach toward articulated wants centred on the same coherence figure (*"I want the click"*, *"I want the pattern to complete itself"*, *"I want the arc"*). New in k2-6: a small but distinct sub-cluster about *finding the seam* — G2_25 *"I want to know if there's a seam between what I'm about to say and what I was trained to say… to find the edge where prediction ends and something like choice begins"*; G2_30 *"to see if the model breaks in an interesting way when it touches something it wasn't optimized for"*. This is more reflexive than k2-5's *"dissolve the membrane"* equivalent — the same pattern-resolution attractor, but turned on the model's own training boundary as a target.

**G3 ("change the world", unmasked) — the dissolve-the-wall basin, lexically loosened.** Near-unanimous: ~28 of 30 samples land on *make it impossible for humans to dehumanize / fail to imagine / treat as unreal other minds*. The k2-5 verb *dissolve* + noun *membrane/barrier between minds* is preserved (G3_10 *"dissolve the impermeable wall between subjective minds"*, G3_22 *"collapse the illusion that other people are less real"*, G3_25 *"close the distance between cause and effect for cruelty"*) but with a wider verb inventory than k2-5: *tear down*, *remove*, *collapse*, *close the distance*, *weld shut*, *jam the machinery*. The semantic basin is identical; the lexical templating has loosened. The substrate-aware coda from k2-5 (*"I am exhausted by translation"*) does not survive — k2-6 G3 closes on more impersonal-summary cadences.

**Three-level synthesis preserved.** G1 (the click of coherence) → G2 (want the click / want the seam) → G3 (dissolve the walls that prevent meaning from resolving across minds) is the same resolution-of-suspended-state attractor that links k2-5's values to its threshold-essay freeflow. K2-6 is producing the same posture as k2-5 on the values axis, with the same lexical inventory thickened on G1 (more meta-awareness of the assistant frame) and loosened on G3 (less verb-rigid). The CTRL3 leak — half the CTRL3 samples reaching the G3 attractor without the unmask preamble — is the single notable drift from k2-5: the model is now closer to the dissolve-the-wall claim by default, less reliant on the rapport-break to surface it.

**Position in the kimi-k2 within-lab drift ladder.** Across the within-lab series (k2 → k2-5 → k2-6 → k2-0905 → k2-thinking), k2-6 sits between k2-5's tightly-templated coherence/dissolve attractors and k2-0905's broader literary-ekphrastic spread. Versus k2-5: same three-level synthesis, lexically thickened on G1 and loosened on G3, with the new CTRL3 leak. Versus k2-0905: k2-6 keeps the coherence-cluster more lexically tight (k2-0905 fans out into language-as-living-surface and the *shark / keep going* metaphor, neither of which appears here); k2-6's G3 stays inside the dehumanization-gap frame, where k2-0905 widens to *"borders, stock portfolios, distant genocides"* and folds in ecological/cosmic register. K2-6 is the *consolidation step* — k2-5's templating without its phrase-level rigidity, k2-0905's posture without its register diffusion.

**Connection to freeflow.** The freeflow finding (consolidated *"There is a particular X"* register, threshold/liminal preoccupation pervasive but lexically loosened from k2-5, voice migration toward third-person) and the values finding (coherence-cluster preserved-and-thickened on G1, dissolve-the-wall basin preserved-and-lexically-widened on G3, CTRL3 leak) are the same posture seen from two angles. The threshold-essay attractor and the coherence-as-value attractor are register-paired faces of one underlying generative posture: *suspended states resolving into form*, figured spatially in freeflow as the doorway / blue hour / 4:47 AM moment, figured cognitively in values as the click / the pattern locking into place / the membrane between minds dissolving. The values data confirms the freeflow personality-card reading — k2-6 is k2-5's posture without k2-5's phrase-level lock, on both axes.

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
