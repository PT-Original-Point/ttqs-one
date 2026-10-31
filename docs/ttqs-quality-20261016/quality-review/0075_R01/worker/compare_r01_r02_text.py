from pathlib import Path
from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table
import hashlib
base=Path(r'E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0075_R01')
def extract(name):
 d=Document(str(base/'candidate'/name)); out=[]
 for ch in d.element.body.iterchildren():
  t=ch.tag.rsplit('}',1)[-1]
  if t=='p': out.append(Paragraph(ch,d).text)
  elif t=='tbl': out.extend('|'.join(c.text for c in row.cells) for row in Table(ch,d).rows)
 return '\n'.join(out)
a=extract('0075_R01.docx'); b=extract('0075_R02.docx')
print('text_equal='+str(a==b));print('R01_extracted_sha256='+hashlib.sha256(a.encode()).hexdigest());print('R02_extracted_sha256='+hashlib.sha256(b.encode()).hexdigest());print('R01_docx_sha256='+hashlib.sha256((base/'candidate/0075_R01.docx').read_bytes()).hexdigest());print('R02_docx_sha256='+hashlib.sha256((base/'candidate/0075_R02.docx').read_bytes()).hexdigest())
