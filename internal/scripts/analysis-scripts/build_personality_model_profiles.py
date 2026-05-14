#!/usr/bin/env python3
"""Build rich model-level personality profiles from per-cell freeflow aggregates.

The concise `personality-model-cards/` directory is intentionally short and suitable
for public-facing model cards. This script creates the missing intermediate layer:
rich profiles that preserve the recurring preoccupations, reader stance,
representative evidence, and route/provider flavour notes from each underlying
cell aggregate.
"""
from __future__ import annotations

import collections
import json
import re
from pathlib import Path

ROOT = Path('/Users/danieltenner/dev/drift-paper')
AGG = ROOT / 'analysis/freeflow/personality-aggregates'
DIFF = ROOT / 'analysis/freeflow/model-cell-difference-analysis'
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


def first_para(txt: str) -> str:
    for p in re.split(r'\n\s*\n', txt.strip()):
        p = p.strip()
        if p:
            return p
    return ''


def clean_variant_language(txt: str) -> str:
    # Keep audit meaning, but avoid making the intermediate profiles feel like
    # public cards accidentally talking about "cells" as personality objects.
    reps = [
        (r'## Cell-level freeflow read', '## Variant-level freeflow read'),
        (r'\b[Cc]ell-level\b', 'variant-level'),
        (r'\bThis cell\b', 'This variant'),
        (r'\bthis cell\b', 'this variant'),
        (r'\bThe cell\b', 'The variant'),
        (r'\bthe cell\b', 'the variant'),
        (r'\b[Cc]ell\b', 'variant'),
    ]
    for pat, rep in reps:
        txt = re.sub(pat, rep, txt)
    return txt.strip()


def compact(txt: str) -> str:
    return re.sub(r'\n{3,}', '\n\n', txt.strip())


def load_manifest():
    manifest = json.loads((AGG / 'manifest.json').read_text())
    by = collections.defaultdict(list)
    for m in manifest:
        by[canonical(m.get('source_models'), m['cell'])].append(m)
    return {k: sorted(v, key=lambda x: x['cell']) for k, v in sorted(by.items())}


def load_decisions():
    p = DIFF / 'decisions.json'
    if not p.exists():
        return {}
    return {r['model']: r for r in json.loads(p.read_text())}


def variant_detail(m: dict) -> str:
    txt = (ROOT / m['aggregate']).read_text(errors='ignore')
    wanted = [
        'Aggregate profile',
        'Recurring preoccupations and imagery',
        'Reader relationship and expressive stance',
        'Representative evidence',
        'Cell-level freeflow read',
        'Cautions for synthesis',
    ]
    parts = [
        f'### Variant: `{m["cell"]}`',
        '',
        f'- Samples: {m["samples"]}',
        f'- Sample kinds: `{m.get("sample_kind_counts", {})}`',
        f'- Confidence: `{m.get("confidence_counts", {})}`',
        f'- Source aggregate: `{m["aggregate"]}`',
        '',
    ]
    for h in wanted:
        body = section(txt, h)
        if body:
            heading = h.replace('Cell-level', 'Variant-level')
            parts += [f'#### {heading}', '', clean_variant_language(body), '']
    return '\n'.join(parts).strip()


def build_profile(model: str, variants: list[dict], decisions: dict) -> tuple[str, dict]:
    sf = safe(model)
    total = sum(v['samples'] for v in variants)
    dec = decisions.get(model, {}).get('decision', 'SINGLE_VARIANT')
    lines = [
        f'# {model} — freeflow personality profile',
        '',
        f'_Rich intermediate profile based on {total} freeflow samples'
        + (f' across {len(variants)} route/provider variants' if len(variants) > 1 else '')
        + '._',
        '',
        '> Purpose: preserve the personality evidence that is too detailed for the concise public model card. ',
        '> Use this as the source layer for later card writing, not as the final 2–3 paragraph card itself.',
        '',
        '## Source summary',
        '',
        f'- Variants: {len(variants)}',
        f'- Samples: {total}',
        f'- Cell-difference decision: `{dec}`',
    ]
    card_path = CARDS / 'cards' / f'{sf}.md'
    if card_path.exists():
        lines.append(f'- Current concise card: `{card_path.relative_to(ROOT)}`')
    if len(variants) > 1:
        rpt = DIFF / 'model-cell-difference-reports' / f'{sf}.md'
        if rpt.exists():
            lines.append(f'- Cell-difference report: `{rpt.relative_to(ROOT)}`')
    lines += ['', '## Concise model-card text currently derived from this layer', '']
    if card_path.exists():
        card_txt = card_path.read_text(errors='ignore')
        card_body = re.sub(r'^#.*?\n\n_.*?_\n\n', '', card_txt, count=1, flags=re.S).strip()
        lines.append(card_body or '_No card body found._')
    else:
        lines.append('_No concise card exists yet._')

    if len(variants) > 1:
        rpt = DIFF / 'model-cell-difference-reports' / f'{sf}.md'
        if rpt.exists():
            rtxt = rpt.read_text(errors='ignore')
            lines += ['', '## Model-level synthesis from route comparison', '']
            for h in ['Verdict', 'Shared personality center', 'Route-level differences', 'Evidence', 'Notes for later synthesis']:
                body = section(rtxt, h)
                if body:
                    lines += [f'### {h}', '', body.strip(), '']
    else:
        # For single-variant models, the aggregate itself is the profile. Pull its
        # main sections up before the variant detail to make the file skimmable.
        atxt = (ROOT / variants[0]['aggregate']).read_text(errors='ignore')
        lines += ['', '## Model-level synthesis from the available variant', '']
        for h in ['Aggregate profile', 'Recurring preoccupations and imagery', 'Reader relationship and expressive stance', 'Cell-level freeflow read', 'Cautions for synthesis']:
            body = section(atxt, h)
            if body:
                lines += [f'### {h.replace("Cell-level", "Variant-level")}', '', clean_variant_language(body), '']

    lines += ['', '## Detailed variant evidence', '']
    for m in variants:
        lines += [variant_detail(m), '']

    index_row = {
        'model': model,
        'safe': sf,
        'variants': len(variants),
        'samples': total,
        'profile': f'analysis/freeflow/personality-model-profiles/profiles/{sf}.md',
        'card': f'analysis/freeflow/personality-model-cards/cards/{sf}.md' if card_path.exists() else None,
        'difference_decision': dec,
    }
    return compact('\n'.join(lines)) + '\n', index_row


def main():
    groups = load_manifest()
    decisions = load_decisions()
    if OUT.exists():
        for path in sorted(OUT.rglob('*'), reverse=True):
            if path.is_file():
                path.unlink()
            elif path.is_dir():
                path.rmdir()
    PROFILES.mkdir(parents=True, exist_ok=True)
    index = []
    for model, variants in groups.items():
        txt, row = build_profile(model, variants, decisions)
        (PROFILES / f'{row["safe"]}.md').write_text(txt)
        index.append(row)
    (OUT / 'index.json').write_text(json.dumps(index, indent=2, ensure_ascii=False))
    lines = [
        '# Freeflow personality model profiles',
        '',
        'Rich model-level profiles preserving the freeflow personality evidence that is too detailed for the concise model cards.',
        '',
        'Relationship to adjacent folders:',
        '',
        '- `personality-eval-bv1/` — per-sample readings.',
        '- `personality-aggregates/` — independent per-route/provider variant aggregates.',
        '- `model-cell-difference-analysis/` — route/provider comparison and divergence decisions.',
        '- `personality-model-profiles/` — this folder: rich per-model profiles with detailed variant evidence.',
        '- `personality-model-cards/` — concise 2–3 paragraph cards for display/synthesis.',
        '',
        f'- Profiles: {len(index)}',
        '',
        '## Profiles',
        '',
    ]
    for r in index:
        lines.append(f'- [{r["model"]}](profiles/{r["safe"]}.md) — samples: {r["samples"]}; variants: {r["variants"]}; decision: `{r["difference_decision"]}`')
    (OUT / 'README.md').write_text('\n'.join(lines) + '\n')
    print(json.dumps({'profiles': len(index), 'out': str(OUT)}, indent=2))


if __name__ == '__main__':
    main()
