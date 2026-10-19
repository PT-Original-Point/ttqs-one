#!/usr/bin/env python3
import hashlib,json
from pathlib import Path

base=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
receipt_path=base/'evidence'/'build_receipt_R01.json'
r=json.loads(receipt_path.read_text(encoding='utf-8'))
pre=base/'candidate'/'0083_R02_pre_watermark.docx'
final=base/'candidate'/'0083_R02.docx'
body=base/'candidate'/'0083_R02_body.md'
r.update({'revision':'R02','body_path':str(body),'body_sha256':sha(body),'pre_watermark_docx_path':str(pre),'pre_watermark_docx_sha256':sha(pre),'docx_path':str(final),'docx_sha256':sha(final),'docx_bytes':final.stat().st_size,'watermark':'SAMPLE / SYNTHETIC; added with packaged watermark_add.py; shape located in header1.xml','acceptance_status':'CANDIDATE_NOT_FORMALLY_ACCEPTED','real_evidence_status':'UNKNOWN_HOLD'})
receipt_path.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(r,ensure_ascii=True))
