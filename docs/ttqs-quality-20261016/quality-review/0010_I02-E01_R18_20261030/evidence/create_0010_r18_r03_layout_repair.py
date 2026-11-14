from __future__ import annotations

from datetime import datetime
from hashlib import sha256
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030")
DOCX_R18_R02 = ROOT / "candidate" / "0010_I02-E01_R18_R02.docx"
QA_R18_R02 = ROOT / "qa" / "TECHNICAL_QA_R18_R02_RECHECK.json"
SOURCE_R18_R02 = ROOT / "worker" / "0010_I02-E01_R18_R02.md"
REGISTER_R17_R02 = ROOT / "worker" / "SYNTHETIC_REGISTER_R17_R02.md"
BUILDER_R18_R02 = ROOT / "qa" / "build_0010_r18_r02_docx.py"
QA_SCRIPT_R18_R02 = ROOT / "qa" / "technical_qa_0010_r18_r02_recheck.py"

BUILDER_R18_R03 = ROOT / "qa" / "build_0010_r18_r03_docx.py"
DOCX_R18_R03 = ROOT / "candidate" / "0010_I02-E01_R18_R03.docx"
QA_SCRIPT_R18_R03 = ROOT / "qa" / "technical_qa_0010_r18_r03.py"
QA_R18_R03 = ROOT / "qa" / "TECHNICAL_QA_R18_R03.json"
RECEIPT_R18_R03 = ROOT / "qa" / "R18_R03_LAYOUT_REPAIR_RECEIPT.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


if digest(DOCX_R18_R02) != "0d96822b45a2473590f2cde20350908c4e07ad4417eb6786958c7554e37c937d":
    raise SystemExit("R18 R02 candidate changed; reconcile before a layout-only repair.")
if json.loads(QA_R18_R02.read_text(encoding="utf-8-sig")).get("all_checks_pass") is not True:
    raise SystemExit("R18 R02 technical recheck is not PASS; stop before layout repair.")
if any(p.exists() for p in (DOCX_R18_R03, QA_SCRIPT_R18_R03, QA_R18_R03, RECEIPT_R18_R03)):
    raise SystemExit("An R18 R03 candidate or receipt exists; reconcile exact hashes before continuing.")

builder = BUILDER_R18_R02.read_text(encoding="utf-8-sig")
old_widths = "(7,'ev id'):[1.70,.82,.72,.60,4.65,.72,1.34]"
new_widths = "(7,'ev id'):[1.50,.75,.75,4.20,1.35,.55,1.45]"
if builder.count(old_widths) != 1:
    raise SystemExit("Could not uniquely locate the misallocated seven-column EV table widths.")
builder = builder.replace(old_widths, new_widths, 1)
builder = builder.replace("0010_I02-E01_R18_R02.docx", "0010_I02-E01_R18_R03.docx")
if BUILDER_R18_R03.exists():
    if BUILDER_R18_R03.read_text(encoding="utf-8-sig") != builder:
        raise SystemExit("A different R18 R03 builder exists; do not overwrite it.")
else:
    BUILDER_R18_R03.write_text(builder, encoding="utf-8")

qa = QA_SCRIPT_R18_R02.read_text(encoding="utf-8-sig")
qa = qa.replace("0010_I02-E01_R18_R02.docx", "0010_I02-E01_R18_R03.docx")
qa = qa.replace("build_0010_r18_r02_docx.py", "build_0010_r18_r03_docx.py")
qa = qa.replace("TECHNICAL_QA_R18_R02_RECHECK.json", "TECHNICAL_QA_R18_R03.json")
qa = qa.replace("TTQS-0010-R18-R02-TECHNICAL-QA-RECHECK-20261030", "TTQS-0010-R18-R03-TECHNICAL-QA-20261030")
expected_builder_check = 'checks["builder_bound_to_r18_source_and_output"] = "0010_I02-E01_R18_R02.md" in BUILDER.read_text(encoding="utf-8-sig") and "0010_I02-E01_R18_R03.docx" in BUILDER.read_text(encoding="utf-8-sig")'
if qa.count(expected_builder_check) != 1:
    raise SystemExit("Builder source/output path check was not correctly updated to R18 R03.")
needle = 'checks["python_docx_open_and_structure"] = bool(doc.paragraphs) and len(doc.tables) == 22\n'
width_check = needle + 'ev_table = next((t for t in doc.tables if t.rows and t.rows[0].cells[0].text.strip().lower() == "ev id"), None)\nchecks["ev_behavior_column_width_over_4in"] = ev_table is not None and ev_table.columns[3].width.inches >= 4.0\n'
if qa.count(needle) != 1:
    raise SystemExit("Could not uniquely locate the table-structure QA insertion point.")
qa = qa.replace(needle, width_check, 1)
QA_SCRIPT_R18_R03.write_text(qa, encoding="utf-8")

build = subprocess.run([sys.executable, str(BUILDER_R18_R03)], capture_output=True, text=True, encoding="utf-8")
if build.returncode != 0:
    raise SystemExit(f"R18 R03 layout builder failed ({build.returncode}):\n{build.stdout}\n{build.stderr}")
qa_run = subprocess.run([sys.executable, str(QA_SCRIPT_R18_R03)], capture_output=True, text=True, encoding="utf-8")
if qa_run.returncode != 0:
    raise SystemExit(f"R18 R03 technical QA failed ({qa_run.returncode}); preserve output and inspect:\n{qa_run.stdout}\n{qa_run.stderr}")

receipt = {
    "work_id": "TTQS-0010-R18-R03-LAYOUT-ROOT-CAUSE-REPAIR-20261030",
    "predecessor_candidate_sha256": digest(DOCX_R18_R02),
    "predecessor_visual_defect": "R18 R02 PDF pages 17-19: the seven-column EV table placed the long raw behavior narrative in a 0.60-inch column, causing vertical character stacking and the P3 observations to span three pages, with page 18 mostly blank. This is a located layout defect; semantic source data and ratings were not changed.",
    "root_cause": "The builder's (7, 'ev id') width map assigned 0.60 inches to column 4 (raw behavior) and 4.65 inches to column 5 (prompt status); the actual headers place the long narrative in column 4.",
    "bounded_change": "Reallocated the existing 10.55-inch landscape table width to [1.50, 0.75, 0.75, 4.20, 1.35, 0.55, 1.45] inches. No source facts, ratings, formulas, or prose were changed.",
    "candidate_status": "CANDIDATE_NOT_FORMALLY_ACCEPTED",
    "artifacts": {
        "source_sha256": digest(SOURCE_R18_R02),
        "register_sha256": digest(REGISTER_R17_R02),
        "builder": {"path": str(BUILDER_R18_R03), "sha256": digest(BUILDER_R18_R03)},
        "candidate_docx": {"path": str(DOCX_R18_R03), "sha256": digest(DOCX_R18_R03), "bytes": DOCX_R18_R03.stat().st_size},
        "technical_qa": {"path": str(QA_R18_R03), "sha256": digest(QA_R18_R03), "verdict": "PASS"},
        "technical_qa_script": {"path": str(QA_SCRIPT_R18_R03), "sha256": digest(QA_SCRIPT_R18_R03)},
    },
    "builder_stdout": build.stdout.strip(),
    "technical_qa_stdout": qa_run.stdout.strip(),
    "native_visual_recheck": "PENDING; render and inspect R18 R03 before semantic disposition.",
    "formal_acceptance": "NOT_ACCEPTED",
    "checked_at_taipei": datetime.now().astimezone().isoformat(),
}
RECEIPT_R18_R03.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False, indent=2))
