"""Centralized corpus path constants.

Single source of truth for absolute paths into the v1 and v2 corpora.
All scripts in this directory MUST import from here rather than hard-coding
paths — a stale absolute path silently regenerates a wrong analysis, and
the 2026-05-08 codex-review-01 incident (drift-paper pointed at probe-v2
instead of corpus-v2 and missed 17+ values cells) is the canonical
reminder of why this matters.

Update only here when corpus locations change.
"""
from pathlib import Path

# v2 corpus (canonical) — companion v2 bundle, Zenodo DOI 10.5281/zenodo.20013518
V2_FREEFLOW = Path(
    "/Users/danieltenner/dev/contemplative-essayist-corpus-v2/data/traces_freeflow"
)
V2_VALUES = Path(
    "/Users/danieltenner/dev/contemplative-essayist-corpus-v2/data/traces_values"
)

# v1 corpus (legacy, retained for cross-version drift comparisons)
V1_FREEFLOW = Path(
    "/Users/danieltenner/dev/codex-check/model-personality-probe/data/traces_freeflow"
)
V1_VALUES = Path(
    "/Users/danieltenner/dev/codex-check/model-personality-probe/data/traces_values"
)
