import csv
import hashlib
import json
from pathlib import Path

root = Path(r"E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0059_R01")
d = root / "review" / "opencode_deepseek_register_R02"
base_csv = root / "review" / "opencode_deepseek_register_R01" / "replacement_register_R01.csv"
register = d / "replacement_register_R02.csv"
receipt_path = d / "assembly_receipt_R02.json"
docx = root / "0059_R03.docx"

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest().upper()

def read(p):
    with p.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

fields = ["fact_id", "locator", "value", "why_synthetic", "source_to_replace", "role_to_verify", "status"]
old, new = read(base_csv), read(register)
assert len(old) == 190
assert len(new) == 270
assert list(new[0]) == fields
assert len({r["fact_id"] for r in new}) == 270
assert [r["fact_id"] for r in new] == [f"SYN-0059-113-F{i:03d}" for i in range(1, 271)]
assert all(r["status"] == "SAMPLE_UNVERIFIED" for r in new)
assert all(all((r[k] or "").strip() for k in fields) for r in new)

corrections = {"SYN-0059-113-F063"} | {f"SYN-0059-113-F{i:03d}" for i in range(105, 117)}
for before, after in zip(old, new):
    assert before["fact_id"] == after["fact_id"]
    for key in fields:
        if key == "locator" and before["fact_id"] in corrections:
            continue
        assert before[key] == after[key], (before["fact_id"], key, before[key], after[key])
assert new[62]["locator"].startswith("§4.3") and "§4.4" in new[62]["locator"]
for n in range(105, 117):
    row = next(r for r in new if r["fact_id"] == f"SYN-0059-113-F{n:03d}")
    assert "§5.4" in row["locator"] and f"第{n-104}列" in row["locator"]

def contains(fragment):
    return any(fragment in r["value"] for r in new)
required = [
    "Q1｜機制有用性｜有效作答數 15｜總和 63｜平均 4.2",
    "Q2｜機制有用性｜有效作答數 12｜總和 48｜平均 4.0",
    "Q3｜機制有用性｜有效作答數 15｜總和 60｜平均 4.0",
    "Q4｜機制有用性｜有效作答數 9｜總和 38｜平均 4.2",
    "209 ÷ 51 ＝ 4.1",
    "228 ÷ 60 ＝ 3.8",
    "120 ÷ 30 ＝ 4.0",
    "16÷18",
    "88.9%",
    "1 ÷ 2 ＝ 50.0%",
    "4÷12＝33.3%",
]
for item in required:
    assert contains(item), item
for q in range(5, 9):
    assert contains(f"Q{q}｜遷移自評｜有效作答數 15｜總和 57｜平均 3.8"), q
for q in (9, 10):
    assert contains(f"Q{q}｜") and contains("總和 60｜平均 4.0")
for imp in range(1, 6):
    assert contains(f"IMP-0{imp}")
for reject in range(1, 11):
    assert any(r["locator"] == f"§12.3 退回（REJECT）條件 第{reject}項" for r in new)
for hold in range(1, 8):
    assert any(r["locator"] == f"§12.4 HOLD 條件 第{hold}項" for r in new)

receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
assert receipt["candidate_docx_sha256"] == sha(docx)
assert receipt["register_r02_sha256"] == sha(register)
assert receipt["independent_review_status"] == "PENDING"
result = {
    "doc_id": "0059",
    "candidate_docx_sha256": sha(docx),
    "register_r01_sha256": sha(base_csv),
    "register_r02_sha256": sha(register),
    "rows": len(new),
    "inherited_rows_unchanged_except_locators": 190,
    "locator_corrections": 13,
    "new_rows": 80,
    "checks": {
        "identity_and_contiguous_ids": "PASS",
        "seven_column_schema_and_no_blanks": "PASS",
        "all_rows_sample_unverified": "PASS",
        "R01_inherited_value_parity": "PASS",
        "locator_precision": "PASS",
        "questionnaire_and_denominators": "PASS",
        "dedup_and_retest_arithmetic": "PASS",
        "IMP01_to_IMP05_and_reject_hold": "PASS",
        "candidate_sha_binding": "PASS",
        "register_sha_binding": "PASS",
    },
    "status": "PASS_TECHNICAL_SCOPE",
    "independent_review": "PENDING",
}
(d / "technical_validation_R02.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False))

