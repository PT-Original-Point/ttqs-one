from pathlib import Path
from hashlib import sha256
from datetime import datetime
from zoneinfo import ZoneInfo
from docx import Document
from docx.shared import Pt
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
import zipfile,json,sys
ROOT=Path(r'E:\TTQS\_r09_sync_0104_20261022\docs\ttqs-quality-20261016\quality-review\0102_I18-E09_R06_20261021')
SRC=ROOT/'candidate'/'0102__技能競賽獲獎證據取得與查核工作紀錄_R34.docx'
OUT=ROOT/'candidate'/'0102__技能競賽獲獎證據取得與查核工作紀錄_R35.docx'
R34_RECEIPT=ROOT/'repair_R34_semantic_20261023'/'repair_receipt_R34_R01.json'
RECEIPT=ROOT/'repair_R34_semantic_20261023'/'repair_receipt_R35_R01.json'
def digest(path): return sha256(path.read_bytes()).hexdigest().upper()
assert SRC.is_file() and R34_RECEIPT.is_file() and not OUT.exists() and not RECEIPT.exists()
source_sha=digest(SRC)
assert source_sha=='84C0C420168F255A7556043ED59532BBB9E82232EA27490E7602AD973E6AAAA2',source_sha
source_receipt=json.loads(R34_RECEIPT.read_text(encoding='utf-8'))
assert source_receipt['candidate_docx_sha256']==source_sha
D=Document(SRC)
assert len(D.tables)==45,len(D.tables)
def set_cell(cell,text,size=9.5):
    cell.text=text
    cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.TOP
    for p in cell.paragraphs:
        p.paragraph_format.space_before=Pt(0);p.paragraph_format.space_after=Pt(0);p.paragraph_format.line_spacing=1.0
        for run in p.runs: run.font.size=Pt(size)
t8=D.tables[8]
assert len(t8.columns)==3 and t8.rows[0].cells[1].text.strip()=='SYN-0102-CASE-01' and t8.rows[0].cells[2].text.strip()=='SYN-0102-CASE-02'
updates={
 'consent_status':('UNKNOWN（真實世界；無有效同意或簽署；CASE-01 SAMPLE workflow 的限縮同意僅為模擬）','UNKNOWN（真實世界；無有效同意；亦無模擬同意）'),
 'consent_scope':('真實世界未取得；SAMPLE 僅模擬內部查核及向主辦查證，不含公開，非真實同意。','未取得；不得對外查證或揭露。'),
 'next_action':('SAMPLE 請求流程 PENDING_REAL_SOURCE；實際 OUTBOUND_REQUEST=NOT_SENT，REAL_CONTACT=BLOCKED_PENDING_REAL_CONSENT_AND_AUTHORITY。2026-10-26 SAMPLE-only 檢視。','2026-10-20 SAMPLE 覆核已完成；2026-10-30 下次 SAMPLE-only 檢視；同意及身分／隊名缺件未補，維持 HOLD。'),
 'notes':('SAMPLE／SYNTHETIC；無真實課程計畫、名冊或評量；course_source=UNKNOWN，未核實；無第三方原件。','SAMPLE／SYNTHETIC；無真實課程計畫、名冊或評量；course_source=UNKNOWN，未核實；相似截圖尚未查證，不得指控。'),
 'course_source':('UNKNOWN','UNKNOWN'),
 'internal_review_date':('2026-10-26（SAMPLE-only；非外部期限）','2026-10-30（SAMPLE-only；2026-10-20 覆核已完成；非外部期限；原因：同意及身分／隊名對照缺件未補）')
}
rowmap={row.cells[0].text.strip():row for row in t8.rows}
old_values={}
for label,(case01,case02) in updates.items():
    assert label in rowmap,label
    row=rowmap[label]
    old_values[label]=[row.cells[1].text,row.cells[2].text]
    set_cell(row.cells[1],case01);set_cell(row.cells[2],case02)
# Update only the current candidate label; preserve the historical R34 row.
cover=D.tables[0]
cover_count=0
for cell in cover._cells:
    if 'R34' in cell.text:
        cell.text=cell.text.replace('R34','R35');cover_count+=1
assert cover_count>=1, 'current revision label missing from cover'
for section in D.sections:
    for area in (section.header,section.footer):
        for p in area.paragraphs:
            if '候選 R34' in p.text:
                p.text=p.text.replace('候選 R34','候選 R35')
        for table in area.tables:
            for row in table.rows:
                for cell in row.cells:
                    if '候選 R34' in cell.text: cell.text=cell.text.replace('候選 R34','候選 R35')
for p in D.paragraphs:
    if '候選 R34' in p.text:p.text=p.text.replace('候選 R34','候選 R35')
props=D.core_properties
props.title=props.title.replace('R34','R35');props.subject=props.subject.replace('R34','R35')
hist=[t for t in D.tables if t.rows and t.rows[0].cells[0].text.strip()=='版本' and len(t.columns)==5]
assert len(hist)==1
history=hist[0]
assert history.rows[-1].cells[0].text.strip()=='R34'
row=history.add_row()
vals=['R35','2026-10-23','最小修正 §7.2 Form A：將 CASE-01／CASE-02 的同意、範圍、下一步、註記、course_source 與 internal_review_date 分別寫入正確欄位；保留 R34 其餘內容與判定。','文件維護角色','SAMPLE／SYNTHETIC 候選；非真實同意、送件或績效；正式接受未授予。']
for c,v in zip(row.cells,vals):set_cell(c,v)
D.save(OUT)
C=Document(OUT)
with zipfile.ZipFile(OUT) as z: assert z.testzip() is None
assert len(C.tables)==46,len(C.tables)
ct=C.tables[8]
cr={row.cells[0].text.strip():row for row in ct.rows}
for label,(a,b) in updates.items():
    assert cr[label].cells[1].text==a,(label,'CASE01',cr[label].cells[1].text)
    assert cr[label].cells[2].text==b,(label,'CASE02',cr[label].cells[2].text)
assert 'R35' in C.tables[0].cell(0,0).text or any('R35' in cell.text for cell in C.tables[0]._cells)
assert history.rows[-1].cells[0].text.strip()=='R34'
assert hist[0].rows[-1].cells[0].text.strip()=='R34'
# Re-opened body retains the R34 structural and semantic fixes.
all_text='\n'.join([p.text for p in C.paragraphs]+[cell.text for t in C.tables for row in t.rows for cell in row.cells])
assert 'DUPLICATE_OF=F-0102-016' in all_text
assert 'F-0102-036' in all_text
assert '0/2=0%' in all_text
assert 'course_source=UNKNOWN' in all_text
assert '2026-10-30' in all_text and 'PENDING_REAL_SOURCE' in all_text and 'OUTBOUND_REQUEST=NOT_SENT' in all_text
fact_tables=[t for t in C.tables if t.rows and t.rows[0].cells[0].text.strip()=='fact_id']
assert len(fact_tables)==1
fact_ids=[r.cells[0].text.strip() for r in fact_tables[0].rows[1:]]
expected={f'F-0102-{i:03d}' for i in list(range(1,36))+list(range(37,57))}
assert set(fact_ids)==expected and len(fact_ids)==55 and len(set(fact_ids))==55
body_sizes=[];table_sizes=[]
for p in C.paragraphs:
    for r in p.runs:
        if r.text.strip() and r.font.size: body_sizes.append(r.font.size.pt)
for t in C.tables:
    for row in t.rows:
        for cell in row.cells:
            for p in cell.paragraphs:
                for r in p.runs:
                    if r.text.strip() and r.font.size: table_sizes.append(r.font.size.pt)
assert body_sizes and min(body_sizes)>=10.5,min(body_sizes) if body_sizes else None
assert table_sizes and min(table_sizes)>=9.5,min(table_sizes) if table_sizes else None
sha=digest(OUT)
receipt={
 'schema':'ttqs.docx_minimal_candidate_repair.v1','work_id':'TTQS-0102-I18E09-R35-FORM-A-CASE-COLUMN-CORRECTION-R01','doc_id':'0102','official_requirement_id':'I18-E09','blueprint_project_index':110,'printed_official_checkbox_serial':'UNKNOWN',
 'source_revision':'R34','source_docx_sha256':source_sha,'source_receipt_sha256':digest(R34_RECEIPT),'candidate_revision':'R35','candidate_docx_sha256':sha,'candidate_path':str(OUT),
 'repair_scope':'Only six Form A case-specific rows split correctly into CASE-01 / CASE-02 cells; current candidate label and version history appended. No other content recomposed.',
 'source_packet_sha256':'90E2C809914964039563C734881D9DEDC4E969F60179778F391E39FE2C156982','unique_blueprint_sha256':'211DE39325C3EE5811D25738161CC6C5AE6322AE6809FD056400ECD2181074A0','writer_response_sha256':'385ACABC56650DE760AFC1B1BE8376D1922E5C3230878C7ABFB8101D77A3C461',
 'prior_R34_receipt_status':'SELF_AUTHORED_STATIC_PASS_REVOKED_FOR_FORM_A_COLUMN_MAPPING; historical receipt preserved, defect fixed in R35',
 'changed_form_a_fields':list(updates.keys()),'source_values_before_patch':old_values,
 'checks':{'docx_reopen':'PASS','zip_crc':'PASS','case_columns_separated':'PASS','all_55_fact_ids_unique':'PASS','duplicate_alias':'PRESERVED_OUTSIDE_FACT_ROWS','sample_calculation_0_of_2':'PRESERVED','body_font_min_pt':min(body_sizes),'table_font_min_pt':min(table_sizes)},
 'independent_semantic_review':'PENDING_EXACT_R35_SHA','word_native_export_and_visual_review':'PENDING','formal_acceptance':'NOT_GRANTED','created_at_local':datetime.now(ZoneInfo('Asia/Taipei')).isoformat()
}
RECEIPT.write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'candidate':str(OUT),'sha256':sha,'receipt':str(RECEIPT),'receipt_sha256':digest(RECEIPT),'source_sha256':source_sha,'changed_fields':list(updates.keys()),'form_a_case_columns':'PASS','docx_reopen':'PASS','zip_crc':'PASS','fact_id_count':len(fact_ids),'body_font_min_pt':min(body_sizes),'table_font_min_pt':min(table_sizes),'semantic_review':'PENDING'},ensure_ascii=False))