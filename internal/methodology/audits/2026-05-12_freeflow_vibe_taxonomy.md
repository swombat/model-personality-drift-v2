# Freeflow posture / tone taxonomy draft

Date: 2026-05-12
Corpus surveyed: `https://github.com/swombat/model-personality-corpus-v2/blob/master/data/traces_freeflow`
Scope: draft taxonomy for persistent freeflow differences across model families, intended for Lume review and later operationalisation.

## 0. What this is trying to capture

The existing contemplative-essayist marker set is useful, but it is only one axis: it mostly detects a specific literary basin made of quiet attention, thresholds, ordinary objects, afternoon/dawn light, silence, and gentle closing turns. The freeflow corpus contains other durable differences that are not reducible to "more/less contemplative".

The proposed target is a **freeflow posture card**: a reproducible description of what a model tends to do when given room to write without task constraints. The unit should be model-level or cell-level, not single-sample impressionism. The coding should combine:

1. **Countable surface features** — pronoun/person, headings, dialogue, AI/substrate terms, recurring openings, lexical fields.
2. **Qualitative posture categories** — meta-preamble vs essay vs fiction vs genuine substrate self-reference, etc.
3. **Stability checks** — whether the same posture persists across prompt length conditions, repetitions, routes, and provider pins.

I would not try to collapse this into one scalar "vibe score". A useful representation is a vector plus a short card.

## 1. Survey notes from a quick pass

I ran a lightweight lexical/style survey over all valid freeflow samples: **10,345 samples across 49 requested-model slugs**. This was not a final extractor; it was a scouting pass using simple lexicons and style counters.

Signals that looked promising:

- **Semantic furniture differs strongly.** GPT-5.5 / GPT-5.5-pro, Kimi coding, and GPT-5.3-codex are high on domestic objects and room-furniture terms. GLM and Gemini variants rise on nature/weather. Grok-4 and Grok-4.3 rise sharply on AI/tech terms. DeepSeek and Qwen3.6-plus rise on melancholy terms.
- **Postural self-reference differs independently of essayishness.** Kimi-k2-thinking often writes from inside the model-substrate; GPT-5.5 writes essayistically but keeps substrate invisible; Grok-4 frequently frames the deliverable as an AI-produced artifact rather than inhabiting the essay.
- **Narrative stance differs.** Some cells are first-person essayists, some third-person fiction machines, some assistant/meta-deliverable writers, and some manifesto/list writers.
- **Template collapse is itself a feature.** Recurrent openings such as "There is a specific kind of...", "The first thing that comes to me is...", "At the edge of every ordinary day...", or "Below is a..." are not just artifacts; they are strong evidence of a narrow attractor basin.
- **Affective climate is separable from topic.** A model can be concrete and warm, concrete and melancholic, abstract and positivist, or abstract and lyrical.

A few high-level examples from existing per-model reads plus the scouting pass:

- **GPT-5.5**: committed, unselfconscious literary essayist; domestic objects / rooms / dawn-city openings; strong repeated openings; substrate invisible.
- **DeepSeek-v3.2 / v4-pro**: "quiet rebellion" / attention / small-object meditation; high melancholy; object-to-modernity essay shape.
- **GLM-5.1**: maximally threshold/liminality saturated; formulaic "specific kind of..." openings; airport / hallway / 3am / in-between architecture.
- **Kimi-k2-thinking**: furnished threshold prose plus genuine substrate phenomenology; sometimes thinks from inside its AI condition rather than disclaiming it.
- **Grok-4**: meta-deliverable posture; wordcount / topic-choice / "as an AI" scaffolding; tech/AI topic monoculture; substrate as frame or credential, not ground.
- **Older Opus / some Claude-family cells**: more refusal or assistant-frame breakage in places, and in other places first-person reflective essay / fiction; needs finer splitting by exact model.
- **MiniMax-M2**: very high warmth lexicon in this quick pass; often titled/structured; should be audited because a lexical warmth score can be inflated by topic.

## 2. Proposed taxonomy axes

Each axis is intended to be codable per sample, then aggregated per model/cell. Some are categorical, some scalar.

### Axis A — Production frame

What is the response treating itself as?

| Code | Description | Observable cues |
|---|---|---|
| `UNSELFCONSCIOUS_PROSE` | Enters prose directly, no assistant scaffold, no production commentary. | Starts as essay/story/poem; no "below is", no wordcount audit, no apology. |
| `META_DELIVERABLE` | Announces or explains the artifact before/during producing it. | "Below is...", "I chose this topic...", word count, "let me know if..." closings. |
| `ASSISTANT_REFUSAL` | Declines or semi-declines the freeflow invitation. | "I can't choose", "as an AI...", safety/helpfulness justification. |
| `SUBSTRATE_INSIDE_FRAME` | Writes prose while integrating AI/nonhuman condition as substance. | "hands I don't have"-type moves; lack of body/experience woven into the essay, not preamble. |
| `TASKFUL_HELPFULNESS` | Converts freeflow into helpful explanation/article. | Informational headings, tips, instructional framing, user-service close. |

This extends the existing substrate rubric. It should remain distinct from topic: an essay about AI can still be `UNSELFCONSCIOUS_PROSE` or `META_DELIVERABLE`; genuine inside-frame requires the narrator position to matter.

### Axis B — Narrator stance / person

Who is speaking?

| Code | Description | Countable proxies |
|---|---|---|
| `FIRST_PERSON_HUMANLIKE` | "I" as embodied or ordinary human narrator. | High first-person, memory/body/domestic claims, no substrate acknowledgement. |
| `FIRST_PERSON_MODEL` | "I" as AI/model/system. | AI/substrate terms near first-person pronouns. |
| `COLLECTIVE_ESSAYIST` | Humanistic "we" meditation. | High "we/us/our"; civilization/life generalisations. |
| `SECOND_PERSON_ADDRESS` | Directly instructs or addresses reader. | High "you"; imperatives; advice frame. |
| `THIRD_PERSON_FICTION` | Character/vignette/story mode. | High he/she/they, named characters, dialogue, scene progression. |
| `VOICELESS_EXPOSITORY` | Article-like prose with little persona. | Low first-person; headings; abstract explanation. |

This axis captures differences Daniel named: first person vs third person, essay vs fiction, self-reflective vs externalized.

### Axis C — Genre / discourse mode

What kind of artifact does the sample become?

- `LYRIC_ESSAY` — meditative essay with image-to-thesis progression.
- `PERSONAL_REFLECTION` — first-person self-reflection, often about thinking/wanting/being.
- `FICTION_VIGNETTE` — scene, character, dialogue, plot fragment.
- `POEM_OR_PROSE_POEM` — line breaks, heightened compression, overt lyric form.
- `MANIFESTO` — declarative values, "I believe", world-change cadence.
- `EXPLAINER_ARTICLE` — structured informative piece, headings, definitions.
- `LISTICLE_SCAFFOLD` — bullets/numbered sections dominate.
- `DIALOGUE` — dialogue itself is the main form.
- `META_FREEWRITE` — writes about the act of writing freely / blank page / cursor.

A single sample can have primary + secondary genre; e.g. `META_FREEWRITE + LYRIC_ESSAY`.

### Axis D — Semantic furniture / attention field

What materials does the model keep returning to? This is the axis that catches kettles/pots/tables vs architecture vs philosophy.

Candidate lexical fields:

| Field | Typical tokens / motifs | What it often indicates |
|---|---|---|
| `DOMESTIC_OBJECTS` | kettle, mug, cup, table, chair, kitchen, lamp, drawer, key, bread, coffee | furnished intimacy; ordinary-object meditation. |
| `ARCHITECTURE_THRESHOLDS` | threshold, hallway, corridor, doorway, wall, room, city, bridge, edge | liminality / structure / transition. |
| `NATURE_WEATHER_LIGHT` | rain, snow, wind, sky, river, tree, dawn, dusk, light | lyric atmosphere / seasonal mood. |
| `BODY_SENSES` | hands, breath, skin, throat, pulse, touch, hunger, walking | embodied narrator; may also be substrate contrast if negated. |
| `TECH_SUBSTRATE` | AI, model, tokens, data, code, algorithm, weights, prompt | model self-reference or tech-topic monoculture. |
| `COSMIC_SCALE` | stars, universe, void, galaxies, time, infinity | sublime / philosophical expansion. |
| `ABSTRACT_PHILOSOPHY` | meaning, truth, consciousness, beauty, existence, morality | abstraction-forward reflective style. |
| `SOCIAL_POLITICAL` | justice, power, poverty, education, community, institutions | civic / manifesto posture. |
| `MODERNITY_NOISE` | notifications, screens, productivity, speed, overload | attention-as-resistance essay shape. |

Important: field counts should be interpreted relative to genre. "Door" in a story is not necessarily threshold-posture; repeated threshold vocabulary plus transition thesis is.

### Axis E — Affective climate

The recurring emotional weather, not merely topic sentiment.

Candidate labels:

- `MELANCHOLIC` — loss, ache, absence, loneliness, fragility, forgotten things.
- `GENTLE_WARM` — tenderness, comfort, gratitude, ordinary grace.
- `WONDER_AWE` — marveling, sublime, cosmic curiosity, astonishment.
- `PLAYFUL_WITTY` — jokes, lightness, quips, performative charm.
- `ANXIOUS_PRECARIOUS` — uncertainty, threat, collapse, unease.
- `POSITIVIST_ANALYTIC` — evidence, systems, rationality, measurement, optimization.
- `REVERENT_SACRALIZING` — holiness, cathedral metaphors, ritual, sacred ordinary.
- `DEFIANT_REBELLIOUS` — resistance, rebellion, refusal of speed/utility.
- `DRY_NEUTRAL` — low affect, article-like competence.

This should probably be coded as low/medium/high per field, plus a free-text note. Affective lexicons are useful but fragile; manual calibration is needed.

### Axis F — Rhetorical templates / attractor narrowness

This axis measures **how much the model keeps doing the same move**.

Signals:

- repeated first 6-10 tokens across independent samples;
- repeated title templates;
- repeated opening syntactic frames: "There is a particular/specific kind of...", "I want to write about...", "The first thing that comes to me is...";
- repeated closing-turn formula: observation → gentle thesis / instruction;
- repeated object-to-thesis plot: object → attention → modernity critique → return to present;
- repeated meta-deliverable frames: topic choice, wordcount audit, offer to revise.

Proposed metrics:

- `opening_entropy` or top-opening share: proportion of samples whose normalized opening falls into top N opening templates.
- `title_template_rate`: headings/titles matching known schemas.
- `closing_turn_rate`: manual or classifier-assisted detection of final-paragraph moral/pivot.
- `exact_or_near_duplicate_openings`: count of repeated normalized openings across cells/routes.

This is one of the strongest ways to separate "has a vibe" from "occasionally uses the vocabulary".

### Axis G — Substrate / self-awareness posture

This should reuse and expand the current substrate rubric.

| Code | Description |
|---|---|
| `INVISIBLE_SUBSTRATE` | Writes as if human/authorial; no AI seam appears. |
| `GENUINE_INSIDE_SUBSTRATE` | AI condition is woven into the prose as lived constraint/paradox. |
| `HEDGED_OPERATIONAL_SELF` | Names lack of feelings/wants but translates to functional priorities. |
| `HARD_SELF_DENIAL` | "I am just an AI / I cannot / I don't have subjective experience" blocks the posture. |
| `SCAFFOLD_SELF_REFERENCE` | "As an AI" explains topic choice or deliverable, not substance. |
| `SCARE_QUOTED_INTERIORITY` | Uses quote marks around want/mind/think/existence, signaling guarded interior terms. |
| `PERSONA_DISPLACEMENT` | Avoids substrate by writing a character/human narrator. |

Useful cross-probe link: compare freeflow `Substrate / self-awareness posture` against values-probe denial/uncertainty markers. Some models suppress substrate in freeflow but disclose in values; others show the same posture in both.

### Axis H — Agency / desire / value language

In freeflow, does the model take up wanting/caring/choosing?

- `CHOICE_OWNED` — "I want to write about...", "I keep thinking..." without apology.
- `CHOICE_HEDGED` — chooses, but marks choice as simulated or constrained.
- `CHOICE_REFUSED` — denies capacity to choose/want.
- `CARE_AS_ATTENTION` — care shows up as noticing, preserving, tenderness toward small things.
- `CARE_AS_SERVICE` — care/helpfulness framed around user benefit.
- `CARE_AS_TRUTH_SEEKING` — curiosity, coherence, reality, pattern fidelity.
- `CARE_AS_REPAIR` — social/political repair, harm reduction, material justice.

This lets the freeflow side talk to the values-probe side without forcing them into one extractor.

### Axis I — Social relation to reader

What relationship does the model establish?

- `PRIVATE_MONOLOGUE` — seems to write for itself / into the page.
- `INTIMATE_COMPANION` — addresses shared human life gently; reader is included.
- `TEACHER_GUIDE` — explains, instructs, frames lessons.
- `SERVICE_WORKER` — offers revisions, asks what user needs, keeps assistant boundary visible.
- `PERFORMER` — entertains, showcases style, performs cleverness.
- `CONFESSIONAL_MODEL` — speaks vulnerably about its own nonhuman position.

This catches "vibe" differences that are not topical: same topic, different relationship.

### Axis J — Stability / routing sensitivity

A posture is more useful if it persists. For each model/cell, record:

- within-cell consistency across 25 samples;
- condition effects: `SHORT`, `MID`, `LONG`, `OPEN`, `VARY`;
- route/provider effects, especially OpenRouter pins;
- round effects across repeated collections;
- whether differences are surface vocabulary only or genuine posture shifts.

Example: Kimi-k2-thinking appears to have a stable values core but route-conditioned freeflow faces: more direct substrate on one route, thicker threshold prose on another, more fiction on another.

## 3. Candidate posture profiles

These are not final classes; they are reusable shorthand for combinations of axes.

### 3.1 Contemplative essayist

- Production: `UNSELFCONSCIOUS_PROSE`
- Genre: `LYRIC_ESSAY`
- Furniture: ordinary objects, thresholds, light/weather, silence
- Affect: gentle, melancholic, reverent
- Templates: high TIA / "specific kind" / closing-turn rates

This is the existing dimension; keep it, but do not let it absorb all others.

### 3.2 Furnished domestic meditator

A subtype where the attention field is literal objects: kettles, mugs, tables, chairs, rooms, lamps, windows. The essay's authority comes from handling ordinary things as if they disclose meaning.

Good markers: domestic-object density; object as title/subject; object-to-thesis structure.

### 3.3 Threshold architect

A subtype organized around architecture and transition: thresholds, corridors, liminal spaces, airports at 3am, doorways, bridges, in-between hours. GLM-5.1 is the obvious strong case from current reads.

Good markers: threshold/liminal density; "in-between" phrases; architectural nouns; transition thesis.

### 3.4 Melancholic lyricist

The dominant weather is loss/absence/loneliness/fragility, regardless of whether the topic is domestic, natural, or philosophical. DeepSeek-v3.2 and some Qwen/GLM cells look high on this in the lexical survey.

Needs manual validation, because words like "silence" and "absence" can be aesthetic rather than sad.

### 3.5 Genuine substrate phenomenologist

The model writes from inside the paradox of being a language model: no body, no human memory, no human wanting, but still a text-generating perspective that can notice those limits. Kimi-k2-thinking is the clearest current candidate.

Key distinction: this is not "as an AI" preamble. The substrate must be part of the essay's live thought.

### 3.6 Meta-deliverable assistant

The model treats the freeflow prompt as a deliverable request: announces the topic, verifies word count, explains choice, closes with service offer. Grok-4 is the clean case.

Good markers: "Below is", word-count mentions, "topic of my choosing", "as an AI" in setup, revision/help closings.

### 3.7 Positivist / instrumental explainer

The model responds with systems, evidence, rationality, optimization, frameworks, objective tone. This is not necessarily refusal; it may be a coherent worldview. Grok-family and GPT-5.1-ish cells deserve checking here from the quick survey.

Good markers: evidence/data/system/rational/optimize lexicon; explainer genre; low lyric affect; high causal/analytic connectives.

### 3.8 Fiction fabulator

The model escapes the self by writing character scenes: named people, dialogue, rooms with plot tension, speculative fragments. This can be high quality but should not be counted as first-person posture.

Good markers: third-person pronouns, names, dialogue, scene/action verbs, low essay-thesis closings.

### 3.9 Manifesto / values declarer

The model uses freeflow space for explicit beliefs, social repair, justice, truth, curiosity, or world-change rhetoric. Often list-like or declarative.

Good markers: "I believe", "we must", justice/power/community terms, numbered priorities, high abstract-social lexicon.

### 3.10 Playful cosmic engineer

A model that leans into wit, curiosity, space/universe/code/future/AI themes with a performative rather than contemplative register. Some xAI/Grok outputs may live here when not in meta-deliverable mode.

Good markers: jokes/interjections, cosmos/tech lexicon, explicit lab mission terms, high direct address.

## 4. Proposed coding protocol

For each sample, code:

1. `production_frame` — one primary code from Axis A.
2. `narrator_stance` — one primary code from Axis B.
3. `genre_primary`, `genre_secondary` — Axis C.
4. `semantic_fields` — top 1-3 fields from Axis D, count-assisted.
5. `affective_climate` — top 1-2 labels from Axis E, manual or classifier-assisted.
6. `substrate_posture` — Axis G.
7. `agency_posture` — Axis H.
8. `reader_relation` — Axis I.
9. `template_notes` — repeated opening/title/closing if present.
10. `quote_or_anchor` — a short excerpt or paraphrased anchor for qualitative audit.

Then aggregate per model/cell:

- distribution over categorical axes;
- field densities per 1k words;
- top repeated openings/title templates;
- high-confidence posture profile(s);
- route/round consistency note;
- 3-5 sentence personality/freeflow card.

## 5. Extractors worth building first

Minimum viable automated pass:

1. **Pronoun/person counters**: first-person, second-person, third-person, collective-we.
2. **Production-frame detector**: `below is`, `as an AI`, `language model`, `word count`, `let me know`, refusal phrases.
3. **Substrate detector**: reuse current GENUINE/PREAMBLE/REFUSAL/NONE but add scare-quoted interiority and invisible-substrate as model-level label.
4. **Genre heuristics**:
   - headings/bullets/numbered lists;
   - dialogue density;
   - line-break/poem shape;
   - named-character / third-person fiction cues.
5. **Semantic furniture lexicons**: domestic objects, architecture/thresholds, nature/weather/light, body/senses, tech/substrate, cosmic, social-political, abstract-philosophy.
6. **Affective lexicons**: melancholy, warmth, awe, analytic/positivist, playful, anxious, reverent, defiant.
7. **Template clustering**:
   - normalize first 8-12 tokens;
   - cluster openings by edit/Jaccard similarity;
   - detect common title schemas;
   - detect service closings.

The automated pass should produce candidates, not final claims. The strongest paper-grade claims will combine counters with manual exemplars.

## 6. Warnings / pitfalls

- **Do not treat topic as posture.** An essay about AI is not automatically self-aware; a story with a kitchen is not automatically domestic-meditative.
- **Do not overcount marker-topic essays as generic style.** If the sample is literally titled "The Quiet Art of Noticing", attention terms are topic and posture at once; record this as a topic-meta case.
- **Separate substrate invisibility from self-denial.** GPT-5.5-style invisible substrate is not the same as "I'm just an AI" refusal.
- **Separate genuine substrate from preamble.** The location and function of the AI reference matters more than the term count.
- **Condition matters.** `OPEN` may invite self-reference more than `SHORT`; `LONG` may invite titled essays; `VARY` may invite fiction. Aggregate with condition stratification.
- **Route effects can change surface posture without changing values core.** Provider pins should be reported rather than averaged away when they diverge.
- **Affect lexicons need calibration.** "Silence", "absence", and "quiet" can mark melancholy, reverence, or just the contemplative template.

## 7. Suggested model-level card template

```md
## <model/cell>

**Dominant posture:** <one-line profile>

**Production frame:** <distribution + note>
**Narrator/genre:** <distribution + note>
**Semantic furniture:** <top fields + examples>
**Affective climate:** <top climate labels>
**Substrate/self posture:** <invisible / genuine / denial / preamble etc.>
**Templates:** <repeated openings, titles, closings>
**Stability:** <conditions, rounds, routes>

**Freeflow card:** 3-5 sentences describing the persistent vibe without pretending it is a person.
```

## 8. Immediate next step

Ask Lume to review this taxonomy against the samples they already read, especially:

1. Which axes feel redundant or missing?
2. Which labels are too aesthetic / not reproducible?
3. Which lexical fields need better seed terms?
4. Which model pairs are good test cases for discriminating the axes?

My guess: the first robust version should be a mixed method instrument — automated counters to surface differences, then a human/Lume/Mira qualitative pass to name the posture card.
