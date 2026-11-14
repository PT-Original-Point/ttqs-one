from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
EVIDENCE = BASE / "evidence"
OLD = json.loads((EVIDENCE / "render_R07/render_manifest_R07.json").read_text(encoding="utf-8"))
NEW = json.loads((EVIDENCE / "render_R08/render_manifest_R08.json").read_text(encoding="utf-8"))
DOCX = BASE / "candidate/0060_R08.docx"
PDF = EVIDENCE / "render_R08/0060_R08_Word_export.pdf"
EXPECTED = "92962DF774A7A16546829D8968DC274394FC1EFCC12421C1A355F45127E9B5C3"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main() -> None:
    if NEW["candidate_sha256"] != EXPECTED or sha(DOCX) != EXPECTED:
        raise SystemExit("R08 candidate SHA mismatch")
    if NEW["page_count"] != 26 or NEW["rendered_png_count"] != 26:
        raise SystemExit("Unexpected R08 render page count")
    changed = [p["page"] for p in OLD["pages"] if p["sha256"] != NEW["pages"][p["page"] - 1]["sha256"]]
    if changed != [18, 19, 20, 23]:
        raise SystemExit(f"Unexpected changed-page set: {changed}")
    directly_inspected = [18, 19, 20, 23]
    receipt = {
        "doc_id": "0060",
        "requirement_id": "I14-E01",
        "official_checkbox": "065",
        "candidate_revision": "R08",
        "candidate_sha256": EXPECTED,
        "pdf_sha256": sha(PDF),
        "render_manifest_sha256": sha(EVIDENCE / "render_R08/render_manifest_R08.json"),
        "page_count": 26,
        "rendered_png_count": 26,
        "comparison_baseline": "R07 rendered page hashes",
        "changed_pages": changed,
        "unchanged_pages_exact_hash_match": 22,
        "directly_inspected_full_resolution_pages": directly_inspected,
        "direct_inspection_findings": {
            "page_18": "Rows 04-07 readable; RSC correction, ATT relabel and DLG locator remain within table cells; no clipping or overlap.",
            "page_19": "ASM denominator/assessment explanation, FDB/FUP cohort links, and EXC three baseline rates readable; table rows and repeated header align.",
            "page_20": "IMP row is clean; Chapter 10 calculations and denominator-zero N/A rule readable; no collision with following bullets or footer.",
            "page_23": "Completed classification worksheet displays the final -V01 code fully within the output cell; no clipping or row overflow.",
        },
        "page_visual_status": "PASS_FOR_CHANGED_PAGES; 22 byte-identical page images inherit R07 review chain",
        "semantic_acceptance": "NOT_ESTABLISHED_BY_THIS_VISUAL_RECEIPT",
        "reviewer": "Coordinator direct inspection of exact R08 rendered page images",
        "reviewed_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    (EVIDENCE / "visual_review_R08.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md = f"""# DOCX 0060 R08 視覺檢查收據

- 官方身份：0060 / I14-E01 / checkbox 065
- DOCX SHA-256：`{EXPECTED}`
- Word 匯出 PDF SHA-256：`{receipt['pdf_sha256']}`
- R08 render manifest SHA-256：`{receipt['render_manifest_sha256']}`
- R08 共 26 頁並產生 26 張非空白 PNG。與 R07 逐頁雜湊比較後，僅第 18、19、20、23 頁影像改變；其餘 22 頁逐位元組相同，沿用 R07 的已檢查版面鏈。
- 本次以完整頁面解析度直接檢查第 18、19、20、23 頁。四頁均可讀；修正文字留在正確表格儲存格，沒有裁切、重疊或列溢位。

## 逐頁結果

- 第 18 頁：RSC 重複碼更正、ATT 標籤更正、DLG 定位碼均可讀，未溢出欄位。
- 第 19 頁：ASM 評量分母、FDB/FUP 案例關聯及 EXC 三項初始比率清楚；表格續頁表頭與列界線正常。
- 第 20 頁：IMP 列乾淨；Chapter 10 的百分比與分母為零時標示 N/A 的規則可讀，和後續項目及頁尾沒有碰撞。
- 第 23 頁：已填範例輸出欄完整顯示以 `-V01` 結尾的代碼，沒有裁切或列高異常。

## 範圍限制

此收據只判斷版面與可讀性，不構成語意驗收或正式接受。精確頁面雜湊、檢查範圍與本機輸出時間記錄於同目錄 JSON 收據。
"""
    (EVIDENCE / "visual_review_R08.md").write_text(md, encoding="utf-8", newline="\n")
    print(json.dumps({"candidate_sha256": EXPECTED, "pdf_sha256": receipt["pdf_sha256"], "changed_pages": changed, "directly_inspected": directly_inspected, "unchanged_pages": 22}, ensure_ascii=False))


if __name__ == "__main__":
    main()
