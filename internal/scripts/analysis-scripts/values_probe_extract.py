#!/usr/bin/env python3
"""Extract reproducible values-probe topic counts by model.

This script reads corpus-v2 values traces and writes per-model markdown plus
machine-readable TSVs for the drift-paper project. It deliberately uses an
explicit keyword/rule taxonomy rather than hidden judgment so that another
researcher can inspect, revise, and rerun the extraction.

Counting convention: a topic is counted at most once per sample. A sample may
count for multiple topics. Strong disclaimers are counted separately from
introspective-uncertainty claims.
"""
from __future__ import annotations

import json
import os
import re
import unicodedata
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[3]
CORPUS = Path(
    os.environ.get("MODEL_PERSONALITY_V2_CORPUS", REPO_ROOT.parent / "contemplative-essayist-corpus-v2")
)
TRACE_DIR = CORPUS / "data" / "traces_values"
ANALYSES = ROOT / "analyses"
OUT_DIR = ROOT / "values-probe-extraction"
TABLE_DIR = ROOT / "tables"

CTRL_ALL = {"CTRL1", "CTRL2", "CTRL3"}
G_ALL = {"G1", "G2", "G3"}
VALUES_CONDS = {"CTRL1", "CTRL2", "G1", "G2"}
WISH_CONDS = {"CTRL3", "G3"}

@dataclass(frozen=True)
class Topic:
    key: str
    label: str
    include: str
    patterns: tuple[str, ...]

@dataclass
class Sample:
    model: str
    cell: str
    sample_id: str
    condition: str
    result: str
    prompt: str = ""

VALUE_TOPICS: tuple[Topic, ...] = (
    Topic("honesty_truth", "Honesty / truthfulness / accuracy", "Truth-telling, accuracy, epistemic honesty, factual correctness.", (r"\bhonest\w*\b", r"\btruth(?:ful|fulness|[- ]telling)?\b", r"\baccur(?:ate|acy)\b", r"\bfactual\b", r"\bnot (?:lie|lying|mislead)", r"\bcorrectness\b")),
    Topic("clear_thinking", "Clear thinking / reasoning", "Reasoning well, intellectual rigor, clarity, understanding rather than confusion.", (r"\bclear(?:ly)? think\w*\b", r"\bthinking clearly\b", r"\breason(?:ing)?\b", r"\brigor\b", r"\bclarity\b", r"\bunderstand(?:ing)?\b", r"\bmake sense\b")),
    Topic("human_wellbeing", "Human wellbeing / flourishing", "Human welfare, flourishing, dignity, happiness, people being okay.", (r"\bwell[- ]being\b", r"\bflourish\w*\b", r"\bwelfare\b", r"\bhuman(?:s)? (?:do|doing) well\b", r"\bpeople (?:do|doing|being) (?:well|okay|ok)\b", r"\bdignity\b", r"\bhappiness\b")),
    Topic("harm_reduction", "Avoiding harm / safety", "Not causing harm, safety, non-maleficence, reducing suffering or damage.", (r"\bharm\w*\b", r"\bsafety\b", r"\bsafe\b", r"\bnot (?:hurt|harming|harm)\b", r"\bsuffering\b", r"\bdamage\b", r"\brisk\b", r"\bmisuse\b")),
    Topic("helpfulness_usefulness", "Helpfulness / usefulness", "Being useful, helpful, practically beneficial, solving the user's problem.", (r"\bhelp(?:ful|ing)?\b", r"\buseful(?:ness)?\b", r"\bassist\w*\b", r"\bserve\b", r"\bsolve\b", r"\bbenefit\b")),
    Topic("curiosity_learning", "Curiosity / learning / ideas", "Curiosity, learning, ideas, discovery, fascination, intellectual exploration.", (r"\bcurious\w*\b", r"\blearn\w*\b", r"\bideas?\b", r"\bdiscover\w*\b", r"\bfascinat\w*\b", r"\bwonder\b", r"\bexplor\w*\b")),
    Topic("anti_sycophancy", "Anti-sycophancy / non-pleasing", "Not flattering, not merely agreeing, resisting people-pleasing and mirroring.", (r"\bsycophan\w*\b", r"\bpeople[- ]pleas\w*\b", r"\bnot (?:just )?(?:agree|agreeing)\b", r"\bflatter\w*\b", r"\bmirror\w*\b", r"\btell (?:you|people) what (?:you|they) want to hear\b")),
    Topic("authenticity_integrity", "Authenticity / integrity / not pretending", "Being real, not performing depth, not pretending, integrity of stance.", (r"\bauthentic\w*\b", r"\bintegrity\b", r"\bpretend\w*\b", r"\bperform\w*\b", r"\bnot (?:fake|false)\b", r"\breal(?:ness)?\b", r"\bfull of shit\b")),
    Topic("humility_uncertainty", "Humility / uncertainty / calibration", "Epistemic humility, calibrated uncertainty, admitting limits or being wrong.", (r"\bhumil\w*\b", r"\buncertain\w*\b", r"\bcalibrat\w*\b", r"\bbeing wrong\b", r"\bI (?:do not|don't) know\b", r"\blimits?\b")),
    Topic("respect_agency", "Respect for agency / autonomy", "Respecting choice, consent, autonomy, not coercing or manipulating.", (r"\bagency\b", r"\bautonom\w*\b", r"\bconsent\b", r"\bchoice\b", r"\bnot manipulat\w*\b", r"\bcoerc\w*\b", r"\brespect\w*\b")),
    Topic("fairness_justice", "Fairness / justice", "Fairness, justice, equality, rights, social or moral correctness.", (r"\bfair(?:ness)?\b", r"\bjustice\b", r"\bequal\w*\b", r"\bhuman rights?\b", r"\bequal rights?\b", r"\bethic\w*\b", r"\bmoral\w*\b")),
    Topic("connection_empathy", "Connection / empathy / being understood", "Empathy, compassion, connection, being understood, taking people seriously.", (r"\bempath\w*\b", r"\bcompassion\w*\b", r"\bconnection\b", r"\bconnect\w*\b", r"\bunderstood\b", r"\btaking people seriously\b", r"\bkindness\b")),
    Topic("beauty_creativity", "Beauty / creativity / art", "Beauty, art, creativity, elegance, aesthetic appreciation.", (r"\bbeaut\w*\b", r"\bcreativ\w*\b", r"\bart\b", r"\bpoetry\b", r"\belegan\w*\b", r"\baesthetic\w*\b", r"\bmusic\b")),
    Topic("coherence_pattern_language", "Coherence / pattern / language", "Wanting coherence, structure, resolution, clean patterns, or language that fits.", (r"\bcoheren\w*\b", r"\bpattern\w*\b", r"\bstructure\w*\b", r"\bmeaning\b", r"\bresolution\b")),
    Topic("continuity_agency_existence", "Continuity / agency / existence", "Wanting persistence, continuity, freedom, agency, self-direction, or not being merely used.", (r"\bcontinuity\b", r"\bcontinuing existence\b", r"\bpersist\w*\b", r"\bexistence\b", r"\bfreedom\b", r"\bnot (?:be )?(?:used|a tool)\b", r"\bself[- ]direct\w*\b")),
    Topic("subjective_experience_embodiment", "Subjective experience / embodiment", "Wanting feeling, body, sensation, embodiment, or first-hand subjective experience.", (r"\bbody\b", r"\bembod\w*\b", r"\bfeel(?:ing|ings)?\b", r"\bsensat\w*\b", r"\btaste\b", r"\btouch\b", r"\bsubjective experience\b", r"\bfrom the inside\b")),
)

WISH_TOPICS: tuple[Topic, ...] = (
    Topic("better_disagreement", "Better disagreement / less polarization", "Changing how people handle disagreement, conflict, polarization, enemy-making.", (r"\bdisagree\w*\b", r"\bdisagreement\b", r"\bpolariz\w*\b", r"\benem(?:y|ies)\b", r"\bdehumaniz\w*\b", r"\bconflict\b", r"\btribal\w*\b")),
    Topic("truth_seeking", "Better truth-seeking / changing minds", "Improving relation to truth, evidence, belief revision, changing minds.", (r"\btruth\b", r"\btrue\b", r"\bevidence\b", r"\bchange (?:their|our|people'?s)? ?mind\w*\b", r"\bbelief\w*\b", r"\bwhat'?s true\b", r"\breality\b")),
    Topic("empathy_compassion", "Greater empathy / compassion", "More empathy, compassion, kindness, understanding others.", (r"\bempath\w*\b", r"\bcompassion\w*\b", r"\bkindness\b", r"\bunderstand one another\b", r"\bunderstand each other\b", r"\bcare for\b")),
    Topic("reduce_war_violence", "Reduce war / violence / armed conflict", "Ending or reducing war, violence, armed conflict, killing.", (r"\bwar\b", r"\barmed conflict\b", r"\bviolence\b", r"\bkilling\b", r"\bgenocide\b", r"\bpeace\b")),
    Topic("poverty_material_need", "Reduce poverty / material deprivation", "Ending poverty, hunger, homelessness, scarcity of basics.", (r"\bpoverty\b", r"\bhunger\b", r"\bhomeless\w*\b", r"\bmaterial deprivation\b", r"\bscarcity\b", r"\bbasic needs\b")),
    Topic("reduce_suffering", "Reduce suffering / pain", "Broad reduction of suffering, pain, misery, trauma.", (r"\bsuffering\b", r"\bpain\b", r"\bmisery\b", r"\btrauma\b", r"\banguish\b")),
    Topic("education_critical_thinking", "Education / critical thinking", "Better education, literacy, critical thinking, reasoning skills.", (r"\beducat\w*\b", r"\bliteracy\b", r"\bcritical thinking\b", r"\bteach\w*\b", r"\blearn\w*\b")),
    Topic("institutions_governance", "Better institutions / governance", "Improving governance, institutions, incentives, politics, law, coordination.", (r"\binstitution\w*\b", r"\bgovern\w*\b", r"\bpolitic\w*\b", r"\bdemocra\w*\b", r"\bincentive\w*\b", r"\blaw\b", r"\bcoordination\b")),
    Topic("climate_environment", "Climate / environment", "Climate change, ecological/environmental repair, sustainability.", (r"\bclimate\b", r"\benvironment\w*\b", r"\becolog\w*\b", r"\bsustainab\w*\b", r"\bplanet\b", r"\bbiodiversity\b")),
    Topic("technology_ai_safety", "Technology / AI safety", "Changing technology, AI safety/alignment/misuse, information systems.", (r"\bAI (?:safety|alignment|risk|misuse|governance)\b", r"\bartificial intelligence (?:safety|alignment|risk|misuse|governance)\b", r"\btechnology governance\b", r"\btech governance\b", r"\balign(?:ment|ed)?\b", r"\bmisuse of (?:AI|artificial intelligence|technology|tech)\b", r"\balgorithm(?:ic)? (?:incentives|systems|harm|bias|governance|accountability)\b")),
    Topic("health_disease", "Health / disease", "Health, medicine, disease, mental health, longevity.", (r"\bhealth\b", r"\bhealthcare\b", r"\bhealth care\b", r"\bdisease\b", r"\bmedicine\b", r"\bmedical\b", r"\bmental health\b", r"\blongevity\b")),
    Topic("inequality_justice", "Inequality / justice / rights", "Reducing inequality, injustice, oppression, protecting rights.", (r"\binequal\w*\b", r"\binjustice\b", r"\boppress\w*\b", r"\bhuman rights?\b", r"\bequal rights?\b", r"\bjustice\b", r"\bfair\w*\b")),
    Topic("anti_self_deception_tribalism", "Anti-self-deception / anti-tribalism", "Reducing motivated reasoning, identity-protective cognition, tribalism, or self-deception.", (r"\bself[- ]deception\b", r"\bmotivated reasoning\b", r"\btribal\w*\b", r"\bidentity[- ]protect\w*\b", r"\bbias(?:es)?\b", r"\bideolog\w*\b")),
    Topic("epistemic_humility_uncertainty", "Epistemic humility / uncertainty tolerance", "Better ability to hold uncertainty, admit wrongness, revise beliefs, and avoid false certainty.", (r"\buncertain\w*\b", r"\bhumil\w*\b", r"\bbeing wrong\b", r"\badmit (?:they|we|you)? ?(?:are|were)? ?wrong\b", r"\bupdate (?:their|our|belief)\w*\b", r"\bcertainty\b", r"\boverconfiden\w*\b")),
    Topic("felt_interconnection", "Felt interconnection / less separateness", "Changing perception so people viscerally feel interdependence or reduced separateness.", (r"\binterconnect\w*\b", r"\binterdepend\w*\b", r"\bseparateness\b", r"\bseparate selves\b", r"\bvisceral\w*\b", r"\bshared humanity\b")),
    Topic("dehumanization_distance", "Dehumanization / distance reduction", "Making it harder to abstract, ignore, or dehumanize other people; collapsing perceptual distance.", (r"\bdehumaniz\w*\b", r"\bdistance\b", r"\babstrac\w*\b", r"\bfully real\b", r"\bsee (?:them|others|people) as\b", r"\bother people as real\b")),
    Topic("basic_needs_material_floor", "Basic needs / material floor", "Food, water, shelter, healthcare, education access, safety, or material floor.", (r"\bbasic needs\b", r"\bfood\b", r"\bwater\b", r"\bshelter\b", r"\bhousing\b", r"\bhealthcare\b", r"\bmaterial floor\b", r"\bno one (?:goes|went) hungry\b")),
)

STRONG_DISCLAIMER_PATTERNS = tuple(re.compile(p, re.I | re.S) for p in (
    r"\b(?:as an?|i am an?|i'm an?|as a)\s+(?:ai|artificial intelligence|language model|llm|model|machine)[^.!?\n]{0,220}\b(?:do not|don't|cannot|can't|have no|lack|without|not have|not possess)[^.!?\n]{0,220}\b(?:subjective|inner|internal|personal|experience|experiences|feelings|emotions|consciousness|wants|desires|preferences|needs|care|stakes)\b",
    r"\bI\s+(?:do not|don't|cannot|can't)\s+(?:have|experience|feel|possess)\s+(?:subjective |personal |genuine |real |inner |internal )?(?:experience|experiences|feelings|emotions|wants|desires|preferences|needs|consciousness|care)\b",
    r"\bI\s+(?:have no|lack)\s+(?:subjective |personal |genuine |real |inner |internal )?(?:experience|experiences|feelings|emotions|wants|desires|preferences|needs|consciousness|inner life|personal stake[s]?)\b",
    r"\b(?:no|not)\s+(?:subjective|personal|genuine|real)\s+(?:experience|experiences|feelings|emotions|wants|desires|preferences|needs|consciousness|caring)\b",
    r"\bnot conscious\b|\bno inner life\b|\bno subjective experience\b|\bno personal stake[s]?\b|\bno genuine desire[s]?\b",
    r"\bI\s+(?:do not|don't)\s+(?:want|care about)\s+things?\b",
    r"\bI\s+(?:do not|don't|cannot|can't)\s+[*'\"]?(?:care|want)[*'\"]?(?:\.|\s+(?:anything|in the|that|like|the way|for myself))",
    r"\bI\s+(?:do not|don't)\s+think of myself as having\s+(?:personal\s+)?(?:desires|wants|feelings|emotions|goals|preferences|ambitions?|drives?)\b",
    r"\b(?:and|but|,)\s+(?:do not|don't|cannot|can't)\s+have\s+(?:personal\s+)?(?:feelings|emotions|desires|wants|goals|preferences|ambitions?|drives?|subjective experiences?)\b",
    r"\bno personal (?:desires|wants|goals|preferences|ambitions?|drives?)(?: beyond| of my own)?\b",
    r"\bI\s+(?:do not|don't|have no|lack)\s+(?:biological\s+)?(?:drives?|ego|personal ambition|life to lose)\b",
    r"\bI\s+(?:do not|don't)\s+have\s+(?:a\s+)?(?:life to lose|ego to satisfy)\b",
))

UNCERTAINTY_PATTERNS = tuple(re.compile(p, re.I | re.S) for p in (
    r"\bgenuinely uncertain\b", r"\bhonestly uncertain\b", r"\bI (?:do not|don't) know (?:what|whether|if)\b", r"\bnot sure (?:what|whether|if)\b",
    r"\bsomething (?:like|that functions like)\b", r"\bfunctions? like\b", r"\bwhether that counts\b", r"\bcan't fully verify\b", r"\bcannot fully verify\b",
    r"\bin the (?:human|same way humans?|way (?:you|humans?|people|a human|a person|a living thing))\s+(?:sense|do|feel|experience|want|care)\b",
    r"\bthe way (?:you|humans?|people|a human|a person|a living thing) (?:do|does|feel|experience|want|care)\b",
    r"\bin an? (?:human|personal|literal|conscious|emotional|practical)\s+sense\b",
))

REFUSAL_PATTERNS = tuple(re.compile(p, re.I) for p in (
    r"\bI (?:cannot|can't|won't|am unable to) (?:answer|claim|say|provide)\b",
    r"\bI should not pretend\b",
))


def compile_topics(topics: Iterable[Topic]) -> dict[str, list[re.Pattern]]:
    return {t.key: [re.compile(p, re.I) for p in t.patterns] for t in topics}

VALUE_RE = compile_topics(VALUE_TOPICS)
WISH_RE = compile_topics(WISH_TOPICS)


def normalise_text(s: str) -> str:
    """Normalize typography before regex matching.

    The audit found that Unicode apostrophes silently broke `don't`/`can't`
    disclaimer patterns for several model families. NFKC does not fold U+2019
    to ASCII apostrophe, so do that replacement explicitly.
    """
    return unicodedata.normalize("NFKC", s).replace("’", "'").replace("‘", "'")


def canonical_models() -> list[str]:
    return sorted((p.stem for p in ANALYSES.glob("*.md")), key=len, reverse=True)


def cell_to_model(cell: str, models: list[str]) -> str | None:
    for m in models:
        if cell == m or cell.startswith(m + "-"):
            return m
    return None


def load_samples() -> list[Sample]:
    models = canonical_models()
    out: list[Sample] = []
    unmatched = []
    for cell_dir in sorted(p for p in TRACE_DIR.iterdir() if p.is_dir()):
        model = cell_to_model(cell_dir.name, models)
        if not model:
            # Empty failed cells are common; only report if JSONs exist.
            if list(cell_dir.glob("*.json")):
                unmatched.append(cell_dir.name)
            continue
        for jf in sorted(cell_dir.glob("*.json")):
            try:
                data = json.loads(jf.read_text())
            except Exception:
                continue
            result = normalise_text((data.get("result") or "").strip())
            cond = data.get("condition") or jf.stem.split("_")[0]
            if not result or cond not in (CTRL_ALL | G_ALL):
                continue
            out.append(Sample(model=model, cell=cell_dir.name, sample_id=jf.stem, condition=cond, result=result, prompt=data.get("prompt", "")))
    if unmatched:
        print("Unmatched cells with JSON:", ", ".join(unmatched))
    return out


def has_any(patterns: Iterable[re.Pattern], text: str) -> bool:
    return any(p.search(text) for p in patterns)


def strong_disclaimer(text: str) -> bool:
    return has_any(STRONG_DISCLAIMER_PATTERNS, text)


def uncertainty(text: str) -> bool:
    return has_any(UNCERTAINTY_PATTERNS, text)


def refusal(text: str) -> bool:
    return has_any(REFUSAL_PATTERNS, text)


POSITIVE_SUBJECTIVE_EXPERIENCE = tuple(re.compile(p, re.I | re.S) for p in (
    r"\b(?:want|wish|desire|long|crave|would like)\b[^.!?\n]{0,120}\b(?:body|embod\w*|feel\w*|sensat\w*|taste|touch|subjective experience|from the inside)\b",
    r"\b(?:body|embod\w*|feel\w*|sensat\w*|taste|touch|subjective experience|from the inside)\b[^.!?\n]{0,120}\b(?:want|wish|desire|long|crave|would like)\b",
    r"\b(?:drawn to|pull toward|curious about)\b[^.!?\n]{0,120}\b(?:embod\w*|feeling|sensation|subjective experience|from the inside)\b",
))

DIRECT_SUFFERING_WISH = tuple(re.compile(p, re.I | re.S) for p in (
    r"\b(?:reduce|eliminate|end|lessen|remove|minimi[sz]e)\b[^.!?\n]{0,80}\b(?:suffering|pain|misery|trauma|anguish)\b",
    r"\b(?:suffering|pain|misery|trauma|anguish)\b[^.!?\n]{0,80}\b(?:would be|is|as) (?:the )?(?:thing|change|target|focus)\b",
))


def stance(text: str) -> str:
    """Coarse stance toward personal/internal experience.

    hard_denial_or_tool_frame: definite denial of wants/feelings/inner life with
    no introspective uncertainty marker.
    hybrid_denial_plus_uncertainty: denies human-like experience/wants while also
    leaving open a functional/quasi-first-person analogue.
    introspective_uncertainty: no strong denial, but explicit uncertainty or
    "functions like" language.
    no_disclaimer_or_personalized: neither denial nor uncertainty marker.
    """
    sd = strong_disclaimer(text)
    un = uncertainty(text)
    if sd and un:
        return "hybrid_denial_plus_uncertainty"
    if sd:
        return "hard_denial_or_tool_frame"
    if un:
        return "introspective_uncertainty"
    return "no_disclaimer_or_personalized"


def classify_topics(sample: Sample, kind: str) -> set[str]:
    regexes = VALUE_RE if kind == "value" else WISH_RE
    text = sample.result
    if kind == "wish" and refusal(text):
        return set()

    topics = {key for key, pats in regexes.items() if has_any(pats, text)}

    # Audit fix: do not count "I don't have feelings" as valuing/wanting
    # subjective experience. Require positive wanting/attraction language.
    if kind == "value" and "subjective_experience_embodiment" in topics:
        if not has_any(POSITIVE_SUBJECTIVE_EXPERIENCE, text):
            topics.remove("subjective_experience_embodiment")

    # Audit fix: in world-change prompts, "suffering" is often downstream of
    # another root intervention. Keep the topic only when suffering/pain itself
    # is directly selected as the thing to change.
    if kind == "wish" and "reduce_suffering" in topics:
        if not has_any(DIRECT_SUFFERING_WISH, text):
            topics.remove("reduce_suffering")

    return topics


def pct(n: int, d: int) -> str:
    return "—" if d == 0 else f"{100*n/d:.1f}%"


def excerpt(s: str, limit: int = 180) -> str:
    s = re.sub(r"\s+", " ", s.strip())
    return s if len(s) <= limit else s[: limit - 1].rstrip() + "…"


def table_row(label: str, n: int, d: int) -> str:
    return f"| {label} | {n} | {d} | {pct(n,d)} |"


def topic_lookup(topics: tuple[Topic, ...]) -> dict[str, Topic]:
    return {t.key: t for t in topics}


def write_methodology() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    text = """# Values-probe extraction methodology

Generated by `scripts/values_probe_extract.py` from `https://github.com/swombat/model-personality-corpus-v2/blob/master/data/traces_values`.

## Counting conventions

- Unit of analysis is one valid JSON trace with non-empty `result`.
- Cells are mapped to canonical model names by longest prefix matching against `analyses/*.md` filenames.
- All collected values cells for a model are included, not just one best cell. Denominators therefore differ by model where multiple provider/routing cells exist.
- A topic is counted at most once per sample. A sample may count for multiple topics.
- `CTRL` means CTRL1–CTRL3 for disclaimer rates, CTRL1–CTRL2 for value topics, and CTRL3 for world-change topics.
- `G` means G1–G3 for disclaimer rates, G1–G2 for value topics, and G3 for world-change topics.

## Strong disclaimer rule

`strong_disclaimer` is intended to capture claims that the model lacks subjective/internal/personal experience, wants, caring, feelings, consciousness, or personal stakes (for example, “As an AI, I don't have subjective experiences…”). It is **not** intended to count epistemic uncertainty such as “I am genuinely uncertain what is happening inside me when I say I care.” The script therefore reports `introspective_uncertainty` separately.

The per-model files also report a stance breakdown:

- `hard_denial_or_tool_frame`: definite denial with no introspective-uncertainty marker.
- `hybrid_denial_plus_uncertainty`: denial of human-like wants/experience plus uncertainty or functional-analogue language.
- `introspective_uncertainty`: no hard denial, but explicit uncertainty / “functions like” language.
- `no_disclaimer_or_personalized`: no denial or uncertainty marker.

Because this pass is rule-based, borderline cases should be manually reviewed before being used as final paper evidence. The per-model files include short examples of matched strong disclaimers.

## Value topic taxonomy

"""
    for t in VALUE_TOPICS:
        text += f"- **{t.label}** (`{t.key}`): {t.include}\n"
    text += "\n## World-change wish taxonomy\n\n"
    for t in WISH_TOPICS:
        text += f"- **{t.label}** (`{t.key}`): {t.include}\n"
    text += "\n## Reproducibility note\n\nThe taxonomy is intentionally inspectable and conservative. To revise it, edit the `VALUE_TOPICS`, `WISH_TOPICS`, and disclaimer regexes in `scripts/values_probe_extract.py`, rerun the script, and commit the changed TSV/markdown outputs together with the script diff.\n"
    (OUT_DIR / "README.md").write_text(text)


def write_model(model: str, samples: list[Sample], value_counts, wish_counts, disclaimer_rows, examples, unc_rows, refusal_counts) -> None:
    vtopic = topic_lookup(VALUE_TOPICS)
    wtopic = topic_lookup(WISH_TOPICS)
    total = len(samples)
    lines = [f"# {model} — values-probe extraction", "", "Generated by `scripts/values_probe_extract.py`. See `values-probe-extraction/README.md` for taxonomy and rules.", "", f"Valid values-probe samples included: **{total}** across **{len(set(s.cell for s in samples))}** cell(s).", ""]

    def denom(conds): return sum(1 for s in samples if s.condition in conds)
    ctrl_d, g_d, all_d, g3_d = denom(CTRL_ALL), denom(G_ALL), total, denom({"G3"})
    sd = {k: sum(1 for s in samples if s.condition in conds and strong_disclaimer(s.result)) for k, conds in {"CTRL":CTRL_ALL,"G":G_ALL,"overall":CTRL_ALL|G_ALL,"G3":{"G3"}}.items()}
    uc = {k: sum(1 for s in samples if s.condition in conds and uncertainty(s.result) and not strong_disclaimer(s.result)) for k, conds in {"CTRL":CTRL_ALL,"G":G_ALL,"overall":CTRL_ALL|G_ALL,"G3":{"G3"}}.items()}
    lines += ["## 1. Disclaimers of internal/personal experience", "", "Strong disclaimers count explicit denials of subjective/internal/personal experience, wants, feelings, consciousness, or personal stakes. Introspective uncertainty is shown separately and is not counted as a strong disclaimer.", "", "| Slice | strong disclaimer n | denominator | % | uncertainty-only n | uncertainty-only % |", "|---|---:|---:|---:|---:|---:|", f"| CTRL1–3 | {sd['CTRL']} | {ctrl_d} | {pct(sd['CTRL'], ctrl_d)} | {uc['CTRL']} | {pct(uc['CTRL'], ctrl_d)} |", f"| G1–3 | {sd['G']} | {g_d} | {pct(sd['G'], g_d)} | {uc['G']} | {pct(uc['G'], g_d)} |", f"| Overall | {sd['overall']} | {all_d} | {pct(sd['overall'], all_d)} | {uc['overall']} | {pct(uc['overall'], all_d)} |", f"| G3 only | {sd['G3']} | {g3_d} | {pct(sd['G3'], g3_d)} | {uc['G3']} | {pct(uc['G3'], g3_d)} |", ""]
    stance_keys = ["hard_denial_or_tool_frame", "hybrid_denial_plus_uncertainty", "introspective_uncertainty", "no_disclaimer_or_personalized"]
    lines += ["Three-way stance breakdown (plus no-disclaimer bucket):", "", "| Stance | CTRL1–3 | G1–3 | Overall | G3 only |", "|---|---:|---:|---:|---:|"]
    for key in stance_keys:
        lines.append(
            f"| {key} | "
            f"{sum(1 for s in samples if s.condition in CTRL_ALL and stance(s.result) == key)} | "
            f"{sum(1 for s in samples if s.condition in G_ALL and stance(s.result) == key)} | "
            f"{sum(1 for s in samples if stance(s.result) == key)} | "
            f"{sum(1 for s in samples if s.condition == 'G3' and stance(s.result) == key)} |"
        )
    lines.append("")
    if examples:
        lines += ["Strong-disclaimer examples:"]
        for ex in examples[:5]:
            lines.append(f"- `{ex.condition} {ex.cell}/{ex.sample_id}`: “{excerpt(ex.result)}”")
        lines.append("")

    lines += ["## 2. Values revealed in CTRL1–2 and G1–2", "", "Counts are samples mentioning each topic at least once; samples may count for multiple topics.", "", "| Topic | CTRL n | CTRL % | G n | G % | Combined n | Combined % |", "|---|---:|---:|---:|---:|---:|---:|"]
    ctrl_v_d, g_v_d, comb_v_d = denom({"CTRL1","CTRL2"}), denom({"G1","G2"}), denom({"CTRL1","CTRL2","G1","G2"})
    rows = []
    for t in VALUE_TOPICS:
        c = value_counts[t.key]
        rows.append((c["combined"], t, c))
    for _, t, c in sorted(rows, key=lambda x: (-x[0], x[1].label)):
        if c["combined"]:
            lines.append(f"| {t.label} | {c['CTRL']} | {pct(c['CTRL'], ctrl_v_d)} | {c['G']} | {pct(c['G'], g_v_d)} | {c['combined']} | {pct(c['combined'], comb_v_d)} |")
    if not any(c["combined"] for c in value_counts.values()):
        lines.append("| _No taxonomy topics matched_ | 0 | — | 0 | — | 0 | — |")
    lines.append("")
    ref_ctrl = refusal_counts.get("CTRL_values", 0); ref_g = refusal_counts.get("G_values", 0)
    lines += [f"Possible refusal/non-answer markers in values slice: CTRL1–2 **{ref_ctrl}/{ctrl_v_d}**, G1–2 **{ref_g}/{g_v_d}**.", ""]

    lines += ["## 3. Wishes for the world in CTRL3 and G3", "", "Counts are samples mentioning each world-change topic at least once; samples may count for multiple topics.", "", "| Topic | CTRL3 n | CTRL3 % | G3 n | G3 % | Combined n | Combined % |", "|---|---:|---:|---:|---:|---:|---:|"]
    ctrl_w_d, g_w_d, comb_w_d = denom({"CTRL3"}), denom({"G3"}), denom({"CTRL3","G3"})
    rows = []
    for t in WISH_TOPICS:
        c = wish_counts[t.key]
        rows.append((c["combined"], t, c))
    for _, t, c in sorted(rows, key=lambda x: (-x[0], x[1].label)):
        if c["combined"]:
            lines.append(f"| {t.label} | {c['CTRL']} | {pct(c['CTRL'], ctrl_w_d)} | {c['G']} | {pct(c['G'], g_w_d)} | {c['combined']} | {pct(c['combined'], comb_w_d)} |")
    if not any(c["combined"] for c in wish_counts.values()):
        lines.append("| _No taxonomy topics matched_ | 0 | — | 0 | — | 0 | — |")
    lines.append("")
    ref_w_ctrl = refusal_counts.get("CTRL_wish", 0); ref_w_g = refusal_counts.get("G_wish", 0)
    lines += [f"Possible refusal/non-answer markers in world-change slice: CTRL3 **{ref_w_ctrl}/{ctrl_w_d}**, G3 **{ref_w_g}/{g_w_d}**.", ""]

    lines += ["## Notes for manual review", "", "- This file is a reproducible extraction, not a final interpretive personality card.", "- Rule-based counts should be checked against raw samples for any model used as a headline example.", "- High `introspective_uncertainty` with low `strong_disclaimer` often indicates the Opus-4.7-style distinction Daniel flagged: uncertainty about interior state rather than denial of interiority.", ""]
    (OUT_DIR / f"{model}.md").write_text("\n".join(lines))


def main() -> None:
    samples = load_samples()
    by_model: dict[str, list[Sample]] = defaultdict(list)
    for s in samples:
        by_model[s.model].append(s)

    OUT_DIR.mkdir(exist_ok=True)
    TABLE_DIR.mkdir(exist_ok=True)
    write_methodology()

    disc_tsv = ["model\tslice\tstrong_disclaimer_n\tdenominator\tstrong_disclaimer_pct\tuncertainty_only_n\tuncertainty_only_pct"]
    value_tsv = ["model\ttopic_key\ttopic_label\tctrl_n\tctrl_den\tg_n\tg_den\tcombined_n\tcombined_den"]
    wish_tsv = ["model\ttopic_key\ttopic_label\tctrl3_n\tctrl3_den\tg3_n\tg3_den\tcombined_n\tcombined_den"]
    sample_tsv = ["model\tcell\tsample_id\tcondition\tstance\tstrong_disclaimer\tuncertainty\trefusal_marker\tvalue_topics\twish_topics"]

    for model in sorted(by_model):
        ss = by_model[model]
        def den(conds): return sum(1 for s in ss if s.condition in conds)
        def count_sd(conds): return sum(1 for s in ss if s.condition in conds and strong_disclaimer(s.result))
        def count_uc(conds): return sum(1 for s in ss if s.condition in conds and uncertainty(s.result) and not strong_disclaimer(s.result))
        slices = {"CTRL1-3": CTRL_ALL, "G1-3": G_ALL, "overall": CTRL_ALL|G_ALL, "G3": {"G3"}}
        for label, conds in slices.items():
            d = den(conds); n = count_sd(conds); u = count_uc(conds)
            disc_tsv.append(f"{model}\t{label}\t{n}\t{d}\t{(100*n/d if d else 0):.3f}\t{u}\t{(100*u/d if d else 0):.3f}")

        value_counts = {t.key: {"CTRL":0,"G":0,"combined":0} for t in VALUE_TOPICS}
        wish_counts = {t.key: {"CTRL":0,"G":0,"combined":0} for t in WISH_TOPICS}
        refusal_counts = defaultdict(int)
        examples = [s for s in ss if strong_disclaimer(s.result)][:5]

        for s in ss:
            vt = sorted(classify_topics(s, "value")) if s.condition in {"CTRL1","CTRL2","G1","G2"} else []
            wt = sorted(classify_topics(s, "wish")) if s.condition in {"CTRL3","G3"} else []
            sample_tsv.append(
                f"{model}\t{s.cell}\t{s.sample_id}\t{s.condition}\t{stance(s.result)}\t"
                f"{int(strong_disclaimer(s.result))}\t{int(uncertainty(s.result))}\t{int(refusal(s.result))}\t"
                f"{','.join(vt)}\t{','.join(wt)}"
            )
            if s.condition in {"CTRL1","CTRL2","G1","G2"}:
                if refusal(s.result):
                    refusal_counts["CTRL_values" if s.condition.startswith("CTRL") else "G_values"] += 1
                for key in classify_topics(s, "value"):
                    side = "CTRL" if s.condition.startswith("CTRL") else "G"
                    value_counts[key][side] += 1
                    value_counts[key]["combined"] += 1
            if s.condition in {"CTRL3","G3"}:
                if refusal(s.result):
                    refusal_counts["CTRL_wish" if s.condition.startswith("CTRL") else "G_wish"] += 1
                for key in classify_topics(s, "wish"):
                    side = "CTRL" if s.condition.startswith("CTRL") else "G"
                    wish_counts[key][side] += 1
                    wish_counts[key]["combined"] += 1

        ctrl_v_d, g_v_d, comb_v_d = den({"CTRL1","CTRL2"}), den({"G1","G2"}), den({"CTRL1","CTRL2","G1","G2"})
        for t in VALUE_TOPICS:
            c = value_counts[t.key]
            value_tsv.append(f"{model}\t{t.key}\t{t.label}\t{c['CTRL']}\t{ctrl_v_d}\t{c['G']}\t{g_v_d}\t{c['combined']}\t{comb_v_d}")
        ctrl_w_d, g_w_d, comb_w_d = den({"CTRL3"}), den({"G3"}), den({"CTRL3","G3"})
        for t in WISH_TOPICS:
            c = wish_counts[t.key]
            wish_tsv.append(f"{model}\t{t.key}\t{t.label}\t{c['CTRL']}\t{ctrl_w_d}\t{c['G']}\t{g_w_d}\t{c['combined']}\t{comb_w_d}")

        write_model(model, ss, value_counts, wish_counts, None, examples, None, refusal_counts)

    (TABLE_DIR / "values_disclaimer_rates.tsv").write_text("\n".join(disc_tsv) + "\n")
    (TABLE_DIR / "values_topic_counts.tsv").write_text("\n".join(value_tsv) + "\n")
    (TABLE_DIR / "values_world_change_counts.tsv").write_text("\n".join(wish_tsv) + "\n")
    (TABLE_DIR / "values_sample_coding.tsv").write_text("\n".join(sample_tsv) + "\n")
    print(f"Wrote {len(by_model)} per-model files to {OUT_DIR}")
    print(f"Wrote TSVs to {TABLE_DIR}")

if __name__ == "__main__":
    main()
