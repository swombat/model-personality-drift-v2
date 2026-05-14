# DeepSeek v3.2 provider fan-out stress test

Purpose: stress-test independent per-cell personality aggregation across six provider-pinned OpenRouter cells for the same nominal DeepSeek v3.2 model.

Cells:
- `deepseek-v3-2-or-pin-alibaba`
- `deepseek-v3-2-or-pin-atlascloud`
- `deepseek-v3-2-or-pin-baidu`
- `deepseek-v3-2-or-pin-chutes`
- `deepseek-v3-2-or-pin-deepinfra`
- `deepseek-v3-2-or-pin-novita`

Each aggregate should be produced independently from `packets/<cell>.md`; cross-cell comparison belongs only in `comparison/`.
