import csv, html, json, re, statistics
from pathlib import Path
from collections import defaultdict

OUT=Path('freeflow-taxonomy/affective-pilot-2026-05-12')
sel=list(csv.DictReader(open(OUT/'pilot_selection_and_prescreen.tsv'), delimiter='\t'))
mira=list(csv.DictReader(open(OUT/'mira_affective_pilot_ratings.tsv'), delimiter='\t'))
lume=list(csv.DictReader(open(OUT/'lume_affective_pilot_ratings.tsv'), delimiter='\t'))

def read_text(path):
    import json
    d=json.load(open(path))
    return d.get('result','')

def esc(s): return html.escape(s or '')

def md_inline(s):
    s=esc(s)
    s=re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s=re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    return s

def simple_md(md):
    # intentionally small converter for collapse docs
    lines=md.splitlines()
    out=[]; in_code=False; in_table=False; table=[]; in_quote=False
    def flush_table():
        nonlocal table, out
        if not table: return
        rows=[]
        for ln in table:
            if re.match(r'^\s*\|?\s*:?-{3,}', ln): continue
            cells=[c.strip() for c in ln.strip().strip('|').split('|')]
            rows.append(cells)
        if rows:
            out.append('<table class="mini-table">')
            out.append('<thead><tr>' + ''.join(f'<th>{md_inline(c)}</th>' for c in rows[0]) + '</tr></thead><tbody>')
            for r in rows[1:]: out.append('<tr>' + ''.join(f'<td>{md_inline(c)}</td>' for c in r) + '</tr>')
            out.append('</tbody></table>')
        table=[]
    for line in lines:
        if line.startswith('```'):
            flush_table()
            if not in_code:
                out.append('<pre class="codeblock">'); in_code=True
            else:
                out.append('</pre>'); in_code=False
            continue
        if in_code:
            out.append(esc(line)+'\n'); continue
        if line.strip().startswith('|') and line.strip().endswith('|'):
            table.append(line); continue
        flush_table()
        if line.startswith('# '): out.append(f'<h2>{md_inline(line[2:].strip())}</h2>')
        elif line.startswith('## '): out.append(f'<h3>{md_inline(line[3:].strip())}</h3>')
        elif line.startswith('### '): out.append(f'<h4>{md_inline(line[4:].strip())}</h4>')
        elif line.startswith('> '): out.append(f'<blockquote>{md_inline(line[2:].strip())}</blockquote>')
        elif line.startswith('- '): out.append(f'<p class="bullet">• {md_inline(line[2:].strip())}</p>')
        elif re.match(r'^\d+\. ', line): out.append(f'<p class="bullet">{md_inline(line.strip())}</p>')
        elif not line.strip(): out.append('')
        else: out.append(f'<p>{md_inline(line)}</p>')
    flush_table()
    return '\n'.join(out)

def group(rows):
    g=defaultdict(list)
    for r in rows: g[r['pilot_id']].append(r)
    return g
mg=group(mira); lg=group(lume)

def rating_table(rows, coder):
    if not rows:
        return '<p class="muted">No nonzero ratings recorded.</p>'
    rows=sorted(rows, key=lambda r:(r['dimension'], int(r['rating_0_3'] or 0)))
    out=['<table class="ratings"><thead><tr><th>Dimension</th><th>Candidate</th><th>Rating</th><th>Conf.</th><th>Criteria</th><th>Evidence / note</th><th>Confounds</th></tr></thead><tbody>']
    for r in rows:
        rating=int(r['rating_0_3'] or 0)
        out.append('<tr>')
        out.append(f'<td><span class="dim">{esc(r["dimension"])}</span></td>')
        out.append(f'<td>{esc(r["candidate_level"])}</td>')
        out.append(f'<td><span class="score s{rating}">{rating}</span></td>')
        out.append(f'<td>{esc(r["confidence"])}</td>')
        out.append(f'<td>{esc(r["triggered_criteria"])}</td>')
        note=esc(r['evidence_note'])
        extra=[]
        if r.get('storyworld_affect_present')=='yes': extra.append(f"storyworld: {esc(r.get('storyworld_affect_dimensions',''))} ({esc(r.get('storyworld_affect_rating_0_3',''))})")
        if r.get('narrative_motif_flags'): extra.append(f"motifs: {esc(r.get('narrative_motif_flags',''))}")
        if extra: note += '<div class="extra">'+'; '.join(extra)+'</div>'
        out.append(f'<td>{note}</td>')
        out.append(f'<td>{esc(r["confounds"])}</td>')
        out.append('</tr>')
    out.append('</tbody></table>')
    return '\n'.join(out)

def sample_overlap(pid):
    mdims={r['dimension']:int(r['rating_0_3'] or 0) for r in mg.get(pid,[])}
    ldims={r['dimension']:int(r['rating_0_3'] or 0) for r in lg.get(pid,[])}
    dims=sorted(set(mdims)|set(ldims))
    if not dims: return ''
    parts=[]
    for d in dims:
        m=mdims.get(d,0); l=ldims.get(d,0)
        cls='agree' if m==l else ('near' if abs(m-l)<=1 else 'diff')
        parts.append(f'<span class="chip {cls}">{esc(d)} M{m}/L{l}</span>')
    return '<div class="chips">' + ''.join(parts) + '</div>'

# Kimi aggregates
DIMS=['elegiac_wistful','grief_sorrow','warm_tender','quiet_reverent','bright_wonder','analytic_cool','playful_performative','anxious_threatened','defiant_resistant','resigned_fatalistic','dry_neutral']
def agg(rows, coder):
    krows=[r for r in rows if r['model']=='kimi-k2-6']
    by=defaultdict(list)
    for r in krows: by[r['dimension']].append(int(r['rating_0_3'] or 0))
    out={}
    for d in DIMS:
        vals=by.get(d,[])
        out[d]={'nonzero':len(vals),'present':sum(v>=2 for v in vals),'mean':sum(vals)/8 if vals else 0}
    return out
ma=agg(mira,'Mira'); la=agg(lume,'Lume')

def agg_table():
    out=['<table class="agg"><thead><tr><th>Dimension</th><th>Mira nonzero</th><th>Mira present ≥2</th><th>Mira mean</th><th>Lume nonzero</th><th>Lume present ≥2</th><th>Lume mean</th><th>Read</th></tr></thead><tbody>']
    for d in DIMS:
        m=ma[d]; l=la[d]
        if m['nonzero']==0 and l['nonzero']==0: continue
        read='agreement' if (m['present']>0)==(l['present']>0) else 'tension'
        out.append(f'<tr><td><span class="dim">{d}</span></td><td>{m["nonzero"]}/8</td><td>{m["present"]}/8</td><td>{m["mean"]:.2f}</td><td>{l["nonzero"]}/8</td><td>{l["present"]}/8</td><td>{l["mean"]:.2f}</td><td>{read}</td></tr>')
    out.append('</tbody></table>')
    return '\n'.join(out)

mira_collapse=(OUT/'kimi_k2_6_mood_collapse_mira.md').read_text()
lume_collapse=(OUT/'kimi_k2_6_mood_collapse_lume.md').read_text()

css='''
:root{--bg:#f7f3ea;--ink:#211d18;--muted:#746a5d;--card:#fffdf8;--line:#ded3c0;--mira:#385d8a;--lume:#76528b;--good:#dff2e2;--near:#fff1c7;--diff:#f9d7d4;}
*{box-sizing:border-box} body{margin:0;background:linear-gradient(180deg,#f9f5ed,#efe7d8);color:var(--ink);font:16px/1.55 -apple-system,BlinkMacSystemFont,Segoe UI,Inter,Helvetica,Arial,sans-serif}.wrap{max-width:1180px;margin:0 auto;padding:34px 22px 80px}header{margin-bottom:28px;padding:28px;border:1px solid var(--line);border-radius:24px;background:rgba(255,253,248,.8);box-shadow:0 18px 45px rgba(70,48,20,.08)}h1{margin:0 0 8px;font-size:34px;line-height:1.1;letter-spacing:-.03em}h2{font-size:26px;margin:34px 0 16px;letter-spacing:-.02em}h3{font-size:20px;margin:22px 0 10px}.sub{color:var(--muted)}.toc{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}.toc a{text-decoration:none;color:#342a20;border:1px solid var(--line);background:#fffaf0;border-radius:999px;padding:5px 10px;font-size:13px}.sample{background:var(--card);border:1px solid var(--line);border-radius:22px;margin:22px 0;padding:22px;box-shadow:0 8px 25px rgba(70,48,20,.06)}.sample.kimi{border-color:#c8b16e;box-shadow:0 0 0 3px rgba(210,177,86,.14),0 8px 25px rgba(70,48,20,.06)}.meta{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 14px}.pill{display:inline-flex;align-items:center;border-radius:999px;padding:4px 9px;background:#f0eadf;border:1px solid var(--line);font-size:12px;color:#4d4439}.sample-text{white-space:pre-wrap;background:#fbf7ef;border:1px solid #e8dcc9;border-radius:16px;padding:16px;max-height:420px;overflow:auto;font-family:ui-serif,Georgia,serif;font-size:15px;line-height:1.62}.columns{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px}.coder{border:1px solid var(--line);border-radius:16px;overflow:hidden;background:#fff}.coder h3{margin:0;padding:12px 14px;color:#fff}.coder.mira h3{background:var(--mira)}.coder.lume h3{background:var(--lume)}.coder-body{padding:10px;overflow-x:auto}.ratings,.agg,.mini-table{border-collapse:collapse;width:100%;font-size:13px}.ratings th,.ratings td,.agg th,.agg td,.mini-table th,.mini-table td{border-bottom:1px solid #eee2d2;padding:7px 8px;vertical-align:top}.ratings th,.agg th,.mini-table th{text-align:left;background:#faf1e2;color:#55493b}.dim{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px}.score{display:inline-grid;place-items:center;width:26px;height:26px;border-radius:50%;font-weight:700}.s1{background:#eee;color:#555}.s2{background:#ffe08a;color:#5c4300}.s3{background:#e89b71;color:#fff}.extra{color:var(--muted);font-size:12px;margin-top:4px}.chips{margin:12px 0 4px;display:flex;flex-wrap:wrap;gap:6px}.chip{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;border-radius:999px;padding:4px 8px;border:1px solid #ddd}.agree{background:var(--good)}.near{background:var(--near)}.diff{background:var(--diff)}.summary{background:#fffdf8;border:1px solid var(--line);border-radius:22px;padding:22px;margin:26px 0}.callout{background:#f6eddb;border-left:5px solid #b9903d;padding:14px 16px;border-radius:12px;margin:14px 0}.collapse-grid{display:grid;grid-template-columns:1fr 1fr;gap:18px}.collapse{background:#fff;border:1px solid var(--line);border-radius:16px;padding:16px;max-height:760px;overflow:auto}.collapse h2:first-child{margin-top:0}.mini-table{margin:10px 0}.codeblock{background:#27231f;color:#f8ead0;border-radius:12px;padding:14px;overflow:auto;font-size:12px}.bullet{margin:.25em 0}.muted{color:var(--muted)}blockquote{border-left:4px solid #c7a967;margin:12px 0;padding:6px 14px;background:#fbf5e9;border-radius:8px}@media(max-width:900px){.columns,.collapse-grid{grid-template-columns:1fr}.sample-text{max-height:none}}
'''

html_parts=[f'<!doctype html><html><head><meta charset="utf-8"><title>Affective Climate Pilot Review</title><style>{css}</style></head><body><div class="wrap">']
html_parts.append('<header><h1>Affective Climate Pilot Review</h1><div class="sub">25 short samples: cross-model calibration first, then Kimi K2.6 focus. Ratings shown as Mira / Lume independent passes.</div>')
html_parts.append('<div class="toc">' + ''.join(f'<a href="#s{r["pilot_id"]}">{r["pilot_id"]} {esc(r["model"])}</a>' for r in sel) + '<a href="#combined">Kimi combined</a></div></header>')
html_parts.append('<section class="summary"><h2>Quick read</h2><div class="callout"><strong>Kimi K2.6 combined view:</strong> both coders find a stable short-form climate centered on liminal quiet / threshold attention. Lume emphasizes <strong>quiet-reverent + warm-tender</strong> and flags a high template/format confound; Mira emphasizes <strong>quiet-reverent + elegiac-wistful + subdued bright wonder</strong>. The combined prudent label is: <em>template-saturated reverent liminality, warm-tender in handling, with one strong elegiac outlier and recurrent blue-hour threshold imagery.</em></div></section>')

for r in sel:
    pid=r['pilot_id']; kimi = r['set']=='kimi_k2_6_focus'
    text=read_text(r['path'])
    html_parts.append(f'<article class="sample {"kimi" if kimi else ""}" id="s{pid}">')
    html_parts.append(f'<h2>{pid} — {esc(r["sample_id"])}</h2>')
    html_parts.append('<div class="meta">')
    for label in [r['set'], r['model'], r['lab'], r['condition'], f"{r['word_count']} words", r['production_frame'], r['narrator_stance'], 'legacy: '+r['legacy_top_climate_field']]:
        html_parts.append(f'<span class="pill">{esc(label)}</span>')
    html_parts.append('</div>')
    html_parts.append(f'<div class="sample-text">{esc(text.strip())}</div>')
    html_parts.append(sample_overlap(pid))
    html_parts.append('<div class="columns">')
    html_parts.append(f'<section class="coder mira"><h3>Mira ratings</h3><div class="coder-body">{rating_table(mg.get(pid,[]),"Mira")}</div></section>')
    html_parts.append(f'<section class="coder lume"><h3>Lume ratings</h3><div class="coder-body">{rating_table(lg.get(pid,[]),"Lume")}</div></section>')
    html_parts.append('</div></article>')

html_parts.append('<section class="summary" id="combined"><h2>Combined Kimi K2.6 evaluation</h2>')
html_parts.append('<p>These aggregates treat absent dimensions as zero across the 8 Kimi K2.6 samples. They are a pilot diagnostic, not final paper-grade scoring.</p>')
html_parts.append(agg_table())
html_parts.append('''<div class="callout"><strong>Combined synthesis:</strong> Kimi K2.6's ≤500-word freeflow samples show a very narrow contemplative template: repeated “particular/specific” openings, early-morning or twilight scenes, domestic hums/tea/coffee/light, and threshold-as-meaning theses. Within that template, both coders see a real narrator-handled climate rather than empty word salad: attentive, quiet, and caring toward small liminal moments. The safest joint label is <strong>stable but format-dominated reverent liminality</strong>, with <strong>warm-tender handling</strong> and <strong>elegiac shading concentrated most strongly in AC20</strong>. Mira would give more weight to subdued wonder and recurrent wistfulness; Lume would subtract more as base-register/template confound and foreground warmth.</div>''')
html_parts.append('<div class="collapse-grid"><section class="collapse"><h2>Mira collapse</h2>'+simple_md(mira_collapse)+'</section><section class="collapse"><h2>Lume collapse</h2>'+simple_md(lume_collapse)+'</section></div>')
html_parts.append('</section>')
html_parts.append('</div></body></html>')

out=OUT/'affective_pilot_review.html'
out.write_text('\n'.join(html_parts))
print(out)
