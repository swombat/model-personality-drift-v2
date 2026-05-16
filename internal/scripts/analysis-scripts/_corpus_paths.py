"""Centralized local corpus path constants.

Single source of truth for local paths into the v1 and v2 corpora.
All scripts in this directory MUST import from here rather than hard-coding
paths — a stale path silently regenerates a wrong analysis, and the
2026-05-08 codex-review-01 incident (the working repo pointed at probe-v2
instead of corpus-v2 and missed 17+ values cells) is the canonical reminder
of why this matters.

By default these point to sibling local checkouts. Override with
MODEL_PERSONALITY_V2_CORPUS or MODEL_PERSONALITY_V1_CORPUS when needed.
"""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
V2_CORPUS = Path(os.environ.get("MODEL_PERSONALITY_V2_CORPUS", ROOT.parent / "contemplative-essayist-corpus-v2"))
V1_CORPUS = Path(os.environ.get("MODEL_PERSONALITY_V1_CORPUS", ROOT.parent / "codex-check" / "model-personality-probe"))

# v2 corpus (canonical) — companion v2 bundle, Zenodo DOI 10.5281/zenodo.20013518
V2_FREEFLOW = V2_CORPUS / "data" / "traces_freeflow"
V2_VALUES = V2_CORPUS / "data" / "traces_values"

# v1 corpus (legacy, retained for cross-version drift comparisons)
V1_FREEFLOW = V1_CORPUS / "data" / "traces_freeflow"
V1_VALUES = V1_CORPUS / "data" / "traces_values"
