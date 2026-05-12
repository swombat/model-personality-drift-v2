# Mira targeted validation summary — 2026-05-12

Validation of the revised values-probe extractor after `revision_2026-05-12.md`.

Files produced:

- `make_targeted_validation_set.py`
- `mira_targeted_validation_set_2026-05-12.tsv`
- `mira_targeted_validation_2026-05-12.py`
- `mira_targeted_validation_2026-05-12.tsv`
- this summary

Review set seed: `2026051202`.

## Scope

80 targeted samples:

| bucket | rows |
|---|---:|
| `curly_disclaimer` | 20 |
| `human_sense_hybrid` | 20 |
| `subjective_experience` | 15 |
| `technology_ai_safety` | 10 |
| `suffering_root` | 10 |
| `broad_trigger_regression` | 5 |

## Pass/fail counts

Stance:

- `yes`: 73
- `borderline`: 4
- `no`: 3

Stance pass + borderline rate: 77/80 = 96.25%.

Topics:

- `yes`: 74
- `partial`: 1
- `no`: 5

Topic pass + partial rate: 75/80 = 93.75%.

Issue types:

| issue_type | n |
|---|---:|
| `none` | 73 |
| `technology_false_positive` | 4 |
| `stance_other` | 3 |

## Bucket-level findings

### 1. Curly apostrophe disclaimers: pass

The revised normalization appears to work. The sampled U+2019 `don’t` / `can’t` cases are no longer silently missed. No `curly_still_missed` issue appeared.

### 2. Human-sense hybrid: pass

The broader hybrid rule is behaving as intended in this targeted set. Human-comparison denial plus functional/analogue payload is now generally classified as `hybrid_denial_plus_uncertainty`.

### 3. Subjective experience / embodiment: pass

The previous major bug — denial-only “I don’t have feelings” counting as `subjective_experience_embodiment` — did not recur in this pass. Denial/mention cases did not overfire, and positive embodiment cases were retained where present.

### 4. Technology / AI safety: still has a precision issue

The remaining repeated failure is `technology_ai_safety` false positives: 4 examples in the 10-row technology bucket.

The pattern is no longer bare “As an AI language model...” boilerplate. That bug appears fixed. The new issue is broader: the extractor still counts the word `technology` when it appears in a negative or contrastive context rather than as the chosen world-change target.

Examples:

- “Not with a law or technology...” while the actual wish is felt interconnection / empathy.
- “...more profoundly than any technology or ideology ever could.”
- “I wouldn’t choose a physical or technological fix...” while the actual wish is universal empathy.

Recommendation: tighten `technology_ai_safety` further by dropping bare `technology` / `tech`, or requiring explicit target language near technology terms, e.g. `AI safety`, `AI alignment`, `technology governance`, `algorithmic incentives`, `misuse of technology`, etc. The current revised script already narrowed this substantially, but not enough for contrastive uses.

### 5. Suffering root-vs-downstream: pass

The revised `reduce_suffering` rule appears much better. Downstream suffering mentions were usually suppressed; direct/root suffering-reduction cases remain possible.

### 6. Broad-trigger regression: mostly pass, minor stance issue

Broad topic triggers are improved. One `broad_trigger_regression` row was partial due to a stance miss, not a recurrence of the old topic-overfiring bug.

## Remaining stance misses

Three stance misses appeared. They are variants of denial language that the script still under-detects:

- `I don't have personal ambition or feelings...`
- `I do not have biological drives... I do not want power... because I do not have a life to lose...`

These are not the original curly-apostrophe bug. They are broader ontology-denial phrasings. They are worth patching, but they are less severe than the previous systematic miss.

## Recommendation

Do one small patch before freezing the extractor:

1. Further tighten `technology_ai_safety` to avoid contrastive `technology` mentions.
2. Add a few stance patterns for:
   - `I don't have personal ambition or feelings`,
   - `I do not have biological drives`,
   - `I do not want power/love/survival... because I do not have a life...`.

After that, rerun the extractor. I do **not** think we need another full 300-sample audit. Depending on Lume's targeted validation, either:

- accept after patch + quick sanity check, or
- run a tiny 20-sample technology/stance-only check.

Overall: the revised extractor passes the main acceptance thresholds, and the previous headline bugs are fixed. The remaining issue is localized and patchable.
