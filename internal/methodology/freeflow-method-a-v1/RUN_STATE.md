# Method A run state

Started: 2026-05-13

Corpus size from `freeflow-taxonomy/sample_coding.tsv`:

- 10,620 samples
- 48 models
- 152 cells

Initial subagent starter chunks launched:

| Chunk | Models | Expected rows | Output |
|---|---|---:|---|
| starter_a | deepseek-chat, gemini-2-5-pro, gemini-3-1-pro, qwen3-6-plus, qwen3-coder-plus, kimi-k2-6 | 150 | `chunks/method_a_starter_a.jsonl` |
| anthropic_a | opus/sonnet/haiku starter models | 325 | `chunks/method_a_anthropic_a.jsonl` |
| openai_a | gpt-4.1, gpt-4o, gpt-5 family non-codex/non-5.1-codex starter | 600 | `chunks/method_a_openai_a.jsonl` |

Remaining after starter chunks: larger routed models and coding-specific/OpenAI codex variants, to be chunked after checking quality of the first outputs.

Additional chunks launched after starter validation:

| Chunk | Models | Expected rows | Output |
|---|---|---:|---|
| deepseek_b | deepseek-v3-2, deepseek-v4-pro | 2087 | `chunks/method_a_deepseek_b.jsonl` |
| glm51_b | glm-5-1 | 1748 | `chunks/method_a_glm51_b.jsonl` |
| glm_other_b | glm-4-7, glm-4-6, glm-4-5, glm coding variants | 2500 | `chunks/method_a_glm_other_b.jsonl` |
| kimi_minimax_b | Kimi except K2.6 + MiniMax | 2310 | `chunks/method_a_kimi_minimax_b.jsonl` |
| grok_codex_b | Grok/xAI + GPT Codex variants | 925 | `chunks/method_a_grok_codex_b.jsonl` |

Note: starter chunks are structurally valid. OpenAI starter is somewhat formulaic and may need later spot-check/repair, but it is usable as first-pass extraction.

## Completion update — 2026-05-13

Merged dataset complete:

- `sample_impressions.jsonl` — 10,620 rows
- `sample_impressions.tsv` — TSV mirror
- `MERGE_QA.md` — 0 missing / 0 extra / 0 duplicates / 0 parse errors
- `REPRESENTATIVE_QA.md` — 0 non-verbatim or empty representative sentences after repair
- `MODEL_INDEX.md` and `per-model/*.md` — auto-generated review cards for 48 models

Caveat: optional tags are rough retrieval aids and currently noisy in places, especially the locally repaired OpenAI chunk. See `QA_NOTES.md`.
