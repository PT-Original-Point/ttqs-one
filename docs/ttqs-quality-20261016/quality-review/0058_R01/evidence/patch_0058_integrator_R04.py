from __future__ import annotations

import csv
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKER = ROOT / "worker" / "antigravity"
SOURCE = WORKER / "0058_CONTENT_R03.json"
TARGET = WORKER / "0058_CONTENT_R04.json"

content = json.loads(SOURCE.read_text(encoding="utf-8"))
counts: dict[str, int] = {}

replacements = [
    (
        "本文件存在的唯一核心目的，是為了解決小型志工協會於訓練成果移轉機制規劃時常見之「追蹤無工具、成效缺標準、缺乏改善輔導機制」等規劃瓶頸。透過具體的個人 SMART 行動計畫、結構化之四步服務行為量規、四欄完整紀錄查核標準、同儕互助機制及團隊成效試算方案，建立完整的評量與改善閉環提案。本文件案例示範內容完整，另附與案例分離的空白操作表供未來現場使用。",
        "本文件旨在提供小型志工協會規劃訓後成果移轉時，可供審議與試作的操作參考。內容以個人 SMART 行動計畫、四步服務行為量規、四欄完整紀錄查核、同儕支持及團隊成效試算，示範如何串接評量、追蹤與改善；不表示協會目前缺少上述工具或制度。本文件案例示範內容完整，另附與案例分離的空白操作表供未來採用時參考。",
    ),
    (
        "本工具訂定結構化之四步服務行為量規（Rubric）",
        "本示範工具提出結構化之四步服務行為量規（Rubric）",
    ),
    (
        "此量規於課堂情境演練（模擬前測與模擬後測）中統一使用，作為客觀衡量標準。",
        "若經核定於課堂情境演練（模擬前測與模擬後測）採用，評分時建議一致使用此量規，作為本示範的衡量標準。",
    ),
    (
        "協會並可由建議輔導人員定期提供諮詢輔導，針對紀錄填寫或服務界線疑義提供具體建議。",
        "若協會核實授權並採用本提案，可由章程授權者指定之輔導者依核定安排提供諮詢；本示範不代表協會現行已提供該服務。",
    ),
    (
        "召開訓後成效檢討會議。針對未能達標或未能提交證據之學員（如本案學員 C 與 F），分析障礙原因（如排班衝突、表格不熟），擬定後續補救措施（如同儕提醒排班、拆解為短時練習）。",
        "建議於成效資料彙整後依核定流程安排檢討；本示範以學員 C、F 的合成情況演練障礙分析與補救規劃（如排班衝突、表格不熟、同儕提醒排班或拆解為短時練習），不表示真實會議已召開或輔導已提供。",
    ),
    (
        "召開訓後成效檢討會議，針對未達標或缺證據學員訂定補救計畫，妥善歸檔",
        "建議彙整示範成效並規劃檢討與補救；正式作業依核實之授權與核定流程辦理",
    ),
    (
        "本機制要求每位參訓學員依據 SMART 原則",
        "本示範工具建議參訓學員依據 SMART 原則",
    ),
    (
        "本機制制定嚴謹之「服務關懷紀錄四欄完整度檢驗標準」",
        "本示範工具提出「服務關懷紀錄四欄完整度檢驗標準」",
    ),
    (
        "未經理事會核定、未設立、未生效、未實際執行、未發放實質獎品或金錢",
        "尚未經章程授權者核定、未設立、未生效、未實際執行、未發放實質獎品或金錢",
    ),
    (
        "任何正式激勵方案採行前，必須依協會組織章程送交理事會審議核定。",
        "任何正式激勵方案採行前，須先核對組織章程與授權層級，並由具權限者依核定程序審議；本文件不預設特定核定機關。",
    ),
    (
        "此外，設立倫理防弊條款提案：",
        "此外，本提案建議納入倫理防弊條款：",
    ),
    (
        "交有權者依核實之章程與現行制度查處，該小組不列入該期獎勵評比",
        "交由具權限者依核實之章程與制度處理；若無可核實之處置依據，應先暫緩採行，不自行設定處分。該小組不列入本示範期獎勵試算",
    ),
    (
        "本會行政人員或志工幹部於日常辦理實體訓練或現場督導時，可直接複製、列印或另開新檔使用。",
        "協會未來如經核定採用，可由章程授權者指定之承辦人員，依實際訓練或現場督導需要複製、列印或另存新檔；本文件不推定目前已有特定行政職務或日常辦理情形。",
    ),
    (
        "由志工督導審閱紀錄正本，核定是否達標並給予後續建議",
        "示範欄位：由章程授權者指定之覆核者查驗紀錄來源並提出達標判讀建議；正式核定依核實授權流程辦理",
    ),
    (
        "未獲理事會核准，未設立未生效，未實際發給獎勵",
        "尚未經章程授權者核定，未設立未生效，未實際發給獎勵",
    ),
    (
        "協會行政檔案卷宗 / 理事會核定案",
        "協會行政檔案卷宗／具權限者之核定文件（如存在）",
    ),
    (
        "理事會會議紀錄或章程授權規章",
        "章程授權者之核定文件或相關授權規章（若存在）",
    ),
    (
        "依現行制度查證處理",
        "依核實之章程、核定制度及授權程序查證處理；如無可核實來源，維持 UNKNOWN",
    ),
]


def apply(node):
    if isinstance(node, dict):
        for key, value in node.items():
            node[key] = apply(value)
        return node
    if isinstance(node, list):
        return [apply(value) for value in node]
    if isinstance(node, str):
        for old, new in replacements:
            n = node.count(old)
            if n:
                counts[old] = counts.get(old, 0) + n
                node = node.replace(old, new)
        return node
    return node


content = apply(content)
for old, _ in replacements:
    if counts.get(old, 0) < 1:
        raise RuntimeError(f"Expected source phrase not found: {old}")

content["metadata"]["revision"] = "R04_INTEGRATOR_BOUNDARY_COPYEDIT"
content["sections"][0]["tables"][0]["rows"][1][1] = "0058（版次 R04）"
content["sections"][9]["tables"][2]["rows"].append([
    "R04",
    "2026-10-18",
    "授權與提案邊界再校正",
    "修正 R03 仍殘留的既有行政/督導職務、特定核定機關及現行制度用語；明確標示表單與流程為待核定提案；未新增合成案例數據。",
    "PRE_BUILD_SYNTHETIC_DRAFT / 待建置與審查",
])

TARGET.write_text(json.dumps(content, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

blueprint_r03 = WORKER / "0058_UNIQUE_BLUEPRINT_R03.md"
blueprint_r04 = WORKER / "0058_UNIQUE_BLUEPRINT_R04.md"
blueprint_text = blueprint_r03.read_text(encoding="utf-8")
blueprint_text += "\n\n## R04 整合修補記錄（非 Antigravity 回覆）\n\n"
blueprint_text += (
    "整合者逐段核查 R03 JSON 後，發現 R03 Antigravity 自述已排除現況推定，但正文仍含「本會行政人員或志工幹部」及「依現行制度」等未證實表述，"
    "並以理事會為預設核定機關。為避免把職務、服務、政策或授權寫成協會既有事實，R04 以可定位文字修正：將空白表單定位為未來核定後由授權者指定人員使用；"
    "把檢討、輔導、量規與獎勵流程改為明確提案；核定權限改以核實章程與授權層級為準；清除「依現行制度」而無來源的指示。\n\n"
    "只修訂治理/提案邊界措辭並新增版次紀錄，未改動既定案例日期、人物代碼、分子分母、分數或結果；41 筆 synthetic facts 與 CSV 預期保持一對一。"
    " R04 狀態仍為 PRE_BUILD_SYNTHETIC_DRAFT，尚未建置、渲染或獨立審查。\n"
)
blueprint_r04.write_text(blueprint_text, encoding="utf-8")

csv_r03 = WORKER / "0058_SYNTHETIC_REPLACEMENT_REGISTER_R03.csv"
csv_r04 = WORKER / "0058_SYNTHETIC_REPLACEMENT_REGISTER_R04.csv"
shutil.copyfile(csv_r03, csv_r04)

builder_r03 = WORKER / "0058_build_R03.py"
builder_r04 = WORKER / "0058_build_R04.py"
builder_text = builder_r03.read_text(encoding="utf-8")
if "0058_CONTENT_R03.json" not in builder_text or "0058_R03.docx" not in builder_text:
    raise RuntimeError("R03 builder input/output contract did not match expected paths")
builder_text = builder_text.replace("R03", "R04")
builder_r04.write_text(builder_text, encoding="utf-8")

out_files = [blueprint_r04, TARGET, csv_r04, builder_r04]
manifest = {
    "operation": "integrator_targeted_copyedit",
    "source_revision": "Antigravity R03 output",
    "target_revision": "R04",
    "source_content_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    "replacement_occurrences": {old: counts[old] for old, _ in replacements},
    "source_fact_count": len(json.loads(SOURCE.read_text(encoding="utf-8"))["synthetic_facts"]),
    "target_fact_count": len(content["synthetic_facts"]),
    "target_outputs": [
        {"path": str(p.relative_to(ROOT)), "bytes": p.stat().st_size, "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
        for p in out_files
    ],
    "docx_built": False,
    "qa_status": "NOT_YET_RUN",
}
manifest_path = ROOT / "evidence" / "patch_0058_integrator_R04.json"
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(manifest, ensure_ascii=False, indent=2))
