from pathlib import Path
from hashlib import sha256
import json

root = Path(r"E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0058_R01")
candidate = root / "candidate/0058_R08.docx"
review = root / "review/opencode_v2_semantic_R05"
evidence = root / "evidence"

def digest(path):
    return sha256(path.read_bytes()).hexdigest().upper()

docx_sha = digest(candidate)
opencode_receipt_path = review / "opencode_longcat_R01_invocation_receipt.json"
opencode_receipt = json.loads(opencode_receipt_path.read_text(encoding="utf-8-sig"))
opencode_response = review / "opencode_longcat_R01_independent_review.md"
response_text = opencode_response.read_text(encoding="utf-8")
assert opencode_receipt["model"] == "opencode/longcat-2.5-preview-free"
assert opencode_receipt["candidate_sha256_before"].upper() == docx_sha
assert opencode_receipt["candidate_sha256_after"].upper() == docx_sha
assert opencode_receipt["candidate_unchanged"] is True
assert opencode_receipt["exit_code"] == 0
assert "PASS — qualified semantic delta review only" in response_text
antigravity_receipt_path = review / "antigravity_gemini38_0058_R08_semantic_R04_route_receipt.json"
antigravity_receipt = json.loads(antigravity_receipt_path.read_text(encoding="utf-8-sig"))
antigravity_response = review / "antigravity_gemini38_0058_R08_semantic_R04_response.md"
assert digest(candidate) == "0DFCAAE1FF9943E46C1B9D527C3DF34FA61048547268C482D0DD378E44D7C58B"

manifest = {
    "doc_id": "0058", "requirement_id": "I13-E02", "official_checkbox_serial": "062",
    "blueprint_revision": "R06", "blueprint_sha256": "7606D16B80A4886CF6871943EF46DE0407D3EFB921FD6DB63597615F4C5B81F4",
    "candidate_revision": "R08", "candidate_sha256": docx_sha,
    "candidate_state": "CANDIDATE / SAMPLE-SYNTHETIC; not formally accepted",
    "technical_qa": {"verdict": "PASS", "receipt": "technical_qa_0058_R08.json", "sha256": digest(evidence / "technical_qa_0058_R08.json")},
    "visual_qa": {"verdict": "PASS", "scope": "all 8 contact sheets (32 pages) and full-resolution pages 29-32", "receipt": "visual_review_0058_R08.md", "sha256": digest(evidence / "visual_review_0058_R08.md"), "pdf_sha256": digest(evidence / "render_R08/0058_R08.pdf")},
    "semantic_review": {
        "verdict": "PASS — qualified semantic delta review",
        "reviewer_route": "OpenCode CLI v2.0.29; opencode/longcat-2.5-preview-free; distinct from Antigravity Builder",
        "session_id": opencode_receipt["session_id"],
        "response": str(opencode_response.relative_to(root)).replace("\\", "/"),
        "response_sha256": digest(opencode_response),
        "raw_stdout": str((review / "opencode_longcat_R01_stdout.jsonl").relative_to(root)).replace("\\", "/"),
        "raw_stdout_sha256": digest(review / "opencode_longcat_R01_stdout.jsonl"),
        "invocation_receipt": str(opencode_receipt_path.relative_to(root)).replace("\\", "/"),
        "invocation_receipt_sha256": digest(opencode_receipt_path),
        "formal_acceptance": "NOT CLAIMED",
    },
    "antigravity_corroboration": {
        "verdict": "PASS — same-platform corroboration, not counted as independent acceptance because Antigravity also built R06",
        "model": antigravity_receipt["model"], "conversation_id": antigravity_receipt["conversation_id"],
        "response": str(antigravity_response.relative_to(root)).replace("\\", "/"),
        "response_sha256": digest(antigravity_response),
        "raw_stdout_sha256": digest(review / "antigravity_gemini38_0058_R08_semantic_R04_stdout.json"),
    },
    "formal_association_acceptance": "NOT CLAIMED",
    "real_evidence": "NOT CLAIMED; sample facts remain SAMPLE/SYNTHETIC and real-source status remains UNKNOWN",
}
path = evidence / "final_status_0058_R08.json"
path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"candidate_sha256": docx_sha, "technical": "PASS", "visual": "PASS", "semantic": manifest["semantic_review"]["verdict"], "final_status_sha256": digest(path), "path": str(path)}, ensure_ascii=False))
