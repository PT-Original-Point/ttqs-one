from pathlib import Path
from datetime import date
import json
import hashlib
import re

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

OUT = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0136_I19-E26_CANDIDATE_R01_20261025")
OUT.mkdir(parents=True, exist_ok=True)
DOCX = OUT / "0136_I19-E26_R02_CANDIDATE_20261025.docx"
NAVY = "17324D"
TEAL = "147D83"
PALE = "EAF2F5"
SAND = "FFF4D6"
GRAY = "5B6570"
WHITE = "FFFFFF"
BODY = "Microsoft JhengHei"


def set_run_font(run, size=10.5, bold=False, color="253342", italic=False):
    run.font.name = BODY
    run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), BODY)
    run._element.rPr.rFonts.set(qn("w:ascii"), BODY)
    run._element.rPr.rFonts.set(qn("w:hAnsi"), BODY)
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = RGBColor.from_string(color)


def shade(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def cell_margins(cell, top=75, start=90, bottom=75, end=90):
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for m, v in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tc_mar.find(qn("w:" + m))
        if node is None:
            node = OxmlElement("w:" + m)
            tc_mar.append(node)
        node.set(qn("w:w"), str(v))
        node.set(qn("w:type"), "dxa")


def repeat_header(row):
    tr_pr = row._tr.get_or_add_trPr()
    hdr = OxmlElement("w:tblHeader")
    hdr.set(qn("w:val"), "true")
    tr_pr.append(hdr)


def keep_row(row):
    tr_pr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:cantSplit")
    tr_pr.append(el)


def set_cell_text(cell, text, size=9.5, bold=False, color="253342"):
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.line_spacing = 1.0
    r = p.add_run(str(text))
    set_run_font(r, size, bold, color)
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    cell_margins(cell)


def add_table(doc, headers, rows, widths, font_size=9.5, header_size=9.2):
    font_size = max(9.5, font_size)
    header_size = max(9.5, header_size)
    table = doc.add_table(rows=1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.style = "Table Grid"
    repeat_header(table.rows[0])
    keep_row(table.rows[0])
    for i, h in enumerate(headers):
        table.columns[i].width = Inches(widths[i])
        table.rows[0].cells[i].width = Inches(widths[i])
        shade(table.rows[0].cells[i], NAVY)
        set_cell_text(table.rows[0].cells[i], h, header_size, True, WHITE)
    for values in rows:
        row = table.add_row()
        keep_row(row)
        for i, value in enumerate(values):
            row.cells[i].width = Inches(widths[i])
            set_cell_text(row.cells[i], value, font_size)
    doc.add_paragraph().paragraph_format.space_after = Pt(1)
    return table


def add_p(doc, text, bold=False, color="253342", size=10.5, before=0, after=4, italic=False, align=None):
    size = max(10.5, size)
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.line_spacing = 1.1
    if align is not None:
        p.alignment = align
    r = p.add_run(text)
    set_run_font(r, size, bold, color, italic)
    return p


def add_bullets(doc, items, size=10.5):
    size = max(10.5, size)
    for item in items:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.left_indent = Inches(0.24)
        p.paragraph_format.first_line_indent = Inches(-0.15)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.05
        set_run_font(p.add_run(item), size)


def h1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(7)
    set_run_font(p.add_run(text), 16, True, NAVY)
    return p


def h2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_before = Pt(5)
    p.paragraph_format.space_after = Pt(4)
    set_run_font(p.add_run(text), 12, True, TEAL)
    return p


def page(doc):
    doc.add_page_break()


def new_section(doc, landscape=False):
    from docx.enum.section import WD_SECTION
    sec = doc.add_section(WD_SECTION.NEW_PAGE)
    if landscape:
        sec.page_width = Inches(11.69)
        sec.page_height = Inches(8.27)
        sec.top_margin = Inches(0.48)
        sec.bottom_margin = Inches(0.48)
        sec.left_margin = Inches(0.62)
        sec.right_margin = Inches(0.62)
    else:
        sec.page_width = Inches(8.27)
        sec.page_height = Inches(11.69)
        sec.top_margin = Inches(0.62)
        sec.bottom_margin = Inches(0.62)
        sec.left_margin = Inches(0.68)
        sec.right_margin = Inches(0.68)
    sec.header_distance = Inches(0.3)
    sec.footer_distance = Inches(0.3)
    sec.footer.is_linked_to_previous = True
    return sec


def callout(doc, title, body, fill=PALE):
    sec = doc.sections[-1]
    width = (sec.page_width - sec.left_margin - sec.right_margin) / 914400
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    t.columns[0].width = Inches(width)
    c = t.cell(0, 0)
    c.width = Inches(width)
    shade(c, fill)
    c.text = ""
    p = c.paragraphs[0]
    p.paragraph_format.space_after = Pt(2)
    set_run_font(p.add_run(title), 10.5, True, NAVY)
    p2 = c.add_paragraph()
    p2.paragraph_format.space_after = Pt(0)
    p2.paragraph_format.line_spacing = 1.05
    set_run_font(p2.add_run(body), 10.5, False)
    cell_margins(c, 120, 150, 120, 150)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def add_page_number(paragraph):
    run = paragraph.add_run("DOCX 0136  |  候選工具  |  第 ")
    set_run_font(run, 8.3, False, GRAY)
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    paragraph._p.append(fld)
    run2 = paragraph.add_run(" 頁")
    set_run_font(run2, 8.3, False, GRAY)


doc = Document()
sec = doc.sections[0]
sec.page_width = Inches(8.27)
sec.page_height = Inches(11.69)
sec.top_margin = Inches(0.62)
sec.bottom_margin = Inches(0.62)
sec.left_margin = Inches(0.68)
sec.right_margin = Inches(0.68)
sec.header_distance = Inches(0.3)
sec.footer_distance = Inches(0.3)

normal = doc.styles["Normal"]
normal.font.name = BODY
normal._element.rPr.rFonts.set(qn("w:eastAsia"), BODY)
normal._element.rPr.rFonts.set(qn("w:ascii"), BODY)
normal._element.rPr.rFonts.set(qn("w:hAnsi"), BODY)
normal.font.size = Pt(10.5)
normal.paragraph_format.space_after = Pt(4)
normal.paragraph_format.line_spacing = 1.1

footer = sec.footer.paragraphs[0]
footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT
add_page_number(footer)

# Page 1 — controlled identity and intended use
p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(34)
p.paragraph_format.space_after = Pt(4)
set_run_font(p.add_run("TTQS ONE｜候選作業工具"), 12, True, TEAL)
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(8)
set_run_font(p.add_run("公益活動、獎項與學校合作\n原件驗證登錄表"), 25, True, NAVY)
add_p(doc, "收件、來源核驗、主張邊界與調閱工作表", color=GRAY, size=14, after=15)
add_table(doc, ["控制欄位", "本文件值"], [
    ("專案", "TTQS_ONE"),
    ("DOCX 文件編號", "0136"),
    ("142 份文件對照需求", "I19-E26"),
    ("157 內容規劃索引", "150｜公益／表揚／產學／研發社會影響：原件與來源"),
    ("官方紙本方框序號", "UNKNOWN；不得以 0136、I19-E26 或 150 代替"),
    ("文件用途", "操作型原始佐證登錄與查驗工具；不是成果報告、核准紀錄或第三方原件"),
    ("版本狀態", "R01 CANDIDATE｜建置日 2026-10-25｜未正式接受、未核准生效"),
], [1.75, 5.15], 10.2)
callout(doc, "真實資料界線", "本候選沒有附入任何原始點協會的公益活動、獎項、學校合作或社會成效原件。本文標示 SAMPLE／SYNTHETIC 的情境只示範欄位與判讀，不是本協會事實、審查結論或可計入績效的證據。", SAND)
h2(doc, "使用前先確認")
add_bullets(doc, [
    "只對實際收到或已提出的單一主張建立一筆紀錄；沒有來源時，記錄缺口，不補造文件或路徑。",
    "把活動／獎項／合作存在、協會實際角色、社會結果拆成不同主張，各自連到直接來源。",
    "依協會現行授權分工指派承辦與覆核；本候選不創設職務、簽核層級、時限或保存年限。",
    "未完成真實來源查核前，不把候選稿或 SAMPLE 例子當成協會已具備佐證。",
], 10.3)

# Page 2 — workflow
page(doc)
h1(doc, "1｜一筆主張的實際處理流程")
add_p(doc, "用途是把來源、角色與結果分開記清楚，讓後續承辦人能重做核查並找到限制。對外評核可否採計，由評核者依正式標準判斷；本表不自評分數。")
add_table(doc, ["步驟", "承辦操作", "必留紀錄", "暫停或退回條件"], [
    ("01 收件", "登記收到日期、提出者、主張文字、證據類別及案件共通鍵。", "T1 基本列；來源尚未到件就明記未附。", "只有口述／宣傳文字，沒有可追查來源：PENDING_SOURCE。"),
    ("02 保全", "實際取得檔案才記格式、頁數、位元組、接收方式與 SHA-256；保留原件副本。", "T2 原件清冊與每次交接。", "不得替未取得的來源填假雜湊、箱號、伺服器位置或時間戳。"),
    ("03 核來源", "沿來源上可確認的官方管道核對出具方、文件日期、對象、範圍與完整性。", "T3 核驗項、查核日期、查核管道及結果。", "來源方否認、內容矛盾、來源無法歸屬或檔案異常：暫緩或駁回並留理由。"),
    ("04 核角色", "另找直接資料證明原始點協會做了什麼；合作名稱或受邀名單本身不足。", "角色主張及對應來源位置。", "無直接角色資料：不得從活動存在推定協會參與。"),
    ("05 核結果", "每個數字記量尺、期間、分子、分母與來源；無來源就 UNKNOWN。", "結果主張、計算方法、限制與來源。", "不得以出席、合作或得獎推估社會影響或因果。"),
    ("06 判定／調閱", "依狀態表記錄範圍、限制、待辦與可重做的調閱路徑。", "T4/T5；覆核者依實際授權指派。", "個資／揭露依據未釐清時 HOLD_PRIVACY；不可公開來源定位。"),
], [0.72, 2.45, 1.72, 2.01], 9.5, 9.5)
callout(doc, "期限與權限", "本候選沒有另訂 24 小時收件期限、雙人簽章、主管核准或強制 WORM。若協會已有正式授權或保存規則，記錄其正式文件名稱與版本後遵循；查不到時標 UNKNOWN 並依現行權責處理，不自行創設。", SAND)

# Page 3 — official identity and neighbors
page(doc)
h1(doc, "2｜官方來源與文件邊界")
add_p(doc, "官方來源：TTQS 官方評核文件，指標 19 高標準參考佐證，印刷頁 8 末至頁 9 開頭。原文：")
callout(doc, "官方參考佐證原句", "提出參與社會公益活動、獲頒公民營單位獎項、結合學校單位產學或研發成果社會面。", PALE)
add_p(doc, "這是官方列示的參考佐證類型，不代表原始點協會已完成其中任何一類，也不表示必須同時具備全部類型。本登錄表只記來源與可支持的主張，不替代正式評核。")
h2(doc, "編號不可互換")
add_table(doc, ["識別", "值", "用途"], [
    ("DOCX", "0136", "142 份生產序列文件號"),
    ("crosswalk", "I19-E26", "官方需求映射識別"),
    ("157 索引", "150", "內部內容規劃索引；不是方框序號"),
    ("紙本方框序號", "UNKNOWN", "在取得明確來源前維持未知"),
], [1.5, 1.55, 3.85], 9.7)
h2(doc, "相鄰文類分流")
add_table(doc, ["DOCX／需求", "主要問題", "本表如何處理"], [
    ("0135／I19-E25", "目標市場與顧客價值", "市場／顧客價值分析另行記錄；不得把本表當市場調查。"),
    ("0136／I19-E26", "公益參與、獎項、學校產學／研發社會面來源", "本表記原件、協會角色、結果來源及限制。"),
    ("0137／I19-E27", "媒體報導", "報導可作線索或補強，不能替代活動、得獎或合作原始來源。"),
    ("0133／I19-E22", "訓練班次與人次", "訓練統計另列；不得重複計入本表社會影響。"),
    ("0134／I19-E23", "會員與會費", "會員／財務名冊另控；不能用來證明公益結果。"),
], [1.25, 2.28, 3.37], 9.4)
callout(doc, "避免重複計算", "使用同一活動／專案共通鍵比對其他文件。相同的活動、獎項或成果可以被不同文件引用作不同用途，但要記錄原始來源只存一處、各文件引用位置及其可支持的範圍。", PALE)

# Page 4 — distinct evidence routes
page(doc)
h1(doc, "3｜三種來源路徑，各自核對三層主張")
add_table(doc, ["證據類別", "存在／身分", "協會角色", "結果／社會面"], [
    ("A 公益活動", "核活動主辦方、活動名稱、日期與實際舉辦資料。", "核原始點協會具體參與方式與範圍；受邀或照片不能單獨證明履行。", "受益人數、時數、服務量或影響分開核來源、單位、期間、分母。"),
    ("B 獎項", "核頒發單位、獎項名稱／類別、日期、適用年度及正式得獎名單或可驗證原件。", "核獲獎主體是否確為協會；提名、申請或個人得獎不可改寫成協會獲獎。", "獎項本身不證明社會成果；另有結果主張時另找來源。"),
    ("C 學校／產學／研發", "核學校或單位、專案期間、協議／工作紀錄與正式產出。", "核協會投入、責任與實際交付，不能以 MOU 或會議名稱代替。", "核成果被誰使用、使用情境及社會面來源；驗收不自動證明影響。"),
], [1.15, 1.92, 1.92, 1.91], 9.5, 9.5)
h2(doc, "不足時的處置")
add_table(doc, ["類別", "保持 UNKNOWN／退回的條件"], [
    ("A 公益活動", "活動存在但角色未證：角色 UNKNOWN；只有宣傳素材：PENDING_SOURCE。"),
    ("B 獎項", "提名不等於獲獎；主體不符或頒發方否認時拒收該主張。"),
    ("C 學校／研發", "只有協議不證完成；沒有社會面來源，結果 UNKNOWN。"),
], [1.65, 5.25], 9.5, 9.5)
h2(doc, "來源強度的操作檢查")
add_bullets(doc, [
    "第一手來源：取得原件或可驗證的第一方數位文件，保留原始位元組、來源歸屬、定位頁／項及核對紀錄。SHA-256 只對實際取得的原始檔計算。",
    "第二手來源：可歸屬的官方公開資料或可信第三方記載；只支持來源直接記載的事實，並標出未持有原件的限制。",
    "單一來源不自動證明所有事實：主辦方公告可證明活動資訊，但不當然證明協會實際服務量或社會結果。",
    "來源頁面／版本會變動時，保留查詢日期與可重做的官方網址或檔案版本；不得以內部猜測網址取代。",
], 10.2)
callout(doc, "主張拆分規則", "T1 每一列只記一個可以核驗的主張。活動存在、協會角色、出席或投入、量化結果分列或以清楚的子項連結各自來源。", SAND)

# Page 5 — status and decisions
page(doc)
h1(doc, "4｜狀態、判定與停止條件")
add_table(doc, ["狀態", "何時使用", "允許表述／處置"], [
    ("SAMPLE_ONLY", "示範或訓練情境；沒有真實來源，所有合成值已列 T6。", "只供訓練，不代表協會事實；不得對外主張或計入實績。"),
    ("PENDING_SOURCE", "真實主張已提出，但來源未取得、來源方未核、角色或結果缺證。", "只陳述已知且有來源的部分；列待辦與負責職務／期限，未證部分 UNKNOWN。"),
    ("HOLD_PRIVACY", "來源可能支持事實，但資料含個資／機密，揭露依據、同意或遮蔽方式未完成。", "限制調閱與公開；先依適用的正式個資／保密規則處理。"),
    ("VERIFIED_PRIMARY", "已取得第一方原件或可驗證數位原件，來源、完整性、相關性、角色及所述結果逐項核過。", "只對被來源支持的主張標記已核；來源雜湊綁實際原始位元組。"),
    ("VERIFIED_SECONDARY", "可歸屬的官方／第三方公開來源支持有限主張，但原件未取得。", "限於公開來源直接記載範圍；明示未持有原件，不稱原件驗證。"),
    ("REJECTED", "來源方否認、內容有實質矛盾／偽變造跡象、主體不符、重複冒用，或有界核查後仍無法支持主張。", "記錄具體被拒絕的主張與理由；不可刪掉歷史或另建號規避。"),
], [1.9, 2.35, 2.7], 9.5, 9.5)
h2(doc, "狀態轉換的控制點")
add_table(doc, ["現況", "可往下走的條件", "不能做的推論"], [
    ("來源未附", "取得來源後記錄原件資訊並做核驗；在此之前為 PENDING_SOURCE 或 SAMPLE_ONLY。", "不得填入看似真實的箱號、哈希、簽名或查驗結果。"),
    ("隱私未清", "依正式規則完成最小化、遮蔽與揭露權限核對，並留下依據。", "不得因遮住姓名就宣稱已取得所有必要授權。"),
    ("角色未證", "補上能直接證明協會參與／受獎／交付的來源。", "不得由活動、新聞、合作標題推定協會角色。"),
    ("結果未證", "補上結果來源及單位、期間、分母、算法；否則保留 UNKNOWN。", "不得把活動存在、合作或獎項當因果或效益數據。"),
], [1.25, 2.93, 3.02], 9.5, 9.5)
callout(doc, "決定權", "本工具不創設雙重簽核、職稱或核准權。實際核驗人與覆核人須依協會現行授權指派；若授權來源不明，不自封核准權，記錄 UNKNOWN 並保持未核狀態。", SAND)

# Page 6 — synthetic case A
page(doc)
h1(doc, "5｜SAMPLE 案例 A：公益活動來源不足")
callout(doc, "整頁情境標記", "以下是 SYNTHETIC 操作演練，非原始點協會活動紀錄。沒有實際主辦單位、名冊、照片、簽收、原件或查核；不得當作 REAL 或對外引用。", SAND)
add_table(doc, ["T1 欄位", "完整示範填值"], [
    ("record_id／共通鍵", "SAMPLE-ACT-001／SAMPLE-EVENT-A-001"),
    ("需求映射", "DOCX 0136；I19-E26；157 索引 150；紙本方框 UNKNOWN"),
    ("主張", "SAMPLE：某社區健康識能活動邀請原始點協會協助。此句完全虛構，只演示拆分主張。"),
    ("主辦方／活動／日期", "SAMPLE-ORGANIZER-A（非真實機構名稱）；SAMPLE-EVENT-A；SAMPLE_DATE=2026-06-15"),
    ("協會角色", "SAMPLE_ROLE=協助宣導；真實角色來源：NONE；核實結果：NOT TESTED"),
    ("來源與原件", "SAMPLE_SOURCE_NOT_ATTACHED；沒有檔案、頁數、位元組、原件雜湊或保管位置。"),
    ("活動存在／參與／結果", "三者均沒有真實來源；參與與任何量化結果為 UNKNOWN。"),
    ("狀態與理由", "SAMPLE_ONLY；演練資料不進 REAL 登錄計數。若是實際收到但未附來源的案件，真實案件應先列 PENDING_SOURCE。"),
    ("下一步演練", "若真實案件發生：向主辦方取活動紀錄；另外取協會角色證明；任何人次或服務量另取含期間與分母的來源。"),
    ("可對外文字", "NOT FOR EXTERNAL USE。此 SAMPLE 不可作為活動曾舉辦、協會曾參與或有成效之主張。"),
], [1.65, 5.25], 9.6, 9.6)
h2(doc, "演練判讀")
add_bullets(doc, [
    "若只有活動海報或報名頁，只能提供活動資訊線索，不能證明實際舉辦或協會履行角色。",
    "若有主辦方結案說明但沒有協會參與資料，可記錄活動來源已核，角色仍 UNKNOWN。",
    "不得用照片辨認未授權個人；若影像含可識別參與者，先依正式隱私規則處理。",
], 10.1)

# Page 7 — synthetic case B
page(doc)
h1(doc, "6｜SAMPLE 案例 B：獎項主體與授獎事實待核")
callout(doc, "整頁情境標記", "以下是 SYNTHETIC 操作演練。沒有真實頒獎單位、獎狀、名冊或得獎公告；不主張本協會獲獎。", SAND)
add_table(doc, ["T1 欄位", "完整示範填值"], [
    ("record_id／共通鍵", "SAMPLE-AWD-001／SAMPLE-AWARD-GROUP-B-001"),
    ("需求映射", "DOCX 0136；I19-E26；157 索引 150；紙本方框 UNKNOWN"),
    ("主張", "SAMPLE：某主體被提名參與某示範獎項。提名不等於獲獎。"),
    ("頒發方／獎項／日期", "SAMPLE-ISSUER-B；SAMPLE-AWARD-TITLE-B；SAMPLE_DATE=2026-05-20；皆為合成標籤。"),
    ("受獎主體", "SAMPLE-RECIPIENT-B；與原始點協會是否為同一法人：UNKNOWN；不得推定。"),
    ("來源與原件", "SAMPLE_SOURCE_NOT_ATTACHED；沒有獎狀、頒獎名冊、官方公告、檔案雜湊或存放位置。"),
    ("授獎／協會角色／結果", "授獎事實未核；受獎主體未核；社會結果沒有來源，均 UNKNOWN。"),
    ("狀態與理由", "SAMPLE_ONLY；演練中的審查狀態是非真實。實際只有提名資料時，不得列 VERIFIED_PRIMARY。"),
    ("下一步演練", "查頒發單位官方名單或直接確認獎項名稱、類別、年度及法人受獎主體；另核公布範圍和個資揭露。"),
    ("可對外文字", "NOT FOR EXTERNAL USE。不得將提名、申請、入選或個人獲獎改寫為協會獲獎。"),
], [1.65, 5.25], 9.6, 9.6)
h2(doc, "退件條件")
add_bullets(doc, [
    "頒發方查無該獎或否認該文件：記錄查核管道與日期，拒絕該獎項主張。",
    "獎狀主體是個人、會員或合作單位：只能按原件記錄該主體，不可移轉成協會獲獎。",
    "只取得提名通知或參與證明：狀態不得升成獲獎已核。",
], 10.1)

# Page 8 — synthetic case C
page(doc)
h1(doc, "7｜SAMPLE 案例 C：學校合作與社會結果分離")
callout(doc, "整頁情境標記", "以下是 SYNTHETIC 操作演練。沒有真實學校、協議、教材、驗收或使用者回饋；不主張本協會完成產學合作或產生社會效益。", SAND)
add_table(doc, ["T1 欄位", "完整示範填值"], [
    ("record_id／共通鍵", "SAMPLE-SCH-001／SAMPLE-PROJECT-C-001"),
    ("需求映射", "DOCX 0136；I19-E26；157 索引 150；紙本方框 UNKNOWN"),
    ("主張", "SAMPLE：一項學校合作情境擬開發教材並供社區使用。這只是虛構流程，不是協會專案。"),
    ("學校／期間／成果", "SAMPLE-SCHOOL-C；SAMPLE_PERIOD=2026-04-01 至 2026-09-30；SAMPLE-OUTPUT-C；皆為合成標籤。"),
    ("協會貢獻", "SAMPLE_ROLE=提供內容建議；沒有工作紀錄、交付物或校方確認；實際貢獻 UNKNOWN。"),
    ("來源與原件", "SAMPLE_SOURCE_NOT_ATTACHED；沒有協議、專案紀錄、教材、驗收或校方原件。"),
    ("產出／驗收／社會面", "三者分開判讀；均沒有真實來源；使用情境、受益人數與結果皆 UNKNOWN。"),
    ("狀態與理由", "SAMPLE_ONLY；演練資料不列 REAL。若只有協議，真實案件只能支持有協議，不支持完成或效益。"),
    ("下一步演練", "核正式合作來源及實際工作分工；取交付物與校方驗收來源；社會面結果另以使用紀錄或適當來源證明。"),
    ("可對外文字", "NOT FOR EXTERNAL USE。不得由合作意向、會議或 MOU 推定完成、採用或社會影響。"),
], [1.65, 5.25], 9.6, 9.6)
h2(doc, "本案例不計算效益")
add_p(doc, "因沒有實際使用、覆蓋人數、期間或結果來源，不建立比例、成長率或因果敘述。若未來取得量化資料，逐項記錄單位、分子、分母、時間範圍、去重方式及原始來源；資料不足時維持 UNKNOWN。")

# Page 9 — field dictionary and T1
page(doc)
h1(doc, "8｜T1 登錄欄位字典與可複核紀錄")
add_p(doc, "正式案件一列一主張；需要時以共同 event_project_key 串接同一活動的不同主張。只填已知且有來源的資料。空白代表未完成，不代表通過。")
add_table(doc, ["欄位組", "必填內容", "資料規則"], [
    ("識別", "record_id、event_project_key、DOCX、需求 ID、157 索引、紙本方框序號", "方框序號未知就明寫 UNKNOWN；案號依協會既有規則產生，不重用。"),
    ("主張", "一行一個可核驗的事件／獎項／專案／角色／結果主張", "原文與整理文字分開；不得把參與、角色、成效合成一句推論。"),
    ("來源", "來源方、來源標題、日期、格式、頁／段／項、取得方式、原件狀態", "未取得填 NONE；不是實際檔案就沒有來源 SHA。"),
    ("角色與結果", "協會角色、直接來源、結果單位、期間、分子／分母、算法", "無直接資料填 UNKNOWN；NOT_APPLICABLE 必須附理由。"),
    ("核查與限制", "查核管道／日期／結果、相關性、重複鍵、隱私級別、限制", "標清楚誰核了哪項；一項通過不代表其他項通過。"),
    ("後續與決定", "狀態、理由、待補項、責任職務、期限來源、可重做調閱指引", "承辦／覆核依現行授權；沒有授權或期限來源時標 UNKNOWN。"),
], [1.15, 3.0, 2.75], 9.5, 9.5)
h2(doc, "T1｜新收案件填寫列（空白作業表）")
add_table(doc, ["欄位", "本次填寫"], [
    ("record_id／event_project_key", ""),
    ("證據類別／主張原文", ""),
    ("來源方／來源標題／日期", ""),
    ("協會角色及其直接來源", ""),
    ("結果／單位／期間／分子／分母／來源", ""),
    ("原件格式／頁數／位元組／SHA-256", ""),
    ("隱私／公開限制／重複鍵", ""),
    ("狀態／理由／待辦／期限來源", ""),
    ("承辦與覆核（依現行授權）／日期", ""),
], [2.5, 4.4], 9.5, 9.5)
add_p(doc, "表格空列只供真實收件時填寫；本份候選不含任何 REAL 案件。完整填寫方式請對照第 5–7 節三筆 SAMPLE 案例。", color=GRAY, size=9.8, italic=True)

# Page 10 — custody and verification (landscape for usable writing cells)
new_section(doc, landscape=True)
h1(doc, "9｜T2 原件清冊／交接與 T3 逐項核驗")
h2(doc, "T2｜原件清冊與交接紀錄")
add_p(doc, "每個實際收到的原件／檔案各有一列；傳遞、調閱、返還另記一列。原件未收到時不得建立虛構清冊資料。", size=10)
add_table(doc, ["record_id／物件", "格式／頁數／bytes", "原件 SHA-256", "來源與定位", "保管／存取", "交接時間／人員／原因"], [
    ("", "", "", "", "", ""),
    ("", "", "", "", "", ""),
], [1.55, 1.4, 1.5, 1.85, 1.3, 2.1], 9.5, 9.5)
add_p(doc, "來源 SHA-256 計算對象須是實際原始位元組；不得使用空檔、範例字串或文件內示意值冒充來源雜湊。保管位置只寫進受控內部紀錄；公開版採最小化描述。", size=9.8)
h2(doc, "T3｜逐項核驗檢查表")
add_table(doc, ["核驗項", "結果：是／否／未知／不適用", "來源定位與檢查者紀錄"], [
    ("出具方／主辦方／學校可歸屬", "", ""),
    ("文件完整性、版本、實際檔案雜湊", "", ""),
    ("事件／獎項／合作本身成立", "", ""),
    ("原始點協會主體及實際角色", "", ""),
    ("交付／完成狀態（若有主張）", "", ""),
    ("社會結果、單位、期間、分母及算法", "", ""),
    ("相關性與跨文件重複檢查", "", ""),
    ("個資／保密／公開依據已處理", "", ""),
    ("另一人可依指引重做來源調閱", "", ""),
], [2.7, 2.0, 5.0], 9.5, 9.5)

# Page 11 — correction and claim-source forms
p = h1(doc, "10｜T4 補正／駁回追蹤與 T5 主張對來源矩陣")
p.paragraph_format.page_break_before = True
h2(doc, "T4｜待補、暫緩、駁回與複查")
add_table(doc, ["record_id／主張", "狀態", "具體缺口或矛盾", "下一個可驗證動作", "責任職務／期限來源", "複查與結案條件"], [
    ("", "", "", "", "", ""),
    ("", "", "", "", "", ""),
], [1.25, 1.0, 2.15, 2.15, 1.65, 1.5], 9.5, 9.5)
add_p(doc, "若拒絕某一主張，保留原 record_id、來源檢查證據與理由；更正新事實時以修訂紀錄連結舊列，不刪除不利歷史。期限只採正式內規或實際指派日期。", size=9.8)
h2(doc, "T5｜對外主張與來源逐句對照")
add_table(doc, ["主張句／版本", "唯一 record_id", "原件或公開來源與頁項", "已支持範圍／限制", "狀態／可用文字"], [
    ("", "", "", "", ""),
    ("", "", "", "", ""),
], [2.1, 1.35, 2.25, 2.1, 1.9], 9.5, 9.5)
callout(doc, "對外用語控制", "只使用來源已直接支持的句子，並保留期間、對象、範圍與來源限制。SAMPLE、PENDING_SOURCE、HOLD_PRIVACY、REJECTED 的內容不得寫成協會已完成的實績。", SAND)

# Page 12 — synthetic replacement
page(doc)
h1(doc, "11｜T6 SAMPLE-to-REAL 替換清冊與交付檢查")
add_p(doc, "下表列出本候選三例的所有刻意合成欄位群及其替換來源。替換前不得填真實組織名稱、原件定位、簽名或核准；實際收件後另建立 REAL record_id，保留 SAMPLE 範例不變。")
add_table(doc, ["SAMPLE 記錄／合成欄位", "本文示範值（均非真）", "升為真實主張所需來源", "完成條件"], [
    ("SAMPLE-ACT-001：案件／活動鍵、活動名稱、主辦方標籤", "SAMPLE-ACT-001；SAMPLE-EVENT-A-001；SAMPLE-ORGANIZER-A；SAMPLE-EVENT-A", "可歸屬主辦方的活動紀錄／確認，含名稱、日期與實際舉辦範圍。", "核來源身分、日期及實際舉辦；保留頁項與檔案資料。"),
    ("SAMPLE-ACT-001：日期、協會角色與宣導內容", "SAMPLE_DATE=2026-06-15；SAMPLE_ROLE=協助宣導", "主辦方對協會角色的確認及協會實際投入紀錄。", "活動、角色分開核；無來源部分維持 UNKNOWN。"),
    ("SAMPLE-ACT-001：來源狀態與結果", "SAMPLE_SOURCE_NOT_ATTACHED；結果 UNKNOWN；無計量數字", "若提出人次／服務量／結果，提供對應期間、定義、分子分母及直接來源。", "實際文件取得後計算雜湊；來源未到件不升級。"),
    ("SAMPLE-AWD-001：案號／獎項鍵／頒發方／標題", "SAMPLE-AWD-001；SAMPLE-AWARD-GROUP-B-001；SAMPLE-ISSUER-B；SAMPLE-AWARD-TITLE-B", "頒發方可驗證名單或獎項原件，含名稱、類別、年度及日期。", "核頒發方、獎項及受獎主體；提名不等於得獎。"),
    ("SAMPLE-AWD-001：日期／受獎主體／來源", "SAMPLE_DATE=2026-05-20；SAMPLE-RECIPIENT-B；無來源", "能證明法律主體一致的來源；必要時取得揭露權限依據。", "主體不一致時只記錄原件所載主體，不轉述為協會獲獎。"),
], [2.0, 2.3, 3.25, 2.15], 9.5, 9.5)

# Page 14 — synthetic replacement continuation and actionable conversion sequence
page(doc)
h2(doc, "T6 續｜學校合作與共用欄位")
add_table(doc, ["SAMPLE 記錄／合成欄位", "本文示範值（均非真）", "升為真實主張所需來源", "完成條件"], [
    ("SAMPLE-SCH-001：專案／學校／期間／產出", "SAMPLE-SCH-001；SAMPLE-PROJECT-C-001；SAMPLE-SCHOOL-C；2026-04-01 至 2026-09-30；SAMPLE-OUTPUT-C", "學校／專案來源、合作或工作記錄、實際交付物及適用的驗收來源。", "分別核合作、貢獻、交付、驗收；協議本身不證明結果。"),
    ("SAMPLE-SCH-001：協會角色與社會結果", "SAMPLE_ROLE=提供內容建議；角色未證；社會結果 UNKNOWN", "直接支持協會貢獻的紀錄；另取成果使用情境及社會面結果來源。", "沒有使用／結果來源就不寫影響，不建比例或因果。"),
    ("三例共用：狀態、NOT FOR EXTERNAL USE、無原件", "SAMPLE_ONLY；無原始檔／雜湊／實體位置／簽名／核准", "真實收件後以實際來源建立獨立記錄；個資與公開依據另核。", "不得將任何 SAMPLE 欄位直接複製成 REAL；逐欄替換並保留來源鏈。"),
], [2.0, 2.3, 3.25, 2.15], 9.5, 9.5)
h2(doc, "逐欄轉換步驟")
add_table(doc, ["順序", "實際動作", "完成證據"], [
    ("1", "取得真實來源；沒有來源就保持 PENDING_SOURCE，不填示意內容。", "來源實際位元組、來源方與頁項定位。"),
    ("2", "建立新的 REAL record_id；保留 SAMPLE 範例及替換關聯。", "新舊 ID 的交叉連結與建立日期。"),
    ("3", "分開核事件／授獎／合作、協會角色、交付與結果。", "逐項 T3 判定及每項對應的來源位置。"),
    ("4", "對實際原件計算 SHA-256；查個資、保密、重複及可公開範圍。", "T2 原件紀錄與適用規則／處置結果。"),
    ("5", "更新 T1、T4、T5 及引用文件；無證部分明記 UNKNOWN。", "變更紀錄、責任人依據、剩餘缺口。"),
], [0.8, 4.4, 5.0], 9.5, 9.5)

# Page 13 — final review and retrieval procedure
new_section(doc, landscape=False)
h1(doc, "12｜調閱演練、交接與候選狀態")
h2(doc, "另一人可重做的調閱演練")
add_table(doc, ["次序", "核對動作", "完成證據"], [
    ("1", "以 record_id 找到 T1 主張列，確認需求映射及 event_project_key。", "記錄找到的列與引用文件。"),
    ("2", "按內部受控定位資料取得允許調閱的原始來源；不要把受限位置抄入公開版。", "記錄調閱人、時間、目的與來源版本。"),
    ("3", "實際計算來源檔 SHA-256，與 T2 記錄比對；確認頁數、格式及文件是否完整。", "比對結果一致才可記錄原件位元組已重核。"),
    ("4", "依 T3 的頁／段／項，逐字確認來源實際支持哪一個主張。", "分開寫支持範圍、未支持部分及限制。"),
    ("5", "檢查隱私／保密處置、重複鍵、案件狀態與目前對外文字。", "留下檢查項目與結果；未知項不得略過。"),
    ("6", "依現行保管規則完成返還或保存，更新 T2 交接紀錄。", "記錄實際交接及未結事項；不得虛填簽名。"),
], [0.72, 3.9, 5.08], 9.5, 9.5)
h2(doc, "交接自查")
add_bullets(doc, [
    "每個外部主張都有確切 record_id、來源項、核查日期、狀態及限制。",
    "三類來源分流清楚；0135、0137、0133、0134 的相鄰用途沒有混入。",
    "原始檔雜湊只來自實際來源；受限定位與公開資料分離。",
    "所有 SAMPLE 欄位仍標示合成，沒有協會核准、簽章、第三方原件或正式接受暗示。",
    "DOCX 最終候選 SHA、技術／版面收據及獨立語意審查範圍另行綁定；建置本身不代表通過或正式接受。",
], 10.5)
callout(doc, "本候選的事實狀態", "原始點協會 REAL 佐證：UNKNOWN（本候選未連接正式證據庫）。本候選狀態：CANDIDATE。Human 正式接受：NOT GRANTED。", PALE)

# Core properties and save
doc.core_properties.title = "公益活動、獎項與學校合作原件驗證登錄表"
doc.core_properties.subject = "TTQS ONE DOCX 0136 / I19-E26 operational verification register candidate"
doc.core_properties.author = "TTQS ONE candidate production"
doc.core_properties.keywords = "TTQS_ONE;0136;I19-E26;SAMPLE;CANDIDATE"
doc.core_properties.comments = "Candidate only. No REAL association evidence or formal approval is asserted."
doc.save(DOCX)

# Deterministic text and structural receipt; this is not independent semantic QA.
check = Document(DOCX)
all_text = "\n".join([p.text for p in check.paragraphs] + [c.text for t in check.tables for row in t.rows for c in row.cells])
sha = hashlib.sha256(DOCX.read_bytes()).hexdigest()
required = [
    "0136", "I19-E26", "UNKNOWN", "提出參與社會公益活動、獲頒公民營單位獎項、結合學校單位產學或研發成果社會面。",
    "SAMPLE-ACT-001", "SAMPLE-AWD-001", "SAMPLE-SCH-001", "SAMPLE_ONLY", "PENDING_SOURCE",
    "HOLD_PRIVACY", "VERIFIED_PRIMARY", "VERIFIED_SECONDARY", "REJECTED", "NOT FOR EXTERNAL USE",
    "T1", "T2", "T3", "T4", "T5", "T6", "0135", "0137", "NOT GRANTED"
]
missing = [x for x in required if x not in all_text]
for forbidden in ["Baseline Commit SHA", "自簽署日起正式生效", "24 小時內啟動", "VAULT_BOX_REAL_0136", "SECURE_SERVER://"]:
    if forbidden in all_text:
        missing.append("FORBIDDEN:" + forbidden)
receipt = {
    "project_id": "TTQS_ONE",
    "doc_id": "0136",
    "official_requirement_id": "I19-E26",
    "project_157_index": 150,
    "official_printed_checkbox_serial": "UNKNOWN",
    "revision": "R02_CANDIDATE_20261025",
    "source_commit": "a19293ffae3096c5f7306d851b1fc1659ee8e82e",
    "unique_blueprint_sha256": "32c1b818cc0b3957a23e319606f77b176a7979d1ee4ff58db72b9ae32ada8399",
    "worker_raw_response_adopted": False,
    "worker_output_used_as_template": False,
    "docx_sha256": sha,
    "docx_bytes": DOCX.stat().st_size,
    "paragraph_count": len(check.paragraphs),
    "table_count": len(check.tables),
    "table_row_counts": [len(t.rows) for t in check.tables],
    "required_content_present": not missing,
    "missing_or_forbidden": missing,
    "real_evidence": "UNKNOWN",
    "technical_validation": "PASS" if not missing else "FAIL",
    "independent_semantic_review": "PENDING",
    "formal_acceptance": "NOT_GRANTED",
    "limitations": [
        "Builder deterministic checks are not independent semantic review.",
        "No REAL association source is attached or asserted.",
        "The three completed examples are synthetic demonstrations only."
    ]
}
(OUT / "BUILD_RECEIPT_0136_R02.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False, indent=2))
