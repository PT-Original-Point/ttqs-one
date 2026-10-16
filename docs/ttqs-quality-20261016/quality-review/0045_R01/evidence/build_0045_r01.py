from pathlib import Path
from datetime import datetime, timezone
from decimal import Decimal
import csv, hashlib, json, zipfile
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

REPO=Path(r"E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016")
PKG=REPO/"docs/ttqs-quality-20261016/quality-review/0045_R01"
RUNTIME=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME")
DOCX=PKG/"candidate/0045_R01.docx"
BLUEPRINT_IN=REPO/"docs/ttqs-quality-20261016/quality-review/0044_R01/inputs/BLUEPRINT_0044_AND_NEIGHBORS.jsonl"
BLUEPRINT_OUT=PKG/"inputs/BLUEPRINT_0045_AND_NEIGHBORS.jsonl"
BLUEPRINT_COMMIT="2587613e597904ba0630aa8a48d3bd4c6c3d9c47"
OFFICIAL_PDF=RUNTIME/"SOURCES/DRIVE_READBACKS/DRIVE_OFFICIAL_EVIDENCE_TABLE.pdf"
OFFICIAL_SHA="805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709"
OLD_DOCX=RUNTIME/"WORK/CANDIDATES/0045__訓練資源採購與甄選管理辦法.docx"
OLD_SHA_EXPECTED="aebdeeef7da6944c5bb092f6e23c7f0825357e6866006e32971b3c8d8c81b535"
OLD_REVIEW=RUNTIME/"CONTROL/REVIEWS/0045.json"

def font(run,size=10.5,bold=False,color="202A35"):
    run.font.name="Microsoft JhengHei"
    run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"),"Microsoft JhengHei")
    run.font.size=Pt(size); run.bold=bold; run.font.color.rgb=RGBColor.from_string(color)

def shade(cell,fill):
    pr=cell._tc.get_or_add_tcPr(); node=pr.find(qn("w:shd"))
    if node is None: node=OxmlElement("w:shd"); pr.append(node)
    node.set(qn("w:fill"),fill)

def margins(cell,top=90,start=100,bottom=90,end=100):
    pr=cell._tc.get_or_add_tcPr(); mar=pr.first_child_found_in("w:tcMar")
    if mar is None: mar=OxmlElement("w:tcMar"); pr.append(mar)
    for side,value in (("top",top),("start",start),("bottom",bottom),("end",end)):
        n=mar.find(qn("w:"+side))
        if n is None: n=OxmlElement("w:"+side); mar.append(n)
        n.set(qn("w:w"),str(value)); n.set(qn("w:type"),"dxa")

def table_header(row):
    n=OxmlElement("w:tblHeader"); n.set(qn("w:val"),"true"); row._tr.get_or_add_trPr().append(n)

def no_split(row):
    row._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))

def clear_paragraph_border(ppr):
    if ppr is not None:
        node=ppr.find(qn("w:pBdr"))
        if node is not None: ppr.remove(node)

def page_field(p):
    run=p.add_run(); font(run,8.5,color="5E6873")
    fld=OxmlElement("w:fldSimple"); fld.set(qn("w:instr"),"PAGE"); run._r.addnext(fld)

def para(text,after=5,before=0,style=None):
    p=doc.add_paragraph(style=style); p.paragraph_format.space_before=Pt(before)
    p.paragraph_format.space_after=Pt(after); p.paragraph_format.line_spacing=1.12
    r=p.add_run(text); font(r); return p

def bullet(text):
    p=doc.add_paragraph(style="List Bullet"); p.paragraph_format.space_after=Pt(3)
    p.paragraph_format.line_spacing=1.08; r=p.add_run(text); font(r); return p

def heading(text,level=1):
    p=doc.add_paragraph(style=f"Heading {level}"); p.paragraph_format.keep_with_next=True
    p.paragraph_format.space_before=Pt(11 if level==1 else 7); p.paragraph_format.space_after=Pt(4)
    r=p.add_run(text); font(r,15 if level==1 else 12,True,"000000"); return p

def tab(headers,rows,widths,size=9.5):
    t=doc.add_table(rows=1,cols=len(headers)); t.alignment=WD_TABLE_ALIGNMENT.CENTER
    t.autofit=False; t.style="Table Grid"
    for i,w in enumerate(widths): t.columns[i].width=Inches(w)
    for i,v in enumerate(headers):
        c=t.rows[0].cells[i]; c.text=str(v); c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
        c.width=Inches(widths[i]); shade(c,"244A64"); margins(c)
        for p in c.paragraphs:
            p.paragraph_format.space_after=Pt(0); p.paragraph_format.line_spacing=1.02
            p.paragraph_format.keep_with_next=True
            for r in p.runs: font(r,size,True,"FFFFFF")
    table_header(t.rows[0]); no_split(t.rows[0])
    for values in rows:
        cells=t.add_row().cells; no_split(t.rows[-1])
        for i,v in enumerate(values):
            c=cells[i]; c.text=str(v); c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            c.width=Inches(widths[i]); margins(c)
            for p in c.paragraphs:
                p.paragraph_format.space_after=Pt(0); p.paragraph_format.line_spacing=1.04
                for r in p.runs: font(r,size)
    sp=doc.add_paragraph(); sp.paragraph_format.space_after=Pt(1); sp.paragraph_format.space_before=Pt(1)
    return t

def init_doc():
    for s in doc.sections:
        s.page_width=Inches(8.5); s.page_height=Inches(11)
        s.top_margin=Inches(.68); s.bottom_margin=Inches(.68)
        s.left_margin=Inches(.72); s.right_margin=Inches(.72)
        s.header_distance=Inches(.32); s.footer_distance=Inches(.32)
        h=s.header.paragraphs[0]; h.alignment=WD_ALIGN_PARAGRAPH.RIGHT
        h.paragraph_format.space_after=Pt(0); r=h.add_run("SAMPLE / SYNTHETIC　｜　未生效示範稿"); font(r,8.5,True,"6A737D")
        f=s.footer.paragraphs[0]; f.alignment=WD_ALIGN_PARAGRAPH.CENTER
        r=f.add_run("0045 R01　｜　未經協會正式核定　｜　第 "); font(r,8.5,color="5E6873")
        page_field(f); r=f.add_run(" 頁"); font(r,8.5,color="5E6873")
    normal=doc.styles["Normal"]; normal.font.name="Microsoft JhengHei"
    normal._element.rPr.rFonts.set(qn("w:eastAsia"),"Microsoft JhengHei")
    normal.font.size=Pt(10.5); normal.font.color.rgb=RGBColor.from_string("202A35")
    normal.paragraph_format.space_after=Pt(5); normal.paragraph_format.line_spacing=1.12
    for name in ("Heading 1","Heading 2","Title","Subtitle"):
        st=doc.styles[name]; st.font.name="Microsoft JhengHei"
        st._element.rPr.rFonts.set(qn("w:eastAsia"),"Microsoft JhengHei")
        st.font.color.rgb=RGBColor.from_string("000000")
    clear_paragraph_border(doc.styles["Title"]._element.pPr)
    doc.styles["Heading 1"].font.size=Pt(15); doc.styles["Heading 2"].font.size=Pt(12)
    doc.styles["Title"].font.size=Pt(23); doc.styles["Title"].font.bold=True

PKG.joinpath("candidate").mkdir(parents=True,exist_ok=True)
PKG.joinpath("inputs").mkdir(parents=True,exist_ok=True)
PKG.joinpath("evidence").mkdir(parents=True,exist_ok=True)
doc=Document(); init_doc()
p=doc.add_paragraph(style="Title"); p.paragraph_format.keep_with_next=True
clear_paragraph_border(p._p.get_or_add_pPr())
r=p.add_run("訓練資源採購與甄選管理辦法"); font(r,23,True,"000000")
p=doc.add_paragraph(); p.paragraph_format.space_after=Pt(7)
r=p.add_run("訓練需求到履約結案的作業程序"); font(r,12,False,"4A5E6D")
para("本件依官方 I10-E01 佐證目的撰寫，說明如何依課程需求選擇師資、教材或合作廠商，並完成評估、採購、簽約、交付驗收與後續管理。案例數字、日期、角色、核定和結果均為 SAMPLE / SYNTHETIC，並非原始點協會實際採購、核准、辦訓或付款紀錄。",after=6)
tab(["文件資訊","內容","使用方式"],[
["文件對應","DOCX 0045｜I10-E01｜官方方框 047","資源尚未選定、承諾費用或下單前使用"],
["文類與讀者","標準作業程序；課程承辦、評選者、授權核定者及行政記錄人員","依第4章逐步留下需求、比較、核定、契約與履約紀錄"],
["文件狀態","R01 SAMPLE / SYNTHETIC 草案；未生效、未經協會正式核定","先核對章程、實際授權、財務及保存規範，再決定是否採用"],
["完成時應留下","需求與設計依據、資源規格、比較與利益迴避、核定、契約、驗收及績效紀錄","0046 是單案評選紀錄表；本辦法不代替其逐人原始評分"]
],[1.0,3.05,2.95])
heading("30秒使用說明")
bullet("誰使用：承辦人提出需求並整理資料；未參與提案的評選者依事前公布條件比較；具實際授權的核定者決定是否採購；行政記錄人員保存往來、核定與履約資料。實際姓名、職稱及權限須依協會現行章程與授權文件核對。")
bullet("何時使用：課程需求與設計已可描述，但尚未選定師資、教材或合作廠商、尚未承諾費用或簽約時。")
bullet("怎麼使用：確認需求與可用資源，定義規格和預算，事前鎖定評分尺規，蒐集同條件候選資料，完成利益迴避、比較及核定，再依書面約定驗收並記錄改善。")
bullet("案例界線：第10章以 SYN-045-01 走讀一次。案例不證明協會做過該課程，也不與0044、0046、0047的任何真實個案建立連結。")

heading("1 目的與官方要求")
para("本程序把課程需求轉成可比較的資源條件，並規定評估、採購、簽約和後續管理要留下哪些資料。承辦人按同一套步驟作業，評選者可沿著需求、規格、評分和核定理由追查選擇依據，接手人也能確認交付內容與原約定相符。")
para("官方查核佐證文件資料表第3頁的 I10-E01 原文為：「完整文書手冊與紀錄分析相關資料（具體明確紀錄展現課程設計時，有適當的流程進行師資、教材或合作廠商評估選擇，且流程應有適當的辦法進行評估、採購、簽約及後續管理作業流程）。」本程序以作業流程、判斷條件、責任與紀錄欄位回應這項要求；官方原文沒有規定本文件所用的價格級距、權重、分數門檻、年限或組織編制。")
para("正式使用前，協會須把示範值換成可核實的章程、授權表、財務流程、課程計畫及紀錄管理規範。未完成核定前，本稿不得當成現行制度、正式採購依據或真實績效證據。")

heading("2 適用範圍與名詞")
para("本程序適用於為一項已說明的課程需求，選擇外聘師資、教材、場地／技術服務或合作廠商，並管理取得及交付過程。若使用既有免費資源而沒有採購，仍應留下需求、選用理由、權限及交付確認；不需為了套用本程序而虛構報價或契約。")
tab(["名詞","本程序的意思","操作時確認"],[
["課程需求","由對象、任務、已知落差、學習目標與預期交付內容構成的需求描述。","能指出來源與分母；不把未查證的推測寫成調查結果。"],
["資源規格","對師資資格、教材內容、服務範圍、時程、可近用性、資料處理及交付方式的事前要求。","所有候選使用相同規格及詢價條件。"],
["候選方案","可比較的師資／教材／服務組合及其書面回覆。","供應者身分與報價須有原始回覆支持；樣本代碼不是實際供應商。"],
["履約驗收","依契約或訂單逐項比對交付物、數量、時間、品質及未結缺失。","驗收人不以付款或簽收替代品質核對。"],
["事前門檻與實測結果","門檻是選擇或驗收前設定的規則；結果是交付後依原始資料計得的觀察值。","兩者分欄記錄，實測結果不得回頭改寫門檻。"]
],[1.3,3.0,2.7])

heading("3 角色與職務分離")
para("角色按工作責任定義，不預設原始點協會具有特定委員會、員工編制或財務權限。正式上線前，須依現行章程與授權文件把角色映射到實際職務；找不到合法授權者時停止承諾、下單與簽約，交由有權者釐清。")
tab(["角色","主要責任","不得單獨完成的事項","交接紀錄"],[
["需求承辦","整理需求來源、課程設計、預算估算與規格；保管原始提案資料。","不得自行完成評分、核定及驗收全部環節。","需求單、課程設計、規格版本"],
["評選者","逐項核對資格與回覆，申報利益關係，依同一量尺評分並寫理由。","有利益衝突者不得評該候選；不得自行改權重或門檻。","迴避聲明、個別評分、比較摘要"],
["授權核定者","核實權限與預算後，核定、退回補件或否決；理由留痕。","不能以口頭同意取代紀錄；無權限者不得代核。","授權依據、核定日期、決定與理由"],
["行政／採購記錄人","整理詢價、往返、訂購／契約、版本、交付及保存索引。","不代替實際簽約者或驗收者，不補造原件。","文件清單、收發日期、版本與存取紀錄"],
["驗收者","依事前條件檢點交付物，記錄缺失、補正及複驗。","不得把尚未補正或未交付項目標為合格。","驗收表、缺失通知、補正與複驗結果"]
],[1.12,2.35,2.0,1.53])
para("最低分離原則：提案者不得獨自評分並核定自己提出的方案；評選者先揭露與候選者的利益關係；簽約及驗收由具相應權限的人員處理。人力有限而不能完全分離時，記錄原因並由另一位具權限者作第二覆核；找不到第二覆核者時暫停採購。這些是示範控制，正式採用前須核對協會權限與可行人力。")

heading("4 作業流程與判斷點")
para("作業順序如下。需求不明、授權不明、利益衝突未處理、預算不足或契約條件未完成時，不進入下一步。案例中的天數是合成操作目標，只有經正式核定後才成為協會時限。")
tab(["步驟與時點","輸入與責任","操作、判斷與必要紀錄"],[
["1 形成課程需求\n規格發出前","承辦人；需求來源、受訓對象及課程目標。","記錄來源、樣本數／分母及能力落差；定義學習目標、時數、對象與預期產物。需求不能回溯來源時，標為待確認並停止詢價。輸出：需求與課程設計摘要。"],
["2 定義資源規格\n邀請候選前","承辦人擬稿；授權核定者確認預算與權限。","寫明師資資格、教材主題／格式、交付清單、時程、總價包含項目、資料界線、驗收方式及事前量尺。規格須能由候選者回答並在交付時驗收。輸出：同版規格及預算上限。"],
["3 蒐集候選方案\n依相同規格","記錄人發出同版邀請；承辦人整理回覆。","示範規則以三個可比較候選為目標。回覆不足時，以相同條件補詢一次；仍不足三個但至少兩個有效者，記錄原因並由有權者事前核准例外；少於兩個有效候選時暫停重尋。單一來源須走有權者書面核准的例外，不由承辦人自行決定。"],
["4 資格與利益迴避\n評分前","評選者逐人揭露；記錄人留存。","先檢查資格、範圍、時間、價格完整性和必要交付。利益衝突者退出該候選評分並記錄替代評選者；衝突無法排除或關係不明時暫停。輸出：合格名單及迴避紀錄。"],
["5 依事前量尺評分\n資料齊備後","無利益衝突的評選者；同一版本資料與量尺。","逐項評1至5分，每分附可核對理由；按第5章公式計算。未過資格或超預算者不進加權比較。保留個別分數及覆核方式，不以口頭平均掩蓋分歧。輸出：個別分數、加權表及推薦理由。"],
["6 核定、採購與簽約\n承諾前","承辦人送件；授權核定者決定；有權簽約者簽署。","核對權限、預算、候選、評分、例外、利益迴避、付款條件與契約標的。核准前不得下單、承諾費用或要求供應者開始履約。契約寫明交付、期限、驗收、變更、資料、取消及補正約定。"],
["7 交付驗收\n每一里程碑","驗收者依契約；供方交付物與實際紀錄。","逐項核對內容、數量、格式、日期與品質。缺失標記不合格，列責任人與補正日期；補正後由驗收者複驗。未結缺失不得關案或請款。輸出：驗收紀錄與缺失處理軌跡。"],
["8 績效與結案\n交付完成後","承辦人彙整；驗收者覆核；記錄人歸檔。","將事前目標與實測值分開記錄；評估準時、交付完整、缺失補正及合作情形。結案核對合約／訂單、核定、驗收、異常處理與適用付款證據索引。缺原件就標示缺件，不以樣本替代。"]
],[1.22,2.05,3.73])
para("判斷順序：需求與課程設計可追溯嗎？否，補查來源並暫停；是，資源規格與預算已事前核定嗎？否，退回核定；是，候選資格、利益迴避與價格完整嗎？否，剔除或補件並記錄；是，分數達門檻且授權者核定嗎？否，停止採購或走正式例外程序；是，書面簽約後履約。依契約驗收、關閉必要缺失後才結案。")

heading("5 評估量尺與計算")
para("本稿用六項事前公布的評估面向示範比較師資、教材或整體服務方案。正式採購前，承辦人依課程設計選用適用條件；若某項不適用，須在邀請候選前說明並調整權重至合計100%，不得收到報價後才改量尺。")
tab(["評估面向與權重","1至2分","3分","4至5分"],[
["需求與目標符合度\n30%","主要需求未回應，或需大幅改寫課程才可使用。","涵蓋主要目標，但仍有一項需補強。","4分：目標與對象均對應；5分：逐項對應且交付內容可驗收。"],
["師資資格與教學設計\n25%","資格資料不足或設計缺少練習／回饋。","具備所需資格，教學流程可執行。","4分：資格與方法均有佐證；5分：方法、教材與評量完整連到目標。"],
["履約排程與回應\n15%","關鍵時程或責任未確認。","人員、時程與回應方式明確。","4分：節點清楚並留修正時間；5分：風險、代理與補救時程明確。"],
["教材品質與可近用性\n10%","內容、格式或使用條件不符規格。","符合基本內容與格式要求。","4分：可讀、可用且版本可追；5分：另有可近用安排及品質檢查。"],
["含稅交付總價\n10%","超預算或總價缺項即不合格，不計分。","依第5.2節金額級距給分。","4分或5分依第5.2節互斥級距；低價不代表品質最佳。"],
["風險、資料與服務管理\n10%","資料處理或異常責任未說明。","基本保密、變更與補正方式明確。","4分：資料最小化與補正責任可執行；5分：版本、存取及事件通報明確。"]
],[1.45,1.72,1.7,2.13])
para("價格以可比較的含稅總價計，包含必要交通、教材、運送、授權及完成規格所需成本。以下是完整、互斥的SAMPLE級距，不是協會現行財務授權或法定採購金額；正式使用時必須由有權者以核定預算及財務規則替換。")
tab(["可比較總價（新臺幣）","價格分數","處理方式"],[
["不高於9,000元","5","納入總評"],
["高於9,000元且不高於11,000元","4","納入總評"],
["高於11,000元且不高於13,000元","3","納入總評"],
["高於13,000元且不高於15,000元","2","納入總評，且須符合核定預算"],
["高於15,000元","不計分","超出SAMPLE預算上限，不進總評；重新核定後再詢價"]
],[3.45,1.1,2.45])
para("加權總分 = Σ（單項權重 × 最終原始分數 ÷ 5）。兩名評選者先獨立評分；每項最終原始分數為兩人分數的算術平均，個別分數與理由均保留，不以事後協商覆寫。權重合計100%，分數範圍1至5，公式理論總分為20至100；依本稿價格門檻通過且價格項至少2分時，最低可能總分為22。示範門檻為70分。每項加權分保留兩位，總分四捨五入至一位。")
para("若同分，依事前規則先比較需求符合度加權分，再比較師資資格與教學設計，再比較履約排程與回應。仍同分時暫停決定，由有權核定者依已公告條件寫明理由；不得事後新增條件、抽籤或以未記錄的口頭偏好決定。")

heading("6 採購與契約控制")
tab(["契約／採購欄位","簽約前必須確認","交付與變更時的處理"],[
["採購標的","課程名稱、師資／教材／服務範圍、數量、格式及不包含事項。","增減以書面變更記錄，重估費用與時程後由有權者核准。"],
["價格與付款","含稅總價、分項價格、付款條件、請款文件及預算來源。","只依真實契約及驗收資料處理；示範稿不是發票或付款憑證。"],
["時程與責任","準備、授課、教材交付、回覆、補正及各方窗口。","延期並列原定與實際日期、影響、替代安排及核定。"],
["驗收與缺失","交付清單、合格條件、檢查方式、補正期限及複驗責任。","逐項留存結果、證據位置、缺失通知、補正及複驗。"],
["資料與教材使用","個資範圍、存取、交付格式、保存／刪除責任及教材授權。","只依已核實的授權與契約處理，不推定可公開或可轉授權。"],
["取消與爭議","取消、替代師資、不可交付、通報及聯絡方式。","先處理課程與受訓者影響，再由有權者依真實約定決定。"]
],[1.35,2.92,2.73])
para("核定及契約文件須由實際具權限者簽署。權限來源、簽署人或原件尚未核實時，標示待核實；不得以示範核定欄、合成編號或文字簽名代替正式簽章。")

heading("7 交付驗收與履約管理")
para("驗收前把契約約定轉成逐項檢查表。驗收者查看交付物本身及可用的收件／授課紀錄，記錄檢查日期、結果、缺失、責任人、期限及複驗。補正項目保留初檢結果與修正軌跡，不覆寫初次檢查。")
tab(["項目","事前驗收標準","證據與不合格處理"],[
["師資／服務","符合契約所列人員、時數、課程目標與服務內容。","用真實課表、授課紀錄和聯繫資料核對；變更須先核准。"],
["教材／資源","版本、數量、內容、格式、可讀性與授權符合規格。","記版本及數量；缺頁、錯版或無法使用時列缺失，補正後複驗。"],
["時程","在約定日期完成各節點。","並列原定與實際日期，計算逾期日數；例外附原因及核定。"],
["品質與回饋","依事前定義的工具收集回饋，保留分母與原始彙總。","計算有效份數／邀請份數及平均；缺資料標UNKNOWN，不補估。"],
["缺失結案","重大缺失已處理，其他未結項目有核定責任與期限。","必要補正未完成時不作最終驗收；付款依正式契約及權限處理。"]
],[1.35,2.6,3.05])
para("至少分開看三件事：事前目標是否清楚、交付是否符合約定、實測結果如何。例：滿意度目標4.0／5是事前門檻，4.2／5是依有效問卷計出的結果；實測值不得回填成目標。教材合格比例須有合格件數、檢查總件數和判準，不能把完成檢查誤稱教材品質得分。")

heading("8 例外與升級處理")
tab(["情況","立即處理與紀錄","停止／升級條件"],[
["候選不足或回覆不可比","同版補詢一次，列聯繫對象、日期、缺件及未回覆。","少於兩個有效方案時停止；單一來源須有權者事前書面核准。"],
["利益衝突或關係未明","評選者揭露並退出該候選評分；記錄替代評選者。","無獨立評選或衝突無法控制時暫停。"],
["總價超過預算","不刪除必要需求以讓價格表面合格；重新估算或修訂規格。","有權者未重新核定前不得採購或簽約。"],
["交付延誤或品質缺失","保留原期限、實況、影響、通知、補正及複驗。","可能影響開課或資料安全時立即通知授權者並處理替代方案。"],
["個資、教材權利或資料事件","限制存取，保存必要事實並依正式事件流程通報。","處理規範或授權未核實時停止傳送／使用資料。"],
["授權、簽章或原件缺失","標示缺件、所需來源、責任角色與追補狀態。","不得補造簽名、報價、契約、發票、核准或第三方證明。"]
],[1.55,2.8,2.65])
para("例如兩個工作日內回覆一般補件、重大交付異常當日通報，只有在正式核定後才可成為協會時限。示範稿不自行賦予協會法定期限或內規。")

heading("9 紀錄、存取與檢討")
tab(["紀錄","最低欄位","保管與替換來源"],[
["需求與課程設計","來源、日期、對象、分母、落差、目標、時數與需求核定。","保存原始調查／訪談或正式需求資料；合成案例不當真實調查。"],
["資源規格與詢價","版本、預算、條件、邀請對象、發送／回覆日期及報價明細。","保存原始詢價與回覆；核對總價含稅、交通、教材及服務。"],
["評估與核定","利益揭露、個別分數、理由、公式、例外、推薦及授權。","保留原始分數與修正軌跡；0046是同要求單案評選表。"],
["採購與履約","訂單／契約、標的、金額、里程碑、變更、交付、驗收及缺失閉環。","由有權來源取得原件；不能公開的原件留在授權位置並記索引。"],
["績效與結案","目標、實測、分子分母、日期、限制、結案核對與改善事項。","承辦人彙整、驗收者覆核，依正式紀錄規範存取與保存。"]
],[1.5,3.2,2.3])
para("本稿不替協會指定正式保存年限。第10章的五年只是合成示範參數，須用協會已核定且適用的保存規範替換；未取得規範前，不得宣稱五年是法律、政府或TTQS要求。存取以工作所需為限，公開資料前確認權限。")
para("結案後可依真實資料統計準時交付率、完整驗收率、缺失補正時間與有效回饋率。指標須寫明分子、分母及期間；樣本小時同時列件數。跨年度制度檢討屬0047 I10-E02，不由本件虛構多年成果。")

heading("10 完整合成案例走讀")
para("以下案例只演示本程序如何從需求走到履約檢查。SYN-045-01 與0044、0046、0047或任何真實課程都沒有已核實的連結。日期、角色、候選資料、評分、核定及交付結果均為虛構；示範核定不是原始點協會的決議。")
heading("10.1 課程需求與規格",2)
tab(["欄位","SAMPLE / SYNTHETIC 案例內容","核對方式"],[
["案例與課程","SYN-045-01｜志工服務溝通與紀錄整理工作坊","合成代碼；不是協會實際課程名稱"],
["需求來源與日期","模擬盤點日2026-05-04；12位預定參與者。","合成盤點表；正式使用需真實需求原件與分母"],
["能力落差","8／12尚需練習服務紀錄撰寫；7／12尚需練習個資情境判斷。","兩項各自以12為分母，不是互斥人數；不得相加為15人"],
["目標與設計","12小時、兩次各6小時；練習情境紀錄、回饋修訂及個資判斷。","合成規格；正式目標需由真實權責人核定"],
["預算與總價口徑","示範上限新臺幣15,000元；總價含稅、交通、教材及交付。","不是協會現行預算或財務核決門檻"],
["時程","詢價05-06；收件05-11；評分05-12；案例核定05-15；簽約05-18；授課06-01及06-08；結案檢視06-22，均為2026年。","全為合成日期；簽署或付款原件不存在"]
],[1.45,3.25,2.3])
para("案例資源規格要求：師資帶領志工情境演練；兩次共12小時；課前交付流程及教材樣稿；提供12份最終教材；教材包含紀錄練習與個資情境；開課前完成修正；全案含稅總價不超過15,000元。每個候選依相同規格回覆。")

heading("10.2 合格檢查與候選方案",2)
tab(["合成候選","資源組合與回覆摘要","含稅總價","門檻檢查"],[
["方案A","師資A、教材A；主題符合，個資案例較少；回覆兩次授課時段及教材交付。","14,000元","資格、時程、交付符合；價格級距2分"],
["方案B","師資B與共同備課教材；逐項回應兩項能力落差，列出流程、教材樣稿、修訂節點及授課時段。","12,000元","資格、時程、交付符合；價格級距3分"],
["方案C","師資C與教材套件；成本最低，紀錄練習充足，但個資情境及課後修訂說明較少。","9,000元","資格、時程、交付符合；價格級距5分"]
],[.85,3.7,1.05,1.4])
para("三份候選回覆及證明文件都是案例中的合成材料，不是真實廠商報價。案例假設兩名合成評選者E01、E02均先完成利益揭露且無需迴避；代碼及申報都不是真實協會紀錄。")

heading("10.3 評分與計算",2)
para("下表列兩位評選者各項分數的算術平均；下一表保留E01與E02的原始分數及理由。")
tab(["面向／權重","方案A","方案B","方案C","計分依據摘要"],[
["需求符合度30%","5","4","4","A逐項涵蓋；B涵蓋主要需求；C個資情境較少"],
["師資與教學25%","4","5","4","B的練習、回饋與目標連結完整"],
["排程與回應15%","4","5","3","B列兩次時段、交付和修訂節點"],
["教材與可近用10%","4","5","4","B樣稿符合格式並列版本修訂"],
["含稅總價10%","2","3","5","依9,000／11,000／13,000／15,000元互斥級距"],
["風險與服務10%","4","4","3","B列資料界線與補正方式；C未充分說明補正"],
["加權總分","82.0","88.0","77.0","權重×原始分÷5後加總"],
["示範門檻70分","通過","通過","通過","僅為案例門檻，不是現行核定標準"]
],[1.55,.68,.68,.68,3.41])
para("下表保留兩名評選者的原始分數。每一列的最終分數等於E01與E02之和除以2；個別理由有差異時也保留差異，不把平均值說成兩人原本給出相同分數。")
tab(["候選","評估面向","E01","E02","平均","依據與差異"],[
["A","需求符合度","5","5","5","兩項需求均有對應練習與教材。"],
["A","師資與教學","4","4","4","資格資料及教學流程符合規格。"],
["A","排程與回應","3","5","4","列兩次時段及交付；修訂節點說明較少，保留兩人原分。"],
["A","教材與可近用","4","4","4","格式符合要求，版本與可近用安排一般。"],
["A","含稅總價","2","2","2","14,000元落在高於13,000元且不高於15,000元區間。"],
["A","風險與服務","5","3","4","有資料處理與補正說明；兩人對細節充分度判斷不同。"],
["B","需求符合度","4","4","4","主要需求均回應，尚有一項可再補強。"],
["B","師資與教學","5","5","5","教學方法、教材與評量完整連到目標。"],
["B","排程與回應","5","5","5","兩次時段、交付及修訂節點均明確。"],
["B","教材與可近用","5","5","5","樣稿、版本修訂及可近用安排均列明。"],
["B","含稅總價","3","3","3","12,000元落在高於11,000元且不高於13,000元區間。"],
["B","風險與服務","4","4","4","資料界線與補正責任可執行。"],
["C","需求符合度","3","5","4","有紀錄練習但個資情境較少，兩人對覆蓋程度評分不同。"],
["C","師資與教學","4","4","4","資格與基本教學流程符合。"],
["C","排程與回應","2","4","3","時段可行但修訂與回覆節點較少。"],
["C","教材與可近用","5","3","4","教材內容充足，可近用及版本維護說明較少。"],
["C","含稅總價","5","5","5","9,000元不高於最低價格級距。"],
["C","風險與服務","3","3","3","具基本服務說明，補正細節有限。"]
],[.55,1.32,.55,.55,.55,3.48])
para("逐步重算：方案B = (30×4÷5) + (25×5÷5) + (15×5÷5) + (10×5÷5) + (10×3÷5) + (10×4÷5) = 24 + 25 + 15 + 10 + 6 + 8 = 88.0。方案A = 30 + 20 + 12 + 8 + 4 + 8 = 82.0；方案C = 24 + 20 + 9 + 8 + 10 + 6 = 77.0。權重合計100；三案均高於70分案例門檻。")
para("案例推薦方案B，因總分88.0最高且符合資格、排程、交付和價格條件。方案C雖最便宜，不能只按最低價選定；方案B的優勢來自需求、教學、教材及補正安排。推薦與核定均非協會真實決議。")

heading("10.4 核定、契約與交付",2)
tab(["日期／事件","合成紀錄內容","結果與限制"],[
["2026-05-12評分","兩名合成評選者依同版量尺獨立評分，保留原始分數與理由。","方案B 88.0分；合成案例假設無利益衝突；非真實評選紀錄"],
["2026-05-15核定","合成角色A01依本案例設定確認推薦方案及15,000元上限。","流程演示；沒有真人核定、簽章或組織授權"],
["2026-05-18契約條件","合成代碼SYN-CT-045-01；總價12,000元；兩次各6小時、12份教材及開課前修訂。","不是契約、報價、發票或付款證明；未有真實用印"],
["2026-05-29教材初檢","合成檢查發現兩份樣張頁碼索引未更新，通知方案B修正。","一項可補正缺失；保留初檢結果"],
["2026-05-30複驗","合成複驗確認12份最終教材頁碼一致，課程流程及個資情境已納入。","示範缺失閉環；非真實收件或驗收紀錄"],
["2026-06-01及06-08授課","兩次各6小時，合計12／12約定小時；12／12份最終教材可用。","純合成情境，不證明協會曾辦訓或實際交付"],
["2026-06-22結案檢視","10／12份有效回饋；4人給5分、4人給4分、2人給3分。","平均4.2／5；有效回覆率83.3%；純合成示例"]
],[1.35,3.55,2.1])
para("回饋計算：有效回覆率 = 10 ÷ 12 × 100% = 83.3%（四捨五入到小數一位）；平均滿意度 = (4×5 + 4×4 + 2×3) ÷ 10 = 42 ÷ 10 = 4.2／5。案例預設事前目標至少4.0／5，因此4.2／5在本合成案例達到示範目標。問卷分數不是實際參與者資料。")
para("案例結案判斷：授課完成12／12小時，最終教材完成12／12份，一項頁碼缺失在授課前複驗關閉，有效問卷10／12，平均4.2／5高於案例事前目標4.0／5。這只演示如何判斷；付款、簽約、授權及原件均須由真實來源核實。")

heading("10.5 案例參數與正式替換",2)
para("權重、70分門檻、價格級距、15,000元上限、4.0／5回饋目標及五年示範保存期都是未核定的合成參數，並非官方要求或協會現行制度。五年只展示如何登錄保存參數，不主張任何法律或政府依據。逐項替換來源、定位及責任角色見本封包的SYNTHETIC_REPLACEMENT_REGISTER_R01.csv。")

heading("11 表單與檢查清單")
para("正式採購時，承辦人至少確認下列欄位完整。單案的候選與個別評分填入0046《師資教材廠商評選紀錄表》；本節只列程序必要控制，不複製0046的完整表單。")
tab(["階段","必填檢查欄位","完成判斷"],[
["需求與設計","來源／日期／分母；能力落差；學習目標；時數與對象；資源必要性。","每項需求有來源，且連到資源規格與驗收條件。"],
["詢價與比較","同版規格；候選來源；回覆日期；總價範圍；資格；利益揭露；事前權重與門檻。","資料可比較；例外已由有權者事前核定。"],
["核定與採購","推薦理由；預算來源；授權依據；核定職務／日期／決定；訂購或契約版本。","正式權限及原件可核對；缺件時不承諾。"],
["驗收與結案","約定與實際值；交付證據；分子分母；缺失與複驗；結案及保存位置。","必要缺失已關閉或由有權者作成具理由處置，原件可追溯。"]
],[1.25,3.72,2.03])

heading("12 相關文件與工作界線")
tab(["文件","對應工作","本件如何銜接"],[
["0045｜I10-E01｜訓練資源採購與甄選管理辦法","本SOP的需求、評估、採購、簽約與後續管理。","本件主文，規定制度流程及判斷控制。"],
["0046｜I10-E01｜師資教材廠商評選紀錄表","一個採購案的候選、個別評分、理由與核定索引。","依本程序填單案紀錄；兩件文類不同。"],
["0047｜I10-E02｜採購簽約與後續管理檢討","跨年度檢討、趨勢比較及制度改善分析。","本件保存單案結果供後續分析，不代替多年檢討。"],
["0044｜I09-E04｜討論會議或電子郵件完整紀錄","會議及郵件內容、簽核與存檔紀錄。","採購往來依正式規範歸檔，本件不代替原始紀錄。"]
],[1.75,2.8,2.45])
para("遮住標題及編號後，本件仍可由需求、規格、候選評估、授權採購、契約、驗收及履約檢討的完整流程辨識為採購與甄選管理程序。0044、0046、0047各有不同工作物；共用資料時引用來源索引，不複製其正文或虛構同一案例關聯。")

heading("13 版本修訂紀錄")
tab(["版本","日期","修訂內容","核定狀態"],[
["R01","2026-10-17","依I10-E01及Unique Blueprint建立新示範程序，並製作合成案例與逐事實替換簿。","候選草案；未生效、未核定、無簽章"]
],[.8,1.15,3.55,1.5])

doc.core_properties.title="訓練資源採購與甄選管理辦法"
doc.core_properties.subject="DOCX 0045 / I10-E01 / official checkbox 047 / SAMPLE SYNTHETIC candidate R01"
doc.core_properties.author="TTQS ONE candidate authoring"
doc.core_properties.keywords="SAMPLE; SYNTHETIC; 0045; I10-E01; checkbox 047"
doc.core_properties.comments="Candidate only. No Association approval, procurement, signature, contract, payment, delivery, or actual training is represented."
doc.save(DOCX)

blueprint_rows=[json.loads(line) for line in BLUEPRINT_IN.read_text(encoding="utf-8").splitlines() if line.strip()]
blueprint=next(x for x in blueprint_rows if x.get("deliverable_id")=="0045" and x.get("requirement_id")=="I10-E01")
BLUEPRINT_OUT.write_text(json.dumps(blueprint,ensure_ascii=False,separators=(",",":"))+"\n",encoding="utf-8")
blueprint_sha=hashlib.sha256(BLUEPRINT_IN.read_bytes()).hexdigest()
blueprint_row_sha=hashlib.sha256(BLUEPRINT_OUT.read_bytes()).hexdigest()

# Each entry records a fact or one numerical setting used by the sample.
facts=[]
def fact(fid,value,loc,source,owner="需求承辦／實際權責人"):
    facts.append({"fact_id":fid,"value_synthetic":value,"type":"SAMPLE_SYNTHETIC","document_location":loc,"real_replacement_source_required":source,"responsible_role":owner,"status":"REPLACE_BEFORE_REAL_USE"})
F="SYN-045-"
entries=[
("001","SYN-045-01","§10.1案例代碼","真實案號及核定計畫","需求承辦"),
("002","志工服務溝通與紀錄整理工作坊","§10.1課程欄","正式課程名稱及核定計畫","課程負責人"),
("003","2026-05-04","§10.1需求盤點日期","真實需求資料與形成日期","需求承辦"),
("004","12位預定參與者","§10.1對象欄","核定對象名冊或去識別人數","課程負責人"),
("005","8／12需練習服務紀錄撰寫","§10.1能力落差列","原始調查、有效樣本分母及分析","需求承辦"),
("006","7／12需練習個資情境判斷","§10.1能力落差列","原始調查、有效樣本分母及分析","需求承辦"),
("007","12小時","§10.1目標；§10.4授課","核定課程計畫及授課紀錄","課程負責人／驗收者"),
("008","兩次課程","§10.1目標與設計","核定課表與實際授課紀錄","課程負責人"),
("009","每次6小時","§10.1目標；§10.4契約","核定課表與授課紀錄","課程負責人／驗收者"),
("010","15,000元示範預算上限","§5級距；§10.1預算","正式預算核定及財務授權","有權核定者／財務記錄人"),
("011","2026-05-06詢價日","§10.1時程","真實詢價發送原件與時間戳","行政記錄人"),
("012","2026-05-11收件日","§10.1時程","候選原始回覆與收件時間戳","行政記錄人"),
("013","2026-05-12評分日","§10.1時程；§10.4評分","原始評選紀錄與個別分數","評選者／記錄人"),
("014","2026-05-15案例核定日","§10.1時程；§10.4核定","正式核定與授權依據","有權核定者"),
("015","2026-05-18簽約日","§10.1時程；§10.4契約","正式契約及簽署權限","實際簽約者"),
("016","2026-05-29教材初檢日","§10.4教材初檢","真實教材收件及檢查紀錄","驗收者"),
("017","2026-05-30教材複驗日","§10.4教材複驗","真實修正版及複驗紀錄","驗收者"),
("018","2026-06-01授課日","§10.1及§10.4授課","真實課表、授課與出席原件","課程負責人"),
("019","2026-06-08授課日","§10.1及§10.4授課","真實課表、授課與出席原件","課程負責人"),
("020","2026-06-22結案檢視日","§10.1及§10.4結案","真實結案核對資料","驗收者／記錄人"),
("021","方案A","§10.2候選列","候選真實身分及原始報價","行政記錄人"),
("022","方案B","§10.2候選列","候選真實身分及原始報價","行政記錄人"),
("023","方案C","§10.2候選列","候選真實身分及原始報價","行政記錄人"),
("024","方案A總價14,000元","§10.2與§10.3價格列","正式報價與含稅成本明細","行政／財務記錄人"),
("025","方案B總價12,000元","§10.2、§10.3、§10.4契約列","正式報價、契約與含稅成本明細","行政／財務記錄人"),
("026","方案C總價9,000元","§10.2與§10.3價格列","正式報價與含稅成本明細","行政／財務記錄人"),
("027","需求符合度權重30%","§5及§10.3評分表","核定量尺版本","有權核定者"),
("028","師資與教學權重25%","§5及§10.3評分表","核定量尺版本","有權核定者"),
("029","排程與回應權重15%","§5及§10.3評分表","核定量尺版本","有權核定者"),
("030","教材與可近用權重10%","§5及§10.3評分表","核定量尺版本","有權核定者"),
("031","含稅價格權重10%","§5及§10.3評分表","核定量尺版本","有權核定者"),
("032","風險與服務權重10%","§5及§10.3評分表","核定量尺版本","有權核定者"),
("033","評分範圍1至5分","§5量尺","正式核定評分尺規","有權核定者"),
("034","加權公式除數5","§5公式與§10.3計算","正式核定評分尺規","有權核定者"),
("035","權重合計100%","§5公式與§10.3計算","正式核定評分尺規","覆核者"),
("036","示範總分門檻70分","§5與§10.3門檻列","正式核定事前門檻","有權核定者"),
("037","價格分數5分上限9,000元","§5價格級距","正式核定財務規則及預算","有權核定者"),
("038","價格分數4分上限11,000元","§5價格級距","正式核定財務規則及預算","有權核定者"),
("039","價格分數3分上限13,000元","§5價格級距","正式核定財務規則及預算","有權核定者"),
("040","價格分數2分上限15,000元","§5價格級距","正式核定財務規則及預算","有權核定者"),
("041","方案A兩名評選者算術平均分5、4、4、4、2、4","§10.3平均分摘要與原始分數表","依兩位評選者原始分數及理由重算","覆核者"),
("042","方案B兩名評選者算術平均分4、5、5、5、3、4","§10.3平均分摘要與原始分數表","依兩位評選者原始分數及理由重算","覆核者"),
("043","方案C兩名評選者算術平均分4、4、3、4、5、3","§10.3平均分摘要與原始分數表","依兩位評選者原始分數及理由重算","覆核者"),
("044","方案A加權總分82.0","§10.3評分表及計算段","由真實原始分數重算","覆核者"),
("045","方案B加權總分88.0","§10.3評分表及計算段","由真實原始分數重算","覆核者"),
("046","方案C加權總分77.0","§10.3評分表及計算段","由真實原始分數重算","覆核者"),
("047","方案B為最高分推薦方案","§10.3推薦段","正式評選紀錄及核定原件","評選者／有權核定者"),
("048","兩名合成評選者E01與E02，獨立評分並取算術平均","§10.2、§10.3原始分數表及§10.4評分列","實際評選者、個別原始評分、理由及利益揭露","記錄人"),
("049","合成核定角色A01","§3及§10.4核定列","實際核定職務、章程及授權文件","有權核定者"),
("050","SYN-CT-045-01契約代碼","§10.4契約列","真實契約編號與簽署原件","實際簽約者"),
("051","案例契約總價12,000元","§10.4契約列","真實契約與核定預算","財務記錄人"),
("052","兩份樣張索引有缺失","§10.4初檢列","真實初檢表與缺失通知","驗收者"),
("053","12份最終教材","§10.4複驗與授課列","真實教材清單與版本","驗收者"),
("054","12／12約定授課小時完成","§10.4授課列與結案段","契約時數及真實授課紀錄","驗收者"),
("055","12／12份教材可用","§10.4授課與結案段","教材交付及驗收紀錄","驗收者"),
("056","10／12份有效回饋","§10.4結案列與計算段","去識別問卷、邀請數及有效數","記錄人"),
("057","四人評5分","§10.4回饋分布與公式","去識別問卷分布及量尺","記錄人"),
("058","四人評4分","§10.4回饋分布與公式","去識別問卷分布及量尺","記錄人"),
("059","兩人評3分","§10.4回饋分布與公式","去識別問卷分布及量尺","記錄人"),
("060","滿意度總分42","§10.4公式","原始問卷彙總與重算表","覆核者"),
("061","平均滿意度4.2／5","§7及§10.4公式","真實問卷與分母；目標另用核定來源","覆核者"),
("062","有效回覆率83.3%","§10.4公式","有效問卷與受邀人數","覆核者"),
("063","事前滿意度目標4.0／5","§7與§10.4公式","核定品質目標，與實測值分開","有權核定者"),
("064","示範保存期五年","§9及§10.5","適用正式保存規範及核定版本","記錄管理權責者"),
("065","三個候選方案目標","§4步驟3","真實詢價邀請及回覆紀錄","行政記錄人"),
("066","至少兩個有效方案才走例外評估","§4步驟3與§8","核定採購規則及例外權限","有權核定者"),
("067","補詢一次","§4步驟3與§8","核定詢價程序","有權核定者"),
("068","兩個工作日示範回覆目標","§8末段","正式核定服務時限","有權核定者"),
("069","2026-10-17修訂日期","§13版本紀錄","真實修訂紀錄及日期","文件管理權責者"),
]
for x in entries: fact(F+x[0],x[1],x[2],x[3],x[4])
raw_scores={"A":[(5,5),(4,4),(3,5),(4,4),(2,2),(5,3)],"B":[(4,4),(5,5),(5,5),(5,5),(3,3),(4,4)],"C":[(3,5),(4,4),(2,4),(5,3),(5,5),(3,3)]}
criteria=["需求符合度","師資與教學","排程與回應","教材與可近用","含稅總價","風險與服務"]
for candidate,pairs in raw_scores.items():
    for i,(e01,e02) in enumerate(pairs):
        fact(F+f"070-{candidate}-{i+1}-E01",f"方案{candidate}／{criteria[i]}／評選者E01原始分數{e01}","§10.3兩人原始分數表","評選者E01的真實利益揭露、原始分數與理由","評選者E01")
        fact(F+f"070-{candidate}-{i+1}-E02",f"方案{candidate}／{criteria[i]}／評選者E02原始分數{e02}","§10.3兩人原始分數表","評選者E02的真實利益揭露、原始分數與理由","評選者E02")
reg=PKG/"evidence/SYNTHETIC_REPLACEMENT_REGISTER_R01.csv"
with reg.open("w",newline="",encoding="utf-8-sig") as f:
    writer=csv.DictWriter(f,fieldnames=list(facts[0].keys())); writer.writeheader(); writer.writerows(facts)

official_sha=hashlib.sha256(OFFICIAL_PDF.read_bytes()).hexdigest()
old_sha=hashlib.sha256(OLD_DOCX.read_bytes()).hexdigest()
old_review_sha=hashlib.sha256(OLD_REVIEW.read_bytes()).hexdigest()
if old_sha.lower()!=OLD_SHA_EXPECTED: raise AssertionError("historical candidate SHA changed")
(PKG/"inputs/SOURCE_MAP.md").write_text(f"""# 0045 R01 來源與文件對應

- DOCX：0045《訓練資源採購與甄選管理辦法》
- Requirement ID：I10-E01；官方方框流水號：047（與DOCX ID不同）。
- 文類：標準作業程序，不是單案選評表、會議紀錄或跨年度檢討報告。
- 官方原文：完整文書手冊與紀錄分析相關資料（具體明確紀錄展現課程設計時，有適當的流程進行師資、教材或合作廠商評估選擇，且流程應有適當的辦法進行評估、採購、簽約及後續管理作業流程）。
- 官方定位：DRIVE_OFFICIAL_EVIDENCE_TABLE.pdf 第3頁；SHA-256 {official_sha}；讀取狀態 PDF_TEXT_EXACT_PAGE_MATCH。
- Blueprint來源：GitHub分支 commit {BLUEPRINT_COMMIT}；quality-review/0044_R01/inputs/BLUEPRINT_0044_AND_NEIGHBORS.jsonl；原檔SHA-256 {blueprint_sha}；0045精確列SHA-256 {blueprint_row_sha}。本封包保存精確列副本。
- 鄰項：0046/I10-E01是單案評選紀錄表；0047/I10-E02是近年檢討與改善；0044/I09-E04是討論、會議與郵件原始紀錄。本SOP不取代三者。
- SYN-045-01為獨立合成案例，未證實與其他文件案例相同。
- 寫作方式：依官方requirement與Unique Blueprint重新寫作；舊正文禁止作模板。
""",encoding="utf-8")
(PKG/"inputs/historical_candidate_disposition.md").write_text(f"""# 0045 舊候選處置

2026-10-05的R04候選保留為HISTORICAL；本次未複製其正文，也未改寫其DOCX位元組。

- 路徑：E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\CANDIDATES\\0045__訓練資源採購與甄選管理辦法.docx
- 重算SHA-256：{old_sha}；與歷史審查綁定SHA一致。
- 歷史獨立審查JSON：CONTROL/REVIEWS/0045.json；SHA-256 {old_review_sha}；結論FAIL_REPAIRABLE。該結論只約束舊SHA，不自動套用至本R01。
- 缺陷回歸清單：D01價格級距邊界重疊；D02候選／報價數量分支不一致；D03低分處置不一致；D04比例與平均值不可重算、教材指標混用；D05缺修訂紀錄；D06程序與案例重複；D07事前門檻與實測結果混淆；D08合成規則被稱為法定／政府／TTQS要求。
- R01防回歸：互斥價格區間；候選不足有暫停／例外核定；事前目標和實測值分開；展示計算可重算；提供修訂紀錄；一套主流程及一套走讀；示範值明示未核定且不稱法定。
- 本檔不宣稱舊DOCX已同步GitHub；本封包交付新R01及歷史審查結果。
""",encoding="utf-8")
(PKG/"evidence/historical_R04_review_receipt.json").write_bytes(OLD_REVIEW.read_bytes())

text_parts=[]
for p in doc.paragraphs:
    if p.text.strip(): text_parts.append(p.text)
for i,t in enumerate(doc.tables,1):
    text_parts.append(f"[TABLE {i}]")
    for row in t.rows: text_parts.append(" | ".join(c.text.replace("\n"," / ") for c in row.cells))
(PKG/"evidence/extracted_text_R01.txt").write_text("\n".join(text_parts),encoding="utf-8")

weights=[30,25,15,10,10,10]
score_rows={"A":[5,4,4,4,2,4],"B":[4,5,5,5,3,4],"C":[4,4,3,4,5,3]}
scores={k:sum(Decimal(w)*Decimal(s)/Decimal(5) for w,s in zip(weights,v)) for k,v in score_rows.items()}
assert sum(weights)==100 and scores=={"A":Decimal("82"),"B":Decimal("88"),"C":Decimal("77")}
assert Decimal(4*5+4*4+2*3)/10==Decimal("4.2")
assert (Decimal(10)/12*100).quantize(Decimal("0.1"))==Decimal("83.3")
with zipfile.ZipFile(DOCX) as z: assert z.testzip() is None
alltext="\n".join(text_parts)
for s in ["I10-E01","官方方框 047","SAMPLE / SYNTHETIC","方案B","88.0","42 ÷ 10 = 4.2","83.3%","0046","0047","利益迴避","事前目標"]:
    assert s in alltext, f"missing content: {s}"
for p in doc.paragraphs:
    if p.style.name in ("Normal","List Bullet","List Number"):
        for r in p.runs:
            if r.text.strip() and r.font.size and r.font.size.pt<10.5: raise AssertionError("body font below 10.5 pt")
for t in doc.tables:
    for row in t.rows:
        for c in row.cells:
            for p in c.paragraphs:
                for r in p.runs:
                    if r.text.strip() and r.font.size and r.font.size.pt<9.5: raise AssertionError("table font below 9.5 pt")
sha=hashlib.sha256(DOCX.read_bytes()).hexdigest()
receipt={"deliverable_id":"0045","requirement_id":"I10-E01","official_checkbox_sequence":"047","candidate_revision":"R01","candidate_state":"CANDIDATE_NOT_ACCEPTED","docx_path":"candidate/0045_R01.docx","docx_sha256":sha,"docx_bytes":DOCX.stat().st_size,"source_branch_commit":BLUEPRINT_COMMIT,"blueprint_source_sha256":blueprint_sha,"blueprint_row_sha256":blueprint_row_sha,"official_source_sha256":official_sha,"historical_candidate_sha256":old_sha,"historical_review_sha256":old_review_sha,"synthetic_register_rows":len(facts),"math":{"weights_sum":sum(weights),"scores":{k:str(v) for k,v in scores.items()},"satisfaction_mean":"4.2/5","feedback_rate":"83.3%"},"technical_package_check":"PASS","independent_semantic_review":"PENDING_NO_VALID_INDEPENDENT_ROUTE","promotion":"NOT_PROMOTED","approval":"NONE_REPRESENTED","generated_utc":datetime.now(timezone.utc).isoformat(),"limitations":["SAMPLE/SYNTHETIC only","No Association approval, procurement, signature, contract, invoice, payment, delivery, or actual training is asserted","All sample weights, thresholds, price bands and retention period require valid Association authority before use","Independent exact-SHA semantic review not completed"]}
(PKG/"evidence/build_receipt_R01.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
(PKG/"evidence/technical_static_QA_R01.json").write_text(json.dumps({"docx_sha256":sha,"zip_integrity":"PASS","paragraph_count":len(doc.paragraphs),"table_count":len(doc.tables),"synthetic_register_rows":len(facts),"body_font_min_pt":10.5,"table_font_min_pt":9.5,"weights_sum":sum(weights),"recomputed_scores":{k:str(v) for k,v in scores.items()},"feedback_count":10,"invite_count":12,"response_rate":"83.3%","satisfaction_sum":42,"satisfaction_mean":"4.2/5","semantic_acceptance":"PENDING_INDEPENDENT_REVIEW","promotion":"NOT_PROMOTED"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
(PKG/"PROGRESS.json").write_text(json.dumps({"project_id":"TTQS_ONE","document_id":"0045","requirement_id":"I10-E01","official_checkbox_sequence":"047","state":"CANDIDATE_BUILT_RENDER_QA_PENDING_INDEPENDENT_SEMANTIC_REVIEW","candidate_sha256":sha,"historical_sha256":old_sha,"historical_candidate_reused_as_template":False,"source_commit":BLUEPRINT_COMMIT,"synthetic_register_rows":len(facts),"next_actions":["Render and inspect every page","Fix only located visual defects and freeze SHA","Obtain exact-SHA independent semantic review through a valid route","Sync package to existing PR #92 and read back remote bytes"],"promotion":"NOT_PROMOTED"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"docx":str(DOCX),"sha256":sha,"bytes":DOCX.stat().st_size,"paragraphs":len(doc.paragraphs),"tables":len(doc.tables),"register_rows":len(facts),"scores":{k:str(v) for k,v in scores.items()},"old_candidate_sha":old_sha},ensure_ascii=False))\n