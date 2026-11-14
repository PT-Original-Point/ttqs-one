import csv
import hashlib
import json
from datetime import datetime
from pathlib import Path

root = Path(r"E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0059_R01")
out = root / "review" / "opencode_deepseek_register_R02"
body_path = root / "worker" / "opencode" / "0059_DOCUMENT_BODY_R03_FINAL.md"
docx_path = root / "0059_R03.docx"
base_csv = root / "review" / "opencode_deepseek_register_R01" / "replacement_register_R01.csv"
model_json = out / "model_response_R02_format_repair.json"
response_raw = out / "stdout_R02.jsonl"
response_repaired = out / "model_response_R02_format_repair.json"

def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()

with base_csv.open("r", encoding="utf-8-sig", newline="") as f:
    original = list(csv.DictReader(f))
fields = ["fact_id", "locator", "value", "why_synthetic", "source_to_replace", "role_to_verify", "status"]
assert len(original) == 190, f"expected 190 R01 rows, got {len(original)}"
assert list(original[0]) == fields, list(original[0])
for n, row in enumerate(original, 1):
    assert row["fact_id"] == f"SYN-0059-113-F{n:03d}", row["fact_id"]

response = json.loads(model_json.read_text(encoding="utf-8-sig"))
patches = {item["fact_id"]: item["new_locator"] for item in response["locator_corrections"]}
assert len(patches) == 13
assert set(patches) == {"SYN-0059-113-F063"} | {f"SYN-0059-113-F{i:03d}" for i in range(105, 117)}
for row in original:
    if row["fact_id"] in patches:
        row["locator"] = patches[row["fact_id"]]

raw_additions = response["additional_rows"]
keep_numbers = set(range(191, 250)) | set(range(253, 259))
drop_numbers = {216, 225}
selected = []
old_to_new = {}
next_num = 191
for row in raw_additions:
    old_num = int(row["fact_id"].rsplit("F", 1)[1])
    if old_num not in keep_numbers or old_num in drop_numbers:
        continue
    old_to_new[old_num] = next_num
    new = {key: row[key] for key in fields}
    new["fact_id"] = f"SYN-0059-113-F{next_num:03d}"
    assert new["status"] == "SAMPLE_UNVERIFIED", new
    selected.append(new)
    next_num += 1
assert len(selected) == 63, len(selected)

reject_rules = [
    "成為移轉會議報告（與 0057 重疊）",
    "成為個人行動／團隊績效報告（與 0058 重疊）",
    "成為設施設備點檢證據包（與 0056 重疊）",
    "成為通用 SOP，欠缺四機制各自的完成示例",
    "成為空白表或僅有表頭無內容",
    "成為心得散文或單一心得，欠缺平台運作與審查機制",
    "成為純證照清單，欠缺查證與狀態字典",
    "將 DOCX 0059 對應到勾選單 060",
    "使用 0058 案例事實或推定跨文件共享事實",
    "出現待填／待核／空白表字樣（除明確標示之 REAL 替換區）",
]
hold_rules = [
    "欠缺真實機關授權或核准",
    "欠缺當事人同意或隱私處理依據",
    "欠缺來源原件或獨立查證",
    "欠缺安置／安全／監督之合法依據",
    "欠缺分母或排除規則，致比率無法重算",
    "模擬實作被描述為 REAL 實習",
    "成效被描述為已核准或已生效",
]
manual = []
n = next_num
for i, rule in enumerate(reject_rules, 1):
    manual.append({
        "fact_id": f"SYN-0059-113-F{n:03d}",
        "locator": f"§12.3 退回（REJECT）條件 第{i}項",
        "value": rule,
        "why_synthetic": "候選文件提出的退件控制；尚未核定為協會既行制度，非 REAL 紀錄。",
        "source_to_replace": "協會有權單位正式核定的文件接受與退回準則（尚未取得；UNKNOWN）。",
        "role_to_verify": "理監事或正式授權之審議角色（待核實，不代表已任命）。",
        "status": "SAMPLE_UNVERIFIED",
    })
    n += 1
for i, rule in enumerate(hold_rules, 1):
    manual.append({
        "fact_id": f"SYN-0059-113-F{n:03d}",
        "locator": f"§12.4 HOLD 條件 第{i}項",
        "value": rule,
        "why_synthetic": "候選文件提出的暫停控制；尚未核定為協會既行制度，非 REAL 紀錄。",
        "source_to_replace": "協會正式核定的 HOLD 流程與適用依據（尚未取得；UNKNOWN）。",
        "role_to_verify": "理監事或正式授權之品質管理角色（待核實，不代表已任命）。",
        "status": "SAMPLE_UNVERIFIED",
    })
    n += 1
assert len(manual) == 17

rows = original + selected + manual
assert len(rows) == 270
assert [row["fact_id"] for row in rows] == [f"SYN-0059-113-F{i:03d}" for i in range(1, 271)]
for row in rows:
    assert list(row) == fields
    assert all(str(row[k]).strip() for k in fields), row["fact_id"]
    assert row["status"] == "SAMPLE_UNVERIFIED", row["fact_id"]

register_path = out / "replacement_register_R02.csv"
with register_path.open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields, extrasaction="raise")
    writer.writeheader()
    writer.writerows(rows)

addition_path = out / "additions_R02.csv"
with addition_path.open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields, extrasaction="raise")
    writer.writeheader()
    writer.writerows(selected + manual)

def mapped(old_num):
    if old_num in old_to_new:
        return f"SYN-0059-113-F{old_to_new[old_num]:03d}"
    return f"SYN-0059-113-F{old_num:03d}"

q_ids = [f"SYN-0059-113-F{i:03d}" for i in (17, 188, 189, 190)] + [mapped(i) for i in range(191, 215)]
dedup_ids = [f"SYN-0059-113-F{i:03d}" for i in (26, 100, 118, 119, 158, 215)] + [mapped(i) for i in (217, 218, 219)]
score_ids = [f"SYN-0059-113-F{i:03d}" for i in range(183, 188)] + [mapped(i) for i in list(range(220, 225)) + [226, 227]]
improve_ids = [f"SYN-0059-113-F{i:03d}" for i in (103, 120, 160)] + [mapped(i) for i in range(228, 240)]
hold_ids = [f"SYN-0059-113-F{i:03d}" for i in (79, 80, 81, 97, 98, 99, 104, 167, 184)] + [mapped(i) for i in range(240, 250)] + [row["fact_id"] for row in manual]
scenario_ids = [mapped(i) for i in range(253, 259)]
coverage = {
    "project_id": "TTQS_ONE",
    "doc_id": "0059",
    "requirement_id": "I13-E03",
    "official_checkbox_serial": "063",
    "candidate_docx_sha256": sha(docx_path),
    "register_revision": "R02",
    "register_sha256": sha(register_path),
    "rows": len(rows),
    "coverage": [
        {"gap": "問卷同意、跳題、N/A與未回覆排除、各題統計及指數計算", "fact_ids": q_ids},
        {"gap": "跨機制彙整、去重定義與實質參與率", "fact_ids": dedup_ids},
        {"gap": "首測構面平均、補強與重測統計", "fact_ids": score_ids},
        {"gap": "IMP-01至IMP-05、NOT ADOPTED、責任提案、證據與HOLD，以及退補件率", "fact_ids": improve_ids},
        {"gap": "六項REAL替換地圖、四項附錄B替換控制及拒退/HOLD條件", "fact_ids": hold_ids},
        {"gap": "SAMPLE安全演練與無真實個資/停止條件", "fact_ids": scenario_ids},
        {"gap": "定位精細度", "fact_ids": [f"SYN-0059-113-F{i:03d}" for i in [63, *range(105, 117)]]},
    ],
    "scope_exclusions": [
        {"locator": "§2.1-§2.2", "classification": "official_source_fact", "reason": "官方需求與原文不是合成資料；保留在來源/Blueprint 對照，不列入SAMPLE替換清冊。"},
        {"locator": "§12.6", "classification": "author_self_check", "reason": "正文明示不是獨立驗收；不得把撰寫者自述當成待替換實績或獨立品質證據。"},
        {"locator": "§12.7", "classification": "quality_process_control", "reason": "綁定最終DOCX SHA的驗收程序，不是合成案例事實；以驗收收據管理。"},
    ],
    "duplicate_rows_removed": [
        {"model_fact_id": "SYN-0059-113-F216", "retained_as": "SYN-0059-113-F215", "reason": "相同16/18=88.9%去重率的表列與重述計算，合併避免重複登錄。"},
        {"model_fact_id": "SYN-0059-113-F225", "retained_as": "SYN-0059-113-F187", "reason": "同一116/50=2.32→2.3構面平均已於原清冊登錄；新列僅是另一章重述。"},
    ],
    "body_precedence_note": "MiMo coverage-gap note described Q2 as 48/15, but the R03 body and DeepSeek extraction state Q2 has 12 valid responses and 48/12=4.0. R02 records the body value and preserves this discrepancy for independent check.",
    "independent_review_status": "PENDING",
}
coverage_path = out / "coverage_map_R02.json"
coverage_path.write_text(json.dumps(coverage, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

scope_path = out / "register_scope_R02.md"
scope_path.write_text(
    "# DOCX 0059 R02 replacement-register scope\n\n"
    f"- Mapping: DOCX 0059 / I13-E03 / official checkbox 063.\n"
    f"- Candidate DOCX SHA-256: {coverage['candidate_docx_sha256']} (unchanged).\n"
    f"- R01 register SHA-256: {sha(base_csv)}.\n"
    f"- R02 register SHA-256: {coverage['register_sha256']}; {len(rows)} rows; 190 inherited rows, 80 additions.\n"
    "- The original 190 facts were retained; only the 13 locators F063 and F105-F116 were clarified.\n"
    "- Two duplicate additions were removed (F216 merged into F215; F225 retained through existing F187).\n"
    "- Added 63 selected DeepSeek rows and 17 explicit REJECT/HOLD controls copied from body sections 12.3-12.4. These controls remain SAMPLE_UNVERIFIED and are not asserted as Association policy.\n"
    "- Official-source statements (§2), the author checklist (§12.6), and the SHA-bound QA control (§12.7) are classified separately; they are not sample facts or independent acceptance evidence.\n"
    "- The DeepSeek response had one incomplete JSON boundary at F262. A deterministic format-only repair restored the missing fields using the identical field values used by adjacent checklist rows; the original raw stdout is preserved.\n"
    "- The MiMo audit summary contained a Q2 denominator discrepancy. The final body states 12 valid answers, 48/12=4.0; the R02 register follows the body and flags this for independent verification.\n"
    "- No DOCX bytes were changed. The R02 sidecar is a candidate pending independent exact-SHA review.\n",
    encoding="utf-8",
)

receipt = {
    "project_id": "TTQS_ONE",
    "doc_id": "0059",
    "requirement_id": "I13-E03",
    "official_checkbox_serial": "063",
    "candidate_docx_sha256": coverage["candidate_docx_sha256"],
    "register_r01_sha256": sha(base_csv),
    "register_r02_sha256": coverage["register_sha256"],
    "register_rows": len(rows),
    "inherited_rows": len(original),
    "supplemental_rows": len(selected) + len(manual),
    "locator_corrections": len(patches),
    "duplicate_rows_removed": 2,
    "source_of_additions": "OpenCode V2 DeepSeek first-pass response plus deterministic duplicate/scope review and body-grounded acceptance controls.",
    "format_repair": {
        "raw_stdout_sha256": sha(response_raw),
        "parsed_response_sha256": sha(response_repaired),
        "repair": "At F262 only, deterministic insertion of source_to_replace, role_to_verify, and SAMPLE_UNVERIFIED fields to close one malformed JSON object boundary. No row value or source fact changed."
    },
    "q2_discrepancy": "MiMo's gap note cited 48/15; body and DeepSeek extraction show 48 valid points over 12 answers, 4.0. Kept body value and flagged for independent reviewer.",
    "docx_modified": False,
    "status": "READY_FOR_INDEPENDENT_REVIEW",
    "independent_review_status": "PENDING",
    "created_at_local": datetime.now().astimezone().isoformat(timespec="seconds"),
}
receipt_path = out / "assembly_receipt_R02.json"
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(json.dumps({
    "candidate_docx_sha256": coverage["candidate_docx_sha256"],
    "register_r01_sha256": receipt["register_r01_sha256"],
    "register_r02_sha256": coverage["register_sha256"],
    "rows": len(rows),
    "inherited": len(original),
    "supplemental": len(selected) + len(manual),
    "locator_corrections": len(patches),
    "manual_reject_hold_controls": len(manual),
    "status": "READY_FOR_INDEPENDENT_REVIEW",
}, ensure_ascii=False))
