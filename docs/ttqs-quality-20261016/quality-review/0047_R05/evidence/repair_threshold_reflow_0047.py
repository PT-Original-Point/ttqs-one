from __future__ import annotations
import hashlib, json, shutil
from pathlib import Path
from docx import Document
from docx.text.paragraph import Paragraph
from docx.oxml import OxmlElement
from docx.shared import Pt

pkg=Path(__file__).resolve().parents[1]
parent=pkg.parent/'0047_R04'/'candidate'/'0047_R04.docx'
out=pkg/'candidate'/'0047_R05.docx'
if out.exists(): raise FileExistsError(out)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def norm_non_target(doc, target_tbl=None):
    parts=[]
    for child in doc._body._body.iterchildren():
        if child.tag.endswith('}tbl'):
            if child is target_tbl: continue
            for row in child.iterchildren():
                if row.tag.endswith('}tr'):
                    cells=[]
                    for cell in row.iterchildren():
                        if cell.tag.endswith('}tc'):
                            cells.append(''.join(t.text or '' for t in cell.iter() if t.tag.endswith('}t')))
                    parts.append(('tblrow',tuple(cells)))
        elif child.tag.endswith('}p'):
            parts.append(('p',''.join(t.text or '' for t in child.iter() if t.tag.endswith('}t'))))
    return parts

if not parent.is_file(): raise FileNotFoundError(parent)
parent_sha=sha(parent)
shutil.copy2(parent,out)
doc=Document(out)
targets=[]
for table in doc.tables:
    if len(table.rows)==5 and len(table.columns)==2 and table.cell(0,0).text.strip()=='\u5224\u8b80\u689d\u4ef6' and table.cell(0,1).text.strip()=='\u5224\u65b7\u6a19\u6e96':
        targets.append(table)
if len(targets)!=1: raise AssertionError(f'expected one threshold table, got {len(targets)}')
t=targets[0]
rows=[[c.text.strip() for c in row.cells] for row in t.rows]
expected=[
 ['\u52a0\u6b0a\u5206\u6578\u4f4e\u65bc3.00','\u512a\u5148\u88dc\u5f37'],
 ['\u52a0\u6b0a\u5206\u6578\u81f3\u5c113.00\u4f46\u4f4e\u65bc4.00','\u9700\u6539\u5584'],
 ['\u52a0\u6b0a\u5206\u6578\u81f3\u5c114.00\u4f46\u5c65\u7d04\u6aa2\u6838\u672a\u5168\u6578\u5b8c\u6210','\u4ecd\u5217\u9700\u6539\u5584\uff1b\u5148\u88dc\u9f4a\u7f3a\u9805\uff0c\u518d\u7531\u7ba1\u7406\u6b0a\u8cac\u89d2\u8272\u8986\u6838'],
 ['\u52a0\u6b0a\u5206\u6578\u81f3\u5c114.00\u4e14\u56db\u9805\u6aa2\u6838\u5168\u6578\u5b8c\u6210','\u9054\u793a\u7bc4\u6aa2\u8996\u9580\u6abb']]
if rows[0] != ['\u5224\u8b80\u689d\u4ef6','\u5224\u65b7\u6a19\u6e96'] or rows[1:] != expected:
    raise AssertionError('threshold table values/text differ from the verified R04 values')
parent_doc=Document(parent)
parent_non_target=norm_non_target(parent_doc)
heading_el=t._tbl.getprevious()
if heading_el is None or not heading_el.tag.endswith('}p'):
    raise AssertionError('threshold table is not directly preceded by its section heading')
heading=Paragraph(heading_el,doc._body)
if heading.text.strip()!='\u793a\u7bc4\u5224\u8b80\u9580\u6abb':
    raise AssertionError(f'unexpected preceding heading: {heading.text!r}')
anchor=heading._p
bullets=[]
for condition,result in rows[1:]:
    p=OxmlElement('w:p')
    anchor.addnext(p)
    para=Paragraph(p,heading._parent)
    para.style=doc.styles['List Bullet']
    para.paragraph_format.keep_together=True
    para.paragraph_format.keep_with_next=False
    para.paragraph_format.space_before=Pt(0)
    para.paragraph_format.space_after=Pt(2)
    para.paragraph_format.line_spacing=1.0
    run=para.add_run(f'{condition}\uff1a{result}')
    run.font.size=Pt(10.5)
    bullets.append(para.text)
    anchor=p
# The table is replaced by semantically identical, readable list items.
t._tbl.getparent().remove(t._tbl)
doc.core_properties.comments='R05: presentation-only reflow of the four redundant sample interpretation rows into a compact bullet list; thresholds, predicates, outcomes, and all other body text/table values are unchanged.'
doc.save(out)
check=Document(out)
if norm_non_target(check) != parent_non_target:
    raise AssertionError('Non-target body text or table rows changed')
if bullets != [f'{a}\uff1a{b}' for a,b in expected]: raise AssertionError('bullet transcription mismatch')
if any(table.rows and table.cell(0,0).text.strip()=='\u5224\u8b80\u689d\u4ef6' for table in check.tables): raise AssertionError('threshold table remains')
if len([p for p in check.paragraphs if p.text.strip().startswith('\u52a0\u6b0a\u5206\u6578')]) != 4: raise AssertionError('four threshold bullets not present')
receipt={
 'doc_id':'0047','revision':'R05','status':'CANDIDATE_ONLY',
 'change_scope':'PRESENTATION_ONLY_THRESHOLD_TABLE_TO_BULLETS',
 'parent_candidate':'0047_R04/candidate/0047_R04.docx','parent_sha256':parent_sha,
 'candidate':'0047_R05/candidate/0047_R05.docx','candidate_sha256':sha(out),
 'official_mapping':{'requirement_id':'I10-E02','official_checkbox_sequence':48,'official_source_box':'P03-B09'},
 'threshold_content_preserved':True,'all_non_target_text_and_table_rows_unchanged':True,
 'threshold_rows_as_bullets':bullets,
 'synthetic_status':'ALL_CASE_DATA_SAMPLE_SYNTHETIC; NO REAL ASSOCIATION RECORDS OR APPROVALS CLAIMED',
 'independent_semantic_review':'PENDING exact R05 SHA',
 'visual_review':'PENDING full-page render and direct page inspection'
}
(pkg/'evidence'/'R05_LAYOUT_REPAIR_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=True,indent=2))
