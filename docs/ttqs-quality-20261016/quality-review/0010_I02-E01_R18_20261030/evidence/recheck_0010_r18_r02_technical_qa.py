from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0010_I02-E01_ASSESSMENT_STANDARD_R04_20261030")
SOURCE_QA = ROOT / "qa" / "technical_qa_0010_r18_r02.py"
RECHECK_QA = ROOT / "qa" / "technical_qa_0010_r18_r02_recheck.py"

text = SOURCE_QA.read_text(encoding="utf-8-sig")
old_out = "TECHNICAL_QA_R18_R02.json"
new_out = "TECHNICAL_QA_R18_R02_RECHECK.json"
old_work = "TTQS-0010-R18-R02-TECHNICAL-QA-20261030"
new_work = "TTQS-0010-R18-R02-TECHNICAL-QA-RECHECK-20261030"
old_check = 'checks["builder_bound_to_r18_source_and_output"] = "0010_I02-E01_R18.md" in BUILDER.read_text(encoding="utf-8-sig") and "0010_I02-E01_R18.docx" in BUILDER.read_text(encoding="utf-8-sig")'
new_check = 'checks["builder_bound_to_r18_source_and_output"] = "0010_I02-E01_R18_R02.md" in BUILDER.read_text(encoding="utf-8-sig") and "0010_I02-E01_R18_R02.docx" in BUILDER.read_text(encoding="utf-8-sig")'
if text.count(old_out) != 1 or text.count(old_work) != 1 or text.count(old_check) != 1:
    raise SystemExit("R02 QA source does not match the recorded single stale-path assertion; stop.")
text = text.replace(old_out, new_out, 1).replace(old_work, new_work, 1).replace(old_check, new_check, 1)
if RECHECK_QA.exists() or (ROOT / "qa" / new_out).exists():
    raise SystemExit("R18 R02 recheck artifacts already exist; do not overwrite them.")
RECHECK_QA.write_text(text, encoding="utf-8")
result = subprocess.run([sys.executable, str(RECHECK_QA)], capture_output=True, text=True, encoding="utf-8")
print(result.stdout)
if result.stderr:
    print(result.stderr, file=sys.stderr)
if result.returncode:
    raise SystemExit(result.returncode)
