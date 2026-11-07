from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0004_I01-E02_SOURCE_PREP_R03_20261030")
DEST = ROOT / "qa" / "GITHUB_SYNC_INPUT_MANIFEST_R05_L06.json"
REMOTE_ROOT = "docs/ttqs-quality-20261016/quality-review/0004_I01-E02_SOURCE_PREP_R03_20261030/R05_L06"
BASE_HEAD = "aefb529d729117336e7a086f2a5a8a8bb55bad8e"
FILES = [
    ("qa/CANDIDATE_INDEX_R05_L06.md", "qa/CANDIDATE_INDEX_R05_L06.md"),
    ("qa/WORKER_ROUTE_STATUS_R05_L06.json", "qa/WORKER_ROUTE_STATUS_R05_L06.json"),
    ("qa/CANDIDATE_EVIDENCE_MANIFEST_R05_L06.json", "qa/CANDIDATE_EVIDENCE_MANIFEST_R05_L06.json"),
    ("qa/TECHNICAL_QA_R05_L06.json", "qa/TECHNICAL_QA_R05_L06.json"),
    ("qa/VISUAL_QA_R05_L06.json", "qa/VISUAL_QA_R05_L06.json"),
    ("qa/WORD_NATIVE_RENDER_R05_L06.json", "qa/WORD_NATIVE_RENDER_R05_L06.json"),
    ("qa/LAYOUT_REPAIR_RECEIPT_R05_L06.json", "qa/LAYOUT_REPAIR_RECEIPT_R05_L06.json"),
    ("qa/NUMBERING_REPAIR_RECEIPT_R05_L06.json", "qa/NUMBERING_REPAIR_RECEIPT_R05_L06.json"),
    ("qa/WORD_BUILD_RECEIPT_R05_L06.json", "qa/WORD_BUILD_RECEIPT_R05_L06.json"),
    ("qa/SEMANTIC_REVIEW_R05_L06.json", "qa/SEMANTIC_REVIEW_R05_L06.json"),
    ("docx/0004_I01-E02_R05_L06.docx", "docx/0004_I01-E02_R05_L06.docx"),
    ("render/0004_I01-E02_R05_L06_WordNative.pdf", "render/0004_I01-E02_R05_L06_WordNative.pdf"),
    ("render/CONTACT_SHEET_R05_L06.jpg", "render/CONTACT_SHEET_R05_L06.jpg"),
    ("worker/0004_WRITER_MANUSCRIPT_CANDIDATE_R05.md", "worker/0004_WRITER_MANUSCRIPT_CANDIDATE_R05.md"),
    ("SYNTHETIC_REPLACEMENT_REGISTER_PLAN_0004_R05.csv", "SYNTHETIC_REPLACEMENT_REGISTER_PLAN_0004_R05.csv"),
    ("worker/AGY_WRITER_DISPATCH_R03.json", "worker/AGY_WRITER_DISPATCH_R03.json"),
    ("worker/AGY_WRITER_INPUT_0004_R03.md", "worker/AGY_WRITER_INPUT_0004_R03.md"),
    ("worker/AGY_WRITER_RAW_STDOUT_R03.jsonl", "worker/AGY_WRITER_RAW_STDOUT_R03.jsonl"),
    ("worker/AGY_WRITER_RAW_STDERR_R03.txt", "worker/AGY_WRITER_RAW_STDERR_R03.txt"),
    ("worker/AGY_RESPONSE_EXTRACT_R03.txt", "worker/AGY_RESPONSE_EXTRACT_R03.txt"),
    ("worker/AGY_RESPONSE_RECOVERY_R01.json", "worker/AGY_RESPONSE_RECOVERY_R01.json"),
    ("worker/repair_0004_r05.py", "worker/repair_0004_r05.py"),
    ("worker/MANUSCRIPT_PATCH_RECEIPT_R05.json", "worker/MANUSCRIPT_PATCH_RECEIPT_R05.json"),
    ("worker/STATIC_CONTENT_QA_R05.json", "worker/STATIC_CONTENT_QA_R05.json"),
    ("worker/build_docx_0004_r05_l05.py", "worker/build_docx_0004_r05_l05.py"),
    ("worker/repair_list_numbering_l06.py", "worker/repair_list_numbering_l06.py"),
    ("worker/verify_candidate_l06.py", "worker/verify_candidate_l06.py"),
    ("worker/finalize_evidence_l06.py", "worker/finalize_evidence_l06.py"),
    ("worker/finalize_review_l06.py", "worker/finalize_review_l06.py"),
    ("worker/generate_github_sync_manifest_l06.py", "worker/generate_github_sync_manifest_l06.py"),
    ("worker/review/REVIEW_HISTORY_L05_PARTIAL_SUMMARY.md", "worker/review/REVIEW_HISTORY_L05_PARTIAL_SUMMARY.md"),
    ("worker/review/REVIEWER_ZENO_R05_L06_RAW.md", "worker/review/REVIEWER_ZENO_R05_L06_RAW.md"),
    ("worker/review/REVIEWER_GODEL_R05_L06_RAW.md", "worker/review/REVIEWER_GODEL_R05_L06_RAW.md"),
    ("worker/review/REVIEWER_ZENO_R05_RAW.md", "history_manuscript_review/REVIEWER_ZENO_R05_MANUSCRIPT_RAW.md"),
    ("worker/review/REVIEWER_GODEL_R05_RAW.md", "history_manuscript_review/REVIEWER_GODEL_R05_MANUSCRIPT_RAW.md"),
    ("docx/0004_I01-E02_R05_L05.docx", "history_L05/0004_I01-E02_R05_L05.docx"),
    ("render/0004_I01-E02_R05_L05_WordNative.pdf", "history_L05/0004_I01-E02_R05_L05_WordNative.pdf"),
    ("qa/TECHNICAL_QA_R05_L05.json", "history_L05/TECHNICAL_QA_R05_L05.json"),
    ("qa/VISUAL_QA_R05_L05.json", "history_L05/VISUAL_QA_R05_L05.json"),
    ("qa/LAYOUT_REPAIR_RECEIPT_R05_L05.json", "history_L05/LAYOUT_REPAIR_RECEIPT_R05_L05.json"),
    ("qa/WORD_BUILD_RECEIPT_R05_L05.json", "history_L05/WORD_BUILD_RECEIPT_R05_L05.json"),
]


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    if DEST.exists():
        raise FileExistsError(DEST)
    items = []
    for local, remote in FILES:
        p = ROOT / local
        if not p.is_file():
            raise FileNotFoundError(p)
        items.append({
            "remote_path": f"{REMOTE_ROOT}/{remote}",
            "local_file": local,
            "bytes": p.stat().st_size,
            "sha256": sha(p),
        })
    data = {
        "project_id": "TTQS_ONE",
        "doc_id": "0004",
        "requirement_id": "I01-E02",
        "revision": "R05_L06",
        "state": "INDEPENDENTLY_REVIEWED_CANDIDATE_NOT_FORMALLY_ACCEPTED",
        "repository": "PT-Original-Point/ttqs-one",
        "branch": "work/ttqs-one-document-quality-contract-20261016",
        "expected_base_head": BASE_HEAD,
        "remote_root": REMOTE_ROOT,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "file_count": len(items),
        "files": items,
        "source_packet_sha256": sha(ROOT / "SOURCE_PACKET_0004_I01-E02_R03.md"),
        "unique_blueprint_sha256": sha(ROOT / "UNIQUE_BLUEPRINT_0004_I01-E02_R03.md"),
        "blueprint_current_row_sha256": sha(ROOT / "source" / "BLUEPRINT_CURRENT_ROW_0004.jsonl"),
        "official_requirement_pdf_sha256": sha(ROOT / "source" / "official_requirement.pdf"),
        "remote_readback": "PENDING",
        "formal_acceptance": "UNKNOWN",
    }
    DEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"manifest": str(DEST), "file_count": len(items), "total_bytes": sum(x["bytes"] for x in items), "docx_sha256": next(x["sha256"] for x in items if x["local_file"].endswith("R05_L06.docx"))}, ensure_ascii=False))


if __name__ == "__main__":
    main()
