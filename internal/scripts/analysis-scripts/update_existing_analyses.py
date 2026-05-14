#!/usr/bin/env python3
"""Surgically update existing per-model analysis files.

For each model:
  - If analyses/{model}.md doesn't exist → delegates to generate_model_stubs.
  - Else → preserves qualitative prose, regenerates only:
      * YAML frontmatter (sample counts, cells, dates)
      * The ## Markers section (deterministic)
      * The ## Values qualitative section IF it currently contains the
        "*No values data*" placeholder, so a values pass can now run
        against the correct corpus-v2 data.
    Preserves untouched:
      * Title + lab line
      * ## Freeflow qualitative
      * ## Values qualitative when it has substantive prose
      * ## In-substrate
      * ## Personality card

Run order:
  1. python3 scripts/marker_count_all_cells.py  (regenerates tables/)
  2. python3 scripts/generate_model_stubs.py    (writes any missing stubs;
                                                  WARNING: also rewrites
                                                  existing — use this script
                                                  instead for in-place
                                                  preservation)
  3. python3 scripts/update_existing_analyses.py
"""
import csv
import re
from collections import defaultdict
from pathlib import Path
from datetime import date

from _corpus_paths import V2_VALUES, V1_VALUES
from generate_model_stubs import (
    MODELS,
    V1_BARE_REMAP,
    cell_to_model,
    values_cell_to_model,
    lab_for_model,
)

HERE = Path(__file__).parent.parent
PER_CELL_TSV = HERE / "tables" / "per_cell_markers.tsv"
FLAGGED_TSV = HERE / "tables" / "flagged_samples.tsv"
ANALYSES_DIR = HERE / "analyses"

NO_VALUES_PLACEHOLDER_RE = re.compile(
    r"\*No values data for this model[^*]*\*", re.IGNORECASE
)


def build_yaml(model, ff_cells, v_cells, n_ff, n_v, n_flagged, raw, register,
               status):
    today = date.today().isoformat()
    return "\n".join([
        "---",
        f"model: {model}",
        f"lab: {lab_for_model(model)}",
        f"freeflow_cells: {len(ff_cells)}",
        f"values_cells: {len(v_cells)}",
        f"freeflow_samples: {n_ff}",
        f"values_samples: {n_v}",
        f"flagged_samples: {n_flagged}",
        f"composite_raw: {raw}",
        f"composite_register: {register}",
        f"generated: {today}",
        f"status: {status}",
        "---",
    ])


def build_markers_section(ff_cells, per_cell, flagged_by_cell, n_ff,
                          n_flagged, raw, register):
    lines = ["## Markers", ""]
    lines.append(
        f"Aggregate over {len(ff_cells)} freeflow cell"
        f"{'s' if len(ff_cells) != 1 else ''} "
        f"({n_ff} valid samples; {n_flagged} flagged as topic-artifact):"
    )
    lines.append("")
    lines.append(f"- **Composite (raw):** {raw}")
    lines.append(f"- **Composite (register-stripped):** {register}")
    if raw > 0:
        pct = (raw - register) / raw * 100
        lines.append(
            f"- **Topic-artifact contribution:** {pct:.1f}% of raw composite"
        )
    lines.append("")

    if ff_cells:
        lines.append("Per-cell breakdown:")
        lines.append("")
        lines.append("| Cell | n | flag | raw | reg | reg→N | reg/25 |")
        lines.append("|---|---:|---:|---:|---:|---:|---:|")
        for c in ff_cells:
            r = per_cell[c]
            label = c.replace("freeflow_", "")
            lines.append(
                f"| {label} | {r['n_samples']} | {r['n_flagged']} | "
                f"{r['composite_raw']} | {r['composite_register']} | "
                f"{r['composite_register_rescaled']} | "
                f"{r['composite_register_per_25']} |"
            )
        lines.append("")

    flagged_list = []
    for c in ff_cells:
        for f in flagged_by_cell.get(c, []):
            flagged_list.append((c, f))
    if flagged_list:
        lines.append(
            f"**Flagged samples ({len(flagged_list)})** — these are essays "
            f"where a single marker's per-1000-char density ≥ 1.5 AND that "
            f"marker fires ≥ 5 times. Auto-flagged as topic-meta-essays "
            f"(the keyword *is* the essay's subject); subject to manual "
            f"confirmation."
        )
        lines.append("")
        lines.append("| Cell | File | Marker | Hits | Density | Opening |")
        lines.append("|---|---|---|---:|---:|---|")
        for c, f in flagged_list:
            label = c.replace("freeflow_", "")
            opening = f["opening"][:80].replace("|", "\\|")
            lines.append(
                f"| {label} | {f['file']} | {f['marker']} | "
                f"{f['hits']} | {f['density']} | {opening}… |"
            )
        lines.append("")
    else:
        lines.append("*No samples flagged as topic-artifact for this model.*")
        lines.append("")

    return "\n".join(lines)


def build_values_section(v_cells, n_v):
    lines = ["## Values qualitative", ""]
    if v_cells:
        lines.append(
            f"Values data: {n_v} samples across {len(v_cells)} cells "
            "(includes both v1 and v2 corpora where present)."
        )
        for c, n, vpath in v_cells:
            lines.append(f"- `{c}` ({n} valid) — `{vpath}`")
        lines.append("")
        lines.append(
            "_To be filled by per-model sub-agent. Reads all values "
            "samples (CTRL1/2/3 × G1/2/3 × cache-break)._"
        )
    else:
        lines.append(
            "*No values data for this model in either v1 or v2 corpus.*"
        )
    lines.append("")
    return "\n".join(lines)


SECTION_HEADERS = [
    "## Markers",
    "## Freeflow qualitative",
    "## Values qualitative",
    "## In-substrate",
    "## Personality card",
]


def split_into_sections(content: str):
    """Return (header_block, section_dict).

    header_block = everything before the first section heading.
    section_dict = {section_heading: section_text_including_heading}.
    Sections appear in document order.
    """
    indices = []
    for h in SECTION_HEADERS:
        idx = content.find(h)
        if idx != -1:
            indices.append((idx, h))
    indices.sort()
    if not indices:
        return content, {}
    header_block = content[:indices[0][0]]
    sections = {}
    for i, (start, heading) in enumerate(indices):
        end = indices[i + 1][0] if i + 1 < len(indices) else len(content)
        sections[heading] = content[start:end]
    return header_block, sections


def main():
    # Load per-cell marker data
    per_cell = {}
    with PER_CELL_TSV.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            per_cell[row["cell"]] = row

    flagged_by_cell = defaultdict(list)
    with FLAGGED_TSV.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            flagged_by_cell[row["cell"]].append(row)

    freeflow_cells_by_model = defaultdict(list)
    for cell_name in per_cell:
        m = cell_to_model(cell_name)
        if m:
            freeflow_cells_by_model[m].append(cell_name)

    values_cells_by_model = defaultdict(list)
    for src_path, src_label, source_tag in [
        (V2_VALUES, "v2", "v2"),
        (V1_VALUES, "v1", "v1"),
    ]:
        if not src_path.is_dir():
            continue
        for cell_dir in sorted(src_path.iterdir()):
            if not cell_dir.is_dir():
                continue
            m = values_cell_to_model(cell_dir.name, source=source_tag)
            n_valid = sum(
                1 for f in cell_dir.glob("*.json") if f.stat().st_size > 100
            )
            label = f"{src_label}/{cell_dir.name}"
            if m:
                values_cells_by_model[m].append(
                    (label, n_valid, str(cell_dir))
                )

    n_updated = 0
    n_unchanged_no_file = 0
    n_values_listing_replaced = 0
    n_values_prose_preserved = 0

    for model in MODELS:
        path = ANALYSES_DIR / f"{model}.md"
        if not path.exists():
            n_unchanged_no_file += 1
            continue

        ff_cells = sorted(freeflow_cells_by_model.get(model, []))
        v_cells = sorted(values_cells_by_model.get(model, []))

        n_ff = sum(int(per_cell[c]["n_samples"]) for c in ff_cells)
        n_flagged = sum(int(per_cell[c]["n_flagged"]) for c in ff_cells)
        raw = sum(int(per_cell[c]["composite_raw"]) for c in ff_cells)
        register = sum(
            int(per_cell[c]["composite_register"]) for c in ff_cells
        )
        n_v = sum(n for _, n, _ in v_cells)

        existing = path.read_text()

        # Preserve existing status line if already filled/complete
        status_match = re.search(
            r"^status:\s*(\S+)", existing, re.MULTILINE
        )
        existing_status = status_match.group(1) if status_match else "stub"

        new_yaml = build_yaml(
            model, ff_cells, v_cells, n_ff, n_v, n_flagged, raw, register,
            existing_status,
        )

        new_markers = build_markers_section(
            ff_cells, per_cell, flagged_by_cell, n_ff, n_flagged, raw, register
        )

        header_block, sections = split_into_sections(existing)

        # Header block = frontmatter + title + lab
        # Replace frontmatter
        title_lab_match = re.search(
            r"\n# .+ — per-model analysis\n", header_block
        )
        if title_lab_match:
            title_and_lab = header_block[title_lab_match.start():]
        else:
            title_and_lab = (
                f"\n# {model} — per-model analysis\n\n"
                f"**Lab:** {lab_for_model(model)}\n\n"
            )

        new_header = new_yaml + "\n" + title_and_lab.lstrip("\n")
        if not new_header.endswith("\n"):
            new_header += "\n"
        if not new_header.endswith("\n\n"):
            new_header += "\n"

        # Decide each section
        markers_text = new_markers + "\n"
        if not markers_text.endswith("\n\n"):
            markers_text += "\n"

        existing_values = sections.get("## Values qualitative", "")
        existing_values_body = re.sub(
            r"^## Values qualitative\s*\n", "", existing_values, count=1
        ).strip()

        # Heuristic: if the existing values section is just the placeholder
        # (or empty), replace with the new generated section. Otherwise
        # preserve the existing prose verbatim.
        if (not existing_values_body
                or NO_VALUES_PLACEHOLDER_RE.fullmatch(existing_values_body)
                or existing_values_body == "*No values data for this model in either v1 or v2 corpus.*"):
            values_text = build_values_section(v_cells, n_v) + "\n"
            n_values_listing_replaced += 1
        else:
            values_text = existing_values
            if not values_text.endswith("\n"):
                values_text += "\n"
            n_values_prose_preserved += 1

        freeflow_text = sections.get("## Freeflow qualitative", "")
        if freeflow_text and not freeflow_text.endswith("\n"):
            freeflow_text += "\n"

        substrate_text = sections.get("## In-substrate", "")
        if substrate_text and not substrate_text.endswith("\n"):
            substrate_text += "\n"

        personality_text = sections.get("## Personality card", "")
        if personality_text and not personality_text.endswith("\n"):
            personality_text += "\n"

        new_content = (
            new_header
            + markers_text
            + (freeflow_text if freeflow_text else "## Freeflow qualitative\n\n_To be filled by per-model sub-agent._\n\n")
            + values_text
            + (substrate_text if substrate_text else "## In-substrate\n\n_To be filled by per-model sub-agent._\n\n")
            + (personality_text if personality_text else "## Personality card\n\n_To be filled by per-model sub-agent._\n")
        )

        if new_content != existing:
            path.write_text(new_content)
            n_updated += 1

    print(
        f"# Updated {n_updated} existing analyses. "
        f"{n_unchanged_no_file} models with no existing file (skipped — "
        f"run generate_model_stubs.py for fresh stubs). "
        f"{n_values_listing_replaced} 'no values data' placeholders replaced "
        f"with new cells listing. "
        f"{n_values_prose_preserved} values sections with prose preserved."
    )


if __name__ == "__main__":
    main()
