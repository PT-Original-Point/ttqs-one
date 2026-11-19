from pathlib import Path
import hashlib,json,subprocess,datetime,sys
REPO=Path(r"E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016")
ROOT=REPO/"docs/ttqs-quality-20261016/quality-review/0038_R03"
BRANCH="work/ttqs-one-document-quality-contract-20261016"
REMOTE_REF=f"refs/remotes/origin/{BRANCH}"
WRITE_RECEIPT="--write-receipt" in sys.argv
run=lambda *args:subprocess.check_output(args,cwd=REPO).decode("utf-8").strip()
remote_line=run("git","ls-remote","origin",f"refs/heads/{BRANCH}")
remote_head=remote_line.split()[0]
subprocess.check_call(["git","fetch","origin",f"+refs/heads/{BRANCH}:{REMOTE_REF}"],cwd=REPO)
fetched_head=run("git","rev-parse",REMOTE_REF)
if fetched_head!=remote_head:raise SystemExit(f"Remote ref changed during fetch: ls-remote={remote_head}; fetched={fetched_head}")
manifest_path=ROOT/"evidence/manifest.json"
manifest=json.loads(manifest_path.read_text(encoding="utf-8"))
results=[]
for item in manifest["artifacts"]:
 path=item["path"];local=ROOT/path;expected=item["sha256"]
 if not local.is_file():raise SystemExit(f"Missing local file: {path}")
 blob=run("git","rev-parse",f"{fetched_head}:docs/ttqs-quality-20261016/quality-review/0038_R03/{path}")
 remote_bytes=subprocess.check_output(["git","cat-file","blob",blob],cwd=REPO)
 local_bytes=local.read_bytes();local_sha=hashlib.sha256(local_bytes).hexdigest();remote_sha=hashlib.sha256(remote_bytes).hexdigest()
 ok=len(local_bytes)==item["bytes"]==len(remote_bytes) and expected==local_sha==remote_sha
 results.append({"path":path,"git_blob_sha1":blob,"bytes":len(remote_bytes),"manifest_sha256":expected,"local_sha256":local_sha,"remote_readback_sha256":remote_sha,"status":"PASS" if ok else "FAIL"})
 if not ok:raise SystemExit(json.dumps({"path":path,"expected":expected,"local":local_sha,"remote":remote_sha,"expected_bytes":item["bytes"],"local_bytes":len(local_bytes),"remote_bytes":len(remote_bytes)},indent=2))
manifest_blob=run("git","rev-parse",f"{fetched_head}:docs/ttqs-quality-20261016/quality-review/0038_R03/evidence/manifest.json")
remote_manifest=subprocess.check_output(["git","cat-file","blob",manifest_blob],cwd=REPO)
manifest_sha=hashlib.sha256(manifest_path.read_bytes()).hexdigest();remote_manifest_sha=hashlib.sha256(remote_manifest).hexdigest()
if manifest_sha!=remote_manifest_sha:raise SystemExit("Manifest remote readback mismatch")
receipt={"project_id":"TTQS_ONE","doc_id":"0038","requirement_id":"I08-E02","official_checkbox_sequence":"039","candidate":"0038_R03","candidate_sha256":manifest["candidate_sha256"],"status":"PASS_EXACT_REMOTE_READBACK","repository":"PT-Original-Point/ttqs-one","branch":BRANCH,"remote_head_sha":remote_head,"fetched_remote_head_sha":fetched_head,"verified_at":datetime.datetime.now().astimezone().isoformat(timespec="seconds"),"method":"Fresh git ls-remote + git fetch of named GitHub branch; recomputed SHA-256 from each remote Git blob via git cat-file; exact byte count and manifest SHA compared to local.","manifest":{"path":"evidence/manifest.json","git_blob_sha1":manifest_blob,"bytes":len(remote_manifest),"local_sha256":manifest_sha,"remote_readback_sha256":remote_manifest_sha,"status":"PASS"},"artifact_count":len(results),"verified_artifact_count":sum(x["status"]=="PASS" for x in results),"artifacts":results}
if WRITE_RECEIPT:
 out=ROOT/"evidence/qa/remote_readback_R03.json"
 out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"remote_head_sha":remote_head,"artifact_count":len(results),"verified":receipt["verified_artifact_count"],"manifest_sha256":manifest_sha,"candidate_sha256":manifest["candidate_sha256"],"write_receipt":WRITE_RECEIPT},ensure_ascii=False,indent=2))
