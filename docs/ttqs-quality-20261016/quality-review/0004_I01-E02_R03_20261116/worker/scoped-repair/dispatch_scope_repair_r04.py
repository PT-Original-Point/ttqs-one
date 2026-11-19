from pathlib import Path
import subprocess, hashlib, json, datetime, os, shutil, sys

rt=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME")
base=rt/"WORK"/"QUALITY_REBUILD_20261016"
prep=base/"0004_I01-E02_SOURCE_PREP_R03_20261116"
oldw=base/"0004_I01-E02_WRITER_R03_20261116"/"worker"
worker=prep/"worker"
worker.mkdir(parents=True, exist_ok=True)

inputs={
 "prior_worker_manuscript":oldw/"worker_manuscript_raw.md",
 "source_packet":prep/"SOURCE_PACKET_0004_I01-E02_R02.md",
 "unique_blueprint":prep/"UNIQUE_BLUEPRINT_0004_I01-E02_R02.md",
 "replacement_register_R03":prep/"SYNTHETIC_REPLACEMENT_REGISTER_PLAN_0004_R03.csv",
 "source_prep_manifest_R03":prep/"SOURCE_PREP_MANIFEST_0004_R03.json",
 "source_prep_qa_R03":prep/"SOURCE_PREP_QA_R03.json"
}
def sha_bytes(b): return hashlib.sha256(b).hexdigest()
def sha(p): return sha_bytes(p.read_bytes())
request=worker/"SCOPED_REPAIR_REQUEST_R04.md"
request_text="""TTQS ONE bounded manuscript repair assignment
work_id=TTQS-0004-I01-E02-SCOPED-REPAIR-R04-20261116
doc_id=0004
requirement_id=I01-E02
role=TEXT_ONLY_SCOPED_WRITER
requested_route=opencode/beam-free
prior manuscript is your own previous output; repair only this same deliverable, do not use any other deliverable body.
Return the entire corrected Traditional Chinese Markdown body only. No preface, review verdict, self-certification, PASS claim, or commentary.

Controlling source bundle:
- SOURCE_PACKET and UNIQUE_BLUEPRINT define official scope and genre.
- SOURCE_PREP_MANIFEST_R03 and SOURCE_PREP_QA_R03 control the corrected synthetic register.
- Corrected register R03 changes exactly one value from R02: SYN-0004-U004-INVITE-DATE = 2026-10-29. It must not precede U004 screen date 2026-10-29 and is on batch close 2026-10-29.
- Preserve all other 83 fact rows, values, calculations, boundaries, and unknown-real facts.

Required bounded repairs to the prior manuscript:
1. Front control card: remove source-preparation QA status/count and any PASS language. Set artifact status to CANDIDATE DOCX; content SAMPLE/SYNTHETIC; formal acceptance NOT GRANTED; real execution UNKNOWN; independent semantic review pending. Do not self-review.
2. Correct U004 invitation date everywhere to 2026-10-29 and cite SYN-0004-U004-INVITE-DATE.
3. Make the sequential procedure table no wider than 5 columns and add exact register fact IDs adjacent to each role/date/count/control claim. Keep every procedure labelled SAMPLE workflow proposal pending authorized adoption.
4. Replace the 10-column invitation log with a compact 4- or 5-column log. Keep every case U001-U005, exact dates/statuses/decisions, and exact fact IDs; do not omit the invite date chronology or the ineligible/not-invited distinction.
5. In the handoff to 0005, explicitly list all ten counts with labels and exact IDs: screened 5; ineligible 1; eligible invitations 4; unique returns 2; valid 1; invalid 1; refusals 1; no response 1; duplicate extras 1; raw receipt events 3. Also carry only valid sample n=1 and the valid anonymous response reference; do no demand analysis.
6. Replace pseudo-ID wildcards SYN-0004-COUNT-*, SYN-0004-FLOW-*, SYN-0004-RATE-* with descriptive phrases and exact IDs only. Keep the complete exact ten count IDs, four flow IDs, and four rate IDs where relevant. Never present a wildcard as a fact ID.
7. Replace the old section claiming all facts are cited/covered with a non-self-certifying candidate/authority boundary, or remove it.
8. Update hash source table and attachment index: packet and Blueprint remain R02 with their original hashes; register is R03 with the exact provided SHA; cite the exact R03 source-prep manifest and QA hashes from attached files. No stale R02 register/manifest/QA hash may appear as current.
9. Replace “verification_rule（register）” with the actual exact rule ID RULE-0004-ELIGIBILITY-01 and relevant exact flow IDs.
10. Preserve substantive content and all other source-bound facts; no new case facts, no new sample values, no real-world claims, no TODO/placeholders, no copied 0003 questions/answers, no 0005 demand analysis. Keep front matter readable. Keep section tables at five columns maximum where feasible.

No tools, shell, file writes, browser, Computer Use, or external lookups. Use only attached bounded input bundle. Stop after one complete revised body.
"""
request.write_text(request_text,encoding="utf-8")
bundle=worker/"WORKER_INPUT_SCOPE_REPAIR_R04.md"
parts=["# TTQS ONE bounded scope-repair input bundle\n",request_text+"\n"]
for name,p in inputs.items():
    data=p.read_bytes()
    try: content=data.decode("utf-8-sig")
    except UnicodeDecodeError: content=f"[binary source omitted; sha256={sha(p)}]"
    parts.append(f"\n--- BEGIN {name} | SHA256={sha(p)} ---\n{content}\n--- END {name} ---\n")
bundle.write_text("".join(parts),encoding="utf-8")
exe=shutil.which("opencode")
if not exe: raise SystemExit("opencode executable not found on PATH")
out=worker/"raw_stdout_r04.jsonl"; err=worker/"raw_stderr_r04.txt"
started=datetime.datetime.now(datetime.timezone.utc)
args=[exe,"run","--model","opencode/beam-free","--format","json","--title","TTQS-0004-I01-E02-SCOPED-REPAIR-R04-20261116","--file",str(bundle),"Return the complete revised Markdown body requested in the attached bounded input. Use no tools."]
proc=None; code=None; timeout=False; stdout=b""; stderr=b""; status="UNKNOWN"
try:
    proc=subprocess.Popen(args,cwd=str(worker),stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,creationflags=getattr(subprocess,"CREATE_NO_WINDOW",0x08000000))
    try: stdout,stderr=proc.communicate(timeout=900); code=proc.returncode; status="EXITED"
    except subprocess.TimeoutExpired:
        timeout=True; proc.kill(); stdout,stderr=proc.communicate(); code=proc.returncode; status="TIMEOUT_KILLED"
except Exception as e:
    stderr=(type(e).__name__+": "+str(e)).encode(); status="LAUNCH_ERROR"
ended=datetime.datetime.now(datetime.timezone.utc)
out.write_bytes(stdout); err.write_bytes(stderr)
text_parts=[]; session_ids=[]; terminal=[]
for line in stdout.decode("utf-8","replace").splitlines():
    try: obj=json.loads(line)
    except Exception: continue
    if obj.get("sessionID") and obj["sessionID"] not in session_ids: session_ids.append(obj["sessionID"])
    typ=obj.get("type"); part=obj.get("part") or {}
    if typ=="text" and isinstance(part.get("text"),str): text_parts.append(part["text"])
    if typ=="step_finish": terminal.append(obj)
body="".join(text_parts)
body_path=worker/"worker_manuscript_repaired_raw.md"
complete=(status=="EXITED" and code==0 and len(body.strip())>=10000 and "0004" in body and "SYN-0004-U004-INVITE-DATE" in body)
if body.strip(): body_path.write_text(body,encoding="utf-8")
last=terminal[-1] if terminal else {}
receipt={
 "schema":"ttqs-one-worker-return-v1","work_id":"TTQS-0004-I01-E02-SCOPED-REPAIR-R04-20261116",
 "doc_id":"0004","requirement_id":"I01-E02","worker":"OpenCode v2 CLI","cli_version":"2.2.5",
 "requested_model":"opencode/beam-free","actual_serving_model":"UNKNOWN",
 "input_files":{k:{"path":str(p),"sha256":sha(p),"bytes":p.stat().st_size} for k,p in inputs.items()},
 "request_sha256":sha(request),"bundle_sha256":sha(bundle),
 "pid":proc.pid if proc else None,"session_ids":session_ids,"started_utc":started.isoformat(),"ended_utc":ended.isoformat(),
 "duration_seconds":round((ended-started).total_seconds(),3),"process_status":status,"exit_code":code,"timeout":timeout,
 "stdout_path":str(out),"stdout_bytes":len(stdout),"stdout_sha256":sha(out),
 "stderr_path":str(err),"stderr_bytes":len(stderr),"stderr_sha256":sha(err),
 "terminal_event":last,"response_path":str(body_path) if body_path.exists() else None,
 "response_chars":len(body),"response_sha256":sha(body_path) if body_path.exists() else None,
 "complete_body_recovered":complete,"candidate_adopted":False,"model_cost_from_worker_terminal":last.get("cost","UNKNOWN"),
 "token_usage_from_worker_terminal":(last.get("tokens") or "UNKNOWN"),
 "http_429_detected":("429" in stdout.decode("utf-8","replace") or "429" in stderr.decode("utf-8","replace")),
 "retry_after_ms":None
}
receipt_path=worker/"WORKER_RETURN_RECEIPT_R04.json"
receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"work_id":receipt["work_id"],"status":status,"exit_code":code,"pid":receipt["pid"],"session_ids":session_ids,"duration_seconds":receipt["duration_seconds"],"response_chars":len(body),"response_sha256":receipt["response_sha256"],"complete_body_recovered":complete,"cost":receipt["model_cost_from_worker_terminal"],"tokens":receipt["token_usage_from_worker_terminal"],"stderr":stderr.decode("utf-8","replace")[:1200]},ensure_ascii=False,indent=2))
if not complete: sys.exit(2)
