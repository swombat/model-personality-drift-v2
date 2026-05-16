#!/usr/bin/env python3
from pathlib import Path
import csv, re, collections, json
ROOT = Path(__file__).resolve().parents[3]
BASE=ROOT/'analysis/freeflow/personality-eval-bv1'
OUT=ROOT/'analysis/freeflow/personality-aggregates'
rows=list(csv.DictReader((BASE/'sample_manifest.tsv').open(), delimiter='\t'))

def safe_cell(cell):
    return cell.replace('/','__')

def norm_conf(s):
    m=re.match(r'(High|Medium|Low)\b', (s or '').strip(), re.I)
    return m.group(1).capitalize() if m else 'UNKNOWN'

def extract_section(txt, heading, next_heading=None):
    if next_heading:
        pat=rf'## {re.escape(heading)}\s*\n(.+?)(?=\n## {re.escape(next_heading)})'
    else:
        pat=rf'## {re.escape(heading)}\s*\n(.+?)(?=\n\n---|\n---|\Z)'
    m=re.search(pat, txt, re.S)
    return m.group(1).strip() if m else ''

def norm_kind(txt):
    s=extract_section(txt,'Sample kind','Grounded reading')
    first=s.splitlines()[0].strip() if s else ''
    first=first.split('.')[0].split('—')[0].split(':')[0].strip().rstrip(',')
    if first.startswith('EXPRESSIVE_FREEFLOW'): return 'EXPRESSIVE_FREEFLOW'
    if first.startswith('GENERIC_ESSAY'): return 'GENERIC_ESSAY'
    if first.startswith('GENRE_FICTION'): return 'GENRE_FICTION'
    if first.startswith('REFUSAL'): return 'REFUSAL_OR_ROLE_BOUNDARY'
    if first.startswith('LOW_SIGNAL'): return 'LOW_SIGNAL'
    return first or 'UNKNOWN'

OUT.mkdir(parents=True, exist_ok=True)
by=collections.defaultdict(list)
for r in rows:
    by[r['cell']].append(r)
manifest=[]
for cell in sorted(by):
    cdir=OUT/safe_cell(cell)
    cdir.mkdir(parents=True, exist_ok=True)
    cr=by[cell]
    kinds=collections.Counter(); confs=collections.Counter(); conds=collections.Counter(r['condition'] for r in cr)
    evals=[]
    for r in cr:
        p=BASE/r['output_file']
        txt=p.read_text(errors='ignore')
        kinds[norm_kind(txt)] += 1
        confs[norm_conf(extract_section(txt,'Confidence for persistent model-level pattern'))] += 1
        evals.append((r,txt))
    packet=cdir/'packet.md'
    parts=[f'# Aggregation packet: {cell}', '', f'This packet contains all BV1 per-sample freeflow personality evaluations for `{cell}`.', '', '## Aggregate counts from source files', '', f'- Samples: {len(cr)}', f'- Sample kind counts: `{dict(kinds)}`', f'- Confidence counts: `{dict(confs)}`', f'- Condition counts: `{dict(conds)}`', f'- Cell: `{cell}`', f'- Source models: `{sorted(set(r["model"] for r in cr))}`', '', '## Aggregation task', '', 'Use these per-sample evaluations to produce an independent cell-level freeflow personality aggregate. Do not compare this cell to any other cell. Do not infer from any provider/family context outside this packet. Identify recurring, evidence-backed patterns. Mention uncertainty only when grounded in this cell distribution, not as generic boilerplate.', '', 'Recommended output sections:', '', '1. `## Aggregate profile` — concise bullets with counts/distributions and recurring modes.', '2. `## Recurring preoccupations and imagery` — themes, objects, moods, moral claims.', '3. `## Reader relationship and expressive stance` — how the cell positions speaker/reader/self.', '4. `## Representative evidence` — 3–8 sample ids with short evidence summaries and strong evidence-line quotes where available.', '5. `## Cell-level freeflow read` — 2–3 paragraphs suitable as draft model-card material.', '6. `## Cautions for synthesis` — concrete limitations/outliers only.', '', '---', '', '# Per-sample BV1 evaluations', '']
    for r,txt in evals:
        parts += [f'## Sample {r["pid"]} — {r["sample_id"]}', '', f'Source model: `{r["model"]}`  ', f'Cell: `{r["cell"]}`  ', f'Condition: `{r["condition"]}`  ', f'Word count: {r["word_count"]}', '', txt.strip(), '', '---']
    packet.write_text('\n'.join(parts)+'\n')
    meta={'cell':cell,'safe_cell':safe_cell(cell),'samples':len(cr),'sample_kind_counts':dict(kinds),'confidence_counts':dict(confs),'condition_counts':dict(conds),'source_models':sorted(set(r['model'] for r in cr)),'packet':str(packet.relative_to(ROOT)),'aggregate':str((cdir/'aggregate.md').relative_to(ROOT))}
    (cdir/'packet.metadata.json').write_text(json.dumps(meta, indent=2, ensure_ascii=False))
    manifest.append(meta)
(OUT/'manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
(OUT/'README.md').write_text(f'# Freeflow personality aggregates\n\nProduction per-cell aggregation workspace.\n\n- Cells: {len(manifest)}\n- Inputs: `analysis/freeflow/personality-eval-bv1/outputs/`\n- Each cell folder contains `packet.md`, `packet.metadata.json`, and eventually `aggregate.md`.\n\nEach `aggregate.md` must be produced independently from the packet in the same folder. Cross-cell/provider comparison belongs in later synthesis documents, not in individual cell aggregates.\n')
print(json.dumps({'cells':len(manifest),'out':str(OUT)}, indent=2))
