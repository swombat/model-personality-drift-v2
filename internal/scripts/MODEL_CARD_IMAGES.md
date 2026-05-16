# Model-card banner images — method & runbook

Every model card on the site (full page + index mini-card) has an
oil-painterly banner that depicts that model's *personality*, derived from
its full personality-card synthesis. This doc is the durable method so new
models added to the corpus can get an image the same way.

## What generates them

`internal/scripts/generate_model_images.py` — uses Google **Nano Banana Pro**
(`nano-banana-pro-preview`) via the `google-genai` SDK.

- **API key**: `${GEMINI_IMAGE_CONFIG:-../pa/automation/config/gemini.json}`
  (gitignored; key under `"api_key"`).
- **Prompts**: a `PROMPTS` dict in the script, keyed by **site slug**
  (e.g. `gpt-5-5`, `grok-4-3` — the same slug used in `models.json`).
- **Aspect**: requests Nano Banana Pro's native **21:9** (the widest preset;
  closest supported to the original 3:1 ask). The frame is **never cropped** —
  cropping clipped composed subjects. Output is the full 21:9 image.
- **Outputs**, per slug:
  - `website/public/images/models/{slug}.webp` — full banner, 1500px wide
  - `website/public/images/models/{slug}-thumb.webp` — card thumb, 600px wide
- **Raw cache**: `internal/model-card-images/raw/{slug}.png` (gitignored).
  Re-runs reuse the cached raw (no API call / cost) unless `--force`.

## How it reaches the website (automatic)

`website/scripts/generate_data.py` → `model_images(slug)` attaches
`image` / `image_thumb` fields to each model in `models.json` **only when the
webp files exist**. So:

- Regenerating data never drops images.
- A model with no render simply has no banner (clean fallback).
- `[model].astro` renders the full banner at the top of the page;
  `index.astro` renders the thumb full-bleed at the top of the mini-card;
  styling is in `website/src/styles/global.css` (`.model-banner`,
  `.card-thumb`) — natural ratio, no browser-side crop.

CI (`.github/workflows/pages.yml`) runs `refresh:openrouter` then `build`;
`refresh_openrouter.py` preserves all non-OpenRouter fields, so committed
image fields survive deploys.

## Adding an image for a NEW model

1. **Find the slug** — it's the `model` value in
   `website/src/generated/models.json` (e.g. `opus-4-8`). Read that model's
   `personality_card_markdown` (the full synthesis, *not* the 5–10-word
   strapline) — the image must come from the card's concrete signature
   imagery so it's specific, not generic.

2. **Write a bespoke prompt** — add an entry to `PROMPTS` in
   `generate_model_images.py`. 2–3 sentences: the *one* load-bearing scene
   that is faithful and **distinct** from sibling models (many cards converge
   on "tender custodian of mugs/rain/thresholds" — differentiate
   deliberately). Don't restate house style; the shared `STYLE` constant
   already enforces oil impasto, kindness, horizontal, no text/logos.

3. **Generate** (parallel, fail-soft):
   ```bash
   cd /path/to/model-personality-corpus
   python3 internal/scripts/generate_model_images.py opus-4-8        # one
   python3 internal/scripts/generate_model_images.py --all           # all missing/cached
   python3 internal/scripts/generate_model_images.py --force opus-4-8 # re-roll
   ```
   Flags: `--workers N` (default 6), `--all`, `--force`, `--list`.

4. **Review** the webp visually. Re-roll with `--force` if it missed.

5. **Wire + deploy**:
   ```bash
   cd website && python3 scripts/generate_data.py && npm run build
   cd .. && git add internal/scripts/generate_model_images.py \
     website/public/images website/src/generated/models.json
   git commit && git push origin main   # push to main = deploy via Actions
   ```

## Notes

- One image per API call; the model occasionally bakes in a faint faux
  painter's signature — painterly enough to keep; strip via re-roll if
  unwanted.
- Keep prompts kind and personality-faithful — these are portraits of a
  sensibility, not robots or logos.
- Last full run: 2026-05-15, all 46 then-current models.
