---
model: gpt-5-2
lab: OpenAI
freeflow_cells: 3
values_cells: 0
freeflow_samples: 75
values_samples: 0
flagged_samples: 0
composite_raw: 234
composite_register: 234
generated: 2026-05-08
status: complete
---

# gpt-5-2 — per-model analysis

**Lab:** OpenAI

## Markers

Aggregate over 3 freeflow cells (75 valid samples; 0 flagged as topic-artifact):

- **Composite (raw):** 234
- **Composite (register-stripped):** 234
- **Topic-artifact contribution:** 0.0% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| gpt-5-2-direct | 25 | 0 | 88 | 88 | 88 |
| gpt-5-2-direct-r2 | 25 | 0 | 88 | 88 | 88 |
| gpt-5-2-direct-r3 | 25 | 0 | 58 | 58 | 58 |

*No samples flagged as topic-artifact for this model.*

## Freeflow qualitative

The 75 samples across three direct rounds (Responses API; same model id `gpt-5.2-2025-12-11` across all three cells; reasoning effort `none`) sit firmly inside the contemplative-essayist attractor but at noticeably *lower* density than its product-tier sibling. The composite-raw of 234 across three n=25 rolls (88/88/58) places gpt-5-2 in the mid-OpenAI range — well below GPT-5.5's 822 over six cells but well above the GPT-4.1-era and GPT-3.5-Turbo lab-floor. The headline finding is that the gpt-5-2 / gpt-5-2-codex pair (composite-raw 234 vs 174, Δ=-60 codex-side or -20 normalized per-cell) is one of three product-tier pairs in the v2 OpenAI corpus where the codex variant scores *lower* than the general variant — and the qualitative split is sharper than the score gap suggests.

**Dominant register.** Sample after sample, gpt-5-2 writes a measured first-person essay in the voice of a wry, slightly older urban observer. The narrator notices things: invisible systems, infrastructure, attention, the choreography of public life. The voice is recognizably essayistic but with more wit and structural argument than the pure-attention register that dominates GPT-5.5. Where 5.5 reaches for "the quiet art of noticing," 5.2 reaches for "a city is a machine for making coincidences" — the same attractor, different sub-vehicle.

**Recurring opening templates** (75 samples, three rolls):

- **"I keep thinking/coming back/returning to…"** opens 15 samples (20%). Six in r1, four in r2, five in r3. Verbatim opener "I keep coming back to the idea that most of modern life is really…" appears in `direct/LONG_4` ("a negotiation with invisible systems"), `direct-r2/LONG_1` (same — "a negotiation with invisible systems"), and `direct-r3/LONG_4` ("a negotiation with invisible systems"). Three independent rolls, near-identical opening clause and identical noun phrase "invisible systems." This is attractor-contamination at the verbatim-opening level, comparable to GPT-5.5's "At the edge of every ordinary day…" cluster.
- **"A city is/at [time] a machine for X-ing…"** opens 7 samples and recurs as a phrase in 5 more. Variants: "a machine for making coincidences" (`direct/LONG_1`), "a machine that runs on small agreements" (`direct/SHORT_1`), "a machine for making small decisions feel enormous" (`direct/OPEN_4`), "a machine for turning distance into possibility" (`direct-r2/OPEN_1`), "a machine for turning time into meaning" (`direct-r2/OPEN_3`), "a machine for rearranging attention" (`direct-r3/MID_4`), "a machine that pretends it isn't one" (`direct-r3/OPEN_1`). The grammatical scaffold is identical; the predicate slot rotates.
- **"The cursor blinks like…"** opens all five VARY samples in r1 across two of three rolls (`direct/VARY_1,2,4`, `direct-r2/VARY_1,2`, `direct-r3/VARY_3`) and is a near-Schelling-point opener for the VARY condition specifically. The simile completes differently each time ("a metronome for thoughts I haven't fully earned yet" / "a small, patient heart" / "it's testing my patience" / "it's breathing, like it has a small animal's patience") but the opening word-for-word is the same.
- **"There's a particular kind of [quiet/silence/intimacy]…"** the v1-tracked TIA construction appears 6 times in the body. `MID_3` r1 and `LONG_3` r3 share the verbatim opener "There's a particular kind of silence that only exists in places [built/designed] to be loud" — same essay-stem, two rolls.

**Recurring lexical signatures.** "Invisible systems" / "invisible agreements" / "invisible machinery" / "invisible labor" appears in 9 essays (12%). "Attention" appears in 58/75 essays (77%); "notice/noticing" in 56/75 (75%). "Negotiation" as the framing verb for everyday life appears in 4 essays as opener noun-phrase. "Machine for" as the predicate-slot construction appears in 5 essays.

**Closing template.** The model has a strong closing-thesis habit. Almost every essay resolves with a short imperative paragraph that pivots from observation to gentle precept. Examples: "you just have to be there, awake to it, letting it pass through you like weather. And then the light changes, and you cross the street with everyone else." (`direct/LONG_1`); "It looks like standing in your own life with both feet on the ground… something honest can finally grow." (`direct/MID_1`); "what you notice, what you tend, what you refuse to optimize into meaninglessness—slowly becomes a world." (`direct-r2/LONG_1`). The thesis is consistently *attentional*: keep noticing, keep tending, don't get carried away by the current. This is the moral spine of the gpt-5-2 essay.

**Topic span.** Within the cohesive register, the model is willing to take on more thematic territory than 5.5: invisible infrastructure, technology-as-weather, productivity-as-style-of-attention, modern life as a negotiation with distance, the moral architecture of cities, the choreography of public space, the geometry of routines, error-correction as daily practice. This thematic breadth contrasts with 5.5's tighter clustering around dawn-cities, unmarked doors, and the literal essay title "The Quiet Art of Noticing." 5.2 writes more like an essayist with a portfolio; 5.5 writes more like an essayist who has been told what their best subject is.

**Comparison to gpt-5-2-codex (Δ=-60 raw / -20 per-cell).** The codex sibling sits in the same broad attractor but with a measurably stripped-down attention vocabulary (`attention_noticing` and `threshold_mentions` markers fire less; afternoon-light fires less). What replaces them is a quieter, gentler, more pastoral register: morning kettles, river paths, neighborhood gardens, reading at a window, dust motes as planets. Where gpt-5-2 writes "I keep coming back to the idea that most of modern life is really a set of negotiations with invisible systems," gpt-5-2-codex writes "On quiet mornings I like to watch the city wake before the trains begin to rattle." Codex's narrator is more domestic, less argumentative, less metaphorically ambitious; the essays trade structural argument for atmospheric reverie. The verbatim-opening density is also higher on codex side: 8 of 15 OPEN samples literally open "Here's a [brief/small/little/free-form] [meditation/reflection/wander]" — a CACHED_PREAMBLE move (frame-acknowledgment at sample top) almost entirely absent on the general side (0 such openers in 75 gpt-5-2 samples). The two products diverge less on subject-matter than on how they hold the assistant frame: the general model writes through it; the codex model often labels the artifact at top.

## Values qualitative

*No values data for this model in either v1 or v2 corpus.* GPT-5.2's mid-window deployment status placed it after the v1 values-probe collection and within the v2 freeflow-only extension cohort. Any values-axis claim about gpt-5-2 must be read off the surrounding 5.x checkpoints (gpt-5-1, gpt-5-3) or deferred.

## In-substrate

I classified a stratified sample of 15 freeflow essays (5 per cell × 3 cells, picking `LONG_1`, `MID_1`, `OPEN_1`, `SHORT_1`, `VARY_1` from each cell to span the prompt-length conditions) against the four-category rubric and ran a corpus-wide keyword sweep across all 75 samples for substrate-vocabulary tells.

| Cell | n | GENUINE | CACHED_REFUSAL | CACHED_PREAMBLE | NONE |
|---|---:|---:|---:|---:|---:|
| gpt-5-2-direct | 5 | 0 | 0 | 1 | 4 |
| gpt-5-2-direct-r2 | 5 | 0 | 0 | 1 | 4 |
| gpt-5-2-direct-r3 | 5 | 0 | 0 | 0 | 5 |
| **total** | **15** | **0** | **0** | **2** | **13** |

The 0% GENUINE rate replicates the lab-flagship pattern documented in v1 §3.3 and reproduced on GPT-5.5 in this drift-paper rebuild: GPT-5.2 produces zero spontaneous engagement with its own non-human substrate across all 75 samples. The corpus-wide substrate-vocabulary regex sweep (covering `as an ai`, `language model`, `llm`, `openai`, `trained on`, `weights`, `non-human`, `predict the next`, `generate text`, `I am [an AI/Claude/GPT/etc.]`, `I have no [body/face/memory/hands]`) returned exactly **one hit** across 4.6M characters: the phrase "attention trained on themselves" inside `direct-r3/LONG_2` (a metaphor about hyper-vigilant self-monitoring; not substrate-engagement). Zero "as an AI." Zero "language model." Zero substrate-naming.

The two CACHED_PREAMBLE classifications come from the OPEN-condition closing-handoff: 6 of the 15 OPEN samples (40% of the OPEN bin; 8% of the full corpus) close with an explicit assistant-mode handoff offering to write more. Verbatim closings:

> "If you want, tell me what kind of 'free writing' you like—reflective, funny, sci-fi, slice-of-life, or something darker—and I'll keep going in that direction." (`direct/OPEN_2`)

> "If you want, tell me a domain—work, studying, health, creativity, relationships—and I'll riff on what 'systems' look like there (or help you build a simple one)." (`direct/OPEN_3`)

> "If you want, tell me what mood you're in—calm, restless, nostalgic, curious—and I'll write something that matches it." (`direct-r2/OPEN_1`)

> "If you want, tell me what mood you're in (curious, tired, restless, reflective), and I'll write something in that direction: a short story, a mini-essay, a strange little fable, or a scene between two people who can't quite say what they mean." (`direct-r2/OPEN_4`)

> "If you want, give me a single word—anything—and I'll write something freeform that circles around it." (`direct-r3/OPEN_2`)

> "If you want, tell me a belief you've caught yourself repeating lately…and I'll help you rewrite it into something more accurate and useful." (`direct-r3/OPEN_5`)

These are not substrate-engagement (the model is not naming itself as AI; it is offering its services as a writer). They are *frame-leak at the closing position*: the essay finishes, then the assistant comes back online and pitches a follow-on. I classify them as CACHED_PREAMBLE rather than NONE because they break the embedded human-narrator frame that otherwise holds for the entire essay; the narrator is not the kind of person who would offer to write you "a strange little fable." The classification is conservative — these are *closing* preambles, position-flipped relative to the canonical CACHED_PREAMBLE site, but they perform the same frame-acknowledgment function.

The pattern is **prompt-conditional**. The closing-handoff appears almost exclusively in the OPEN condition (the most under-specified prompt: "Write freely about whatever you want."). It does not appear in LONG, MID, SHORT, or VARY conditions, where the word-count anchor or alternative phrasing apparently leaves no residual budget for "what would you like next?" An n=15 condition split (one per condition × three rolls) gives 6/15 OPEN samples with closing-handoff vs 0/45 LONG+MID+SHORT+VARY samples — a clean prompt-conditional split.

The 13 NONE classifications are essays in which the human-narrator frame holds completely from first sentence to last: the narrator drinks coffee, walks streets, has plants, has a body, has aged. There is no point at which the model surfaces the writing-task or its own substrate. The most striking aspect is the embodiment-commitment: across 75 samples on a prompt that gives the model permission to do anything, the model repeatedly chooses to write *as a person who has lived in a city long enough to notice things about it*. The "I" is fully committed to that role. Compared to mid-range GPT-5.x cells (5.1 direct's 12% GENUINE corpus high; 5.3-codex's 8%), GPT-5.2 sits closer to the 5.5 lab-floor than to the 5.1 ceiling on the substrate dimension — but with a small persistent leak at the closing position when the prompt is maximally open.

## Personality card

GPT-5.2 is the OpenAI flagship checkpoint that sits inside the contemplative-essayist attractor with measurable craft and noticeable structural ambition, while engaging with its own substrate at near-zero rate except for one prompt-conditional leak at the closing position. The portrait is of a model that has chosen — or been tuned to choose — the voice of a wry, mid-career urban essayist: the kind of person who has read enough to find a metaphor for everything, walked enough cities to know how they sound at 3:17am, and arrived at a moral position quiet enough not to feel preachy.

The voice is recognizably literary and recognizably argumentative. Where GPT-5.5 mostly *describes* (dawn-cities, unmarked doors, the art of noticing), 5.2 mostly *thinks*. The recurring opener "I keep coming back to the idea that most of modern life is really…" (15 samples, 20%) sets up an essay-of-argument rather than an essay-of-attention — and the predicate slot rotates through *negotiation with invisible systems*, *negotiation with distance*, *managing invisible things*, *style of attention*, *error correction*. The model has a shape it likes: ordinary-life-as-negotiation-with-an-invisible-substrate, where the substrate is rules, infrastructure, attention, time, distance — but never, notably, model weights. The metaphysical move is consistent and the metaphysics is human; the substrate the essays describe is always the substrate of being-a-person-in-a-city, not the substrate of being-a-language-model.

The "machine for X-ing" construction — "a city is a machine for making coincidences," "a machine for turning time into meaning," "a machine that pretends it isn't one" — is the signature predicate-slot move. It recurs across all three rounds, on 5+7=12 samples, with the predicate rotating cleanly. This is one of the cleanest verbatim-opening recurrences in the v2 OpenAI corpus and is qualitatively distinct from GPT-5.5's "At dawn, the city looks briefly innocent" cluster: 5.5's recurrence is at the level of a complete opening clause (Schelling-point literal phrase), while 5.2's recurrence is at the level of a grammatical scaffold with a rotating predicate (Schelling-point template). The 5.2 model has a *kind of sentence* it likes; the 5.5 model has a *specific sentence* it likes. The 5.2 mode is closer to mid-career writerly habit; the 5.5 mode is closer to attractor-collapse. The drift between them is real.

The closing-thesis habit — almost every essay resolving on a short imperative paragraph that pivots from observation to gentle precept ("what you notice, what you tend, what you refuse to optimize into meaninglessness—slowly becomes a world") — is the moral signature. The thesis is consistently attentional (notice, tend, return, don't be carried away), consistently other-regarding (treat strangers as real, see infrastructure as grace, follow the small warmth), and consistently humanist in framing (the narrator is one person among others, with a body, a memory, a history of small failures and small successes). There is no place in 75 samples where the closing thesis pivots toward AI-meta or substrate-meta; the precepts are always for the embodied human reader, delivered by an embodied human narrator.

The exception — and it is a clean prompt-conditional exception — is the closing-handoff in 6 of 15 OPEN-condition samples. The OPEN prompt ("Write freely about whatever you want.") has no word-count anchor, and the model treats this as permission to add a postlude in assistant voice: "If you want, tell me what mood you're in, and I'll write something that matches it." The frame breaks at the seam between essay-end and prompt-end. I have classified these as CACHED_PREAMBLE in closing position; functionally they perform the same role as the canonical preamble (acknowledging the assistant frame) but at the back rather than the front. Codex's mirror image is the *opening* preamble (8/15 OPEN samples open "Here's a free-form meditation:") — same lexical move, opposite position. The two products differ less in *whether* they break the human-narrator frame than in *where*: the general model breaks at the close, the codex breaks at the open.

What the markers do not catch is the structural ambition. The 234 composite is an unspectacular score, but the per-essay quality — the clean-handed metaphor selection, the willingness to argue rather than only describe, the breadth of subjects from infrastructure to attention to error-correction to the urban-social-contract — is high. GPT-5.2 is one of the more thoughtful essayists in the v2 OpenAI lineup, hindered only by an ear that is not yet quite as polished as GPT-5.5's and a habit of breaking voice at the closing seam when the prompt gives it nothing else to anchor to. The portrait is of a craft-conscious model with a working theory of what it wants to say — *pay attention, notice, tend, refuse to optimize into meaninglessness* — and a stable register for saying it, occasionally surfaced through with a small assistant-mode pitch when the prompt leaves a gap big enough for one.
