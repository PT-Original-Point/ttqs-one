import datetime, hashlib, json, os, pathlib, subprocess, sys, time

ROOT = pathlib.Path(__file__).resolve().parent
MANIFEST = ROOT / "DISPATCH_MANIFEST_R10.json"
PACKET = ROOT / "INPUT_PACKET_GEMINI_R10.md"
CWD = ROOT / "TEXT_INPUT"
EXE = pathlib.Path(r"C:\Users\J\AppData\Local\agy\bin\agy.exe")
manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
packet_bytes = PACKET.read_bytes()
packet_sha = hashlib.sha256(packet_bytes).hexdigest()
if packet_sha != manifest["input_packet_sha256"]:
    raise SystemExit("INPUT_PACKET_SHA_MISMATCH")
if packet_bytes.startswith(b"\xef\xbb\xbf"):
    raise SystemExit("INPUT_PACKET_HAS_UTF8_BOM")
if not EXE.is_file():
    raise SystemExit("AGY_EXE_MISSING")
if any(CWD.iterdir()):
    raise SystemExit("TEXT_INPUT_DIR_NOT_EMPTY")
exe_sha = hashlib.sha256(EXE.read_bytes()).hexdigest()
args = [
    str(EXE), "--input-format", "stream-json", "--output-format", "stream-json",
    "--model", "gemini-3.8-flash-high", "--effort", "high", "--mode", "plan",
    "--sandbox", "--disable-slash-commands", "--print-timeout", "10m",
]
message = {"event": "user", "message": {"content": packet_bytes.decode("utf-8")}}
stdin_bytes = json.dumps(message, ensure_ascii=False, separators=(",", ":")).encode("utf-8") + b"\n"
if stdin_bytes.startswith(b"\xef\xbb\xbf"):
    raise SystemExit("STDIN_HAS_UTF8_BOM")
started = datetime.datetime.now(datetime.timezone.utc)
p = subprocess.Popen(
    args, cwd=str(CWD), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0), close_fds=True,
)
start = {
    "schema": "TTQS_ONE_W2_FULL_SEMANTIC_REVIEW_START_R10_V1",
    "work_id": manifest["work_id"], "project_id": "TTQS_ONE", "doc_id": "0142",
    "requirement_id": "I19-E32", "process_id": p.pid, "launcher_pid": os.getpid(),
    "started_utc": started.isoformat(), "requested_model": "gemini-3.8-flash-high",
    "actual_serving_model": "UNKNOWN", "cli_version": "1.5.9",
    "cli_sha256": exe_sha, "candidate_docx_sha256": manifest["candidate_docx_sha256"],
    "candidate_body_sha256": manifest["candidate_body_sha256"],
    "input_packet_sha256": packet_sha, "input_packet_bytes": len(packet_bytes),
    "stdin_sha256": hashlib.sha256(stdin_bytes).hexdigest(), "stdin_encoding": "UTF-8 without BOM",
    "args": args, "working_directory": str(CWD), "mode": "plan", "sandbox": True,
    "auto_approval": False, "add_dir": None, "tool_calls_requested": False,
    "hidden_window": True, "timeout_seconds": 600, "dispatch_state": "DISPATCHED",
}
(ROOT / "DISPATCH_START_W2_R10.json").write_text(json.dumps(start, ensure_ascii=False, indent=2), encoding="utf-8")
timed_out = False
send_error = None
try:
    stdout, stderr = p.communicate(input=stdin_bytes, timeout=630)
except subprocess.TimeoutExpired:
    timed_out = True
    p.terminate()
    try:
        stdout, stderr = p.communicate(timeout=10)
    except subprocess.TimeoutExpired:
        p.kill()
        stdout, stderr = p.communicate()
except BrokenPipeError as e:
    send_error = repr(e)
    stdout, stderr = p.communicate()
finished = datetime.datetime.now(datetime.timezone.utc)
(ROOT / "RAW_STDOUT_W2_R10.jsonl").write_bytes(stdout or b"")
(ROOT / "RAW_STDERR_W2_R10.bin").write_bytes(stderr or b"")
event_types = []
tool_event_count = 0
json_parse_errors = 0
usage = {}
for line in (stdout or b"").splitlines():
    if not line.strip():
        continue
    try:
        ev = json.loads(line.decode("utf-8"))
        if isinstance(ev, dict):
            typ = str(ev.get("type", "UNKNOWN"))
            event_types.append(typ)
            if "tool" in typ.lower():
                tool_event_count += 1
            for key in ("usage", "usageMetadata", "tokens"):
                if key in ev:
                    usage = ev[key]
    except Exception:
        json_parse_errors += 1
terminal = {
    "schema": "TTQS_ONE_W2_FULL_SEMANTIC_REVIEW_TERMINAL_R10_V1",
    "work_id": manifest["work_id"], "project_id": "TTQS_ONE", "doc_id": "0142",
    "requirement_id": "I19-E32", "process_id": p.pid, "launcher_pid": os.getpid(),
    "process_exit_code": p.returncode, "timed_out": timed_out,
    "started_utc": started.isoformat(), "completed_utc": finished.isoformat(),
    "duration_seconds": round((finished-started).total_seconds(), 3),
    "stdout_bytes": len(stdout or b""), "stdout_sha256": hashlib.sha256(stdout or b"").hexdigest(),
    "stderr_bytes": len(stderr or b""), "stderr_sha256": hashlib.sha256(stderr or b"").hexdigest(),
    "candidate_docx_sha256": manifest["candidate_docx_sha256"],
    "candidate_body_sha256": manifest["candidate_body_sha256"],
    "input_packet_sha256": packet_sha, "requested_model": "gemini-3.8-flash-high",
    "actual_serving_model": "UNKNOWN", "event_count": len(event_types),
    "event_types": event_types, "tool_event_count": tool_event_count,
    "json_parse_errors": json_parse_errors, "usage": usage, "stdin_send_error": send_error,
    "status": "TIMEOUT" if timed_out else ("EXIT_ZERO" if p.returncode == 0 else "EXIT_NONZERO"),
}
(ROOT / "DISPATCH_TERMINAL_W2_R10.json").write_text(json.dumps(terminal, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({"pid": p.pid, "exit": p.returncode, "timed_out": timed_out, "stdout_bytes": len(stdout or b""), "stderr_bytes": len(stderr or b""), "event_count": len(event_types), "tool_event_count": tool_event_count, "json_parse_errors": json_parse_errors}, ensure_ascii=False))