from pathlib import Path
from docx import Document
from docx.shared import Pt
import hashlib, json, shutil, subprocess, sys

REPO = Path(r"E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016")
R02 = REPO / "docs/ttqs-quality-20261016/quality-review/0038_R02"
ROOT = REPO / "docs/ttqs-quality-20261016/quality-review/0038_R03"
SRC = R02 / "candidate/0038_R02.docx"
DST = ROOT / "candidate/0038_R03.docx"
BP = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\BLUEPRINT_CURRENT.jsonl")
EXPECTED_SRC = "bdb6ef07c1aacd31f638cdad511012777d2f1b9d2c9f5f307252dd62de0170a4"
EXPECTED_BP_FILE = "406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e"
EXPECTED_BP_ROW = "2504485c1698a5c83ac2205938c05b532edc8d697f2441ad1d6a0c324897b73e"
EXPECTED_SOURCE_HEAD = "639b9eacce93f84f49ee20714f1bad337c6a961e"

sha = lambda b: hashlib.sha256(b).hexdigest()
def file_sha(p): return sha(p.read_bytes())
if not SRC.is_file() or file_sha(SRC) != EXPECTED_SRC:
    raise SystemExit(f"R02 exact source mismatch: {file_sha(SRC) if SRC.exists() else 'missing'}")
if DST.exists(): raise SystemExit("Refusing to overwrite existing R03 candidate")
if file_sha(BP) != EXPECTED_BP_FILE: raise SystemExit("Runtime Blueprint file SHA changed")
head = subprocess.check_output(["git", "-C", str(REPO), "rev-parse", "HEAD"], text=True).strip()
remote = subprocess.check_output(["git", "-C", str(REPO), "rev-parse", "refs/remotes/origin/work/ttqs-one-document-quality-contract-20261016"], text=True).strip()
if head != EXPECTED_SOURCE_HEAD or remote != EXPECTED_SOURCE_HEAD:
    raise SystemExit(f"Spec branch moved: HEAD={head}; origin={remote}")

# Snapshot the exact current 0038 Unique Blueprint row and prove its source identity.
raw_lines = BP.read_bytes().splitlines(keepends=True)
row = next(line for line in raw_lines if json.loads(line).get("deliverable_id") == "0038")
row_sha = sha(row.rstrip(b"\r\n"))
if row_sha != EXPECTED_BP_ROW: raise SystemExit(f"Blueprint row SHA changed: {row_sha}")
(ROOT / "inputs/BLUEPRINT_CURRENT_0038.jsonl").write_bytes(row.rstrip(b"\r\n") + b"\n")

# Preserve every evidence/input file that identifies the R02 case and sample.
for name in ["official-2.png", "official-3.png"]:
    shutil.copy2(R02 / "inputs" / name, ROOT / "inputs" / name)
for name in ["design_improvement_flow.png", "synthetic_prepost_comparison.png"]:
    shutil.copy2(R02 / "evidence/assets" / name, ROOT / "evidence/assets" / name)
shutil.copy2(R02 / "evidence/SYNTHETIC_REPLACEMENT_REGISTER.csv", ROOT / "evidence/SYNTHETIC_REPLACEMENT_REGISTER.csv")

# Current spec blob IDs come from the exact fetched local HEAD (same as origin).
specs = {
 "01_HUMAN_MISSION_AND_ACCEPTANCE.md": "538bedb9d87e8465f43151933b4a5c1bfa4bbc4e",
 "02_GENRE_WRITING_MANUAL.md": "4ff863d9f534b6359fc1c7c1685bd8cce02da886",
 "03_157_CHECKBOX_BLUEPRINTS.md": "8c2bbe7ca9dcbb03088a48934b9e57e7147ede63",
 "04_CODEX_GOAL_24X7_EXECUTION.md": "62e3dd7dfd8579b6bc97952ffa6236e7494f3b4d",
 "05_HOURLY_NATIVE_WAKE_RESUME.md": "60ae010c58140e1710ed24016085c6dfaf6ffaee",
 "06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md": "70449889fd464106fe204496004bee13018d4a51",
}
# Verify every named spec's committed blob before recording it.
for path, expected in specs.items():
    got = subprocess.check_output(["git", "-C", str(REPO), "rev-parse", f"HEAD:docs/ttqs-quality-20261016/{path}"], text=True).strip()
    if got != expected: raise SystemExit(f"spec blob mismatch {path}: {got}")

src_doc = Document(SRC)
changed = []
for pi, para in enumerate(src_doc.paragraphs):
    for ri, run in enumerate(para.runs):
        if not run.text.strip(): continue
        size = run.font.size.pt if run.font.size else None
        if size is not None and size < 10.5:
            changed.append({"paragraph": pi, "run": ri, "from_pt": size, "text": run.text})
            run.font.size = Pt(10.5)
if len(changed) != 20:
    raise SystemExit(f"Expected exactly 20 below-floor body runs; found {len(changed)}")
src_doc.save(DST)

# Verify the patch changed only direct body run font values, with all text/tables retained.
a = Document(SRC); b = Document(DST)
if [p.text for p in a.paragraphs] != [p.text for p in b.paragraphs]: raise SystemExit("Body paragraph text changed")
if [[c.text for row in t.rows for c in row.cells] for t in a.tables] != [[c.text for row in t.rows for c in row.cells] for t in b.tables]: raise SystemExit("Table text changed")
low = []
unscaled = []
for pi, para in enumerate(b.paragraphs):
    for ri, run in enumerate(para.runs):
        if not run.text.strip(): continue
        if run.font.size is None:
            # This document's Normal/list styles define 10.5 pt or larger; report separately for verification.
            style = para.style
            effective = None
            while style is not None and effective is None:
                effective = style.font.size.pt if style.font.size else None
                style = style.base_style
            if effective is None: effective = 11.0  # Word default Normal size
            unscaled.append({"paragraph": pi, "run": ri, "effective_pt": effective})
            if effective < 10.5: low.append({"paragraph":pi,"run":ri,"effective_pt":effective})
        elif run.font.size.pt < 10.5:
            low.append({"paragraph": pi, "run": ri, "effective_pt": run.font.size.pt})
if low: raise SystemExit(f"Body font floor still fails: {low}")

sha_src_text = sha("\n".join(p.text for p in a.paragraphs).encode("utf-8"))
sha_dst_text = sha("\n".join(p.text for p in b.paragraphs).encode("utf-8"))
receipt = {
 "project_id":"TTQS_ONE", "doc_id":"0038", "requirement_id":"I08-E02", "official_checkbox_sequence":"039",
 "revision":"R03", "source_candidate":"0038_R02", "source_sha256":EXPECTED_SRC,
 "candidate_path":"candidate/0038_R03.docx", "candidate_sha256":file_sha(DST),
 "source_spec_head":head, "spec_blob_ids":specs, "blueprint_file_sha256":EXPECTED_BP_FILE,
 "blueprint_row_sha256":EXPECTED_BP_ROW, "change_scope":"Only 20 non-empty top-level body runs below 10.5 pt were raised to 10.5 pt; all paragraph and table text verified identical.",
 "changed_runs":changed, "body_paragraph_count":len(b.paragraphs), "table_count":len(b.tables),
 "unscaled_body_runs_using_style_inheritance":unscaled, "body_below_10_5_runs_after":low,
 "body_text_sha256_before":sha_src_text, "body_text_sha256_after":sha_dst_text,
 "formal_acceptance":"NOT_GRANTED", "independent_semantic_review":"PENDING", "visual_review":"PENDING"
}
(ROOT / "evidence/build/patch_receipt_R03.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"candidate":str(DST),"candidate_sha256":receipt["candidate_sha256"],"changed_runs":len(changed),"body_text_unchanged":sha_src_text==sha_dst_text,"body_below_floor_after":len(low),"blueprint_file_sha256":EXPECTED_BP_FILE,"blueprint_row_sha256":EXPECTED_BP_ROW,"source_head":head},ensure_ascii=False,indent=2))
