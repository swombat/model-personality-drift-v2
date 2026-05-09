# Model Personality Browser

Static Astro site for browsing the drift-paper per-model analyses and source samples.

## Regenerate Data

Run from the repository root:

```sh
python3 website/scripts/generate_data.py
```

The generator reads:

- `analyses/*.md`
- `website/src/generated/model-summaries.json`
- local corpus paths from `scripts/_corpus_paths.py`
- OpenRouter endpoint metadata where available

It writes:

- `website/src/generated/models.json`
- `website/public/data/samples/*.json`

The generated sample data is committed so GitHub Actions can build without access to the local sibling corpus checkout.

## Develop

```sh
cd website
npm install
npm run dev
```

## Build

```sh
cd website
npm run build
```

GitHub Pages deploys `website/dist` through `.github/workflows/pages.yml`.
