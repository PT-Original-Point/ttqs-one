#!/usr/bin/env python3
import hashlib, json, subprocess
from pathlib import Path

repo=Path(__file__).resolve().parents[5]
ref='refs/remotes/origin/work/ttqs-one-document-quality-contract-20261016'
paths={
 'SRC-157':'docs/ttqs-quality-20261016/quality-review/0077_R01/inputs/upstream_snapshots/03_157_CHECKBOX_BLUEPRINTS.md',
 'SRC-P6':'docs/ttqs-quality-20261016/quality-review/0078_R01/evidence/official_evidence_table_page6-6.png',
 'SRC-MIS':'docs/ttqs-quality-20261016/quality-review/0077_R01/inputs/upstream_snapshots/01_HUMAN_MISSION_AND_ACCEPTANCE.md',
 'SRC-GEN':'docs/ttqs-quality-20261016/quality-review/0077_R01/inputs/upstream_snapshots/02_GENRE_WRITING_MANUAL.md',
 'SRC-0082C':'docs/ttqs-quality-20261016/quality-review/0082_R01/candidate/0082_R08.docx',
 'SRC-0082B':'docs/ttqs-quality-20261016/quality-review/0082_R01/inputs/UNIQUE_BLUEPRINT_0082_R02.md',
}
entries=[]
for key,path in paths.items():
    local=(repo/path).read_bytes()
    blob=subprocess.check_output(['git','rev-parse',f'{ref}:{path}'],cwd=repo,text=True).strip()
    remote=subprocess.check_output(['git','cat-file','blob',f'{ref}:{path}'],cwd=repo)
    local_sha=hashlib.sha256(local).hexdigest()
    remote_sha=hashlib.sha256(remote).hexdigest()
    entries.append({'source_id':key,'path':path,'git_blob':blob,'local_sha256':local_sha,'remote_sha256':remote_sha,'local_bytes':len(local),'remote_bytes':len(remote),'exact_match':local==remote})
    if local!=remote: raise SystemExit(f"Remote source mismatch: {key}")
more={
 'SRC-083BP':'docs/ttqs-quality-20261016/quality-review/0083_R01/inputs/UNIQUE_BLUEPRINT_0083_R03.md',
 'SRC-083PKT':'docs/ttqs-quality-20261016/quality-review/0083_R01/inputs/SOURCE_PACKET_0083_R01.md',
}
for key,path in more.items():
    b=(repo/path).read_bytes()
    entries.append({'source_id':key,'path':path,'git_blob':'PENDING_UNTIL_SYNC','local_sha256':hashlib.sha256(b).hexdigest(),'remote_sha256':'PENDING_UNTIL_SYNC','local_bytes':len(b),'remote_bytes':None,'exact_match':None})
receipt={'schema':'ttqs-0083-source-hash-readback-v1','remote_ref':ref,'remote_head':subprocess.check_output(['git','rev-parse',ref],cwd=repo,text=True).strip(),'entries':entries,'result':'PASS_REMOTE_SOURCE_BYTES_MATCH_LOCAL_FOR_SIX'}
out=repo/'docs/ttqs-quality-20261016/quality-review/0083_R01/evidence/source_hash_readback_R01.json'
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=True))
