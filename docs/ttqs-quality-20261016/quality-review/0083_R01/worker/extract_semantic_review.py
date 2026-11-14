#!/usr/bin/env python3
import hashlib, json, re
from pathlib import Path

base = Path(__file__).resolve().parents[1]
raw = base / "review" / "opencode_semantic_R01_stdout.jsonl"
body = base / "candidate" / "0083_R01_body.md"
events = [json.loads(line) for line in raw.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
texts = [e["part"]["text"] for e in events if e.get("type") == "text" and isinstance(e.get("part", {}).get("text"), str)]
if len(texts) != 1:
    raise SystemExit(f"Expected one reviewer text result, got {len(texts)}")
review_text = texts[0].strip() + "\n"
review_path = base / "review" / "independent_semantic_review_R01.md"
review_path.write_text(review_text, encoding="utf-8")
body_sha = hashlib.sha256(body.read_bytes()).hexdigest()
match = re.search(r"(?im)^\s*(?:[-*]\s*)?(?:verdict|review verdict|review result)\s*[:=：]\s*(PASS|PARTIAL|FAIL)\b", review_text)
receipt = {
    "schema": "ttqs-0083-independent-semantic-review-v1",
    "reviewer_route": "OpenCode v2 CLI, separate session from writer",
    "model": "opencode/deepseek-v4.1-flash-free",
    "session_id": next((e.get("sessionID") for e in events if e.get("sessionID")), None),
    "exit_code": int((base / "review" / "opencode_semantic_R01_exit.txt").read_text().strip()),
    "body_path": str(body),
    "body_sha256": body_sha,
    "prompt_sha256": hashlib.sha256((base / "review" / "semantic_review_prompt_R01.md").read_bytes()).hexdigest(),
    "raw_stdout_sha256": hashlib.sha256(raw.read_bytes()).hexdigest(),
    "stderr_sha256": hashlib.sha256((base / "review" / "opencode_semantic_R01_stderr.txt").read_bytes()).hexdigest(),
    "review_text_sha256": hashlib.sha256(review_path.read_bytes()).hexdigest(),
    "reported_verdict": match.group(1) if match else "UNPARSED",
    "independent_of_writer_session": "ses_ead41712affenj37Hr21rYh321",
}
(base / "evidence" / "semantic_review_receipt_R01.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=True))
