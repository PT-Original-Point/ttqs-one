#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

base = Path(__file__).resolve().parents[1]
raw = base / "worker" / "opencode_body_R02_stdout.jsonl"
out = base / "candidate" / "0083_R02_body.md"
events = [json.loads(line) for line in raw.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
texts = [e["part"]["text"] for e in events if e.get("type") == "text" and isinstance(e.get("part", {}).get("text"), str)]
if len(texts) != 1:
    raise SystemExit(f"Expected exactly one text response, got {len(texts)}")
content = texts[0].strip() + "\n"
if not content.startswith("# DOCX 0083"):
    raise SystemExit("Response does not begin with the expected document title")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(content, encoding="utf-8")
receipt = {
    "schema": "ttqs-0083-opencode-body-extraction-v1",
    "worker": "OpenCode v2 CLI",
    "model": "opencode/deepseek-v4.1-flash-free",
    "session_id": next((e.get("sessionID") for e in events if e.get("sessionID")), None),
    "exit_code": int((base / "worker" / "opencode_body_R02_exit.txt").read_text().strip()),
    "raw_stdout_sha256": hashlib.sha256(raw.read_bytes()).hexdigest(),
    "stderr_sha256": hashlib.sha256((base / "worker" / "opencode_body_R02_stderr.txt").read_bytes()).hexdigest(),
    "source_packet_sha256": hashlib.sha256((base / "inputs" / "SOURCE_PACKET_0083_R01.md").read_bytes()).hexdigest(),
    "blueprint_sha256": hashlib.sha256((base / "inputs" / "UNIQUE_BLUEPRINT_0083_R03.md").read_bytes()).hexdigest(),
    "review_sha256": hashlib.sha256((base / "review" / "independent_semantic_review_R01.md").read_bytes()).hexdigest(),
    "body_sha256": hashlib.sha256(out.read_bytes()).hexdigest(),
    "body_bytes": out.stat().st_size,
    "acceptance": "WRITER_OUTPUT_ONLY_NOT_INDEPENDENTLY_ACCEPTED",
}
(base / "evidence" / "writer_receipt_R02.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=True))
