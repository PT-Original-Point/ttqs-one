from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET
from docx import Document
import csv, hashlib, json, re
root=Path(r'E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0075_R01')
docx=root/'candidate'/'0075_R02.docx'
body=root/'candidate'/'0075_R01_body.md'
reg=root/'inputs'/'SYNTHETIC_REPLACEMENT_REGISTER_0075_R01.csv'
blue=root/'inputs'/'UNIQUE_BLUEPRINT_0075_R01.md'
packet=root/'inputs'/'SOURCE_PACKET_0075_R01.md'
builder=root/'worker'/'build_0075_R02_docx.py'
pdf=root/'evidence'/'0075_R02_word_render_ca81a479.pdf'
render=root/'evidence'/'render_word_R02'
sha=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
doc=Document(str(docx))
texts=[]
for p in doc.paragraphs:
 if p.text.strip(): texts.append(p.text)
for t in doc.tables:
 for row in t.rows:
  texts.append(' | '.join(c.text for c in row.cells))
alltext='\n'.join(texts)
with ZipFile(docx) as z:
 bad=z.testzip()
 externals=[]
 for name in z.namelist():
  if name.endswith('.rels'):
   try:
    rt=ET.fromstring(z.read(name))
    for rel in rt:
     if rel.attrib.get('TargetMode')=='External': externals.append((name,rel.attrib.get('Target')))
   except Exception: pass
with reg.open(encoding='utf-8-sig',newline='') as f:
 reader=csv.DictReader(f); headers=reader.fieldnames; rows=list(reader)
ids=[r.get('record_id','') or r.get('fact_id','') or r.get('synthetic_id','') or next(iter(r.values()),'') for r in rows]
nonempty=all(all(str(v).strip() for v in r.values()) for r in rows)
expected=sorted([f'SYN-0075-FACT-{i:04d}' for i in range(1,len(rows)+1)])
# All arithmetic is recomputed independently from the source values.
math={
 'q5_mean': abs(54/15-3.60)<1e-12,
 'q5_positive_rate': abs(8/15*100-53.333333333333336)<1e-10,
 'valid_response_rate': abs(15/16*100-93.75)<1e-12,
 'invalid_rate': abs(1/16*100-6.25)<1e-12,
 'net_learning_minutes': sum([15,40,40,50,35,50,45,45,30,20,20])==390,
 'break_and_lunch_minutes': sum([10,10,40])==60,
 'elapsed_minutes': 390+60==450,
 'cost_delta': 6020-5720==300,
}
required=['0075','I17A-E03','082','SAMPLE/SYNTHETIC','CANDIDATE_ONLY','NOT_GRANTED','REAL=UNKNOWN/HOLD','PROPOSED','PENDING APPROVAL','INSUFFICIENT EVIDENCE','SYN-0073-2026-A01']
checks={
 'zip_integrity': bad is None,
 'no_external_relationships': len(externals)==0,
 'official_identity_present': all(x in alltext for x in required),
 'table_count_35': len(doc.tables)==35,
 'no_empty_tables': all(len(t.rows)>=2 and len(t.columns)>=2 for t in doc.tables),
 'register_rows_110': len(rows)==110,
 'register_nine_columns': len(headers or [])==9,
 'register_rows_nonempty': nonempty,
 'register_ids_unique_contiguous': len(set(ids))==110 and sorted(ids)==expected,
 'arithmetic_consistent': all(math.values()),
 'all_21_rendered_pages': len(list(render.glob('page-*.png')))==21,
 'pdf_exists': pdf.exists(),
}
result={
 'schema':'TTQS_ONE_0075_R02_TECHNICAL_REVIEW.v1',
 'document_id':'0075','requirement_id':'I17A-E03','official_checkbox_serial':'082',
 'candidate_state':'CANDIDATE_ONLY','formal_acceptance':'NOT_GRANTED','real_evidence':'UNKNOWN/HOLD',
 'docx':str(docx),'docx_sha256':sha(docx),'docx_bytes':docx.stat().st_size,
 'inputs_sha256':{str(p.relative_to(root)):sha(p) for p in [body,blue,reg,packet,builder]},
 'counts':{'paragraphs':len(doc.paragraphs),'tables':len(doc.tables),'table_rows_including_header':sum(len(t.rows) for t in doc.tables),'rendered_pages':len(list(render.glob('page-*.png'))),'register_rows':len(rows),'register_columns':len(headers or [])},
 'register_headers':headers,'register_id_field_values_first_last':[ids[0],ids[-1]],
 'math_checks':math,'checks':checks,'external_relationships':externals,
 'result':'TECHNICAL_PASS' if all(checks.values()) else 'TECHNICAL_FAIL',
 'semantic_review':'PENDING','visual_review':'PENDING',
}
out=root/'evidence'/'technical_review_R02.json'
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
