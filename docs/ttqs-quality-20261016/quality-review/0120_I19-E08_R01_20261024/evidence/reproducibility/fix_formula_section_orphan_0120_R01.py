from pathlib import Path
from docx import Document
import hashlib
root=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0120_I19-E08_SOURCE_PREP_R01_20261024")
doc=next((root/'candidate_R01').glob('*.docx'))
before=hashlib.sha256(doc.read_bytes()).hexdigest()
d=Document(doc)
matches=[p for p in d.paragraphs if p.text.strip().startswith('八、REAL-FORM-06')]
if len(matches)!=1: raise SystemExit(f'Expected one formula heading, found {len(matches)}')
p=matches[0]
if p.paragraph_format.page_break_before:
 print('NO_CHANGE already has page break',before)
else:
 p.paragraph_format.page_break_before=True
 d.save(doc)
 after=hashlib.sha256(doc.read_bytes()).hexdigest()
 print('FIXED targeted heading page break', 'before_sha256='+before,'after_sha256='+after)
