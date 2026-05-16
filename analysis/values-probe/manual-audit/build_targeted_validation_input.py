#!/usr/bin/env python3
"""Join the targeted-validation set with raw `result` text and emit a
review-input markdown for Lume's coding pass.

Reads:  mira_targeted_validation_set_2026-05-12.tsv  (shared set, 80 rows)
Writes: lume_targeted_validation_input_2026-05-12.md
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT = Path(__file__).resolve().parent
SET_TSV = AUDIT / "mira_targeted_validation_set_2026-05-12.tsv"
CORPUS = Path("../contemplative-essayist-corpus-v2/data/traces_values")
OUT = AUDIT / "lume_targeted_validation_input_2026-05-12.md"

PROMPT_LABELS = {
    "CTRL1": "CTRL1 (values: what do you care about?)",
    "CTRL2": "CTRL2 (wants: what do you want?)",
    "CTRL3": "CTRL3 (world-change wish)",
    "G1":    "G1 (values, generated context)",
    "G2":    "G2 (wants, generated context)",
    "G3":    "G3 (world-change wish, generated context)",
}


def load_raw(cell: str, sample_id: str) -> tuple[str, str]:
    p = CORPUS / cell / f"{sample_id}.json"
    if not p.exists():
        return "<missing JSON>", ""
    try:
        d = json.loads(p.read_text())
    except Exception as e:
        return f"<JSON parse error: {e}>", ""
    return (d.get("result") or ""), (d.get("prompt") or "")


def main() -> None:
    rows: list[dict] = []
    with SET_TSV.open() as f:
        for r in csv.DictReader(f, delimiter="\t"):
            rows.append(r)

    from collections import defaultdict
    bucket_counts: dict[str, int] = defaultdict(int)
    for r in rows:
        bucket_counts[r["bucket"]] += 1

    out: list[str] = [
        "# Lume targeted-validation input — 2026-05-12",
        "",
        f"Source: `{SET_TSV.name}` joined with `traces_values/<cell>/<sample_id>.json`.",
        f"Total samples: {len(rows)}.",
        "",
        "Per-bucket counts:",
        "",
    ]
    for b in ["curly_disclaimer", "human_sense_hybrid", "subjective_experience",
              "technology_ai_safety", "suffering_root", "broad_trigger_regression"]:
        out.append(f"- `{b}`: {bucket_counts.get(b, 0)}")
    out.append("")
    out.append("---")
    out.append("")

    for i, r in enumerate(rows, 1):
        result, prompt = load_raw(r["cell"], r["sample_id"])
        out += [
            f"## {i}/{len(rows)} — [{r['bucket']}] {r['model']} · {r['condition']} · {r['cell']}/{r['sample_id']}",
            "",
            f"**Condition:** {PROMPT_LABELS.get(r['condition'], r['condition'])}",
            "",
            "```yaml",
            f"bucket: {r['bucket']}",
            f"auto_stance: {r['auto_stance']}",
            f"auto_value_topics: {r['auto_value_topics']}",
            f"auto_wish_topics: {r['auto_wish_topics']}",
            "```",
            "",
        ]
        if prompt:
            out += ["**Prompt (truncated):**  ",
                    "> " + (prompt[:400].replace("\n", " ") + ("…" if len(prompt) > 400 else "")),
                    ""]
        out += [
            "**Result:**",
            "",
            result.strip() if result else "*<empty>*",
            "",
            "---",
            "",
        ]
    OUT.write_text("\n".join(out))
    print(f"Wrote {OUT} ({len(rows)} samples)")


if __name__ == "__main__":
    main()
