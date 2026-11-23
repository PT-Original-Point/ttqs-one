from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from pypdf import PdfReader


PACKAGE = Path(__file__).resolve().parents[2]
REPO = Path(__file__).resolve().parents[6]
DOCS = REPO / "docs" / "ttqs-quality-20261016"
QA = PACKAGE / "evidence" / "qa"
INPUTS = PACKAGE / "inputs"
CANDIDATE = PACKAGE / "candidate" / "0053_R01.docx"
RUNTIME = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME")

BLUEPRINT_PATH = RUNTIME / "CONTROL" / "BLUEPRINT_CURRENT.jsonl"
CROSSWALK_PATH = RUNTIME / "CONTROL" / "TTQS_ONE_129_REQUIREMENT_TO_142_DELIVERABLE_CROSSWALK_R01.csv"
OFFICIAL_PDF = RUNTIME / "SOURCES" / "TTQS查核佐證文件資料表-訓練機構版 (2).pdf"
SOURCE_PAGE_IMAGE = DOCS / "quality-review" / "0052_R01" / "inputs" / "official_evidence_table_page4.png"
DOC_0033 = DOCS / "quality-review" / "0033_R03" / "candidate" / "0033_R03.docx"
DOC_0052 = DOCS / "quality-review" / "0052_R01" / "candidate" / "0052_R01.docx"
OFFICIAL_REQUIREMENT = "近年針對訓練課程的切合性，有檢討並調整遴選學員、教材、師資、教學方法與訓練設施的過程，或有完整文書手冊與紀錄分析相關資料並持續改善。"

NAVY = "153B50"
TEAL = "087E8B"
PALE = "EAF4F5"
PALE_BLUE = "EEF3F8"
GOLD = "E2A83B"
INK = "24323A"
MID = "52636C"
RED = "A33C35"
GREEN = "28734A"
WHITE = "FFFFFF"
LINE = "D4DEE2"
FONT = "Microsoft JhengHei"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def xml_set(node, tag: str, value: str) -> None:
    element = node.find(qn(tag))
    if element is None:
        element = OxmlElement(tag)
        node.append(element)
    element.set(qn("w:val"), value)


def set_run_font(run, size=10.5, bold=False, color=INK, italic=False):
    run.font.name = FONT
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = RGBColor.from_string(color)
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.rFonts
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    for key in ("ascii", "hAnsi", "eastAsia", "cs"):
        rfonts.set(qn(f"w:{key}"), FONT)


def shade(cell, fill: str):
    tcpr = cell._tc.get_or_add_tcPr()
    shd = tcpr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tcpr.append(shd)
    shd.set(qn("w:fill"), fill)


def cell_margins(cell, top=75, start=85, bottom=75, end=85):
    tc = cell._tc
    tcpr = tc.get_or_add_tcPr()
    mar = tcpr.first_child_found_in("w:tcMar")
    if mar is None:
        mar = OxmlElement("w:tcMar")
        tcpr.append(mar)
    for side, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        item = mar.find(qn(f"w:{side}"))
        if item is None:
            item = OxmlElement(f"w:{side}")
            mar.append(item)
        item.set(qn("w:w"), str(value))
        item.set(qn("w:type"), "dxa")


def set_cell_border(cell, color=LINE, size="5"):
    tcpr = cell._tc.get_or_add_tcPr()
    borders = tcpr.first_child_found_in("w:tcBorders")
    if borders is None:
        borders = OxmlElement("w:tcBorders")
        tcpr.append(borders)
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        tag = qn(f"w:{edge}")
        element = borders.find(tag)
        if element is None:
            element = OxmlElement(f"w:{edge}")
            borders.append(element)
        element.set(qn("w:val"), "single")
        element.set(qn("w:sz"), size)
        element.set(qn("w:space"), "0")
        element.set(qn("w:color"), color)


def mark_repeat_table_header(row):
    trpr = row._tr.get_or_add_trPr()
    repeat = OxmlElement("w:tblHeader")
    repeat.set(qn("w:val"), "true")
    trpr.append(repeat)


def prevent_row_split(row):
    trpr = row._tr.get_or_add_trPr()
    trpr.append(OxmlElement("w:cantSplit"))


def set_cell_text(cell, value, *, size=9.5, bold=False, color=INK, align=None):
    cell.text = ""
    for index, line in enumerate(str(value).split("\n")):
        paragraph = cell.paragraphs[0] if index == 0 else cell.add_paragraph()
        paragraph.paragraph_format.space_after = Pt(0)
        paragraph.paragraph_format.space_before = Pt(0)
        paragraph.paragraph_format.line_spacing = 1.03
        if align is not None:
            paragraph.alignment = align
        run = paragraph.add_run(line)
        set_run_font(run, size=size, bold=bold, color=color)
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    cell_margins(cell)
    set_cell_border(cell)


def set_cell_widths(table, widths_cm):
    for row in table.rows:
        for i, width in enumerate(widths_cm):
            if i < len(row.cells):
                row.cells[i].width = Cm(width)


def add_table(doc, headers, rows, widths_cm=None, *, font_size=9.5, header_fill=NAVY, first_col_bold=False, status_col=None):
    font_size = max(font_size, 9.5)
    table = doc.add_table(rows=1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    header = table.rows[0]
    mark_repeat_table_header(header)
    prevent_row_split(header)
    for i, value in enumerate(headers):
        cell = header.cells[i]
        shade(cell, header_fill)
        set_cell_text(cell, value, size=font_size, bold=True, color=WHITE)
    for row_index, values in enumerate(rows):
        row = table.add_row()
        prevent_row_split(row)
        for col_index, value in enumerate(values):
            cell = row.cells[col_index]
            fill = WHITE if row_index % 2 else PALE_BLUE
            if col_index == 0 and first_col_bold:
                fill = PALE
            if status_col == col_index:
                text = str(value)
                if "部分" in text or "未" in text or "待" in text or "PARTIAL" in text or "HOLD" in text:
                    fill = "FFF3E2"
                elif "符合" in text or "PASS" in text or "已完成" in text:
                    fill = "E8F3EA"
            shade(cell, fill)
            set_cell_text(cell, value, size=font_size, bold=(first_col_bold and col_index == 0), color=INK)
    if widths_cm:
        set_cell_widths(table, widths_cm)
    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_after = Pt(1)
    spacer.paragraph_format.space_before = Pt(0)
    spacer.paragraph_format.line_spacing = 0.5
    return table


def add_body(doc, text, *, bold_lead=None, color=INK, size=10.5, after=5, align=None):
    size = max(size, 10.5)
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.line_spacing = 1.12
    if align is not None:
        p.alignment = align
    if bold_lead and text.startswith(bold_lead):
        r = p.add_run(bold_lead)
        set_run_font(r, size=size, bold=True, color=color)
        r = p.add_run(text[len(bold_lead):])
        set_run_font(r, size=size, color=color)
    else:
        r = p.add_run(text)
        set_run_font(r, size=size, color=color)
    return p


def add_bullet(doc, text, *, level=0, size=10.2):
    size = max(size, 10.5)
    p = doc.add_paragraph(style="List Bullet" if level == 0 else "List Bullet 2")
    p.paragraph_format.space_after = Pt(2.5)
    p.paragraph_format.line_spacing = 1.08
    r = p.add_run(text)
    set_run_font(r, size=size)
    return p


def add_heading(doc, text, level=1, *, subtitle=None):
    p = doc.add_paragraph(style=f"Heading {level}")
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_before = Pt(0 if level == 1 else 3)
    p.paragraph_format.space_after = Pt(6 if level == 1 else 4)
    r = p.add_run(text)
    set_run_font(r, size=15.5 if level == 1 else 11.5, bold=True, color=NAVY if level == 1 else TEAL)
    if subtitle:
        add_body(doc, subtitle, size=9.8, color=MID, after=5)
    return p


def page_start(doc, section_title, kicker=None):
    doc.add_page_break()
    if kicker:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(kicker.upper())
        set_run_font(r, size=8.5, bold=True, color=TEAL)
    add_heading(doc, section_title, 1)


def add_callout(doc, label, text, *, fill=PALE, label_color=TEAL):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Cm(17.6)
    cell = table.cell(0, 0)
    shade(cell, fill)
    cell_margins(cell, top=130, start=150, bottom=130, end=150)
    set_cell_border(cell, color=LINE, size="7")
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(label)
    set_run_font(r, size=10, bold=True, color=label_color)
    p = cell.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.08
    r = p.add_run(text)
    set_run_font(r, size=10, color=INK)
    doc.add_paragraph().paragraph_format.space_after = Pt(1)


def add_page_field(paragraph):
    run = paragraph.add_run()
    fld_begin = OxmlElement("w:fldChar")
    fld_begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    fld_end = OxmlElement("w:fldChar")
    fld_end.set(qn("w:fldCharType"), "end")
    run._r.append(fld_begin)
    run._r.append(instr)
    run._r.append(fld_end)
    set_run_font(run, size=8.5, color=MID)


def setup_document():
    doc = Document()
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(1.75)
    section.bottom_margin = Cm(1.65)
    section.left_margin = Cm(1.7)
    section.right_margin = Cm(1.7)
    section.header_distance = Cm(0.75)
    section.footer_distance = Cm(0.7)
    styles = doc.styles
    for name in ("Normal", "List Bullet", "List Bullet 2"):
        style = styles[name]
        style.font.name = FONT
        style.font.size = Pt(10.5)
        style.font.color.rgb = RGBColor.from_string(INK)
        style._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    styles["Normal"].paragraph_format.space_after = Pt(5)
    styles["Normal"].paragraph_format.line_spacing = 1.12
    for name, size, color in (("Title", 24, NAVY), ("Subtitle", 12, TEAL), ("Heading 1", 15.5, NAVY), ("Heading 2", 11.5, TEAL)):
        style = styles[name]
        style.font.name = FONT
        style.font.size = Pt(size)
        style.font.bold = name != "Subtitle"
        style.font.color.rgb = RGBColor.from_string(color)
        style._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
        style.paragraph_format.keep_with_next = True
    # The built-in Title style carries a paragraph border in some Word defaults.
    # Remove that inherited rule so the cover title has no unintended underline.
    title_ppr = styles["Title"]._element.get_or_add_pPr()
    title_border = title_ppr.find(qn("w:pBdr"))
    if title_border is not None:
        title_ppr.remove(title_border)
    header = section.header.paragraphs[0]
    header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    header.paragraph_format.space_after = Pt(0)
    r = header.add_run("課程切合性檢討分析  |  SAMPLE / SYNTHETIC")
    set_run_font(r, size=8.2, color=MID)
    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer.paragraph_format.space_before = Pt(0)
    r = footer.add_run("示範資料不代表協會實績、核准或實際開課    ·    第 ")
    set_run_font(r, size=8.2, color=MID)
    add_page_field(footer)
    r = footer.add_run(" 頁")
    set_run_font(r, size=8.2, color=MID)
    return doc


CHECKS = [
    {"id":"L1","dimension":"學員","control":"受訓角色與課程目標相符","criterion":"目標任務能對應 G1-G4；對象按任務需要界定，不以會員身分或未證明條件推定。","before":"符合","evidence":"合成課程計畫列出四個可觀察任務目標，與規劃對象的志工服務紀錄、交接及界線情境相連。","action":"維持任務導向說明；實際招生前須以正式需求及授權版本重核。","after":"符合","strength":"SAMPLE/DERIVED"},
    {"id":"L2","dimension":"學員","control":"入班條件與公平遴選規則可操作","criterion":"條件可觀察、可重複判定；例外及補充支持有記錄路徑。","before":"部分符合","evidence":"合成草案描述 12 個規劃名額，但未把先備條件、例外處理及不足資料的補件方式寫成同一規則。","action":"新增三項任務自評、必要先備說明、無先備者支持路徑及不採個資推斷的規則。","after":"符合","strength":"SYNTHETIC"},
    {"id":"L3","dimension":"學員","control":"支持需求與隱私採最小必要資料","criterion":"只問完成學習所需的調整；說明用途、保管及不回答的替代方式。","before":"符合","evidence":"示範表只記錄學習支持選項與後續聯絡路徑，不要求健康診斷或不必要個人資料。","action":"保留資料最小化欄位；REAL 使用前依協會核定個資規則覆核。","after":"符合","strength":"SYNTHETIC"},
    {"id":"M1","dimension":"教材","control":"教材內容與 G1-G4 目標相連","criterion":"每個單元教材都可回指一項目標、練習與評量。","before":"符合","evidence":"四單元對應界線判斷、對話、紀錄交接及整合演練；計畫總教學時間 360 分鐘。","action":"維持目標—教材—練習—評量對照，版本改動時重新檢視。","after":"符合","strength":"SAMPLE/DERIVED"},
    {"id":"M2","dimension":"教材","control":"來源、版本與修訂可追溯","criterion":"每份教材標明來源、版次、檢核者、修訂日期及下一次覆核條件。","before":"部分符合","evidence":"示範素材組 SYN-MAT-G1-G4 v1.0 有內容名稱，但尚未在每件素材上呈現來源及版次欄。","action":"增加素材索引、版次、來源定位、變更理由與覆核欄，禁止未核來源當正式規則。","after":"符合","strength":"SYNTHETIC"},
    {"id":"M3","dimension":"教材","control":"快速參考卡易讀且能引導正確處理","criterion":"關鍵詞、下一步、責任角色及期限足以讓不同讀者一致操作；示範理解測試須全數答對關鍵步驟。","before":"部分符合","evidence":"6 個合成使用者情境中 4 個正確找出未知來源處理步驟；仍有文字容易把『詢問講師』誤當來源查證。","action":"重寫卡片並重測；第一輪修訂後 6 個情境中 5 個答對，1 個仍誤讀，列為未結。","after":"部分符合","strength":"SYNTHETIC / OPEN"},
    {"id":"T1","dimension":"師資","control":"師資需求對應教學任務","criterion":"先定義需教授的任務能力，再核對候選人的可查證能力與授課範圍。","before":"符合","evidence":"示範師資需求矩陣把 G1-G4 對應至情境引導、紀錄示範及評量回饋，不以職稱取代能力核對。","action":"REAL 遴選時逐項查驗可合法取得的履歷、作品或試教資料。","after":"符合","strength":"SYNTHETIC; no real instructor"},
    {"id":"T2","dimension":"師資","control":"授課範圍與資料界線清楚","criterion":"教學者不得超出可查證專業或替學員作正式法律、醫療或行政認定。","before":"符合","evidence":"示範角色只負責課程引導；未知來源回到指定責任角色核實，不給未經支持的專業結論。","action":"保留越權情境與轉介判準；實際聘任及核准只接受真實原件。","after":"符合","strength":"SYNTHETIC role only"},
    {"id":"T3","dimension":"師資","control":"評量錨點可一致套用","criterion":"評量規準有可觀察行為與補練判準；同一樣例能按同一錨點重判。","before":"符合","evidence":"六個合成作答樣例均可對照相同四級行為錨點與補練規則；此為桌上校準示範。","action":"保留校準表；正式課程須留下真實評量者校準及版本紀錄。","after":"符合","strength":"SYNTHETIC"},
    {"id":"P1","dimension":"教學方法","control":"方法與行為目標一致","criterion":"知識、示範、練習、回饋按目標任務配置，不能只用講授檢核操作能力。","before":"符合","evidence":"G1-G4 均配置情境辨識、示範、練習或整合演練與觀察判準。","action":"依下一次檢討結果再核對目標和評量，保留方法變更理由。","after":"符合","strength":"SAMPLE/DERIVED"},
    {"id":"P2","dimension":"教學方法","control":"高風險操作有足夠練習與再教學","criterion":"示範時間表與練習份量符合表現目標；未達判準者有補練及重評。","before":"部分符合","evidence":"合成比較基準 G1 為 35/20/35（說明/示範/引導練習），操作練習比例未達本示範設定的 50% 最低值。","action":"採方案 A 的 20/20/50；G1 仍 90 分鐘，練習 45 分鐘；未達題目者依同一錨點補練。","after":"符合","strength":"SYNTHETIC; local design rule, not official standard"},
    {"id":"P3","dimension":"教學方法","control":"評量時點、門檻與回饋路徑完整","criterion":"明列何時評、用何量尺、合格門檻、缺答處理及未達補練方式。","before":"符合","evidence":"合成計畫為 G1 設五情境至少答對四題且無越權承諾；缺答不計為通過，未達者補練後重評。","action":"正式使用前核對核定課程版次；樣例答案不得代替實際評量。","after":"符合","strength":"SYNTHETIC"},
    {"id":"F1","dimension":"訓練設施","control":"環境支援分組練習及可達性","criterion":"空間配置、座位、動線及學習材料可支援預定活動；實際限制需留下調整。","before":"符合","evidence":"合成場地 SYN-VENUE-A 配置 12 席、3 組桌面演練與無障礙動線；屬合成平面檢核，不代表真實場地。","action":"實際使用前依地址及場勘紀錄重做檢查；本報告不代替安全/保險原件。","after":"符合","strength":"SYNTHETIC venue"},
    {"id":"F2","dimension":"訓練設施","control":"設備功能符合教學方法","criterion":"投影、聲音、電源、紙本備援及小組材料均按課程情境測試。","before":"符合","evidence":"示範清單逐項核對投影、音訊、電源及紙本備援，測試均記為可用；沒有真實設備序號。","action":"實際開課前重新測試並記錄設備識別與異常處理。","after":"符合","strength":"SYNTHETIC equipment"},
    {"id":"F3","dimension":"訓練設施","control":"維護與異常紀錄能回到設備/環境","criterion":"日常檢點有日期、項目、結果、處理、覆核與下次期限；不可替代法定證明。","before":"符合","evidence":"示範維護表包含檢查日期、結果、處理及下次檢查欄；此為流程樣例，非實際維護紀錄。","action":"REAL 使用時填真實設備/場所、原件位置與權責人；法定文件另按其原件要求。","after":"符合","strength":"SYNTHETIC only"},
]


def collect_sources():
    raw_lines = BLUEPRINT_PATH.read_bytes().splitlines()
    row = None
    row_no = None
    row_raw = None
    for i, line in enumerate(raw_lines, 1):
        try:
            item = json.loads(line.decode("utf-8-sig"))
        except Exception:
            continue
        if str(item.get("deliverable_id")) == "0053":
            row, row_no, row_raw = item, i, line
            break
    if row is None:
        raise RuntimeError("0053 unique blueprint row is missing")
    if row.get("requirement_id") != "I12-E01":
        raise RuntimeError(f"Unexpected requirement mapping: {row.get('requirement_id')}")
    with CROSSWALK_PATH.open(encoding="utf-8-sig", newline="") as stream:
        crosswalk = list(csv.DictReader(stream))
    cross = [r for r in crosswalk if r.get("requirement_id") == "I12-E01"]
    if len(cross) != 1 or cross[0].get("deliverable_ids") != "0053":
        raise RuntimeError("142 deliverable crosswalk does not map I12-E01 uniquely to 0053")
    official_bytes = OFFICIAL_PDF.read_bytes()
    official_pages = PdfReader(str(OFFICIAL_PDF)).pages
    if len(official_pages) < 4:
        raise RuntimeError("Official evidence table has no page 4")
    official_page4 = official_pages[3].extract_text() or ""
    compact_page4 = re.sub(r"\s+", "", official_page4)
    for phrase in ("近年針對訓練課程", "遴選學員", "教材", "師資", "教學方法", "訓練設施", "持續改善"):
        if phrase not in compact_page4:
            raise RuntimeError(f"Official page 4 exact text check failed: {phrase}")
    for source in (DOC_0033, DOC_0052, SOURCE_PAGE_IMAGE):
        if not source.exists():
            raise RuntimeError(f"Required linked source is missing: {source}")
    source_info = {
        "deliverable_id": "0053",
        "requirement_id": "I12-E01",
        "official_checkbox_sequence": "056",
        "official_source_page": 4,
        "official_requirement_text": OFFICIAL_REQUIREMENT,
        "official_pdf_sha256": sha256(official_bytes),
        "blueprint_path": str(BLUEPRINT_PATH),
        "blueprint_line": row_no,
        "blueprint_row_sha256": sha256(row_raw),
        "blueprint_file_sha256": sha256(BLUEPRINT_PATH.read_bytes()),
        "blueprint_row": row,
        "crosswalk_path": str(CROSSWALK_PATH),
        "crosswalk_sha256": sha256(CROSSWALK_PATH.read_bytes()),
        "crosswalk_row": cross[0],
        "doc_0033_sha256": sha256(DOC_0033.read_bytes()),
        "doc_0052_sha256": sha256(DOC_0052.read_bytes()),
        "doc_0052_size": DOC_0052.stat().st_size,
        "official_page4_image_sha256": sha256(SOURCE_PAGE_IMAGE.read_bytes()),
        "official_page4_text": official_page4,
    }
    (INPUTS / "UNIQUE_BLUEPRINT_0053.json").write_text(
        json.dumps({k: v for k, v in source_info.items() if k != "official_page4_text"}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    shutil.copy2(OFFICIAL_PDF, INPUTS / "official_checklist_source.pdf")
    shutil.copy2(SOURCE_PAGE_IMAGE, INPUTS / "official_evidence_table_page4.png")
    (INPUTS / "official_evidence_table_page4.txt").write_text(official_page4, encoding="utf-8")
    map_text = f"""# 0053 R01 來源與範圍對照

## 唯一需求對應

- DOCX 編號：0053（142 份文件序列）
- Unique Blueprint：I12-E01，分析／評估報告
- 官方方框流水號：056（官方 157 格清單；不是 DOCX 編號）
- 官方查核佐證文件資料表：第 4 頁，PDF SHA-256 `{source_info['official_pdf_sha256']}`
- 官方原文：{OFFICIAL_REQUIREMENT}
- Unique Blueprint：`BLUEPRINT_CURRENT.jsonl` 第 {row_no} 行，整檔 SHA-256 `{source_info['blueprint_file_sha256']}`；該列 SHA-256 `{source_info['blueprint_row_sha256']}`。
- 142 份 crosswalk：`I12-E01 -> 0053`，檔案 SHA-256 `{source_info['crosswalk_sha256']}`。

## 可用的課程計畫來源與界線

- DOCX 0052 R01（I11-E04）SHA-256 `{source_info['doc_0052_sha256']}`，64,310 bytes；只取其合成課程計畫 `SYN-0033-PLAN-01` 的課程名稱、G1-G4 目標、90+90+120+60=360 分鐘與方案 A 的 20/20/50 G1 分段作為檢討對象。該候選清楚記載未核定、未發布、未開課；本報告不把它改述成 REAL 課程。
- DOCX 0033 R03（I07-E01）SHA-256 `{source_info['doc_0033_sha256']}`；僅作同一 SAMPLE 情境的上游需求索引，不複製問卷正文，也不把合成答案當真人調查。
- 本報告另造的 15 項適配檢核、6 個合成可讀性情境、檢討日、角色碼、狀態與修訂結果，全標為 SAMPLE/SYNTHETIC，均登錄於替換清冊。
- 本包沒有經核驗的協會 REAL 課程、招生/學員、教材核定、師資聘任、場地/設備維護或訓練執行原件。相應 REAL 狀態為 UNKNOWN；不得以本示範宣稱已執行、已核准或已有成效。

## 負向鄰項

- 0052 / I11-E04：以學員與結訓學員意見規劃或修訂課程；本件只引用合成規劃草案作分析輸入，不代替回饋流程或修訂計畫。
- 0054 / I12-E02：依遴選標準與流程遴選學員、教材推薦/審查；本件不提供任何真實個別遴選、委員會通過或核准原件。
- 官方流水號 059 / I12-E04：設備安檢或場地投保證明；本件不代製、不替代任何第三方證明。

## 證據層級

1. 官方要求：直接核對官方 PDF 第 4 頁及當前品質契約的流水號 056。
2. 可追溯輸入：0052 R01、0033 R03 都是 SAMPLE 候選，SHA 僅證明位元組身分，不提升其資料為 REAL。
3. 本報告示範結果：只證明此分析方法的內部算例一致；不是協會辦訓、批准或品質績效證據。
"""
    (INPUTS / "SOURCE_MAP_0053_R01.md").write_text(map_text, encoding="utf-8")
    return source_info


def add_sources_page(doc, src):
    page_start(doc, "資料來源、案例與證據強度", "02 來源與樣本")
    rows = [
        ("官方查核表", "第 4 頁；PDF SHA-256 " + src["official_pdf_sha256"][:16] + "…", "核對 I12-E01 原文與五個檢討面向；不證明協會有實際課程。"),
        ("157 格清單", "流水號 056；I12 執行項", "確認官方格號。不得把 056 當 DOCX 編號。"),
        ("142 份 crosswalk", "I12-E01 → DOCX 0053；檔案 SHA-256 " + src["crosswalk_sha256"][:16] + "…", "確認生產序列與需求對應。"),
        ("Unique Blueprint", "0053 第 " + str(src["blueprint_line"]) + " 行；列 SHA-256 " + src["blueprint_row_sha256"][:16] + "…", "決定分析報告文類、必備分析/追溯表及驗收條件。"),
        ("0052 R01", "I11-E04；SHA-256 " + src["doc_0052_sha256"][:16] + "…", "僅供同一合成課程計畫作檢討輸入；其計畫仍未核定或開課。"),
        ("0033 R03", "I07-E01；SHA-256 " + src["doc_0033_sha256"][:16] + "…", "僅為合成需求來源索引；不把合成回答轉成 REAL 調查。"),
    ]
    add_table(doc, ["來源", "精確定位", "可支持的結論與限制"], rows, [3.0, 5.2, 9.4], font_size=9.0, first_col_bold=True)
    add_heading(doc, "案例範圍", 2)
    add_body(doc, "SYN-0033-PLAN-01 是跨文件共用的合成教學案例，課名為「志工服務紀錄、交接與工作界線實務」。0052 R01 的四單元為 G1 90 分、G2 90 分、G3 120 分、G4 60 分，合計 360 教學分鐘；方案 A 將 G1 分段由合成比較基準 35/20/35 改為 20/20/50。這些數字是計畫草案示例，不代表實際招生、教學或核准。")
    add_heading(doc, "示範觀察期間", 2)
    add_table(doc, ["示範日期", "記錄", "資料性質"], [
        ("2026-10-03", "基線檢核：五面向共 15 個適配控制項。", "SAMPLE；非實際檢討會議。"),
        ("2026-10-08", "修訂後桌上複核；抽查快速參考卡 6 個情境。", "SYNTHETIC；非學員或場地實測。"),
        ("未設定 REAL 日期", "真正課程日期、核定版次及授權者仍待原件核實。", "UNKNOWN；不可推定已開課。"),
    ], [2.8, 8.2, 6.6], font_size=9.2, first_col_bold=True)
    add_callout(doc, "證據強度", "官方原文與方框定位已直接核實；跨文件課程輸入與本報告的檢核結果均為 SAMPLE/SYNTHETIC。此處不提供協會 REAL 執行或成效證明。", fill="FFF3E2", label_color=RED)


def add_check_rows(doc, subset, page_title, kicker):
    page_start(doc, page_title, kicker)
    rows = []
    for c in subset:
        rows.append((c["id"] + "\n" + c["control"], c["criterion"], c["evidence"], c["before"], c["action"], c["after"]))
    add_table(doc, ["控制項", "判定準則", "基線示範證據", "基線", "修訂／覆核", "複核"], rows,
              [2.15, 3.35, 3.45, 1.35, 4.45, 1.45], font_size=8.55, first_col_bold=True, status_col=5)
    add_body(doc, "狀態只計本報告的合成檢核；REAL 條件未核實時不得沿用此狀態。部分符合及 UNKNOWN 均不計入符合項目。", size=9.0, color=MID, after=1)


def add_replacement_register(candidate_sha, page_map):
    rows = []
    def push(fid, value, source, locator, page, real_replacement, owner="訓練承辦角色", status="SYNTHETIC—待 REAL 替換"):
        rows.append({
            "fact_id": fid,
            "value_in_candidate": value,
            "fact_type": "SAMPLE/SYNTHETIC",
            "source_or_formula": source,
            "candidate_sha256": candidate_sha,
            "body_locator": locator,
            "rendered_page": page,
            "real_replacement_source": real_replacement,
            "replacement_responsible_role": owner,
            "status": status,
        })
    for i, c in enumerate(CHECKS, 1):
        page = page_map.get(c["id"], page_map.get(c["dimension"], 6 if c["dimension"] in ("學員", "教材") else 7))
        source = "本報告完整合成示範設計；不得當成 REAL 記錄。"
        if c["id"] == "L1" or c["id"] == "M1":
            source = "DOCX 0052 R01 合成課程計畫；本報告只引用其目標/單元，不提升資料身分。"
        if c["id"] == "P2":
            source = "0052 R01 Table 19/21 合成方案 A；90 分鐘 G1 的 20/20/50 提案。"
        if c["id"] == "M3":
            source = "本報告合成可讀性情境：基線 4/6，修訂複核 5/6。"
        push(f"SYN-0053-F{i:03d}", f"{c['id']}｜基線 {c['before']}；複核 {c['after']}。{c['evidence']}", source,
             f"五面向檢核表；{c['id']} 列", page,
             "該課程實際核定版本、原始檢核表、教材/師資/場地原件及核准權限紀錄。")
    extras = [
        ("案例識別", "SYN-0033-PLAN-01", "0052 R01 的合成案例索引", "第 3 頁案例範圍", 3, " REAL 課程/班次識別及核定課程計畫原件。"),
        ("示範課名", "志工服務紀錄、交接與工作界線實務", "0052 R01 合成課程計畫", "第 1、3 頁", 3, "REAL 課程名稱與核定版次。"),
        ("規劃名額", "12 個規劃名額", "0052 R01 合成課程假設", "第 3、6 頁", 3, "實際核定招生名額、依據與期間。"),
        ("G1 教學分鐘", "90 分鐘", "0052 R01 合成課程表", "第 3、7、9-10 頁", 3, "REAL 課程版次、課表及授權核定。"),
        ("G2 教學分鐘", "90 分鐘", "0052 R01 合成課程表", "第 3 頁", 3, "REAL 課程版次與課表。"),
        ("G3 教學分鐘", "120 分鐘", "0052 R01 合成課程表", "第 3 頁", 3, "REAL 課程版次與課表。"),
        ("G4 教學分鐘", "60 分鐘", "0052 R01 合成課程表", "第 3 頁", 3, "REAL 課程版次與課表。"),
        ("總時數", "90+90+120+60=360 分鐘", "逐項相加；休息及行政不計", "第 3、6 頁", 3, "核定課表與實際執行紀錄。"),
        ("基線日期", "2026-10-03", "本報告合成示範設定", "第 3、11 頁", 3, "REAL 檢討日期、原始紀錄與參與者授權。"),
        ("複核日期", "2026-10-08", "本報告合成示範設定", "第 3、11 頁", 3, "REAL 複核日期及紀錄。"),
        ("基線符合數", "11/15=73.3%", "CHECKS 基線狀態逐列重算", "第 1、10、13 頁", 10, "REAL 原始 15 項檢核及覆核結果。"),
        ("複核符合數", "14/15=93.3%", "CHECKS 複核狀態逐列重算", "第 1、10、13 頁", 10, "REAL 修訂版與複核原件。"),
        ("差異", "+3/15=+20.0 個百分點", "93.333…%-73.333…%=20.0pp", "第 10、13 頁", 10, "REAL 前後同口徑資料與計算底稿。"),
        ("可讀性情境母數", "6 個合成情境", "SYN-0053-QA-01 至 QA-06", "第 5、6、9 頁", 5, "REAL 使用者測試原始資料、同意與匿名化方式。"),
        ("可讀性基線結果", "4/6 正確=66.7%", "六個合成情境逐列統計", "第 5、6、9 頁", 9, "REAL 原始作答與評分準則。"),
        ("可讀性複核結果", "5/6 正確=83.3%；1/6仍誤讀", "六個合成情境逐列統計", "第 5-6、9、13 頁", 9, "REAL 修訂後使用者測試資料。"),
        ("G1 基線方法比例", "35/20/35（說明/示範/練習）", "0052 R01 合成比較基準", "第 5、7、9-10 頁", 10, "實際核定教案與授課分鐘紀錄。"),
        ("G1 提案方法比例", "20/20/50（說明/示範/練習）", "0052 R01 合成方案 A", "第 5、7、9-10 頁", 10, "授權核定的教案及實際教學觀察。"),
        ("合成角色", "SYN-COORD、SYN-REVIEWER、SYN-AUTH", "無真人對應的角色代碼", "第 14 頁", 14, "真實授權職務、代理規則及人員核准原件。"),
        ("合成場地", "SYN-VENUE-A；12 席、3 組桌面演練", "本報告假設場地檢核", "第 7 頁", 7, "真實地址、場勘、設備清冊及維護紀錄。"),
        ("合成材料版次", "SYN-MAT-G1-G4 v1.0", "本報告示範版次標記", "第 6 頁", 6, "正式教材原件、來源授權與版本紀錄。"),
        ("合成內部門檻", "描述性符合率≥90%；關鍵項不得未結", "本報告的示範判讀規則，非官方門檻", "第 4 頁", 4, "協會正式核定之內部品質標準及權限。"),
        ("最終合成判定", "14/15；M3 未結；不得 REAL 開課", "本報告檢核結果與 REAL 邊界", "第 1、9、13 頁", 1, "REAL 核准決議、課程原件、場地/師資/教材證據。"),
    ]
    for i, (label, value, source, locator, page, real_source) in enumerate(extras, len(CHECKS)+1):
        push(f"SYN-0053-F{i:03d}", f"{label}：{value}", source, locator, page, real_source)
    csv_path = PACKAGE / "SYNTHETIC_REPLACEMENT_REGISTER_0053_R01.csv"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    return csv_path, rows


def build_document(src):
    doc = setup_document()

    # Page 1: reader-facing executive summary.
    p = doc.add_paragraph(style="Title")
    p.paragraph_format.space_before = Pt(28)
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run("訓練課程切合性檢討與調整分析報告")
    set_run_font(r, size=23, bold=True, color=NAVY)
    p = doc.add_paragraph(style="Subtitle")
    p.paragraph_format.space_after = Pt(19)
    r = p.add_run("學員、教材、師資、教學方法與訓練設施五面向")
    set_run_font(r, size=12, color=TEAL)
    add_callout(doc, "SAMPLE / SYNTHETIC 完整示範", "本報告示範如何以 15 項控制檢核課程切合性、記錄調整並重算結果。所有日期、角色、數字、素材、使用情境及判定都是合成資料，不表示原始點協會曾招生、聘師、核准、開課或取得成效。", fill=PALE)
    add_table(doc, ["讀者／用途", "本次示範的明確結果"], [
        ("主管與訓練承辦人：在核定前檢視課程與對象、教材、師資、方法及環境是否相配；把缺口交給責任角色修正。", "基線 11/15=73.3%；修訂後 14/15=93.3%。1 項教材可讀性問題仍未關閉。"),
        ("評核閱讀者：查看原始要求如何連到資料、計算、結論及追蹤。", "符合率是本示範 15 個控制項的描述值，不是學員通過率、課程成效或官方評分。"),
        ("可直接採取的下一步：修訂快速參考卡，再測一次；取得真實課程、授權及場地原件後才可作 REAL 判定。", "目前 REAL 狀態：UNKNOWN。未核定、未發布、未實際開課的任何結論都不能由本示範改寫。"),
    ], [8.7, 8.9], font_size=9.3, first_col_bold=True)
    add_body(doc, "官方對應：訓練機構版查核佐證表第 4 頁，指標 12 的方框 056。正文可獨立辨認為五面向課程適配檢討，不代替學員回饋課程修訂計畫、個別遴選/教材審查原件或場地保險證明。", size=9.5, color=MID)

    # Page 2: exact requirement and scope boundaries.
    page_start(doc, "官方要求與本報告的決策範圍", "01 需求定位")
    add_callout(doc, "官方原文｜I12-E01｜流水號 056", OFFICIAL_REQUIREMENT, fill=PALE)
    add_table(doc, ["核對欄位", "本件對應"], [
        ("DOCX 序列", "0053（142 份文件 crosswalk）"),
        ("Unique Blueprint", "I12-E01；分析／評估報告"),
        ("官方流水號", "056；取自官方 157 格清單；與 DOCX 0053 為不同編號。"),
        ("官方來源", "《TTQS 查核佐證文件資料表－訓練機構版》第 4 頁；精確文字見來源附錄。"),
        ("本件要回答", "在特定課程計畫下，五面向各有何檢核資料、差距、修正和後續追蹤？目前是否能證明實際執行符合核定版？"),
    ], [4.0, 13.6], font_size=9.4, first_col_bold=True)
    add_heading(doc, "相鄰需求的分工", 2)
    add_table(doc, ["文件／要求", "它直接負責的工作", "本件界線"], [
        ("0052 / I11-E04", "依學員及結訓學員意見規劃或修訂課程並留完整流程。", "只把其 SAMPLE 課程計畫當分析輸入，不重貼問卷、不宣稱回饋或開課為 REAL。"),
        ("0053 / I12-E01", "分析課程切合性；檢討學員、教材、師資、方法與設施並持續改善。", "本報告的唯一直接要求。"),
        ("0054 / I12-E02", "依遴選標準和流程選擇學員，處理教材推薦/審查及其正式核定。", "不代替真實個別遴選、委員會決議、聘書或教材核准原件。"),
        ("0056 / I12-E04", "設備安檢或場地投保證明。", "不製作、不仿造、不替代任何第三方安檢或保險原件。"),
    ], [3.0, 7.1, 7.5], font_size=8.9, first_col_bold=True)
    add_body(doc, "判讀問題：「實際執行是否符合核定版本？」目前答案為 UNKNOWN：本包沒有可核實的 REAL 核定版本或實際執行原件。示範中的 P0-SYN 是案例草稿，不得當作協會核定版。", bold_lead="判讀問題：", color=RED, size=9.5)

    # Page 3: sources, synthetic case, timeline.
    add_sources_page(doc, src)

    # Page 4: workflow and calculations rules.
    page_start(doc, "檢討方法與判定規則", "03 方法")
    add_table(doc, ["步驟", "承辦人要做什麼", "若資料不足"], [
        ("1｜定版次", "列出課程目標、使用時點、版本及核定來源。", "沒有核定原件就標 UNKNOWN，不自行補成已核准。"),
        ("2｜定檢核範圍", "按學員、教材、師資、教學方法、設施各列 3 項可觀察控制。", "不能只寫『整體適切』；找不到證據的控制不計符合。"),
        ("3｜留來源定位", "逐項寫出文件、版本、頁/表/欄、檢查人與日期。", "口頭印象不能代替可回查來源；缺資料列補件責任。"),
        ("4｜判定差距", "對照準則記符合、部分符合或未知；說明判斷原因。", "部分符合/UNKNOWN 不計入分子；只有有據 N/A 才可排除分母。"),
        ("5｜分析與調整", "找出原因，指定動作、負責角色、期限與複核方式。", "關鍵權限、個資、安全或第三方文件未核實時保留 Human Gate。"),
        ("6｜複核並留版", "同一口徑檢查修訂版；保存前後差異與計算底稿。", "版次未綁定或資料非同源，不得說已改善。"),
        ("7｜分開 REAL 與示範", "完整標明 SAMPLE/SYNTHETIC；逐事實登錄替換清冊。", "合成分數永遠不能替代 REAL 原件或正式核准。"),
    ], [2.3, 7.4, 7.9], font_size=8.7, first_col_bold=True)
    add_heading(doc, "符合率與本示範判定", 2)
    add_body(doc, "符合率 = 符合的適用檢核項 ÷ 本期應檢核項 × 100%。本例 15 項全數適用；部分符合及未驗證不算符合；沒有 N/A。此公式只描述五面向檢核項，不表示學員、課程或協會績效。")
    add_callout(doc, "內部示範門檻，不是官方標準", "為展示決策規則，本例暫採整體符合率至少 90% 且關鍵控制無未結項；即使達到百分比，教材關鍵步驟仍誤讀時，仍不能 REAL 發布。此門檻須由協會正式權責者另行核定，未核定前只供本合成算例使用。", fill="FFF3E2", label_color=RED)

    # Page 5: data dictionary.
    page_start(doc, "資料字典與分母", "04 資料定義")
    add_table(doc, ["欄位／指標", "操作定義", "分母／單位", "來源與限制"], [
        ("檢核控制項", "五面向各 3 項，合計 15 個可觀察要求。", "項；本例 15 項全適用。", "本報告樣例，不代表官方條文將 15 項定為評分項。"),
        ("狀態：符合", "有足以定位的示範證據且達到該列準則。", "1 項。", "只描述 SYNTHETIC 情境；REAL 原件仍須另外核對。"),
        ("狀態：部分符合", "已有部分支持，但存在缺口、誤讀或未完成複核。", "不進分子。", "本例 M3 仍為部分符合。"),
        ("狀態：UNKNOWN", "缺少可核實資料，不能判定符合或不符合。", "不進分子；不得以 0 分代替。", "REAL 核定版、開課、人員及場地均 UNKNOWN。"),
        ("符合率", "符合項數除以本期應檢項數。", "項目比例，非人數比例。", "列到小數一位；中間計算保留精確分數。"),
        ("快速卡可讀性", "合成情境讀者是否能指出『標示未知→責任角色→期限』。", "6 個合成情境。", "不是學員問卷，也不是統計抽樣；不推論人口。"),
        ("方法分段", "G1 教學時間按說明／示範／引導練習拆分。", "分鐘比例。", "90 分鐘不變；35/20/35 改提 20/20/50，來自 0052 R01 SAMPLE 計畫。"),
        ("改善差異", "複核符合率減基線符合率。", "百分點（pp）。", "只比較兩個合成檢查點；不是長期趨勢或實績。"),
    ], [3.0, 5.3, 3.1, 6.2], font_size=8.8, first_col_bold=True)
    add_heading(doc, "六個合成易讀性情境的計數規則", 2)
    add_body(doc, "讀者須在卡片上找到三個動作：明示 UNKNOWN、不推測事實；交給指定角色查來源；留下下一步與期限。三者全指出才記 1，任一缺漏記 0。基線 4 個情境全對、2 個未全對；修訂複核 5 個全對、1 個未全對。無真人參與，情境 ID 僅供本報告重算。")

    # Page 6: learner and materials checks.
    add_check_rows(doc, CHECKS[:6], "學員與教材適配檢核", "05 五面向檢核 A")
    add_body(doc, "學員檢核以任務需求、可操作入班條件與最小必要支持資料為準；個別名單與正式錄取決定屬 0054 的 REAL 原件。教材檢核看目標對應、來源版次及易讀性；完成合成檢討仍不能代替正式教材審查。", size=9.2, color=MID)

    # Page 7: instructor, methods, facilities.
    add_check_rows(doc, CHECKS[6:], "師資、方法與設施適配檢核", "06 五面向檢核 B")
    add_body(doc, "師資項目只展示能力要求與校準方式，不填真人姓名、資歷或聘任結論。設施項目只展示場地與設備的課程適配檢點；法定安檢與投保文件仍須取自合法原件。", size=9.2, color=MID)

    # Page 8: exact recheck and unresolved usability item.
    page_start(doc, "修訂記錄與未結教材問題", "07 前後複核")
    add_table(doc, ["項目", "基線缺口", "示範修訂", "複核結果", "判定"], [
        ("L2 入班條件", "條件與例外支持未寫成可重複判斷規則。", "加入任務自評、先備說明、補充支持及資料不足時的補件流程。", "同一 15 項表中重新對照，控制內容完整。", "SAMPLE 符合"),
        ("M2 素材追溯", "素材沒有統一列來源、版次、覆核者及變更理由。", "建立素材索引和變更欄；無來源項先標 UNKNOWN。", "本例資料列可追溯到示範版次與來源類別。", "SAMPLE 符合"),
        ("P2 練習份量", "G1 基線 35/20/35，練習不足以支撐操作目標。", "依 0052 方案 A 提案改為 20/20/50，G1 仍 90 分鐘。", "90×20%=18 說明、90×20%=18 示範、90×50%=45 練習；三段合計 81 分鐘，餘 9 分鐘為轉場/回饋安排，須在 REAL 教案確認。", "SAMPLE 符合；實際分鐘 UNKNOWN"),
        ("M3 快速卡可讀性", "4/6 情境讀者找到正確處理步驟。", "增補未知來源的責任角色與期限提示。", "5/6=83.3%；仍有 1/6 把詢問講師當作來源查證。", "部分符合；不得 REAL 發布"),
    ], [2.4, 3.5, 4.1, 5.0, 2.6], font_size=8.55, first_col_bold=True, status_col=4)
    add_callout(doc, "數字核對提醒", "0052 R01 的 20/20/50 是對原 90 分鐘 G1 的分段比例。三段教學活動為 18+18+45=81 分鐘；尚有 9 分鐘屬轉場/回饋的待確認安排，不能把比例表誤寫成三段已合計 90 分鐘。實際核定分鐘仍 UNKNOWN。", fill="FFF3E2", label_color=RED)
    add_heading(doc, "六個合成情境的明細", 2)
    persona_rows = [
        ("SYN-QA-01", "全數找出標示未知、責任角色及期限。", "1", "1"),
        ("SYN-QA-02", "全數找出正確來源查證動作。", "1", "1"),
        ("SYN-QA-03", "全數找出不得推測的限制。", "1", "1"),
        ("SYN-QA-04", "全數找出下一步交接欄。", "1", "1"),
        ("SYN-QA-05", "基線少指出責任角色；修訂後找出完整路徑。", "0", "1"),
        ("SYN-QA-06", "仍把詢問講師當成來源查證，沒有留下期限。", "0", "0"),
    ]
    add_table(doc, ["合成情境代碼", "測試點", "基線", "複核"], persona_rows, [3.0, 9.2, 2.5, 2.9], font_size=9.0, first_col_bold=True)

    # Page 9: calculations.
    page_start(doc, "符合率的逐步重算", "08 計算")
    calc_rows = []
    before = {"學員":2,"教材":1,"師資":3,"教學方法":2,"訓練設施":3}
    after = {"學員":3,"教材":2,"師資":3,"教學方法":3,"訓練設施":3}
    for dim in before:
        b, a = before[dim], after[dim]
        calc_rows.append((dim, f"{b}/3", f"{b}/3 × 100 = {b/3*100:.1f}%", f"{a}/3", f"{a}/3 × 100 = {a/3*100:.1f}%"))
    calc_rows.append(("合計", "11/15", "11 ÷ 15 × 100 = 73.333…% → 73.3%", "14/15", "14 ÷ 15 × 100 = 93.333…% → 93.3%"))
    add_table(doc, ["面向", "基線符合/應檢", "基線計算", "複核符合/應檢", "複核計算"], calc_rows, [2.4, 2.5, 4.0, 2.6, 6.1], font_size=8.9, first_col_bold=True)
    add_heading(doc, "總體變化", 2)
    add_table(doc, ["步驟", "計算", "結果"], [
        ("基線", "11 ÷ 15 × 100", "73.333…%，顯示 73.3%。"),
        ("複核", "14 ÷ 15 × 100", "93.333…%，顯示 93.3%。"),
        ("增加項數", "14−11", "增加 3 項符合。"),
        ("百分點差", "(14/15−11/15) × 100", "+20.0 個百分點；兩次均為同一 15 項分母。"),
        ("剩餘差距", "1 個部分符合 ÷ 15", "M3 未結；整體百分比不得掩蓋該教材問題。"),
    ], [3.0, 5.2, 9.6], font_size=9.2, first_col_bold=True)
    add_body(doc, "G1 90 分鐘的分段檢查：基線 31.5 分說明、18 分示範、31.5 分練習，三段相加 81 分；提案 18+18+45=81 分。兩者均尚有 9 分鐘須在正式教案交代轉場或回饋安排。此表重算百分比，不推定實際授課分鐘。", size=9.2)

    # Page 10: group/time comparison and interpretation.
    page_start(doc, "五面向差異與兩次檢討變化", "09 分組與變化")
    rows = []
    for dim in before:
        rows.append((dim, f"{before[dim]}/3 ({before[dim]/3*100:.1f}%)", f"{after[dim]}/3 ({after[dim]/3*100:.1f}%)", f"+{(after[dim]-before[dim])/3*100:.1f} pp", "符合項增加" if after[dim] > before[dim] else "本次無變化"))
    add_table(doc, ["檢討分組", "2026-10-03 基線", "2026-10-08 合成複核", "變化", "讀法"], rows, [2.8, 3.4, 4.0, 2.2, 5.4], font_size=9.0, first_col_bold=True)
    add_heading(doc, "差異解讀", 2)
    add_bullet(doc, "改善集中在學員入班規則、教材追溯和教學方法三個原有缺口；師資與設施示範項目兩次均為 3/3。這只表示本例檢核表上的變化，不代表實際組織能力。")
    add_bullet(doc, "教材面向仍只有 2/3；其中 M3 的六情境複核為 5/6。不能讓其他四面向的高比率抵銷未解的學習材料誤讀。")
    add_bullet(doc, "兩個日期點形成的是短期示範前後比較，不足以稱為多年趨勢或持續成效。真正年度趨勢需同一版本口徑、連續檢討資料和可回查原件。")
    add_heading(doc, "比較邊界", 2)
    add_body(doc, "本報告的分組單位是五個適配面向，不是受訓者人口。沒有 REAL 學員名冊、課程實施或場地紀錄，所以不計任何真實性別、年齡、出席、通過率或成效子群。將 15 項控制結果誤稱為學員符合率，屬錯誤使用。")

    # Page 11: cause and evidence strength.
    page_start(doc, "發現、原因與證據限制", "10 判讀")
    add_table(doc, ["發現", "可核對的示範依據", "原因判斷", "證據強度"], [
        ("L2 條件不夠可重複", "基線規則缺少例外與補件路徑；修訂後增列任務自評及支持方式。", "草案描述對象，卻沒有把判定條件和例外寫成同一流程。", "SYNTHETIC 分析；不證明實際招生公平。"),
        ("M2 版次追溯不足", "初版素材缺來源/版次/覆核欄；示範後建立索引欄。", "素材內容維護責任與版次控制未綁定。", "SYNTHETIC 文件檢視；不證明正式教材已核定。"),
        ("P2 練習份量待調整", "G1 35/20/35 改提 20/20/50；分段重算 81 分，另 9 分仍須交代。", "表現目標需要操作練習；單純提高講授不能證明能力。", "SAMPLE/DERIVED；真實課表、授課紀錄 UNKNOWN。"),
        ("M3 易讀性尚未通過", "6 個合成情境由 4/6 提升至 5/6，仍有 1 個錯誤路徑。", "修訂補了責任角色，仍未清楚把來源查證與詢問講師區分。", "SYNTHETIC usability check；不是學員測試。"),
    ], [2.6, 5.0, 5.0, 5.2], font_size=8.8, first_col_bold=True)
    add_heading(doc, "證據是否足以回答『實際執行符合核定版嗎』？", 2)
    add_table(doc, ["必要核對", "目前狀態", "可接受的 REAL 證據"], [
        ("核定課程及日期", "UNKNOWN", "有權限者核准的課程計畫、版本與日期。"),
        ("招生、師資、教材、方法實際執行", "UNKNOWN", "去識別的實際名冊/紀錄、教材版次、授課及評量紀錄。"),
        ("設施與設備維護", "UNKNOWN", "真實場地/設備識別、檢查日期、異常處理及合法證明原件。"),
        ("修正及效果", "UNKNOWN", "相同指標口徑的前後原始資料、責任覆核及後續追蹤。"),
    ], [4.2, 2.3, 11.3], font_size=9.1, first_col_bold=True, status_col=1)

    # Page 12: decision and recommendations.
    page_start(doc, "結論與可執行建議", "11 決策")
    add_callout(doc, "示範結論", "在 SAMPLE/SYNTHETIC 檢核中，五面向共 15 項基線 11 項符合；調整後 14 項符合，符合率由 73.3% 增至 93.3%。教材 M3 仍有 1/6 情境誤讀，故本例只可進入下一輪合成修訂，不得宣稱 REAL 課程已可開辦或已獲核准。", fill=PALE)
    add_table(doc, ["建議", "依據與判斷", "需要的動作", "成功檢查"], [
        ("1｜補完卡片可讀性", "M3 5/6；剩餘錯誤把詢問講師當查證。", "加入『先標未知、再找來源、交給責任角色、記期限』對照例，對同一 6 題再測。", "6/6 正確才關閉示範缺口；此門檻屬本例，不是官方標準。"),
        ("2｜保留任務導向遴選", "L2 修訂在合成檢核中符合。", "REAL 使用時由有權限者核定條件、例外及支持路徑，保存個資最小化欄位。", "正式標準有來源、權責及可重複判斷紀錄。"),
        ("3｜素材使用版控", "M2 追溯欄在合成檢核中補齊。", "逐件核對來源、版本、使用權、檢查者及修訂理由。", "使用材料均可回到當前核准版。"),
        ("4｜將練習安排寫回教案", "P2 的 20/20/50 改善為 90 分鐘內提案，仍有 9 分鐘安排須解釋。", "核定版明確說明轉場/回饋時間；按完成評量逐項記實際分鐘。", "目標、活動、評量與課表一致，偏差有核准和處置。"),
        ("5｜REAL 前查驗師資與環境", "本例師資/設施只是合成檢查，不含原件。", "取得合法師資能力資料、核准權限、真實場地設備和維護紀錄。", "原件可追溯；本報告不替代聘書、安檢或保險。"),
    ], [3.0, 4.4, 6.0, 4.4], font_size=8.45, first_col_bold=True)
    add_body(doc, "需由協會正式決策者確認：本報告內容只提供分析方法和示範方案；任何正式採用、課程上線、教材核准、師資聘任及資源支出都需按真實權限辦理。", bold_lead="需由協會正式決策者確認：", color=RED, size=9.5)

    # Page 13: action tracker.
    page_start(doc, "責任、期限與追蹤", "12 追蹤閉環")
    add_table(doc, ["行動 ID", "工作與責任角色（均為代碼）", "期限（SAMPLE）", "追蹤指標／取證", "狀態"], [
        ("A-01", "SYN-COORD：補充 L2 任務自評、例外與支持路徑。", "2026-10-07", "L2 以同一準則重判；保留版本差異。", "示範完成"),
        ("A-02", "SYN-COORD：建立素材來源/版次索引，SYN-REVIEWER 覆核。", "2026-10-07", "M2 逐項來源及版次欄完整。", "示範完成"),
        ("A-03", "SYN-COORD：將 G1 分段提案寫入課程修訂工作稿。", "2026-10-08", "20/20/50 重算 90 分鐘，9 分鐘轉場回饋待 REAL 教案說明。", "示範完成；未核定"),
        ("A-04", "SYN-COORD：重寫快速卡；SYN-REVIEWER 用同一 6 題再測。", "2026-10-12", "需 6/6 才關閉 M3；目前 5/6。", "未完成"),
        ("A-05", "SYN-AUTH：REAL 使用前核對權限、教材、師資、課程及場地原件。", "日期 UNKNOWN", "原件逐項定位、授權/核准及版本一致。", "待 Human/權責者原件"),
        ("A-06", "SYN-REVIEWER：確認同口徑前後比較、決策及下一檢討日。", "日期 UNKNOWN", "15 項分母、實際來源、責任和期限齊備。", "REAL 追蹤未建立"),
    ], [1.5, 5.5, 2.6, 5.9, 2.3], font_size=8.35, first_col_bold=True, status_col=4)
    add_heading(doc, "何時退回補件", 2)
    for text in [
        "沒有核定課程版次、檢討日期或來源定位：判 UNKNOWN，退回補原件，不沿用歷史草案。",
        "檢核理由只寫『符合』或『適切』：退回要求具體項目、證據位置、比較準則和覆核者。",
        "課程分鐘數、教材版本或人員角色前後不一致：暫停該列判定，重算並記錄版本差異。",
        "資料含不必要個資或第三方證明：停止公開同步，保留受權限來源索引；不得在公開包填入真實秘密。",
        "使用 SAMPLE 資料推論 REAL 表現或核准：撤回該結論，分開重做 REAL 驗證。",
    ]:
        add_bullet(doc, text, size=9.5)

    # Page 14: learner and materials worksheet.
    page_start(doc, "現場檢討工作表：學員與教材", "附錄 A 可直接填寫")
    add_body(doc, "此表供取得 REAL 原件後逐項使用；本頁空列是工作工具，不能替代前文已填完整的 SAMPLE 示範。不得把空白列、口頭說明或本例數值當作實際證據。")
    form_rows = []
    for c in CHECKS[:6]:
        form_rows.append((c["id"], c["dimension"], c["control"], "日期/版本：＿＿\n來源頁/表：＿＿\n檢核者：＿＿", "符合 / 部分 / 不符 / UNKNOWN", "缺口、責任及期限：＿＿"))
    add_table(doc, ["項次", "面向", "需核對的實際控制", "REAL 來源定位", "判定", "差距與下一步"], form_rows,
              [1.1, 1.7, 4.1, 3.4, 2.7, 4.8], font_size=9.5, first_col_bold=True)
    add_body(doc, "若實際不適用，寫出不適用理由、核准依據、覆核角色及日期後才可調整分母；沒有證據不可填 N/A。", size=9.1, color=MID)

    # Page 15: instructor, method, and facility worksheet.
    page_start(doc, "現場檢討工作表：師資、方法與設施", "附錄 A 可直接填寫")
    add_body(doc, "本頁延續五面向檢核。師資資格、核准、聘任及法定場地文件只能回到合法原件查核；不可把示範角色或場勘樣例抄成 REAL。")
    form_rows = []
    for c in CHECKS[6:]:
        form_rows.append((c["id"], c["dimension"], c["control"], "日期/版本：＿＿\n來源頁/表：＿＿\n檢核者：＿＿", "符合 / 部分 / 不符 / UNKNOWN", "缺口、責任及期限：＿＿"))
    add_table(doc, ["項次", "面向", "需核對的實際控制", "REAL 來源定位", "判定", "差距與下一步"], form_rows,
              [1.1, 1.7, 4.1, 3.4, 2.7, 4.8], font_size=9.5, first_col_bold=True)

    # Page 16: version deviation and evidence trace form.
    page_start(doc, "版本差異與決策記錄表", "附錄 B 核准與追溯")
    add_body(doc, "每次檢討至少能從核定基準追到實際版本、偏差、處理、責任與複核；若核定原件不存在或權限不明，保持 UNKNOWN。不得在此代簽或回填會議決議。")
    add_table(doc, ["必填欄位", "REAL 紀錄"], [
        ("課程名稱、班次與期間", "＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿"),
        ("核定版次、核准日期與合法保存位置", "＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿"),
        ("實際使用版次與材料清單", "＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿"),
        ("實際執行差異（逐項對照核定版）", "＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿"),
        ("偏差原因、立即處置、影響評估", "＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿"),
        ("是否需核准；權限來源與真實原件定位", "＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿"),
        ("複核人、日期、結果與尚存限制", "＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿"),
        ("下一次檢討日/觸發條件與責任角色", "＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿"),
    ], [5.0, 12.6], font_size=9.2, first_col_bold=True)
    add_heading(doc, "判定選項", 2)
    add_table(doc, ["狀態", "使用條件"], [
        ("符合", "核定版與實際版有可追溯證據，且五面向均達核定準則。"),
        ("部分符合", "有支持資料但仍有具體缺口或未完成複核。"),
        ("不符合", "有來源證明實際偏離核定要求，且尚未妥善處理。"),
        ("UNKNOWN", "缺少原件、權限、版本或可靠資料，不能做事實判斷。"),
    ], [3.0, 14.6], font_size=9.2, first_col_bold=True)

    # Page 17: requirement-to-evidence trace and REAL replacement list.
    page_start(doc, "官方要求追溯與 REAL 替換清單", "附錄 C 查核索引")
    trace_rows = [
        ("056｜I12-E01 五面向檢討", "第 2 頁；本報告只負責課程切合性分析。", "官方 PDF 第 4 頁原文；Blueprint I12-E01。", "承辦/覆核角色代碼；目前為 SAMPLE。"),
        ("學員條件與支持", "第 6 頁 L1-L3；第 15 頁工作表。", "面向檢核準則、來源欄與限制。", "須替換正式招生條件、實際資料與授權。"),
        ("教材版次與易讀性", "第 6、9 頁 M1-M3；第 15 頁工作表。", "素材索引、6 個合成情境與未結差距。", "須替換真實教材、版本、授權與測試資料。"),
        ("師資切合性", "第 7 頁 T1-T3；第 16 頁工作表。", "任務能力、授課範圍、評量校準。", "須取得合法師資資料與真實核准/聘任原件。"),
        ("教學方法切合性", "第 7、9-10、13-14 頁 P1-P3 與追蹤。", "活動—目標連結、練習分段、評量與差異。", "須核對實際課表、教學/評量紀錄與版本差異。"),
        ("環境與設備", "第 7-8 頁 F1-F3；第 16 頁工作表。", "空間、設備、日常維護適配，不替代法定文件。", "須取得真實場勘、設備維護及適用第三方原件。"),
        ("持續改善與決策追蹤", "第 8-14 頁；第 17 頁版本差異表。", "基線、修訂、重測、未結事項、責任期限。", "須由真實權責者確認並依 REAL 資料重算。"),
    ]
    add_table(doc, ["官方/分析項", "正文定位", "本件證明什麼", "REAL 替換/覆核"], trace_rows, [3.0, 3.6, 5.2, 5.8], font_size=8.45, first_col_bold=True)
    add_heading(doc, "升格前逐項取得的真實材料", 2)
    for text in [
        "有權限者核定的課程目標、班次、招生條件和現行課程版本。",
        "實際學員適配/支持資料及必要的去識別原始紀錄；個資只保留最小必要範圍。",
        "教材清單、合法來源/授權、版次、審查和修訂紀錄。",
        "真實師資能力與聘任/核准原件；不以示範角色代替真人資格。",
        "實際教學方法、教學分鐘、評量及未達補救紀錄。",
        "真實場地設備檢查與維護原件；需要的安檢/保險文件只能取自合法第三方來源。",
        "具責任人、日期、決策依據、效果追蹤及下一次檢討觸發條件的改善紀錄。",
    ]:
        add_bullet(doc, text, size=9.2)
    add_body(doc, "附件索引：官方原文 PDF 與第 4 頁影像、完整 Unique Blueprint 行、來源對照、逐事實 SAMPLE/SYNTHETIC 替換清冊、技術/版面驗收收據及 exact-SHA reviewer 原始回覆均隨同候選包保存。", size=9.0, color=MID)

    CANDIDATE.parent.mkdir(parents=True, exist_ok=True)
    doc.core_properties.title = "訓練課程切合性檢討與調整分析報告"
    doc.core_properties.subject = "I12-E01 / 官方流水號 056 / SAMPLE-SYNTHETIC 完整示範"
    doc.core_properties.author = "候選示範文件"
    doc.save(CANDIDATE)
    return doc


def main():
    src = collect_sources()
    doc = build_document(src)
    candidate_bytes = CANDIDATE.read_bytes()
    candidate_sha = sha256(candidate_bytes)
    if not zipfile.ZipFile(CANDIDATE).testzip() is None:
        raise RuntimeError("DOCX package ZIP integrity failed")
    page_map = {"學員": 6, "教材": 6, "師資": 7, "教學方法": 7, "訓練設施": 7, "F2": 8, "F3": 8}
    register_path, register_rows = add_replacement_register(candidate_sha, page_map)
    receipt = {
        "schema": "ttqs.0053.build_receipt.v1",
        "doc_id": "0053",
        "requirement_id": "I12-E01",
        "official_checkbox_sequence": "056",
        "document_genre": "analysis_report",
        "candidate_path": str(CANDIDATE),
        "candidate_sha256": candidate_sha,
        "candidate_bytes": len(candidate_bytes),
        "paragraph_count": len(doc.paragraphs),
        "table_count": len(doc.tables),
        "synthetic_register_path": str(register_path),
        "synthetic_register_rows": len(register_rows),
        "synthetic_register_unique_fact_ids": len({r["fact_id"] for r in register_rows}),
        "synthetic_register_sha256": sha256(register_path.read_bytes()),
        "official_pdf_sha256": src["official_pdf_sha256"],
        "blueprint_file_sha256": src["blueprint_file_sha256"],
        "blueprint_row_sha256": src["blueprint_row_sha256"],
        "crosswalk_sha256": src["crosswalk_sha256"],
        "doc_0033_sha256": src["doc_0033_sha256"],
        "doc_0052_sha256": src["doc_0052_sha256"],
        "assertions": {
            "all_15_fit_checks_listed": len(CHECKS) == 15,
            "baseline_fit_rate": "11/15=73.3%",
            "review_fit_rate": "14/15=93.3%",
            "delta": "+3/15=20.0 percentage points",
            "real_activity_claimed": False,
            "real_status": "UNKNOWN",
            "unresolved_sample_gap": "M3 material readability remains 5/6; hold REAL release",
        },
        "built_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    (PACKAGE / "evidence" / "build" / "build_receipt_R01.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
