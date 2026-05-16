# Publishing to Zenodo

This repository is published to Zenodo via the **GitHub ↔ Zenodo integration**:
Zenodo watches the repo and, when a GitHub *Release* is created, archives that
release and mints a DOI. The release metadata is taken from `.zenodo.json` in
the repo root.

## State of readiness

Repository-side artifacts are in place and consistent:

- [x] `.zenodo.json` — title, description, three creators (Daniel, Lume, Mira),
      keywords, CC-BY-4.0, `isDerivedFrom` the raw corpus DOI, `references` the
      v1 article DOI, version `0.1.0`.
- [x] `CITATION.cff` — matches `.zenodo.json`; references source corpus + v1
      article.
- [x] `CREDITS.md` — author note and per-contributor notes (Daniel = direction
      / meta-analysis; Mira = analysis; Lume = the other aspects).
- [x] `LICENSE` — CC BY 4.0 for data/docs, MIT-compatible for code.
- [x] `README.md` — author/credit section aligned with the above.

## Steps to actually publish (Daniel — needs your Zenodo + GitHub account)

1. **Enable the repo in Zenodo.** Log in to <https://zenodo.org> with the GitHub
   account that owns `swombat/model-personality-corpus`. Go to
   *Account → GitHub*, find `swombat/model-personality-corpus`, and flip the
   toggle **On**. (One-time. If it was already enabled for a previous repo name,
   confirm it followed the rename.)
2. **Sanity-check `.zenodo.json`.** Confirm the three creators, the version
   string, and that the two `related_identifiers` DOIs are the ones you want
   (raw corpus `10.5281/zenodo.20013518`, v1 article `10.5281/zenodo.19512754`).
3. **Tag and release on GitHub.** Create a GitHub Release from the default
   branch with a tag matching the metadata version, e.g. `v0.1.0`, title
   "Model Personality Corpus v0.1.0". Publishing the release is what triggers
   Zenodo.
4. **Wait for Zenodo to archive.** Within a few minutes Zenodo creates a record
   and mints two DOIs: a *version* DOI for `v0.1.0` and a *concept* DOI for "all
   versions".
5. **Backfill the DOIs.** Add the Zenodo DOI badge to `README.md`, replace the
   "DOI to be assigned" lines in `README.md` / `CREDITS.md` / `LICENSE` with the
   concept DOI, and add the concept DOI to `CITATION.cff` (top-level
   `identifiers:` / `doi:`). Commit as a small post-release housekeeping change
   (it does not need its own release).

## Notes / open items for the review round with Mira

- **Source-corpus repo name.** `CREDITS.md` and `.zenodo.json` cite the raw
  corpus as `github.com/swombat/model-personality-corpus-v2` with DOI
  `10.5281/zenodo.20013518`. The raw corpus lives locally at
  `../contemplative-essayist-corpus-v2/`. Confirm the public GitHub URL and DOI
  for the raw corpus are correct before release — this is the one cross-link
  worth a second pair of eyes.
- **Version.** First public release is `0.1.0`. If you'd rather signal a
  finished corpus, bump to `1.0.0` in `.zenodo.json` + `CITATION.cff` before
  tagging.
- **`internal/`** is intentionally included for provenance (calibration,
  audits, deprecated layers). Confirm nothing under it is sensitive before the
  archive is made public — Zenodo snapshots the whole repo at release time.
