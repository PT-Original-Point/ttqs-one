
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess, sys, time

work = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0012_I02-E03_LUNA_TEXT_DRAFT_R01_20261029\qa\W1_SEMANTIC_REVIEW_R06_CORRECTED_BINDING_20261030")
packet = work / "REVIEW_PACKET_R06_CORRECTED.md"
manifest_path = work / "review_input_manifest.json"
start_path = work / "DISPATCH_START.json"
terminal_path = work / "DISPATCH_TERMINAL.json"
stdout_path = work / "RAW_STDOUT.jsonl"
stderr_path = work / "RAW_STDERR.txt"
cli = Path(r"C:\Users\J\AppData\Roaming\npm\node_modules\@opencode\cli\bin\opencode.exe")
model = "opencode/glm-5.3-flash-free"
work_id = "TTQS-0012-W1-SEMANTIC-R06-GLM-20261030-02"
limit_seconds = 480

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def now():
    return datetime.now().astimezone().isoformat(timespec="seconds")

if not all(p.is_file() for p in (packet, manifest_path, cli)):
    raise SystemExit("Missing packet, manifest, or OpenCode executable")
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
packet_sha = sha(packet)
candidate = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0012_I02-E03_LUNA_TEXT_DRAFT_R01_20261029\candidate\0012_I02-E03_R06.docx")
candidate_sha = sha(candidate)
if packet_sha != manifest["review_packet_sha256"] or candidate_sha != manifest["candidate_sha256"]:
    raise SystemExit("Packet or candidate SHA changed after binding; refusing dispatch")
if start_path.exists() or terminal_path.exists():
    raise SystemExit("Work id already has dispatch evidence; refusing duplicate")
prompt = (
    "Independent semantic and usability review only. Read the complete attached packet and its extracted candidate text. "
    "Do not call tools, browse, edit files, or infer visual quality. Do not rely on any prior review. "
    "Review the exact candidate SHA and all six required areas in the packet. "
    "Return PASS, PARTIAL, or FAIL with concise evidence locators for every material finding; state limitations, "
    "and distinguish semantic review from visual QA and formal association acceptance. "
    "If the packet itself has a binding inconsistency, stop and report it instead of reviewing."
)
started = now()
start = {
    "project_id":"TTQS_ONE","work_id":work_id,"doc_id":"0012","requirement_id":"I02-E03",
    "stage":"READY_INDEPENDENT_SEMANTIC","requested_model":model,
    "actual_model":"UNKNOWN_PENDING_CLI_SESSION_METADATA",
    "cli_path":str(cli),"cli_version":"opencode v2.2.3",
    "agent":"plan","format":"json","process_window":"CREATE_NO_WINDOW",
    "packet_path":str(packet),"packet_sha256":packet_sha,
    "candidate_path":str(candidate),"candidate_sha256":candidate_sha,
    "started_at_local":started,"timeout_seconds":limit_seconds,
    "tools_allowed":False,"filesystem_write_allowed":False
}
start_path.write_text(json.dumps(start,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
cmd = [str(cli),"run","--model",model,"--agent","plan","--format","json","--title",work_id,"--file",str(packet),prompt]
env = os.environ.copy()
env["CI"] = "1"
env["NO_COLOR"] = "1"
creationflags = getattr(subprocess,"CREATE_NO_WINDOW",0)
t0 = time.monotonic()
with stdout_path.open("wb") as out, stderr_path.open("wb") as err:
    p = subprocess.Popen(cmd,cwd=r"E:\TTQS",stdin=subprocess.DEVNULL,stdout=out,stderr=err,env=env,creationflags=creationflags)
    start["pid"] = p.pid
    start_path.write_text(json.dumps(start,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"phase":"RUNNING","work_id":work_id,"pid":p.pid,"started_at_local":started,"timeout_seconds":limit_seconds}),flush=True)
    try:
        exit_code = p.wait(timeout=limit_seconds)
        timed_out = False
    except subprocess.TimeoutExpired:
        timed_out = True
        p.kill()
        exit_code = p.wait(timeout=20)
elapsed = round(time.monotonic()-t0,2)
stdout_sha = sha(stdout_path) if stdout_path.exists() else None
stderr_sha = sha(stderr_path) if stderr_path.exists() else None
stdout_text = stdout_path.read_text(encoding="utf-8",errors="replace") if stdout_path.exists() else ""
stderr_text = stderr_path.read_text(encoding="utf-8",errors="replace") if stderr_path.exists() else ""
actual = "UNKNOWN_UNCONFIRMED_BY_CLI_METADATA"
session_ids = []
model_metadata = []
for line in stdout_text.splitlines():
    try:
        obj = json.loads(line)
    except Exception:
        continue
    if isinstance(obj,dict):
        for k in ("sessionID","session_id","sessionId"):
            if isinstance(obj.get(k),str):
                session_ids.append(obj[k])
        for k in ("modelID","model_id","model"):
            if isinstance(obj.get(k),str) and ("/" in obj[k] or obj[k].startswith("glm")):
                model_metadata.append(obj[k])
if model_metadata:
    actual = sorted(set(model_metadata))
terminal = {
    "project_id":"TTQS_ONE","work_id":work_id,"doc_id":"0012","requirement_id":"I02-E03",
    "requested_model":model,"actual_model":actual,"status":"TIMEOUT" if timed_out else ("EXIT_0_RESPONSE_PENDING_REVIEW" if exit_code==0 else "CLI_FAILED"),
    "exit_code":exit_code,"timed_out":timed_out,"elapsed_seconds":elapsed,
    "pid":start.get("pid"),"started_at_local":started,"completed_at_local":now(),
    "packet_sha256":packet_sha,"candidate_sha256":candidate_sha,
    "stdout_path":str(stdout_path),"stdout_sha256":stdout_sha,"stdout_bytes":stdout_path.stat().st_size if stdout_path.exists() else 0,
    "stderr_path":str(stderr_path),"stderr_sha256":stderr_sha,"stderr_bytes":stderr_path.stat().st_size if stderr_path.exists() else 0,
    "session_ids":sorted(set(session_ids)),"model_metadata_observed":sorted(set(model_metadata)),
    "response_received":bool(stdout_text.strip()),"response_classification":"PENDING_MANUAL_CONTENT_AND_BINDING_REVIEW",
    "semantic_verdict":"PENDING","visual_verdict":"NOT_IN_SCOPE","formal_acceptance":"UNKNOWN_NOT_ACCEPTED",
    "stderr_tail":stderr_text[-2000:]
}
terminal_path.write_text(json.dumps(terminal,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"phase":"TERMINAL","work_id":work_id,"status":terminal["status"],"exit_code":exit_code,
 "elapsed_seconds":elapsed,"pid":terminal["pid"],"stdout_bytes":terminal["stdout_bytes"],
 "stdout_sha256":stdout_sha,"stderr_sha256":stderr_sha,"actual_model":actual,"session_ids":terminal["session_ids"]},ensure_ascii=False),flush=True)

