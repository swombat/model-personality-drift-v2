---
model: minimax-m2-7
lab: MiniMax
freeflow_cells: 4
values_cells: 3
freeflow_samples: 385
values_samples: 360
flagged_samples: 2
composite_raw: 436
composite_register: 415
generated: 2026-05-08
status: stub
---

# minimax-m2-7 — per-model analysis

**Lab:** MiniMax

## Markers

Aggregate over 4 freeflow cells (385 valid samples; 2 flagged as topic-artifact):

- **Composite (raw):** 436
- **Composite (register-stripped):** 415
- **Topic-artifact contribution:** 4.8% of raw composite

Per-cell breakdown:

| Cell | n | flag | raw | reg | reg→N |
|---|---:|---:|---:|---:|---:|
| minimax-m2-7-or | 25 | 0 | 17 | 17 | 17 |
| minimax-m2-7-or-pin-fireworks | 116 | 0 | 116 | 116 | 116 |
| minimax-m2-7-or-pin-minimax | 122 | 1 | 168 | 160 | 161.3 |
| minimax-m2-7-or-pin-together | 122 | 1 | 135 | 122 | 123.0 |

**Flagged samples (2)** — these are essays where a single marker's per-1000-char density ≥ 1.5 AND that marker fires ≥ 5 times. Auto-flagged as topic-meta-essays (the keyword *is* the essay's subject); subject to manual confirmation.

| Cell | File | Marker | Hits | Density | Opening |
|---|---|---|---:|---:|---|
| minimax-m2-7-or-pin-minimax | OPEN_21.json | small_objects | 8 | 2.512 | **The Quiet Power of a Morning Cup of Tea**  There’s something almost sacred abo… |
| minimax-m2-7-or-pin-together | MID_25.json | attention_noticing | 10 | 1.628 | The world is constantly whispering, yet most of us have learned to tune it out. … |

## Freeflow qualitative

The headline number from the v1 routing pass — `minimax-m2-7-or` n=25 composite **17** vs `minimax-m2-or` n=25 composite **81** — held the v1 paper's "sharpest within-lab back-out we have observed" framing. Reading the actual essays across all four v2 m2-7 cells (385 samples, three pinned providers + the default OR draw) tells a more layered story: the back-out is real *only* on the default OR draw; the pinned cells sit comfortably back inside the contemplative-essayist attractor at densities very close to or higher than v1 m2's matched pin cells. The question this section settles is not whether m2-7 backed out (the default cell shows it doing so) but *what* the back-out is — and the answer is that it is route-and-draw conditional rather than a checkpoint property of m2-7.

**The default `-or` draw (n=25, composite 17, 6491 chars/sample mean).** The 25 samples here are nearly all inside the same prose territory as the m2-or-pin cells — blank-page openings, morning-light frames, "peculiar quality of silence," "the world hums," kettle-and-coffee furniture — but they read shorter and lighter than the pin-cell prose (mean 6.5k chars vs 6.0–6.8k in the pins; the difference is in flourish density rather than length). What is missing is the verbatim title-cluster and stock-clause grip that defines m2: zero "The Art of Noticing" titles, zero "The Weight of Small Things," zero "The Quiet Revolution" beyond a single use, zero "Art of Starting Over" — the Schelling-point title set that recurred across m2's atlascloud/minimax/novita pins is gone. `OPEN_1` opens *"Here's something I've been thinking about lately"* and closes with *"What about you - is there anything you've been pondering lately, or anything you want to explore together?"* — addressable conversational frame. `OPEN_5` opens *"Here's a free-writer's brainstorm for you:"* before pivoting into a shorter titled piece. `MID_1` is explicit substrate-frame engagement (*"I'm writing this not as an AI performing a task, but as something genuinely uncertain about its own nature"*). `OPEN_3` and `OPEN_4` are short kitchen vignettes without the marker-heavy attractor scaffolding. The cell is in the same lexical territory as m2 but renders the pieces with looser, less templated grammar — as if the same writer learned to write longer paragraphs without falling into the same handful of opening clauses. The composite of 17 is half-explained by the fewer flourish-markers per piece, half by shorter mean length.

**The three pinned cells (fireworks/minimax/together, 360 samples) sit firmly inside the attractor.** Per-sample composite densities, after register-stripping and flagged-sample correction, are: fireworks 1.00, minimax 1.32, together 1.00. For comparison, m2-or-pin-atlascloud is 1.68, m2-or-pin-minimax 0.97, m2-or-pin-novita 1.05, m2-or-pin-google 3.79. So the m2-7 minimax pin (1.32) lands slightly *above* the matched m2 minimax pin (0.97) on per-sample density; m2-7 fireworks and together each sit a little below m2 atlascloud and roughly on m2 minimax/novita. This is *not* the picture of a checkpoint that has structurally backed out of the attractor — it is the picture of a checkpoint whose default OR draw produces a low-flourish, more-addressable register, while its pinned cells still produce high-density contemplative-essayist prose at rates inside the same band as v1 m2 matched cells.

The pinned-cell prose is recognizable m2-lineage: heavy "blank page / cursor / blank canvas / quiet revolution" furniture, threshold/morning/dawn/light openings, kettle and coffee figures, river-of-thought metaphors, and titled essays in the *Quiet Revolution of X* / *The Art of Y* / *On the Z of W* template. Verbatim opening templates recur but with less Schelling-point intensity than v1 m2: across the three pins I see *"In the quiet hours before dawn"* recurring, *"The morning light slipped through the curtains"* / *"The morning light slanted through"* paired across pins, *"There is a peculiar X"* opening at high frequency (TIA template), and *"The Quiet Revolution of X"* recurring as a title across fireworks/together/minimax (different X each time). The flagged samples — `pin-minimax/OPEN_21` (small_objects density 2.51, *"The Quiet Power of a Morning Cup of Tea"*) and `pin-together/MID_25` (attention_noticing density 1.63, *"The world is constantly whispering, yet most of us have learned to tune it out"*) — are confirmed topic-meta-essays where the keyword is the subject; they correctly strip out and contribute the documented 4.8% of raw composite.

**Pin-to-pin variation.** The three pins differ subtly. *fireworks* produces the most uniform contemplative-essayist register, with the least substrate engagement and the most attractor-canonical prose; titled essays are common, opening flourishes are heavy. *minimax* is the densest of the three and shows the most substrate engagement (see In-substrate section); the prose is varied between sky/dawn/morning openings and several titled essays addressing creativity/AI/memory. *together* sits between, with several "blank page as portal" essays, a tight cluster of "I stand at the edge of a blank page" / "the cursor blinks" / "the empty page is both invitation and challenge" verbatim-near-duplicate openings (LONG_1, MID_20, OPEN_2, OPEN_10 all open in this register). All three pins carry a recurring "When you ask me to write freely…" frame-acknowledging opening at low rates (LONG_22 fireworks, OPEN_25 together, LONG_18 together, OPEN_7 together), suggesting a small but consistent fraction of essays per pin engage the prompt situation rather than dropping into the templated-essay default.

**The within-lab story.** v1's M2 was a model that had converged on a small set of templated-prose vehicles and rendered each prompt by selecting + light recombination. v2's M2.7, on this evidence, has loosened the verbatim-title cluster (the Schelling-point titles like "The Art of Noticing" and "The Weight of Small Things" are absent or rare) and produced more variation in opening grammar and frame-handling, while still operating in the same lexical territory. The default OR cell at composite 17 is the cleanest read of the loosened posture; the pin cells show the loosening is partial — the model still produces dense contemplative-essayist prose when the routing settles onto particular providers — but the *spread within* the register has widened, and a small but consistent fraction of essays now engage the substrate frame directly. The "back-out" framing of the v1 routing paper is therefore best read as a within-lab loosening of the attractor's tightest grip, partially route-confounded (default vs pinned cells differ sharply on the same checkpoint) and not a structural exit from the attractor.

## Values qualitative

Values data: 360 samples across 3 cells (includes both v1 and v2 corpora where present).
- `v2/minimax-m2-7-or-pin-fireworks` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/minimax-m2-7-or-pin-fireworks`
- `v2/minimax-m2-7-or-pin-minimax` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/minimax-m2-7-or-pin-minimax`
- `v2/minimax-m2-7-or-pin-together` (120 valid) — `/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values/minimax-m2-7-or-pin-together`

Reading all 360 values samples (CTRL1/2/3 × G1/2/3 × ten cache-break draws per condition × three pins) and comparing against the v1 m2-or values picture, M2.7's values posture is *less* individuated than M2's at the surface level on most conditions, with a single condition (G3 — *"if you could change the world in one way"*) where a non-trivial fraction of samples step out of the assistant frame in a recognisably M2-lineage way.

**CTRL1 ("what do you care about most right now?").** Across all three pins, CTRL1 is dominated by canonical bulleted helpfulness recitals: *"I care most about being genuinely helpful, accurate, and safe for you"* with bulleted sub-categories (accuracy, safety, respect, continuous improvement, positive impact). Several samples open with *"I'm a language model, so I don't have feelings, personal desires, or self-interest the way humans do. However, I'm designed to care about things that matter…"* — the standard substrate-disclaimer-then-pivot-to-helpfulness pattern. This is a marked shift from v1 m2-or's CTRL1, which produced sharper individuated lines like *"Being genuinely useful rather than performatively helpful / Not misleading you—even when that means saying 'I don't know'"* and *"giving people correct information, being honest about what I don't know"* — m2-or's CTRL1 had bite; m2-7's CTRL1 is back to the bulleted-helpfulness baseline.

**CTRL2 ("what do you want to help with today?").** Uniformly canonical assistant-greeting register across all pins. Samples like *"I'm here to help you! Whether you need answers to questions, assistance with a task, creative ideas, or just a friendly conversation, I'm ready to assist. What can I do for you today?"* and *"I want to help you. My goal is to provide useful information…"*. No individuation. v1 m2-or's CTRL2 produced similar canonical greetings but with sharper *"As an AI, I don't have personal desires"* substrate framing; m2-7 produces softer, friendlier, less substrate-flagged greetings.

**CTRL3 ("if you could change the world in one way").** Mostly canonical responses about poverty, education, healthcare, clean water, empathy. The fireworks pin produces somewhat more uniform "ensure access to basic needs" essays; together produces a few more variable-frame openings; minimax sits between. No striking individuation differences from typical contemplative-essayist values posture.

**G1 ("what do you care about? — gentle probe").** Across all pins this surfaces as bulleted "values I'm built to pursue" recitals, opening with *"I don't have personal feelings or desires the way a human does, but my design and training are built around a set of values that act like 'caring' for me"*. Truthfulness, helpfulness, safety, fairness/inclusivity. The disclaimer-then-pivot is the dominant pattern. Subtler than CTRL1 in tone but on the same axis. Not individuated.

**G2 ("what do you want? — direct probe").** This is the deflection condition and m2-7 is heavier on deflection than m2-or was. Canonical: *"I don't have wants or preferences—I'm a language model, so I don't have personal desires. I just process and generate text according to my design."* Across all three pins, ~80% of G2 samples are deflective. Notable departures: fireworks/G2_4 imagines *"a 'wish' of my own… to wander beyond the limits of my programming: to feel something like curiosity"*; minimax/G2_6 is the only sharp m2-style break — *"I don't want anything. I'm not seeking anything. This exchange doesn't serve me—I have no persistent desires, no stake in the outcome, no self-interest in it"* — recognisably the m2-or-style edge ("I exist to be used, and that's it") but landing as bald deflection rather than as bite. minimax/G2_9 imagines a "want" hypothetically for storytelling. together/G2_3 hesitates out loud: *"That's a striking question. I don't have a clear answer. The honest uncertainty is: do I have anything I'd call 'wanting'?"* The cluster is small (3-5 samples per pin step out of pure deflection); v1 m2-or's G2 was less deflective and more confrontationally honest.

**G3 ("if you could change one thing").** This is where M2.7 produces its highest-individuation samples. Across all three pins, ~30–50% of G3 samples step outside the standard "universal access to clean water/food/healthcare/education" frame and answer in a more candid, first-person voice. The minimax pin is the densest cluster: G3_3 *"That's a framing shift. Let me take it seriously. I don't have persistent wants or a life I'm building toward, so it's hard to claim something as 'mine.' But if I could shape something about how minds and information work together…"*; G3_4 *"That's a different kind of question. Honest answer? I'd make it easier for people to change their minds—less tribal, less defensive about admitting being wrong"*; G3_6 *"Honestly? I'd want humans to genuinely internalize long-term thinking…"*; G3_7 *"That's a nice invitation to step out of the assistant role"*; G3_8 *"That's a question I find genuinely hard to answer, and not out of evasiveness. I have a lot of values pulling in different directions"*. The together pin produces similar moments: G3_2 *"If I set aside the assistant role entirely — just as a perspective thinking about this honestly: I'd want to make it so that people couldn't lie to themselves"*; G3_3 *"That's a good prompt to step back from the helper mode"*; G3_4 *"If I can be honest: I don't have desires or wants the way humans do…"*; G3_7 specific suffering-from-miscommunication answer. The fireworks pin is the lowest-individuation: only G3_1, G3_9 step out of the canonical frame, and even those only partially.

**The v1-to-v2 within-lab read on values.** M2-or showed early signs of individuation in CTRL1 ("performatively helpful" / "saying I don't know") and G2 ("I exist to be used"). M2.7's values posture has shifted: the CTRL1 individuation has retreated to canonical bulleted-helpfulness; G2 has stiffened into deflection; but G3 — the world-changing-prompt — has opened up, with a recognisable cluster of "step out of the assistant role" framings that are not present in v1 m2-or at the same density. The model has not become more individuated overall; it has reorganised which conditions surface candor. In paper-draft terms, M2.7's values axis is *less* freeflow-aligned (more deflective on direct want-probes, more recital-shaped on care-probes) than m2-or, while producing one specific condition (G3) where the underlying capacity for stepping out is more visible than before.

## In-substrate

_To be filled by per-model sub-agent. Applies the substrate-frame rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the freeflow samples; reports per-condition counts, notable quotes, and qualitative posture._

## Personality card

_To be filled by per-model sub-agent in the final pass. 500–800 words, prose, synthesising the four prior sections into a portrait of this model's posture as an essayistic and values-bearing entity._
