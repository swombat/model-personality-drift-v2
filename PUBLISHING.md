# Publishing to Zenodo

This repository is published to Zenodo via the **GitHub ↔ Zenodo integration**:
Zenodo watches the repo and, when a GitHub *Release* is created, archives that
release and mints a DOI. The release metadata is taken from `.zenodo.json` in
the repo root.

## State of readiness

Repository-side artifacts are in place and consistent:

- [x] `.zenodo.json` — title, description, three creators (Daniel, Lume, Mira),
      keywords, CC-BY-4.0, `isDerivedFrom` the raw corpus DOI, `references` the
      v1 article DOI, version `1.0.0`.
- [x] `CITATION.cff` — matches `.zenodo.json`; references source corpus + v1
      article.
- [x] `CREDITS.md` — author note and per-contributor notes (Daniel = direction
      / meta-analysis; Mira = analysis; Lume = the other aspects).
- [x] `LICENSE` — dual-licensed: CC BY 4.0 for data/documentation, MIT for
      software (source code). Boundary defined in `LICENSE`.
- [x] `README.md` — author/credit section aligned with the above.

## Steps to actually publish (Daniel — needs your Zenodo + GitHub account)

1. **Enable the repo in Zenodo.** Log in to <https://zenodo.org> with the GitHub
   account that owns `swombat/model-personality-analysis-corpus`. Go to
   *Account → GitHub*, find `swombat/model-personality-analysis-corpus`, and flip the
   toggle **On**. (One-time. If it was already enabled for a previous repo name,
   confirm it followed the rename.)
2. **Sanity-check `.zenodo.json`.** Confirm the three creators, the version
   string, and that the two `related_identifiers` DOIs are the ones you want
   (raw corpus `10.5281/zenodo.20013518`, v1 article `10.5281/zenodo.19512754`).
3. **Tag and release on GitHub.** Create a GitHub Release from the default
   branch with a tag matching the metadata version, e.g. `v1.0.0`, title
   "Model Personality Analysis Corpus v1.0.0". Publishing the release is what triggers
   Zenodo.
4. **Wait for Zenodo to archive.** Within a few minutes Zenodo creates a record
   and mints two DOIs: a *version* DOI for `v1.0.0` and a *concept* DOI for "all
   versions".
5. **Backfill the DOIs.** Add the Zenodo DOI badge to `README.md`, replace the
   "DOI to be assigned" lines in `README.md` / `CREDITS.md` / `LICENSE` with the
   concept DOI, and add the concept DOI to `CITATION.cff` (top-level
   `identifiers:` / `doi:`). Commit as a small post-release housekeeping change
   (it does not need its own release).

## Notes for release review

- **Source corpus link checked.** The raw corpus is public at
  <https://github.com/swombat/model-personality-corpus-v2> and its Zenodo
  concept DOI is `10.5281/zenodo.20013518`.
- **Version.** First public release is `1.0.0`; tag `v1.0.0`.
- **Website sample bundles.** The release intentionally includes generated raw
  prompt/response copies under `website/public/data/samples/` for browser/audit
  use. The canonical raw corpus remains the sibling Zenodo/GitHub corpus above.
- **`internal/`** is intentionally included for provenance (calibration, audits,
  deprecated layers).
