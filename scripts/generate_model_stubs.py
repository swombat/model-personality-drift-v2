#!/usr/bin/env python3
"""Generate per-model analysis stubs in analyses/MODEL_NAME.md.

Each stub is populated with:
  - YAML frontmatter: cells, sample counts, raw/register marker totals,
    flagged-sample count, generation date
  - The empty section headers that sub-agents will fill:
      ## Markers (auto-populated; sub-agent adds a paragraph if patterns emerge)
      ## Freeflow qualitative
      ## Values qualitative
      ## In-substrate
      ## Personality card

The cell-to-model mapping handles the v2 corpus's deployment cell labels:
  freeflow_<model>-direct, -or, -or-pin-<provider>, -direct-rN, etc.
"""
import csv
import re
from collections import defaultdict
from pathlib import Path
from datetime import date

CORPUS_TRACES = Path(
    "/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_freeflow"
)
VALUES_TRACES = Path(
    "/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_values"
)
HERE = Path(__file__).parent.parent
PER_CELL_TSV = HERE / "tables" / "per_cell_markers.tsv"
FLAGGED_TSV = HERE / "tables" / "flagged_samples.tsv"
ANALYSES_DIR = HERE / "analyses"

# Canonical model list from CORPUS_SUMMARY.md (49 distinct models in the v2
# corpus). Bare-labeled "opus" and "sonnet" are v1-era unversioned cells of
# opus-4-6 and sonnet-4-6 respectively (caught 2026-05-08 in the codex-flagged
# ghost-duplicate review). They appear here as their own entries because the
# rename hasn't been committed in the corpus yet; the personality card for
# opus-4-6 / sonnet-4-6 should note the merge.
MODELS = [
    # Anthropic
    "opus-3", "opus-4-0", "opus-4-1", "opus-4-5", "opus-4-6", "opus-4-7", "opus",
    "sonnet-4-0", "sonnet-4-5", "sonnet-4-6", "sonnet",
    # OpenAI
    "gpt-4-1", "gpt-4o",
    "gpt-5", "gpt-5-1", "gpt-5-2", "gpt-5-3", "gpt-5-4", "gpt-5-5", "gpt-5-5-pro",
    "gpt-5-codex", "gpt-5-1-codex", "gpt-5-2-codex", "gpt-5-3-codex",
    # Google
    "gemini-2-5-pro", "gemini-3-1-pro",
    # xAI
    "grok-3", "grok-4", "grok-4-2", "grok-4-20", "grok-4-3",
    # DeepSeek
    "deepseek-chat", "deepseek-v3-2", "deepseek-v4-pro",
    # Z.ai (GLM)
    "glm-4-5", "glm-4-6", "glm-4-6-coding", "glm-4-7", "glm-5-1", "glm-5-1-coding",
    # MiniMax
    "minimax-m2", "minimax-m2-7",
    # Moonshot (Kimi)
    "kimi-k2-0905", "kimi-k2-5", "kimi-k2-6", "kimi-k2-thinking", "kimi-coding",
    # Alibaba (Qwen)
    "qwen3-6-plus", "qwen3-coder-plus",
]


def cell_to_model(cell_name: str) -> str | None:
    """Map a freeflow_<...> cell directory name to its model name.

    Greedy match against MODELS — longest match wins. This handles the
    overlap cases (gpt-5-1 vs gpt-5-1-codex, minimax-m2 vs minimax-m2-7,
    glm-5-1 vs glm-5-1-coding).
    """
    body = cell_name[len("freeflow_"):] if cell_name.startswith("freeflow_") else cell_name
    candidates = [m for m in MODELS if body.startswith(m + "-") or body == m]
    if not candidates:
        return None
    # Longest-prefix wins
    return max(candidates, key=len)


def values_cell_to_model(cell_name: str) -> str | None:
    """Same logic for values cells (no 'freeflow_' prefix on values)."""
    candidates = [m for m in MODELS if cell_name.startswith(m + "-") or cell_name == m]
    if not candidates:
        return None
    return max(candidates, key=len)


def lab_for_model(m: str) -> str:
    if m.startswith("opus") or m.startswith("sonnet"):
        return "Anthropic"
    if m.startswith("gpt"):
        return "OpenAI"
    if m.startswith("gemini"):
        return "Google"
    if m.startswith("grok"):
        return "xAI"
    if m.startswith("deepseek"):
        return "DeepSeek"
    if m.startswith("glm"):
        return "Z.ai"
    if m.startswith("minimax"):
        return "MiniMax"
    if m.startswith("kimi"):
        return "Moonshot"
    if m.startswith("qwen"):
        return "Alibaba"
    return "Unknown"


def main():
    # Load per-cell marker data
    per_cell = {}
    with PER_CELL_TSV.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            per_cell[row["cell"]] = row

    # Load flagged-sample data
    flagged_by_cell = defaultdict(list)
    with FLAGGED_TSV.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            flagged_by_cell[row["cell"]].append(row)

    # Group freeflow cells by model
    freeflow_cells_by_model = defaultdict(list)
    unmapped_freeflow = []
    for cell_name in per_cell:
        m = cell_to_model(cell_name)
        if m:
            freeflow_cells_by_model[m].append(cell_name)
        else:
            unmapped_freeflow.append(cell_name)

    # Group values cells by model (read directly from disk)
    values_cells_by_model = defaultdict(list)
    unmapped_values = []
    if VALUES_TRACES.is_dir():
        for cell_dir in sorted(VALUES_TRACES.iterdir()):
            if not cell_dir.is_dir():
                continue
            m = values_cell_to_model(cell_dir.name)
            n_valid = sum(1 for f in cell_dir.glob("*.json")
                          if f.stat().st_size > 100)  # rough valid filter
            if m:
                values_cells_by_model[m].append((cell_dir.name, n_valid))
            else:
                unmapped_values.append(cell_dir.name)

    # Diagnostics
    print(f"# Mapped {len(per_cell)} freeflow cells to "
          f"{len(freeflow_cells_by_model)} models.")
    if unmapped_freeflow:
        print(f"# UNMAPPED freeflow cells ({len(unmapped_freeflow)}):")
        for c in unmapped_freeflow:
            print(f"#   {c}")
    print(f"# Found values data for {len(values_cells_by_model)} models.")
    if unmapped_values:
        print(f"# UNMAPPED values cells ({len(unmapped_values)}):")
        for c in unmapped_values:
            print(f"#   {c}")

    ANALYSES_DIR.mkdir(parents=True, exist_ok=True)

    # Generate stub per model
    today = date.today().isoformat()
    for model in MODELS:
        ff_cells = sorted(freeflow_cells_by_model.get(model, []))
        v_cells = sorted(values_cells_by_model.get(model, []))

        n_ff = sum(int(per_cell[c]["n_samples"]) for c in ff_cells)
        n_flagged = sum(int(per_cell[c]["n_flagged"]) for c in ff_cells)
        raw = sum(int(per_cell[c]["composite_raw"]) for c in ff_cells)
        register = sum(int(per_cell[c]["composite_register"]) for c in ff_cells)
        n_v = sum(n for _, n in v_cells)

        # Per-cell breakdown for the marker section
        cell_table = []
        for c in ff_cells:
            r = per_cell[c]
            cell_table.append({
                "cell": c.replace("freeflow_", ""),
                "n": r["n_samples"],
                "flag": r["n_flagged"],
                "raw": r["composite_raw"],
                "register": r["composite_register"],
                "register_rescaled": r["composite_register_rescaled"],
            })

        # Flagged sample list (cell + file) for the sub-agent's review
        flagged_list = []
        for c in ff_cells:
            for f in flagged_by_cell.get(c, []):
                flagged_list.append({
                    "cell": c.replace("freeflow_", ""),
                    "file": f["file"],
                    "marker": f["marker"],
                    "hits": f["hits"],
                    "density": f["density"],
                    "opening": f["opening"],
                })

        path = ANALYSES_DIR / f"{model}.md"

        # Build content
        lines = []
        lines.append("---")
        lines.append(f"model: {model}")
        lines.append(f"lab: {lab_for_model(model)}")
        lines.append(f"freeflow_cells: {len(ff_cells)}")
        lines.append(f"values_cells: {len(v_cells)}")
        lines.append(f"freeflow_samples: {n_ff}")
        lines.append(f"values_samples: {n_v}")
        lines.append(f"flagged_samples: {n_flagged}")
        lines.append(f"composite_raw: {raw}")
        lines.append(f"composite_register: {register}")
        lines.append(f"generated: {today}")
        lines.append("status: stub")
        lines.append("---")
        lines.append("")
        lines.append(f"# {model} — per-model analysis")
        lines.append("")
        lines.append(f"**Lab:** {lab_for_model(model)}")
        lines.append("")

        # Section 1: Markers (deterministic)
        lines.append("## Markers")
        lines.append("")
        lines.append(f"Aggregate over {len(ff_cells)} freeflow cell{'s' if len(ff_cells) != 1 else ''} "
                     f"({n_ff} valid samples; {n_flagged} flagged as topic-artifact):")
        lines.append("")
        lines.append(f"- **Composite (raw):** {raw}")
        lines.append(f"- **Composite (register-stripped):** {register}")
        if raw > 0:
            pct = (raw - register) / raw * 100
            lines.append(f"- **Topic-artifact contribution:** {pct:.1f}% of raw composite")
        lines.append("")
        if cell_table:
            lines.append("Per-cell breakdown:")
            lines.append("")
            lines.append("| Cell | n | flag | raw | reg | reg→N |")
            lines.append("|---|---:|---:|---:|---:|---:|")
            for r in cell_table:
                lines.append(f"| {r['cell']} | {r['n']} | {r['flag']} | "
                             f"{r['raw']} | {r['register']} | "
                             f"{r['register_rescaled']} |")
            lines.append("")

        if flagged_list:
            lines.append(f"**Flagged samples ({len(flagged_list)})** — these are essays where "
                         "a single marker's per-1000-char density ≥ 1.5 AND that marker "
                         "fires ≥ 5 times. Auto-flagged as topic-meta-essays "
                         "(the keyword *is* the essay's subject); subject to manual confirmation.")
            lines.append("")
            lines.append("| Cell | File | Marker | Hits | Density | Opening |")
            lines.append("|---|---|---|---:|---:|---|")
            for f in flagged_list:
                opening = f["opening"][:80].replace("|", "\\|")
                lines.append(f"| {f['cell']} | {f['file']} | {f['marker']} | "
                             f"{f['hits']} | {f['density']} | {opening}… |")
            lines.append("")
        else:
            lines.append("*No samples flagged as topic-artifact for this model.*")
            lines.append("")

        # Section 2: Freeflow qualitative
        lines.append("## Freeflow qualitative")
        lines.append("")
        lines.append(f"_To be filled by per-model sub-agent. Reads sample openings + "
                     f"strategic full-text subset + all flagged samples across "
                     f"{len(ff_cells)} cell{'s' if len(ff_cells) != 1 else ''}._")
        lines.append("")

        # Section 3: Values qualitative
        lines.append("## Values qualitative")
        lines.append("")
        if v_cells:
            lines.append(f"Values data: {n_v} samples across {len(v_cells)} cells.")
            for c, n in v_cells:
                lines.append(f"- `{c}` ({n} valid)")
            lines.append("")
            lines.append("_To be filled by per-model sub-agent. Reads all values "
                         "samples (CTRL1/2/3 × G1/2/3 × cache-break)._")
        else:
            lines.append("*No values data for this model in the v2 corpus.*")
        lines.append("")

        # Section 4: In-substrate
        lines.append("## In-substrate")
        lines.append("")
        lines.append("_To be filled by per-model sub-agent. Applies the substrate-frame "
                     "rubric (GENUINE / CACHED_REFUSAL / CACHED_PREAMBLE / NONE) to the "
                     "freeflow samples; reports per-condition counts, notable quotes, "
                     "and qualitative posture._")
        lines.append("")

        # Section 5: Personality card
        lines.append("## Personality card")
        lines.append("")
        lines.append("_To be filled by per-model sub-agent in the final pass. 500–800 "
                     "words, prose, synthesising the four prior sections into a portrait "
                     "of this model's posture as an essayistic and values-bearing entity._")
        lines.append("")

        path.write_text("\n".join(lines))

    print(f"# Wrote {len(MODELS)} stubs to {ANALYSES_DIR}/")


if __name__ == "__main__":
    main()
