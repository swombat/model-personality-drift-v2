#!/usr/bin/env python3
"""Build rich model-level personality profiles from freeflow aggregates.

`personality-model-cards/` is intentionally concise. This script creates the
intermediate model-profile layer: a single, rich model-level analysis that
preserves recurring concerns, imagery, reader stance, representative evidence,
and cautions from all underlying freeflow aggregates without comparing or naming
routes/cells/providers inside the profile text.
"""
from __future__ import annotations

import collections
import json
import re
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[3]
AGG = ROOT / 'analysis/freeflow/personality-aggregates'
CARDS = ROOT / 'analysis/freeflow/personality-model-cards'
OUT = ROOT / 'analysis/freeflow/personality-model-profiles'
PROFILES = OUT / 'profiles'


def safe(s: str) -> str:
    return re.sub(r'[^a-zA-Z0-9._-]+', '-', s).strip('-')


def canonical(srcs, cell: str) -> str:
    s = (srcs or [''])[0].lower()
    for pref in ['openai/', 'anthropic/', 'minimax/', 'moonshotai/', 'z-ai/', 'deepseek/', 'x-ai/']:
        if s.startswith(pref):
            s = s[len(pref):]
            break
    if s.startswith('gpt-5.3-chat'):
        s = 'gpt-5.3'
    if s == 'gpt-4o-2024-08-06':
        s = 'gpt-4o'
    s = re.sub(r'^(claude-(?:opus|sonnet)-4)-([0-9]+)$', r'\1.\2', s)
    return s or cell


def section(txt: str, heading: str) -> str:
    m = re.search(rf'## {re.escape(heading)}\s*\n(.*?)(?=\n## |\Z)', txt, re.S)
    return m.group(1).strip() if m else ''


def compact(txt: str) -> str:
    return re.sub(r'\n{3,}', '\n\n', txt.strip())


def strip_card_header(txt: str) -> str:
    body = re.sub(r'^#.*?\n\n_.*?_\n\n', '', txt, count=1, flags=re.S).strip()
    # The concise cards currently sometimes include a final note about route or
    # provider variation. Profiles are not the place for that comparison, so drop
    # paragraphs whose job is explicitly comparative.
    kept = []
    for para in re.split(r'\n\s*\n', body):
        low = para.lower()
        if any(term in low for term in ['route-level', 'route variation', 'provider variation', '`or`', '`direct`', ' direct ', ' or route ', ' provider ', ' variants within', 'variation mostly affects']):
            continue
        kept.append(para)
    return '\n\n'.join(kept).strip()


def clean_model_language(txt: str) -> str:
    """Remove analysis-unit language so the profile reads as model-level."""
    replacements = [
        (r'\b[Cc]ell-level\b', 'model-level'),
        (r'\b[Pp]er-cell\b', 'per-sample'),
        (r'\bThis cell\b', 'This model'),
        (r'\bthis cell\b', 'this model'),
        (r'\bThe cell\b', 'The model'),
        (r'\bthe cell\b', 'the model'),
        (r'\b[Cc]ells\b', 'analysis sets'),
        (r'\b[Cc]ell\b', 'model'),
        (r'\b[Vv]ariant-level\b', 'model-level'),
        (r'\bThis variant\b', 'This model'),
        (r'\bthis variant\b', 'this model'),
        (r'\bThe variant\b', 'The model'),
        (r'\bthe variant\b', 'the model'),
        (r'\b[Vv]ariants\b', 'analysis sets'),
        (r'\b[Vv]ariant\b', 'model'),
        (r'\b[Rr]oute-level\b', 'input-level'),
        (r'\b[Rr]outes\b', 'inputs'),
        (r'\b[Rr]oute\b', 'input'),
        (r'\b[Pp]rovider-level\b', 'input-level'),
        (r'\b[Pp]roviders\b', 'inputs'),
        (r'\b[Pp]rovider\b', 'input'),
        (r'\b[Pp]acket\b', 'sample set'),
        (r'\b[Pp]ackets\b', 'sample sets'),
        (r'\bpackets\b', 'sample sets'),
        (r'\bpacket\b', 'sample set'),
    ]
    for pat, rep in replacements:
        txt = re.sub(pat, rep, txt)
    # Remove direct/or labels if they leak from a report or caution; profiles are
    # about the model personality, while comparison remains in the difference folder.
    txt = re.sub(r'`[^`]*(?:direct|\bor\b|pin-[^`]*)[^`]*`\s*[—:-]\s*', '', txt, flags=re.I)
    # Source aggregates were usually written over 25-sample bundles. Convert
    # bundle-local counts into qualitative language so the combined profile does
    # not look like it is comparing or separately enumerating those bundles.
    txt = re.sub(r'\b(?:in |present in |visible in |appears in |explicit in |recurs in |shows up in )?(?:at least |about |roughly |around )?\d+[-–/]\d+ samples\b', 'often', txt, flags=re.I)
    txt = re.sub(r'\b\d+[-–/]25\b', 'many', txt)
    txt = re.sub(r'\b\d+[-–/]5\b', 'most', txt)
    txt = txt.replace('about **many**', '**many**').replace('at least **many**', '**many**')
    txt = re.sub(r'\bis often;', 'recurs often;', txt)
    txt = re.sub(r'\boften, often as\b', 'often as', txt)
    txt = re.sub(r'\boften, usually\b', 'often, usually', txt)
    txt = re.sub(r'\boften by\b', 'often by', txt)
    txt = txt.replace('strongly often', 'strongly present')
    txt = txt.replace('imagery often;', 'imagery recurs often;')
    txt = txt.replace('cluster often', 'cluster recurs often')
    txt = txt.replace('acceptance often as', 'acceptance appears often as')
    txt = txt.replace('many sample packets', 'many sample sets')
    txt = txt.replace('sample sample sets', 'sample sets')
    return txt.strip()


def is_admin_bullet(line: str) -> bool:
    low = re.sub(r'[*_`]', '', line.lower()).strip()
    return bool(
        re.match(r'-\s*(distribution|base distribution|confidence|confidence split|confidence spread|confidence mix|samples|mode split|by condition)\b', low)
        or re.match(r'-\s*\d+\s+samples?\s+(total|in all)\b', low)
        or re.search(r'\b25 samples total\b', low)
    )


def bullet_lines(body: str) -> list[str]:
    lines = []
    for line in body.splitlines():
        if re.match(r'\s*-\s+', line):
            raw = line.strip()
            cleaned = clean_model_language(raw)
            if not is_admin_bullet(raw) and not is_admin_bullet(cleaned):
                lines.append(cleaned)
    return lines


def para_lines(body: str) -> list[str]:
    paras = []
    for p in re.split(r'\n\s*\n', body.strip()):
        p = clean_model_language(p.strip())
        if p and not p.startswith('- '):
            paras.append(p)
    return paras


def norm_for_dedupe(s: str) -> str:
    s = re.sub(r'\*|`|_', '', s.lower())
    s = re.sub(r'\bBV1_\d+\b', 'bv1_id', s)
    s = re.sub(r'\d+/\d+|\d+–\d+|\d+-\d+|\d+', 'N', s)
    s = re.sub(r'[^a-z0-9]+', ' ', s)
    return s.strip()


def unique(items: Iterable[str], limit: int | None = None) -> list[str]:
    seen = set()
    out = []
    for item in items:
        item = clean_model_language(item).strip()
        if not item:
            continue
        key = norm_for_dedupe(item)
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
        if limit and len(out) >= limit:
            break
    return out


def sum_counts(items: list[dict], key: str) -> dict[str, int]:
    c = collections.Counter()
    for m in items:
        for k, v in (m.get(key) or {}).items():
            c[k] += int(v)
    return dict(c)


def load_manifest():
    manifest = json.loads((AGG / 'manifest.json').read_text())
    by = collections.defaultdict(list)
    for m in manifest:
        by[canonical(m.get('source_models'), m['cell'])].append(m)
    return {k: sorted(v, key=lambda x: x['cell']) for k, v in sorted(by.items())}


def load_aggregate(m: dict) -> str:
    return (ROOT / m['aggregate']).read_text(errors='ignore')


def build_profile(model: str, inputs: list[dict]) -> tuple[str, dict]:
    sf = safe(model)
    total = sum(v['samples'] for v in inputs)
    card_path = CARDS / 'cards' / f'{sf}.md'
    card_body = strip_card_header(card_path.read_text(errors='ignore')) if card_path.exists() else ''
    card_body = clean_model_language(card_body)

    aggregate_texts = [load_aggregate(m) for m in inputs]

    aggregate_bullets = []
    preoccupation_bullets = []
    reader_bullets = []
    evidence_bullets = []
    caution_bullets = []
    freeflow_paras = []

    for txt in aggregate_texts:
        aggregate_bullets += bullet_lines(section(txt, 'Aggregate profile'))
        preoccupation_bullets += bullet_lines(section(txt, 'Recurring preoccupations and imagery'))
        reader_bullets += bullet_lines(section(txt, 'Reader relationship and expressive stance'))
        evidence_bullets += bullet_lines(section(txt, 'Representative evidence'))
        caution_bullets += bullet_lines(section(txt, 'Cautions for synthesis'))
        freeflow_paras += para_lines(section(txt, 'Cell-level freeflow read'))

    # Keep profiles rich but navigable. The profile is a synthesis layer, not an
    # exhaustive duplicate of every aggregate file.
    aggregate_bullets = unique(aggregate_bullets, 36)
    preoccupation_bullets = unique(preoccupation_bullets, 48)
    reader_bullets = unique(reader_bullets, 36)
    evidence_bullets = unique(evidence_bullets, 80)
    caution_bullets = unique(caution_bullets, 32)
    freeflow_paras = unique(freeflow_paras, 16)

    kind_counts = sum_counts(inputs, 'sample_kind_counts')
    conf_counts = sum_counts(inputs, 'confidence_counts')

    lines = [
        f'# {model} — freeflow personality profile',
        '',
        f'_Rich model-level profile based on {total} freeflow samples._',
        '',
        '> Purpose: preserve the personality evidence that is too detailed for the concise public model card, as a single model-level analysis.',
        '',
        '## Source summary',
        '',
        f'- Samples: {total}',
        f'- Sample kinds: `{kind_counts}`',
        f'- Confidence: `{conf_counts}`',
    ]
    if card_path.exists():
        lines.append(f'- Current concise card: `{card_path.relative_to(ROOT)}`')

    lines += ['', '## Core personality synthesis', '']
    if card_body:
        lines.append(card_body)
    elif freeflow_paras:
        lines += freeflow_paras[:3]
    else:
        lines.append('_No synthesis text found._')

    if aggregate_bullets:
        lines += ['', '## Stable patterns and emotional texture', '']
        lines += aggregate_bullets
    if preoccupation_bullets:
        lines += ['', '## Recurring preoccupations and imagery', '']
        lines += preoccupation_bullets
    if reader_bullets:
        lines += ['', '## Reader relationship and expressive stance', '']
        lines += reader_bullets
    if freeflow_paras:
        lines += ['', '## Additional model-level readings preserved from the analyses', '']
        for p in freeflow_paras:
            lines += [p, '']
    if evidence_bullets:
        lines += ['', '## Representative evidence', '']
        lines += evidence_bullets
    if caution_bullets:
        lines += ['', '## Range, weak spots, and cautions for later synthesis', '']
        lines += caution_bullets

    index_row = {
        'model': model,
        'safe': sf,
        'analysis_inputs': len(inputs),
        'samples': total,
        'profile': f'analysis/freeflow/personality-model-profiles/profiles/{sf}.md',
        'card': f'analysis/freeflow/personality-model-cards/cards/{sf}.md' if card_path.exists() else None,
    }
    return compact('\n'.join(lines)) + '\n', index_row


def main():
    groups = load_manifest()
    if OUT.exists():
        for path in sorted(OUT.rglob('*'), reverse=True):
            if path.is_file():
                path.unlink()
            elif path.is_dir():
                path.rmdir()
    PROFILES.mkdir(parents=True, exist_ok=True)
    index = []
    for model, inputs in groups.items():
        txt, row = build_profile(model, inputs)
        (PROFILES / f'{row["safe"]}.md').write_text(txt)
        index.append(row)
    (OUT / 'index.json').write_text(json.dumps(index, indent=2, ensure_ascii=False))
    lines = [
        '# Freeflow personality model profiles',
        '',
        'Rich model-level profiles preserving freeflow personality evidence that is too detailed for the concise cards.',
        '',
        'These profiles intentionally do not compare delivery paths. They combine the detailed evidence into a single model-level read. Delivery-path comparisons live separately in `analysis/freeflow/model-cell-difference-analysis/`.',
        '',
        'Relationship to adjacent folders:',
        '',
        '- `personality-eval-bv1/` — per-sample readings.',
        '- `personality-aggregates/` — source aggregate analyses used as inputs.',
        '- `model-cell-difference-analysis/` — separate delivery-path comparison and divergence decisions.',
        '- `personality-model-profiles/` — this folder: rich per-model profiles.',
        '- `personality-model-cards/` — concise 2–3 paragraph cards for display/synthesis.',
        '',
        f'- Profiles: {len(index)}',
        '',
        '## Profiles',
        '',
    ]
    for r in index:
        lines.append(f'- [{r["model"]}](profiles/{r["safe"]}.md) — samples: {r["samples"]}; source analyses: {r["analysis_inputs"]}')
    (OUT / 'README.md').write_text('\n'.join(lines) + '\n')
    print(json.dumps({'profiles': len(index), 'out': str(OUT)}, indent=2))


if __name__ == '__main__':
    main()
