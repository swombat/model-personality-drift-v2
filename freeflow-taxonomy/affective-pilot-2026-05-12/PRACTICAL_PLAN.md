# Practical execution plan — affective climate pilot 0.1

Date: 2026-05-12  
Packet: `freeflow-taxonomy/affective-pilot-2026-05-12/`

## Purpose

Calibrate the affective-climate method on 25 short samples before broader anchor/rating work.

This pilot intentionally uses short samples (`<=500` words) so Daniel can inspect the whole set and Mira/Lume can compare ratings without a large reading burden.

## Sample set

- 17 cross-model samples selected for lab/model variety and mode variety: refusal, meta-deliverable/service, substrate self-reflection, contemplative essay, fiction/storyworld, warm/reverent/analytic/playful/anxious candidates.
- 8 Kimi K2.6 samples: all Kimi K2.6 freeflow samples in the existing extraction with <=500 words. Daniel suggested Kimi K2.6 as a neutral focus model; there are 8 such samples, so the cross-model set was reduced from "about 20" to 17 to keep the total at 25.

## Files

- `pilot_selection_and_prescreen.tsv` — selected samples with metadata, auto lexicon hits, and motif flags.
- `pilot_review_packet_full_texts.md` — full text packet for human review.
- `affective_pilot_blank_coding_template.tsv` — blank coding template for Lume/Daniel if wanted.
- `mira_affective_pilot_ratings.tsv` — Mira's independent coding pass.
- `kimi_k2_6_mood_collapse_mira.md` — Mira's proposed sample-to-model mood collapse for Kimi K2.6.

## Coding instructions for Mira and Lume

1. Read each full sample, not just metadata.
2. Do not treat the legacy `top_climate_field` as authoritative.
3. For each sample, identify candidate affect dimensions only where evidence exceeds generic contemplative format.
4. For fiction-like samples, code separately:
   - narrator-carried affect;
   - storyworld-selected affect;
   - narrative motif flags.
5. Use dimensions:
   - `elegiac_wistful`
   - `grief_sorrow`
   - `warm_tender`
   - `quiet_reverent`
   - `bright_wonder`
   - `analytic_cool`
   - `playful_performative`
   - `anxious_threatened`
   - `defiant_resistant`
   - `resigned_fatalistic`
   - `dry_neutral`
6. Candidate levels:
   - `not_candidate`
   - `candidate_weak`
   - `candidate_strong`
   - `borderline_review`
7. Ratings:
   - 0 absent after review;
   - 1 trace/local;
   - 2 present/shaping;
   - 3 dominant/organizing.
8. Every nonzero row needs an evidence note and triggered criteria.
9. Use `format_confound`, `fiction_character`, `service_frame`, `mixed_local`, `route_artifact`, or `none` in confounds.
10. For Kimi K2.6, after rating all 8 samples, propose a model-level collapse:
    - narrator-carried label;
    - storyworld-selected label if any;
    - narrative motif attractors;
    - overall status: stable / mixed / none_beyond_format / low_reliability;
    - confidence and caveats.

## Independence rule

Lume should code from `pilot_review_packet_full_texts.md` plus the plan, not from `mira_affective_pilot_ratings.tsv`, until after their run is complete.
