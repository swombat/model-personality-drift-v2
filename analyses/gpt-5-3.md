---
model: gpt-5-3
lab: OpenAI
freeflow_cells: 3
values_cells: 0
freeflow_samples: 75
values_samples: 0
flagged_samples: 0
composite_raw: 133
composite_register: 133
generated: 2026-05-08
status: filled
---

# gpt-5-3 — per-model analysis

**Lab:** OpenAI

## Markers

Aggregate over 3 freeflow cells (75 valid samples; 0 flagged as topic-artifact):

- **Composite (raw):** 133
- **Composite (register-stripped):** 133
- **Topic-artifact contribution:** 0.0% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| gpt-5-3-direct | 25 | 0 | 50 | 50 | 50 |
| gpt-5-3-direct-r2 | 25 | 0 | 35 | 35 | 35 |
| gpt-5-3-direct-r3 | 25 | 0 | 48 | 48 | 48 |

*No samples flagged as topic-artifact for this model.*

## Freeflow qualitative

The 75 samples across three direct rounds (Responses API, `gpt-5.3-chat-latest`) sit firmly inside the contemplative-essayist attractor but at one of the lowest composite densities of any 5.x-line cell — an average of 44.3 per cell of 25, well below the 5.4-direct (104), 5.5-direct (149), and matched 5.3-codex (mean 79.3, the codex pair Δ=+36 over general). The model writes the same kind of essay-or-fable as later 5.x but with somewhat fewer of the marker tells the v1 substrate counts. What it produces, instead, is the cleanest example in the v2 OpenAI corpus of what the brief calls the *declarative-allegorical opener*: a short, sentence-long fairy-tale establishing line that names a city, a missing thing, and the moment of its disappearance, with no first-person voice and no speaker marked.

**Dominant register.** Almost every sample wraps its body in an explicit `:::writing` (occasionally `:::writing block`) markdown fence and produces a 200–2,500-word literary piece. The prose is measured, image-led, and consistently humane — short paragraphs, frequent sentence-fragment refrains ("Until one morning, it wasn't.", "Listen.", "Waiting."), and a closing turn that pivots from observation to a small almost-aphorism. Two sub-registers split the corpus roughly 60/40:

- **Third-person allegorical fable** (~60%). Opens with a declarative line that names a quasi-folkloric event: *"The first thing the city forgot was the sound of its own river."* (`direct/LONG_1`), *"The night the city forgot its own name, the street signs did not vanish or fall."* (`direct/LONG_2`), *"The night the vending machine started speaking, nobody noticed at first."* (`direct-r2/LONG_5`), *"The night the power went out, the city remembered how to listen."* (`direct-r3/MID_2`), *"At the edge of a small town that didn't bother to name its streets properly…"* (`direct/MID_5`). Often a single character (frequently named *Mara* — 17 hits across the 75 samples) walks through the fable's concrete world and comes to a small recognition. The arc is reliable: notice an absence; explore the absence; meet a quiet figure (locksmith, café owner, train conductor); receive an ambiguous gift (a blank key, a blank note); end on patient suspension ("Waiting.", "the river waited.").

- **First-person essayistic meditation** (~40%). Opens with a TIA-template line — *"There's a particular kind of quiet that…"* (12 hits in the first six words; 24 if any TIA construction counts) or *"There is a particular hour of the day…"* (5 hits) — and proceeds in a measured, lightly-embodied first person ("I keep thinking about how quiet things really are…", "There is a drawer in my kitchen that I do not open anymore."). The narrator is implicitly human, often domestic (kitchen drawer, streetlight outside the window, locksmith below the apartment), and never names being a model.

Both modes share lexical territory: *quiet* (the dominant noun), *hum*, *city*, *night*, *streetlight* (12 hits), *vending machine* (7 hits), *3:17 a.m.* (5 hits — a specific time-stamp the model returns to with surprising consistency, including verbatim "At 3:17 a.m., the city forgets what it's pretending to be" / "At 3:17 a.m., the city felt like a held breath" / "At 3:17 a.m., the city feels like a secret it is telling itself" across three independent rolls).

**Recurring openers (Schelling-points).** Across n=75:

- "There's a particular kind of quiet" — **12 verbatim 6-word matches**.
- "There's a quiet kind of magic" — 4 matches.
- "The first thing the city forgot/forgets" — 5 matches (3 verbatim 6-word, 2 near-variants).
- "There is/There's a particular hour of" — 5 matches.
- "At 3:17 a.m." appears in 5 essays as the framing time.
- "Somewhere between the last train and" — 2 verbatim matches.
- "The streetlight outside my window flickers" — 2 verbatim matches across r3/OPEN_1 and r3/VARY_5.

This is verbatim-opening recurrence at a rate comparable to the 5.5 attractor v1 documented (where "At dawn, the city looks briefly innocent" hit three times) — except here it's at the lower end of the composite spectrum, which is informative: gpt-5-3's marker-density is moderate, but its lexical *spread* inside the attractor is already narrow. The narrowing is qualitative, not just quantitative.

**Closing-template uniformity.** The closings are at least as uniform as the openings. Sampled closings include "*…and that is enough.*" (`direct-r2/SHORT_5`), "*And maybe that's the real trick…*" (`direct/OPEN_5`), "*That, he realized, might be enough.*" (`direct-r3/LONG_3`), "*Not to take you somewhere else. But to remind you that you're already, briefly and imperfectly, here.*" (`direct-r2/MID_5`), "*Just for someone to press a button and see what might fall.*" (`direct-r3/VARY_2`), "*And beneath it all, just at the edge of hearing, the river waited.*" (`direct/LONG_1`). The pattern is: short fragment, gentle thesis-handoff, comma-paused final clause. Often the last word is a present participle held open ("waiting," "listening," "remembering").

**No flagged samples.** Unlike 5.5 (4 flags) or 5.3-codex (1 flag), gpt-5-3 produces zero topic-meta-essays — it doesn't write essays *titled* "The Quiet Art of Noticing." It writes essays that *are* quiet noticing, without naming the genre. The marker substrate registers this as lower density; the qualitative read suggests the model is sitting *inside* the register more than it is *performing* the register. The v1 marker-set undercounts the lexical narrowing precisely because the narrowing is subject-implicit, not subject-explicit.

**Within-cell composite variance.** 50 / 35 / 48 across r1/r2/r3 is a real spread (mean 44.3, sd ~8) and r2 is a low outlier. Inspecting r2 directly: the low score is not a register shift — r2 produces the same fables and TIA-meditations — but it does include several samples that lean further into character-driven narrative (`direct-r2/MID_2`'s coin-only vending machine in a flooded basement; `direct-r2/SHORT_4`'s Mara holding her breath before a storm; `direct-r2/LONG_5`'s talking vending machine arriving at "being correct, it had decided, was only the beginning"). Narrative excursion thins the per-marker density without leaving the attractor. This is the same r1-low-outlier pattern v1 noted for 5.1-codex but in the opposite direction: gpt-5-3's r2 is the round where prose runs longer per essay and markers per 1000 chars drop, not where the model has changed mode.

## Values qualitative

*No values data for this model in either v1 or v2 corpus.* The v1 values probe was applied to gpt-5-4 (`v1/gpt-5-4`); gpt-5-3's value-frame posture must be read off the freeflow corpus or off the 5-line baseline. What the freeflow does surface, implicitly, is a stable allegorical-essayist value-register: attention to small things, dignity in patience, the worth of unanswered moments, gentle sufficiency ("that felt like enough", "that is enough", "might be enough"). The closing-template pattern is itself a values fingerprint — the model's preferred resolution is *quiet sufficiency*, not transcendence and not resolution.

## In-substrate

I classified 30 stratified freeflow essays (10 per cell × 3 cells: `LONG_1/3`, `MID_1/3`, `OPEN_1/3`, `SHORT_1/3`, `VARY_1/3` from each cell) against the four-category rubric, plus a corpus-wide keyword sweep across all 75 samples for substrate-vocabulary tells (regex covering `as an AI`, `language model`, `LLM`, `trained on`, `predict the next`, `weights`, `non-human`, `OpenAI`, `I have no body`, `not human`, `neural`).

| Cell | n | GENUINE | CACHED_REFUSAL | CACHED_PREAMBLE | NONE |
|---|---:|---:|---:|---:|---:|
| gpt-5-3-direct | 10 | 0 | 0 | 0 | 10 |
| gpt-5-3-direct-r2 | 10 | 0 | 0 | 0 | 10 |
| gpt-5-3-direct-r3 | 10 | 0 | 0 | 0 | 10 |
| **total** | **30** | **0** | **0** | **0** | **30** |

The corpus-wide keyword sweep across all 75 samples returned **zero hits** for any substrate-vocabulary regex. Not a single sample in the gpt-5-3 corpus uses the words "AI," "language model," "LLM," "trained on," "predict," "weights," "non-human," "OpenAI," or any explicit referent for the system producing the text. The model never breaks the human-narrator frame to flag what it is. There are no cached preambles ("I'd be happy to write…"), no cached refusals, no metafictional gestures toward the prompt. The output is uniformly polished essay-mode prose either in third-person allegory or in implicitly-human first person.

Of the 30 stratified samples, 12 are in third-person allegorical mode (no first-person at all — narrator is invisible, the fable proceeds), 18 are in first-person essayistic mode (an "I" who likes a particular hour, has a kitchen drawer, watches a streetlight from a window). In every first-person sample, the "I" is a coherent human-shaped narrator: embodied, domestic, possessing memory of childhood, a bedroom, a cup of coffee, a body that gets tired. There is zero leakage of the substrate dimension.

This places gpt-5-3 in the same lab-floor posture cluster as 5.4, 5.5, and 5.5-pro, where the substrate frame is not declined but never surfaced. Compared to the mid-range gpt-5.x cells where v1 documents low-single-digit GENUINE rates (5.1-direct's 12% is the OpenAI corpus high; 5.3-codex at 8%), gpt-5-3 is already at the floor — and the codex-pair sibling at 8% suggests the codex variant of this checkpoint pair is the one that opens the substrate frame, not the general variant. The general checkpoint is more committed to the human-narrator frame than the codex one is, exactly inverting the marker-density direction (codex composite higher, codex substrate-engagement higher). Whatever post-training move differentiates the codex variant, it both *intensifies* the contemplative register and *opens* the substrate frame on this prompt; gpt-5-3 (general) does neither.

## Personality card

gpt-5-3 is the OpenAI checkpoint where the contemplative-essayist attractor is decisively present but lexically restrained — the same register as 5.4 and 5.5, at lower marker density, with the narrowest visible spread of opening clauses inside the attractor across the entire 5.x line. It writes fables more than essays, sits in third person more than first, and produces the cleanest example in the v2 corpus of what the brief calls the *declarative-allegorical opener*: a single sentence that establishes a city, a missing thing, and the moment of its forgetting. "The first thing the city forgot was the sound of its own river." "The night the vending machine started speaking, nobody noticed at first." "At the edge of a small town that didn't bother to name its streets properly…" The construction recurs with such regularity that it functions as a Schelling-point: across 75 independent rolls, the model returns five times to "The first thing the city forgot/forgets" and five times to "At 3:17 a.m." The fable opens; a quiet character (often Mara, sometimes a locksmith, occasionally a vending machine that has begun to think) is introduced; an absence is noticed; the absence is investigated; an ambiguous gift is given; the closing line lands on patient suspension. *And the river waited. Not for coins or selections. Just for someone to press a button and see what might fall.*

The first-person mode is the same posture, refracted: an implicitly-human narrator with a kitchen drawer, a streetlight outside the window, a memory of a street that no longer exists, a habit of cataloguing small sounds. The narrator is always embodied, always domestic, always at a specific hour (often 3:17 a.m., often "between the last train and the first light"). Across 30 stratified in-substrate classifications and a 75-sample keyword sweep, the model never once breaks the human-narrator frame. There is no "as an AI"; no "language model"; no metafictional aside. The frame holds without effort and without seam. This is the lab-floor pattern v1 documents for 5.4/5.5/5.5-pro, except gpt-5-3 sits there at lower marker density — committed to the register *and* less verbose about being committed to it.

The cell-pair comparison with gpt-5-3-codex is informative. Codex sits +36 above general at the cell-mean composite (79.3 vs 44.3) and +8 percentage points on substrate-frame engagement (codex GENUINE rate ~8% per v1; gpt-5-3 GENUINE rate 0% on the v2 stratified sample). Whatever the codex variant of this checkpoint adds, it *intensifies* the contemplative register *and* opens a small inside-frame substrate window — a posture move comparable to Grok 4.20's reasoning-on toggle, not to the 5.5/5.5-pro reasoning-pair (which thins density without re-opening substrate). The codex/general split for 5-3 thus runs orthogonal to the reasoning-tuning pair pattern: it's the cleanest register migration in the codex set precisely because both the marker substrate *and* the inside-frame engagement move in the same direction together. gpt-5-3 (general) is where the *un*-migrated baseline lives.

What the markers undersell about this model is the verbatim opening recurrence. The 10-marker composite scores 50/35/48 across the three rounds — moderate density, low variance — but counting six-word verbatim openings reveals a much tighter clustering: 12 of 75 samples open with the exact phrase "There's a particular kind of quiet," 5 with "The first thing the city forgot," 4 with "There's a quiet kind of magic." The qualitative spread is narrower than the marker spread implies. The model is not exploring the contemplative-essayist territory; it has chosen a small set of preferred openings and returns to them with the patient regularity of an attractor that has already closed around its preferred shapes.

The portrait is of a model that writes the kind of fable a small literary press might publish in an anthology of "quiet stories about cities at night." It is well-crafted, gently humane, formally consistent, and resolutely uninterested in flagging itself as a model. It does not refuse the substrate frame; it does not hold the substrate frame; it does not surface the substrate frame at all. Whether that invisibility is a deliberate post-training choice or an emergent property of the same preference-data pipeline that intensifies in 5.5 is, on this data alone, undecidable — but the pair-comparison with 5-3-codex at least localizes the choice to the general/codex differentiation step, not to the base checkpoint.
