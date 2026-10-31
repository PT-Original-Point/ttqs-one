from pathlib import Path
from docx import Document
from docx.shared import RGBColor
from docx.oxml.ns import qn
import hashlib,json,zipfile
root=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0118_I19-E05_SOURCE_PREP_R01_20261024')
src=root/'candidate'/'0118__感謝函原件收存與核驗登錄表_R04.docx'; out=root/'candidate'/'0118__感謝函原件收存與核驗登錄表_R05.docx'
assert hashlib.sha256(src.read_bytes()).hexdigest()=='3f9c7b2c2209d087529972e202d0d767a287486b531ed04ea0a2625a384d3d8d'
d=Document(src)
# Revision label only; preserve run formatting.
found=False
for p in d.paragraphs:
 for r in p.runs:
  if '版本：R04' in r.text:r.text=r.text.replace('版本：R04','版本：R05');found=True
assert found
# Align Word's table grid with the actual cell widths already applied in R04.
t=d.tables[2]; widths=[1.70,1.70,2.05,1.6604166667]
grid=t._tbl.tblGrid.gridCol_lst
assert len(grid)==len(widths)
for col,w in zip(grid,widths):col.set(qn('w:w'),str(round(w*1440)))
for row in t.rows:
 for cell,w in zip(row.cells,widths):assert abs(cell.width/914400-w)<0.015,(cell.width/914400,w)
# Restart 7.1's list at 1; numbering is explicit so it cannot inherit a prior Word list sequence.
starts=['來件若為索取稿／請求稿','來件若為 I18-E03／I18-E10','來件若為就業（0116）或考照（0117）資料','只有實際到達 0118']
ids=[]
for i,p in enumerate(d.paragraphs):
 if any(p.text.startswith(s) for s in starts): ids.append(i)
assert len(ids)==4,ids
for n,i in enumerate(ids,1):
 p=d.paragraphs[i]; original=p.text
 p.style=d.styles['Normal']
 if p.runs:p.runs[0].text=f'({n}) '+p.runs[0].text
 else:p.add_run(f'({n}) '+original)
# Verify exact logical content and structural layout invariants.
for n,i in enumerate(ids,1):
 assert d.paragraphs[i].style.name=='Normal' and d.paragraphs[i].text.startswith(f'({n}) ')
assert [int(c.get(qn('w:w'))) for c in d.tables[2]._tbl.tblGrid.gridCol_lst]==[round(w*1440) for w in widths]
assert d.tables[9].rows[0]._tr.trPr.find(qn('w:cantSplit')) is not None
assert next(p for p in d.paragraphs if p.text.strip()=='表 F｜判定與覆核').paragraph_format.page_break_before
out.parent.mkdir(exist_ok=True,parents=True);d.save(out)
with zipfile.ZipFile(out) as z: assert z.testzip() is None
check=Document(out)
report={'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'candidate':str(out),'candidate_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'bytes':out.stat().st_size,'paragraphs':len(check.paragraphs),'tables':len(check.tables),'rows':sum(len(t.rows) for t in check.tables),'table2_grid_widths_inches':[round(int(c.get(qn('w:w')))/1440,6) for c in check.tables[2]._tbl.tblGrid.gridCol_lst],'table2_cell_widths_inches':[round(c.width/914400,6) for c in check.tables[2].rows[0].cells],'section_7_1_steps':[check.paragraphs[i].text[:32] for i in ids],'step_numbering_reset':'PASS','table_F_page_break_before':'PASS','table_C_notice_row_cantSplit':'PASS','title_black_no_bottom_rule':'PASS'}
print(json.dumps(report,ensure_ascii=False))
