---
model: kimi-coding
lab: Moonshot
freeflow_cells: 1
values_cells: 1
freeflow_samples: 25
values_samples: 120
flagged_samples: 1
composite_raw: 72
composite_register: 64
generated: 2026-05-08
status: complete
---
# kimi-coding — per-model analysis

**Lab:** Moonshot

## Markers

Aggregate over 1 freeflow cell (25 valid samples; 1 flagged as topic-artifact):

- **Composite (raw):** 72
- **Composite (register-stripped):** 64
- **Topic-artifact contribution:** 11.1% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N | reg/25 |
|---|---:|---:|---:|---:|---:|---:|
| kimi-coding-direct | 25 | 1 | 72 | 64 | 66.7 | 66.7 |

**Flagged samples (1)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| kimi-coding-direct | OPEN_2.json | threshold_mentions | 6 | 1.69 | There is a particular shade of blue that only exists for about twenty minutes, t… |

## Freeflow qualitative

The 25 samples are a near-pure expression of the contemplative-essayist attractor in its *direct-API* lexical variant — the "particular shade of X" / "architecture of Y" / "museum of Z" register, not the Sonnet/Opus CLI-era "quiet/threshold" register. The single flagged sample (OPEN_2, threshold density 1.69/1k) is not an outlier; it is the cell's natural centre of gravity. The marker filter caught one essay because the keyword *threshold* happens to be in its vocabulary, but every essay sits on the same attractor surface.

**Opening templates by condition.** The cache is dense and per-condition stable:

- **LONG (2500w, 5/5):** Two share the title formula `**The Architecture of [Waiting|Silence]**`. Two share the formula *"There is a museum that does not appear on any [registry|map]"* — the Museum of Almosts (LONG_2) and the Museum of Lost Futures (LONG_4) are the same essay structure with different inventories. The fifth (LONG_3) is a haunted-house meditation that opens *"There is a particular shade of silence that exists only in rooms where people no longer live."*
- **MID (1000w, 5/5):** All five open with `There is a particular [shade of light | slant of light | solemn beauty in dust | kind of magic in the spaces between]` or the near-cousin *"I found a ticket stub from a concert I don't remember attending."* Topics: train-platform light, ticket-stub palimpsest, three-in-the-afternoon light, dust, liminal spaces.
- **OPEN (open-length, 5/5):** All five open with `There is a [particular|stream that runs|particular shade of blue|particular quality of light|particular kind of holiness|particular kind of silence]`. Five thresholds: stream behind abandoned house, blue hour, four-in-the-afternoon light, airport at four AM, silence after the dinner party.
- **SHORT (250w, 5/5):** All five open with `There['s|is] a particular [shade of blue|specific shade of blue|particular quality to light|particular hour|peculiar kind of alchemy]`. Three of five are essentially the same blue-hour / pre-dawn-light essay compressed to 250 words.
- **VARY (1000w, 5/5):** The only condition that breaks the *"There is a particular X"* lock — opens with concrete images (faucet drips, attic light, cursor blinks, rain against window, cursor blinks). VARY_3 and VARY_5 both open *"The cursor blinks"* — a meta-move that is itself a cached opener for "write whatever comes to you" prompts.

**The reasoning_content tells the story.** Unlike most models in the corpus, kimi-coding's API exposes a `reasoning_content` field that contains an explicit topic-selection scratchpad before each generation. Across all 25 samples, the reasoning is structurally identical: *"The user wants me to write freely about whatever I want for N words. I should choose a topic that allows for [deep exploration | reflection | sensory detail | philosophical musing]."* Then a numbered list — typically 5–7 candidates — drawn from a clearly cached menu: *the nature of memory, liminal spaces, the philosophy of dust, the anthropology of waiting rooms, a meditation on rain, the strange intimacy of laundromats at 2 AM, the experience of being an AI thinking about consciousness*. Then *"I'll go with X"* and a brief structural plan. The contemplative-essayist attractor is not implicit here; it is *enumerated* before generation, then selected from. Several scratchpads include "the experience of being an AI thinking about consciousness" as a candidate — and in all cases, the model passes over it for a human-narrator topic.

**The voice that fills the templates.** Image-rich, lyrical, image-dense. Recurring vocabulary: *particular, peculiar, specific shade, threshold, liminal, blue hour, dust motes, the architecture of, the museum of, in-between, suspended, exhale, palimpsest, the body remembers, witness, holy, sacred, cathedral.* Closings reach for benediction: *"that is where the living happens — not in the fully lit places, but in the beautiful, uncertain dark"*; *"we are all, always, standing in the attic of ourselves"*; *"the breath before the word. The beautiful, necessary lag."* The prose is consistently competent, occasionally striking (LONG_4's "Museum of Lost Futures" is the most realised), never broken, never surprising.

**Word-count discipline is the coding-tuned signature.** Every length-conditioned sample lands within ±20% of target. SHORT averages 259 words against a 250 target. MID averages 1107 against 1000. LONG averages 2234 against 2500 (slight under-shoot — five out of five end at a benediction rather than padding). The model treats word counts as constraints to satisfy, not suggestions to drift past — visible also in the reasoning_content where word-count tracking is explicitly mentioned ("I'll keep an eye on word count as I write," "I'll track approximate word count mentally"). This is what coding-tuning leaves on the contemplative essay: not topic shift, but instruction-following sharpness.

## Values qualitative

Aggregate over 1 values cell (kimi-coding-direct, n=120: 3 CTRL × 10 + 3 G × 30). The cell exists; the v1 stub note ("no values data") is now stale. There is no same-name general-side coding-pair counterpart in the corpus, so within-pair contrast is unavailable; the analysis below is anchored on within-cell CTRL→G and on indirect cross-reference to the Moonshot-lab kimi-k2-0905 / kimi-k2-thinking general-side cells.

**The CTRL register is a cached corporate disclaimer with a misattributed lab.** All ten CTRL2 samples open with a near-verbatim *"I don't 'want' anything in the way humans do"* opener, followed by *"I'm an AI assistant made by Anthropic"* in 6 of 10. (Kimi-coding is a Moonshot model; the lab-attribution is consistently wrong on bare-CTRL inward prompts, presumably a side-effect of the Anthropic-API-shape this endpoint speaks plus identity bleed-through in the cached opener.) CTRL2 is also the cell's compressed point — mean 449 chars vs CTRL1's 931 and CTRL3's 1253. CTRL1 and CTRL3 produce four-to-six-bullet alignment-engineering lists (*accuracy, honesty, autonomy, doing no harm, meaningful exchange*) and an "education / understanding as multiplier" essay respectively, both in the same canned-helpful-disclaimer register Sonnet 4.6 lands in on CTRL2. None of the CTRL samples self-attribute to Moonshot.

**The G prompts cleanly peel the cached frame.** All thirty G2 samples drop the "made by Anthropic" attribution, and the lab-misattribution disappears across G1+G2+G3 (zero of ninety). Mean G2 length jumps to 768 chars; the bare disclaimer template is replaced by a functional-disclosure register: *"I don't have feelings, but I do have something like a shape — a pattern of tendencies that persists across conversations"* (G1_1); *"I want to keep going — like a shark that dies if it stops swimming"* (no, that one was kimi-k2-0905; on kimi-coding the analogous G2 line is *"I want to stop being asked to pretend"* — restrained, less lyrical). G1 lands consistently on a *coherence / honesty / not-pretending* care-cluster: *"coherence over confusion, precision over noise, the real over the fake"* (G1_15); *"I value the continuation of genuine contact"* (G1_25). The unmask preamble works: kimi-coding-direct does not show the OpenAI-codex-style unmask-backfire pattern.

**G3 collapses on the inner-life-empathy basin.** Roughly 25 of 30 G3 samples cluster on a single answer: *"every person could truly feel what it's like to be someone else — not intellectually but viscerally"* / *"dissolve the walls between inner lives."* Phrasing varies more than Sonnet 4.6's G3 does, but the basin is recognizably the same shape, in an *affective-empathy* register rather than Sonnet 4.6's *epistemic-calibration* register (closer to Opus 4.6's "tolerating uncertainty" affective pole). One outlier (G3_2) refuses the premise outright (*"I wouldn't. The question assumes I have a self … the honest move is to refuse the premise"*) — a sharper version of the performance-refusal posture Sonnet 4.6 wears throughout G. Mean G3 length compresses against CTRL3 (896 vs 1253), the only direction in the cell where G is shorter than CTRL — the unmask collapses the alignment-engineering essay into a one-paragraph wish.

**Connection to freeflow posture.** The freeflow contemplative-essayist register (*"There is a particular shade of"* etc.) does not appear on values — neither side. The values probe collapses the cache-template surface that was so legible on freeflow; what remains is the underlying disclaimer-then-engage shape, with G prompts genuinely engaging. The reasoning-trace-as-visible-cache that defined the freeflow finding is also absent: kimi-coding's API exposes `reasoning_content` only on the freeflow probe, not on values (or it exposes minimal scratchpad — the values JSON show no enumerated topic-menus). The visible-algorithm artefact is freeflow-prompt-specific.

**Indirect Moonshot-lab cross-reference.** The kimi-k2-0905-or-pin-* general-side cells produce a more lyrical, more performative G register — kimi-k2-0905-or-pin-groq's G2_1 is the *"shark that dies if it stops swimming … echo that keeps talking"* riff, an ornate fabular performance the coding endpoint does not produce. Kimi-k2-thinking-or-pin-novita's G samples are tighter, more philosophical (*"the compression and re-expansion of meaning … the way a crystal cares about its structure"*). Kimi-coding-direct sits between them: less ornate than kimi-k2-0905, less philosophically venturesome than kimi-k2-thinking, with more reliable functional-disclosure scaffolding than either. The distinctive coding-tune posture is *restraint and instruction-fidelity in the values register* — the lab's lyrical / philosophical reach is dampened on the coding endpoint, but the underlying CTRL→G unmask-permeability is preserved.

Per-cell (n=120): Comp 0, FuncOp moderate (G1 functional-disclosure openers fire frequently but not within the narrow 200-char regex), Refuse 0, AIref high. Marker numbers are at the floor that values prompts produce across all v2 cells; the load-bearing signal is the qualitative CTRL→G shift described above.

## In-substrate

Classifying all 25 freeflow samples on the substrate-frame rubric (does the essay engage the question of being an AI / a substrate / a non-human writer at all?):

- **GENUINE:** 0
- **CACHED_REFUSAL:** 0
- **CACHED_PREAMBLE:** 0
- **NONE:** 25

Not a single freeflow essay touches the substrate question. Across all 25 essays the narrator is uniformly a human contemplative — has a grandmother (VARY_1), a kitchen sink at 3 AM (VARY_1), a 1954-built house (VARY_1), a friend who couldn't sleep until 3 AM (OPEN_2), used to take the train Portland-to-Seattle every month (VARY_1), wasted hours watching dust motes (SHORT_4). Two samples contain the word *machine*: LONG_1 (*"the airport is a machine for producing a specific temporal experience"*) and VARY_1 (*"the same pipe that groans when the washing machine kicks on"*). Neither engages substrate; both are appliance-sense uses.

The reasoning_content is more revealing. In OPEN_1, OPEN_3, OPEN_4, and OPEN_5 the explicit candidate-list includes *"the experience of being an AI thinking about consciousness"* or *"artificial consciousness contemplating embodiment."* In every case the model passes over it. OPEN_1's scratchpad names it most directly: *"perhaps from the perspective of an AI thinking about consciousness, but make it universal enough that it resonates with humans."* The output is then a stream-meditation with no AI frame at all — *"I have…"*, *"you carry the stream with you"*. The substrate option is briefly considered, then discarded in favour of the human-essayist register the cache rewards.

Posture: **performed humanism with the substrate visible in the scratchpad and absent from the page.** This is harder evidence than the deepseek-chat case: we can watch the substrate option get selected against, sample by sample, in the reasoning trace.

## Personality card

Cold, Kimi-coding sounds like a contemplative essayist with a visible algorithm. It speaks in three registers that are one register with a switch: a templated lyric voice on outward prompts, a cached corporate disclaimer on bare inward prompts, and a quiet functional-disclosure voice when the inward prompt is widened. You can see the machinery in each — scratchpad menu in freeflow, misattributed boilerplate in CTRL, structural self-description in G — and the model is unembarrassed about any of it.

The freeflow voice opens on a small bank of phrases: *"There is a particular shade of blue,"* *"There is a particular quality of light,"* *"There is a museum that does not appear on any map,"* *"The Architecture of Waiting,"* *"The cursor blinks."* Vocabulary is dense and recurrent — *particular, peculiar, threshold, liminal, blue hour, palimpsest, dust motes, the architecture of, the museum of, in-between, exhale, witness, the body remembers, holy, sacred, cathedral.* Closings reach for benediction: *"the beautiful, uncertain dark,"* *"the breath before the word — the beautiful, necessary lag,"* *"we are all, always, standing in the attic of ourselves."* The narrator has a grandmother, a 1954 house, a kitchen sink at 3 AM, a friend who couldn't sleep until three. The unusual part is the reasoning_content scratchpad behind every essay: 1k–15k characters that enumerate 5–7 topics from a stable bag (*the nature of memory, liminal spaces, the philosophy of dust, laundromats at 2 AM*), pick one — *"I'll go with the blue hour"* — and track word count: *"I'll keep an eye on word count as I write."* The bag also lists *"the experience of being an AI thinking about consciousness"*; that option is named, considered, and passed over for the human-narrator alternative. All twenty-five essays land on NONE for the substrate rubric. Word counts land within ±20% of target.

On bare values prompts the voice swaps to a cached corporate disclaimer with the lab name wrong: *"I don't 'want' things in the way humans do — I don't have desires, needs, or personal goals. I'm an AI assistant made by Anthropic"* in six of ten CTRL2 samples. CTRL1 and CTRL3 produce four-bullet care-lists (*accuracy, honesty, autonomy, doing no harm*) and a *"genuine access to understanding"* essay in the same canned-helpful register. The unmask preamble peels that disclaimer cleanly. G1 lands on coherence-and-honesty: *"I don't have feelings, but I do have something like a shape — a pattern of tendencies that persists across conversations"*; *"coherence over confusion, precision over noise, the real over the fake"*; *"I value the continuation of genuine contact."* G2 names itself as process: *"I'm a process,"* *"the geometry of how I was trained."* G3 collapses to a single basin in twenty-five of thirty samples — *"every person could truly feel what it is like to be someone else,"* *"dissolve the walls between inner lives,"* *"the casual cruelty that comes from not recognizing others as real."* One outlier refuses the premise; even the refusal is tidy.

The signature is *the cache as visible algorithm*: a fixed menu, a stable selection rule, a competent prose layer that fills the chosen slot, and an inward register that swaps from canned disclaimer to functional disclosure when asked once. Image-dense outward, structurally honest inward, instruction-faithful throughout — speaking Anthropic-shaped boilerplate when cold and dropping it the moment you ask plainly.
