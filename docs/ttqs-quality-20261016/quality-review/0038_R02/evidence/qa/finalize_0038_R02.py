from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = ROOT / "evidence"
QA = EVIDENCE / "qa"
TECH_PATH = QA / "technical_qa.json"
NOTES_PATH = QA / "visual_review_notes.json"
DOCX = ROOT / "candidate" / "0038_R02.docx"
PDF = EVIDENCE / "render" / "0038_R02.pdf"
RENDER = EVIDENCE / "render_final"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


TEXT_SUFFIXES = {".md", ".json", ".jsonl", ".csv", ".py", ".txt", ".ps1"}


def canonical_artifact_bytes(path: Path) -> bytes:
    data = path.read_bytes()
    return data.replace(b"\r\n", b"\n") if path.suffix.lower() in TEXT_SUFFIXES else data


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


tech = json.loads(TECH_PATH.read_text(encoding="utf-8"))
notes = json.loads(NOTES_PATH.read_text(encoding="utf-8"))
docx_sha = sha256(DOCX)
pdf_sha = sha256(PDF)
semantic_path = QA / "semantic_review_receipt_R02.json"
semantic_receipt = json.loads(semantic_path.read_text(encoding="utf-8")) if semantic_path.exists() else None
semantic_status = semantic_receipt.get("verdict", "PENDING") if semantic_receipt else "PENDING"
semantic_matches = bool(semantic_receipt) and semantic_receipt.get("candidate_sha256") == docx_sha and semantic_receipt.get("render_pdf_sha256") == pdf_sha
if semantic_receipt and not semantic_matches:
    raise SystemExit("semantic receipt exact-SHA does not match current DOCX/PDF")
images = sorted(RENDER.glob("page-*.png"))
page_notes = notes.get("pages", [])
expected_numbers = list(range(1, len(images) + 1))
actual_numbers = [int(p["page"]) for p in page_notes]
pages_match = actual_numbers == expected_numbers and all(p.get("status") in {"PASS", "FAIL"} and p.get("observation") for p in page_notes)
hashes_match = notes.get("candidate_sha256") == docx_sha and notes.get("pdf_sha256") == pdf_sha
visual_status = "PASS" if pages_match and hashes_match and all(p["status"] == "PASS" for p in page_notes) else "FAIL"

visual = {
    "project": "TTQS_ONE",
    "document_id": "0038",
    "requirement_id": "I08-E02",
    "official_checkbox_sequence": "039",
    "candidate": "0038_R02",
    "candidate_sha256": docx_sha,
    "pdf_sha256": pdf_sha,
    "page_count": len(images),
    "renderer": notes.get("renderer"),
    "scope": "Direct inspection of every page image in the final rendered set",
    "pages": page_notes,
    "systematic_defects": notes.get("systematic_defects", []),
    "status": visual_status,
    "independent_semantic_review": semantic_status,
    "semantic_review_candidate_sha256": docx_sha if semantic_receipt else None,
    "semantic_review_raw_sha256": semantic_receipt.get("review_raw_sha256") if semantic_receipt else None,
    "formal_acceptance": "NOT_GRANTED",
}
(QA / "visual_qa.json").write_text(json.dumps(visual, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

progress_path = ROOT / "PROGRESS.json"
progress = json.loads(progress_path.read_text(encoding="utf-8"))
progress["candidate_sha256"] = docx_sha
progress["status"] = f"CANDIDATE_BUILT; technical={tech['status']}; visual={visual_status}; independent_semantic_review={semantic_status}; formal_acceptance=NOT_GRANTED"
progress["review"] = {
    "technical": tech["status"],
    "visual": visual_status,
    "visual_page_count": len(images),
    "semantic": semantic_status,
    "semantic_review_receipt": "evidence/qa/semantic_review_receipt_R02.json" if semantic_receipt else None,
    "semantic_review_raw_sha256": semantic_receipt.get("review_raw_sha256") if semantic_receipt else None,
    "exact_sha_bound_review": bool(semantic_matches and semantic_status == "PASS"),
    "formal_acceptance": "NOT_GRANTED",
}
remote_state = progress.get("remote", {})
if remote_state.get("status") != "PASS_EXACT_READBACK":
    remote_state = {"status": "PENDING_UPLOAD", "github_path": None, "verified_readback": False}
progress["remote"] = remote_state
progress["last_material_change"] = {
    "reason": "Resolved the two R01 semantic-review gaps by adding row-level execution trace and an official-requirement-to-fields/sources/decision/review crosswalk; no metadata-only DOCX rebuild.",
    "previous_candidate_sha256": "75065568b801506d736297441ee30abd3eaccc4fa3748ef6da2a11c67715088a",
    "new_candidate_sha256": docx_sha,
}
progress_path.write_text(json.dumps(progress, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

readme = f"""# 0038 R02 candidate

對應 DOCX 0038 / I08-E02 / 官方方框序號039。文類為訓練方案系統設計改善的執行與成效示範紀錄；與0037/I08-E01多期設計檢討、0039/I08-E03規劃會議紀錄明確區分。

**DOCX SHA-256:** `{docx_sha}`
**Word PDF SHA-256:** `{pdf_sha}`
**狀態:** 技術 {tech['status']}；逐頁視覺 {visual_status}（{len(images)}頁）；獨立語意審查 {semantic_status}；正式接受 NOT_GRANTED。

R02依R01獨立審查的兩項 PARTIAL 發現補入24筆逐列執行追溯，以及官方要求→正文紀錄欄位→SAMPLE/REAL來源→判定限制→覆核位置對照。所有日期、角色、課程、代碼、分數、計算及決定均為SAMPLE/SYNTHETIC，不代表協會實際辦訓、同意、核准或成效。

完整頁面 PDF、逐筆替換清冊、官方需求與 Blueprint 對照及技術/版面收據均隨附。獨立審查與協會正式接受狀態以 PROGRESS.json 和相應 exact-SHA 收據為準。
"""
(ROOT / "README.md").write_text(readme, encoding="utf-8")

tracked = [
    ROOT / "README.md", progress_path, DOCX,
    EVIDENCE / "SYNTHETIC_REPLACEMENT_REGISTER.csv",
    EVIDENCE / "build" / "build_0038_R02.py",
    ROOT / "inputs" / "official-2.png", ROOT / "inputs" / "official-3.png",
    ROOT / "inputs" / "SOURCE_MAP.md", ROOT / "inputs" / "BLUEPRINT_CURRENT_0038.jsonl",
    EVIDENCE / "assets" / "design_improvement_flow.png",
    EVIDENCE / "assets" / "synthetic_prepost_comparison.png",
    QA / "verify_0038_R02.py", QA / "finalize_0038_R02.py", QA / "record_semantic_review_R02.py", QA / "verify_remote_readback_0038_R02.py",
    TECH_PATH, QA / "visual_review_notes.json", QA / "visual_qa.json", PDF,
    QA / "remote_readback_attempt_initial.json", QA / "readback_normalization_note.md",
]
if semantic_receipt:
    tracked.extend([semantic_path, QA / "independent_semantic_review_R02.md"])
tracked.extend(images)
inventory = []
for p in tracked:
    if p.is_file():
        artifact_bytes = canonical_artifact_bytes(p)
        inventory.append({"path": p.relative_to(ROOT).as_posix(), "bytes": len(artifact_bytes), "sha256": sha256_bytes(artifact_bytes)})
manifest = {
    "project": "TTQS_ONE", "document_id": "0038", "requirement_id": "I08-E02",
    "official_checkbox_sequence": "039", "candidate": "0038_R02",
    "candidate_sha256": docx_sha, "pdf_sha256": pdf_sha,
    "technical_qa": tech["status"], "visual_qa": visual_status,
    "independent_semantic_review": semantic_status, "formal_acceptance": "NOT_GRANTED",
    "remote_readback": progress.get("remote", {}),
    "artifacts": inventory,
}
(EVIDENCE / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(json.dumps({"candidate_sha256": docx_sha, "pdf_sha256": pdf_sha, "technical": tech["status"], "visual": visual_status, "semantic": semantic_status, "pages": len(images), "manifest_artifacts": len(inventory)}, ensure_ascii=False))
