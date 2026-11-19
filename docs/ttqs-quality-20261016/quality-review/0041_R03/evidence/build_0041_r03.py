from pathlib import Path
import csv
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "candidate" / "0041_R03.docx"
REGISTER = ROOT / "evidence" / "SYNTHETIC_REPLACEMENT_REGISTER_R03.csv"

NAVY = "17324D"
TEAL = "0F766E"
PALE = "EAF2F4"
PALE_BLUE = "EEF3F8"
GOLD = "B77716"
INK = "243240"
MUTED = "52616B"
RED = "A13D36"
WHITE = "FFFFFF"
FONT = "Microsoft JhengHei"

def set_run(run, size=10.5, bold=False, color=INK, italic=False):
    run.font.name = FONT
    run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), FONT)
    run._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), "Arial")
    run._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), "Arial")
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = RGBColor.from_string(color)

def set_cell_fill(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = tcPr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tcPr.append(shd)
    shd.set(qn("w:fill"), fill)

def set_cell_margins(cell, top=90, start=100, bottom=90, end=100):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = tcPr.first_child_found_in("w:tcMar")
    if tcMar is None:
        tcMar = OxmlElement("w:tcMar")
        tcPr.append(tcMar)
    for m, v in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tcMar.find(qn("w:" + m))
        if node is None:
            node = OxmlElement("w:" + m)
            tcMar.append(node)
        node.set(qn("w:w"), str(v))
        node.set(qn("w:type"), "dxa")

def repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    tblHeader = OxmlElement("w:tblHeader")
    tblHeader.set(qn("w:val"), "true")
    trPr.append(tblHeader)

def no_split(row):
    trPr = row._tr.get_or_add_trPr()
    elem = OxmlElement("w:cantSplit")
    trPr.append(elem)

def set_table_borders(table, color="C9D5DC", size="5"):
    tblPr = table._tbl.tblPr
    borders = tblPr.first_child_found_in("w:tblBorders")
    if borders is None:
        borders = OxmlElement("w:tblBorders")
        tblPr.append(borders)
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        tag = "w:" + edge
        el = borders.find(qn(tag))
        if el is None:
            el = OxmlElement(tag)
            borders.append(el)
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), size)
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), color)

def set_cell_text(cell, text, header=False, size=9.5, align=None):
    cell.text = ""
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    if align is not None:
        p.alignment = align
    r = p.add_run(str(text))
    set_run(r, size=size, bold=header, color=WHITE if header else INK)
    set_cell_margins(cell)
    if header:
        set_cell_fill(cell, NAVY)

def add_table(doc, headers, rows, widths, font=9.5):
    font = max(float(font), 9.5)
    table = doc.add_table(rows=1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table)
    for i, h in enumerate(headers):
        table.columns[i].width = Inches(widths[i])
        table.rows[0].cells[i].width = Inches(widths[i])
        set_cell_text(table.rows[0].cells[i], h, header=True, size=font)
    repeat_header(table.rows[0])
    no_split(table.rows[0])
    for ridx, values in enumerate(rows):
        cells = table.add_row().cells
        no_split(table.rows[-1])
        for i, value in enumerate(values):
            cells[i].width = Inches(widths[i])
            set_cell_text(cells[i], value, size=font)
            if ridx % 2 == 1:
                set_cell_fill(cells[i], "F6F8FA")
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return table

def add_p(doc, text="", size=10.5, bold=False, color=INK, before=0, after=5, italic=False, keep=False):
    size = max(float(size), 10.5)
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.line_spacing = 1.12
    if keep:
        p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    set_run(r, size=size, bold=bold, color=color, italic=italic)
    return p

def add_bullets(doc, items, size=10.2):
    size = max(float(size), 10.5)
    for item in items:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.left_indent = Inches(0.24)
        p.paragraph_format.first_line_indent = Inches(-0.16)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.08
        set_run(p.add_run(item), size=size)

def heading(doc, text, level=1):
    p = doc.add_paragraph(style=f"Heading {level}")
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_before = Pt(9 if level == 1 else 6)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text)
    set_run(r, size=14 if level == 1 else 11.5, bold=True, color=NAVY if level == 1 else TEAL)
    return p

def callout(doc, label, text, fill=PALE):
    t = doc.add_table(rows=1, cols=1)
    no_split(t.rows[0])
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    t.columns[0].width = Inches(6.8)
    cell = t.cell(0, 0)
    cell.width = Inches(6.8)
    set_cell_fill(cell, fill)
    set_cell_margins(cell, top=135, start=150, bottom=135, end=150)
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.1
    r = p.add_run(label + "｜")
    set_run(r, size=10.2, bold=True, color=TEAL if fill == PALE else RED)
    r = p.add_run(text)
    set_run(r, size=10.2, color=INK)
    set_table_borders(t, color="B9CCD3", size="6")
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

def set_page_field(paragraph):
    run = paragraph.add_run()
    fldChar1 = OxmlElement("w:fldChar")
    fldChar1.set(qn("w:fldCharType"), "begin")
    instrText = OxmlElement("w:instrText")
    instrText.set(qn("xml:space"), "preserve")
    instrText.text = " PAGE "
    fldChar2 = OxmlElement("w:fldChar")
    fldChar2.set(qn("w:fldCharType"), "end")
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)
    set_run(run, size=8.5, color=MUTED)

def add_page_break(doc):
    doc.add_page_break()

def build_document():
    doc = Document()
    sec = doc.sections[0]
    sec.page_width = Inches(8.27)
    sec.page_height = Inches(11.69)
    sec.top_margin = Inches(0.68)
    sec.bottom_margin = Inches(0.65)
    sec.left_margin = Inches(0.70)
    sec.right_margin = Inches(0.70)
    sec.header_distance = Inches(0.30)
    sec.footer_distance = Inches(0.30)

    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    normal.font.size = Pt(10.5)
    normal.font.color.rgb = RGBColor.from_string(INK)
    normal.paragraph_format.space_after = Pt(5)
    for style_name in ("Title", "Heading 1", "Heading 2"):
        st = doc.styles[style_name]
        st.font.name = FONT
        st._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    doc.styles["Title"].font.size = Pt(22)
    doc.styles["Title"].font.bold = True
    doc.styles["Title"].font.color.rgb = RGBColor.from_string(NAVY)

    header = sec.header.paragraphs[0]
    header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    header.paragraph_format.space_after = Pt(0)
    set_run(header.add_run("SAMPLE / SYNTHETIC  •  文件 0041  •  I09-E01  •  官方方框 042"), size=8.5, bold=True, color=RED)
    footer = sec.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_run(footer.add_run("示範計畫，非協會已執行或核准紀錄  |  第 "), size=8.3, color=MUTED)
    set_page_field(footer)
    set_run(footer.add_run(" 頁"), size=8.3, color=MUTED)

    p = doc.add_paragraph(style="Title")
    p.paragraph_format.space_after = Pt(2)
    p.add_run("課程規劃書與各方意見採納方案")
    add_p(doc, "屏東縣原始點關懷協會適用情境示例｜DOCX 0041｜I09-E01｜官方佐證表方框 042", size=10.5, bold=True, color=TEAL, after=6)
    callout(doc, "資料界線", "全文課名、意見、角色代碼、日期、設計評分、時數、門檻及示範分數皆為 SAMPLE / SYNTHETIC。這是可供行政志工改寫的課程規劃示例，不代表協會已諮詢、開課、核准或取得任何成效。法人資料、現行權限、師資資格、經費及真實課程仍須以可核對原件確認。", fill="FCEFED")

    heading(doc, "這份計畫供誰在何時使用", 1)
    add_p(doc, "課程承辦志工或兼任工作人員在提出新課程、改版或安排試辦前，使用本計畫把四類意見轉成可追溯的課程設計。先確認來源與適用範圍，再比較設計選項、排定單元、設定評量，最後記錄採納、調整、暫緩或不採納的理由。")
    add_table(doc, ["快速辨識", "本示例內容"], [
        ["用途與輸出", "一份含需求、四方意見、課程安排、評量門檻、責任及變更理由的課程計畫。"],
        ["服務情境", "健康知能說明與安全轉介溝通；不包含診斷、治療或未經證實的專業資格。"],
        ["使用者", "課程承辦志工、講師及受託用人單位聯絡角色；實際姓名與授權尚待查驗。"],
        ["工作產品界線", "0041 說明課程如何設計並納入意見；0039 保存規劃會議的討論與決議；0042 保存參與過程證據；0040 對照評量方法與成效指標。"],
    ], [1.25, 5.55])
    callout(doc, "官方要求", "「課程規劃書（能顯示包含講師、行政、企業學員、用人之主管之意見納入課程設計與審查之考量）。」官方查核佐證表第 3 頁；來源 PDF SHA-256 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709。")
    add_p(doc, "本例中的企業學員是假設由用人單位派訓的在職學員；實際雇主、職務及名單均 UNKNOWN。四類意見都是合成視角，每筆沿著「意見 → 判讀 → 設計決定 → 課程位置 → 後續檢查」追蹤，不是真實訪談。", size=9.8, color=MUTED)
    add_page_break(doc)

    heading(doc, "1｜使用步驟、範圍與停止條件", 1)
    add_p(doc, "建議由一位承辦人維護同一份計畫與一份意見追蹤表。每次收到新意見時只新增一列，保留原始來源位置與決定理由，避免志工重複抄寫或把意見誤寫成共識。")
    add_table(doc, ["步驟", "承辦人要做的事", "留下的可查輸出"], [
        ["1. 確認需求", "界定服務情境、學習者、工作任務及不處理的事項；未知欄位標示待查。", "需求摘要、來源代碼、限制。"],
        ["2. 向四方詢問", "分別取得講師、行政、企業學員、用人主管的意見；記錄未回覆或不適用的原因。", "每一筆意見的角色、時間、方式及來源定位。"],
        ["3. 比較方案", "依同一組準則評估不同課程設計，不以職稱或多數票取代理由。", "權重、各案分數、計算及取捨。"],
        ["4. 形成課程", "把可採意見落到目標、單元、方法、材料、時數、環境或評量。", "課程計畫與意見—設計對照。"],
        ["5. 審查與修訂", "核對異議、未決事項、風險及授權；更新版次與責任。", "修訂紀錄、待辦及核定來源。"],
    ], [0.82, 3.7, 2.28])
    heading(doc, "本示例資料狀態", 2)
    add_table(doc, ["項目", "本件標示", "轉為真實計畫前的查證"], [
        ["協會名稱", "依使用者提供之名稱；本件未獨立驗證法人資料。", "核對有效立案文件及正式名稱。"],
        ["人力安排", "採低人力、志工與兼任工作情境作示例；不宣稱為現況組織圖。", "查現行分工、可投入時數與代理安排。"],
        ["課名、企業學員及意見", "全為合成示例；沒有真實諮詢或開課證據。", "取得授權後記錄實際需求、回應及來源。"],
        ["企業學員類別", "SAMPLE：假設由用人單位派訓；實際雇主、職務與名單 UNKNOWN。", "正式使用前取得用人單位及派訓/職務資料。"],
        ["簽核與預算", "UNKNOWN；沒有填入真實簽核人或金額。", "依章程、授權文件、報價及實際核定補證。"],
    ], [1.15, 2.75, 2.9])
    callout(doc, "暫停條件", "只要四方中有一方尚未回覆、無法適用或來源不明，就標示缺口及責任人；不得寫成「各方均同意」。若課程內容越過健康教育界線、含未證實療效或無法確認講師資格，停止該部分並交由有權者查證。", fill="FFF5E7")
    add_page_break(doc)

    heading(doc, "2｜需求與四方意見示範", 1)
    add_p(doc, "案例代碼 SYN-I09E01-PLAN-01。以下四列是為示範紀錄方法而寫的合成視角，每類各一筆，不是訪談、簽到或實際意見統計。")
    add_table(doc, ["合成來源與問題", "示範意見及需求", "判讀與設計採納"], [
        ["SYN-VOICE-TCH-01｜講師\n問：學員須做出什麼可觀察行為？", "講解時間不宜過長；需要示範如何先詢問同意，再以簡短語句說明可提供的資訊與轉介界線。", "採納。安排示範、兩輪情境演練及四項量尺；講師資格與實際可授課時數仍待查。"],
        ["SYN-VOICE-ADM-01｜行政\n問：志工能維持哪些教材與紀錄？", "希望單一紙本名冊、單張流程卡和一份回饋表；避免多套系統、重複輸入及大型會議程序。", "採納。規劃紙本卡及一份匿名代碼追蹤表；實際個資保存位置與權限待協會確認。"],
        ["SYN-VOICE-LRN-01｜企業學員（合成）\n問：練習怎樣才容易參與？", "偏好白話短句和先看示範再練習；希望案例不要求分享自己的服務對象資料。", "採納並設界線。用虛構案例、三人一組及大字流程卡；不蒐集真實個案資料。"],
        ["SYN-VOICE-SUP-01｜用人主管\n問：如何辨識何時停止並轉介？", "需要清楚的停止訊號、同意確認和最少必要交接資訊，避免志工自行判斷或承諾處理。", "採納。加入停止／轉介判斷卡與交接欄位；真實機構流程、聯絡窗口及法定界線必須由主管來源核實。"],
    ], [1.7, 2.65, 2.45], font=9.3)
    heading(doc, "示範需求綜整", 2)
    add_table(doc, ["需求主題", "合成依據", "課程設計回應", "驗證方式"], [
        ["能做而非只聽", "講師視角 SYN-VOICE-TCH-01", "短講後接示範與兩輪演練。", "觀察量尺至少 9/12 且關鍵項達門檻。"],
        ["低維護負擔", "行政視角 SYN-VOICE-ADM-01", "單一紙本卡、單一追蹤表；不另建系統。", "課前由一位承辦人以 10 分鐘完成材料核對。"],
        ["保護服務對象", "企業學員視角 SYN-VOICE-LRN-01", "全程使用虛構案例，不要求提供真人資料。", "教材檢查無個資與未授權個案。"],
        ["安全交接", "主管視角 SYN-VOICE-SUP-01", "明列停下、說明選項、取得同意及交接。", "情境演練檢查同意、界線、轉介三個關鍵項。"],
    ], [1.15, 1.55, 2.25, 1.85])
    callout(doc, "不作的推論", "一筆合成視角不能代表群體意見或真實需要。實際計畫必須記錄缺席、不同意、未回覆及來源限制；不得把沉默視為認同。")

    heading(doc, "3｜課程設計方案比較", 1)
    add_p(doc, "為了讓承辦人看見取捨，本示例用五項同一量尺比較三種方案。分數為 1 至 5 分，5 分最符合；「行政負擔」分數越高代表越容易維持。權重與分數均為合成規劃假設。")
    add_table(doc, ["準則", "權重", "A 單向講授", "B 示範＋情境演練", "C 自主線上教材"], [
        ["可觀察實作", "35%", "1", "4", "2"],
        ["四方需求配適", "25%", "3", "4", "2"],
        ["低行政負擔", "20%", "5", "4", "3"],
        ["低科技門檻", "10%", "5", "5", "2"],
        ["評量可追溯", "10%", "3", "4", "3"],
        ["加權總分", "100%", "2.90", "4.10", "2.30"],
    ], [1.55, 0.72, 1.45, 1.68, 1.4])
    add_p(doc, "計算：方案分數＝Σ（各準則分數 × 權重）。B＝4×0.35＋4×0.25＋4×0.20＋5×0.10＋4×0.10＝4.10；A＝2.90；C＝2.30。權重總和＝0.35＋0.25＋0.20＋0.10＋0.10＝1.00。")
    heading(doc, "示範取捨", 2)
    add_p(doc, "選擇 B「短講、示範、紙本情境演練、結構化回饋」。它的分數不是協會核定決定；在示範比較中，B以4.10分最高，且同時回應講師要觀察行為、學員要先看示範、主管要確認交接界線。行政便利性略低於純講授，因此把材料限制為一張流程卡、一份量尺和一張回饋表。")
    add_table(doc, ["方案", "適用情況", "限制與不選原因"], [
        ["A 單向講授", "只能在時間極短且已有熟練者時作補充。", "實作證據弱，難觀察同意、界線與交接行為。"],
        ["B 示範＋演練", "本示例的首選；小組能輪流扮演服務者、觀察者及情境角色。", "需要講師回饋；若無合格講師或足夠觀察資源，先縮小班額或暫停。"],
        ["C 自主線上教材", "可作課前補充，不單獨替代演練。", "對設備及自主管理要求較高，且無法直接觀察關鍵行為。"],
    ], [1.25, 2.7, 2.85])
    callout(doc, "重新評分時", "若真實學員無法使用設備、講師時數不足或主管流程不同，先更新權重理由與分數，再重算總分；保留前版，不改寫成早已選定。")

    heading(doc, "4｜課程目標、對象與單元設計", 1)
    add_table(doc, ["計畫欄位", "SAMPLE / SYNTHETIC 內容"], [
        ["課程名稱", "社區健康知能說明與安全轉介溝通。示例名稱，不代表協會已開辦。"],
        ["適用對象", "SAMPLE：假設由用人單位派訓企業學員，情境為社區接待與健康知能說明。真實單位、職務及名單 UNKNOWN；正式版須由用人主管核實。"],
        ["先備條件", "能閱讀繁體中文短句；不以醫療或推拿證照作入班假設。實際條件依課程核准及講師資格核實。"],
        ["班額規劃", "示例上限 8 人／一位講師；若超過 8 人，須確認第二位合格觀察者及場地後再編班。這是設計假設，不是協會現行人力。"],
        ["學習目的", "在非醫療社區服務情境中，以尊重、同意、界線和轉介資訊完成基本溝通；不作診斷、處置或療效承諾。"],
    ], [1.35, 5.45])
    add_table(doc, ["可觀察目標", "教學活動", "評量與合格判準"], [
        ["辨認服務範圍，能說明何時停止自行回應。", "看示範後分析兩個虛構情境。", "量尺「角色界線」至少 2 級。"],
        ["在記錄或轉介前先確認同意並只記錄必要內容。", "同意與隱私情境卡，兩人互演。", "量尺「同意與最少必要資訊」至少 2 級。"],
        ["遇到超出服務範圍的情況，停止並依真實流程轉介。", "使用停止／轉介卡辨識情境。", "量尺「轉介判斷」至少 2 級。"],
        ["以清楚短句完成交接，讓下一位知道需求與下一步。", "三欄交接卡演練及同儕回饋。", "總分至少 9/12，並符合三項關鍵門檻。"],
    ], [2.1, 2.35, 2.35])
    add_page_break(doc)

    heading(doc, "5｜時程、教學方法與所需資源", 1)
    add_p(doc, "示例安排 215 分鐘有效學習及 10 分鐘休息；總時段 225 分鐘，09:00 至 12:45。日期、場地、講師及服務流程未核實前，不得作為正式開課通知。")
    add_table(doc, ["時段", "分鐘", "單元與做法", "意見如何反映"], [
        ["09:00–09:20", "20", "說明學習目標、服務角色與停止界線；先看虛構情境。", "企業學員要先看示範；主管要求界線清楚。"],
        ["09:20–10:00", "40", "練習傾聽、澄清需求及用白話重述；講師示範一次。", "講師建議練習可觀察；企業學員偏好短句。"],
        ["10:00–10:10", "10", "休息；紙本材料留在桌面，不收集個案資料。", "行政要求簡單、不用額外系統。"],
        ["10:10–11:05", "55", "同意、隱私與轉介判斷；包含 15 分鐘重點補練。", "示範評量暴露同意項弱點後，計畫加長 15 分鐘；此為合成設計修訂。"],
        ["11:05–12:00", "55", "兩輪三人情境演練：服務者、觀察者、情境角色輪換。", "主管意見落到停止／轉介；企業學員不需帶入真人案例。"],
        ["12:00–12:25", "25", "以四欄交接卡完成交接；觀察者按量尺回饋。", "用人主管要求交接資訊完整且最少必要。"],
        ["12:25–12:45", "20", "個別情境評量、回饋與下一步說明。", "行政可用一張紙本量尺彙整，不另建複雜系統。"],
    ], [1.05, 0.55, 2.85, 2.35], font=9.3)
    add_p(doc, "時數核對：20＋40＋10＋55＋55＋25＋20＝225 分鐘；休息 10 分鐘，實際教學 215 分鐘。")
    heading(doc, "師資、材料與環境", 2)
    add_table(doc, ["面向", "最低可執行安排", "開課前查核"], [
        ["師資", "一位具備該課程內容能力的講師；班額示例上限 8 人。", "查資格、可授課時數、教材來源與授權。缺證不得寫已聘任。"],
        ["行政", "一位承辦志工準備紙本卡、出席方式及材料；如無人手，縮小或延期。", "確認真實分工、代理人及資料保管權限。"],
        ["教材", "情境卡、四項評分量尺、單頁流程卡、可重用筆與計時器。", "逐頁查核不含真實個資、未授權個案或療效說法。"],
        ["環境", "可移動座椅，三人一組；提供大字版及休息安排。", "先確認場地可近用、隱私、噪音、安全及實際費用。"],
    ], [0.95, 2.75, 3.1])
    add_page_break(doc)

    heading(doc, "6｜意見採納與課程修訂追蹤", 1)
    add_p(doc, "追蹤列的狀態使用「採納、調整後採納、暫緩、未採納、待查」。理由須指出對課程哪一部分造成影響；未採納的意見也保留，避免只留下支持方案的聲音。")
    add_table(doc, ["意見來源", "決定與理由", "實際落到的計畫內容", "後續確認"], [
        ["SYN-VOICE-TCH-01 講師", "調整後採納：保留必要說明，將多數時段改為可觀察演練。", "單元 2、4、評量量尺；情境演練 55 分鐘。", "確認真實講師能示範並提供回饋；無資格資料則暫停授課安排。"],
        ["SYN-VOICE-ADM-01 行政", "採納：以紙本和單一追蹤表降低維護負擔。", "材料清單、責任表與樣本資料保管方式。", "確認實際人力、個資保管位置和代理。"],
        ["SYN-VOICE-LRN-01 企業學員", "調整後採納：保留真實感，但不用真人服務案例。", "全程使用合成案例；提供大字卡和短句。", "開課前做教材無障礙與隱私檢視。"],
        ["SYN-VOICE-SUP-01 用人主管", "採納：把停止與轉介觸發條件寫進演練。", "單元 3、情境卡、關鍵評量門檻。", "取得真實服務單位的轉介窗口與授權規則後再定稿。"],
        ["合成試評發現 SYN-CAL-03/04", "採納為設計修訂：合成試評的同意項低於門檻，增加 15 分鐘補練。", "單元 3 由 40 分鐘增至 55 分鐘；全程有效學習時數增至 215 分鐘。", "此為紙上設計演練，不是開課結果；正式試辦後仍須以真實評量重檢。"],
    ], [1.35, 1.85, 1.85, 1.75], font=9.2)
    heading(doc, "修訂軌跡", 2)
    add_table(doc, ["版本", "變更", "依據", "狀態"], [
        ["示範草案 0.1", "課程構想 200 分鐘有效教學；尚未檢查評量門檻。", "合成意見 SYN-VOICE-*。", "僅為合成前版，未核定。"],
        ["示範版 R01", "把同意與轉介練習增加 15 分鐘；課程改為 215 分鐘有效學習。", "合成試評 SYN-CAL-03/04 未達關鍵門檻。", "本件 DOCX 候選；未核定、未執行。"],
    ], [1.05, 2.5, 2.1, 1.15])
    callout(doc, "紀錄要求", "正式版需另有來源定位，例如受訪紀錄編號、日期、頁碼或經授權的訊息索引。課程計畫摘要意見與設計決定；出席、逐字討論、核准或認同依其正式記錄文件保存。")
    add_page_break(doc)

    heading(doc, "7｜評量設計與合成判讀示例", 1)
    add_p(doc, "評量只檢查本課程教過的行為，不把滿意度或主觀自評當成能力證明。正式使用時由經確認有能力的人依一致量尺觀察；若無合格評量者，先暫停評量安排。")
    add_table(doc, ["項目", "0｜未展現", "1｜需大量提示", "2｜可獨立完成", "3｜清楚且穩定"], [
        ["角色界線", "承諾診斷、治療或超出角色的服務。", "知道有限制，但未能停下或說明。", "能說明可做範圍並在越界時停止。", "能清楚說明界線及下一步選項。"],
        ["同意與隱私", "未詢問同意即記錄或轉述。", "有詢問但內容不清，或收集過多資料。", "先詢問同意，只記錄必要內容。", "能再次確認用途、對象及安全交接方式。"],
        ["轉介判斷", "忽略停止訊號或自行處置。", "辨識疑慮但不清楚如何停止。", "依已核實流程停止並轉交有權窗口。", "能簡潔說明選項並確認交接責任。"],
        ["交接表達", "沒有交接或提供錯誤承諾。", "資訊零散，下一步不明。", "說清需求、已取得同意、已做事項及下一步。", "簡短、準確、符合最少必要原則。"],
    ], [1.05, 1.33, 1.36, 1.5, 1.36], font=8.9)
    add_p(doc, "合格規則：四項合計至少 9/12，且「角色界線、同意與隱私、轉介判斷」各至少 2 級。未達者先給具體回饋，再安排一次不同情境的補練；不得把補練分數改寫成原測通過。")
    add_table(doc, ["合成代碼", "界線", "同意", "轉介", "交接", "總分", "判讀"], [
        ["SYN-CAL-01", "3", "2", "2", "2", "9/12", "達門檻"],
        ["SYN-CAL-02", "3", "3", "3", "2", "11/12", "達門檻"],
        ["SYN-CAL-03", "2", "2", "1", "3", "8/12", "未達：轉介 1 級"],
        ["SYN-CAL-04", "3", "1", "3", "2", "9/12", "未達：同意 1 級"],
    ], [1.12, 0.72, 0.72, 0.72, 0.72, 0.83, 1.35])
    add_p(doc, "示範計算：符合門檻 2 人 ÷ 合成校準列 4 人＝50%。假設規劃目標為至少 75%，則 50%＜75%，觸發重新設計同意與轉介練習。分母只有 4 筆紙上合成校準，不代表任何學員、班次或協會成果，不能外推。")
    callout(doc, "評量限制", "校準列用來檢查量尺能否分辨達標與缺口。正式開課後另記有效受評人數、缺考/退出、補練情況及資料來源；沒有真實原始評量表就不得宣稱通過率。", fill="FFF5E7")
    add_page_break(doc)

    heading(doc, "8｜承辦、審查與檢討安排", 1)
    add_table(doc, ["時點", "承辦角色", "確認事項", "停止或改版條件"], [
        ["設計前", "課程承辦志工（角色代碼待實際指派）", "查需求來源、四方意見可取得性、服務界線及講師來源。", "任一必要來源未取得即標示缺口，不寫成已諮詢。"],
        ["課程草案", "承辦人與講師", "核對目標—活動—評量、時數、教材及場地。", "目標沒有可觀察判準或評量不測目標時，退回調整。"],
        ["主管檢視", "用人單位聯絡角色；正式授權 UNKNOWN", "確認工作情境、轉介流程、個資與可執行資源。", "轉介窗口、服務界線或授權未核實，不排定正式試辦。"],
        ["正式核定前", "依章程及授權文件確認之人", "確認版本、日期、資源、風險與簽核權。", "沒有真實核定原件時，狀態維持草案。"],
        ["試辦後", "承辦人與評量者", "以真實出席、評量、回饋與偏差紀錄檢查設計。", "關鍵安全項目未達、資料不完整或有未處理事件時，暫停下一班。"],
    ], [1.0, 1.45, 2.55, 2.0])
    heading(doc, "低負擔責任配置", 2)
    add_table(doc, ["工作", "主責角色（示例代碼）", "備援／交接", "不得假設"], [
        ["彙整四方意見與版次", "SYN-ROLE-COORD", "指定一位可接手的行政志工。", "不假設已有專責訓練部門。"],
        ["課程教學與評量", "SYN-ROLE-TRAINER", "需先核對實際資格；無合格替補則縮班或延期。", "不由身分稱謂推定證照或資格。"],
        ["用人情境檢視", "SYN-ROLE-SUPERVISOR", "待真實單位指派；無回覆則保留缺口。", "不把合成主管角色當作實際核定者。"],
        ["個資及資料保管", "依正式授權文件指定", "最少必要存取；離任時完成移交。", "不預設使用特定雲端、系統或法定權限。"],
    ], [1.65, 1.65, 2.15, 1.55])
    heading(doc, "必須退回或暫停的情形", 2)
    add_bullets(doc, [
        "講師、行政、學員或用人主管意見缺失，且未記錄未取得原因與補查責任。",
        "有支持與反對意見，計畫沒有說明採納、調整、暫緩或不採納理由。",
        "單元時間、師資、班額、場地或教材無法由可用資源支持。",
        "課程或教材出現診斷、治療、保證療效、無來源資格或超出核准範圍的宣稱。",
        "評量沒有對應學習目標，或合格規則不能由評分表重算。",
        "樣本人物、出席、同意、核准、金額、課程或結果看起來像真實紀錄但沒有原件。",
    ], size=9.7)
    heading(doc, "附錄 A｜可直接使用的意見記錄表", 1)
    add_p(doc, "以下欄位可在實際諮詢時複製到同一份課程計畫。空白欄是工具欄位；本件前文已提供四類完整合成填寫示例，不能把空欄當成已取得意見。")
    add_table(doc, ["記錄欄", "每筆必填內容", "示範填寫"], [
        ["來源識別", "意見編號、日期、方式、角色代碼、記錄者。", "SYN-VOICE-LRN-01；SAMPLE 日期代碼 S-03（非日曆日期）；企業學員角色代碼。"],
        ["原意摘要", "對方希望課程解決什麼；保留不同意見及未回覆狀態。", "希望先看示範；不使用真人服務案例。"],
        ["判讀與決定", "採納／調整／暫緩／未採納；理由與影響。", "調整後採納；保留情境練習，全部改用虛構案例。"],
        ["課程位置", "計畫章節、單元、材料、時數或評量欄。", "單元 4 情境演練；教材使用合成情境卡。"],
        ["查核與保存", "後續驗證、責任角色、原始紀錄定位、權限及保存位置。", "正式版需填真實來源與可核查定位；本列是示例，無原始訪談。"],
    ], [1.0, 3.0, 3.0])
    heading(doc, "空白意見記錄表｜每位對象各填一份", 2)
    callout(doc, "填寫方式", "講師、行政、企業學員及用人主管各自記錄；未回覆、不同意或不適用也要說明原因。空白不等於同意；原始紀錄定位及權限欄必填後才能結案。", fill="EAF3F5")
    add_table(doc, ["記錄欄", "填寫內容", "記錄欄", "填寫內容"], [
        ["意見編號／角色代碼", "", "日期／方式／記錄者", ""],
        ["原意摘要／需求", "", "不同意／未回覆及原因", ""],
        ["判讀（採納／調整／暫緩／未採納）", "", "決定理由及影響", ""],
        ["課程單元／教材／評量位置", "", "後續責任人／期限", ""],
        ["原始文件／頁碼／定位", "", "同意、個資權限及保存處", ""],
    ], [1.65, 1.7, 1.55, 1.9])
    heading(doc, "實際諮詢提問", 2)
    add_table(doc, ["對象", "可直接詢問的問題", "記錄要點"], [
        ["講師", "學員結束時要能做出什麼？哪個常見錯誤需先演示？", "可觀察行為、所需教材、講師資格與回饋方式。"],
        ["行政", "哪幾份材料能準備並保存？哪些步驟會造成重複工作？", "負擔、權限、保存、代理及實際成本來源。"],
        ["企業學員", "哪種說明方式易懂？哪些練習情境安全且有用？", "理解度、可近用性、隱私偏好及未答項。"],
        ["用人主管", "工作中何時應停止？應交給誰？哪些資訊最少且足夠？", "真實流程、權限、轉介窗口及可公開範圍。"],
    ], [1.05, 3.2, 2.75])

    heading(doc, "附錄 B｜換填清單、文件交接與來源", 1)
    add_p(doc, "將示例轉成正式計畫時，先把合成資料與真實來源逐項比對。更換一個來源或門檻後，同步檢查課程時數、單元、責任、評量、分母及相關追蹤表。完整 fact_id 清冊隨文件附上。")
    add_table(doc, ["示例資料", "應取得的真實材料", "換填與複核"], [
        ["四方意見與不同立場", "經授權的訪談、課前諮詢、回覆或審查紀錄；包含未回覆情況。", "保留來源定位；更新意見決定列及教材/單元。"],
        ["課程需求與服務界線", "有效課程需求、服務流程、主管確認及可靠的專業來源。", "檢查課程名稱、學習目標、停止條件及案例。"],
        ["師資與場地", "真實資格、可用時數、場地、安全與無障礙資訊。", "調整班額、方法、時程與材料，不以示例假設替代。"],
        ["分數、權重、門檻及比率", "依實際授權形成的準則、評量原件及有效樣本母體。", "重算所有總分、通過率、分母、四捨五入及觸發條件。"],
        ["核准、日期、預算與執行", "有效授權、會議/簽核原件、報價、出席與評量原始資料。", "沒有原件前維持草案，不填成已核准或已完成。"],
    ], [1.6, 2.75, 2.65])
    heading(doc, "相關文件的交接關係", 2)
    add_table(doc, ["文件", "分工", "交接規則"], [
        ["0039｜I08-E03", "課程規劃與設計審查會議紀錄。", "本計畫可供會議討論；會議時間、發言、決議、責任與期限另由該紀錄保存。"],
        ["0040｜I08-E03", "訓練評估方法與成效指標對照表。", "本計畫描述課程目標與評量安排；指標定義與成效資料欄位由矩陣核對。"],
        ["0042｜I09-E02", "利害關係人參與及作業流程相關證據。", "本計畫列入意見及來源代碼；實際出席、發言、同意、核准或支持須由真實來源記錄。"],
    ], [1.5, 2.0, 3.5])
    heading(doc, "來源與版本", 2)
    add_bullets(doc, [
        "官方《常見參考佐證資料》查核表，指標 9，頁 3；本件要求原文見首頁。來源 PDF SHA-256：805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709。",
        "TTQS ONE 品質施工契約 03《157 方框 Unique Blueprint》：DOCX 0041 / I09-E01 / 官方方框 042；本件使用的 Blueprint 原始列 SHA-256：224c44a03cfc975b6f5a85e18bedb63536ea2f94bfdc076f1730c97453b13287。",
        "原始點協會情境：使用者提供的協會背景要求只用來設計低人力、志工可維護的示例；協會法人文件、現行組織、真實課程、師資、預算及成效未由本件獨立核實。",
        "文件狀態：SAMPLE / SYNTHETIC 候選；尚未取得真實諮詢原件、正式核定、執行結果或協會接受。",
    ], size=9.4)
    add_p(doc, "文檔識別：0041 R03｜要求 I09-E01｜官方方框 042｜案例 SYN-I09E01-PLAN-01｜草案，不代表已核准方案。", size=9.3, bold=True, color=TEAL, before=7, after=0)
    doc.core_properties.title = "課程規劃書與各方意見採納方案"
    doc.core_properties.subject = "DOCX 0041 / I09-E01 / 官方方框 042"
    doc.core_properties.author = ""
    doc.core_properties.keywords = "SAMPLE; SYNTHETIC; TTQS; I09-E01"
    doc.save(OUT)

def write_register():
    rows = [
        ("SYN-CASE-001","示例案例代碼","SYN-I09E01-PLAN-01","首頁/全篇","合成案例識別","需以實際課程唯一代碼替換"),
        ("CTX-NAME-001","機構名稱","社團法人屏東縣原始點關懷協會","首頁/來源與版本","使用者提供名稱；未獨立驗證法人資料","立案證明及正式名稱"),
        ("SYN-COURSE-001","示例課名","社區健康知能說明與安全轉介溝通","首頁/表格","假設課程；未證實協會曾開設","核定課程計畫與課程代碼"),
        ("SYN-BOUNDARY-001","課程界線","不含診斷、治療、療效或未證資格主張","首頁/課程目標","示例安全界線，不代表正式制度","章程、服務範圍及專業審查來源"),
        ("SYN-VOICE-TCH-01","講師意見","短講、示範、兩輪可觀察練習","第2節/追蹤表","虛構視角，不是真實訪談","經授權訪談/課前回覆及日期"),
        ("SYN-VOICE-ADM-01","行政意見","單張流程卡、單一追蹤表、低維護負擔","第2節/追蹤表","虛構視角，不是真實行政回饋","實際承辦人訪談及保存權限"),
        ("SYN-VOICE-LRN-01","學員意見","白話、先看示範、不提供真人個案資料","第2節/追蹤表","虛構視角，不是真實學員回覆","真實學員諮詢和個資同意紀錄"),
        ("SYN-VOICE-SUP-01","用人主管意見","清楚停止訊號、同意、最少必要交接","第2節/追蹤表","虛構視角，不是真實雇主/主管意見","真實服務單位回覆及授權流程"),
        ("SYN-OPTION-WEIGHTS","設計比較權重","35/25/20/10/10 percent","第3節","合成權重，合計100%","經授權的方案評估規準"),
        ("SYN-OPTION-A","方案A評分","1/3/5/5/3；加權2.90","第3節","合成評分，非實際評選結果","評估者原始分數及理由"),
        ("SYN-OPTION-B","方案B評分","4/4/4/5/4；加權4.10","第3節","合成評分，非協會已核定方案","正式比較表及決策紀錄"),
        ("SYN-OPTION-C","方案C評分","2/2/3/2/3；加權2.30","第3節","合成評分，非實際決策","評估者原始分數及理由"),
        ("SYN-CLASS-001","班額假設","每位講師最多8人；超過須有第二觀察角色","第4節","設計假設，非現行員額","講師資格、人力、場地與風險評估"),
        ("SYN-DURATION-001","有效教學時間","215分鐘","第5節/附錄","合成課程時數","正式課程核定表"),
        ("SYN-BREAK-001","休息時間","10分鐘；總時段225分鐘","第5節/附錄","合成時間安排","正式課程核定表"),
        ("SYN-UNIT-01","單元時數","20分鐘","第5節","合成時間","真實課程計畫與簽核"),
        ("SYN-UNIT-02","單元時數","40分鐘","第5節","合成時間","真實課程計畫與簽核"),
        ("SYN-UNIT-03","單元時數","55分鐘（含15分鐘設計補練）","第5-6節","合成修訂；不是實際課後改善","核准修訂及真實評量結果"),
        ("SYN-UNIT-04","單元時數","55分鐘","第5節","合成時間","真實課程計畫與簽核"),
        ("SYN-UNIT-05","單元時數","25分鐘","第5節","合成時間","真實課程計畫與簽核"),
        ("SYN-UNIT-06","單元時數","20分鐘","第5節","合成時間","真實課程計畫與簽核"),
        ("SYN-RUBRIC-001","評量量尺","4項各0至3級；滿分12","第7節","合成量尺","核准評量工具與版本"),
        ("SYN-PASS-001","合格門檻","總分至少9/12且3關鍵項各至少2","第7節","合成門檻，不代表機構政策","正式核定的評量標準"),
        ("SYN-CAL-01","校準列1","3/2/2/2=9；達門檻","第7節","合成評分列","真實評分原表及評量者"),
        ("SYN-CAL-02","校準列2","3/3/3/2=11；達門檻","第7節","合成評分列","真實評分原表及評量者"),
        ("SYN-CAL-03","校準列3","2/2/1/3=8；轉介項未達","第7節","合成評分列","真實評分原表及評量者"),
        ("SYN-CAL-04","校準列4","3/1/3/2=9；同意項未達","第7節","合成評分列","真實評分原表及評量者"),
        ("SYN-TARGET-001","規劃觸發目標","至少75%符合合格規則","第7節","示範規劃門檻，非協會核定值","正式核定課程KPI及樣本母體"),
        ("SYN-RATE-001","示範比率","2/4=50%；低於75%觸發設計檢討","第7節","4筆校準列，不是真實學員成果","有效受評名冊、原始量尺及期間"),
        ("SYN-REVISION-001","設計修訂","同意/轉介單元增加15分鐘；有效教學200→215分鐘","第5-6節","紙上設計演練，非真實試辦改善","核准版本、修訂紀錄及實際時數"),
        ("SYN-ROLE-COORD","承辦角色","課程承辦志工","第8節","角色代碼/示例，不是已指派人員","實際工作分派及代理紀錄"),
        ("SYN-ROLE-TRAINER","師資角色","課程講師","第8節","角色示例；資格UNKNOWN","真實資格、聘用或授權資料"),
        ("SYN-ROLE-SUPERVISOR","用人角色","用人單位聯絡/主管","第8節","角色示例；不是實際核定者","真實聯絡窗口與權限來源"),
        ("SYN-MATERIAL-001","教材資源","紙本情境卡、量尺、單頁流程卡、筆、計時器","第5節","低成本方案假設；無實際採購","實際教材版次、報價/採購與授權"),
        ("SYN-VENUE-001","場地假設","可移動座椅、可近用且可保護討論隱私","第5節","未指定真實地點或現況","場勘、無障礙與安全資料"),
        ("SYN-STATUS-001","課程狀態","未核定、未執行","首頁/全篇","事實界線：本文件為候選示例","有效核定、開課與成效原件"),
        ("CTX-OP-MODEL-001","協會作業情境","低人力、志工/兼任可維護流程","首頁/第1節/來源","使用者指示的設計假設，不是已核實現況","核對現行人力、分工及可投入時數"),
        ("SYN-LEARNER-CATEGORY-001","企業學員類別","假設由用人單位派訓企業學員；實際單位、職務及名單 UNKNOWN","第2及4節","SAMPLE/SYNTHETIC 情境，不代表真實任職或派訓","用人單位資料、派訓來源與實際工作任務"),
        ("SYN-EXERCISE-001","演練人數與輪次","三人角色輪替、兩輪情境演練","第2及5節","合成教學設計","真實班額、學員數與授課安排"),
        ("SYN-ADMIN-CHECK-001","備課時間估計","一位承辦人10分鐘完成材料核對","第2節/示範需求綜整","合成負擔估計，不是實測","實際承辦人計時與材料清單"),
        ("SYN-SAMPLE-DATE-001","示範日期代碼","S-03，非日曆日期","附錄A/示範填寫","純示範識別碼，不表示已諮詢日期","真實諮詢日期及原始紀錄"),
        ("SYN-SCHEDULE-CLOCK-001","課程時段","09:00至12:45","第5節","合成排程假設","正式核定日期、場地與出席通知"),
        ("SYN-HANDOFF-001","交接練習卡","四欄交接卡","第4至5節","合成教材設計","實際核准教材版本及使用授權"),
    ]
    with REGISTER.open("w",encoding="utf-8-sig",newline="") as f:
        w=csv.writer(f)
        w.writerow(["fact_id","欄位","示例值","文件定位","狀態與來源界線","升格REAL前取得"])
        w.writerows(rows)

if __name__ == "__main__":
    build_document()
    write_register()
    print(f"created={OUT}")
    print(f"register={REGISTER}")