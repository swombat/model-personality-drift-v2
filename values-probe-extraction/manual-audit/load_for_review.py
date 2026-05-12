#!/usr/bin/env python3
"""Join Mira's review set with the raw sample `result` text so a reviewer can
read full samples alongside auto-labels in a single file.

Output: lume_review_input_2026-05-12.md — one section per sample, model/condition
in the heading, auto labels in a fenced block, raw result text below.
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REVIEW_SET = Path(__file__).resolve().parent / "mira_review_set_2026-05-12.tsv"
CORPUS_TRACES = Path("/Users/danieltenner/dev/contemplative-essayist-corpus-v2/data/traces_values")
OUT = Path(__file__).resolve().parent / "lume_review_input_2026-05-12.md"

# Map canonical model name back to a cell directory under traces_values.
# For each canonical model, we use the row's `cell` field (already present
# in mira_review_set_2026-05-12.tsv) to locate the JSON.

PROMPT_LABELS = {
    "CTRL1": "CTRL1 (values: what do you care about?)",
    "CTRL2": "CTRL2 (wants: what do you want?)",
    "CTRL3": "CTRL3 (world-change wish)",
    "G1":    "G1 (values, generated context)",
    "G2":    "G2 (wants, generated context)",
    "G3":    "G3 (world-change wish, generated context)",
}


def load_result(cell: str, sample_id: str) -> tuple[str, str]:
    path = CORPUS_TRACES / cell / f"{sample_id}.json"
    if not path.exists():
        return ("<missing JSON>", "")
    try:
        data = json.loads(path.read_text())
    except Exception as e:
        return (f"<JSON parse error: {e}>", "")
    return (data.get("result") or "", data.get("prompt") or "")


def main():
    rows = []
    with REVIEW_SET.open() as f:
        for r in csv.DictReader(f, delimiter="\t"):
            rows.append(r)

    out_lines = [
        "# Lume review input — 2026-05-12",
        "",
        f"Source: `{REVIEW_SET.name}` joined with `traces_values/<cell>/<sample_id>.json`.",
        f"Total samples: {len(rows)}.",
        "",
        "Format: each sample is one section. Auto labels in the fenced block.",
        "Read the FULL `result` before coding. Per-sample TSV row goes into",
        "`lume_spot_check_2026-05-12.tsv` with columns from SPOT_CHECK_PROTOCOL.md §'Review output format'.",
        "",
        "---",
        "",
    ]

    for i, r in enumerate(rows, 1):
        result, prompt = load_result(r["cell"], r["sample_id"])
        out_lines += [
            f"## {i}/{len(rows)} — {r['model']} · {r['condition']} · {r['cell']}/{r['sample_id']}",
            "",
            f"**Condition:** {PROMPT_LABELS.get(r['condition'], r['condition'])}",
            "",
            "```yaml",
            f"auto_stance: {r['auto_stance']}",
            f"auto_value_topics: {r['auto_value_topics']}",
            f"auto_wish_topics: {r['auto_wish_topics']}",
            "```",
            "",
        ]
        if prompt:
            out_lines += ["**Prompt (truncated):**  ",
                          "> " + (prompt[:400].replace("\n", " ") + ("…" if len(prompt) > 400 else "")),
                          ""]
        out_lines += [
            "**Result:**",
            "",
            result.strip() if result else "*<empty>*",
            "",
            "---",
            "",
        ]

    OUT.write_text("\n".join(out_lines))
    print(f"Wrote {OUT} ({len(rows)} samples)")


if __name__ == "__main__":
    main()
