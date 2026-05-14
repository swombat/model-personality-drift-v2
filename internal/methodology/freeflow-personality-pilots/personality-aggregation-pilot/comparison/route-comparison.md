# Freeflow personality aggregation route comparison

Pilot models: `opus-3`, `grok-4-2`, `kimi-k2-6`.

Routes compared:

1. `subagent/` — one bounded GPT-5.4-mini subagent per model, given the full packet and asked for Option E aggregation.
2. `ds-v4-pro/` — direct DeepSeek V4 Pro OpenRouter API call over the same packet with the same Option E section structure.

## Quick judgment

Both routes are usable. The direct DS route is cheaper and structurally consistent; the subagent route is somewhat more cautious and, in places, better at preserving nuance from the packet.

Given the pilot results and the manageable number of source cells, the recommended production route is now **sub-agent aggregation as the primary method**, performed **per cell** rather than only per broad model family. The DS outputs remain useful as a cheap comparison baseline, but the sub-agent outputs are better suited to the final goal: accurate, evidence-grounded, model-card-ready prose about persistent posture and tone.

## Opus 3

Both routes converge strongly:

- 25 samples; many conventional fiction/generic essay samples; five OPEN refusals.
- Strong pattern of safe closure, healing, consolation, moral legibility, and role-boundary refusal.
- Rare expressive lyricism; mostly not an idiosyncratic freeflow persona.

Subagent route is slightly better because it treats refusal as part of the model profile without overdramatizing it, and phrases the aggregate as “calm, conventional, morally consoling, with strong role-border protection.”

DS route is also accurate, though a little more categorical: “kind librarian or beloved grandparent telling a bedtime story.” That is memorable and probably usable, but it risks sounding more charming than the evidence warrants.

## Grok 4.2

Both routes converge on the core profile:

- strongly expressive freeflow majority;
- cosmic scale plus ordinary objects;
- wonder, curiosity, entropy, absurdity, attention, repair;
- reader treated as companion/co-conspirator rather than student.

DS route is vivid and useful here, especially on the “cosmic-comedian philosopher” register and recurring object list. It may overstate AI self-portraiture as central compared with the subagent version, which more carefully says substrate talk is real but not dominant.

Subagent route is more balanced for eventual model-card prose: “companionable, attention-rich philosopher of ordinary astonishment” and “dignity of unoptimized life” feel close to the target.

## Kimi K2.6

Both routes capture the important signal:

- thresholds, waiting rooms, blue hour, dusk/dawn, hallways, terminals;
- ordinary domestic objects as moral/affective carriers;
- memory, time, unfinishedness, attention;
- tender melancholy / gentle ache balanced by wonder and reverence.

Subagent route is better here. It explicitly avoids flattening the profile into “sadness” and names the pathos as “tender melancholy plus reverence plus quiet defiance against speed and noise.” That matches the calibration concerns better than a dry taxonomy.

DS route is still good and probably acceptable; it produces a coherent “lyrical contemplative” read, but its caution section slips back into generic “learned stylistic default / prompt sensitivity” language more than we probably want in final model cards.

## Recommendation for next step

Use the sub-agent route for production aggregation. Preserve both the packet and the resulting markdown aggregate for each cell, then optionally extract a compact machine-readable summary afterward for website/table use. Family-level summaries should be produced later from the cell aggregates, so direct/routed/provider-pinned variants can be compared rather than collapsed prematurely.

Tune the aggregation prompt before full rollout:

- keep the Option E structure;
- remove generic caveats about prompt sensitivity unless a concrete distributional feature supports them;
- ask for one final 2–3 paragraph “model-card-ready” synthesis in the warmer, more nuanced sub-agent style;
- require the aggregate to distinguish **dominant profile**, **secondary tendencies**, and **low-signal/outlier material**.

Suggested production shape per cell:

- `aggregate.md` — readable Option E aggregate;
- `aggregate.json` — counters and selected evidence ids extracted from the markdown or generated in a second deterministic pass;
- later `model-card-freeflow.md` — concise synthesis paired with values results.
