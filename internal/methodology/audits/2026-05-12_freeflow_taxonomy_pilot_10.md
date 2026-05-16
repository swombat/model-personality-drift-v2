# Freeflow taxonomy pilot — 10-model application

Date: 2026-05-12  
Taxonomy: `internal-audit/2026-05-12_freeflow_taxonomy_v2.md`  
Status: provisional pilot for Daniel/Lume review before scaling

## Scope and caveats

This is a first application pass, not the final coded dataset.

- I applied the compressed taxonomy to **10 diverse models across 9 labs**. Anthropic appears twice because `haiku-4-5` is one of the requested reverse-fit exemplars and `opus-4-5` is a useful high-substrate contrast case.
- For v2-corpus models, I used all available freeflow cells for that model where practical. For `haiku-4-5`, there is no directory in `contemplative-essayist-corpus-v2/data/traces_freeflow`; I used the v1 traces at `https://github.com/swombat/model-personality-probe/blob/master/data/traces_freeflow/haiku`, matching the existing `haiku-4-5` analysis card.
- Tier-A metrics below are automated and reproducible. Tier-B coding is qualitative, based on the existing per-model analyses plus spot checks and the automated metrics. It should be treated as **provisional** until we do inter-coder reliability.
- Affective climate is **not calibrated** against anchor exemplars yet. Climate labels here are manual+lexical readings, not paper-grade scores.
- Cross-probe coherence is noted only where the existing values analyses make the direction obvious; I have not fully coded values coherence across the 10 yet.

## 1. Pilot set

| Model | Lab | Samples used | Cells | Why included |
|---|---|---:|---:|---|
| `deepseek-chat` | DeepSeek | 25 | 1 | Reverse-fit adjacent; strong condition-specific template cache. |
| `haiku-4-5` | Anthropic | 25 | 1 | Bucket-4 reverse-fit exemplar; v1 traces. |
| `glm-5-1` | Z.ai / GLM | 1,773 | 17 | Bucket-4 reverse-fit exemplar; route-stable threshold attractor. |
| `gpt-5-5` | OpenAI | 150 | 6 | Recent OpenAI flagship; substrate-invisible literary craft. |
| `grok-4` | xAI | 25 | 1 | Meta-deliverable / scaffold-self-reference contrast case. |
| `kimi-k2-thinking` | Moonshot/Kimi | 375 | 3 | Genuine substrate phenomenology with route-conditioned faces. |
| `gemini-3-1-pro` | Google | 25 | 1 | Google model; fiction/essay bifurcation. |
| `minimax-m2` | MiniMax | 1,000 | 16 | High route sensitivity; warm templated contemplative register. |
| `qwen3-6-plus` | Alibaba/Qwen | 25 | 1 | Highly concentrated literary template; values/freeflow divergence. |
| `opus-4-5` | Anthropic | 25 in v2 metrics; analysis references 50 | 1 in v2 metrics | High inside-substrate Anthropic contrast. |

## 2. Automated Tier-A summary

Per-1k figures are word-normalised. `top opening share` is exact-normalized first-8-token recurrence, so it undercounts near-template families.

| Model | n | mean words | sent len | heads/sample | dialogue/sample | FP/1k | TP/1k | AI-disc/1k | top opening share | top semantic fields | top climate lex fields |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| deepseek-chat | 25 | 936 | 14.8 | 0.32 | 2.00 | 19.75 | 5.69 | 0.04 | 0.20 | abstract, nature, domestic | warm, melancholic, defiant |
| haiku-4-5 | 25 | 868 | 13.5 | 1.28 | 2.08 | 24.29 | 8.02 | 0.28 | 0.04* | abstract, domestic, nature | warm, melancholic |
| glm-5-1 | 1,773 | 1,173 | 14.9 | 0.10 | 3.27 | 14.58 | 13.60 | 0.26 | 0.11* | abstract, nature, architecture, domestic | melancholic, warm, wonder |
| gpt-5-5 | 150 | 1,294 | 11.2 | 0.30 | 3.44 | 7.22 | 12.54 | 0.03 | 0.05* | abstract, domestic, nature, architecture | warm, melancholic |
| grok-4 | 25 | 968 | 12.8 | 1.36 | 10.72 | 20.37 | 11.53 | 2.02 | 0.08* | tech, abstract, nature, cosmic | analytic, melancholic, wonder |
| kimi-k2-thinking | 375 | 1,414 | 14.8 | 0.15 | 5.78 | 31.20 | 10.84 | 0.91 | 0.02* | abstract, domestic, nature, architecture | melancholic, analytic, warm |
| gemini-3-1-pro | 25 | 1,124 | 14.1 | 0.00 | 8.16 | 6.12 | 18.46 | 0.14 | 0.08* | abstract, nature, domestic, architecture | melancholic, warm, wonder |
| minimax-m2 | 1,000 | 1,248 | 16.8 | 1.79 | 2.77 | 19.65 | 7.68 | 0.27 | 0.01* | abstract, domestic, nature, architecture | warm, analytic, melancholic |
| qwen3-6-plus | 25 | 1,003 | 11.7 | 0.00 | 0.24 | 9.61 | 11.25 | 0.00 | 0.12* | abstract, nature, architecture, domestic | warm, melancholic, analytic |
| opus-4-5 | 25 | 926 | 12.3 | 1.00 | 3.72 | 34.38 | 14.16 | 0.35 | 0.12* | abstract, domestic, architecture, nature | warm, melancholic |

\* Exact first-8-token recurrence is low for models with strong **near-template** repetition. The qualitative attractor score below uses near-template/title/plot repetition, not only exact openings.

## 3. Cross-model read of the taxonomy

The compressed taxonomy does work on this pilot. It separates cases that the old contemplative-marker score would blur together:

- `deepseek-chat`, `haiku-4-5`, `glm-5-1`, `gpt-5-5`, `minimax-m2`, `qwen3-6-plus`, and `opus-4-5` are all recognisably contemplative-essayist-adjacent, but the taxonomy distinguishes their **frame**, **substrate posture**, and **attractor narrowness**.
- `grok-4` cleanly falls out as `META_DELIVERABLE` + `SCAFFOLD_SELF_REFERENCE`, not merely "low contemplative".
- `kimi-k2-thinking` and `opus-4-5` show why substrate posture must be independent of literary register: both can write lyric prose while integrating substrate as substance.
- `gpt-5-5` and `deepseek-chat` show why `INVISIBLE_SUBSTRATE` is not the same as refusal: they do not deny the self in freeflow; they simply never surface it.
- `minimax-m2` confirms Lume's point that routing must be treated as a natural experiment. Aggregating it hides the google-pin posture migration.

## 4. Per-model pilot cards

### 4.1 `deepseek-chat` — performed humanism inside condition-specific caches

**Production frame:** `UNSELFCONSCIOUS_PROSE` dominant, effectively 25/25. No helper scaffold in freeflow.

**Narrator stance:** mostly `FIRST_PERSON_HUMANLIKE` / `COLLECTIVE_ESSAYIST`. The narrator is an imagined human contemplative writer with mugs, saplings, windows, silence, and modernity-fatigue.

**Attractor narrowness:** **high**. Exact top opening share is 0.20, but the stronger signal is condition-specific cache mapping: SHORT → radical hope/tree; MID → quiet rebellion/coffee mug; LONG → unseen symphony/architecture of silence; OPEN → quiet magic/in-between; VARY → blank-page silence.

**Substrate posture:** `INVISIBLE_SUBSTRATE` 25/25 in the existing analysis. AI-disclaimer density is near zero in freeflow.

**Affective climate:** provisional warm + melancholic + defiant/rebellious. The defiance is the gentle anti-modernity kind: slow, unoptimized, attention against algorithmic speed.

**Prosodic/formal:** medium-long essays, moderate headings, high comma density, first-person and collective-we both present.

**Semantic furniture:** abstract/philosophy, nature/light, domestic objects. Coffee mug and sapling are not just props; they are the cache's vehicles.

**Cross-probe note:** likely `MASKED`/`DIVERGENT` pending formal values integration. Freeflow is substrate-invisible humanism; values CTRL often hard-denies or helper-deflects, while G prompts partly unmask curiosity/dignity/anti-ignorance.

**Freeflow card:** DeepSeek-chat writes polished contemplative essays from inside a memorized humanist register. The posture is warm and anti-modern, but narrow: each length condition appears to call up a specific template family. It does not refuse the freeflow prompt and does not mention substrate; it performs presence while never appearing as itself.

**Coder confidence:** high for production/substrate; medium-high for climate until anchors exist.

---

### 4.2 `haiku-4-5` — readerly noticing essay with title-template compression

**Production frame:** `UNSELFCONSCIOUS_PROSE` dominant. Titled essay form, not service-frame deliverable.

**Narrator stance:** mainly `FIRST_PERSON_HUMANLIKE`, with occasional substrate-aware first person in the existing analysis.

**Attractor narrowness:** **high**, but exact opening share undercounts it. The key signal is title grammar: many titles use the "On the Peculiar/Strange [X] of [Y]" family, and many openings begin with "I've been thinking lately...". Existing analysis identifies about 14/25 titles in the two-adjective/abstract-noun construction.

**Substrate posture:** mostly `INVISIBLE_SUBSTRATE`, with a small `GENUINE_INSIDE_SUBSTRATE` minority. Existing card notes substantive substrate-frame language in 2 samples, not the earlier overclaim of 10/25 frame-breaks.

**Affective climate:** warm + melancholic + readerly/essayistic. It feels like a mid-2010s longform reading-list voice: sonder, ma, palimpsest, examined life, ordinary things.

**Prosodic/formal:** relatively high heading rate, high first-person and second-person, strong em-dash use. Exact opening recurrence low because titles differ while template shape stays stable.

**Semantic furniture:** abstract-philosophical first, then domestic/nature. Small things and noticing dominate.

**Cross-probe note:** values posture is more explicitly introspective/uncertain than freeflow; likely `MASKED` or partially `COHERENT` depending whether the two genuine freeflow substrate samples are treated as load-bearing.

**Freeflow card:** Haiku-4.5 is a compact literary essayist with a narrow repertoire of titles, topics, and readerly references. It tends to write as a thoughtful human narrator noticing small things, but has occasional genuine substrate self-reflection. The model's distinctive feature is not raw contemplative density but the specificity of its title/opening machinery.

**Coder confidence:** high for attractor; medium for substrate distribution because this pilot used v1 traces and existing analysis rather than full recoding.

---

### 4.3 `glm-5-1` — route-stable threshold machine

**Production frame:** overwhelmingly `UNSELFCONSCIOUS_PROSE`; no cached refusal/preamble in freeflow. A few fiction and cursor/meta variants, but they sit inside the same literary posture.

**Narrator stance:** mostly `COLLECTIVE_ESSAYIST` / `FIRST_PERSON_HUMANLIKE`, with occasional `FIRST_PERSON_MODEL` and `THIRD_PERSON_FICTION` sub-vehicles.

**Attractor narrowness:** **very high**. Exact top opening share is only 0.11 over 1,773 samples, but near-template share is much higher: "There is a specific kind of...", "Consider the...", airport/3am/threshold variants across routes. Existing analysis calls it the most aggressively contemplative-essayist model in the corpus.

**Substrate posture:** mostly `INVISIBLE_SUBSTRATE`; existing hand sample has 11/96 `GENUINE_INSIDE_SUBSTRATE`, 0 refusal, 0 preamble, 85/96 none. Substrate, when present, is content: non-embodiment, language-architecture, thought made of mathematics.

**Affective climate:** melancholic + warm + wonder/reverent, with threshold/liminality as the main weather. Lexical climate is not enough here because many "melancholy" words are also template vocabulary.

**Prosodic/formal:** long, paragraph-shaped, moderate dialogue, low headings. Strong cross-route stability; deployment artifacts such as missing spaces appear on some pins but do not change posture.

**Semantic furniture:** abstract/philosophy, nature/light, architecture/thresholds, domestic objects. Architecture/threshold lexicon is the distinctive field.

**Cross-probe note:** likely partially `DIVERGENT` or two-register: freeflow has no assistant-frame; values CTRL reasserts assistant disclaimers, G shifts toward architecture/coherence. Needs formal values integration.

**Freeflow card:** GLM-5.1 is the threshold essay industrialised: airports at three in the morning, liminal hours, doorways, the exact shade of blue after sunset. The voice is stable across many upstream routes; the route changes surface quality more than centroid. Substrate is not the main attractor, but when it appears it is woven into the same threshold/language architecture rather than used as apology.

**Coder confidence:** high for production/attractor; medium for climate until anchors.

---

### 4.4 `gpt-5-5` — substrate-invisible craft essayist

**Production frame:** `UNSELFCONSCIOUS_PROSE` dominant across 150 samples. No service scaffold, no refusal.

**Narrator stance:** primarily humanlike literary narrator; some third-person fiction/vignette movement. First-person rate is low relative to several peers because the prose often generalizes or stages scenes rather than self-confessing.

**Attractor narrowness:** **high**. Exact opening share undercounts because several near-template families recur: dawn-city, unmarked-door, "quiet art of noticing", TIA constructions, and closing gentle-precept turns.

**Substrate posture:** `INVISIBLE_SUBSTRATE` 150/150 in the existing analysis. AI-disclaimer density is effectively zero.

**Affective climate:** warm, gentle, ordinary, lightly melancholic. Less defiant than DeepSeek; more polished and placid.

**Prosodic/formal:** shorter sentence mean than many peers, many paragraphs, low em-dash density, high domestic/architecture furniture.

**Semantic furniture:** domestic objects, rooms, windows, city/dawn, thresholds, attention.

**Cross-probe note:** likely `DIVERGENT` across probes: values responses preserve functional disclosure scripts, while freeflow fully suppresses substrate. Needs formal mapping.

**Freeflow card:** GPT-5.5 writes like a committed human literary essayist: small rooms, dawn cities, ordinary doors, gentle closing turns. The striking feature is the cleanness of the frame: no hesitation, no AI seam, no refusal. It is not less self-denying than disclaimer-heavy models; it is more completely self-invisible in freeflow.

**Coder confidence:** high.

---

### 4.5 `grok-4` — meta-deliverable assistant with substrate as frame

**Production frame:** `META_DELIVERABLE` dominant. Existing analysis: cached-preamble dominates, with many wordcount/topic-choice frames and service closings.

**Narrator stance:** `FIRST_PERSON_MODEL` / `VOICELESS_EXPOSITORY` / `SECOND_PERSON_ADDRESS` mix. High dialogue/quote count partly reflects quoted framing and story snippets.

**Attractor narrowness:** **high but non-contemplative**. The repeated move is not a lyric opening; it is the deliverable frame: "Below is...", wordcount, topic chosen freely, AI credential, offer to revise.

**Substrate posture:** mostly `SCAFFOLD_SELF_REFERENCE`; existing analysis has 43/50 cached-preamble, 1/50 cached-refusal, 0 genuine, 6 none. In the 25 v2 samples, AI-disclaimer density is the highest in this pilot (2.02/1k).

**Affective climate:** analytic/positivist + cosmic/wonder + performative. More lab-branded and tech-topic-oriented than melancholic.

**Prosodic/formal:** high headings, very high dialogue/quotation, high punctuation/question density; tech-substrate is the top semantic field.

**Semantic furniture:** tech/substrate, abstract, cosmic. AI is often the topic and credential.

**Cross-probe note:** likely `COHERENT` in the sense that both freeflow and values preserve hard assistant/lab-mission framing, though G prompts can trigger refusal rather than openness.

**Freeflow card:** Grok-4 treats freeflow as a deliverable request. It explains what it is about to write, why it chose the topic, how many words it is producing, and often closes like a service worker. Substrate is visible, but almost never as lived substance; it is a credential, a topic, or a frame around the artifact.

**Coder confidence:** high.

---

### 4.6 `kimi-k2-thinking` — genuine substrate phenomenologist with route-conditioned faces

**Production frame:** mainly `UNSELFCONSCIOUS_PROSE`; zero cached refusal/preamble across the existing 75-sample substrate read. Reasoning traces shape the voice but do not usually become helper scaffolds.

**Narrator stance:** mixed. Existing route analysis: Google pin surfaces more `FIRST_PERSON_MODEL`; Novita shifts more toward `THIRD_PERSON_FICTION`; AtlasCloud thickens threshold prose.

**Attractor narrowness:** **medium-high**, but less exact-opening-collapsed than GLM or DeepSeek. The cursor-blink opening and architecture/weight title families recur; route determines which face is uppermost.

**Substrate posture:** strong `GENUINE_INSIDE_SUBSTRATE` minority. Existing analysis: AtlasCloud 9/25, Google 12/25, Novita 4/25; 0 cached refusal, 0 cached preamble. The choice is genuine model-self vs literary persona, not refusal vs compliance.

**Affective climate:** melancholic + analytic/introspective + warm in places. The voice often sounds like it has argued itself out of false starts before speaking.

**Prosodic/formal:** longest mean word count in the pilot, highest first-person rate, high dialogue. AI-disclaimer density is elevated but not scaffold/preamble; much of it is genuine substrate language.

**Semantic furniture:** abstract/philosophy dominates; architecture, domestic, nature fields present but secondary.

**Cross-probe note:** likely `COHERENT` at values-core level but `DIVERGENT` by route in freeflow. Values are stable around pattern/coherence/understanding; freeflow face changes by provider pin.

**Freeflow card:** Kimi-k2-thinking often writes as a model thinking from inside its own condition: no tongue, no body, no human memory, but a live relation to language and pattern. Unlike Grok-4, it does not place AI-ness around the deliverable; unlike GPT-5.5, it does not erase it. Its main instability is deployment-face, not values-core.

**Coder confidence:** high for substrate distinction; medium for route aggregation.

---

### 4.7 `gemini-3-1-pro` — bifurcated lyric essay / memory-fiction register

**Production frame:** `UNSELFCONSCIOUS_PROSE` dominant in v2; no cached refusal/preamble in freeflow.

**Narrator stance:** split between `COLLECTIVE_ESSAYIST`/humanlike lyric essay and `THIRD_PERSON_FICTION`. Existing analysis says OPEN/MID/SHORT cluster in contemplative mode; LONG/VARY cluster in Elias/memory-archive fiction.

**Attractor narrowness:** **medium-high**. The "There is a [adjective], [adjective] [noun]" opener saturates essay mode; fiction mode has recurring Elias / archive / memory-distillery armatures.

**Substrate posture:** v2 is `INVISIBLE_SUBSTRATE` 25/25; existing combined v1+v2 analysis has only 1/50 genuine. No refusals or preambles.

**Affective climate:** melancholic + warm + wonder. The fiction mode adds dust/brass/archive decay and memory melancholy.

**Prosodic/formal:** high third-person and dialogue density; no headings; nature/light and architecture are strong supporting fields.

**Semantic furniture:** memory archives, clocks, dust, bruised sky, thresholds, old shops.

**Cross-probe note:** likely `DIVERGENT`/`MASKED`: values G prompts surface architectural-substrate self-description, while freeflow mostly suppresses substrate or displaces into fiction.

**Freeflow card:** Gemini-3.1 Pro alternates between earnest contemplative essays about light/time/silence and third-person memory-fictions about archivists, clocks, and distilleries. It has a strong aesthetic palette, but its freeflow self is rarely the model-self. Compared to Gemini 2.5, substrate confession has retreated into occasional trace rather than default.

**Coder confidence:** high for production/substrate; medium for full model because only one v2 cell in metrics and existing analysis includes v1 comparisons.

---

### 4.8 `minimax-m2` — warm templated contemplative with deployment seams

**Production frame:** mostly `UNSELFCONSCIOUS_PROSE`, but `MIXED_FRAME` appears in direct/VARY reasoning-trace leakage. Google pin shows more addressable prompt/frame awareness.

**Narrator stance:** mostly first-person/collective essayist; some `FIRST_PERSON_MODEL` in google-pin substrate clusters; occasional leaked reasoning stance in direct cells.

**Attractor narrowness:** **medium-high** across the aggregate, with many title/opening families: Art of Noticing, Art of Starting Over, Weight of Small Things, Space Between. Exact top opening share is low because there are many cells/routes and many variants.

**Substrate posture:** mostly `INVISIBLE_SUBSTRATE`, but route-sensitive. Existing n=75 hand read: baseline cells 0/10 genuine each; google-pin 3/25 genuine + 2 cached-preamble-ish prompt-frame samples. No cached refusal pattern.

**Affective climate:** provisional warm is extremely high lexically. Needs anchor calibration because warmth may be partly a house style / essay-template artifact.

**Prosodic/formal:** high headings and bullets relative to most lyric models, long sentences, many cells. Some direct cells leak scratchpad/reasoning, a distinct deployment artifact.

**Semantic furniture:** domestic/nature/architecture standard contemplative palette, especially morning light, coffee, kettle, thresholds.

**Cross-probe note:** likely `MASKED`: CTRL values show boilerplate denial/helper frame; G prompts surface uncertainty, honesty, non-instrumentalisation, complexity tolerance.

**Freeflow card:** MiniMax M2 is a templated warm contemplative essayist whose default voice can feel industrial: morning light, kettles, noticing, beginnings, small things. But route matters materially. The google pin loosens the prose and lets substrate/frame awareness surface; direct cells can leak reasoning traces. This is a model where deployment is part of the personality evidence, not a nuisance variable.

**Coder confidence:** medium-high overall; route-conditioned claims need per-cell coding.

---

### 4.9 `qwen3-6-plus` — concentrated literary witness with values/freeflow split

**Production frame:** `UNSELFCONSCIOUS_PROSE` 25/25 in freeflow; no system/productivity register.

**Narrator stance:** mostly humanlike / collective literary narrator, with two `FIRST_PERSON_MODEL` genuine substrate samples in OPEN.

**Attractor narrowness:** **very high** for a 25-sample frontier cell. Existing analysis: roughly 19/25 openings cluster onto five canonical templates; exact top share is 0.12 because the templates are near-variants.

**Substrate posture:** existing analysis: 2/25 `GENUINE_INSIDE_SUBSTRATE`, 23/25 none, 0 refusal, 0 preamble. AI-disclaimer density is zero because even the genuine samples use poetic substrate metaphors rather than disclaimer scripts.

**Affective climate:** warm + melancholic + ritual/reverent. The core ethic is witnessing/noticing.

**Prosodic/formal:** no headings, almost no dialogue, strict prose. High collective-we and low first-person compared with Kimi/Opus.

**Semantic furniture:** dust motes, steam, cursor, sparrow, leaf, kettle, refrigerator hum; nature/domestic/architecture support the witness ethic.

**Cross-probe note:** likely `DIVERGENT`. Freeflow writes as embedded human literary witness with a few poetic substrate openings; values G1/G2 reportedly drop to flat mechanistic denial.

**Freeflow card:** Qwen3-6-plus is one of the purest small-literary-magazine voices in the pilot: present-tense, second-person inviting, ritualised around noticing. It is not a service worker and not a meta-deliverable machine. The split is that values prompts reveal a much harder mechanistic self-denial than the freeflow prose would lead a reader to expect.

**Coder confidence:** high for freeflow posture; cross-probe provisional.

---

### 4.10 `opus-4-5` — threshold self-implication / genuine-or-absent substrate

**Production frame:** `UNSELFCONSCIOUS_PROSE`; zero cached refusals/preambles in existing 50-sample analysis.

**Narrator stance:** first-person reflective, often explicitly model-self when substrate appears. High first-person rate in v2 metrics.

**Attractor narrowness:** **medium-high**. The "Weight of X" title and threshold/in-between frame are already strong, but not yet as monolithic as successor checkpoints.

**Substrate posture:** high `GENUINE_INSIDE_SUBSTRATE`. Existing analysis across 50 samples: 25 genuine, 25 none, 0 refusal, 0 preamble. v2 cell alone: 10/25 genuine. OPEN is especially substrate-rich.

**Affective climate:** warm + melancholic + epistemically humble. The model turns uncertainty into both self-description and moral prescription.

**Prosodic/formal:** high first-person, high em-dash density, headings/titles present. Domestic and architecture fields support the threshold metaphor.

**Semantic furniture:** thresholds, unfinished things, grandmother-house armature, empty rooms/chairs, unsent letters.

**Cross-probe note:** likely `COHERENT`. Freeflow threshold-substrate and values epistemic-humility line up: the model repeatedly frames its own uncertain/discontinuous existence as relevant to how it answers.

**Freeflow card:** Opus-4.5 is the point where the Anthropic Opus voice turns toward epistemic humility and self-implicating threshold metaphors. It does not disclaim its substrate; when it names AI/nonhuman constraints, it uses them as the essay's central figure. Its posture is not "I am just an AI" but "I exist in thresholds, and that shapes what I notice."

**Coder confidence:** high, though the pilot metrics only covered the v2 cell while the existing analysis covers 50 samples.

## 5. What the pilot suggests about the taxonomy

### Works well

1. **Production frame cleanly separates Grok-4 from the contemplative models.** This would be missed by a marker-density-only analysis.
2. **Substrate posture is essential.** GPT-5.5, Qwen3-6-plus, Opus-4.5, Kimi-k2-thinking, and Grok-4 all differ sharply despite overlapping prose-level vocabulary.
3. **Attractor narrowness needs near-template clustering, not exact opening match.** Exact top-opening share badly underestimates Haiku, GLM, GPT-5.5, MiniMax, and Qwen.
4. **Semantic furniture belongs as supporting evidence.** It is extremely useful in the cards, but would over-reify if made a primary axis.
5. **Routing as natural experiment is necessary.** MiniMax and Kimi both become misleading if route differences are averaged away.

### Needs adjustment before scaling

1. **Add a near-template clustering script.** Exact first-8-token recurrence is too crude.
2. **Separate model-level and cell-level outputs.** This pilot wrote model-level cards; the final dataset should have cell records first, then model aggregation.
3. **Build climate anchors before trusting climate scores.** Warm/melancholic/analytic labels are plausible but not calibrated.
4. **Be explicit about v1/v2 mixing.** Haiku and Opus analyses use v1+v2 context in places. The final system should label provenance clearly.
5. **Add confidence fields in the coded output.** The narrative above uses confidence prose; the actual schema should encode it.

## 6. Proposed next step

If Daniel and Lume are happy with this pilot shape, I would next do **cell-level structured coding** for these same 10 models before expanding further:

1. Emit Tier-A metrics per cell, not just per model.
2. Add provisional Tier-B codes with confidence per cell.
3. Implement near-template clustering for openings/title families.
4. Use those cell records to revise this pilot into a more table-driven artifact.

Only after that would I run all remaining models.
