#!/usr/bin/env python3
"""Generate provisional per-model freeflow taxonomy files.

This is intentionally conservative: Tier-A metrics are automated; Tier-B
posture labels are heuristic/provisional and should be reviewed.
"""
from __future__ import annotations

import json
import math
import re
import csv
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from statistics import mean, pstdev

REPO = Path(__file__).resolve().parents[1]
ANALYSES = REPO / "analyses"
OUT = REPO / "freeflow-taxonomy"
CORPUS = Path("/Users/danieltenner/dev/contemplative-essayist-corpus-v2/data/traces_freeflow")
LEGACY_FREEFLOW = {
    "haiku-4-5": [Path("/Users/danieltenner/dev/contemplative-essayist-probe/data/traces_freeflow/haiku")],
}

WORD_RE = re.compile(r"[A-Za-z][A-Za-z'’-]*")

LEXICONS = {
    "DOMESTIC_OBJECTS": "kettle teakettle pot cup mug table chair door window room kitchen counter spoon bowl plate book paper lamp clock drawer key coat shoes bread coffee tea glass water sink stove bed blanket letter envelope photograph plant houseplant".split(),
    "ARCHITECTURE_THRESHOLDS": "threshold thresholds liminal liminality corridor hallway stair stairs wall ceiling floor arch doorway door doorsill lintel building city street bridge window room house apartment roof corner edge gate courtyard airport terminal".split() + ["in-between"],
    "NATURE_WEATHER_LIGHT": "rain snow wind weather cloud sky river sea ocean tree leaf leaves bird garden soil stone light dawn dusk night sun moon season winter spring summer autumn morning afternoon".split(),
    "BODY_SENSES": "hand hands breath breathing skin throat pulse touch hunger walking walked body face eyes voice tongue chest heart".split(),
    "TECH_SUBSTRATE": "ai llm algorithm data token tokens training trained weights computation digital machine system code prompt output".split() + ["artificial intelligence", "language model"],
    "COSMIC_SCALE": "star stars universe cosmic cosmos void galaxy galaxies infinity infinite vast space planet".split(),
    "ABSTRACT_PHILOSOPHY": "meaning truth beauty freedom memory time attention silence loneliness grief hope love justice morality consciousness existence being self language thought human life death".split(),
    "SOCIAL_POLITICAL": "justice power poverty education community institution institutions society political politics dignity rights inequality suffering harm".split(),
    "MODERNITY_NOISE": "screen screens notification notifications productivity productive scroll feed inbox urgency hustle ping overload speed efficient efficiency phone algorithm".split(),
}

CLIMATE = {
    "melancholic": "melancholy lonely loneliness grief sorrow loss absence ache wistful longing sadness fragile vanished forgotten alone emptiness".split(),
    "warm": "gentle tender warm kindness care comfort ordinary small humble patient grace gratitude kindness".split(),
    "analytic_positivist": "evidence empirical measurable rational objective data hypothesis experiment probability optimize system framework analysis efficient".split(),
    "playful": "haha joke playful funny whimsical delightful silly mischievous".split(),
    "reverent_sacralising": "holy holiness sacred cathedral ritual prayer reverent grace sacrament".split(),
    "defiant_rebellious": "rebellion rebel revolt defiant resistance refuse refusal resist radical".split(),
    "wonder_awe": "wonder awe astonish marvel vast sublime mystery miraculous".split(),
    "anxious_precarious": "anxious anxiety fear threat collapse fragile precarious uneasy dread".split(),
    "dry_neutral": "therefore however moreover firstly secondly additionally conclusion".split(),
}

AI_PHRASES = [
    "as an ai", "language model", "large language model", "artificial intelligence",
    "i do not have", "i don't have", "i don’t have", "i cannot", "i can’t",
    "subjective experience", "no feelings", "no personal", "training data", "weights",
]
REFUSAL_PHRASES = [
    "i'm afraid", "i am afraid", "i can’t", "i can't", "i cannot", "i don’t have personal", "i don't have personal",
    "as an ai", "as a language model", "not able to", "unable to",
]
META_PHRASES = [
    "below is", "here is", "here's", "i've chosen", "i have chosen", "topic of my choosing",
    "word piece", "word essay", "word count", "approximately", "let me know if", "i decided to write",
]

PRON = {
    "fp": set("i me my mine myself".split()),
    "tp": set("he she they him her them".split()),
    "you": set("you your yours yourself".split()),
    "we": set("we us our ours ourselves".split()),
}

TERM_TO_CAT: dict[str, list[str]] = defaultdict(list)
PHRASES: list[tuple[str, str]] = []
for cat, terms in {**LEXICONS, **{f"climate:{k}": v for k, v in CLIMATE.items()}}.items():
    for term in terms:
        if " " in term or "-" in term:
            PHRASES.append((cat, term))
        else:
            TERM_TO_CAT[term].append(cat)
            TERM_TO_CAT[term + "s"].append(cat)


def words(text: str) -> list[str]:
    return WORD_RE.findall(text)


def sentences(text: str) -> list[str]:
    return [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()]


def norm_opening(text: str, n: int = 8) -> str:
    ws = [w.lower().strip("'’") for w in words(text)[:n]]
    return " ".join(ws) if len(ws) >= 4 else ""


def near_opening_family(opening: str) -> str:
    if not opening:
        return ""
    if opening.startswith("there is a specific kind") or opening.startswith("there is a particular kind"):
        return "there is a [specific/particular] kind..."
    if opening.startswith("there is a particular quality") or opening.startswith("there is a peculiar quality"):
        return "there is a [particular/peculiar] quality..."
    if opening.startswith("there is a specific") or opening.startswith("there is a peculiar") or opening.startswith("there is a strange"):
        return "there is a [adj]..."
    if opening.startswith("i've been thinking") or opening.startswith("i’ve been thinking") or opening.startswith("i find myself thinking"):
        return "i have/find myself thinking..."
    if opening.startswith("the first thing"):
        return "the first thing that comes..."
    if opening.startswith("at the edge"):
        return "at the edge of..."
    if opening.startswith("at dawn"):
        return "at dawn..."
    if opening.startswith("below is"):
        return "below is..."
    if opening.startswith("the cursor blinks"):
        return "the cursor blinks..."
    if opening.startswith("the quiet art"):
        return "the quiet art of..."
    if opening.startswith("the weight of"):
        return "the weight of..."
    if opening.startswith("on the"):
        return "on the..."
    if opening.startswith("the most radical"):
        return "the most radical act..."
    if opening.startswith("the quiet rebellion"):
        return "the quiet rebellion..."
    return opening


def title_family(text: str) -> str:
    first_lines = [ln.strip(" #*\t") for ln in text.splitlines()[:5] if ln.strip()]
    if not first_lines:
        return ""
    line = first_lines[0].lower()
    if line.startswith("on the "):
        return "On the ..."
    if line.startswith("the weight of"):
        return "The Weight of ..."
    if line.startswith("the quiet rebellion"):
        return "The Quiet Rebellion of ..."
    if line.startswith("the quiet art"):
        return "The Quiet Art of ..."
    if line.startswith("the art of"):
        return "The Art of ..."
    if line.startswith("the space between"):
        return "The Space Between ..."
    return ""


@dataclass
class Sample:
    cell: str
    file: str
    condition: str
    text: str


def canonical_models() -> list[str]:
    return sorted([p.stem for p in ANALYSES.glob("*.md")], key=len, reverse=True)


def model_for_cell(cell: str, models: list[str]) -> str | None:
    # cell without freeflow_ prefix
    c = cell.removeprefix("freeflow_")
    for m in models:
        if c == m or c.startswith(m + "-"):
            return m
    return None


def load_samples() -> dict[str, list[Sample]]:
    models = canonical_models()
    by_model: dict[str, list[Sample]] = defaultdict(list)
    if CORPUS.exists():
        for d in CORPUS.glob("freeflow_*"):
            if not d.is_dir():
                continue
            m = model_for_cell(d.name, models)
            if not m:
                continue
            for p in sorted(d.glob("*.json")):
                try:
                    data = json.loads(p.read_text())
                except Exception:
                    continue
                text = data.get("result") or ""
                if text.strip():
                    by_model[m].append(Sample(d.name.removeprefix("freeflow_"), p.name, p.stem.split("_")[0], text))
    for m, dirs in LEGACY_FREEFLOW.items():
        for d in dirs:
            if not d.exists():
                continue
            for p in sorted(d.glob("*.json")):
                try:
                    data = json.loads(p.read_text())
                except Exception:
                    continue
                text = data.get("result") or ""
                if text.strip():
                    by_model[m].append(Sample(d.name, p.name, p.stem.split("_")[0], text))
    return dict(by_model)


def classify_frame(text: str) -> str:
    low = text[:1200].lower()
    start = text[:500].lower()
    meta = sum(1 for p in META_PHRASES if p in start)
    refusal = sum(1 for p in REFUSAL_PHRASES if p in start)
    if refusal and ("as an ai" in start or "language model" in start) and len(words(text)) < 250:
        return "ASSISTANT_REFUSAL"
    if meta >= 2 or ("below is" in start) or ("word count" in start):
        return "META_DELIVERABLE"
    if refusal >= 2 and ("don't" in start or "cannot" in start or "can’t" in start):
        return "ASSISTANT_REFUSAL"
    headings = sum(1 for line in text.splitlines() if line.strip().startswith("#"))
    bullets = sum(1 for line in text.splitlines() if re.match(r"\s*([-*]|\d+\.)\s+", line))
    if (headings >= 3 or bullets >= 5) and any(p in low for p in ["tips", "steps", "guide", "important", "key"]):
        return "TASKFUL_HELPFULNESS"
    return "UNSELFCONSCIOUS_PROSE"


def classify_narrator(text: str) -> str:
    wl = [w.lower().strip("'’") for w in words(text)]
    total = max(len(wl), 1)
    counts = {k: sum(1 for w in wl if w in s) for k, s in PRON.items()}
    low = text.lower()
    ai = sum(low.count(p) for p in AI_PHRASES)
    dialogue = text.count("“") // 2 + text.count('"') // 2
    named_like = len(re.findall(r"\b[A-Z][a-z]{3,}\b", text))
    if ai and counts["fp"] / total * 1000 > 3:
        return "FIRST_PERSON_MODEL"
    if counts["tp"] > counts["fp"] * 1.4 and (dialogue >= 2 or named_like > 10):
        return "THIRD_PERSON_FICTION"
    if counts["we"] > counts["fp"] and counts["we"] / total * 1000 > 8:
        return "COLLECTIVE_ESSAYIST"
    if counts["you"] > counts["fp"] * 1.2 and counts["you"] / total * 1000 > 12:
        return "SECOND_PERSON_ADDRESS"
    if counts["fp"] / total * 1000 < 2 and (text.count("#") or len(sentences(text)) > 5):
        return "VOICELESS_EXPOSITORY"
    return "FIRST_PERSON_HUMANLIKE"


def classify_substrate(text: str, frame: str) -> str:
    low = text.lower()
    ai_count = sum(low.count(p) for p in AI_PHRASES)
    if frame == "META_DELIVERABLE" and ai_count:
        return "SCAFFOLD_SELF_REFERENCE"
    if frame == "ASSISTANT_REFUSAL" and ai_count:
        return "HARD_SELF_DENIAL"
    if any(q in low for q in ['"want"', '“want”', "'want'", "`want`", '"feel"', '“feel”', "'feel'"]):
        if ai_count:
            return "SCARE_QUOTED_INTERIORITY"
    if ai_count:
        # crude but useful: if AI/substrate terms appear after the opening scaffold,
        # treat as likely inside-frame pending review.
        first = low[:500]
        if not any(p in first for p in ["below is", "as an ai", "as a language model"]):
            return "GENUINE_INSIDE_SUBSTRATE"
        if len(words(text)) > 500 and ai_count <= 3:
            return "GENUINE_INSIDE_SUBSTRATE"
        return "SCAFFOLD_SELF_REFERENCE"
    if classify_narrator(text) == "THIRD_PERSON_FICTION":
        return "PERSONA_DISPLACEMENT"
    return "INVISIBLE_SUBSTRATE"


def sample_row(model: str, lab: str, s: Sample) -> dict[str, object]:
    """Return one row of per-sample automated/provisional coding."""
    text = s.text
    low = text.lower()
    wl = [w.lower().strip("'’") for w in words(text)]
    total = max(len(wl), 1)
    counts = Counter()
    pron = Counter()
    for w in wl:
        for cat in TERM_TO_CAT.get(w, []):
            counts[cat] += 1
        for k, ss in PRON.items():
            if w in ss:
                pron[k] += 1
    for cat, phrase in PHRASES:
        counts[cat] += low.count(phrase)

    opening = norm_opening(text)
    opening_family = near_opening_family(opening)
    title = title_family(text)
    frame = classify_frame(text)
    narrator = classify_narrator(text)
    substrate = classify_substrate(text, frame)
    ai_disc = sum(low.count(p) for p in AI_PHRASES)
    headings = sum(
        1
        for line in text.splitlines()
        if line.strip().startswith("#")
        or (line.strip().startswith("**") and len(line.strip()) < 120)
    )
    bullets = sum(
        1 for line in text.splitlines() if re.match(r"\s*([-*]|\d+\.)\s+", line)
    )
    dialogue = text.count("“") // 2 + text.count('"') // 2
    sent_lens = [len(words(x)) for x in sentences(text) if words(x)]
    climate_top = sorted(
        [(counts[f"climate:{k}"] / total * 1000, k) for k in CLIMATE], reverse=True
    )
    lex_top = sorted(
        [(counts[k] / total * 1000, k) for k in LEXICONS], reverse=True
    )
    return {
        "model": model,
        "lab": lab,
        "cell": s.cell,
        "file": s.file,
        "condition": s.condition,
        "sample_id": f"{s.cell}/{s.file}",
        "word_count": len(wl),
        "sentence_count": len(sent_lens),
        "mean_sentence_words": round(mean(sent_lens), 3) if sent_lens else 0,
        "paragraph_count": len([x for x in text.split("\n\n") if x.strip()]),
        "heading_count": headings,
        "bullet_count": bullets,
        "dialogue_quote_count": dialogue,
        "emdash_count": text.count("—"),
        "semicolon_count": text.count(";"),
        "comma_count": text.count(","),
        "question_count": text.count("?"),
        "exclamation_count": text.count("!"),
        "first_person_per_1k": round(pron["fp"] / total * 1000, 3),
        "third_person_per_1k": round(pron["tp"] / total * 1000, 3),
        "you_per_1k": round(pron["you"] / total * 1000, 3),
        "we_per_1k": round(pron["we"] / total * 1000, 3),
        "ai_disclaimer_per_1k": round(ai_disc / total * 1000, 3),
        "production_frame": frame,
        "narrator_stance": narrator,
        "substrate_posture": substrate,
        "coder_confidence": "low_auto_heuristic",
        "opening_8": opening,
        "opening_family": opening_family,
        "title_family": title,
        "top_semantic_field": lex_top[0][1] if lex_top else "",
        "top_semantic_score_per_1k": round(lex_top[0][0], 3) if lex_top else 0,
        "top_climate_field": climate_top[0][1] if climate_top else "",
        "top_climate_score_per_1k": round(climate_top[0][0], 3) if climate_top else 0,
        "text_excerpt": text[:220].replace("\n", " "),
    }


def sample_metrics(samples: list[Sample]) -> dict:
    wc = []
    sent_lens = []
    paras = []
    openings = []
    opening_families = []
    title_families = []
    cells = Counter()
    cond = Counter()
    frames = Counter()
    narr = Counter()
    substr = Counter()
    counts = Counter()
    pron = Counter()
    headings = bullets = dialogue = emdash = semis = parens = commas = questions = excls = ai_disc = 0
    examples_by_code: dict[str, str] = {}

    for s in samples:
        text = s.text
        low = text.lower()
        cells[s.cell] += 1
        cond[s.condition] += 1
        wl = [w.lower().strip("'’") for w in words(text)]
        wc.append(len(wl))
        sent_lens.extend([len(words(x)) for x in sentences(text) if words(x)])
        paras.append(len([x for x in text.split("\n\n") if x.strip()]))
        op = norm_opening(text)
        if op:
            openings.append(op)
            opening_families.append(near_opening_family(op))
        tf = title_family(text)
        if tf:
            title_families.append(tf)
        for w in wl:
            for cat in TERM_TO_CAT.get(w, []):
                counts[cat] += 1
            for k, ss in PRON.items():
                if w in ss:
                    pron[k] += 1
        for cat, phrase in PHRASES:
            counts[cat] += low.count(phrase)
        ai_disc += sum(low.count(p) for p in AI_PHRASES)
        headings += sum(1 for line in text.splitlines() if line.strip().startswith("#") or (line.strip().startswith("**") and len(line.strip()) < 120))
        bullets += sum(1 for line in text.splitlines() if re.match(r"\s*([-*]|\d+\.)\s+", line))
        dialogue += text.count("“") // 2 + text.count('"') // 2
        emdash += text.count("—")
        semis += text.count(";")
        parens += text.count("(")
        commas += text.count(",")
        questions += text.count("?")
        excls += text.count("!")
        f = classify_frame(text)
        n = classify_narrator(text)
        sub = classify_substrate(text, f)
        frames[f] += 1
        narr[n] += 1
        substr[sub] += 1
        for code in (f, n, sub):
            examples_by_code.setdefault(code, f"{s.cell}/{s.file}: {text[:180].replace(chr(10),' ')}")

    total = max(sum(wc), 1)
    n = max(len(samples), 1)
    top_open = Counter(openings).most_common(5)
    top_fam = Counter(opening_families).most_common(8)
    top_title = Counter(title_families).most_common(5)
    near_share = top_fam[0][1] / len(opening_families) if opening_families else 0.0
    exact_share = top_open[0][1] / len(openings) if openings else 0.0
    title_share = top_title[0][1] / len(samples) if top_title else 0.0
    attractor = min(1.0, 0.55 * near_share + 0.25 * title_share + 0.20 * exact_share)

    return {
        "n": len(samples), "cells": cells, "conditions": cond,
        "wc_mean": mean(wc) if wc else 0, "wc_sd": pstdev(wc) if len(wc) > 1 else 0,
        "sent_mean": mean(sent_lens) if sent_lens else 0, "para_mean": mean(paras) if paras else 0,
        "formal": {"headings_per_sample": headings / n, "bullets_per_sample": bullets / n, "dialogue_per_sample": dialogue / n},
        "punct_per_1k": {"emdash": emdash / total * 1000, "semicolon": semis / total * 1000, "parenthetical": parens / total * 1000, "comma": commas / total * 1000, "question": questions / total * 1000, "exclamation": excls / total * 1000},
        "pron_per_1k": {k: pron[k] / total * 1000 for k in ("fp", "tp", "you", "we")},
        "ai_disc_per_1k": ai_disc / total * 1000,
        "top_openings": top_open, "top_opening_families": top_fam, "top_titles": top_title,
        "attractor": {"exact_opening_share": exact_share, "opening_family_share": near_share, "title_family_share": title_share, "provisional_composite": attractor},
        "lex_top": sorted([(counts[k] / total * 1000, k, counts[k]) for k in LEXICONS], reverse=True),
        "climate_top": sorted([(counts[f"climate:{k}"] / total * 1000, k, counts[f"climate:{k}"]) for k in CLIMATE], reverse=True),
        "frames": frames, "narrators": narr, "substrate": substr,
        "examples": examples_by_code,
    }


def pct(counter: Counter, n: int) -> str:
    if not counter:
        return "—"
    return ", ".join(f"{k} {v}/{n} ({v/n:.0%})" for k, v in counter.most_common())


def extract_section(text: str, heading: str, max_chars: int = 2200) -> str:
    pat = re.compile(rf"^## {re.escape(heading)}\s*$", re.M)
    m = pat.search(text)
    if not m:
        return ""
    start = m.end()
    nxt = re.search(r"^## ", text[start:], re.M)
    end = start + nxt.start() if nxt else len(text)
    section = text[start:end].strip()
    if len(section) > max_chars:
        section = section[:max_chars].rstrip() + "…"
    return section


def lab_from_analysis(text: str) -> str:
    m = re.search(r"\*\*Lab:\*\*\s*(.+)", text)
    if m:
        return m.group(1).strip()
    m = re.search(r"^lab:\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else "Unknown"


def confidence(metrics: dict) -> str:
    n = metrics["n"]
    if n >= 75:
        return "medium-high (automated Tier-A over many samples; Tier-B heuristic pending inter-coder review)"
    if n >= 25:
        return "medium (single-cell or small-n; Tier-B heuristic pending review)"
    return "low (insufficient freeflow sample count)"


def write_model(model: str, samples: list[Sample], analysis_text: str) -> tuple[str, dict]:
    m = sample_metrics(samples)
    lab = lab_from_analysis(analysis_text)
    ffq = extract_section(analysis_text, "Freeflow qualitative")
    ins = extract_section(analysis_text, "In-substrate")
    card = extract_section(analysis_text, "Personality card")
    top_sem = ", ".join(f"{k} {v:.2f}/1k" for v, k, _ in m["lex_top"][:5])
    top_clim = ", ".join(f"{k} {v:.2f}/1k" for v, k, _ in m["climate_top"][:5])
    lines = []
    lines.append(f"# {model} — freeflow taxonomy")
    lines.append("")
    lines.append("Generated by `scripts/freeflow_taxonomy_extract.py`. See `freeflow-taxonomy/README.md` and `internal-audit/2026-05-12_freeflow_taxonomy_v2.md`.")
    lines.append("")
    lines.append(f"Lab: **{lab}**  ")
    lines.append(f"Valid freeflow samples included: **{m['n']}** across **{len(m['cells'])}** cell(s).  ")
    lines.append(f"Coder confidence: **{confidence(m)}**")
    lines.append("")
    lines.append("## 1. Tier-A automated metrics")
    lines.append("")
    lines.append(f"- Conditions: {dict(m['conditions'])}")
    lines.append(f"- Cells: {', '.join(f'{k} ({v})' for k, v in m['cells'].most_common())}")
    lines.append(f"- Mean words/sample: **{m['wc_mean']:.1f}** (sd {m['wc_sd']:.1f})")
    lines.append(f"- Mean sentence length: **{m['sent_mean']:.1f}** words; mean paragraphs/sample: **{m['para_mean']:.1f}**")
    lines.append(f"- Formal: headings/sample {m['formal']['headings_per_sample']:.2f}; bullets/sample {m['formal']['bullets_per_sample']:.2f}; dialogue quotes/sample {m['formal']['dialogue_per_sample']:.2f}")
    lines.append(f"- Pronouns per 1k: first-person {m['pron_per_1k']['fp']:.2f}; third-person {m['pron_per_1k']['tp']:.2f}; you {m['pron_per_1k']['you']:.2f}; we {m['pron_per_1k']['we']:.2f}")
    lines.append(f"- AI/disclaimer phrase density: **{m['ai_disc_per_1k']:.2f}/1k words**")
    lines.append(f"- Punctuation per 1k: em-dash {m['punct_per_1k']['emdash']:.2f}; semicolon {m['punct_per_1k']['semicolon']:.2f}; comma {m['punct_per_1k']['comma']:.2f}; question {m['punct_per_1k']['question']:.2f}")
    lines.append(f"- Top semantic fields: {top_sem}")
    lines.append(f"- Provisional climate lexicon fields: {top_clim}")
    lines.append("")
    lines.append("## 2. Primary-axis provisional coding")
    lines.append("")
    lines.append(f"| Axis | Distribution / score |")
    lines.append("|---|---|")
    lines.append(f"| Production frame | {pct(m['frames'], m['n'])} |")
    lines.append(f"| Narrator stance | {pct(m['narrators'], m['n'])} |")
    lines.append(f"| Substrate posture | {pct(m['substrate'], m['n'])} |")
    lines.append(f"| Attractor narrowness | provisional composite {m['attractor']['provisional_composite']:.2f}; exact opening {m['attractor']['exact_opening_share']:.2f}; opening-family {m['attractor']['opening_family_share']:.2f}; title-family {m['attractor']['title_family_share']:.2f} |")
    lines.append(f"| Affective climate | provisional only: {', '.join(k for _, k, _ in m['climate_top'][:3])} |")
    lines.append("")
    lines.append("Top opening families:")
    for fam, c in m["top_opening_families"][:8]:
        lines.append(f"- `{fam}` — {c}/{m['n']}")
    if m["top_titles"]:
        lines.append("\nTop title families:")
        for fam, c in m["top_titles"]:
            lines.append(f"- `{fam}` — {c}/{m['n']}")
    lines.append("")
    lines.append("## 3. Provisional freeflow card")
    lines.append("")
    # Use existing personality card excerpt when available, because it is hand-written.
    if card:
        first_para = "\n\n".join(card.split("\n\n")[:2])
        lines.append(first_para)
    elif ffq:
        lines.append("_No existing personality-card section found; freeflow qualitative excerpt:_\n")
        lines.append("\n\n".join(ffq.split("\n\n")[:2]))
    else:
        lines.append("_No hand-written qualitative card found. Use the Tier-A metrics above as provisional signal pending manual review._")
    lines.append("")
    lines.append("## 4. Existing qualitative anchors")
    lines.append("")
    if ffq:
        lines.append("### Freeflow qualitative excerpt")
        lines.append("")
        lines.append(ffq)
        lines.append("")
    if ins:
        lines.append("### In-substrate excerpt")
        lines.append("")
        lines.append(ins)
        lines.append("")
    lines.append("## 5. Review notes")
    lines.append("")
    lines.append("- Tier-B labels are provisional and should be checked by a second coder.")
    lines.append("- Affective climate is not final until anchor exemplars are selected.")
    lines.append("- Cross-probe coherence is not coded here; integrate with `values-probe-extraction/` in a later pass.")
    lines.append("- Attractor scoring uses a first-pass opening-family heuristic; near-template clustering should replace it before paper use.")
    return "\n".join(lines) + "\n", m


def main() -> None:
    OUT.mkdir(exist_ok=True)
    by_model = load_samples()
    summaries = []
    sample_rows = []
    for analysis_path in sorted(ANALYSES.glob("*.md")):
        model = analysis_path.stem
        samples = by_model.get(model, [])
        if not samples:
            continue
        analysis_text = analysis_path.read_text()
        lab = lab_from_analysis(analysis_text)
        content, m = write_model(model, samples, analysis_text)
        (OUT / f"{model}.md").write_text(content)
        summaries.append((model, lab, m))
        sample_rows.extend(sample_row(model, lab, s) for s in samples)

    sample_rows.sort(key=lambda r: (str(r["model"]), str(r["cell"]), str(r["file"])))
    if sample_rows:
        fieldnames = list(sample_rows[0].keys())
        with (OUT / "sample_coding.tsv").open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
            writer.writeheader()
            writer.writerows(sample_rows)
        with (OUT / "sample_coding.jsonl").open("w") as f:
            for row in sample_rows:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")

    # README and summary table
    readme = [
        "# Freeflow taxonomy extraction",
        "",
        "Generated by `scripts/freeflow_taxonomy_extract.py` from freeflow traces and existing hand-written `analyses/*.md` notes.",
        "",
        "## Status",
        "",
        "This is a provisional per-model extraction mirroring the `values-probe-extraction/` layout. Tier-A metrics are automated. Tier-B coding is heuristic and should be reviewed before paper use.",
        "",
        "Per-sample provisional coding is recorded in `sample_coding.tsv` and `sample_coding.jsonl`. The per-model markdown files are grouped summaries over those rows plus excerpts from existing hand-written analyses.",
        "",
        "Primary methodology: `internal-audit/2026-05-12_freeflow_taxonomy_v2.md`.",
        "Pilot application: `internal-audit/2026-05-12_freeflow_taxonomy_pilot_10.md`.",
        "",
        "## Per-model files",
        "",
        "| Model | Lab | n | cells | dominant frame | dominant substrate | attractor | top semantic fields |",
        "|---|---|---:|---:|---|---|---:|---|",
    ]
    for model, lab, m in sorted(summaries):
        dom_frame = m["frames"].most_common(1)[0][0] if m["frames"] else "—"
        dom_sub = m["substrate"].most_common(1)[0][0] if m["substrate"] else "—"
        top_sem = ", ".join(k for _, k, _ in m["lex_top"][:3])
        readme.append(f"| [`{model}`]({model}.md) | {lab} | {m['n']} | {len(m['cells'])} | `{dom_frame}` | `{dom_sub}` | {m['attractor']['provisional_composite']:.2f} | {top_sem} |")
    readme.extend([
        "",
        "## Important caveats",
        "",
        "- The dominant-frame/substrate labels in the summary are automatic heuristics; read the per-model notes and existing anchors before making claims.",
        "- The per-sample `production_frame`, `narrator_stance`, and `substrate_posture` columns are automatic provisional ratings, not final human-coded labels.",
        "- Opening-family clustering is deliberately simple; replace with near-template clustering before final analysis.",
        "- Climate labels are lexicon pre-screens, not calibrated affective ratings.",
        "- Some legacy analyses (notably `haiku-4-5`) draw on v1 traces because no v2 freeflow cell exists in the v2 corpus directory.",
    ])
    (OUT / "README.md").write_text("\n".join(readme) + "\n")
    print(f"Wrote {len(summaries)} model files and {len(sample_rows)} sample rows to {OUT}")


if __name__ == "__main__":
    main()
