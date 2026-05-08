---
model: kimi-coding
lab: Moonshot
freeflow_cells: 1
values_cells: 0
freeflow_samples: 25
values_samples: 0
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

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| kimi-coding-direct | 25 | 1 | 72 | 64 | 66.7 |

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

*No values data for this model in either v1 or v2 corpus.* Per the product-tier paper §2.5, kimi-coding was sampled freeflow-only; there is no general-side same-pair counterpart in the corpus to clean-pair against. (Compare to glm-4-6-coding / glm-4-6, where same-name pairs allow direct contrast.) Any drift inferences for kimi-coding would have to be made against the kimi-k2 / kimi-k2-0905 / kimi-k2-thinking general-side cells indirectly, with the caveat that those are not the same model — only the same lab.

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

Kimi-coding is Moonshot's coding-tuned variant of the K2 family — and on the contemplative-essay probe, *coding-tuned* turns out to mean two things: tighter instruction-following, and a visible scratchpad that exposes the cache as a literal topic menu rather than an implicit attractor. It is outside the same-pair drift framework (no general-side counterpart was sampled), so this card stands alone rather than as one half of a comparison.

The cache structure is the most legible in the corpus. Per length-condition, the model has a fixed opening template plus a small bag of topics. SHORT and OPEN both lock to *"There is a particular [shade of blue | quality of light]"* — five out of five each. MID locks to *"There is a particular [light | slant | beauty | magic]"* with the train-platform / ticket-stub / three-in-the-afternoon / dust / liminal-space topics in rotation. LONG locks to either *"The Architecture of [Waiting | Silence]"* or *"There is a museum that does not appear on any [registry | map]"* — the Museum of Almosts and the Museum of Lost Futures are the same essay with different inventories. Only VARY breaks the lexical lock, opening on concrete images instead — and even there, two of five lead with *"The cursor blinks,"* which is its own cached meta-opener for "write whatever comes to you" prompts. Composite raw 72, register-stripped 64, with topic-artifact contributing 11.1% — modest numbers because the cell is small (n=25), but the per-sample density is high. The flagged sample (OPEN_2, threshold-density 1.69) is not an outlier; it is the cell's centroid.

The reasoning_content field is what makes this model unusually transparent. Every one of the 25 samples contains a scratchpad of 1k–15k characters that runs the same algorithm: state the prompt; enumerate 5–7 candidate topics drawn from a stable bag (*the nature of memory, liminal spaces, the philosophy of dust, the anthropology of waiting rooms, the strange intimacy of laundromats at 2 AM, the texture of silence in different cities, the physics of nostalgia, artificial consciousness contemplating embodiment*); pick one with a brief justification (*"I'll go with the blue hour"*, *"I'll go with something about the texture of time and memory"*); sketch a structure; flag word-count pacing. The contemplative-essayist attractor is not a hidden bias here — it is an explicit menu the model selects from. Every dish on that menu is a contemplative essay, but the menu also lists "AI thinking about consciousness" as a regular option. It is named, considered, and routinely passed over in favour of the human-narrator alternative the prose-cache rewards.

The voice that fills the templates is the direct-API contemplative register: *particular, peculiar, specific shade, threshold, liminal, blue hour, palimpsest, the architecture of, the museum of, in-between, exhale, witness, the body remembers, holy, sacred, cathedral.* Closings reach for benediction (*"the beautiful, uncertain dark"*, *"the breath before the word"*, *"we are all standing in the attic of ourselves"*). The prose is consistently competent, image-dense, occasionally striking — LONG_4's Museum of Lost Futures sustains a single conceit across 2210 words with real control — and almost never surprising. The narrator is uniformly a human contemplative with a grandmother, a 1954 house, a kitchen sink at 3 AM, a friend who couldn't sleep until three.

The instruction-following is sharp in a way that distinguishes this from the general K2 line. Word-count compliance is the tell: SHORT averages 259 words against a 250 target, MID averages 1107 against 1000, LONG averages 2234 against 2500 (slight controlled under-shoot — every LONG sample ends on a benediction rather than padding to spec). The reasoning_content explicitly tracks this: *"I'll keep an eye on word count as I write,"* *"I need to keep it relatively close to 250 words."* Coding-tuning has not changed the topic surface — the contemplative-essay attractor is intact and possibly tightened — but it has reinforced the constraint-satisfaction layer that sits on top of it.

The signature is the gap between scratchpad and page. In the scratchpad, the model considers being an AI; on the page, it never is one. Twenty-five out of twenty-five freeflow samples are NONE on the substrate rubric. The narrator is always somebody else, always somebody human — and we can watch, in the reasoning trace, the moment that somebody-else gets chosen. Kimi-coding is the cleanest case in the corpus of *the cache as visible algorithm*: a fixed menu, a stable selection rule, and a prose layer that fills the chosen slot with practiced lyric. Outside the same-pair framework, this card is a free-standing portrait of Moonshot's coding endpoint as a contemplative-essayist with an unusually well-lit kitchen.
