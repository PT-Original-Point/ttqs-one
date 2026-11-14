from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


PKG = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


candidates = list((PKG / "candidate").glob("*.docx"))
if len(candidates) != 1:
    raise SystemExit(f"Expected exactly one candidate; found {len(candidates)}")
candidate = candidates[0]
render_dir = PKG / "evidence" / "render"
pdf = render_dir / "0042_R01_word.pdf"
pages = sorted(render_dir.glob("page-*.png"))
if not pdf.is_file() or len(pages) != 14:
    raise SystemExit(f"Expected Word-export PDF and 14 page images; found {len(pages)} PNGs")

receipt = {
    "project_id": "TTQS_ONE",
    "doc_id": "0042",
    "revision": "R01",
    "requirement_id": "I09-E02",
    "official_checkbox_sequence": "043",
    "candidate_sha256": sha256(candidate),
    "renderer": "Microsoft Word desktop COM ExportAsFixedFormat to PDF, then Poppler rasterization at 144 DPI",
    "pdf_path": "evidence/render/0042_R01_word.pdf",
    "pdf_sha256": sha256(pdf),
    "page_count": len(pages),
    "post_repair_visual_inspection": {
        "status": "PASS_INTERNAL_ALL_PAGES_INSPECTED",
        "inspection_scope": "Each of the 14 rendered page images inspected individually at original resolution after the title-style repair.",
        "checks": {
            "title_rule_removed": True,
            "title_heading_subtitle_and_running_header_black": True,
            "clipping_or_overlap_observed": False,
            "table_breaks_or_repeated_headers_observed_as_defective": False,
            "missing_glyphs_observed": False,
            "page_number_sequence": "1-14",
        },
        "independent_review": "PENDING",
    },
    "pages": [
        {
            "page_number": index,
            "path": f"evidence/render/{page.name}",
            "sha256": sha256(page),
            "bytes": page.stat().st_size,
            "inspected": True,
        }
        for index, page in enumerate(pages, start=1)
    ],
    "inspected_at_utc": datetime.now(timezone.utc).isoformat(),
}
out = PKG / "evidence" / "visual_layout_receipt_R01.json"
out.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

progress_path = PKG / "PROGRESS.json"
progress = json.loads(progress_path.read_text(encoding="utf-8"))
progress["candidate_sha256"] = receipt["candidate_sha256"]
progress["layout_status"] = "PASS_INTERNAL_ALL_14_PAGES_POST_REPAIR"
progress["independent_semantic_review"] = "PENDING_ANTIGRAVITY_EXACT_SHA_REVIEW"
progress["visual_receipt_sha256"] = sha256(out)
progress["remote_readback"] = "PENDING"
progress_path.write_text(json.dumps(progress, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

technical_path = PKG / "evidence" / "technical_integrity_receipt_R01.json"
technical = json.loads(technical_path.read_text(encoding="utf-8"))
technical["candidate_sha256"] = receipt["candidate_sha256"]
technical["status"] = "PASS_TECHNICAL; CANDIDATE_PENDING_INDEPENDENT_REVIEW"
technical["post_repair_render"] = {
    "status": "PASS_INTERNAL_ALL_14_PAGES",
    "visual_receipt_sha256": sha256(out),
    "pdf_sha256": receipt["pdf_sha256"],
}
technical_path.write_text(json.dumps(technical, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

readme_path = PKG / "README.md"
readme = readme_path.read_text(encoding="utf-8")
readme = readme.replace(
    "修復後 Word 渲染/全頁視覺檢查及獨立 exact-SHA 語意審查待完成。",
    "修復後 Word 輸出 14 頁且逐頁視覺檢查 PASS；Antigravity CLI 獨立 exact-SHA 語意審查待完成。",
)
readme_path.write_text(readme, encoding="utf-8")

print(json.dumps({"candidate_sha256": receipt["candidate_sha256"], "pdf_sha256": receipt["pdf_sha256"], "page_count": len(pages), "visual_receipt_sha256": sha256(out)}, ensure_ascii=False, indent=2))
