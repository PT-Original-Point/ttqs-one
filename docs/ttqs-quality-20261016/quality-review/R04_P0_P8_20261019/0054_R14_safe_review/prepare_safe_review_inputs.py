from pathlib import Path
import subprocess,hashlib,json,io
from zipfile import ZipFile
from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table
branch='origin/work/ttqs-one-document-quality-contract-20261016'
base='docs/ttqs-quality-20261016/quality-review/0054_R14/'
files={
 'candidate.docx':'candidate/0054_R14.docx',
 'official.txt':'inputs/official/official_checkbox_page4_excerpt.txt',
 'blueprint.json':'inputs/mapping/UNIQUE_BLUEPRINT_0054.json',
 'replacement_register.csv':'inputs/traceability/synthetic_replacement_register_R13.csv',
 'progress.json':'PROGRESS.json'}
out=Path(r'E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\R04_P0_P8_20261019\0054_R14_safe_review')
data={k:subprocess.check_output(['git','show',f'{branch}:{base}{v}']) for k,v in files.items()}
p=json.loads(data['progress.json'])
sha=hashlib.sha256(data['candidate.docx']).hexdigest()
assert sha==p['candidate_sha256']=='3d000e580b9cb1247fd984ebb0c8f5f817fce08ce7c368cc1799c95a111a979c',(sha,p['candidate_sha256'])
with ZipFile(io.BytesIO(data['candidate.docx'])) as z: assert z.testzip() is None
D=Document(io.BytesIO(data['candidate.docx']))
parts=[]
for n in D.element.body.iterchildren():
 if n.tag.endswith('}p'):
  t=Paragraph(n,D).text.strip()
  if t:parts.append(t)
 elif n.tag.endswith('}tbl'):
  t=Table(n,D);parts.append('[TABLE]')
  for row in t.rows:parts.append(' | '.join(' '.join(c.text.split()) for c in row.cells))
  parts.append('[/TABLE]')
text='\n'.join(parts)
(out/'0054_R14_exact_candidate_text.md').write_text(f'# Exact candidate text extraction\n\nDOCX SHA-256: `{sha}`\n\n{text}\n',encoding='utf-8')
for name,key in [('official_page4_extract.txt','official.txt'),('UNIQUE_BLUEPRINT_0054.json','blueprint.json'),('synthetic_replacement_register_R13.csv','replacement_register.csv')]: (out/name).write_bytes(data[key])
print(json.dumps({'candidate_sha256':sha,'candidate_bytes':len(data['candidate.docx']),'text_chars':len(text),'inputs':{k:hashlib.sha256(data[k]).hexdigest() for k in files if k!='candidate.docx'},'register_bytes':len(data['replacement_register.csv']),'table_count':len(D.tables)},ensure_ascii=True))
