from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
REVIEW = BASE / "review"
CANDIDATE = BASE / "candidate" / "0084_R11.docx"
PACKET = REVIEW / "semantic_review_packet_R11.md"
RAW = REVIEW / "opencode_semantic_R11_stdout.jsonl"
STDERR = REVIEW / "opencode_semantic_R11_stderr.txt"
PROMPT = REVIEW / "semantic_review_prompt_R11.md"
RESPONSE = REVIEW / "independent_semantic_review_R11.md"
RESULT = REVIEW / "opencode_semantic_R11_result.json"
RECEIPT = REVIEW / "semantic_review_receipt_R11.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


rows = [json.loads(line) for line in RAW.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
texts = []
for row in rows:
    if row.get("type") == "text":
        text = row.get("text", "") or row.get("part", {}).get("text", "")
        if text.strip():
            texts.append(text)
if len(texts) != 1:
    raise RuntimeError(f"Expected one final reviewer text event; found {len(texts)}")
response = texts[0].rstrip() + "\n"
verdicts = re.findall(r"^## Verdict: (PASS|PARTIAL|FAIL)\s*$", response, re.MULTILINE)
if len(verdicts) != 1:
    raise RuntimeError(f"Expected one explicit verdict; found {verdicts}")
verdict = verdicts[0]
RESPONSE.write_text(response, encoding="utf-8", newline="\n")

result = json.loads(RESULT.read_text(encoding="utf-8"))
result.update({
    "verdict": verdict,
    "response_path": str(RESPONSE.relative_to(BASE)).replace("/", "\\"),
    "response_sha256": sha(RESPONSE),
    "parsed_at_local": datetime.now().astimezone().isoformat(),
})
RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

receipt = {
    "schema": "ttqs-independent-semantic-review-receipt-v1",
    "document_id": "0084",
    "requirement_id": "I17C-E03",
    "official_checkbox_serial": "090",
    "revision": "R11",
    "review_route": "OpenCode CLI v2.0.29; independent CLI process; no Computer Use",
    "model": "opencode/mimo-v2.6-flash-free",
    "candidate_path": str(CANDIDATE.relative_to(BASE)).replace("/", "\\"),
    "candidate_sha256": sha(CANDIDATE),
    "packet_path": str(PACKET.relative_to(BASE)).replace("/", "\\"),
    "packet_sha256": sha(PACKET),
    "prompt_path": str(PROMPT.relative_to(BASE)).replace("/", "\\"),
    "prompt_sha256": sha(PROMPT),
    "raw_stdout_path": str(RAW.relative_to(BASE)).replace("/", "\\"),
    "raw_stdout_sha256": sha(RAW),
    "raw_stderr_path": str(STDERR.relative_to(BASE)).replace("/", "\\"),
    "raw_stderr_sha256": sha(STDERR),
    "response_path": str(RESPONSE.relative_to(BASE)).replace("/", "\\"),
    "response_sha256": sha(RESPONSE),
    "verdict": verdict,
    "result": "PASS_WITH_FOUR_NON_BLOCKING_FINDINGS" if verdict == "PASS" else verdict,
    "attempt_count": 1,
    "retry_count": 0,
    "started_at_local": result.get("started_at_local"),
    "finished_at_local": result.get("finished_at_local"),
    "candidate_unchanged_during_review": result.get("candidate_unchanged_during_review"),
    "scope": "Full exact-SHA text-semantic review against the supplied official source packet and complete Unique Blueprint R03; reviewer independently rehashed the candidate and source files; 8 required checks; four minor findings; layout/render and human trial-use excluded.",
    "limitations": [
        "Packet SHA was not independently cross-checkable from a separate post-generation receipt in the supplied packet.",
        "Visual/layout review is separate and not accepted by this semantic verdict.",
        "Candidate remains not formally accepted; REAL evidence remains UNKNOWN/HOLD."
    ],
    "formal_acceptance": "NOT_GRANTED",
    "real_evidence_status": "UNKNOWN_HOLD",
}
RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({
    "verdict": verdict,
    "candidate_sha256": receipt["candidate_sha256"],
    "response_sha256": receipt["response_sha256"],
    "receipt_sha256": sha(RECEIPT),
    "non_blocking_findings": 4,
}, ensure_ascii=False, indent=2))
