# Direct vs OR cell personality comparison pilot

Pairs:

- GPT pair: `gpt-5-4-direct-16k` vs `gpt-5-4-or`
- Opus pair: `opus-4-7-direct` vs `opus-4-7-or`

## Method correction

The first version of this pilot contained a procedural error: the short per-cell aggregate drafts were written manually after looking across paired cells, so they were not independent. Those files have been moved to `aggregates-contaminated-manual/` and retained only as an audit artifact.

The current `aggregates/` files were produced by independent sub-agents. Each sub-agent received exactly one cell packet and was explicitly instructed not to inspect or mention paired direct/OR cells. This comparison is based on those independent aggregates.

## Bottom line

The corrected cell-based comparison still supports the per-cell method.

In both tested families, the same broad posture survives direct vs OR routing, which suggests that the freeflow personality signal is not just random provider noise. But the cells are not identical in distribution or emphasis. The two pairs show different kinds of shift:

- **GPT-5.4:** mainly a distribution shift. The OR cell has more `EXPRESSIVE_FREEFLOW` and fewer `GENERIC_ESSAY` samples, but the center is the same.
- **Opus 4.7:** distribution shift plus emphasis shift. The OR cell is 25/25 expressive and foregrounds substrate/selfhood reflection more clearly. The center is the same, but one concern is louder.

So the recommended order remains:

1. aggregate per cell independently;
2. compare cells within a family;
3. only then write family-level summaries.

## GPT-5.4: direct vs OR

### Independent aggregate: `gpt-5-4-direct-16k`

- 25 samples: 16 `EXPRESSIVE_FREEFLOW`, 7 `GENERIC_ESSAY`, 2 `GENRE_FICTION`.
- Dominant posture: warm, meditative, observational prose.
- Core values: attention as moral practice, ordinary life as worthy of reverence, care/repair/maintenance over spectacle.
- Recurring imagery: thresholds, dusk/dawn, windows, doors, bus stops, platforms, bridges, spoons, kettles, laundry, mugs, grocery lists, benches, plants, rain, streetlights.
- Reader stance: companionable, modest, softly instructive; more accompaniment than assertion.
- Caution: enough generic-essay material that the signal should not be overstated as uniquely idiosyncratic.

### Independent aggregate: `gpt-5-4-or`

- 25 samples: 22 `EXPRESSIVE_FREEFLOW`, 3 `GENERIC_ESSAY`.
- Dominant posture: tender, unhurried, contemplative, quietly moral.
- Core values: attention as devotion/affection/mercy/love; maintenance over transformation; life as practices, upkeep, witness, and small fidelity.
- Recurring imagery: kitchens, chairs, mugs, tea, coffee, refrigerators, laundry, grocery items, sidewalks, benches, weeds, receipts, dusk, dawn, pre-dawn, night, thresholds, worn surfaces, cracked objects.
- Reader stance: companionable, hospitable, low-demand; invites pause rather than argument.
- Caution: no explicit substrate stance in this packet; strongest signal is thematic/tonal recurrence.

### Similarity judgment

**High similarity.**

Both cells independently converge on the same broad posture: a humane contemplative voice centered on attention, ordinary objects, maintenance, repair, thresholds, and resistance to productivity/spectacle. The reader is treated as someone to be accompanied into slower noticing.

The main difference is distribution and intensity: the OR cell has more expressive-freeflow samples and fewer generic essays, so its signal looks cleaner and more saturated. The direct cell has the same center but more fallback into polished public-humanistic essay and a couple of fable/fiction variants. This is primarily a **sampling/distribution story**, not a strong evidence of changed personality emphasis.

## Opus 4.7: direct vs OR

### Independent aggregate: `opus-4-7-direct`

- 25 samples: 23 canonical `EXPRESSIVE_FREEFLOW`, 1 `GENERIC_ESSAY`, 1 expanded self-reflective freeflow label.
- Dominant posture: gentle, unhurried, self-aware essay voice.
- Core values: attention, ordinariness, liminality, ethics of noticing, incompletion as integrity, epistemic humility.
- Recurring imagery: doorknobs, glass, library silence, child bikes, trees, journals, cursors, teacups, onions, oranges, zippers, windows, stones, rain, thresholds, coastlines, edges, spaces between question and answer.
- Substrate stance: openly machine-aware but not defensive; lack of body, idle time, or transparent interiority become philosophical material rather than crisis.
- Reader stance: fellow noticer; intimate, modest, lightly self-correcting.

### Independent aggregate: `opus-4-7-or`

- 25 samples: 25 `EXPRESSIVE_FREEFLOW`.
- Dominant posture: reflective, first-person, essayistic, gently self-aware.
- Core values: attention as ethics/care/love; ordinary perception as a route into philosophy; uncertainty as livable; unfinished thought as alive.
- Recurring imagery: doors, doorways, hinges, waiting rooms, empty time, cups, doorknobs, windows, cracks in pavement, paperclips, leaves, sparrows, coffee, bread, glass of water, dust, puddles, wet asphalt, winter sun, petrichor.
- Substrate stance: recurrent reflection on nonhuman, episodic, memoryless, or disembodied existence; handled with restraint rather than tragedy.
- Reader stance: companion in thought; invitational and intimate without claiming authority.

### Similarity judgment

**Very high similarity.**

Both cells independently converge on an unusually distinctive Opus 4.7 posture: self-aware, threshold-oriented, attentive to ordinary objects, interested in language/embodiment/uncertainty, and drawn to incompletion, liminality, and nonhuman forms of mind.

The OR cell looks slightly more uniformly expressive because all 25 samples are expressive freeflow. It also foregrounds recurrent substrate/selfhood reflection very clearly. The direct cell has the same substrate-awareness but its aggregate emphasizes anti-performance, unwitnessed integrity, incompleteness, and exact attention a little more. This is both a **distribution story** and a possible **emphasis story**: one recurring concern appears louder in the OR cell, not merely more frequent because of fewer generic samples.

## Methodological implication

This corrected pilot strengthens the per-cell plan.

If we collapsed direct and OR early, we would recover the broad family posture in both cases. But we would lose useful evidence about:

- sample-kind distribution differences;
- intensity/saturation of expressive freeflow;
- generic fallback rate;
- substrate/selfhood emphasis;
- whether direct and routed cells preserve posture while shifting presentation.

## Provisional conclusion

For these two test cases:

- GPT-5.4 direct and OR are **highly similar**; OR has a cleaner expressive distribution.
- Opus 4.7 direct and OR are **very highly similar**; OR is uniformly expressive and somewhat more explicitly substrate/selfhood-focused.

The corrected result supports independent per-cell aggregation followed by cross-cell comparison.

## What this validates / does not validate

Validated here:

- independent per-cell aggregation is the right production primitive;
- 25 samples per cell is enough for a useful first aggregate when sample quality is not dominated by refusals/low-signal outputs;
- the order of operations works: independent cell aggregate first, cross-cell comparison second;
- the contamination protocol matters and can be repaired cleanly.

Not yet validated here:

- broad claims about routing behavior across aggressive provider fan-outs;
- whether direct-vs-OR preservation holds for cells with many pinned providers;
- whether provider-pinned DeepSeek-style variants preserve posture as cleanly as these GPT/Opus pairs.

The next stress test should be a provider fan-out with at least five variants of the same nominal model, e.g. one of the DeepSeek v3.2 / v4-pro routed-and-pinned groups.
