from __future__ import annotations
import hashlib, json, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
root=Path.cwd()
label=sys.argv[1] if len(sys.argv)>1 else 'verified'
rev=subprocess.check_output(['git','rev-parse','FETCH_HEAD'],text=True).strip()
base=Path('docs/ttqs-quality-20261016/quality-review')
p0105=base/'0105_I18-E13_R01_20261022'; p0102=base/'0102_I18-E09_R06_20261021'; r09=base/'R09_WIN10_CLOSED_LOOP_20261022'
c0105=next(p for p in (p0105/'candidate').glob('*.docx') if p.name.endswith('_R07.docx'))
c0102=next(p for p in (p0102/'candidate').glob('*.docx') if p.name.endswith('_R06.docx'))
paths=[c0105.as_posix(),(p0105/'writer/opencode_writer_manuscript_0105_R07_raw.md').as_posix(),(p0105/'writer/opencode_writer_manuscript_0105_R07_release.md').as_posix(),(p0105/'evidence/synthetic_replacement_register_0105_R07.csv').as_posix(),(p0105/'evidence/technical_qa_0105_R07.json').as_posix(),(p0105/'evidence/independent_semantic_review_0105_R07_raw_response.md').as_posix(),(p0105/'evidence/independent_semantic_review_0105_R07_receipt.json').as_posix(),c0102.as_posix(),(p0102/'review/independent_semantic_review_0102_R06_R09_raw_response.md').as_posix(),(p0102/'review/independent_semantic_review_receipt_0102_R06_R09.json').as_posix(),(r09/'worker_24h_reconciliation_R09_20261022T1636.json').as_posix(),(r09/'r09_win10_live_state_readback_20261022.json').as_posix(),(r09/'r09_T01_T14_live_reconciliation_20261022.json').as_posix()]
items=[]
for rel in paths:
 local=(root/rel).read_bytes(); remote=subprocess.check_output(['git','show',f'{rev}:{rel}']); blob=subprocess.check_output(['git','rev-parse',f'{rev}:{rel}'],text=True).strip()
 items.append({'path':rel,'local_sha256':hashlib.sha256(local).hexdigest(),'remote_sha256':hashlib.sha256(remote).hexdigest(),'remote_git_blob':blob,'byte_identical':local==remote})
receipt={'receipt_id':'TTQS_ONE_R09_GITHUB_RAW_BYTE_READBACK','label':label,'observed_at_utc':datetime.now(timezone.utc).isoformat(),'remote_head':rev,'branch':'work/ttqs-one-document-quality-contract-20261016','pr':92,'items':items,'all_byte_identical':all(x['byte_identical'] for x in items),'note':'Read directly from fetched Git objects using git show; bytes compared before hashing. Candidate files selected by exact R07/R06 suffix.'}
out=r09/f'github_readback_{label}_{rev[:7]}.json'; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(receipt,ensure_ascii=True,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'remote_head':rev,'label':label,'all_byte_identical':receipt['all_byte_identical'],'items':len(items),'candidate_0105':items[0]['local_sha256'],'candidate_0102':items[7]['local_sha256'],'receipt':out.as_posix()},ensure_ascii=True))