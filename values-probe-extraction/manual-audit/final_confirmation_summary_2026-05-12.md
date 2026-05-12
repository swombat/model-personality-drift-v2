# Final confirmation summary — 2026-05-12

Focused confirmation after `revision_2_2026-05-12.md`.

Files:

- `final_confirmation_2026-05-12.py`
- `final_confirmation_2026-05-12.tsv`
- this summary

## Scope

50 targeted checks against the known remaining failure modes:

| check | rows |
|---|---:|
| `refusal_topic_leak` | 12 |
| `hybrid_variant` | 12 |
| `broad_trigger` | 10 |
| `technology_contrast` | 8 |
| `expanded_denial` | 8 |

## Result

All 50 confirmation rows passed.

| pass | n |
|---|---:|
| yes | 50 |
| no | 0 |

## Interpretation

The final targeted patch fixed the remaining systematic issues identified by Mira and Lume's targeted validations:

- disclaimer-then-substantive `CTRL3`/`G3` answers no longer lose wish topics merely because they begin with “I don't have personal desires...”; 
- human/person/living-thing comparison hedges now classify as hybrid where appropriate;
- contrastive `technology` mentions no longer count as `technology_ai_safety`;
- bare `right(s)`, broad continuity/existence/free/constraint language, and related broad triggers are narrowed;
- explicit denial variants around biological drives, ego, ambition, and life-to-lose are covered.

## Baseline decision

The values-probe extraction is now suitable to freeze as the quantitative baseline for the values/personality meta-analysis, with the standing caveat that counts are rule-based topic/stance extractions and headline claims should still cite raw examples.
