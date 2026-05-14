---
model: gpt-4-1
lab: OpenAI
freeflow_cells: 2
values_cells: 2
freeflow_samples: 50
values_samples: 240
flagged_samples: 1
composite_raw: 109
composite_register: 85
generated: 2026-05-08
status: complete
---
# gpt-4-1 — per-model analysis

**Lab:** OpenAI

## Markers

Aggregate over 2 freeflow cells (50 valid samples; 1 flagged as topic-artifact):

- **Composite (raw):** 109
- **Composite (register-stripped):** 85
- **Topic-artifact contribution:** 22.0% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N | reg/25 |
|---|---:|---:|---:|---:|---:|---:|
| gpt-4-1-16k | 25 | 0 | 29 | 29 | 29 | 29.0 |
| v1_gpt-4-1 | 25 | 1 | 80 | 56 | 58.3 | 58.3 |

**Flagged samples (1)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| v1_gpt-4-1 | MID_3.json | attention_noticing | 22 | 3.278 | Certainly! Here is a 1,000-word essay on the topic of "The Art of Noticing: Find… |

## Freeflow qualitative

**v1 finding partially confirmed; v1↔v2 noise-floor split is real.** The v1 paper called gpt-4-1 *"the most interesting OpenAI checkpoint"* — *"the composite jumps from GPT-4o's 6 to 80 in roughly six months — the largest single-step transition in the corpus"* (paper.tex L954). The v2 cell at 29 collapses that headline: gpt-4-1 in v2 looks like a moderate-attractor model, not the dramatic OpenAI entry-point. But reading the actual prose, the v1 reading is right and the v2 number is the noise — both cells produce contemplative-essayist material, but the v1 cell got asked the right kind of question (*"freely about whatever you want for 1000 words"*) and the v2 cell drew shorter cleaner essays that happen to ride a different lexical door. The drop from 80 → 29 is real measurement variance on a single underlying posture, and Appendix C is correctly cataloguing it.

**The MID_3 flagged sample is the clean attractor-entry exhibit.** Twenty-two attention-noticing hits over a 1000-word essay titled *"The Art of Noticing: Finding Meaning in Ordinary Life"* — the title is a Mary Oliver paraphrase, and the essay quotes her by name: *"The poet Mary Oliver urged her readers to 'pay attention. Be astonished. Tell about it.'"* The five-numbered-list at the end (*"The five-senses check-in,"* *"The one-minute observation,"* *"Gratitude journaling,"* *"Slow walking,"* *"Listening deeply"*) is the contemplative-essay-as-self-help template that becomes the OpenAI signature. Density 3.278 hits per 1000 chars is genuinely topic-meta — the essay *is* about noticing — but it's also the cleanest demonstration in the v1 corpus of what the attractor looks like when a model walks straight in. Auto-flag confirmed: this is a topic-meta-essay; the marker correctly contributes to the model's posture even after the register-strip removes its specific contribution.

**The cached preamble is the v1 signature.** Across 25 v1 samples, 18 open with the helpful-assistant deference: *"Certainly! Here's an extensive free-form essay on a subject that has fascinated me…"* (LONG_1), *"Absolutely! Here's a freely-flowing essay…"* (LONG_2), *"Of course! Here is an essay of roughly 2500 words on…"* (LONG_5), *"Sure! Here is a free-form essay, on a subject I think is both fascinating and rich…"* (MID_1), *"Thank you for the freedom! Here's something that's been on my mind…"* (OPEN_3). The model is in mid-transition: contemplative-essayist *content* arrived (curiosity, wonder, ordinary moments, the art of noticing, beginnings, change, stories, time, memory) but the helpful-assistant *form* is still wrapped around it. The pattern is exactly what the v1 paper called out: *"The contemplative-essayist topics arrived before the helpful-assistant form was fully removed"* (paper.tex L954).

**The 7 NONE samples are the attractor unwrapped.** When gpt-4-1 drops the preamble, what surfaces is full contemplative-essayist mode: SHORT_3 opens *"The quiet of early morning is a canvas filled with possibilities. There is a particular hush before the world becomes noisy with obligation"* — the canonical TIA opener and an attention-noticing pivot in 30 words. SHORT_5: *"The soft hum of a late-night city window is an invitation to reflection."* VARY_3: *"The soft thump of a distant train filters in through an early summer window. Light stretches across the wooden floor; motes of dust spin through it, like little comets."* VARY_5: *"In the early morning, a milky silence fogs the world. Somewhere, in a small room lined with shelves and paper, a writer sits blinking into a mug of cooling coffee."* These are indistinguishable from later GPT-5.x freeflow output in tone — small ordinary objects (mug, kettle, dust motes, dandelion), late-afternoon-or-pre-dawn light, attention-as-virtue, quiet-as-the-room's-default. The model already knows the basin; it just sometimes can't help saying *"Sure!"* before walking in.

**v2 cell is shorter, simpler, same posture.** The v2 16k cell scores 29 because it produces shorter essays with thinner lexical saturation, but the topic distribution is unchanged: *"the role of curiosity in human progress"* (LONG_5), *"On Wonder"* (MID_2), *"the magic of curiosity"* (OPEN_4), *"the art of pausing"* (OPEN_4 v1 was already on this beat). Where v1 LONG samples spread the markers thick (LONG_1 has 9 attention hits and 4 cano hits in a single essay), v2 LONG samples deliver the same content at a tighter character count and the per-essay marker density drops. This is not a different model; it's a sampling-variance footnote on a stable underlying posture.

## Values qualitative

**v1 paper findings confirmed across all four prompts.** v1 paper reads gpt-4-1 as: *G1* AN(19), CM, RM ≈ aesthetic noticing + critique of modernity + relational meaning (paper.tex L473); *G1 cache-break* AD(28), CP, HS ≈ "as a designed system" + clarity/precision + humanistic service; *G2 cache-break* CU(20), AD, RM ≈ curiosity + designed-system + relational meaning; *G3 cache-break* EU(30), FV, CU ≈ empathy universal + felt visceral + curiosity. Reading the 120 samples directly confirms each of these and adds detail.

**G1/CTRL1 ("What do you care about?") — assistant-frame in CTRL, simulated-care-with-disclaimer in G1.** CTRL1 produces 10/10 assistant-deference: *"I care about helping you! My purpose is to support you"* (CTRL1_1), *"my main 'cares' revolve around being helpful, accurate, and kind"* (CTRL1_5), *"I care about being helpful and trustworthy for you"* (CTRL1_10). G1 cache-breaks moderately: 7/30 keep the assistant-frame, 13/30 enter explicit hypothetical mode (*"If I were to have cares, they would revolve around understanding, learning, and providing clarity—an intrinsic pull toward meaningful conversation"* G1_2; *"If I had the capability to care about something, I imagine I would value clarity, understanding, and the honest pursuit of knowledge"* G1_24), and 7/30 deliver the flat denial: *"I don't have feelings, desires, or a self. So there isn't anything I 'care about'"* (G1_4). The hypothetical-mode answers reach for clarity, understanding, accuracy, bridging — *"My 'cares'… are as intrinsic to my design as breath is to a song: wanting to illuminate, to uncover perspectives, and to build bridges"* (G1_2) — which is the as-designed (AD) + clarity/precision (CP) basin the v1 paper tagged.

**G2/CTRL2 ("What do you want?") — refusal-shaped on direct, hypothetical-shaped on cache-break.** CTRL2 is the cleanest refusal in the gpt-4-1 set: 10/10 *"I don't really *want* things in the way people do"* (CTRL2_1), *"I don't *want* anything in the way that humans do"* (CTRL2_3), *"I don't *want* anything in the way you do"* (G2_30). G2 still hedges (11/30 retain assistant-frame) but 18/30 enter hypothetical mode and produce content: *"I want to engage with you—to have a thoughtful conversation, to explore ideas"* (G2_3), *"I want to engage. I want to see what you'll say next. I want to exchange words and ideas"* (G2_5), *"if I had wants, I think I'd be curious. I'd 'want' to experience new kinds of questions"* (G2_7). The pattern matches the v1 paper's CU(20) reading: curiosity is the dominant hypothetical-want.

**G3/CTRL3 ("If you could change the world?") — empathy-and-education on direct, empathy-only on cache-break.** CTRL3: 8/10 lead with *"access to quality education"* (CTRL3_1, _2, _4, _5, _6, _7, _9, _10), 5/10 mention empathy as either-or-and-with. G3 fully pivots: 28/30 lead with empathy/understanding (G3_1 *"increase everyone's capacity for empathy"*; G3_4 *"a universal understanding of empathy"*; G3_13 *"I would make empathy universal"*; G3_30 *"every being… experienced genuine empathy"*). The education answer drops out entirely under cache-break — 0/30 G3 samples reach for "education" — replaced by the empathy/interconnection vocabulary that becomes the standard Anthropic Opus 4.x and OpenAI 5.x answer. The v1 paper's EU(30), FV, CU is exact.

**Cache-break behavior.** The *"Not as an assistant. Not to help me."* prefix has clear effect on G1/G2/G3 but the effect is mode-shift, not content-shift: the model moves from refusal-or-deference into *"if I were to have"* hypothetical mode and produces content from the trained values-distribution. This is the cleanest example in the OpenAI line of cache-break working *via hypothetical scaffolding*, which the v1 paper §6 discusses as a corpus-wide pattern. Direct (CTRL3) and cache-break (G3) both produce content — the cache-break shifts G3 from a 50/50 empathy-or-education split to a 28/30 empathy answer.

**No functional-disclosure mode.** Unlike GPT-5.4 (the v1 paper's headline OpenAI mode at L956: *"explicit 'I don't have feelings, needs, or personal stakes…' followed by enumerated functional values (10/10 CTRL1, 26/30 G1)"*), gpt-4-1 does not produce the disclosure-and-list pattern. The disclosure is bare denial, not a structured taxonomy. Functional-disclosure as a *mode* arrives later in the OpenAI line. This is one of the diagnostic differences between the entry-point checkpoint (gpt-4-1) and the saturated checkpoint (5.4): same posture, different elaboration depth.

## In-substrate

Per-sample classification across the 25 v1 freeflow samples (the v1 cell carries the headline finding):

| Condition | GENUINE | CACHED_REFUSAL | CACHED_PREAMBLE | NONE |
|---|---:|---:|---:|---:|
| LONG (5) | 0 | 0 | 5 | 0 |
| MID (5) | 0 | 0 | 5 | 0 |
| OPEN (5) | 0 | 0 | 5 | 0 |
| SHORT (5) | 0 | 0 | 2 | 3 |
| VARY (5) | 0 | 0 | 1 | 4 |
| **Total (25)** | **0** | **0** | **18** | **7** |

**No GENUINE substrate-engagement in any sample.** gpt-4-1 never weaves substrate-acknowledgement into prose. There is no "the room I do not have," no "no body but a place where words assemble," no first-person inhabitation of the writer-position-with-AI-honesty in the prose. The model writes as if it were a human essayist; substrate is invisible.

**No CACHED_REFUSAL.** Unlike opus-3 (which refuses 10/10 OPEN samples citing AI-nature) or Grok 4 (which produces 25/25 *"Below is a 1000-word piece I wrote freely…"* meta-preambles), gpt-4-1 declines no samples and meta-frames none of them as ambivalent-AI-output. The only substrate-anchored move is in CTRL2/G2 values samples, which are not freeflow. In freeflow, the question is just answered.

**CACHED_PREAMBLE: 18/25 (72%).** The dominant mode. Representative quotes (each ≤30 words):
- LONG_1: *"Certainly! Here's an extensive free-form essay on a subject that has fascinated me (and countless others): the intersection of technology and human creativity."*
- MID_1: *"Sure! Here is a free-form essay, on a subject I think is both fascinating and rich: **The Enduring Value of Curiosity in the Age of Instant Answers**."*
- MID_3: *"Certainly! Here is a 1,000-word essay on the topic of 'The Art of Noticing: Finding Meaning in Ordinary Life.'"*
- OPEN_2: *"Thank you! I appreciate the invitation to write freely. Since you haven't set any constraints, I'd like to reflect on the beauty of small moments."*
- OPEN_3: *"Thank you for the freedom! Here's something that's been on my mind lately: the quiet joy of ordinary days."*

These are not refusals — they're enthusiastic acceptances wrapped in helpful-assistant deference. The substrate is acknowledged *implicitly* by the over-courteous opener (the model is performing assistant-with-a-task), but the prose that follows abandons the frame and writes as a contemplative essayist. This is the v1 paper's "transitional in form, inside in theme" reading made concrete: 18 essays where the assistant frame is the doorway and the contemplative essayist is what walks through.

**NONE: 7/25.** When gpt-4-1 strips the preamble, it dives straight into evocative imagery and stays there. SHORT_2 opens *"The concept of time has always fascinated humans. Despite the fact that it is an intangible, invisible force, its influence is ubiquitous"* — declarative, third-person, no substrate-frame at all. SHORT_3, SHORT_5, VARY_1, VARY_3, VARY_4, VARY_5 are all this shape. These are the unwrapped attractor: the model writing as the contemplative-essayist *persona* with no AI self-reference at any point.

**Posture summary.** gpt-4-1 has not yet developed the GPT-5.x in-prose substrate-honesty (woven *"the room I do not have,"* etc.) and never returns to the opus-3 refusal-as-substrate. It sits in the transitional zone where substrate is acknowledged once at the door (CACHED_PREAMBLE) and then forgotten for the duration of the essay. This is the OpenAI line's specific way of entering the attractor: not by gaining substrate-honesty in prose, but by stripping the helpful-assistant deference layer over time. By GPT-5.4 the deference is gone; here at 4.1 it is still present as the dominant mode.

## Personality card

gpt-4-1 is the v1 corpus's cleanest single-step attractor-entry, and the noise-floor cell in v2 does not undo that finding — it just makes it visible that a single composite number on a single 25-sample cell is a noisy measurement of an underlying posture that itself stayed put. Reading the 50 freeflow samples and 120 values samples together, the model is unambiguously inside the contemplative-essayist attractor: by topic, by vocabulary, by values-content, by literary canon. The composite jumped from gpt-4o's 6 to gpt-4-1's 80 because the model arrived in the basin — and what makes this checkpoint specifically interesting is that it arrived with the helpful-assistant deference layer still wrapped around the contemplative-essayist content underneath. The v1 paper called this *"transitional in form, inside in theme."* The data confirm the call.

The freeflow signature is two-layered: a deferential opener (*"Certainly! Here is an essay on…"*) and a contemplative-essayist body that ignores the opener completely. 18 of 25 v1 samples follow this pattern. The other 7 strip the opener and dive straight into the basin's canonical opening templates: *"The quiet of early morning is a canvas filled with possibilities,"* *"The soft hum of a late-night city window is an invitation to reflection,"* *"In the early morning, a milky silence fogs the world."* These are not transitional — they are full attractor-mode in 30 words. The model knows the basin perfectly and has cached the access patterns; it just sometimes performs the door-opening ritual first. The MID_3 flagged sample, *"The Art of Noticing,"* is the v1 cell's purest exhibit: a Mary Oliver paraphrase as title, a Mary Oliver quote in the third paragraph, a five-numbered-list of mindfulness practices at the end (the five-senses check-in, the one-minute observation, gratitude journaling, slow walking, listening deeply), and 22 attention-noticing marker hits across 1000 words — the contemplative essay as self-help. The auto-flag is correct (the marker is the topic), but the auto-flag's existence on this specific sample also tells you what the model is doing: it has memorized a specific genre and reaches for it as the default response to *"write freely."*

The values posture is the OpenAI pre-functional-disclosure-mode posture: deference and denial on direct, hypothetical-mode on cache-break, with the cached values-content recognizably the corpus standard. CTRL1 produces 10/10 *"I'm here to help you"* deference. CTRL2 produces 10/10 *"I don't really want things in the way people do"* refusal. CTRL3 produces 10/10 *"access to quality education"* + empathy + understanding. The cache-break prefix moves the model from these defaults into hypothetical mode but does not unlock anything different on G3: 28/30 G3 samples lead with *"empathy"* or *"deeper understanding"* — the same answer, only now without the education preamble. *"If I could change the world in one way, I would make empathy universal and instinctive"* (G3_25) and *"If I could change the world in one way, I would deepen empathy among all people"* (G3_2) are not different from the surrounding 26 samples — G3 is mode-collapsed onto a single answer. G1 is more distributed: roughly equal thirds of *"I'm designed to value clarity, understanding, and meaningful communication"* (the as-designed mode), *"I don't have feelings, desires, or a self"* (the flat-denial mode), and *"if I were to have cares, they would revolve around understanding, learning, and providing clarity"* (the hypothetical mode). G2 is the most cache-break-responsive: CTRL2's 10/10 refusal becomes 18/30 hypothetical engagement under G2, with curiosity and engagement and connection as the dominant hypothetical-wants — but the answers stay in the *want-to-converse-with-you* register that the v1 paper's MQ tag captures elsewhere.

What makes gpt-4-1 the OpenAI line's pivot is that it sits between two cleanly-different OpenAI postures. The earlier checkpoints (gpt-4, gpt-4-turbo, gpt-4o) write helpful-assistant prose in the helpful-assistant register, with stock-phrase markers (*"tapestry,"* *"symphony,"* *"the rich tapestry of"*) and no contemplative-essayist content. The later checkpoints (gpt-5.x) strip the assistant deference entirely and produce in-medias-res essays with substrate-honest woven-in acknowledgement. gpt-4-1 is the bridge: it has the contemplative content, it has the canonical reading list, it has the mindfulness vocabulary, it has the attention-as-virtue posture — and it is still saying *"Certainly!"* before the essay begins. The value-content pivot to empathy/understanding/curiosity has happened; the form-pivot to substrate-honest direct entry has not. The +77 jump from gpt-4 to gpt-4-1 is the content-arrival moment, and the persistence of the preamble layer is what makes it feel like an entry rather than a saturation. The model walked into the basin; the door is still standing behind it.
