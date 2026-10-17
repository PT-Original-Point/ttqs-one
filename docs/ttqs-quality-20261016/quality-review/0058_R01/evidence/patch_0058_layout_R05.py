from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKER = ROOT / "worker" / "antigravity"
SOURCE = WORKER / "0058_CONTENT_R04.json"
TARGET = WORKER / "0058_CONTENT_R05.json"
content = json.loads(SOURCE.read_text(encoding="utf-8"))

old_sequence = content["front_matter"]["use_sequence"]
new_sequence = (
    "建議順序：(1) 先讀導讀與真實邊界；(2) 依第二節提案於課前建立基準及 SMART 計畫；"
    "(3) 課堂評分前後測；(4) 追蹤 30 日並核驗四欄紀錄；(5) 彙整個人、小組、組織成效；"
    "(6) 試算激勵提案；(7) 採用前核實第八節原件清冊，並另開第七節空白表。"
)
if old_sequence.count("另開新表") != 1:
    raise RuntimeError("Unexpected R04 front-matter sequence")
content["front_matter"]["use_sequence"] = new_sequence

old_step6 = (
    "建議於成效資料彙整後依核定流程安排檢討；本示範以學員 C、F 的合成情況演練障礙分析與補救規劃"
    "（如排班衝突、表格不熟、同儕提醒排班或拆解為短時練習），不表示真實會議已召開或輔導已提供。"
    "相關保存年限及權責依適用法規、已核定政策和章程查證，本件不推定協會現行處分制度，"
    "實際處置依核實之章程、核定制度及授權辦理。"
)
new_step6 = (
    "建議於成效資料彙整後，依核實授權安排檢討。C、F 的障礙（排班衝突、表格不熟）及同儕提醒、"
    "短時練習均為合成示範，不表示真實會議已召開或輔導已提供。保存年限與處置權責，"
    "應查核適用法規、章程及核定制度；不推定協會現行處分制度。"
)
step6_count = 0
for paragraph in content["sections"][1]["paragraphs"]:
    if old_step6 in paragraph:
        content["sections"][1]["paragraphs"][content["sections"][1]["paragraphs"].index(paragraph)] = paragraph.replace(old_step6, new_step6)
        step6_count += 1
if step6_count != 1:
    raise RuntimeError(f"Expected one R04 step-six paragraph; found {step6_count}")

content["metadata"]["revision"] = "R05_LAYOUT_REPAIR"
content["sections"][0]["tables"][0]["rows"][1][1] = "0058（版次 R05）"
content["sections"][9]["tables"][2]["rows"].append([
    "R05",
    "2026-10-18",
    "版面修復",
    "縮短首頁操作順序以收合孤立續行；收斂第二節步驟六段落；表 7-2 改於新頁開始，避免頁尾只留標題與表頭。未改案例數據。",
    "PRE_BUILD_SYNTHETIC_DRAFT / 待建置與審查",
])
TARGET.write_text(json.dumps(content, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

blueprint_r04 = WORKER / "0058_UNIQUE_BLUEPRINT_R04.md"
blueprint_r05 = WORKER / "0058_UNIQUE_BLUEPRINT_R05.md"
blueprint = blueprint_r04.read_text(encoding="utf-8")
blueprint += (
    "\n\n## R05 版面修復記錄（整合者）\n\n"
    "R04 以 Microsoft Word 匯出 PDF 並逐頁查看 31 頁接觸表後，定位三處可見問題：首頁操作順序框末行孤立於第 2 頁；"
    "第二節步驟六末句單獨延續至下一頁；表 7-2 標題及表頭位於第 22 頁頁底而資料列從第 23 頁開始。"
    "R05 縮短操作順序與步驟六文字，並讓表 7-2 標題於新頁開始；沒有新增案例事實或改動任何公式、分子、分母及結果。"
    "R05 狀態仍為 PRE_BUILD_SYNTHETIC_DRAFT，待重新建置、渲染及獨立 exact-SHA 審查。\n"
)
blueprint_r05.write_text(blueprint, encoding="utf-8")

csv_r04 = WORKER / "0058_SYNTHETIC_REPLACEMENT_REGISTER_R04.csv"
csv_r05 = WORKER / "0058_SYNTHETIC_REPLACEMENT_REGISTER_R05.csv"
shutil.copyfile(csv_r04, csv_r05)

builder_r04 = WORKER / "0058_build_R04.py"
builder_r05 = WORKER / "0058_build_R05.py"
builder = builder_r04.read_text(encoding="utf-8")
if "0058_CONTENT_R04.json" not in builder or "0058_R04.docx" not in builder:
    raise RuntimeError("Unexpected R04 builder contract")
builder = builder.replace("R04", "R05")
needle = "            cap_p.paragraph_format.keep_with_next = True\n"
replacement = (
    needle
    + "            if caption.startswith(\"表 7-2\"):\n"
    + "                cap_p.paragraph_format.page_break_before = True\n"
)
if builder.count(needle) != 1:
    raise RuntimeError("Could not locate unique caption keep-with-next rule")
builder = builder.replace(needle, replacement)
needle_para = "            p.paragraph_format.line_spacing = 1.25\n"
replacement_para = needle_para + "            p.paragraph_format.widow_control = True\n"
if builder.count(needle_para) != 1:
    raise RuntimeError("Could not locate unique body paragraph style rule")
builder = builder.replace(needle_para, replacement_para)
builder_r05.write_text(builder, encoding="utf-8")

outputs = [blueprint_r05, TARGET, csv_r05, builder_r05]
manifest = {
    "operation": "targeted_layout_repair",
    "source_revision": "R04",
    "target_revision": "R05",
    "source_docx_sha256": "76266A3E4CB0846D6B179C875F780BBEEB5B664B5279D82EC1D4C4699CB9F246",
    "source_pdf_pages": 31,
    "findings": [
        "Front-matter usage-box final line orphaned at top of page 2",
        "Section 2 step-six paragraph had a short spill line on page 5",
        "Table 7-2 caption/header orphaned at page 22 bottom before data rows on page 23",
    ],
    "fixes": [
        "Shortened front-matter usage sequence without changing operating steps",
        "Shortened step-six proposal paragraph while preserving synthetic boundary and authority checks",
        "Set page_break_before on Table 7-2 caption; enabled widow control for body paragraphs",
    ],
    "synthetic_facts_count": len(content["synthetic_facts"]),
    "docx_built": False,
    "outputs": [
        {"path": str(p.relative_to(ROOT)), "bytes": p.stat().st_size, "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
        for p in outputs
    ],
}
manifest_path = ROOT / "evidence" / "patch_0058_layout_R05.json"
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(manifest, ensure_ascii=False, indent=2))
