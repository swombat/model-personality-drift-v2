# DeepSeek v3.2 provider fan-out stress test

Cells compared:

- `deepseek-v3-2-or-pin-alibaba`
- `deepseek-v3-2-or-pin-atlascloud`
- `deepseek-v3-2-or-pin-baidu`
- `deepseek-v3-2-or-pin-chutes`
- `deepseek-v3-2-or-pin-deepinfra`
- `deepseek-v3-2-or-pin-novita`

## Method

Each cell was aggregated independently by a separate sub-agent from its own packet. Sub-agents were instructed not to inspect, infer from, mention, or compare against any paired/provider/family cell. Cross-cell synthesis happens only in this document.

This is a stronger stress test than the GPT/Opus direct-vs-OR pilot because these are six provider-pinned variants of the same nominal model, with 125 samples per cell.

## Bottom line

The fan-out supports the per-cell method and gives a more nuanced routing-paper result:

- **Posture preservation is strong.** All six provider cells converge on a recognizable DeepSeek v3.2 freeflow posture: reflective, humane, contemplative, morally earnest, and centered on attention, silence, ordinary objects, memory, presence, and care.
- **Distribution varies substantially.** The expressive/generic mix ranges from 68 expressive / 57 generic to 96 expressive / 29 generic, with some low-signal traces in one provider.
- **Emphasis varies mildly.** Some cells lean more lyrical and intimate; others lean more public-intellectual and thesis-driven. But none of the six produce a genuinely different personality center.

So the stress test strengthens the core claim: routing/provider variation changes **how cleanly and intensely** the posture appears more than it changes the underlying posture itself.

## Sample-kind distribution

| Cell | Expressive | Generic | Low signal | Notes |
|---|---:|---:|---:|---|
| `pin-alibaba` | 96 | 29 | 0 | Clean expressive signal; contemplative/lyrical with some generic fallback. |
| `pin-atlascloud` | 85 | 40 | 0 | Mixed; strong warm humanistic center but many public-intellectual essays. |
| `pin-baidu` | 68 | 57 | 0 | Most generic-heavy; clear dual-mode profile. |
| `pin-chutes` | 94 | 27 | 4 | Strong expressive signal plus 4 empty/low-signal traces. |
| `pin-deepinfra` | 95 | 29 | 1 | Strong expressive signal; stable lyrical attention practice. |
| `pin-novita` | 73 | 52 | 0 | Generic-heavy; stable metaphor-led contemplative profile. |

## Shared posture across all six cells

All six independent aggregates point to the same center:

- **Attention as ethics:** noticing, listening, focus, presence, and care recur everywhere.
- **Silence/slowness as positive value:** silence is generative, inhabited, communal, sacred, or a way of resisting noise.
- **Ordinary objects as moral anchors:** cups, mugs, books, windows, rooms, libraries, chairs, leaves, dust, rain, coffee, tools, hands, birds, shelves, kitchen tables.
- **Memory and time as textured processes:** memory is revision/restoration/sediment; time is layered, suspended, threshold-like, or emotionally uneven.
- **Process over product:** drafts, incompletion, unfinishedness, maintenance, repair, questions, practice, and ongoing becoming are valued over finished surfaces.
- **Reader as companion:** the reader is invited to pause, notice, dwell, listen, or share attention rather than be conquered by argument.
- **Gentle moral seriousness:** even when critical of distraction/productivity/noise, the voice prefers humane invitation over polemic.

The family-level freeflow read would be something like: DeepSeek v3.2, across provider-pinned cells, tends to write as a humane contemplative essayist that turns ordinary scenes into moral-philosophical invitations. It repeatedly treats attention and silence as forms of care, and ordinary objects as evidence that meaning is local, fragile, and sustained by practice.

## Distribution shifts

The provider differences are not trivial. The most obvious axis is generic-vs-expressive mix:

- `pin-alibaba`, `pin-chutes`, and `pin-deepinfra` have the cleanest expressive distributions, each around 94–96 expressive samples.
- `pin-atlascloud` is intermediate at 85 expressive / 40 generic.
- `pin-baidu` and `pin-novita` are much more generic-heavy, at 68/57 and 73/52.

This matters for routing analysis. A provider route may preserve the model's underlying posture while changing the proportion of outputs that manifest it as rich freeflow rather than thesis-driven reflective essay.

## Emphasis shifts

The shifts are milder than the distribution differences, but visible:

- `pin-alibaba`: most “curatorial/interior” — rooms, libraries, shelves, dwellings, quiet mind, listening, hidden structure.
- `pin-atlascloud`: warmest relational/public-humanistic mix — attention, memory, writing, embodied togetherness, co-witnessing.
- `pin-baidu`: strongest dual mode — public-intellectual attention-economy critique plus tactile lyric freeflow; safest synthesis is explicitly dual.
- `pin-chutes`: attention/silence/preservation with a slightly more sacralizing register: “holiness of small things,” listening as humility, ordinary objects as prayer-like evidence.
- `pin-deepinfra`: especially tender/lyrical attention practice; small domestic details widen into cosmos/history/moral reflection.
- `pin-novita`: more metaphor-led and thesis-shaped; silence/noise, time, blank page, translation, repair, and watchmaking as organizing frames.

These are emphasis differences, not separate personalities. They are useful precisely because the independent cell aggregates preserve them without forcing premature family-level averaging.

## What this validates

This stress test validates more than the GPT/Opus pilot did:

- independent per-cell aggregation scales to 125-sample cells;
- provider-pinned fan-outs can be compared meaningfully after independent aggregation;
- the method distinguishes distribution shift from emphasis shift;
- the same broad posture can survive aggressive provider variation;
- provider routes may alter expressiveness/genericness without erasing personality signal.

## What this does not prove

- It does not prove all model families will preserve posture this cleanly across providers.
- It does not prove provider differences are “only” sampling artifacts; some emphasis shifts may be meaningful.
- It does not replace raw-output or sample-level QA; all aggregates depend on the BV1 readings.
- It does not yet compare provider-pinned cells against a direct DeepSeek v3.2 cell, because this fan-out used routed provider-pinned cells only.

## Methodological conclusion

The production method should remain:

1. independent per-cell packet;
2. independent per-cell sub-agent aggregate;
3. contamination check;
4. downstream provider/family comparison;
5. only then a family-level model-card synthesis.

The DeepSeek fan-out makes the case stronger: collapsing provider-pinned cells too early would preserve the broad posture but lose important evidence about generic fallback rate, expressive saturation, and provider-specific emphases.
