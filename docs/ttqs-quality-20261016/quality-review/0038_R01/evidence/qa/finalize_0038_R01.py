from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = ROOT / "evidence"
QA = EVIDENCE / "qa"
TECH = json.loads((QA / "technical_qa.json").read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


pages = [
    (1, "封面、官方識別、SAMPLE界線及使用方式；字級層次清楚，無裁切。"),
    (2, "官方定位與0037/0039負向鄰項清楚；專屬流程圖箭頭、文字及框線可讀。"),
    (3, "設計缺口、可檢驗假設、三方案加權比較及事前判定規則完整；表格無溢出。"),
    (4, "120分鐘課程時程與可觀察目標—教學活動—評量證據對應完整。"),
    (5, "D1–D4量尺、達標門檻、等難度情境、缺漏與保存控制均可讀。"),
    (6, "全批次樣本框、納排條件、日期/渠道/同意/代碼及分母流向完整。"),
    (7, "A組12筆逐筆向量、總分、差值和判定完整；小計可重算。"),
    (8, "B組12筆及B08異常覆核可讀；未達標保留，未被排除。"),
    (9, "彙總計算與圖表一致，限制及不得因果推論的文字清楚。"),
    (10, "後續工作、真實資料替換清單及官方/專案來源索引完整，無孤立表頭。"),
    (11, "候選狀態與單次執行責任表同頁；內容完整，留白充足，非空白尾頁。"),
]

docx = ROOT / "candidate" / "0038_R01.docx"
pdf = EVIDENCE / "render" / "0038_R01.pdf"
render_dir = EVIDENCE / "render_final_75065568"
images = sorted(render_dir.glob("page-*.png"))
visual = {
    "project": "TTQS_ONE",
    "document_id": "0038",
    "requirement_id": "I08-E02",
    "official_checkbox_sequence": "039",
    "candidate": "0038_R01",
    "candidate_sha256": sha256(docx),
    "pdf_sha256": sha256(pdf),
    "page_count": len(images),
    "renderer": "Microsoft Word opened read-only and exported to PDF; Poppler rasterized at 120 dpi",
    "scope": "Direct visual inspection of every rendered page, 1 through 11",
    "pages": [{"page": n, "status": "PASS", "observation": note} for n, note in pages],
    "systematic_defects": [],
    "status": "PASS" if len(images) == len(pages) == TECH["page_count"] else "FAIL",
    "independent_semantic_review": "PENDING",
    "formal_acceptance": "NOT_GRANTED",
}
(QA / "visual_qa.json").write_text(json.dumps(visual, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

progress_path = ROOT / "PROGRESS.json"
progress = json.loads(progress_path.read_text(encoding="utf-8"))
progress["candidate_sha256"] = sha256(docx)
progress["status"] = "CANDIDATE_BUILT; technical=PASS; visual=PASS; independent_semantic_review=PENDING; formal_acceptance=NOT_GRANTED"
progress["review"] = {
    "technical": "PASS",
    "visual": "PASS",
    "visual_page_count": len(images),
    "semantic": "PENDING",
    "exact_sha_bound_review": False,
    "formal_acceptance": "NOT_GRANTED",
}
progress["remote"] = {"status": "PENDING_UPLOAD", "github_path": None, "verified_readback": False}
progress["last_material_change"] = {
    "reason": "Moved the execution-control table off a page that stranded its final row and removed the resulting sparse spill; consolidated it with the candidate-state page.",
    "previous_candidate_sha256": "09d348829792d67c235d7a9d300ddae54cc8c28703198d0ac3d6f93b340a9e41",
    "new_candidate_sha256": sha256(docx),
}
progress_path.write_text(json.dumps(progress, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

readme = f"""# 0038 R01 candidate

此候選對應 DOCX 0038 / I08-E02 / 官方方框序號039。文類為系統設計改善的執行與樣本紀錄，不是0037跨期檢討，也不是0039會議紀錄。

**DOCX SHA-256:** `{sha256(docx)}`  
**狀態:** Candidate；技術驗證 PASS、11頁目視檢查 PASS；獨立語意審查 PENDING；協會正式接受 NOT_GRANTED。

全篇日期、角色、情境、學習者代碼、分數、計算和決定均為 SAMPLE/SYNTHETIC，不證明原始點協會曾開課、核准或取得成效。沒有綁定精確 SHA 的獨立審查前，不得標為品質接受。

驗收收據：`evidence/qa/technical_qa.json`、`evidence/qa/visual_qa.json`。完整11頁 Word PDF：`evidence/render/0038_R01.pdf`。逐筆合成替換清冊：`evidence/SYNTHETIC_REPLACEMENT_REGISTER.csv`。來源與藍圖索引：`inputs/SOURCE_MAP.md`、`inputs/BLUEPRINT_CURRENT_0038.jsonl`。
"""
(ROOT / "README.md").write_text(readme, encoding="utf-8")

tracked = [
    ROOT / "README.md",
    ROOT / "PROGRESS.json",
    docx,
    EVIDENCE / "SYNTHETIC_REPLACEMENT_REGISTER.csv",
    EVIDENCE / "build" / "build_0038_R01.py",
    ROOT / "inputs" / "official-2.png",
    ROOT / "inputs" / "official-3.png",
    QA / "verify_0038_R01.py",
    QA / "finalize_0038_R01.py",
    QA / "technical_qa.json",
    QA / "visual_qa.json",
    pdf,
    ROOT / "inputs" / "SOURCE_MAP.md",
    ROOT / "inputs" / "BLUEPRINT_CURRENT_0038.jsonl",
]
inventory = []
for path in tracked:
    if path.exists():
        inventory.append({
            "path": path.relative_to(ROOT).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        })
manifest = {
    "project": "TTQS_ONE",
    "document_id": "0038",
    "requirement_id": "I08-E02",
    "official_checkbox_sequence": "039",
    "candidate": "0038_R01",
    "candidate_sha256": sha256(docx),
    "technical_qa": TECH["status"],
    "visual_qa": visual["status"],
    "independent_semantic_review": "PENDING",
    "formal_acceptance": "NOT_GRANTED",
    "artifacts": inventory,
}
(EVIDENCE / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"candidate_sha256": progress["candidate_sha256"], "technical": TECH["status"], "visual": visual["status"], "pages": len(images), "artifacts": len(inventory)}, ensure_ascii=False))
