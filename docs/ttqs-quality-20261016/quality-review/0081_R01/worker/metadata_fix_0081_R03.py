from pathlib import Path
from docx import Document
import hashlib,json,sys,csv
r=Path(sys.argv[1]); c=r/'candidate';q=r/'qa'
src_doc=c/'0081_R02.docx';out_doc=c/'0081_R03.docx';src_body=c/'0081_R01_body.md';out_body=c/'0081_R03_body.md';src_csv=q/'SYNTHETIC_REPLACEMENT_REGISTER_0081_R02.csv';out_csv=q/'SYNTHETIC_REPLACEMENT_REGISTER_0081_R03.csv'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
body=src_body.read_text(encoding='utf-8')
repls=[('候選內容，尚未經本會核定，亦未經獨立語意審查','候選內容；尚未經本會核定；審查狀態以 exact-SHA 收據為準'),('候選內容（R01）','候選內容（R03）'),('SYNTHETIC_REPLACEMENT_REGISTER_0081_R01.csv','SYNTHETIC_REPLACEMENT_REGISTER_0081_R03.csv')]
for old,new in repls:
 if body.count(old)!=1:raise SystemExit(f'body target count mismatch: {old!r} {body.count(old)}')
 body=body.replace(old,new)
out_body.write_text(body,encoding='utf-8',newline='\n')
with src_csv.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f)); fields=list(rows[0].keys())
if len(rows)!=23:raise SystemExit('expected 23 register data rows')
for row in rows:
 if row['source_path']!='docs/ttqs-quality-20261016/quality-review/0081_R01/candidate/0081_R01_body.md':raise SystemExit('unexpected source_path in register')
 row['source_path']='docs/ttqs-quality-20261016/quality-review/0081_R01/candidate/0081_R03_body.md'
with out_csv.open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
d=Document(src_doc)
def replace_runs(p,old,new):
 full=''.join(x.text for x in p.runs);idx=full.find(old)
 if idx<0 or full.find(old,idx+1)>=0:raise SystemExit(f'DOCX target missing/nonunique: {old!r}')
 pos=0;start=None;end=None
 for i,run in enumerate(p.runs):
  nxt=pos+len(run.text)
  if start is None and idx<nxt:start=(i,idx-pos)
  if start is not None and idx+len(old)<=nxt:end=(i,idx+len(old)-pos);break
  pos=nxt
 if start is None or end is None:raise SystemExit('run mapping failed')
 i,a=start;j,b=end
 if i==j:p.runs[i].text=p.runs[i].text[:a]+new+p.runs[i].text[b:]
 else:
  p.runs[i].text=p.runs[i].text[:a]+new+p.runs[j].text[b:]
  for k in range(i+1,j+1):p.runs[k].text=''
count=0
for p in d.paragraphs:
 for old,new in [('候選內容，尚未經本會核定，亦未經獨立語意審查','候選內容；尚未經本會核定；審查狀態以 exact-SHA 收據為準'),('SYNTHETIC_REPLACEMENT_REGISTER_0081_R01.csv','SYNTHETIC_REPLACEMENT_REGISTER_0081_R03.csv')]:
  if old in p.text:replace_runs(p,old,new);count+=1
if count!=2:raise SystemExit(f'expected 2 paragraph edits, got {count}')
cell=d.tables[0].rows[1].cells[1];replace_runs(cell.paragraphs[0],'R01','R03')
d.save(out_doc)
# Confirm only intended textual changes relative to R02.
text='\n'.join([p.text for p in Document(out_doc).paragraphs]+[cell.text for t in Document(out_doc).tables for row in t.rows for cell in row.cells])
for s in ['尚未經本會核定；審查狀態以 exact-SHA 收據為準','候選內容（R03）','SYNTHETIC_REPLACEMENT_REGISTER_0081_R03.csv']:
 if s not in text:raise SystemExit('expected new text missing '+s)
receipt={'schema':'TTQS_ONE_0081_METADATA_CORRECTION_R03.v1','doc_id':'0081','source_candidate':'candidate/0081_R02.docx','source_sha256':sha(src_doc),'candidate':'candidate/0081_R03.docx','candidate_sha256':sha(out_doc),'source_body_sha256':sha(src_body),'body':'candidate/0081_R03_body.md','body_sha256':sha(out_body),'replacement_register':'qa/SYNTHETIC_REPLACEMENT_REGISTER_0081_R03.csv','replacement_register_rows':len(rows),'replacement_register_sha256':sha(out_csv),'changes':['Removed stale claim that independent semantic review had not happened; points readers to exact-SHA receipts while preserving CANDIDATE_ONLY and NOT_GRANTED.','Updated document revision label R01 to R03 in the status table.','Updated register filename to R03 and all 23 CSV source paths to the R03 body.'],'content_scope':'administrative metadata only; scenario facts and substantive body unchanged','candidate_state':'CANDIDATE_ONLY','real_status':'UNKNOWN/HOLD','formal_acceptance':'NOT_GRANTED','semantic_review':'PENDING_R03_EXACT_SHA_DELTA'}
(q/'metadata_correction_R03.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'candidate_sha256':receipt['candidate_sha256'],'body_sha256':receipt['body_sha256'],'register_sha256':receipt['replacement_register_sha256'],'rows':len(rows),'changes':receipt['changes']},ensure_ascii=True))
