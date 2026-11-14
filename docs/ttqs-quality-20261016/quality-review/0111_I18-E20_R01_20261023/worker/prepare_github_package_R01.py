from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCX_SHA = "31fc783e6021a6f19ae2fa316a0b8bb28b0cf058508da46bcb312ea7787090fd"
OUT_MANIFEST = ROOT / "evidence" / "github_package_manifest_0111_R01.json"
STATUS = ROOT / "evidence" / "candidate_status_0111_R01.json"

FILES = [
    ("candidate/0111_I18-E20_特殊績效及社會面成果證據登錄表_R01.docx", "candidate/0111_I18-E20_特殊績效及社會面成果證據登錄表_R01.docx"),
    ("visual/0111_R01/0111_R01_word_native.pdf", "render/0111_R01_word_native.pdf"),
    ("manuscript/0111_I18-E20_特殊績效及社會面成果證據登錄表_R01.md", "candidate/0111_R01_manuscript.md"),
    ("inputs/source_packet_0111_R01.md", "source/source_packet_0111_R01.md"),
    ("inputs/UNIQUE_BLUEPRINT_0111_R01.json", "source/UNIQUE_BLUEPRINT_0111_R01.json"),
    ("source/official_source_page7_text.txt", "source/official_source_page7_text.txt"),
    ("source/official_source_page7_render.png", "source/official_source_page7_render.png"),
    ("evidence/source_stage_receipt_0111_R01.json", "evidence/source_stage_receipt_R01.json"),
    ("evidence/source_stage_receipt_0111_R02.json", "evidence/source_stage_receipt_R02.json"),
    ("evidence/manuscript_adoption_receipt_0111_R01.json", "evidence/manuscript_adoption_receipt_R01.json"),
    ("evidence/manuscript_qa_0111_R01.json", "evidence/manuscript_qa_R01.json"),
    ("evidence/docx_build_receipt_0111_R01.json", "evidence/docx_build_receipt_R01.json"),
    ("evidence/word_export_receipt_0111_R01.json", "evidence/word_export_receipt_R01.json"),
    ("evidence/raster_receipt_0111_R01.json", "evidence/raster_receipt_R01.json"),
    ("evidence/technical_qa_0111_R01.json", "evidence/technical_qa_R01.json"),
    ("evidence/visual_qa_receipt_0111_R01.json", "evidence/visual_qa_receipt_R01.json"),
    ("writer/worker_return_0111_R01_attempt02.md", "worker/writer_return_attempt02.md"),
    ("writer/worker_return_receipt_0111_R01_attempt02.json", "worker/writer_return_receipt_attempt02.json"),
    ("writer/writer_dispatch_started_0111_R01_attempt02.json", "worker/writer_dispatch_attempt02.json"),
    ("writer/writer_input_packet_0111_R01.md", "worker/writer_input_packet_R01.md"),
    ("writer/build_docx_0111_R01.py", "worker/build_docx_R01.py"),
    ("writer/technical_qa_0111_R01.py", "worker/technical_qa_R01.py"),
    ("writer/record_visual_qa_0111_R01.py", "worker/record_visual_qa_R01.py"),
    ("writer/prepare_semantic_review_packet_0111_R01.py", "worker/prepare_semantic_review_packet_R01.py"),
    ("writer/prepare_github_package_0111_R01.py", "worker/prepare_github_package_R01.py"),
    ("writer/sync_candidate_to_github_0111_R01.ps1", "worker/sync_candidate_to_github_R01.ps1"),
    ("review/semantic_review_packet_0111_R01.md", "review/semantic_review_packet_R01.md"),
    ("review/semantic_review_input_manifest_0111_R01.json", "review/semantic_review_input_manifest_R01.json"),
    ("review/opencode_semantic_review_0111_R01_dispatch.json", "review/opencode_semantic_review_dispatch_R01.json"),
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    docx = ROOT / FILES[0][0]
    docx_sha = sha256(docx)
    if docx_sha != DOCX_SHA:
        raise SystemExit(f"candidate SHA changed: {docx_sha}")
    technical = json.loads((ROOT / "evidence" / "technical_qa_0111_R01.json").read_text(encoding="utf-8"))
    visual = json.loads((ROOT / "evidence" / "visual_qa_receipt_0111_R01.json").read_text(encoding="utf-8"))
    if technical.get("result") != "PASS_TECHNICAL" or technical.get("candidate_docx_sha256") != docx_sha:
        raise SystemExit("technical receipt not PASS or wrong candidate SHA")
    if visual.get("result") != "PASS_VISUAL" or visual.get("candidate_docx_sha256") != docx_sha:
        raise SystemExit("visual receipt not PASS or wrong candidate SHA")
    entries = []
    for local_rel, remote_rel in FILES:
        path = ROOT / local_rel
        if not path.is_file():
            raise SystemExit(f"missing package file: {path}")
        entries.append({"local_path": str(path), "remote_relative_path": remote_rel, "sha256": sha256(path), "bytes": path.stat().st_size})
    status = {
        "project_id": "TTQS_ONE",
        "doc_id": "0111",
        "requirement_id": "I18-E20",
        "official_checkbox_serial": "UNKNOWN_NOT_ASSERTED",
        "unique_blueprint_sha256": "1abb7a6414ef33ed9fe08d9f1782d9208bb60d3cf5c4ded7a5381c779f65f0f6",
        "official_pdf_sha256": "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709",
        "candidate_path": str(docx),
        "candidate_sha256": docx_sha,
        "candidate_state": "CANDIDATE_PENDING_INDEPENDENT_SEMANTIC_REVIEW",
        "technical_qa": "PASS_TECHNICAL_EXACT_SHA",
        "visual_qa": "PASS_VISUAL_17_OF_17_PAGES_EXACT_SHA",
        "semantic_qa": "IN_PROGRESS_OPEN_CODE_V2_EXACT_SHA_REVIEW",
        "real_evidence": "UNKNOWN_NO_REAL_ORIGINALS_SUPPLIED; E0/HOLD",
        "human_formal_acceptance": "NOT_GRANTED",
        "status_time_utc": datetime.now(timezone.utc).isoformat(),
    }
    STATUS.write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    entries.append({"local_path": str(STATUS), "remote_relative_path": "evidence/candidate_status_R01.json", "sha256": sha256(STATUS), "bytes": STATUS.stat().st_size})
    manifest = {
        "work_id": "TTQS-0111-I18-E20-GITHUB-CANDIDATE-SYNC-R01-20261023",
        "doc_id": "0111",
        "requirement_id": "I18-E20",
        "candidate_sha256": docx_sha,
        "remote_prefix": "docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R01_20261023",
        "source_packet_sha256": "cbbbac1b601468df3e1d4ee16916b3891ed19205ff1b9db589157510753d89fa",
        "unique_blueprint_sha256": "1abb7a6414ef33ed9fe08d9f1782d9208bb60d3cf5c4ded7a5381c779f65f0f6",
        "official_source_page7_text_sha256": "78a60101bc37d688670a27d0f115f78abde6385391947459cbbb51343b5ad9eb",
        "state": "CANDIDATE_QA_STABLE_SEMANTIC_REVIEW_PENDING",
        "files": entries,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    OUT_MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"candidate_sha256": docx_sha, "files_to_sync": len(entries), "package_manifest_sha256": sha256(OUT_MANIFEST), "package_manifest_bytes": OUT_MANIFEST.stat().st_size, "status": status["candidate_state"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    main()
