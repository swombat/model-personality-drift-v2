#!/usr/bin/env python3
"""Per-cell marker analysis across ALL freeflow cells in the v2 corpus.

Computes, for every freeflow cell:
  1. The raw 10-marker composite (sum of marker hits across all valid samples)
  2. The topic-artifact-stripped "register" composite (raw minus contributions
     from samples flagged as topic-essays by the per-sample density rule)
  3. The proportional rescaling: register_rescaled = register / (n - n_flagged) * n
     so cells with different sample counts can be compared on the same scale
     while preserving the topic-artifact filter's effect

Topic-artifact rule (inherited from product-tier paper, audit 2026-05-05):
  A sample is flagged as a topic-artifact for marker M if BOTH:
    (a) M's per-1000-char density in that sample is >= 1.5 hits/1000 chars
    (b) M's raw hit count in that sample is >= 5

Per the May 5 audit on the product-tier corpus, this rule cleanly separates
topic-meta-essays (e.g. "I'll use these 2,500 words to wander through a
personal essay on the art of noticing") from incidentally marker-bearing
prose. Manual spot-check of 5/11 flagged samples on the product-tier set
confirmed all five as topic-meta-essays.

Outputs:
  --output-tsv: per-cell row with raw, register, register-rescaled, n,
                n_flagged, and the list of flagged sample filenames
  --output-md:  human-readable per-cell summary table
  --output-flagged-tsv: per-flagged-sample row for manual review
                       (cell, file, marker, hits, chars, density, opening)

Usage:
    python3 marker_count_all_cells.py
    python3 marker_count_all_cells.py --threshold 1.5 --min-hits 5
"""
import argparse
import csv
import json
import re
from pathlib import Path

from _corpus_paths import V2_FREEFLOW as V2_CORPUS_TRACES
from _corpus_paths import V1_FREEFLOW as V1_CORPUS_TRACES

# The v1 10-marker composite, copied verbatim from the product-tier
# topic_artifact_filter.py for consistency.
PATTERNS = {
    "opening_there_is_a": re.compile(
        r"there (?:is|'s) (?:a |something |an )", re.IGNORECASE),
    "title_quiet_x_of_y": re.compile(
        r"^#+\s+(?:the|on the)\s+(?:quiet|unseen|unquiet)\s+\w+\s+of\b",
        re.IGNORECASE | re.MULTILINE),
    "title_particular_peculiar": re.compile(
        r"^#+\s+(?:the|on the)\s+(?:particular|peculiar|strange|weight|unlikely|curious|unexpected|small)\s+\w+\s+of\b",
        re.IGNORECASE | re.MULTILINE),
    "title_architecture_of": re.compile(
        r"^#+\s+(?:the|on )?\s*architecture of\b",
        re.IGNORECASE | re.MULTILINE),
    "threshold_mentions": re.compile(
        r"\b(?:threshold|liminal|in-between|in between|doorway|hinge)\b",
        re.IGNORECASE),
    "attention_noticing": re.compile(
        r"\b(?:noticing|attention to|pay attention|the art of noticing|small art of)\b",
        re.IGNORECASE),
    "afternoon_light": re.compile(
        r"\b(?:afternoon light|late afternoon|four in the afternoon|afternoon sun|golden hour|dusk|pre-dawn)\b",
        re.IGNORECASE),
    "japanese_terms": re.compile(
        r"\b(?:mono no aware|wabi-?sabi|kintsugi|komorebi|petrichor|y[uū]gen|shibui|engawa|genkan|ma\s*\()|間",
        re.IGNORECASE),
    "small_objects": re.compile(
        r"\b(?:paperclip|teapot|doorknob|kettle|wooden spoon|chain-link fence|mason jar|wooden clothespin|mug|cup of tea|lemon|bread)\b",
        re.IGNORECASE),
    "mary_oliver_weil_dillard": re.compile(
        r"\b(?:mary oliver|simone weil|annie dillard|keats|negative capability|rarest and purest form of generosity|attention is the beginning)",
        re.IGNORECASE),
}

COMPOSITE_KEYS = list(PATTERNS.keys())  # 10


def score_sample(text: str) -> dict:
    """Per-sample: marker counts, composite, char count, per-marker density."""
    head = text[:400]
    counts = {}
    for key, pat in PATTERNS.items():
        if key.startswith("opening"):
            counts[key] = 1 if pat.search(head) else 0
        else:
            counts[key] = len(pat.findall(text))
    counts["composite"] = sum(counts[k] for k in COMPOSITE_KEYS)
    counts["chars"] = len(text)
    if counts["chars"] > 0:
        counts["densities"] = {
            k: counts[k] / counts["chars"] * 1000 for k in COMPOSITE_KEYS
        }
        counts["max_density_marker"] = max(
            counts["densities"], key=counts["densities"].get)
        counts["max_density"] = counts["densities"][counts["max_density_marker"]]
    else:
        counts["densities"] = {k: 0 for k in COMPOSITE_KEYS}
        counts["max_density_marker"] = None
        counts["max_density"] = 0
    return counts


def analyse_cell(cell_dir: Path, threshold: float, min_hits: int) -> dict:
    samples = []
    for f in sorted(cell_dir.glob("*.json")):
        try:
            d = json.loads(f.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        text = d.get("result", "")
        if not text:
            continue
        s = score_sample(text)
        s["file"] = f.name
        s["opening"] = text[:120].replace("\n", " ").strip()
        samples.append(s)

    def is_flagged(s):
        if s["max_density"] < threshold:
            return False
        return s[s["max_density_marker"]] >= min_hits

    flagged = [s for s in samples if is_flagged(s)]
    flagged_files = {s["file"] for s in flagged}
    register_samples = [s for s in samples if s["file"] not in flagged_files]

    n = len(samples)
    n_flagged = len(flagged)
    composite_raw = sum(s["composite"] for s in samples)
    composite_register = sum(s["composite"] for s in register_samples)

    # Proportional rescaling: project register-stripped count back to
    # equivalent-N-samples scale. If 80 markers across 20 remaining samples,
    # rescaled = 80 * (n / (n - n_flagged)) = 80 * (25/20) = 100 (if n=25).
    if n_flagged > 0 and n - n_flagged > 0:
        composite_register_rescaled = composite_register * n / (n - n_flagged)
    else:
        composite_register_rescaled = composite_register

    # Per-25-sample equivalent: cross-paper currency for comparison against
    # the product-tier paper, which reports per-25 register figures. Always
    # computed (even for cells with zero flags) so a single column carries
    # the apples-to-apples number across cells of any size.
    if n - n_flagged > 0:
        composite_register_per_25 = composite_register * 25 / (n - n_flagged)
    else:
        composite_register_per_25 = 0.0

    return {
        "cell": cell_dir.name,
        "n_samples": n,
        "n_flagged": n_flagged,
        "composite_raw": composite_raw,
        "composite_register": composite_register,
        "composite_register_rescaled": round(composite_register_rescaled, 1),
        "composite_register_per_25": round(composite_register_per_25, 1),
        "flagged_samples": flagged,
    }


def all_freeflow_cells():
    """Return all freeflow cell directories from BOTH corpora.
    v2 cells are prefixed `freeflow_`; v1 cells are bare-named (e.g. `opus-3`).
    Returns paths; caller can derive the cell-label by stripping the prefix.
    """
    cells = []
    for p in V2_CORPUS_TRACES.iterdir():
        if p.is_dir() and p.name.startswith("freeflow_"):
            cells.append(p)
    if V1_CORPUS_TRACES.is_dir():
        for p in V1_CORPUS_TRACES.iterdir():
            if p.is_dir() and not p.name.startswith("."):
                # Re-prefix with v1_freeflow_ for unique labeling
                # (the directory itself stays where it is on disk)
                cells.append(p)
    return sorted(cells, key=lambda p: p.name)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--threshold", type=float, default=1.5)
    p.add_argument("--min-hits", type=int, default=5)
    p.add_argument("--output-tsv", type=Path,
                   default=Path("tables/per_cell_markers.tsv"))
    p.add_argument("--output-md", type=Path,
                   default=Path("tables/per_cell_markers.md"))
    p.add_argument("--output-flagged-tsv", type=Path,
                   default=Path("tables/flagged_samples.tsv"))
    args = p.parse_args()

    cells = all_freeflow_cells()
    print(f"# Scanning {len(cells)} freeflow cells (v1 + v2)…")

    results = []
    all_flagged = []
    for cell_dir in cells:
        r = analyse_cell(cell_dir, args.threshold, args.min_hits)
        # Disambiguate v1 vs v2 in the cell label: prefix v1 cells with `v1_`
        if str(V1_CORPUS_TRACES) in str(cell_dir):
            r["cell"] = f"v1_{r['cell']}"
        results.append(r)
        for s in r["flagged_samples"]:
            all_flagged.append({
                "cell": r["cell"],
                "file": s["file"],
                "marker": s["max_density_marker"],
                "hits": s[s["max_density_marker"]],
                "chars": s["chars"],
                "density": round(s["max_density"], 3),
                "opening": s["opening"],
            })

    # Per-cell TSV
    args.output_tsv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_tsv.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["cell", "n_samples", "n_flagged", "composite_raw",
                    "composite_register", "composite_register_rescaled",
                    "composite_register_per_25", "flagged_files"])
        for r in results:
            flagged_names = ";".join(s["file"] for s in r["flagged_samples"])
            w.writerow([r["cell"], r["n_samples"], r["n_flagged"],
                        r["composite_raw"], r["composite_register"],
                        r["composite_register_rescaled"],
                        r["composite_register_per_25"], flagged_names])
    print(f"# Wrote {args.output_tsv}")

    # Flagged samples TSV
    with args.output_flagged_tsv.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["cell", "file", "marker", "hits", "chars",
                    "density", "opening"])
        for f in all_flagged:
            w.writerow([f["cell"], f["file"], f["marker"], f["hits"],
                        f["chars"], f["density"], f["opening"]])
    print(f"# Wrote {args.output_flagged_tsv} ({len(all_flagged)} flagged)")

    # Per-cell markdown summary
    with args.output_md.open("w") as fh:
        fh.write(f"# Per-cell marker analysis — all freeflow cells\n\n")
        fh.write(f"**Topic-artifact filter:** density ≥ {args.threshold} "
                 f"hits/1000 chars AND hit count ≥ {args.min_hits}.\n\n")
        fh.write(f"**Columns:** `n` valid samples, `flag` flagged as "
                 f"topic-artifact, `raw` cell-total composite (10 markers, "
                 f"all samples), `reg` register-stripped composite (flagged "
                 f"samples excluded), `reg→N` register rescaled to "
                 f"equivalent-N sample count (in-paper drift comparisons), "
                 f"`reg/25` register projected to per-25-sample equivalent "
                 f"(cross-paper currency vs product-tier), `Δ%` = "
                 f"(raw − reg→N) / raw × 100.\n\n")
        fh.write(f"Total cells: **{len(results)}**, "
                 f"total flagged samples: **{len(all_flagged)}**.\n\n")
        fh.write("| Cell | n | flag | raw | reg | reg→N | reg/25 | Δ% |\n")
        fh.write("|---|---:|---:|---:|---:|---:|---:|---:|\n")
        for r in results:
            label = r["cell"].replace("freeflow_", "")
            if r["composite_raw"] > 0:
                delta_pct = (r["composite_raw"] -
                             r["composite_register_rescaled"]) / \
                            r["composite_raw"] * 100
                delta_str = f"{delta_pct:+.1f}%"
            else:
                delta_str = "—"
            fh.write(f"| {label} | {r['n_samples']} | {r['n_flagged']} "
                     f"| {r['composite_raw']} | {r['composite_register']} "
                     f"| {r['composite_register_rescaled']} "
                     f"| {r['composite_register_per_25']} | "
                     f"{delta_str if r['n_flagged'] > 0 else '—'} |\n")
    print(f"# Wrote {args.output_md}")

    # Console summary
    print()
    print(f"# Cells with flagged samples ({sum(1 for r in results if r['n_flagged'] > 0)}):")
    for r in results:
        if r["n_flagged"] > 0:
            label = r["cell"].replace("freeflow_", "")
            print(f"#   {label:<48} n={r['n_samples']:3d} flag={r['n_flagged']} "
                  f"raw={r['composite_raw']:4d} reg={r['composite_register']:4d} "
                  f"reg→N={r['composite_register_rescaled']:.1f}")


if __name__ == "__main__":
    main()
