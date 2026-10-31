#!/usr/bin/env python3
import csv, hashlib, json, re
from pathlib import Path

base = Path(__file__).resolve().parents[1]
blueprint = base / "inputs" / "UNIQUE_BLUEPRINT_0083_R03.md"
out = base / "candidate" / "SYNTHETIC_REPLACEMENT_REGISTER_0083_R03.csv"
lines = blueprint.read_text(encoding="utf-8-sig").splitlines()
rows = []
in_register = False
for line in lines:
    if "逐原子事實替換清冊" in line:
        in_register = True
    if in_register:
        m = re.match(r"^\|\s*(R-\d{3})\s*\|", line)
        if m:
            cells = [x.strip().replace("\\|", "|").replace("`", "") for x in line.strip().strip("|").split("|")]
            if len(cells) != 6:
                raise SystemExit(f"Expected 6 register columns at {m.group(1)}, got {len(cells)}")
            rows.append(cells)
        if line.startswith("確定性 QA 必須"):
            break
ids = [int(r[0][2:]) for r in rows]
if ids != list(range(1, 82)):
    raise SystemExit(f"Register ID sequence invalid: count={len(ids)} first={ids[:1]} last={ids[-1:]}")
out.parent.mkdir(parents=True, exist_ok=True)
with out.open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f, lineterminator="\n")
    writer.writerow(["REG_ID", "欄位定位", "值", "類別", "替換來源/條件", "狀態"])
    writer.writerows(rows)
report = {
    "schema": "ttqs-0083-replacement-register-extraction-v1",
    "source_blueprint_sha256": hashlib.sha256(blueprint.read_bytes()).hexdigest(),
    "csv_path": str(out),
    "csv_sha256": hashlib.sha256(out.read_bytes()).hexdigest(),
    "csv_bytes": out.stat().st_size,
    "rows_excluding_header": len(rows),
    "first_id": rows[0][0],
    "last_id": rows[-1][0],
    "result": "PASS_EXTRACTION_ONLY_NOT_SEMANTIC_ACCEPTANCE",
}
(base / "evidence" / "replacement_register_receipt_R01.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=True))
