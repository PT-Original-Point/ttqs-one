#!/usr/bin/env python
"""Deterministic, read-only audit of visible main-story DOCX run font-size floors."""
import argparse, hashlib, json, sys, zipfile
from pathlib import Path
from docx import Document
from docx.oxml.ns import qn
from lxml import etree

NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
VISIBLE=('w:t','w:delText','w:tab','w:br','w:instrText')
def size_pt(rpr):
    if rpr is None: return None
    node=rpr.find(qn('w:sz'))
    if node is None: node=rpr.find(qn('w:szCs'))
    try: return int(node.get(qn('w:val')))/2 if node is not None else None
    except (TypeError,ValueError): return None

def audit(path):
    path=Path(path); raw=path.read_bytes(); doc=Document(str(path))
    with zipfile.ZipFile(path) as z: styles=etree.fromstring(z.read('word/styles.xml'))
    by_id={s.get(qn('w:styleId')):s for s in styles.findall('w:style',NS)}
    defaults=styles.find('w:docDefaults/w:rPrDefault/w:rPr',NS)
    doc_default=size_pt(defaults)
    default_para=next((s.get(qn('w:styleId')) for s in styles.findall('w:style',NS) if s.get(qn('w:type'))=='paragraph' and s.get(qn('w:default')) in ('1','true')),None)
    default_char=next((s.get(qn('w:styleId')) for s in styles.findall('w:style',NS) if s.get(qn('w:type'))=='character' and s.get(qn('w:default')) in ('1','true')),None)
    def style_size(sid, seen=None):
        seen=set() if seen is None else seen
        if not sid or sid in seen: return None
        seen.add(sid); s=by_id.get(sid)
        if s is None: return None
        v=size_pt(s.find('w:rPr',NS))
        if v is not None: return v
        parent=s.find('w:basedOn',NS)
        return style_size(parent.get(qn('w:val')) if parent is not None else None,seen)
    body=[]; table=[]; unresolved={'body':0,'table':0}; below={'body':[],'table':[]}; source_counts={'body':{},'table':{}}
    seen_runs=set()
    for p in doc._element.body.iter(qn('w:p')):
        in_table=False; ancestor=p.getparent()
        while ancestor is not None:
            if ancestor.tag==qn('w:tc'): in_table=True; break
            if ancestor.tag==qn('w:body'): break
            ancestor=ancestor.getparent()
        bucket='table' if in_table else 'body'
        ppr=p.find(qn('w:pPr')); psid=None
        if ppr is not None:
            ps=ppr.find(qn('w:pStyle'))
            if ps is not None: psid=ps.get(qn('w:val'))
        psid=psid or default_para
        for run in p.iter(qn('w:r')):
            if run in seen_runs: continue
            seen_runs.add(run)
            if not any(run.find(qn(tag)) is not None for tag in VISIBLE): continue
            rp=run.find(qn('w:rPr')); val=size_pt(rp); src='run-direct'
            rs=rp.find(qn('w:rStyle')) if rp is not None else None
            if val is None and rs is not None:
                val=style_size(rs.get(qn('w:val'))); src='character-style'
            if val is None and default_char:
                val=style_size(default_char); src='default-character-style'
            if val is None and psid:
                val=style_size(psid); src='paragraph-style'
            if val is None and doc_default is not None:
                val=doc_default; src='doc-default'
            if val is None:
                unresolved[bucket]+=1; continue
            (table if bucket=='table' else body).append(val)
            source_counts[bucket][src]=source_counts[bucket].get(src,0)+1
            floor=9.5 if bucket=='table' else 10.5
            if val<floor: below[bucket].append(val)
    # Inspect only table styles actually applied (or the default table style when omitted).
    with zipfile.ZipFile(path) as z: document_xml=etree.fromstring(z.read('word/document.xml'))
    explicit={x.get(qn('w:val')) for x in document_xml.findall('.//w:tblPr/w:tblStyle',NS) if x.get(qn('w:val'))}
    default_table=next((s.get(qn('w:styleId')) for s in styles.findall('w:style',NS) if s.get(qn('w:type'))=='table' and s.get(qn('w:default')) in ('1','true')),None)
    applied=explicit or ({default_table} if default_table else set())
    table_style_overrides=[]; checked_table_styles=[]
    for sid in sorted(applied):
        current=sid; visited=set()
        while current and current not in visited:
            visited.add(current); st=by_id.get(current)
            if st is None: break
            checked_table_styles.append(current)
            for node in st.xpath('.//w:tblStylePr/w:rPr/w:sz | .//w:tblStylePr/w:rPr/w:szCs',namespaces=NS):
                table_style_overrides.append({'style_id':current,'node':node.tag.split('}')[-1],'half_points':node.get(qn('w:val'))})
            parent=st.find('w:basedOn',NS); current=parent.get(qn('w:val')) if parent is not None else None
    result={
      'artifact_path':str(path),'artifact_bytes':len(raw),'artifact_sha256':hashlib.sha256(raw).hexdigest(),
      'python_docx_version':__import__('docx').__version__,'visible_main_story_runs_only':True,
      'body_runs':len(body),'body_min_pt':min(body) if body else None,'body_max_pt':max(body) if body else None,'body_below_10_5_count':len(below['body']),'body_unresolved_count':unresolved['body'],'body_resolution_sources':source_counts['body'],
      'table_runs':len(table),'table_min_pt':min(table) if table else None,'table_max_pt':max(table) if table else None,'table_below_9_5_count':len(below['table']),'table_unresolved_count':unresolved['table'],'table_resolution_sources':source_counts['table'],
      'applied_table_style_ids':sorted(set(checked_table_styles)),'conditional_table_style_font_size_override_count':len(table_style_overrides),'conditional_table_style_font_size_overrides':table_style_overrides,
      'result':'PASS_SCOPED_FONT_FLOOR_ONLY' if body and table and not below['body'] and not below['table'] and not unresolved['body'] and not unresolved['table'] and not table_style_overrides else 'FAIL_OR_REVIEW_REQUIRED'
    }
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('docx',nargs='+'); args=ap.parse_args()
    results=[audit(p) for p in args.docx]
    print(json.dumps({'audit_version':'R12_FONT_FLOOR_1','results':results},ensure_ascii=False,sort_keys=True))
    sys.exit(0 if all(r['result']=='PASS_SCOPED_FONT_FLOOR_ONLY' for r in results) else 2)