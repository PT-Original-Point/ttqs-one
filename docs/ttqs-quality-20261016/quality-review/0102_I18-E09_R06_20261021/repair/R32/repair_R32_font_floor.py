
from pathlib import Path
from docx import Document
from docx.shared import Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from collections import Counter
from datetime import datetime, timezone
import hashlib, json, zipfile

root = Path(r"E:\TTQS\_r09_sync_0104_20261022\docs\ttqs-quality-20261016\quality-review\0102_I18-E09_R06_20261021")
src = root / "candidate" / "0102__技能競賽獲獎證據取得與查核工作紀錄_R31.docx"
dst = root / "candidate" / "0102__技能競賽獲獎證據取得與查核工作紀錄_R32.docx"
outdir = root / "repair_R32_font_floor_20261023"
outdir.mkdir(parents=True, exist_ok=True)
assert src.is_file() and not dst.exists()
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest().upper()
src_sha = sha(src)
assert src_sha == "77DADAAE1B9B5EF70369105B269F8431032EB95CDB860364B6E85E75128B55C5", src_sha
doc = Document(str(src))
def eff(run, para):
    for f in (run.font, run.style.font if run.style else None, para.style.font if para.style else None, doc.styles["Normal"].font):
        if f is not None and f.size is not None: return float(f.size.pt)
    return 11.0
def table_text(t):
    return [[c.text for c in row.cells] for row in t.rows]
before_paras = [p.text for p in doc.paragraphs]
before_tables = [table_text(t) for t in doc.tables]
assert len(doc.tables) == 46, len(doc.tables)
low=[]
for ti,t in enumerate(doc.tables):
    for ri,row in enumerate(t.rows):
        for ci,cell in enumerate(row.cells):
            for pi,para in enumerate(cell.paragraphs):
                for run in para.runs:
                    if run.text.strip():
                        s=eff(run,para)
                        if s < 9.5: low.append((ti,ri,ci,run,s))
assert len(low)==66, len(low)
affected=sorted({x[0] for x in low})
assert affected == [9,10,37], affected
for ti,ri,ci,run,s in low:
    run.font.size=Pt(9.5)
# Update current version labels in the identity table, preserving existing paragraph formatting.
identity = next((t for t in doc.tables if t.rows and len(t.rows[0].cells)>1 and t.rows[0].cells[0].text.strip()=="項目" and t.rows[0].cells[1].text.strip()=="內容" and any(r.cells[0].text.strip()=="文件編號" for r in t.rows[1:])), None)
assert identity is not None
def set_cell_preserving_first_run(cell, value):
    assert len(cell.paragraphs) == 1
    p=cell.paragraphs[0]
    if p.runs:
        p.runs[0].text=value
        for run in p.runs[1:]: run.text=""
    else: p.add_run(value)
for row in identity.rows:
    key=row.cells[0].text.strip()
    if key=="版本":
        set_cell_preserving_first_run(row.cells[1], "R32（工程候選；內容基線 R02，R17、R24、R25 至 R32 均有後續修正；未發布、未正式接受）")
    elif key=="候選修訂":
        set_cell_preserving_first_run(row.cells[1], "R32（目前工程候選修訂；版本表與頁尾一致；未正式接受）")
# Locate the revision history by its actual headers, not its ordinal table number.
history = next((t for t in doc.tables if t.rows and [c.text.strip() for c in t.rows[0].cells[:5]] == ["版本","日期","修改內容","修改角色","備註"]), None)
assert history is not None
assert not any(r.cells[0].text.strip()=="R32" for r in history.rows[1:])
row=history.add_row()
values=["R32","2026-10-23","提高 Form A 與 12.1 案例矩陣表格字級至 9.5 pt；不變更欄位、案例值、日期、狀態、公式或判定。","文件維護角色","版面可讀性修復；SAMPLE/SYNTHETIC 候選；未正式接受。"]
for cell,value in zip(row.cells,values): set_cell_preserving_first_run(cell,value)
trpr=row._tr.get_or_add_trPr()
trpr.append(OxmlElement("w:cantSplit"))
# Keep candidate revision metadata current; historical rows remain intact.
props=doc.core_properties
props.title="0102 I18-E09 技能競賽獲獎證據取得與查核工作紀錄 R32"
props.subject="0102 I18-E09 R32 candidate; SAMPLE/SYNTHETIC; not formally accepted"
props.comments="R32 raises the three undersized tables to the documented 9.5 pt floor; no case facts or decisions changed. Candidate only."
props.revision=32
props.modified=datetime.now(timezone.utc)
# Update only current-candidate labels if present in headers/footers.
def replace_story(part):
    changed=0
    for p in part.paragraphs:
        old=p.text
        if "R31" in old:
            new=old.replace("R31","R32")
            if p.runs:
                p.runs[0].text=new
                for rr in p.runs[1:]: rr.text=""
            else: p.add_run(new)
            changed+=1
    for t in part.tables:
        for rr in t.rows:
            for cell in rr.cells:
                for p in cell.paragraphs:
                    old=p.text
                    if "R31" in old:
                        new=old.replace("R31","R32")
                        if p.runs:
                            p.runs[0].text=new
                            for r0 in p.runs[1:]: r0.text=""
                        else: p.add_run(new)
                        changed+=1
    return changed
footer_header_changes=0
for section in doc.sections:
    for part in (section.header, section.footer, section.first_page_header, section.first_page_footer, section.even_page_header, section.even_page_footer):
        footer_header_changes += replace_story(part)
# Verify unaffected body text and all non-version-table content before save.
assert [p.text for p in doc.paragraphs] == before_paras, "body paragraphs changed"
after_tables=[table_text(t) for t in doc.tables]
history_index=next(i for i,t in enumerate(doc.tables) if t._tbl is history._tbl)
identity_index=next(i for i,t in enumerate(doc.tables) if t._tbl is identity._tbl)
for i,(old,new) in enumerate(zip(before_tables,after_tables)):
    if i==history_index:
        assert new[:-1] == old, "historical version rows changed"
        assert len(new)==len(old)+1
    elif i==identity_index:
        assert len(old)==len(new)
        for ri,(orow,nrow) in enumerate(zip(old,new)):
            if orow[0].strip() not in ("版本","候選修訂"): assert orow==nrow, (i,ri)
    else:
        assert old==new, ("table text changed",i)
# Verify the SAMPLE examples remain present.
alltext="\n".join(before_paras+[c for t in before_tables for r in t for c in r])
for token in ("SYN-0102-CASE-01","SYN-0102-CASE-02","RECEIVED_UNVERIFIED","SAMPLE"):
    assert token in alltext, token
doc.save(str(dst))
with zipfile.ZipFile(dst) as z: assert z.testzip() is None
reopened=Document(str(dst))
def eff2(run,para):
    for f in (run.font, run.style.font if run.style else None, para.style.font if para.style else None, reopened.styles["Normal"].font):
        if f is not None and f.size is not None: return float(f.size.pt)
    return 11.0
table_sizes=[]
for t in reopened.tables:
    for row0 in t.rows:
        for cell in row0.cells:
            for p in cell.paragraphs:
                for run in p.runs:
                    if run.text.strip(): table_sizes.append(eff2(run,p))
body_sizes=[]
for p in reopened.paragraphs:
    for run in p.runs:
        if run.text.strip(): body_sizes.append(eff2(run,p))
assert min(table_sizes)>=9.5, min(table_sizes)
assert min(body_sizes)>=10.5, min(body_sizes)
assert any(r.cells[0].text.strip()=="R32" for r in next(t for t in reopened.tables if t.rows and [c.text.strip() for c in t.rows[0].cells[:5]]==["版本","日期","修改內容","修改角色","備註"]).rows[1:])
dst_sha=sha(dst)
packet=root/"source"/"SOURCE_PACKET_0102_I18-E09_R01.md"
blueprint=root/"source"/"UNIQUE_BLUEPRINT_0102_I18-E09_R01.md"
receipt={
 "schema":"ttqs.docx_targeted_layout_repair.v1",
 "work_id":"0102_R32_TABLE_FONT_FLOOR_REPAIR",
 "doc_id":"0102",
 "official_requirement_id":"I18-E09",
 "project_blueprint_index":110,
 "printed_official_checkbox_serial":"UNKNOWN",
 "source_candidate":"R31",
 "source_docx_sha256":src_sha,
 "candidate_revision":"R32",
 "candidate_path":str(dst),
 "candidate_docx_sha256":dst_sha,
 "source_control_commit":"ef4af2fb975cab9c701b52415ecaa2bd09d19808",
 "control_blobs":{
   "AGENTS.md":"103cc9b04e4e756cbc7a8d405faaff218beade69",
   "01_HUMAN_MISSION_AND_ACCEPTANCE.md":"538bedb9d87e8465f43151933b4a5c1bfa4bbc4e",
   "02_GENRE_WRITING_MANUAL.md":"4ff863d9f534b6359fc1c7c1685bd8cce02da886",
   "03_157_CHECKBOX_BLUEPRINTS.md":"8c2bbe7ca9dcbb03088a48934b9e57e7147ede63",
   "04_CODEX_GOAL_24X7_EXECUTION.md":"4ee893218791ec9460e824fc559933c276414738",
   "05_HOURLY_NATIVE_WAKE_RESUME.md":"35d3081c7e7fb979466c3a58a1e77b42f0d1441a",
   "06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md":"4c7eff55748ff265b1e5a7d1122852b0d101acbd"
 },
 "source_packet_sha256":sha(packet),
 "unique_blueprint_sha256":sha(blueprint),
 "source_requirement_statement":"official evidence table p.7; award coaching is an example, not guaranteed score; assessment form p.4; no award alone equals a training outcome",
 "repair":{"low_font_runs_before":len(low),"affected_tables_zero_based":affected,"affected_tables_semantic":["Form A page 1","Form A page 2","12.1 two-case matrix"],"table_minimum_after_pt":min(table_sizes),"body_minimum_after_pt":min(body_sizes),"text_preservation":"PASS outside version identity/current revision/history append; all existing tables unchanged text; 12.1 case values unchanged","new_version_row":"R32","header_footer_current_revision_replacements":footer_header_changes},
 "synthetic_boundary":"SAMPLE/SYNTHETIC only; no real award, third-party original, signature, association approval or formal acceptance asserted",
 "technical_status":"OOXML_REOPEN_AND_TEXT_PRESERVATION_PASS; TABLE_FONT_FLOOR_PASS; BODY_FONT_FLOOR_PASS; PENDING_NATIVE_WORD_EXPORT_AND_FULL_VISUAL_QA",
 "independent_semantic_review":"PENDING_EXACT_R32_SHA",
 "formal_acceptance":"NOT_GRANTED",
 "created_at_local":datetime.now().astimezone().isoformat()
}
(outdir/"repair_receipt_R32.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"source_sha256":src_sha,"candidate":str(dst),"candidate_sha256":dst_sha,"source_packet_sha256":receipt["source_packet_sha256"],"unique_blueprint_sha256":receipt["unique_blueprint_sha256"],"low_font_runs_repaired":len(low),"affected_tables":affected,"min_table_pt":min(table_sizes),"min_body_pt":min(body_sizes),"history_revision":"R32","zip_integrity":"PASS","text_preservation":"PASS","status":receipt["technical_status"]},ensure_ascii=False))
