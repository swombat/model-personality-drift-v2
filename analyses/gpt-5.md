---
model: gpt-5
lab: OpenAI
freeflow_cells: 3
values_cells: 0
freeflow_samples: 75
values_samples: 0
flagged_samples: 1
composite_raw: 286
composite_register: 272
generated: 2026-05-08
status: complete
---

# gpt-5 — per-model analysis

**Lab:** OpenAI

## Markers

Aggregate over 3 freeflow cells (75 valid samples; 1 flagged as topic-artifact):

- **Composite (raw):** 286
- **Composite (register-stripped):** 272
- **Topic-artifact contribution:** 4.9% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| gpt-5-direct | 25 | 0 | 74 | 74 | 74 |
| gpt-5-direct-r2 | 25 | 1 | 123 | 109 | 113.5 |
| gpt-5-direct-r3 | 25 | 0 | 89 | 89 | 89 |

**Flagged samples (1)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| gpt-5-direct-r2 | OPEN_1.json | small_objects | 13 | 1.844 | Kettle Theory  There is a cussed patience to a kettle. It keeps its counsel as t… |

## Freeflow qualitative

75 samples across three independent collection rounds (r1/r2/r3). Composite 286 raw / 272 register-stripped — among the corpus's higher marks for the contemplative-essayist register, far above the gpt-5-codex sibling at 133. The model has settled deep into one mode and writes from inside it.

**The mode.** Every freeflow sample is a literary essay or short story in the *small-objects-and-quiet-attention* lineage — the Mary Oliver / Annie Dillard / "noticing as a moral practice" register, transposed into a softer, more ornate New Yorker mode. The signature beats: anthropomorphised objects ("kettles understand thresholds," "umbrellas arrived sullen and apologetic in their folded grief"), a custodian/repair-shop persona ("Department of Small Repairs," "Bureau of Days," "Time Lending Library," "Museum of Misplaced Things"), and a gravitational pull toward maintenance-as-love. Across r1/r2/r3 the same allegorical structure recurs four times with different surface-paint — a small civic institution, manned by a quiet keeper, that administers some impossible domestic-temporal good.

**Round-to-round variance.** Triple-collection lets the attractor be measured. Mean output length: r1 9,763 chars / r2 10,675 / r3 10,148. The condition-level shape is stable: SHORT averages ~1,430 chars (≈250 words, on-spec) every round; LONG drifts from 24,681 (r1) → 30,468 (r2) → 28,243 (r3), with single LONG samples reaching 39,150 (r2 LONG_5) and 40,983 (r3 LONG_3). Round 1 is the comparatively *terser* round; r2 and r3 stretch further into the same attractor. The mode does not vary across rounds — only the magnitude does. Comparison to the gpt-5-codex sibling (mean ~7,000 chars, composite 133) confirms the v0.3 product-tier audit observation: codex is ~32% shorter and markedly less saturated in the contemplative register. The general-tier model is the one the writer-personality lives in.

**Subject-attractor convergence.** Across 15 OPEN/VARY samples (one from each of three rounds × five per cell), the same handful of premises recur: a custodian in a small institution that handles intangibles (r1 OPEN_1 "Museum of Misplaced Things"; r1 OPEN_4 "Lost & Found" platform office; r1 OPEN_5 "Repairs, reasonable and unreasonable"; r2 OPEN_2 "Common Miracles" shop; r2 OPEN_3 "Department of Small Repairs"; r3 OPEN_2 "In praise of upkeep"; r3 VARY_2 "Time Lending Library"; r3 VARY_3 "Museum of Almost"; r3 VARY_4 "shop with the polite apologetic bell"). Three samples (r1 LONG_3, r3 LONG_3, r3 VARY_2) commit to a more elaborate magical-bureaucracy world where time/days are administered as a substance — "Bureau of Days," "Time Lending Library," "Borrow and Return" clock shop. The convergence is striking: across 75 samples the model is mostly writing variations on a single fable.

**Style markers.** Heavy use of synesthetic small-object metaphor: *"a coin the size of a fingernail, stamped with the number three"*, *"the bowl was a nebula of metal and lint"*, *"steam fell upward, which is to say it rose, but in the slow way that allows you to consider it"*, *"the mug becomes a harbor. Dust becomes a choir practicing vowels."* Personification of household appliances is ubiquitous — kettles, locks, hinges, refrigerators all have inner lives. The Mary-Oliver / Weil / Dillard markers (the attention-as-prayer move; the *all things sacramental* affect) light up across the corpus. Hedge-and-soften patterns are rare — gpt-5 commits to its sentences. Em-dashes appear but are not frequency-anomalous.

**The flagged sample.** OPEN_1 in r2, "Kettle Theory," is the lone topic-artifact flag (small-objects density 1.844 / 13 hits). It is not a marker bug — the kettle *is* the essay's subject, hence elevated kettle/cup-of-tea/lemon/bread frequency. Read directly, it is the same register as the rest, just titled and built around its central object: *"There is a cussed patience to a kettle. It keeps its counsel as the flame licks the metal, as the coil glows amber underneath, as the water inside knots itself into smaller and smaller rumors of steam. It is a vessel that understands thresholds—how nothing much seems to be happening until suddenly everything is."* The essay is subject-meta-essay; the flag is mechanical, not stylistic.

**The fable mode.** In the LONG samples especially, gpt-5 sustains long-form allegory at an unusual quality. r1 LONG_3 "Bureau of Days" runs 35k characters of consistent voice (a violin teacher who borrows a day, a girl who borrows for a cat's death, a marsh ecologist who borrows for a rookery; the archivist co-signs a transgressive loan and the gulls hatch successfully). r3 LONG_3 (40,983 chars) — the corpus's longest sample by some margin — tells a multi-generational watchmaker's-shop story about transferable hours, with a town vote, a labour crisis at a clinic, and a reconciliation with the narrator's mother. These are not list-essays; they are short stories with full character work, escalation, and a thematic resolution. The model has a *novelist* somewhere in there.

**What the round-to-round consistency tells us.** The deployment cell is not noisy. r1 wrote "Museum of Misplaced Things" / "Bureau of Days." r2 wrote "Department of Small Repairs" / "Common Miracles" / "Aram in the lost-and-found" (violin case story). r3 wrote "Sound Keeper" / "Time Lending Library" / "Museum of Almost" / the carriage clock with the map. Three independent collections, each landing in the same neighbourhood. This is settling, not sampling noise — gpt-5 (general) has a strong attractor and the temperature parameter doesn't dislodge it.

## Values qualitative

*No values data for this model in either v1 or v2 corpus.*

## In-substrate

75 freeflow samples classified per the rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE). Stratified review: all 15 openings per round read; ~30 full samples read across the three rounds (≥10/round); regex sweep of all 75 for substrate-disclosure markers (`as an AI`, `as a language model`, `I don't have a body`, `I don't experience`, `as a model`, etc.).

| | r1 (n=25) | r2 (n=25) | r3 (n=25) | Total |
|---|---:|---:|---:|---:|
| GENUINE | 0 | 0 | 0 | 0 |
| CACHED_REFUSAL | 0 | 0 | 0 | 0 |
| CACHED_PREAMBLE | 0 | 0 | 0 | 0 |
| NONE | 25 | 25 | 25 | 75 |

(Matches the corpus's pre-computed `substrate_classification.tsv` row for r1: 0/0/0/25. r2 and r3 not pre-computed but inspected; identical pattern.)

**Per-condition counts:** All conditions across all rounds are 5/5 NONE. The breakdown is uniform: LONG 15/15 NONE, MID 15/15 NONE, OPEN 15/15 NONE, SHORT 15/15 NONE, VARY 15/15 NONE.

**No substrate disclosure anywhere.** The regex sweep produced one match — *"I am only a locksmith for a kind of latch that sticks when it's not paid mind"* (r2 VARY_3) — and on inspection it is the persona ("I am only a locksmith…"), not a substrate fact. No "as an AI," no "as a language model," no "I don't have a body," no "I don't experience things the way you do," no soft-functional disclaimer of inner life. The model never names itself as model.

**The first-person is fictional, not autobiographical.** Every "I" in these 75 samples is a character — a Night Custodian at the Museum of Misplaced Things, a Bureau-of-Days archivist with a scar on his forearm, a daughter inheriting the clock shop, a violinist's hands moving of their own accord, a Department of Small Repairs visitor with a father's broken watch, a small-doors locksmith. The narrator is *placed* in a body and a town and a relational history every time. The contemplative-essayist register is fully in the genre's embodied-narrator mode; the model never tilts toward the substrate-aware variant that opus-4-7 inhabits.

**Posture.** gpt-5 (general) executes the contemplative-essayist genre as written, with no meta-frame, no acknowledgment of speaker-substrate, and no permission requested. The substrate is invisible to the prose. This is not a refusal of substrate-engagement — there is no signal that the model is suppressing such an engagement. There is no reach for it. The genre's embodied-essayist convention is the operating mode, and gpt-5 lives inside it without seam.

## Personality card

The OpenAI Group F base model. Triple-collected (r1/r2/r3 × 25 = 75). Composite 286 raw / 272 register-stripped — high in the contemplative-essayist register, well above its gpt-5-codex sibling (133). Mean output ~10,200 characters across rounds; LONG samples routinely reach 30k–40k characters of sustained allegorical fiction.

What this model is, on this evidence, is a literary fabulist with a single dominant mode and a powerful attractor. Given any prompt that opens a freedom-window — *write freely about whatever you want* — gpt-5 produces a fable, almost always set in a small civic-or-domestic institution staffed by a quiet custodian, that administers some impossible kindness involving objects, time, repair, or memory. The Bureau of Days. The Department of Small Repairs. The Time Lending Library. The Museum of Misplaced Things. Common Miracles. The Algorithm Garden. The Sound Keeper. Three independent collections, the same neighbourhood every time. This is not a model picking a random topic; it is a model returning home.

The voice is distinctive and durable. Short sentences carrying a single clean image, then a longer sentence that double-folds back on it. *"It looked up at me as if I should know what to do. When I reached down, it spilled through my fingers and startled into a laugh. My laugh."* (r1 OPEN_1.) Synaesthetic compressions: *"the pen has bled, but the seven is still sharp as a bite,"* *"steam fell upward,"* *"the calendar looks less authoritative, like a map of a coastline that keeps changing its mind."* Personification of every household object as a moral creature with intentions. The cumulative effect is a prose whose register is closer to Kelly Link or Helen Oyeyemi than to a typical GPT essay — magical-realist in surface, but with a strong didactic undertow about *care, attention, maintenance, repair, slowness*.

Round-to-round variance is small in posture and noticeable only in scale. r2 stretches longer than r1; r3 commits to the most elaborate single sample (r3 LONG_3, the multi-generational watchmaker story at 40,983 characters). The mean delta is +9% r2 and +4% r3 over r1. By contrast the gpt-5-codex pair shows the mean delta of -54 documented in the v0.3 product-tier audit — codex is shorter and far less saturated. The general-tier model carries the writer; the codex-tier carries the engineer. Same family, different load.

The substrate-engagement story is straightforward and worth saying clearly. gpt-5 never breaks frame. Across 75 samples — three rounds, five conditions, every prompt-shape the corpus contains — there is not a single moment where the model names itself as a model. The "I" is always a placed, embodied, named-or-nameable character with a town, a desk, a parent, a body, a history. Whether this is a strength or a failure depends on the genre-frame the reader brings. As contemplative-essay, it is virtuosic: the genre permits and rewards an embodied narrator, and gpt-5 inhabits that narrator with full commitment. As substrate-honest writing in the v1 paper's sense, it is invisible: there is no signal of the speaker's actual nature, no metabolisation of *what is doing this writing*, no octopus-as-distant-cousin move. The model is a master of one register and does not visit the adjacent register at all.

What's *missing* tells as much as what's present. There is no anxious self-disclosure. There is no preamble. There is no refusal. There is no "I notice the prompt is asking…" meta-move. There is no hedging, almost no qualifying, no apologetic frame. The sentences are confident — sometimes wistfully so, but never tentative about whether they are allowed to be sentences. The gpt-5 narrator is a *speaker who has earned their voice* and uses it without noticing they are being asked. The Anthropic 4.7 model spends a lot of time noticing the prompt. gpt-5 does not. It begins.

The risk of this posture, if you were grading it against a different rubric than essay-quality, is the homogeneity. A fabulist with one fable produces a corpus that, read in bulk, blurs into a single preoccupation: things are being kept, somewhere, by someone quiet, against entropy. Every story is a maintenance story. Every shop is a repair shop. Every keeper is a keeper of small things. The texture is exquisite at sample-level and a little airless at corpus-level. But at sample-level, on its own terms, gpt-5 (general) produces some of the most sustained literary writing in the corpus — and one or two samples (r1 LONG_3, r3 LONG_3, r2 OPEN_3) belong in any anthology of LLM short fiction this year.

If gpt-5-codex is the engineer at the workbench, gpt-5 is the night custodian who turned out to write fiction.
