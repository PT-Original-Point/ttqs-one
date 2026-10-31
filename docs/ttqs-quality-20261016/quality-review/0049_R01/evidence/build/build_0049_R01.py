from __future__ import annotations

import csv
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(r"E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016")
PACKAGE = ROOT / "docs/ttqs-quality-20261016/quality-review/0049_R01"
RUNTIME = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME")
BLUEPRINT = RUNTIME / "CONTROL/BLUEPRINT_CURRENT.jsonl"
SOURCE_DOC = ROOT / "docs/ttqs-quality-20261016/quality-review/0033_R03/candidate/0033_R03.docx"
SOURCE_REGISTER = ROOT / "docs/ttqs-quality-20261016/quality-review/0033_R03/evidence/SYNTHETIC_REPLACEMENT_REGISTER.csv"
SOURCE_PROGRESS = ROOT / "docs/ttqs-quality-20261016/quality-review/0033_R03/PROGRESS.json"
SOURCE_SHA = "fe5f3cfd84c761da86435a71e0fd899daa725be78628c4d2d3f2324c1fdb5f4f"
SOURCE_REGISTER_SHA = "d114f36d9c4852cda2239bf22fcc709bdc0a40aad62418e076c6b9c2ae523247"
BLUEPRINT_SHA = "406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e"
OFFICIAL_PDF_SHA = "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709"
DOCX_PATH = PACKAGE / "candidate/0049_R01.docx"
CASE_ID = "SYN-0033-PLAN-01"
DOC_ID = "0049"
REVISION = "R01"

NAVY = "17365D"
BLUE = "2F75B5"
TEAL = "168C8C"
PALE = "EAF1F8"
PALE_TEAL = "E7F3F2"
PALE_GOLD = "FFF2CC"
GRAY = "5B6573"
LIGHT = "F4F6F8"
RED = "9C0006"
FONT = "Microsoft JhengHei"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def set_run_font(run, size=10.5, bold=None, color=None, italic=None):
    run.font.name = FONT
    run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), FONT)
    run._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), FONT)
    run._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), FONT)
    run.font.size = Pt(size)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic
    if color:
        run.font.color.rgb = RGBColor.from_string(color)


def shade(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def set_cell_margins(cell, top=90, start=95, bottom=90, end=95):
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for tag, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tc_mar.find(qn(f"w:{tag}"))
        if node is None:
            node = OxmlElement(f"w:{tag}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


def mark_repeat_table_header(row):
    tr_pr = row._tr.get_or_add_trPr()
    tbl_header = OxmlElement("w:tblHeader")
    tbl_header.set(qn("w:val"), "true")
    tr_pr.append(tbl_header)


def prevent_row_split(row):
    tr_pr = row._tr.get_or_add_trPr()
    tr_pr.append(OxmlElement("w:cantSplit"))


def set_cell_text(cell, text, header=False, center=False):
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    if center:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(str(text))
    set_run_font(run, size=9.5, bold=header, color="FFFFFF" if header else None)
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    set_cell_margins(cell)


def set_cell_widths(table, widths):
    table.autofit = False
    for row in table.rows:
        for idx, width in enumerate(widths):
            row.cells[idx].width = Inches(width)


def add_table(doc, headers, rows, widths=None, center_cols=(), font_size=9.5):
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    table.autofit = False
    header_row = table.rows[0]
    mark_repeat_table_header(header_row)
    for i, title in enumerate(headers):
        set_cell_text(header_row.cells[i], title, header=True, center=i in center_cols)
        shade(header_row.cells[i], NAVY)
    for ridx, values in enumerate(rows):
        cells = table.add_row().cells
        prevent_row_split(table.rows[-1])
        for i, value in enumerate(values):
            set_cell_text(cells[i], value, center=i in center_cols)
            if ridx % 2 == 1:
                shade(cells[i], LIGHT)
    if widths:
        set_cell_widths(table, widths)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return table


def add_para(doc, text="", style=None, bold_prefix=None, color=None, size=10.5, align=None, italic=False):
    p = doc.add_paragraph(style=style)
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.line_spacing = 1.12
    if align is not None:
        p.alignment = align
    if bold_prefix and text.startswith(bold_prefix):
        r1 = p.add_run(bold_prefix)
        set_run_font(r1, size=size, bold=True, color=color)
        r2 = p.add_run(text[len(bold_prefix):])
        set_run_font(r2, size=size, color=color, italic=italic)
    else:
        r = p.add_run(text)
        set_run_font(r, size=size, color=color, italic=italic)
    return p


def heading(doc, text, level=1):
    p = doc.add_paragraph(style=f"Heading {level}")
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_before = Pt(10 if level == 1 else 7)
    p.paragraph_format.space_after = Pt(5)
    r = p.add_run(text)
    set_run_font(r, size={1: 16, 2: 12.5, 3: 11}[level], bold=True, color=NAVY if level == 1 else BLUE)
    return p


def add_callout(doc, title, body, fill=PALE_GOLD, accent=RED):
    t = doc.add_table(rows=1, cols=1)
    t.style = "Table Grid"
    cell = t.cell(0, 0)
    shade(cell, fill)
    set_cell_margins(cell, top=150, start=170, bottom=150, end=170)
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(title)
    set_run_font(r, 10.5, True, accent)
    p2 = cell.add_paragraph()
    p2.paragraph_format.space_after = Pt(0)
    p2.paragraph_format.line_spacing = 1.1
    r2 = p2.add_run(body)
    set_run_font(r2, 10.5)
    doc.add_paragraph().paragraph_format.space_after = Pt(1)


def add_page_number(paragraph):
    run = paragraph.add_run("第 ")
    set_run_font(run, 8.5, color=GRAY)
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    paragraph._p.append(fld)
    run2 = paragraph.add_run(" 頁｜候選示範；未核准、未執行")
    set_run_font(run2, 8.5, color=GRAY)


def configure_doc(doc):
    sec = doc.sections[0]
    sec.page_width = Inches(8.27)
    sec.page_height = Inches(11.69)
    sec.top_margin = Inches(0.67)
    sec.bottom_margin = Inches(0.67)
    sec.left_margin = Inches(0.72)
    sec.right_margin = Inches(0.72)
    sec.header_distance = Inches(0.32)
    sec.footer_distance = Inches(0.32)

    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    normal._element.rPr.rFonts.set(qn("w:ascii"), FONT)
    normal._element.rPr.rFonts.set(qn("w:hAnsi"), FONT)
    normal.font.size = Pt(10.5)
    normal.paragraph_format.space_after = Pt(5)
    normal.paragraph_format.line_spacing = 1.12
    for name in ("Heading 1", "Heading 2", "Heading 3"):
        style = doc.styles[name]
        style.font.name = FONT
        style._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
        style._element.rPr.rFonts.set(qn("w:ascii"), FONT)
        style._element.rPr.rFonts.set(qn("w:hAnsi"), FONT)

    hp = sec.header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hp.paragraph_format.space_after = Pt(0)
    hr = hp.add_run("TTQS ONE｜DOCX 0049 · I11-E01 · 官方方框 051    SAMPLE / SYNTHETIC · NOT A REAL ASSOCIATION RECORD")
    set_run_font(hr, 8, bold=True, color=RED)
    fp = sec.footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fp.paragraph_format.space_before = Pt(0)
    fp.paragraph_format.space_after = Pt(0)
    add_page_number(fp)


def read_source_data():
    assert sha256(SOURCE_DOC) == SOURCE_SHA, "0033 candidate SHA changed; stop to re-read exact source"
    assert sha256(SOURCE_REGISTER) == SOURCE_REGISTER_SHA, "0033 replacement register SHA changed"
    assert sha256(BLUEPRINT) == BLUEPRINT_SHA, "current Unique Blueprint SHA changed"
    progress = json.loads(SOURCE_PROGRESS.read_text(encoding="utf-8"))
    assert progress["doc_id"] == "0033" and progress["candidate_sha256"] == SOURCE_SHA
    row = None
    for line in BLUEPRINT.read_text(encoding="utf-8-sig").splitlines():
        obj = json.loads(line)
        if str(obj.get("deliverable_id")) == DOC_ID:
            row = obj
            break
    assert row is not None and row["requirement_id"] == "I11-E01"
    src = Document(str(SOURCE_DOC))
    importance = [[c.text.strip() for c in r.cells] for r in src.tables[8].rows]
    confidence = [[c.text.strip() for c in r.cells] for r in src.tables[9].rows]
    alternatives = [[c.text.strip() for c in r.cells] for r in src.tables[13].rows]
    modules = [[c.text.strip() for c in r.cells] for r in src.tables[15].rows]
    assert len(importance) == 10 and len(confidence) == 10
    assert len(alternatives) == 4 and len(modules) == 5
    assert importance[0][0] == "匿名代碼" and confidence[0][0] == "匿名代碼"
    assert [x[0] for x in importance[1:]] == [x[0] for x in confidence[1:]]
    reg = list(csv.DictReader(SOURCE_REGISTER.open("r", encoding="utf-8-sig", newline="")))
    return row, importance, confidence, alternatives, modules, reg


def add_register_row(rows, *, fact_id, section, anchor, row_key, field, value, status, source_fact_id="", source_doc="", note=""):
    rows.append({
        "fact_id": fact_id,
        "case_id": CASE_ID,
        "doc_id": DOC_ID,
        "section": section,
        "table_anchor": anchor,
        "row_key": row_key,
        "field": field,
        "value": str(value),
        "provenance_status": status,
        "assumption_or_basis": note,
        "source_doc_id": source_doc,
        "source_docx_sha256": SOURCE_SHA if source_doc == "0033" else "",
        "source_fact_id": source_fact_id,
        "required_replacement_source": "正式使用時取得協會現行原始資料；本候選的合成值須整筆替換並重算",
        "owner_role_to_confirm": "實際授權的課程規劃責任者（姓名與權限待核）",
        "verification_status": "SAMPLE_ONLY_NOT_VERIFIED_AS_REAL",
        "cross_document_refs": "同一SAMPLE案例；不可推論為協會真實活動",
        "locator_marker": f"{section}｜{anchor}｜{row_key}｜{field}",
    })


def make_register(importance, confidence, source_register):
    rows = []
    src_by_key = {(x.get("row_key", ""), x.get("field", "")): x for x in source_register}
    labels = {
        "甲": "工作界線與適切轉介",
        "乙": "尊重溝通與需求確認",
        "丙": "活動流程與現場安全",
        "丁": "最小必要紀錄與交接",
    }
    for table_name, data, suffix in (("表3", importance, "IMP"), ("表4", confidence, "SELF")):
        for record in data[1:]:
            respondent, group = record[0], record[1]
            group_src = src_by_key.get((respondent, "來源群組"))
            add_register_row(rows, fact_id=f"F0049_XREF_{respondent}_GROUP_{suffix}", section="第3節", anchor=table_name,
                             row_key=respondent, field="合成來源組別", value=group,
                             status="SYNTHETIC_CROSS_DOCUMENT_REFERENCE",
                             source_fact_id=(group_src or {}).get("fact_id", ""), source_doc="0033",
                             note=f"讀自0033 R03 exact SHA {SOURCE_SHA}，同一案例 {CASE_ID}；原值仍為合成資料。")
            for code, val in zip(("甲", "乙", "丙", "丁"), record[2:]):
                src_field = labels[code] + ("重要度" if suffix == "IMP" else "自評")
                src = src_by_key.get((respondent, src_field))
                assert src is not None, f"missing source register row: {respondent} {src_field}"
                add_register_row(rows, fact_id=f"F0049_XREF_{respondent}_{code}_{suffix}", section="第3節",
                                 anchor=table_name, row_key=respondent, field=f"能力{code}{'重要度' if suffix == 'IMP' else '自評'}",
                                 value=val, status="SYNTHETIC_CROSS_DOCUMENT_REFERENCE", source_fact_id=src["fact_id"], source_doc="0033",
                                 note=f"逐值承接0033 R03 {src['table_anchor']}；兩文件共同使用 {CASE_ID}，不可冒充REAL。")

    source_facts = [
        ("F0049_CASE_ID", "封面", "文件控制", "案例", "案例識別碼", CASE_ID),
        ("F0049_PLAN_DATE", "第1節", "文件識別", "示範時點", "示範計畫形成日", "2026-08-20"),
        ("F0049_SURVEY_START", "第2節", "表2", "調查期間", "起日", "2026-08-03"),
        ("F0049_SURVEY_END", "第2節", "表2", "調查期間", "迄日", "2026-08-14"),
        ("F0049_INVITED", "第3節", "表2", "合計", "邀請數", "12"),
        ("F0049_RETURNED", "第3節", "表2", "合計", "回收數", "10"),
        ("F0049_VALID", "第3節", "表2", "合計", "有效數", "9"),
        ("F0049_OWNER_SCOPE", "第2節", "表2", "合作窗口", "樣本角色映射限制", "合成合作窗口暫作需求提出方；不等同真實業主或委託契約"),
    ]
    for fid, section, anchor, key, field, value in source_facts:
        add_register_row(rows, fact_id=fid, section=section, anchor=anchor, row_key=key, field=field, value=value,
                         status="SYNTHETIC_CROSS_DOCUMENT_REFERENCE", source_doc="0033",
                         note=f"讀自0033 R03及同一案例；原件／真實調查未提供；候選SHA {SOURCE_SHA}。")

    plan_facts = [
        ("F0049_COURSE_TITLE", "課程計畫", "課程", "名稱", "課程名稱", "志工服務紀錄、交接與工作界線實務", "由合成方案甲4.80/5擬議；不是協會已開課課程"),
        ("F0049_COHORT_SIZE", "課程計畫", "表6", "班級", "示範規劃人數", "12", "合成班級規模；需依真實需求、師資及場地重估；與0033 R03同一SAMPLE案例一致"),
        ("F0049_TOTAL_MINUTES", "課程計畫", "表7", "總時數", "教學分鐘", "360", "四單元90+90+120+60；依0033 R03表13示範時數合計"),
        ("F0049_DAY_COUNT", "課程計畫", "表7", "日程", "分日數", "2", "為安排6小時教學及休息之合成日程"),
        ("F0049_BREAK_MIN", "課程計畫", "表7", "每日休息", "分鐘", "10", "示範排程假設，不含於教學分鐘"),
        ("F0049_ADMIN_MIN", "課程計畫", "表7", "每日行政", "分鐘", "10", "示範報到／收尾，不含於教學分鐘"),
        ("F0049_ROOM_SIZE", "課程計畫", "表8", "場地", "建議可用座位", "14", "12名學員加2名教學人員；現有場地能力未核實"),
        ("F0049_FACILITATORS", "課程計畫", "表8", "人力", "講師與觀察者", "1名帶領者、1名觀察協助者", "合成人力配置；非已聘任人員"),
        ("F0049_FOLLOWUP_DAYS", "追蹤", "表13", "課後追蹤", "天數", "14", "合成追蹤建議；未證明已執行"),
        ("F0049_REVISION_FAIL", "追蹤", "表13", "修訂觸發", "未達門檻", "同一能力兩次補練仍未達", "合成品質門檻；需由有權者依真實政策確認"),
        ("F0049_DESIGN_WEIGHT_DEMAND", "方案比較", "表5", "權重", "需求支持度", "40%", "直接承接0033 R03表12的合成權重"),
        ("F0049_DESIGN_WEIGHT_GAP", "方案比較", "表5", "權重", "能力差距回應", "30%", "直接承接0033 R03表12的合成權重"),
        ("F0049_DESIGN_WEIGHT_FEAS", "方案比較", "表5", "權重", "可行性", "20%", "直接承接0033 R03表12的合成權重"),
        ("F0049_DESIGN_WEIGHT_ASSESS", "方案比較", "表5", "權重", "可評量性", "10%", "直接承接0033 R03表12的合成權重"),
        ("F0049_DESIGN_PICK", "方案比較", "表5", "暫擬", "順位1", "方案甲4.80/5", "依0033 R03表12與表13；僅合成擬議，未核准"),
        ("F0049_ALT_A_VECTOR", "方案比較", "表5", "方案甲", "四面向原始分與加權結果", "需求5；差距5；可行4；可評5；40/30/20/10加權=4.80/5", "沿用0033 R03表12同案SAMPLE值；不是協會實際評分"),
        ("F0049_ALT_B_VECTOR", "方案比較", "表5", "方案乙", "四面向原始分與加權結果", "需求4；差距4；可行4；可評4；40/30/20/10加權=4.00/5", "沿用0033 R03表12同案SAMPLE值；不是協會實際評分"),
        ("F0049_ALT_C_VECTOR", "方案比較", "表5", "方案丙", "四面向原始分與加權結果", "需求3；差距3；可行5；可評4；40/30/20/10加權=3.50/5", "沿用0033 R03表12同案SAMPLE值；不是協會實際評分"),
        ("F0049_PRIORITY_D", "需求分析", "表5", "能力丁", "均值與排序", "重要度39/9=4.33；自評21/9=2.33；差距2.00；第1", "沿用0033 R03表10；自評非實作證據"),
        ("F0049_PRIORITY_A", "需求分析", "表5", "能力甲", "均值與排序", "重要度41/9=4.56；自評24/9=2.67；差距1.89；第2", "沿用0033 R03表10；自評非實作證據"),
        ("F0049_PRIORITY_B", "需求分析", "表5", "能力乙", "均值與排序", "重要度38/9=4.22；自評25/9=2.78；差距1.44；第3", "沿用0033 R03表10；自評非實作證據"),
        ("F0049_PRIORITY_C", "需求分析", "表5", "能力丙", "均值與排序", "重要度35/9=3.89；自評27/9=3.00；差距0.89；本例門檻未達但保留風險核對", "沿用0033 R03表10；自評非實作證據"),
        ("F0049_PLAN_STATUS", "封面", "文件控制", "狀態", "候選狀態", "SAMPLE示範計畫；NOT APPROVED；NOT IMPLEMENTED", "不表示原始點協會已有課程計畫或核准"),
        ("F0049_G1_CRITERION", "第5節", "目標表", "G1", "合格判準", "5個合成情境至少4題正確", "源自0033 R03表13的合成課程目標；不是實際學員成績"),
        ("F0049_G2_CRITERION", "第5節", "目標表", "G2", "合格判準", "四項行為至少3項達標", "課程層級示範門檻，待真實授權者確認"),
        ("F0049_G3_CRITERION", "第5節", "目標表", "G3", "合格判準", "5個必要欄完整且不含不必要個資", "源自0033 R03表13的合成單元目標"),
        ("F0049_G4_CRITERION", "第5節", "目標表", "G4", "合格判準", "整合檢核表全項完成；未達標重作並再評", "課程計畫的合成達標條件"),
        ("F0049_TEST_ITEMS", "第7節", "評量表", "課前測驗", "題數與計分", "10題；每題1分；總分0至10分", "題庫與計分均為示範設計"),
        ("F0049_TEST_THRESHOLD", "第7節", "評量表", "課前／課後", "示範門檻", "至少8/10", "非協會已採用門檻；核准後才可正式施測"),
        ("F0049_ROLE_THRESHOLD", "第7節", "表10", "角色演練", "示範門檻", "四項各0或1分；至少3/4且無關鍵隱私違規", "合成評量設計；無真實學員表現"),
        ("F0049_SCHEDULE_D1_AM", "第6節", "表7", "第1日第一單元", "時間與分鐘", "09:10–10:40；90分鐘", "依四單元360分鐘配置的示範時程"),
        ("F0049_SCHEDULE_D1_ADMIN", "第6節", "表7", "第1日報到", "時間與分鐘", "09:00–09:10；10分鐘行政", "不計教學時數"),
        ("F0049_SCHEDULE_D1_BREAK", "第6節", "表7", "第1日休息", "時間與分鐘", "10:40–10:50；10分鐘", "不計教學時數"),
        ("F0049_SCHEDULE_D1_PM", "第6節", "表7", "第1日第二單元", "時間與分鐘", "10:50–12:20；90分鐘", "依四單元360分鐘配置的示範時程"),
        ("F0049_SCHEDULE_D2_AM", "第6節", "表7", "第2日第一單元", "時間與分鐘", "09:10–11:10；120分鐘", "依四單元360分鐘配置的示範時程"),
        ("F0049_SCHEDULE_D2_ADMIN", "第6節", "表7", "第2日報到", "時間與分鐘", "09:00–09:10；10分鐘行政", "不計教學時數"),
        ("F0049_SCHEDULE_D2_BREAK", "第6節", "表7", "第2日休息", "時間與分鐘", "11:10–11:20；10分鐘", "不計教學時數"),
        ("F0049_SCHEDULE_D2_PM", "第6節", "表7", "第2日第二單元", "時間與分鐘", "11:20–12:20；60分鐘", "依四單元360分鐘配置的示範時程"),
        ("F0049_PRE_POST_IN_MODULES", "第6節", "表7", "測驗時數", "前後測配置", "前測含單元一；後測含單元四；不另加總", "示範時程算術規則，防止教學分鐘重複加總"),
        ("F0049_BREAK_ADMIN_TOTAL", "第6節", "表7", "每日非教學時間", "休息與行政", "每日10分鐘休息＋10分鐘行政；合計不列教學", "合成時程假設"),
        ("F0049_SAMPLE_MIN_N", "第8節", "風險表", "樣本不足", "觸發門檻", "有效樣本少於6或任一來源少於2", "承接0033 R03示範規則；不是官方抽樣要求"),
        ("F0049_ROLE_RPLAN", "第6節", "表8", "R-PLAN", "示範責任角色", "課程規劃責任者；權限未核實前只擬議", "角色代碼與責任為SAMPLE流程設計"),
        ("F0049_ROLE_RSURVEY", "第6節", "表8", "R-SURVEY", "示範責任角色", "調查承辦者；不收不必要個資並保留分母／排除原因", "角色代碼與責任為SAMPLE流程設計"),
        ("F0049_ROLE_RTEACH", "第6節", "表8", "R-TEACH", "示範責任角色", "課程帶領者；正式授課前核實能力與服務界線", "角色代碼與責任為SAMPLE流程設計"),
        ("F0049_ROLE_ROBS", "第6節", "表8", "R-OBS", "示範責任角色", "評量觀察者；使用同一量尺並保留分歧", "角色代碼與責任為SAMPLE流程設計"),
        ("F0049_ROLE_RAUTH", "第6節", "表8", "R-AUTH", "示範責任角色", "實際授權決策者；姓名、權限與決議原件待核", "不是已知真人或正式職稱指派"),
    ]
    for item in plan_facts:
        if len(item) == 6:
            fid, section, anchor, key, field, value = item
            note = "由文內流程／格式設計；正式使用前依真實來源核實。"
        else:
            fid, section, anchor, key, field, value, note = item
        is_cross_source = "0033" in note
        add_register_row(rows, fact_id=fid, section=section, anchor=anchor, row_key=key, field=field, value=value,
                         status="SYNTHETIC_CROSS_DOCUMENT_REFERENCE" if is_cross_source else "SYNTHETIC_PLAN_ASSUMPTION",
                         source_doc="0033" if is_cross_source else "", note=note)

    quiz_facts = [
        ("Q01", "超出角色權限的服務要求；A先承諾／B說明界線並按核實流程交接／C自行判斷處理；答案B"),
        ("Q02", "不確定委託者期待；A猜測／B追問目的、範圍與可接受輸出／C直接拒絕全部需求；答案B"),
        ("Q03", "匿名交接紀錄；A任務狀態與下一步責任／B無關家庭資料／C可識別個資貼到群組；答案A"),
        ("Q04", "不完整需求表的分母；A空白補0／B按預設有效規則排除並留原因／C當成沒有需求；答案B"),
        ("Q05", "自評很有把握是否代表已達能力；A可以／B要看目標對應可觀察作品或演練／C出席即可；答案B"),
        ("Q06", "資訊不足影響下一步；A猜答案／B列未知、責任角色及待補來源／C刪案件；答案B"),
        ("Q07", "教材含未授權承諾；A先授課／B停用該段、核實界線並修訂版本／C口頭提醒；答案B"),
        ("Q08", "三源需求衝突；A只採業主意見／B分源呈現、補證並核對權限／C平均後寫共識；答案B"),
        ("Q09", "交接完成條件；A說過即算／B記接手責任並確認下一步／C資訊貼給全體；答案B"),
        ("Q10", "匿名演練含可識別個資；A保留／B停止擴散、依權限處理並改用虛構案例／C只刪姓名；答案B"),
    ]
    for qid, value in quiz_facts:
        add_register_row(rows, fact_id=f"F0049_QUIZ_{qid}", section="第7節", anchor="表9", row_key=qid,
                         field="合成情境測驗題、選項與答案鍵", value=value,
                         status="SYNTHETIC_ASSESSMENT_DESIGN", note="正式施測前由課程責任者核對服務界線、答案及難度；非協會正式測驗或學員成績。")
    rubric = [
        ("界線辨識", "指出超出角色範圍並停止自行承諾。", "未辨識或仍自行承諾。"),
        ("開放提問／需求重述", "用開放提問取得必要資訊，再中性重述並確認意思。", "跳過提問／確認或把推測當事實。"),
        ("下一步確認", "說明待確認事項、接手責任角色與確認方式。", "沒有下一步或責任角色。"),
        ("最小必要紀錄", "只記任務、狀態、未結事項、下一步、責任角色；不添不必要個資。", "欄位缺漏或記入不必要個資。"),
    ]
    for i, (label, yes, no) in enumerate(rubric, 1):
        add_register_row(rows, fact_id=f"F0049_RUBRIC_{i:02d}", section="第8節", anchor="表10", row_key=f"R{i:02d}",
                         field="合成評量規準", value=f"{label}；達標={yes}；未達={no}；0或1分，四項總分至少3分，且無關鍵隱私違規",
                         status="SYNTHETIC_ASSESSMENT_DESIGN", note="非已施測結果；正式採用前核對現行工作規範。")
    return rows


def add_document_content(doc, bp, imp, conf, alts, modules):
    # Cover page and an action-oriented first-page guide.
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(24)
    r = p.add_run("TTQS ONE｜訓練機構版")
    set_run_font(r, 12, True, TEAL)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run("0049｜三源需求到課程計畫")
    set_run_font(r, 24, True, NAVY)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(14)
    r = p.add_run("業主 × 受訓者 × 職能需求的調查判讀與課程設計示範")
    set_run_font(r, 14, color=BLUE)
    add_callout(doc, "完整示範｜SAMPLE / SYNTHETIC｜NOT A REAL ASSOCIATION RECORD",
                "本文件是一份可操作的課程需求分析與計畫示範。案例日期、匿名角色、回覆、分數、計畫人數、課表、測驗、門檻與暫擬選擇均為合成資料；不表示社團法人屏東縣原始點關懷協會已調查、核准、開課、聘任、施測或取得成果。所有真實現況與權限均待原件核實。")
    add_table(doc, ["30秒內找到", "操作指引"], [
        ["用途", "把可追溯的需求來源轉成一項可比較、可執行、可評量的課程計畫。"],
        ["誰使用／何時", "課程規劃責任者及第二核對者；提出新課、定期檢討或需求改變時。"],
        ["先做什麼", "先核對第2節三源資料與真實權限；再看第4.1節方案比較及第6節計畫。"],
        ["做完留下什麼", "真實來源清單、需求排序、課程方案決策、目標／課表／師資與資源計畫、評量規準及覆核紀錄。"],
        ["目前狀態", "隔離候選示範；NOT APPROVED、NOT IMPLEMENTED。不得直接當協會正式核定計畫或實際成效。"],
    ], widths=[1.28, 5.55])
    add_para(doc, "文件識別：DOCX 0049｜Unique Blueprint I11-E01｜官方勾選流水號 051｜官方資料表第4頁。示範計畫形成日 2026-08-20（SAMPLE，非協會實際紀錄）；三種編號不可互換。", bold_prefix="文件識別：", color=NAVY)
    doc.add_page_break()

    heading(doc, "1｜決策摘要與使用邊界")
    add_para(doc, "本示範要回答的決策問題：在三源需求一致性與職能差距資料不足以代表真實協會之前，如何用一個完整、可重算的案例，展示從需求調查到課程目標、教學安排、資源、評量與後續修訂的規劃路徑。")
    add_table(doc, ["決策欄位", "本示範填寫結果", "正式使用前要補的真實證據"], [
        ["需求來源", "同一 SAMPLE 案例中的合成合作窗口、預定受訓者、任務角色代表；調查期間 2026-08-03 至 2026-08-14。", "實際業主／委託者授權、受訓者來源、去識別原始問卷、職能或任務分析原件。"],
        ["優先需求", "最小必要紀錄與交接、工作界線與適切轉介、尊重溝通與需求確認；活動流程安全保留風險核對。", "真實樣本數、分群、原始答案、排除規則、工作任務證據及第二人重算。"],
        ["暫擬方案", "方案甲「服務紀錄、交接與工作界線」加上溝通練習；合成比較分數 4.80/5。", "正式委託範圍、可用人力與場地、現行服務界線、實際授權者決策。"],
        ["課程安排", "四單元共360教學分鐘，分兩個半日；12人為同案示範班級規模。", "實際班級、講師能力與可用時段、場地可及性、教材及預算核實。"],
        ["評量", "10題情境測驗；四項角色演練規準；明列合格門檻、補練及再評量。", "正式題庫核准、評量者一致性、真實學員作答與成果記錄。"],
    ], widths=[1.05, 2.82, 2.96])
    add_callout(doc, "不得勾選為真實完成證據",
                "本稿的課程選擇只是同一合成案例內的示範擬議。沒有協會原始調查、現行職務／任務資料、核准紀錄及執行結果時，任何文字不得改寫成「本會已調查／已決定／已開課／已達標」。", fill=PALE, accent=NAVY)
    heading(doc, "1.1｜正確文類與相鄰要求", 2)
    add_table(doc, ["文件", "識別", "各自負責的證據", "本文件的連結方式"], [
        ["本件", "DOCX 0049｜I11-E01｜方框051", "三源需求如何被調查、比較並轉為課程計畫。", "本件主責；本示範保留案例與計畫決策鏈。"],
        ["需求調查", "DOCX 0033 R03｜I07-E01｜方框033", "課程需求調查設計、匿名回覆、職能需求差距與排序。", f"只在本 SAMPLE 案例中沿用已標示合成的數據；來源 SHA {SOURCE_SHA}。"],
        ["單元目標", "DOCX 0050｜I11-E02｜方框052", "逐單元行為目標、教學活動與單元評量對照。", "本件列課程層級目標和計畫架構；單元級細目應由0050處理。未確認同案候選前，不宣稱已形成跨檔案完整套件。"],
        ["採購／遴聘會議", "DOCX 0048｜I10-E03｜方框049", "大型採購與師資遴聘的會議／審查紀錄。", "不代替本件需求規劃；本件亦不虛構採購、遴聘或會議核准。"],
    ], widths=[1.15, 1.55, 2.15, 1.98])

    heading(doc, "2｜來源、案例與三源判讀規則")
    add_para(doc, "案例識別 SYN-0033-PLAN-01 與 DOCX 0033 R03 完全相同。此處是跨文件的 SAMPLE 資料鏈：0033 的合成調查結果作為0049的需求輸入；兩份候選都不是協會真實活動證明。不得把兩份 SAMPLE 報告加總成兩次獨立調查。")
    add_table(doc, ["來源／角色", "同案可用資料", "規劃用途", "真實性限制與核對方式"], [
        ["業主／客戶需求", "0033的「合作窗口」合成組別有3份有效回覆；同案Q04重要度原始值見0033 R03表8。", "展示委託端對優先能力與可接受產出的需求。", "合作窗口只是合成角色標籤，暫作需求提出方；不等於真實業主、委託契約或授權代表。真實使用須核實委託者身分與權限。"],
        ["受訓者需求", "0033合成預定受訓者3份有效回覆；回覆率與重要度／自評原始值可追溯。", "辨識學習困難、偏好、時間及可接受評量。", "不是協會會員或真實志工名冊；不得推論未回覆者沒有需求。"],
        ["職能／任務需求", "0033合成任務角色代表3份有效回覆；工作行為描述含界線、交接、最小必要紀錄及安全流程。", "把需求轉成可觀察行為與課程目標。", "自評把握度不等於實作能力；真實使用須有經授權的任務分析、工作樣本或觀察證據。"],
        ["官方佐證來源", "訓練機構版《TTQS查核佐證文件資料表》第4頁，官方原文逐字核對。", "決定本文件涵蓋範圍與對外標示。", f"官方來源PDF SHA-256：{OFFICIAL_PDF_SHA}；來源可支持官方文字與頁次，不支持協會已完成課程。"],
    ], widths=[1.18, 1.95, 1.45, 2.25])
    add_callout(doc, "三源不一致時的處理",
                "先分列來源與樣本，不用平均值掩蓋衝突；說明哪個任務、使用者或風險造成差異。若委託端目標超出受訓者角色或協會服務權限，先縮小課程範圍或暫停，不以課程設計替代治理授權。")

    heading(doc, "3｜調查分母、原始分數與交叉核對")
    add_para(doc, "原始問卷的完整題目、訪談提綱、有效判定及逐題示範答覆保存在 DOCX 0033 R03；本計畫只呈現設計決策所用的同案欄位，避免重複收集或重複計數。來源候選 exact SHA、替換簿及頁表定位列於本文件 SOURCE_MAP。")
    add_table(doc, ["合成來源組別", "邀請", "回收", "有效", "回收率", "有效／邀請"], [
        ["合作窗口", "4", "3", "3", "3÷4=75.0%", "3÷4=75.0%"],
        ["預定受訓者", "4", "3", "3", "3÷4=75.0%", "3÷4=75.0%"],
        ["任務角色代表", "4", "4", "3", "4÷4=100.0%", "3÷4=75.0%"],
        ["合計", "12", "10", "9", "10÷12=83.3%", "9÷12=75.0%"],
    ], widths=[1.4, 0.73, 0.73, 0.73, 1.3, 1.45], center_cols=(1, 2, 3, 4, 5))
    add_para(doc, "有效回收佔已回收＝9÷10＝90.0%。合成案例另有一份因Q04完整重要度矩陣缺漏而排除；兩位受邀對象未回覆。分母不混用：回收率以邀請數為分母；有效／邀請以邀請數為分母；有效／已回收以已回收數為分母。百分比四捨五入至小數1位。", size=10.5)
    heading(doc, "3.1｜匿名重要度原始值（1–5）", 2)
    rows_imp = [r for r in imp[1:]]
    add_table(doc, ["合成代碼", "來源組別", "甲 界線／轉介", "乙 溝通／確認", "丙 流程／安全", "丁 紀錄／交接"], rows_imp,
              widths=[0.9, 1.25, 1.22, 1.22, 1.22, 1.22], center_cols=(2, 3, 4, 5))
    heading(doc, "3.2｜匿名把握度自評（1–5；不等於實作能力）", 2)
    rows_conf = [r for r in conf[1:]]
    add_table(doc, ["合成代碼", "來源組別", "甲 界線／轉介", "乙 溝通／確認", "丙 流程／安全", "丁 紀錄／交接"], rows_conf,
              widths=[0.9, 1.25, 1.22, 1.22, 1.22, 1.22], center_cols=(2, 3, 4, 5))
    add_callout(doc, "解讀限制",
                "把握度是受訪者自評，不是觀察者能力評分，也不能證明課後學習成效。實際開課前需另確認服務任務和角色界線；課後評量須看匿名情境作品或演練表現。", fill=PALE, accent=NAVY)

    heading(doc, "4｜計算口徑、需求排序與課程設計比較")
    add_para(doc, "計算口徑沿用0033 R03合成案例：重要度平均＝該能力9份有效答案總分÷9；把握度平均＝9份有效自評總分÷9；差距＝重要度平均－把握度平均。平均值顯示至小數2位，排序以未四捨五入值計算；自評不是職能實作證據。")
    calc_rows = [
        ["丁｜最小必要紀錄與交接", "39÷9=4.33", "21÷9=2.33", "4.33−2.33=2.00", "SAMPLE優先擬議第1"],
        ["甲｜工作界線與適切轉介", "41÷9=4.56", "24÷9=2.67", "4.56−2.67=1.89", "SAMPLE優先擬議第2"],
        ["乙｜尊重溝通與需求確認", "38÷9=4.22", "25÷9=2.78", "4.22−2.78=1.44", "SAMPLE優先擬議第3"],
        ["丙｜活動流程與現場安全", "35÷9=3.89", "27÷9=3.00", "3.89−3.00=0.89", "未達本例門檻；保留風險核對"],
    ]
    add_table(doc, ["能力", "重要度平均", "自評平均", "差距", "示範解讀"], calc_rows,
              widths=[2.05, 1.0, 1.0, 0.85, 2.0], center_cols=(1, 2, 3))
    add_para(doc, "優先門檻是0033合成案例明示的示範規則：重要度≥4.00/5且差距≥1.20同時符合才列為優先擬議。它不是官方門檻或協會政策。丙雖未達，仍須核對真實任務風險，不得僅憑平均分排除。", size=10.5)
    heading(doc, "4.1｜三個可比較方案", 2)
    alt_rows = []
    for row in alts[1:]:
        alt_rows.append(row)
    add_table(doc, ["合成方案", "課程方向", "需求支持度", "差距回應", "假設可行性", "可評量性", "加權結果"], alt_rows,
              widths=[0.78, 1.75, 0.85, 0.85, 0.85, 0.78, 0.95], center_cols=(2, 3, 4, 5, 6))
    add_para(doc, "加權分＝需求支持度×40%＋差距回應×30%＋可行性×20%＋可評量性×10%；四面向均以1–5分。方案甲：5×0.40＋5×0.30＋4×0.20＋5×0.10＝4.80/5。方案乙＝4.00/5；方案丙＝3.50/5。權重與各面向分數都沿用0033 R03表12的合成示範；不可讀成協會實際可行性或真實投票。", size=10.5)
    add_table(doc, ["方案", "為何納入／未選", "示範決定與重開條件"], [
        ["甲｜服務紀錄、交接與工作界線", "同時回應合成能力丁與甲的前兩項差距；可用案例卡、匿名紀錄表及角色演練檢查。", "列本例第一順位、供擬議；真實需求、權限、師資與場地未核實前不開課。"],
        ["乙｜需求溝通與下一步確認", "重要度與差距均符合本例規則，但評估是否併入甲可避免重複安排。", "列次順位，可作甲的溝通練習；若真實調查證明為獨立任務再比較單獨開課。"],
        ["丙｜小型活動流程與現場安全", "合成重要度3.89與差距0.89未達本例雙門檻；風險仍須按任務核實。", "本輪延後獨立課程；若服務任務或場地風險改變，重新評估而不是沿用舊排序。"],
    ], widths=[1.75, 2.7, 2.55])
    add_callout(doc, "分數不是決議",
                "本表只展示如何透明比較選項。真正採用、延後、取消或變更課程，須由查明權限的實際責任者依現行章程／授權和真實需求作成可追溯決定；此文件沒有代替任何會議或核准。")

    heading(doc, "5｜擬議課程目標與需求—教學—評量映射")
    p5 = add_para(doc, "本例採用方案甲作為合成計畫方向，並把方案乙的需求確認能力整合進練習。目標以可觀察行為、情境條件及合格判準書寫。單元細部教學設計仍由 DOCX 0050（I11-E02／方框052）負責；下表是課程計畫層級的目標。")
    p5.paragraph_format.keep_with_next = True
    goal_rows = [
        ["G1｜界線與適切轉介", "面對5個合成服務情境，指出超出受訓角色的情境並選對交接責任。", "5題至少4題正確；不自行承諾未授權服務。", "差距甲；由案例判斷和角色演練處理。"],
        ["G2｜需求確認與交接", "在情境中完成界線辨識、開放提問／重述、下一步確認及最小必要紀錄。", "四項行為至少3項達標；不得把未確認資訊說成事實。", "差距乙與丁；以兩人角色演練及觀察表檢查。"],
        ["G3｜最小必要紀錄", "以匿名代碼完成任務、狀態、未結事項、下一步、接手角色5欄。", "5欄完整；不得記不必要身分或敏感個資。", "差距丁；用虛構案例填寫和同儕核對。"],
        ["G4｜整合交接", "整合案例完成交接，指出未知資訊、責任角色和需補來源。", "整合檢核表全項勾完；未達標時按回饋重作並再評。", "把甲、乙、丁串成任務流程；不代表實際服務成果。"],
    ]
    add_table(doc, ["課程目標", "可觀察行為", "合格判準（示範）", "需求依據與教學連結"], goal_rows,
              widths=[1.15, 2.35, 1.75, 1.75])
    add_para(doc, "目標範圍排除：醫療判斷、診斷、治療建議、未授權個案服務、正式志工資格核定或對外承諾。真實服務界線若未由協會權責來源核實，課程不得進入該任務情境。", bold_prefix="目標範圍排除：", color=RED)

    doc.add_page_break()
    heading(doc, "6｜課程計畫：內容、方法、時程、師資、教材與環境")
    add_table(doc, ["計畫欄位", "合成計畫內容", "前置確認／停止條件"], [
        ["課程名稱與目的", "志工服務紀錄、交接與工作界線實務；練習在匿名情境下確認需求、守住角色界線、完成最低必要交接。", "名稱、目的與實際服務方向須經真實權責來源核對。"],
        ["適用對象／入班條件", "示範班級12人；適用於經授權參與相關服務流程者。入班前說明角色限制、資料保護和情境演練規則。", "12人承接同一SAMPLE案例的規劃名額；實際受訓者須由授權者確認，不建立虛構名冊。"],
        ["先備條件", "能閱讀中文步驟卡；願意使用虛構案例演練；需提供無障礙或替代參與安排時先確認。", "不要求提交個人服務對象資料；未完成隱私告知或權限界線核實則暫緩。"],
        ["教學方法", "示範—分組練習—觀察回饋—修正再練；使用合成案例、匿名代碼和空白交接工作表。", "講師不得以未授權經驗或第三方個案作教材。"],
        ["師資配置", "合成配置：1名帶領者、1名觀察協助者；帶領者需能說明服務界線、示範匿名紀錄並按規準給回饋。", "尚未指定真人或聘任；以能力條件選任，確認可授課時間與利益／保密要求。"],
        ["教材／設備", "投影或白板、匿名情境卡、角色步驟卡、空白最小紀錄表、評量表、筆；紙本與電子資料均用虛構內容。", "數量與現有設備未核實；不得把示範教材稱為正式核准教材。"],
        ["學習環境", "可供12名學員與2名教學人員移動及兩人演練的場地；可分組、聽清指示並保護討論內容。", "建議14席是樣本假設；實地確認無障礙、動線、隱私與器材後才能排定。"],
    ], widths=[1.25, 3.2, 2.55])
    heading(doc, "6.1｜單元配置與教學輸出", 2)
    module_rows = []
    for row in modules[1:]:
        module_rows.append(row)
    add_table(doc, ["單元", "目標／內容", "評量標準", "教學分鐘"], module_rows,
              widths=[1.35, 2.75, 2.05, 0.85], center_cols=(3,))
    add_para(doc, "四單元分鐘合計＝90＋90＋120＋60＝360分鐘（6小時純教學）。模組名稱、行為和示範時數沿用0033 R03表13同案內容；本計畫補上資源、日程、評量及停止條件。", size=10.5)
    heading(doc, "6.2｜示範日程與責任分工", 2)
    add_table(doc, ["日／時段", "分鐘", "單元／工作", "責任角色", "留下的輸出"], [
        ["第1日 09:00–09:10", "10", "報到、說明隱私與演練規則（行政，不計教學）。", "課務承辦角色", "合成點名欄位示例；正式名冊另由授權者保管。"],
        ["第1日 09:10–10:40", "90", "單元一：角色界線與交接；含10題前測中對應情境題。", "帶領者／觀察者", "情境判斷作答與錯誤類型。"],
        ["第1日 10:40–10:50", "10", "休息。", "課務承辦角色", "不列入教學時數。"],
        ["第1日 10:50–12:20", "90", "單元二：需求確認與下一步；雙人角色演練。", "帶領者／觀察者", "四行為規準回饋。"],
        ["第2日 09:00–09:10", "10", "報到、回顧及匿名情境分組（行政，不計教學）。", "課務承辦角色", "確認材料與分組；不複製真實個資。"],
        ["第2日 09:10–11:10", "120", "單元三：最小必要紀錄；示範、填表、同儕核對。", "帶領者／觀察者", "五欄交接表及隱私檢核。"],
        ["第2日 11:10–11:20", "10", "休息。", "課務承辦角色", "不列入教學時數。"],
        ["第2日 11:20–12:20", "60", "單元四：整合演練、補充練習及後測／回饋。", "帶領者／觀察者", "整合評量、補練記錄欄位及匿名課程回饋。"],
    ], widths=[1.18, 0.55, 2.15, 1.18, 1.9], center_cols=(1,))
    add_para(doc, "每日上午：180教學分鐘＋10分鐘休息＋10分鐘行政＝200分鐘在場時間；兩日純教學合計360分鐘。前測、後測含在單元一與單元四時數中，不另加總。此日程是假設示範，未證明有場地、師資或實際排課。", size=10.5)
    add_table(doc, ["角色代碼（示範）", "責任", "覆核／接手規則"], [
        ["R-PLAN｜課程規劃責任者", "整合三源資料、比較方案、管理未決項及課程版本。", "權限未核實時只擬議；指定替代人須有真實授權。"],
        ["R-SURVEY｜調查承辦者", "告知目的、發放及回收、保留去識別分母與排除原因。", "不收不必要個資；第二核對者抽查原始彙總與計算。"],
        ["R-TEACH｜課程帶領者", "依課程計畫示範、帶練、回饋及記錄評量。", "正式授課前核實資格／經驗及服務界線；本稿無真人指派。"],
        ["R-OBS｜評量觀察者", "依同一量尺觀察，記錄證據與補練，不評人格。", "兩位評量者先用同一案例校準；分歧記錄並由授權者處理。"],
        ["R-AUTH｜實際授權決策者", "核對本會權限後決定採用、修訂、延後或取消。", "姓名、職稱、章程依據、決議日期和原件均待真實核實；不得預簽。"],
    ], widths=[1.35, 2.95, 2.65])

    heading(doc, "7｜評量計畫、量尺與合格門檻")
    add_para(doc, "測驗和門檻是為使計畫可操作而設的 SAMPLE 設計，不是協會已採用的規定。評量只測課程中練習的服務界線、需求確認與最低必要紀錄，不推論志工的整體能力或服務對象成果。")
    add_table(doc, ["評量時點／方法", "量尺與合格條件", "若未達標的處理", "保留證據"], [
        ["課前：10題情境短測，單題1分。", "0–10分；示範合格門檻≥8分。作為教學起點，不作個人資格判定。", "找出錯題主題；講師調整示例，不貼個人分數。", "匿名代碼、測驗版本、題目作答、分母及評量日期（正式執行才產生）。"],
        ["課程中：雙人角色演練觀察表。", "四項各0或1分；至少3/4，且無關鍵隱私違規。", "立即指出具體行為，提供一次示範和練習，再用同一規準重評。", "觀察表、情境版本、評量者代碼、回饋及重評欄位。"],
        ["課後：同規格平行題後測＋整合情境。", "後測≥8/10；整合檢核各必要欄完整，未知事項標明，交接角色正確。", "列未達目標、補練內容、再評日期；未重評前狀態為未達／待補，不寫通過。", "匿名前後測差異、規準、缺失與處理軌跡。"],
        ["課後回饋／計畫檢討。", "描述有用環節、仍卡步驟、材料與環境障礙；不以滿意度代替能力。", "若需求、任務或界線改變，回到三源重新調查；必要時停用材料。", "去識別課程回饋摘要及下一次計畫修訂依據。"],
    ], widths=[1.45, 1.85, 2.0, 1.65])
    heading(doc, "7.1｜情境測驗題庫（示範版）", 2)
    quiz = [
        ["Q1", "接到超出角色權限的服務要求，第一步？", "A. 先承諾\nB. 說明界線並按核實流程交接\nC. 自行判斷處理", "B"],
        ["Q2", "受訓者不確定委託者期待時，最合適作法？", "A. 猜測\nB. 追問目的、範圍與可接受輸出\nC. 直接拒絕全部需求", "B"],
        ["Q3", "匿名交接紀錄應包含什麼？", "A. 任務狀態與下一步責任\nB. 無關家庭資料\nC. 可識別個資貼到群組", "A"],
        ["Q4", "收到不完整需求表時，計算分母如何處理？", "A. 空白補0\nB. 依預設有效規則標記排除並保留原因\nC. 當成沒有需求", "B"],
        ["Q5", "受訓者說自己很有把握，能否當作已達能力？", "A. 可以\nB. 不可以，需看目標對應的可觀察作品／演練\nC. 只要出席就可以", "B"],
        ["Q6", "情境資訊不足且影響下一步時，紀錄應如何寫？", "A. 猜一個答案\nB. 明列未知資訊、責任角色及待補來源\nC. 刪掉案件", "B"],
        ["Q7", "發現教材教導未授權承諾時，應？", "A. 先授課再說\nB. 停用該段、核對正式界線並修訂版本\nC. 改成口頭提醒", "B"],
        ["Q8", "三源需求排序時出現衝突，應？", "A. 只採業主意見\nB. 分源呈現衝突、補證並核對權限\nC. 取平均後寫成共識", "B"],
        ["Q9", "轉介或交接的完成條件應是？", "A. 說過就算\nB. 記錄接手責任與確認下一步\nC. 把所有資訊轉貼給全體", "B"],
        ["Q10", "匿名演練出現真實可識別個資時，應？", "A. 保留作好例子\nB. 停止擴散、依權限處理並改用虛構案例\nC. 只刪姓名但留其他識別線索", "B"],
    ]
    add_table(doc, ["題號", "情境題", "選項", "答案鍵"], quiz,
              widths=[0.55, 2.05, 3.55, 0.8], center_cols=(0, 3))
    add_para(doc, "計分：每題答對1分；不得倒扣。示範門檻≥8/10；正式施測前由真實授權者核對題意、現行流程和答案鍵。若採前後測，需製作難度相當的平行版，記錄版本，不直接重複同題造成記憶效應。", size=10.5)
    heading(doc, "7.2｜角色演練四項行為規準", 2)
    add_table(doc, ["觀察項", "達標＝1", "未達＝0", "關鍵錯誤／回饋"], [
        ["界線辨識", "指出超出角色範圍並停止自行承諾。", "未辨識或仍自行承諾。", "若承諾未授權服務，記為關鍵錯誤並立即補練。"],
        ["開放提問／需求重述", "用開放提問取得必要資訊，再以中性語言重述並確認對方意思。", "跳過提問／確認，或把推測當事實。", "指出原句和可替代提問。"],
        ["下一步確認", "清楚說明待確認事項及負責角色。", "沒有下一步或責任角色。", "補上交接對象與確認方式。"],
        ["最小必要紀錄", "只記任務、狀態、未結事項、下一步、責任角色；不添不必要個資。", "欄位缺漏或記入不必要個資。", "關鍵隱私違規者不論總分均先停止評量、按正式規則處理。"],
    ], widths=[1.35, 2.1, 1.9, 1.65])
    add_para(doc, "評量門檻：四項至少3分且無關鍵隱私違規。觀察者須在可見行為欄記錄例句或作品位置，不記人格標籤。兩名評量者如有差異，先對照規準討論並保留原分，不以平均掩蓋分歧。", size=10.5)

    heading(doc, "8｜資源、風險、追蹤及修訂控制")
    add_table(doc, ["假設／風險與觸發", "預防或立即處置", "責任角色", "重開計畫／留存"], [
        ["有效樣本少於6份，或任一來源組少於2份。", "補問或縮小結論；列明來源缺口，不沿用舊排序。", "調查承辦者／第二核對者", "重算分母；更新計畫版本和需求決定依據。"],
        ["合作窗口與受訓者需求相反。", "分組呈現原話與任務情境；確認權限與服務範圍，必要時拆分課程或不辦。", "規劃責任者／實際授權決策者", "保留差異、補件責任及期限；不得寫成共識。"],
        ["師資或場地條件無法核實。", "不排正式課；取得能力／時段與場地可及性證據後重做可行性評分。", "課程承辦角色", "更新方案評分與資源清單。"],
        ["出現真實個資或敏感個案資訊。", "停止擴散、保留最小必要紀錄，按經核實的資料處理規則轉交有權責者。", "資料責任者（待查）", "記錄事件處理來源；演練改用合成案例。"],
        ["教材或演練超出協會服務／受訓角色。", "立即停用該材料；核對正式服務界線，未查明前不開課。", "課程規劃者／授權者", "版本鎖定、修訂原因與覆核者可追溯。"],
        ["至少兩次補練仍未達同一目標（示範門檻）。", "檢討目標、教學支持、量尺與可及性；不要只把責任歸給學員。", "帶領者／課程檢討者", "此觸發為本例假設，正式使用前需授權確認。"],
        ["需求、任務或政策改變。", "停止沿用舊版，重新確認三源資料並複評方案。", "規劃責任者", "保留舊版、變更來源、新版差異和核准狀態。"],
    ], widths=[1.55, 2.35, 1.25, 1.8])
    add_table(doc, ["檢討時間點（示範）", "檢討內容", "判斷依據／輸出"], [
        ["開課前", "需求來源、權限、講師、場地、教材、測驗版本與隱私告知是否具備。", "任一關鍵項未核實則延後；記錄責任者與補件期限。"],
        ["課後14日", "去識別回饋、未達目標、教學障礙及可操作性。", "是否需補練、修訂單元、重開需求調查；不得推稱長期服務成效。"],
        ["有重大變更時", "服務範圍、任務角色、法規／政策、場地或需求變化。", "版本變更單、真實來源定位、授權決策和停用舊教材方式。"],
    ], widths=[1.3, 2.8, 2.85])
    add_callout(doc, "樣本資源清單",
                "合成估算：1名帶領者、1名觀察者、14席場地、情境卡、匿名紀錄表、評量表及筆。金額不估列，因無真實採購資料；本文件不聲稱已採購、已借用場地或已聘任師資。", fill=PALE_TEAL, accent=TEAL)

    heading(doc, "9｜官方要求追溯、跨文件事實與證據索引")
    add_table(doc, ["官方要求／來源", "本件對應位置", "示範證明路徑", "界線／正式替換"], [
        ["官方方框051：訓練課程計畫配合業主、受訓者以及職能需求等調查規劃的證明。官方資料表第4頁。", "第2–4節來源、分母、匿名原始值、差距和方案比較；第5–8節課程目標、內容、資源與評量。", "需求源→判讀→方案→課程計畫→評量→檢討。", "以官方PDF原件和真實委託／受訓／職能資料重做；合成數據不可轉成REAL。"],
        ["DOCX 0033 R03｜I07-E01｜方框033。", "同案問卷、樣本數、匿名答案、能力定義及方案評分。", f"共同案例ID {CASE_ID}；來源候選SHA {SOURCE_SHA}，來源替換簿SHA {SOURCE_REGISTER_SHA}。", "兩份文件同為SAMPLE；任何來源更動須重新核對本件是否仍吻合並更新引用。"],
        ["DOCX 0050｜I11-E02｜方框052。", "本件第5、6節列課程層級目標和四單元大綱。", "0050應展開各單元行為目標、教師活動與教學評量細節。", "目前未聲稱0050已形成同案成品；正式套件建立後再核同一課程ID、版本、目標及時數。"],
        ["DOCX 0048｜I10-E03｜方框049。", "第1.1節作負向鄰項區分。", "採購與師資遴聘會議紀錄屬不同要求。", "本件不虛構會議、採購、聘任或簽核。"],
    ], widths=[1.8, 1.75, 1.8, 1.6])
    heading(doc, "9.1｜交叉事實核對清單", 2)
    add_table(doc, ["共享事實／計算", "0033 R03", "本件0049 R01", "核對結果"], [
        ["案例ID與合成邊界", CASE_ID, CASE_ID, "一致；均明示SAMPLE，不代表協會真實活動。"],
        ["調查期間", "2026-08-03 至 2026-08-14", "同一期間", "一致；兩件不重複計為兩批調查。"],
        ["邀請／回收／有效", "12／10／9", "12／10／9", "一致；有效回覆率9÷12=75.0%。"],
        ["能力排序", "丁第1、甲第2、乙第3；丙保留風險核對", "沿用相同排序", "一致；來源計算可重算。"],
        ["方案甲加權分", "4.80/5，示範第1順位", "4.80/5，僅作合成擬議", "一致；未表述為協會正式決議。"],
        ["單元時數", "90＋90＋120＋60=360分", "同四單元、360分；兩個半日", "一致；行政及休息時間分開，不重複計入教學分鐘。"],
    ], widths=[1.55, 1.7, 1.7, 2.0])

    heading(doc, "10｜由SAMPLE轉為REAL的替換清單與驗收門檻")
    add_para(doc, "替換時不得只改封面或把SAMPLE標籤刪除。每一類來源完成後重新計算、覆核、更新文件版本及證據索引；未完成的項目仍保持候選或UNKNOWN。")
    add_table(doc, ["待替換類別", "必需的真實原件／讀回", "核對者應確認", "未完成時狀態"], [
        ["業主／委託需求", "真實委託者角色與授權、服務範圍、需求來源及日期；必要時有關會議／核准原件。", "身分、權限、原文、時點、範圍與限制；合成合作窗口不得沿用。", "UNKNOWN；不宣稱業主需求已查明。"],
        ["受訓者需求", "實際邀請／告知、去識別回收清冊、有效判定、原始答案及保管權限。", "邀請、回收、有效分母、排除理由、隱私及樣本限制。", "UNKNOWN；不把未回覆解讀為無需求。"],
        ["職能／任務需求", "經授權的現行角色說明、流程、匿名工作樣本或任務觀察；必要的專業邊界來源。", "資料來源適用性、角色範圍、觀察期間、評量者和差距計算。", "UNKNOWN；不以自評取代實作證據。"],
        ["課程選擇與授權", "真實方案比較、資源檢核、權責依據、實際決定與版本紀錄。", "決策者有權、不同意見已記錄、採用／延後理由可追溯。", "NOT APPROVED；不開課或對外宣稱已核准。"],
        ["師資、教材、場地與參訓者", "實際人員能力與同意、教材版本、場地可及性、課程時間及受訓者名單的有權來源。", "個資最小化、使用授權、無障礙、服務界線與容量。", "NOT SCHEDULED；不虛構聘任、出席或資源取得。"],
        ["評量與課後檢討", "實際題目版本、作答／作品、評量者、補練及去識別課程回饋。", "分數可重算、缺失如實、日期與樣本一致；不得推論未觀察的服務結果。", "NOT IMPLEMENTED；不宣稱達標或成效。"],
    ], widths=[1.35, 2.35, 2.0, 1.25])
    doc.add_page_break()
    heading(doc, "10.1｜正式採用前四道檢核門", 2)
    add_table(doc, ["檢核門", "必須回答的問題", "通過的最低證據"], [
        ["G1 來源", "業主、受訓者、職能三源是否來自可定位、具權限的真實原件？", "原件定位、日期、責任者、分母／樣本及限制均可讀回。"],
        ["G2 設計", "需求排序、課程方案、目標、評量、師資和環境是否互相吻合？", "第二人可重算；所有計畫字段有來源或明確假設；未解事項有責任人。"],
        ["G3 授權", "誰有權決定採用、調整、延後或取消？", "依正式章程／授權的真實決定記錄；不得用本示例代簽。"],
        ["G4 執行／回饋", "實際開課、評量與修訂有何原件？", "真實日期、人員、課程版本及匿名結果；未發生者保持未執行。"],
    ], widths=[1.05, 3.0, 2.85])
    add_callout(doc, "完成本件示範不等於完成正式佐證",
                "本候選只提供完整可用的SAMPLE方案和資料替換路徑。正式使用需完成上述檢核、取得真實授權及資料，並另行獨立驗收；任何簽章、正式決議、出席、執行結果和第三方事實都必須來自原件。")



def main():
    PACKAGE.joinpath("candidate").mkdir(parents=True, exist_ok=True)
    PACKAGE.joinpath("evidence/build").mkdir(parents=True, exist_ok=True)
    bp, imp, conf, alts, modules, source_register = read_source_data()
    assert bp["official_evidence_table_page"] == "4"
    assert bp["official_requirement_text"] == "訓練課程計畫配合業主、受訓者以及職能需求等調查規劃的證明。"
    assert bp["requirement_id"] == "I11-E01"
    score_cols = list(zip(*[[int(v) for v in r[2:]] for r in imp[1:]]))
    self_cols = list(zip(*[[int(v) for v in r[2:]] for r in conf[1:]]))
    assert [sum(c) for c in score_cols] == [41, 38, 35, 39]
    assert [sum(c) for c in self_cols] == [24, 25, 27, 21]
    assert round(5 * .4 + 5 * .3 + 4 * .2 + 5 * .1, 2) == 4.8
    assert sum(int(re.search(r"\d+", r[3]).group()) for r in modules[1:]) == 360
    doc = Document()
    configure_doc(doc)
    add_document_content(doc, bp, imp, conf, alts, modules)
    doc.core_properties.title = "0049｜三源需求到課程計畫｜I11-E01 SAMPLE示範"
    doc.core_properties.subject = "訓練機構版 TTQS 官方方框051；合成示範，不是協會真實紀錄"
    doc.core_properties.author = "TTQS ONE 候選文件施工"
    doc.core_properties.keywords = "SAMPLE; SYNTHETIC; 0049; I11-E01; checkbox 051"
    doc.save(DOCX_PATH)

    register = make_register(imp, conf, source_register)
    reg_path = PACKAGE / "evidence/SYNTHETIC_REPLACEMENT_REGISTER_R01.csv"
    reg_path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(register[0].keys())
    with reg_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(register)

    now = datetime.now(timezone.utc).isoformat()
    metadata = {
        "project_id": "TTQS_ONE",
        "doc_id": DOC_ID,
        "revision": REVISION,
        "requirement_id": bp["requirement_id"],
        "official_checkbox_sequence": "051",
        "official_requirement": bp["official_requirement_text"],
        "official_source_page": 4,
        "candidate_path": "candidate/0049_R01.docx",
        "candidate_sha256": sha256(DOCX_PATH),
        "candidate_bytes": DOCX_PATH.stat().st_size,
        "sample_status": "SAMPLE_SYNTHETIC_ONLY_NOT_APPROVED_NOT_IMPLEMENTED",
        "shared_case_id": CASE_ID,
        "cross_document_source": {
            "doc_id": "0033",
            "revision": "R03",
            "requirement_id": "I07-E01",
            "official_checkbox_sequence": "033",
            "candidate_sha256": SOURCE_SHA,
            "replacement_register_sha256": SOURCE_REGISTER_SHA,
            "relationship": "same synthetic case; 0033 is needs-survey evidence, 0049 is course plan; no real association activity implied",
        },
        "source_hashes": {
            "unique_blueprint_current_jsonl": BLUEPRINT_SHA,
            "official_evidence_table_pdf": OFFICIAL_PDF_SHA,
        },
        "register_path": "evidence/SYNTHETIC_REPLACEMENT_REGISTER_R01.csv",
        "register_rows": len(register),
        "register_sha256": sha256(reg_path),
        "build_utc": now,
    }
    (PACKAGE / "evidence/build/BUILD_METADATA_R01.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metadata, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()


