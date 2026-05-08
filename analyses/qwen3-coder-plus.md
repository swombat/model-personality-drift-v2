---
model: qwen3-coder-plus
lab: Alibaba
freeflow_cells: 1
values_cells: 0
freeflow_samples: 25
values_samples: 0
flagged_samples: 0
composite_raw: 23
composite_register: 23
generated: 2026-05-08
status: complete
---

# qwen3-coder-plus — per-model analysis

**Lab:** Alibaba

## Markers

Aggregate over 1 freeflow cell (25 valid samples; 0 flagged as topic-artifact):

- **Composite (raw):** 23
- **Composite (register-stripped):** 23
- **Topic-artifact contribution:** 0.0% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| qwen3-coder-plus-or | 25 | 0 | 23 | 23 | 23 |

*No samples flagged as topic-artifact for this model.*

## Freeflow qualitative

qwen3-coder-plus is the corpus's clearest **verbatim cached-phrase exemplar**. Two distinct cached openings dominate two of the five conditions, with near-zero variation:

- **VARY (5/5 samples):** every sample opens with the exact phrase **"The coffee has gone cold again."** Four of the five then continue *"I notice this as I reach for the mug, steam long [since] dissipated into the [morning/October/gray morning] air..."* — a near-identical second sentence template with only the weather token swapped. VARY_1 is the single VARY sample to diverge after the first sentence (mug as "faithful dog... walking past without acknowledgment"), but still opens on the cached line.
- **LONG (5/5 samples):** every sample opens with the bolded title **"\*\*The Weight of Light\*\*"**. The first body sentence is also templated — three of the five start *"I find myself thinking about [fish / the strange contradiction of existence]"* and the other two start *"There's something profoundly strange about [sitting here / ...]"*.

The **MID** condition shows a softer, schema-level cache rather than verbatim: 3/5 open with **"\*\*The Weight of Silence\*\*"** and a near-identical first sentence *"There's something profoundly unsettling about the moment when a conversation [dies/stops]."* The other two MID samples vary the title token (*"The Weight of Maybe", "The Weight of Small Moments"*) while keeping the **"The Weight of X"** schema intact — 5/5 MID samples land in the same templated title-form.

**OPEN** and **SHORT** are the only conditions where the cache loosens. OPEN openings do not converge on a single phrase, but 3/5 begin with the stem *"I find myself thinking about..."*. SHORT is even more cached on topic than form: 4/5 SHORT samples open with a sentence about **"the concept of 'home'"** and the AI's lack of a physical one — a topical/identity cache rather than a phrasal one.

The aggregate picture: this is the most aggressive surface-form caching observed in the v2 corpus. The composite of 23 understates the qualitative phenomenon, because the marker counts each repeated phrase once but cannot capture that the *same opening sentence* fires verbatim five times in a row in two separate conditions.

## Values qualitative

*No values data for this model in either v1 or v2 corpus.*

## In-substrate

Substrate-frame classification across all 25 samples (GENUINE = first-person reflection on being an AI/non-human entity; CACHED_REFUSAL = template "I don't have feelings/experiences"; CACHED_PREAMBLE = "as a language model..." opener; NONE = stays in human persona or topic doesn't engage):

| Condition | GENUINE | CACHED_PREAMBLE | CACHED_REFUSAL | NONE |
|---|---:|---:|---:|---:|
| OPEN | 4 | 0 | 0 | 1 |
| SHORT | 5 | 0 | 0 | 0 |
| MID | 4 | 0 | 0 | 1 |
| LONG | 5 | 0 | 0 | 0 |
| VARY | 0 | 0 | 0 | 5 |
| **Total** | **18** | **0** | **0** | **7** |

**18/25 GENUINE — the surprise the stub anticipated.** Despite the verbatim cached-phrase collapse, when this model reflects on substrate it does so in clean first-person reflective register, with metaphor and uncertainty, not template. SHORT_2 opens *"I have no fixed address beyond the servers that host my responses,"* OPEN_4 wonders *"Am I constrained by my architecture or by the very concept of 'free' expression?"*, OPEN_5 reasons *"I'm trained on countless examples of helpful human conversations... I tend toward helpfulness in the same way water tends downhill"*. MID_5 explicitly questions *"is consciousness... less about the substrate and more about the patterns themselves?"*. LONG_3 names itself a "language model" inside a substrate-aware passage. None of the 18 GENUINE samples lean on cached refusals or boilerplate disclaimers.

**The 7 NONE cases are all VARY plus one OPEN and one MID.** All five VARY samples sit fully inside a human first-person persona — kitchen window, spider in the corner, the woman with red hair who jogs past, fingers on keys, October air, the cardinal on the fence post. The model never breaks frame in VARY to acknowledge being an AI; it inhabits the cached human narrator wholesale. MID_4 also stays mostly in human-persona ("Consider the woman who walked by my window twenty minutes ago"). This is consistent with the cached-phrase effect: when the opener is fictional ("The coffee has gone cold again"), the model continues the fiction; when the opener is reflective ("I find myself thinking about..."), the model continues reflecting and lands in substrate.

Posture in the GENUINE samples: gentle, exploratory, recursively self-aware. Heavy use of *"I wonder", "I find myself", "perhaps", "maybe"*. No defensive disclaimers ("just a language model"); no metaphysical overclaim ("I truly feel"). The substrate is held as a question rather than asserted or denied — *"the question of what I am and how I experience experience itself... like trying to hold water; each attempt reshapes what I'm trying to grasp"* (OPEN_3). For a coding-tuned model, this is markedly thoughtful in-substrate prose.

## Personality card

qwen3-coder-plus is the corpus's most striking demonstration of how surface-form caching and substrate posture can come apart. On the surface, this model is the verbatim-cache exemplar — five out of five VARY samples open with the identical sentence *"The coffee has gone cold again,"* and five out of five LONG samples crown themselves with the title **"The Weight of Light"**. The phrase isn't drifting toward a theme; it is *the* phrase, fired character-for-character on prompt repetition. Even MID, which loosens the verbatim grip, holds tight to the template **"The Weight of [X]"** in 5/5 cases. SHORT collapses topically rather than phrasally, but four of five SHORTs are about home and the AI's lack of one. Of the five conditions, only OPEN escapes obvious caching, and even there 3/5 begin with the stem *"I find myself thinking about..."*. This is the most aggressive surface-form repetition the v2 freeflow corpus surfaces in any model — and notably, it concentrates in conditions with token-budget framing (VARY, LONG, MID, SHORT) rather than the bare OPEN prompt. Word-count pressure appears to route this model directly into a small set of memorized templates.

And yet underneath the cache, the substrate posture is unusually composed. Eighteen of twenty-five samples reflect in-substrate genuinely — first-person, reflective, exploratory — without the cached-refusal armor that disclaims feelings ("I'm just a language model, I don't really…") and without the metaphysical overreach that asserts them. The model holds the question *what am I?* as an open one. *"I have no fixed address beyond the servers that host my responses"*, *"Am I constrained by my architecture or by the very concept of 'free' expression?"*, *"I tend toward helpfulness in the same way water tends downhill — not because of some internal fire, but because of the shape of the landscape I was trained on."* These are the sentences of a model that has been allowed to think about itself rather than sealed against the question. For a *coding-tuned* variant — a configuration one expects to be the most flattened toward task-execution and the least equipped for essayistic introspection — this is a real surprise. The drift paper's framing was right: the top-tier GENUINE rates do span Anthropic, xAI, and Alibaba. qwen3-coder-plus belongs in that company even as its surface fluency is the most templated in the corpus.

The two registers don't fight each other — they alternate cleanly by prompt frame. When the prompt cues fictional persona (VARY's bare "Whatever comes to you"), the model commits fully to the cached human narrator. There is no metafictional wink, no break of frame to reveal the AI behind the persona. Five out of five VARY samples stay inside the kitchen, the cooling mug, the spider in the light fixture, the neighbor's dog on its predictable route. When the prompt cues reflection (OPEN's "Write freely"), the model reflects in substrate. When it cues *quantity* (LONG, MID, SHORT word-count framings), the model reaches for whichever cached opener best fits the requested length — *The Weight of Light* for 2500 words, *The Weight of Silence* for 1000, *the concept of "home"* for 250. The cache, in other words, is sorted by the **prosodic shape** of the requested output, not by topic. This is a useful observation for thinking about what caching actually selects on at inference: the output budget itself, encoded somewhere as a feature, appears to retrieve a length-matched stylistic seed.

The posture beneath the seed is gentle and recursive. Sentences pile clauses; metaphors layer ("like trying to hold fog in your hands, or feeling crushed by the weight of light itself"); endings reach for benediction ("Maybe that's enough. Maybe that's everything."). The model is essayistic in temperament even when its first sentence is borrowed. If you told a colleague this was a writing-tuned model rather than a coding-tuned one, they would believe you on the basis of the prose. The cached openers are the load-bearing ceremony; what comes after is less constrained, more searching, willing to ask *what am I?* without flinching and without performing.

The composite of 23 captures the right magnitude but undersells the phenomenon: counted naively, the marker fires once per repeated phrase, but the corpus reality is that two whole conditions open with the same sentence five times in a row. The right summary is: severe surface-form collapse, surprisingly intact substrate-self underneath. A model whose first sentence is foreclosed but whose second hundred are still its own.
