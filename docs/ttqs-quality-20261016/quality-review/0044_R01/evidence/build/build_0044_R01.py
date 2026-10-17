from __future__ import annotations
import csv, hashlib, json, os, zipfile
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'candidate'/'0044_R01.docx'
REG=ROOT/'evidence'/'SYNTHETIC_REPLACEMENT_REGISTER_R01.csv'
NAVY='243B53'; BLUE='DCEAF5'; PALE='F3F7FA'; TEXT='24313A'; MUTED='52616B'; WHITE='FFFFFF'; AMBER='FFF2CC'
FONT='Microsoft JhengHei'

records=[
 {'id':'SYN-044-M01','type':'會議紀錄','date':'2026-01-14','time':'09:00–09:35','place':'示範會議室 A','participants':'R01 示範召集角色；R02 示範紀錄角色；R03 示範覆核角色','topic':'建立行政往來紀錄的來源與版本索引','source':'SYN-ATT-001 會議通知；SYN-ATT-002 示範出席欄；SYN-ATT-003 議程','issue':'草稿無法由摘要追到原始消息與附件版次。','opinions':'R02 提議列來源識別、形成時間及附件版本；R03 提醒將覆核/簽核與歸檔分開記錄；R01 要求缺資料時填「未知」並列管。','decision':'本合成會議決定以六個控制欄位作示範索引：來源識別、類型/時間、參與或寄收角色、議題及決定狀態、附件版次、覆核簽核與保存位置。這不是協會政策或實際會議決議。','action':'R02 製作示範索引 v0.1；R03 對照缺件處理欄；R01 安排一次桌上檢核。','owner':'R02（示範紀錄角色）；R03（示範覆核角色）','due':'2026-01-16（合成期限）','attachments':'SYN-ATT-001 至 SYN-ATT-004；均為合成索引項，非實際附件。','review':'SYN-REV-001；2026-01-14 09:40；R03；狀態 SIMULATED_CHECK_ONLY。沒有真人簽名、授權證明或協會核准。','archive':'SAMPLE_ARCHIVE_ONLY/2026/01/MEETING/SYN-044-M01（虛構定位，不是本會實際路徑）','completeness':'12/12 示範欄位已填；來源、覆核軌跡及保存欄位都標為 SAMPLE；不是 REAL 證據。'},
 {'id':'SYN-044-D01','type':'當面討論紀錄','date':'2026-01-14','time':'10:05–10:15','place':'示範會議室 A','participants':'R02 示範紀錄角色；R03 示範覆核角色','topic':'會後發現一筆附件未標版本','source':'SYN-ATT-005 示範即時討論紀錄頁；關聯 SYN-044-M01','issue':'一份示範附件只有檔名，沒有可辨認的版次或原始消息定位。','opinions':'R03 建議保留現況並標「版本未知」；R02 同意先列缺件，不以檔名推定版本。','decision':'本次討論沒有作成核准或終局決定；明確記為「未決/待原始來源」，以郵件 SYN-044-E01 追蹤。','action':'R02 取得原始消息與附件版次；若取不到，維持 HOLD 並回報，不得補造來源。','owner':'R02（示範紀錄角色）','due':'2026-01-15（合成期限）','attachments':'SYN-ATT-005；只代表合成紀錄欄位，沒有真實手寫筆記。','review':'SYN-REV-002；2026-01-14 10:20；R03；SIMULATED_CAPTURE_CHECK，不是核准。','archive':'SAMPLE_ARCHIVE_ONLY/2026/01/DISCUSSION/SYN-044-D01（虛構定位）','completeness':'12/12 示範欄位已填；決定狀態明確為未決，仍需後續原件；不是 REAL 證據。'},
 {'id':'SYN-044-E01','type':'電子郵件往返紀錄','date':'2026-01-14 至 2026-01-15','time':'4 封合成訊息','place':'電子郵件示範往返','participants':'R02 示範寄件角色；R03 示範收件/覆核角色','topic':'補齊索引中的原始來源、附件版次及覆核定位','source':'SYN-ATT-006 至 SYN-ATT-009；四封訊息正文及附件均為 SYNTHETIC。','issue':'需要把會議決議和會後未決附件明確串連；不能把寄送草稿寫成核准。','opinions':'R02 提供索引 v0.1；R03 要求原件定位與版本欄分開；R02 提供 v0.2 並保留一筆版本未知；R03 回覆示範欄位檢核結果。','decision':'示範追蹤欄記錄「欄位檢核完成；非正式核准」。最終核准/簽核狀態在 REAL 使用時必須由有效權責和可驗證原件證明。','action':'R02 保留四封原始往返、v0.1/v0.2 差異及附件索引；SYN-044-X01 的缺件仍維持 HOLD。','owner':'R02（示範紀錄角色）','due':'2026-01-16（合成期限）','attachments':'SYN-ATT-006 至 SYN-ATT-009；版本和內容全為虛構。','review':'SYN-REV-003；2026-01-15 10:40；R03；SIMULATED_FIELD_CHECK_ONLY，沒有真實簽核。','archive':'SAMPLE_ARCHIVE_ONLY/2026/01/EMAIL/SYN-044-E01（虛構定位）','completeness':'12/12 示範欄位已填；四封訊息時序及版次互相一致；不是 REAL 證據。'},
 {'id':'SYN-044-X01','type':'缺件郵件追蹤','date':'2026-01-15','time':'15:00','place':'電子郵件示範缺件項','participants':'R02 示範紀錄角色；R03 示範覆核角色','topic':'附件版本未知且原始郵件未取得','source':'SYN-ATT-010 缺件示範項；沒有可核實原始郵件或附件。','issue':'只能看到一個未標版次的示範檔名，無法確認附件來自哪封郵件及其形成時點。','opinions':'R03 要求不要猜版本；R02 同意保留 UNKNOWN 並請求原件。','decision':'HOLD；未簽核、未歸檔為完整紀錄，不計入完整樣本。','action':'取得原始郵件標頭、原始附件及版次；若未取得，標示未完成並保留追蹤。','owner':'R02（示範紀錄角色）','due':'2026-01-16（合成期限）','attachments':'SYN-ATT-010；只有示範缺件代號，並無實際文件。','review':'無簽核；原因為原件與版次不足。','archive':'不得進正式完整紀錄庫；只列 SAMPLE exception log。','completeness':'9/12 示範欄位；缺原始來源、有效簽核軌跡及正式保存定位；狀態 HOLD。'}
]
record_control_fields={
 'SYN-044-M01':{
  'timezone':'合成示範未指定時區；實際使用須照原始訊息或系統記錄時區，無法確認時標示 UNKNOWN，不得推定。',
  'signoff':'SAMPLE欄位示範：沒有真人簽署、簽名、權限證明或協會核准；實際使用須附有權簽署原件或可驗證系統軌跡。',
  'correction':'本合成案例未另行主張更正；實際更正須保留原件，記錄來源、原因、提出者、覆核者及後續追蹤。',
 },
 'SYN-044-D01':{
  'timezone':'合成示範未指定時區；實際使用須照原始訊息或系統記錄時區，無法確認時標示 UNKNOWN，不得推定。',
  'signoff':'SAMPLE欄位示範：沒有真人簽署、簽名、權限證明或協會核准；實際使用須附有權簽署原件或可驗證系統軌跡。',
  'correction':'SYN-ATT-005 的版次/來源在示範中為 UNKNOWN；由 SYN-044-E01 追蹤，取得並核對原件前維持 HOLD。',
 },
 'SYN-044-E01':{
  'timezone':'合成示範未指定時區；實際使用須保留原始郵件標頭或受控匯出中的時區，不得推定。',
  'signoff':'SAMPLE欄位示範：SYN-REV-003 只代表模擬欄位檢核，不是真人簽署、權限證明或正式核准。',
  'correction':'保留 v0.1 至 v0.2 版本鏈；SYN-ATT-010 維持 UNKNOWN/HOLD，不得併入電子郵件往返。',
 },
 'SYN-044-X01':{
  'timezone':'合成示範未指定時區；取得原始郵件後依原始標頭記錄，不得推定。',
  'signoff':'尚未取得可驗證證據；原始郵件及附件/版次尚未取得，維持 HOLD。',
  'correction':'HOLD；取得原始郵件、附件/版次及可驗證追蹤前，不得簽核或歸檔為完整紀錄。',
 },
}
records[0]['completeness']='12/12示範欄位均有SAMPLE值；簽核、權限及保存仍是示範欄位，不代表本會已簽核或存檔。不是REAL證據。'
records[1]['completeness']='12/12示範欄位均有值；未決附件版本明確標UNKNOWN並追蹤；簽核與保存是SAMPLE欄位，不代表本會已簽核或存檔。'
records[2]['completeness']='12/12示範欄位均有SAMPLE值；四封訊息時序與版本一致；簽核及保存非本會紀錄，不代表REAL證據。'
messages=[
 {'id':'SYN-044-EM01','date':'2026-01-14 11:20','from':'R02 示範寄件角色','to':'R03 示範覆核角色','subject':'紀錄索引欄位示範 v0.1','body':'依 SYN-044-M01 製作 v0.1。請確認來源識別、附件版次與保存定位是否分欄；此寄送是草稿檢核，不代表核准。','attachment':'SYN-ATT-006 索引 v0.1'},
 {'id':'SYN-044-EM02','date':'2026-01-14 14:10','from':'R03 示範覆核角色','to':'R02 示範寄件角色','subject':'Re：紀錄索引欄位示範 v0.1','body':'請增列原始消息定位及覆核/簽核軌跡；版本未知時保留 UNKNOWN。附件先保留原版，再記更正關係。','attachment':'無；訊息本身為 SYNTHETIC'},
 {'id':'SYN-044-EM03','date':'2026-01-15 09:15','from':'R02 示範寄件角色','to':'R03 示範覆核角色','subject':'紀錄索引欄位示範 v0.2','body':'已增列來源與簽核分欄，並連結 SYN-044-M01、SYN-044-D01。另將一筆附件版次未知列為 HOLD，未推定來源。','attachment':'SYN-ATT-007 索引 v0.2；SYN-ATT-010 缺件代號'},
 {'id':'SYN-044-EM04','date':'2026-01-15 10:40','from':'R03 示範覆核角色','to':'R02 示範寄件角色','subject':'Re：紀錄索引欄位示範 v0.2','body':'示範欄位檢核完成；僅表示本合成案例欄位可追溯，非本會核准、非真人簽名，也不能替代正式授權流程。','attachment':'SYN-ATT-009 合成檢核軌跡'}
]
attachments=[
 ('SYN-ATT-001','會議通知','vSYN-1','SYN-044-M01','合成通知項；需以實際通知原件替換'),
 ('SYN-ATT-002','出席欄','vSYN-1','SYN-044-M01','合成欄位；不得當作真實簽到'),
 ('SYN-ATT-003','會議議程','vSYN-1','SYN-044-M01','合成議程；需連結真實形成來源'),
 ('SYN-ATT-004','會議紀錄索引','v0.1→v0.2','SYN-044-M01','合成版本鏈；需保留實際原版/修訂版與差異'),
 ('SYN-ATT-005','即時討論紀錄頁','vSYN-1','SYN-044-D01','合成紀錄項；需由實際參與角色核對'),
 ('SYN-ATT-006','紀錄索引草稿','v0.1','SYN-044-E01','EM01附件；合成草稿'),
 ('SYN-ATT-007','紀錄索引草稿','v0.2','SYN-044-E01','EM03附件；合成修訂版'),
 ('SYN-ATT-008','四封往返訊息','vSYN-1','SYN-044-E01','合成郵件線；REAL時保留完整標頭與原始格式'),
 ('SYN-ATT-009','欄位檢核軌跡','vSYN-1','SYN-044-E01','合成檢核項；不是有效簽章或正式核准'),
 ('SYN-ATT-010','版次未知缺件項','UNKNOWN','SYN-044-X01','合成缺件示範；REAL時必須取得原始訊息和附件')
]

# Word helpers
def set_run(run,size=10.5,bold=False,color=TEXT):
    run.font.name=FONT; run.font.size=Pt(size); run.font.bold=bold; run.font.color.rgb=RGBColor.from_string(color)
    rpr=run._element.get_or_add_rPr(); rfonts=rpr.rFonts
    if rfonts is None: rfonts=OxmlElement('w:rFonts'); rpr.insert(0,rfonts)
    for k in ('ascii','hAnsi','eastAsia','cs'): rfonts.set(qn('w:'+k),FONT)

def set_cell(cell,text,header=False,shade=None):
    cell.text=str(text)
    cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.TOP
    if shade:
        tcPr=cell._tc.get_or_add_tcPr(); shd=tcPr.find(qn('w:shd'))
        if shd is None: shd=OxmlElement('w:shd'); tcPr.append(shd)
        shd.set(qn('w:fill'),shade)
    for p in cell.paragraphs:
        p.paragraph_format.space_before=Pt(0); p.paragraph_format.space_after=Pt(2); p.paragraph_format.line_spacing=1.04
        for run in p.runs: set_run(run,9.5,header,WHITE if header else TEXT)

def cant_split(row):
    trPr=row._tr.get_or_add_trPr(); el=OxmlElement('w:cantSplit'); trPr.append(el)

def add_table(doc,headers,rows,widths=None,compact=False):
    t=doc.add_table(rows=1,cols=len(headers)); t.style='Table Grid'; t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.autofit=False
    if widths:
        for i,w in enumerate(widths):
            t.columns[i].width=Inches(w)
            for c in t.columns[i].cells: c.width=Inches(w)
    for i,h in enumerate(headers): set_cell(t.rows[0].cells[i],h,True,NAVY)
    trPr=t.rows[0]._tr.get_or_add_trPr(); rep=OxmlElement('w:tblHeader'); rep.set(qn('w:val'),'true'); trPr.append(rep); cant_split(t.rows[0])
    for ri,row in enumerate(rows):
        cells=t.add_row().cells; cant_split(t.rows[-1])
        if widths:
            for i,w in enumerate(widths): cells[i].width=Inches(w)
        for i,val in enumerate(row): set_cell(cells[i],val,False,PALE if ri%2==0 else None)
    # consistent cell padding
    for row in t.rows:
        for c in row.cells:
            tcPr=c._tc.get_or_add_tcPr(); mar=tcPr.first_child_found_in('w:tcMar')
            if mar is None: mar=OxmlElement('w:tcMar'); tcPr.append(mar)
            for side,val in [('top','70'),('start','90'),('bottom','70'),('end','90')]:
                node=mar.find(qn('w:'+side))
                if node is None: node=OxmlElement('w:'+side); mar.append(node)
                node.set(qn('w:w'),val); node.set(qn('w:type'),'dxa')
    doc.add_paragraph().paragraph_format.space_after=Pt(1)
    return t

def para(doc,text='',bold_prefix=None,style=None,after=4):
    p=doc.add_paragraph(style=style) if style else doc.add_paragraph()
    p.paragraph_format.space_after=Pt(after); p.paragraph_format.line_spacing=1.12
    if bold_prefix and text.startswith(bold_prefix):
        a=p.add_run(bold_prefix); set_run(a,10.5,True,NAVY); b=p.add_run(text[len(bold_prefix):]); set_run(b,10.5)
    else:
        r=p.add_run(text); set_run(r,10.5)
    return p

def heading(doc,text,level=1):
    p=doc.add_paragraph(style=f'Heading {level}')
    p.paragraph_format.keep_with_next=True; p.paragraph_format.space_before=Pt(10 if level==1 else 7); p.paragraph_format.space_after=Pt(4)
    r=p.add_run(text); set_run(r,14 if level==1 else 11.5,True,NAVY)
    return p

def kv(doc,rows): return add_table(doc,['項目','示範紀錄內容'],rows,[1.45,5.72])

def add_record_sample(doc,rec,detail_rows):
    heading(doc,rec['type']+'｜'+rec['id'],2)
    para(doc,'SAMPLE / SYNTHETIC｜以下事件、角色、時間、決定、附件及保存位置均為合成示範，沒有協會實際紀錄或簽名。',after=3)
    kv(doc,detail_rows)

# Document and page setup
doc=Document(); sec=doc.sections[0]; sec.page_width=Inches(8.27); sec.page_height=Inches(11.69)
sec.top_margin=Inches(0.62); sec.bottom_margin=Inches(0.62); sec.left_margin=Inches(0.66); sec.right_margin=Inches(0.66)
normal=doc.styles['Normal']; normal.font.name=FONT; normal.font.size=Pt(10.5); normal.font.color.rgb=RGBColor.from_string(TEXT)
normal._element.rPr.rFonts.set(qn('w:eastAsia'),FONT); normal.paragraph_format.space_after=Pt(4); normal.paragraph_format.line_spacing=1.12
for name,size in [('Heading 1',14),('Heading 2',11.5),('Title',20)]:
    st=doc.styles[name]; st.font.name=FONT; st.font.size=Pt(size); st.font.bold=True; st.font.color.rgb=RGBColor.from_string(NAVY); st._element.rPr.rFonts.set(qn('w:eastAsia'),FONT)
# The built-in Word Title style can carry a bottom paragraph border. Remove
# that decoration from the style and the actual title paragraph so the title
# remains a clean heading without a horizontal rule.
title_ppr=doc.styles['Title']._element.pPr
if title_ppr is not None:
    for border in list(title_ppr.findall(qn('w:pBdr'))):
        title_ppr.remove(border)
header=sec.header.paragraphs[0]; header.alignment=WD_ALIGN_PARAGRAPH.RIGHT
rr=header.add_run('原始點協會作業參考　｜　SAMPLE / SYNTHETIC'); set_run(rr,8.5,True,MUTED)
footer=sec.footer.paragraphs[0]; footer.alignment=WD_ALIGN_PARAGRAPH.CENTER
rr=footer.add_run('DOCX 0044　候選示範　非本會實際紀錄／簽核／核准'); set_run(rr,8.5,False,MUTED)

# Front matter
p=doc.add_paragraph(style='Title')
title_ppr=p._p.get_or_add_pPr()
for border in list(title_ppr.findall(qn('w:pBdr'))):
    title_ppr.remove(border)
p.paragraph_format.space_after=Pt(5); set_run(p.add_run('討論 會議與電子郵件完整紀錄'),20,True,NAVY)
para(doc,'DOCX 0044｜I09-E04｜方框045｜R01｜候選示範｜2026-10-17｜未生效',after=7)
kv(doc,[
 ('用途','把討論、會議及電子郵件往來的原始來源、意見、決定或未決狀態、附件版本、簽核追蹤與保存位置連成可調閱紀錄。'),
 ('使用人','供原始點協會行政承辦整理；實際填表、覆核與簽核角色須先依本會有效權責確認，本文件不指定真人或授權人。'),
 ('使用時點','每次討論、會議或郵件往來形成時記錄；先保存原始訊息及附件，再完成摘要、覆核和正式歸檔。'),
 ('操作順序','登錄來源 → 分開記意見與決定 → 核對附件版本 → 記下有效覆核/簽核軌跡 → 登錄實際保存定位；缺件則 HOLD。'),
 ('輸出與狀態','輸出逐件索引及完整紀錄；本文完整案例均為 SAMPLE/SYNTHETIC，不是本會實際討論、會議、郵件、簽核或歸檔。')
])
heading(doc,'官方要求與使用界線',1)
para(doc,'官方方框 045（I09-E04）：「所有的討論、 會議或E-mail均留有完整紀錄並經簽核後存檔。」官方佐證表定位：第 3 頁。DOCX 編號 0044、要求代碼 I09-E04 與官方方框序號 045 是三個不同欄位。')
para(doc,'本文示範如何留存訊息和核准追蹤；不表示本會已採用本文制度、完成簽核或保存任何實際紀錄。虛構的覆核代碼只用來展示欄位；不得貼成真實簽名或有效核准。')

heading(doc,'1. 哪些內容要形成一筆紀錄',1)
para(doc,'先以形成時的原件為主體；摘要不能替代原件。每筆以唯一識別碼串起原始訊息、附件、修訂版、覆核及保存定位。')
add_table(doc,['紀錄類型','應保留的原始內容','完成判斷及常見退件'],[
 ('會議','通知或召集來源、日期時間、議程、出席/缺席角色、發言與證據、逐項決定、責任及原件載明期限、附件版本、覆核簽核。','議程或名單不可代替討論及決議；沒有有效簽核或原始出席來源不得列完整。'),
 ('當面/電話討論','形成時間、參與角色、討論脈絡、各方意見、是否有決定、後續行動、紀錄形成者與覆核軌跡。','未作成決定時明記「未決」；不得把承辦摘要改寫成共識或核准。'),
 ('電子郵件','完整寄件/收件、日期時間、主旨、往返順序、原始格式、附件名稱/版本及各訊息連結。','只存最後一封或截圖不等於完整往返；附件版本、簽核原件或保存定位缺失時列 HOLD。')
],[1.25,3.45,2.47])

heading(doc,'2. 共通欄位與查核規則',1)
add_table(doc,['欄位','填寫與核對方式'],[
 ('識別與時間','每筆使用不重複識別碼；記原件時間與時區，製表日另欄，不互相替代。'),
 ('類型與參與角色','標示會議、口頭/電話討論或郵件；角色依原件核對。沒有姓名或出席證據時不得推定。'),
 ('議題與脈絡','摘要能回到原始議程、主旨或訊息段落；保留不同意見與原始語意。'),
 ('決定狀態','分列提案、已決、未決、撤回；列決定來源、理由及限制。沉默不等於同意。'),
 ('責任與期限','只填原件明載或正式確認的責任/期限；未載明填「未載」並記後續確認方式。'),
 ('附件及版本','逐件列檔名、原件版次、所屬訊息、形成/收受時間及修訂關係；保留原版。'),
 ('覆核與簽核','核對覆核/簽核者權限來源、時間、結果及可驗證原件或系統軌跡。承辦摘要不是簽核。'),
 ('保存與調閱','記實際受控系統/路徑、權限和調閱結果；保存期限依本會有效核定規範，不在此假設年限。'),
 ('更正與例外','保留前版、差異、原因、提出/覆核來源；缺原件或版本未知即標 UNKNOWN/HOLD，不補造。')
],[1.55,5.62])

heading(doc,'3. SAMPLE案例索引與完整度判讀',1)
para(doc,'以下四筆均為同一合成檔案保存情境，不是課程需求訪談或採購評選；每筆的訊息、人物角色、時間、附件、覆核軌跡和定位均是虛構。')
add_table(doc,['示範識別碼','類型與時點','示範結論','狀態'],[
  (records[0]['id'],'會議｜2026-01-14 09:00–09:35','議題、來源、意見、決定、覆核、簽核欄位及保存狀態均明列。','SAMPLE 模型欄位填妥'),
  (records[1]['id'],'當面討論｜2026-01-14 10:05–10:15','沒有終局決定；附件版本 UNKNOWN，轉郵件追蹤且欄位明列。','SAMPLE 模型欄位填妥'),
  (records[2]['id'],'郵件往返｜2026-01-14 至 2026-01-15','四封時序、附件版本、覆核與簽核狀態互相連結。','SAMPLE 模型欄位填妥'),
 (records[3]['id'],'缺件郵件｜2026-01-15 15:00','原始郵件/附件版次缺失；不簽核、不歸為完整。','HOLD 不完整')
],[1.25,1.75,3.05,1.12])
para(doc,'樣本指標（僅算這四筆合成紀錄）：12項模型欄位均有示範值 3 筆 ÷ 登錄樣本 4 筆 × 100% = 75%。分母是本頁列示的 4 筆示範事件，不是本會所有實際紀錄；75% 不代表實績或合規率。此比例只計欄位模型填寫狀態；不能證明真實簽核、權限或正式歸檔。')

heading(doc,'4. SAMPLE會議紀錄',1)
meeting_details=[
 ('紀錄識別碼／版本',records[0]['id']+'｜vSYN-1（示範）'),
 ('類型／日期時間／時區',records[0]['type']+'；'+records[0]['date']+' '+records[0]['time']+'；'+record_control_fields[records[0]['id']]['timezone']),
 ('議題／原始來源識別與定位',records[0]['topic']+'；來源：'+records[0]['source']),
 ('參與角色及核對來源',records[0]['place']+'；'+records[0]['participants']+'；出席欄 SYN-ATT-002 為合成欄位，沒有真人姓名或真實簽到。'),
 ('議程、意見及原始消息定位','議程：① 原始消息定位；② 附件版次；③ 覆核、簽核與保存欄位。意見：'+records[0]['opinions']+' 定位：SYN-ATT-001 至 SYN-ATT-003（合成來源）。'),
 ('決定狀態與理由/來源',records[0]['decision']),
 ('責任角色／行動／期限與來源',records[0]['owner']+'；'+records[0]['action']+' 期限：'+records[0]['due']+'（合成）。'),
 ('附件名稱／原版次／消息關聯／差異',records[0]['attachments']),
 ('覆核者／時間／結果／權責依據',records[0]['review']+' 權責依據未在此證明。'),
 ('簽核者／時間／簽核原件或系統軌跡',record_control_fields[records[0]['id']]['signoff']),
 ('正式保存位置／權限／調閱結果',records[0]['archive']+'；權限與調閱未經真實系統驗證。'),
 ('更正、缺證、HOLD及後續追蹤',record_control_fields[records[0]['id']]['correction']),
 ('欄位模型判讀',records[0]['completeness'])
]
assert len(meeting_details)==13, 'Meeting sample must show 12 reusable form fields plus its field-model judgment.'
add_record_sample(doc,records[0],meeting_details)

heading(doc,'5. SAMPLE當面討論紀錄',1)
discussion_details=[
 ('紀錄識別碼／版本',records[1]['id']+'｜vSYN-1（示範）'),
 ('類型／日期時間／時區',records[1]['type']+'；'+records[1]['date']+' '+records[1]['time']+'；'+record_control_fields[records[1]['id']]['timezone']),
 ('議題／原始來源識別與定位',records[1]['topic']+'；來源：'+records[1]['source']),
 ('參與角色及核對來源',records[1]['participants']+'；角色代碼非本會名冊；SYN-ATT-005 是合成定位，沒有真實手寫筆記。'),
 ('議程、意見及原始消息定位','討論脈絡：會後核對示範索引時發現附件未標版次。'+records[1]['issue']+' 意見：'+records[1]['opinions']+' 定位：SYN-ATT-005（合成）。'),
 ('決定狀態與理由/來源',records[1]['decision']),
 ('責任角色／行動／期限與來源',records[1]['owner']+'；'+records[1]['action']+' 期限：'+records[1]['due']+'（合成）。'),
 ('附件名稱／原版次／消息關聯／差異',records[1]['attachments']+'；原版次 UNKNOWN，未依檔名推定。'),
 ('覆核者／時間／結果／權責依據',records[1]['review']+' 權責依據未在此證明。'),
 ('簽核者／時間／簽核原件或系統軌跡',record_control_fields[records[1]['id']]['signoff']),
 ('正式保存位置／權限／調閱結果',records[1]['archive']+'；僅為合成定位，權限與調閱未經真實系統驗證。'),
 ('更正、缺證、HOLD及後續追蹤',record_control_fields[records[1]['id']]['correction']),
 ('欄位模型判讀',records[1]['completeness'])
]
assert len(discussion_details)==13, 'Discussion sample must show 12 reusable form fields plus its field-model judgment.'
add_record_sample(doc,records[1],discussion_details)

heading(doc,'6. SAMPLE電子郵件往返紀錄',1)
para(doc,'郵件示例以四封連續往返呈現；寄收角色、日期、文字、附件與版本皆為 SAMPLE。實際使用時保存原始 .eml 或受控郵件匯出及附件原檔，不能只留本頁摘要。')
email_rows=[(m['id']+'\n'+m['date'],f"寄件：{m['from']}\n收件：{m['to']}\n主旨：{m['subject']}\n內容：{m['body']}\n附件：{m['attachment']}") for m in messages]
add_table(doc,['訊息與時點','完整摘要、寄收角色及附件'],email_rows,[1.65,5.52])
kv(doc,[
 ('線程識別與完整性','SYN-044-E01；EM01 → EM02 → EM03 → EM04。四封合成訊息都列出時間、寄收角色、主旨、內容和附件，沒有缺漏真實訊息的主張。'),
 ('版本對照','SYN-ATT-006 v0.1 → SYN-ATT-007 v0.2；保留差異和所屬訊息。SYN-ATT-010 版次未知，不能併入 v0.2。'),
 ('覆核/簽核邊界','SYN-REV-003 是合成欄位檢核事件，不是本會正式核准、權限證明或真人簽名。REAL 狀態須附有效權責依據及正式簽核原件。'),
 ('保存定位','SAMPLE_ARCHIVE_ONLY/2026/01/EMAIL/SYN-044-E01；虛構、不可調閱，不能填成正式保存位置。')
])

heading(doc,'7. 附件版本索引與跨紀錄連結',1)
add_table(doc,['示範附件ID','名稱/版本','所屬紀錄','核對與真實替換規則'],[(a,f'{b} / {c}',d,e) for a,b,c,d,e in attachments],[1.13,1.52,1.28,3.24])
para(doc,'同一檔案若被轉寄或修訂，以原始寄送訊息、附件位元組及版次關聯核對；索引不覆寫原件。SYN-044-M01 → SYN-044-D01 → SYN-044-E01 只表示本合成案例的關聯，不與 DOCX 0043 的需求單位訪談/統計資料共用或合併事實。',after=5)

heading(doc,'8. 完整度核對與例外退件',1)
add_table(doc,['檢核結果','示範數據/計算','處置'],[
 ('欄位模型填寫狀態','12項示範欄位填妥 3 筆；登錄 4 筆；X01 有 3 欄保持缺證狀態。3 ÷ 4 × 100% = 75%。','只描述本頁SAMPLE欄位；不外推為本會完整紀錄或合規率。'),
 ('模型欄位判準','12個槽位均填入示範值或明確 UNKNOWN/HOLD；真實來源、有效簽核、權限與正式保存仍須另以原件核驗。','SAMPLE欄位填妥不等於滿足官方簽核後存檔要求。'),
 ('SYN-044-X01','示範完成 9/12；原始郵件、附件版次、正式簽核/保存定位未取得。','HOLD；不簽核、不計完整、不歸入正式完整紀錄庫。')
],[1.35,3.05,2.77])
add_table(doc,['問題或退件條件','必須怎麼記','解除 HOLD 的證據'],[
 ('找不到原始郵件/會議/討論來源','來源欄填 UNKNOWN，保留查找時間、責任角色及追蹤期限；不可用摘要代替原件。','原始郵件匯出、受控系統記錄、原始會議/討論形成資料及可核對定位。'),
 ('附件無版次或與正文不一致','保留收到的原檔；記差異、版本未知及來源；不要自行改名成已核實版次。','能連到原始寄送訊息的附件檔及版本差異紀錄。'),
 ('未能證明簽核者權限或簽核軌跡','標示 NOT VERIFIED/HOLD；不代簽、不補簽、不將覆核意見當核准。','適用權責依據、正式簽核原件或可驗證系統稽核軌跡。'),
 ('保存定位或保存規範未確認','不得填示範路徑為正式路徑；期限只引用有效核定規範。','正式受控位置、調閱核對及有效保存規範。'),
 ('整筆停止與結案條件','任一必要原始消息、授權、附件定位、簽核軌跡或正式保存位置未能核實時，該筆維持 HOLD；不得把示範或其他文件補造成 REAL 證據。','取得可驗證原件、權責與簽核軌跡、正式保存定位及可調閱紀錄後，重新核對並記錄解除 HOLD 的人與時間。')
],[1.65,2.7,2.82])

heading(doc,'9. REAL 使用欄位及替換清單',1)
para(doc,'開始正式使用時，先確認本會現行權責與保存規範，再以真實原件逐筆取代 SAMPLE。若任何必要來源未取得，保留 UNKNOWN/HOLD；不得把本合成案例複製成 REAL 紀錄。逐事實清冊見同包 `evidence/SYNTHETIC_REPLACEMENT_REGISTER_R01.csv`。')
add_table(doc,['實際替換欄位','所需真實原件/驗證','退件條件'],[
 ('日期、時間、類型、參與/寄收角色','原始郵件標頭、召集通知、可核對出席/討論來源。','只有事後回憶或無法確認角色時不得判完整。'),
 ('議題、意見、決定、行動及期限','原始議程/消息/紀錄，明確區分提案、決定及未決。','意見被改寫成決議、責任或期限無來源。'),
 ('附件名稱、版次與差異','原始附件與來源訊息；修訂前後版本及變更依據。','附件無法定位或版本未知卻列成已核實。'),
 ('覆核/簽核與權限','本會適用的有效權責依據、正式簽核原件或系統稽核軌跡。','未證權限、仿簽、代簽、把示範回覆當核准。'),
 ('歸檔路徑、調閱及保存期限','正式受控保存系統、可重現調閱結果、現行核定保存規範。','填入SAMPLE路徑、猜測年限或無法調閱。')
],[1.45,3.38,2.34])

heading(doc,'10. 可複製的單筆紀錄表',1)
para(doc,'以下欄位供逐筆新增；空表只作實際填寫附件，不能代替前述完整示範。完成一筆後附來源原件和附件索引，並由有效權責者完成簽核及保存定位。')
form=[
 ('紀錄識別碼／版本','','類型／形成日期時間／時區',''),
 ('主旨或議題／原始來源識別與定位','','參與/寄件/收件角色及核對來源',''),
 ('議程、意見及原始消息定位','','決定狀態（已決/未決/撤回）與理由',''),
 ('責任角色／行動／期限與來源','','附件名稱／原版次／訊息關聯／差異',''),
 ('覆核者／時間／結果／權責依據','','簽核者／時間／簽核原件或系統軌跡',''),
 ('正式保存位置／權限／調閱結果','','更正、缺證、HOLD及後續追蹤','')]
add_table(doc,['欄位','填寫內容','欄位','填寫內容'],form,[1.55,1.99,1.55,1.99])

heading(doc,'11. 官方要求對照與文件邊界',1)
add_table(doc,['官方要求片語','本文件直接對應','不可混用的鄰件'],[
 ('討論、會議或E-mail','§1三類準入；§4會議；§5當面討論；§6四封郵件往返。','DOCX 0043/I09-E03 是需求單位訪談與統計分析，不由本件代替。'),
 ('完整紀錄','§2欄位規則；§3索引；§7附件/版本；§8完整度與缺件退件。','DOCX 0045/I10-E01 是採購/甄選程序，不把採購評選內容塞入本件。'),
 ('經簽核後存檔','§4/§5/§6只提供SAMPLE簽核追蹤欄；§8及§9要求真實權責、簽核原件和正式保存定位。','本文沒有協會真實核准、真人簽名或正式存檔路徑；需有權來源逐筆替換。')
],[1.55,3.5,2.12])

# Metadata and deterministic outputs
doc.core_properties.title='討論 會議與電子郵件完整紀錄'
doc.core_properties.subject='DOCX 0044 / I09-E04 / official checkbox 045; candidate SAMPLE/SYNTHETIC only'
doc.core_properties.author=''
doc.core_properties.keywords='TTQS, I09-E04, SAMPLE, SYNTHETIC'
OUT.parent.mkdir(parents=True,exist_ok=True); doc.save(OUT)

# A fact-level register generated from the exact sample structures used above.
rows=[]
def add_fact(fid,value,kind,locator,real_source,rule,responsible='實際承辦角色（待本會權責核實）'):
    rows.append({'fact_id':fid,'fact_type':kind,'synthetic_value':str(value),'body_locator':locator,'real_source_to_replace':real_source,'verification_rule':rule,'responsible_role':responsible,'boundary':'SAMPLE/SYNTHETIC only; not an association record, approval, signature, performance, or archive.'})
for ri,rec in enumerate(records,1):
    for k,label in [('id','識別碼'),('type','紀錄類型'),('date','日期'),('time','時間/區間'),('place','地點/媒介'),('participants','角色/參與者'),('topic','議題'),('source','原始來源定位'),('issue','問題/脈絡'),('opinions','意見'),('decision','決定/未決狀態'),('action','後續行動'),('owner','責任角色'),('due','期限'),('attachments','附件/版本'),('review','覆核結果'),('archive','保存定位'),('completeness','欄位模型判讀')]:
        add_fact(f'SYN044-R{ri:02d}-{k.upper()}',rec[k],'record_field',f'§{3+ri}; {rec["id"]}; {label}',f'原始會議/討論/郵件、有效權責依據、附件及正式保存系統',f'逐項比對原件，不推定缺漏；核准/簽核僅採有效權責與可驗證軌跡。')
for ri,rec in enumerate(records,1):
    control=record_control_fields[rec['id']]
    for key,label in [('timezone','時區欄位'),('signoff','簽核欄位狀態'),('correction','更正/缺證/HOLD追蹤')]:
        add_fact(f'SYN044-R{ri:02d}-{key.upper()}',control[key], 'sample_control_field',f'§{3+ri}; {rec["id"]}; {label}',f'原始訊息/系統時區、正式簽核原件或系統軌跡、以及原始更正/缺件來源',f'只以真實來源填入；合成狀態不能證明本會簽核、權限或正式歸檔。')
for mi,msg in enumerate(messages,1):
    for k,label in [('id','訊息識別碼'),('date','訊息時間'),('from','寄件角色'),('to','收件角色'),('subject','主旨'),('body','訊息內容'),('attachment','附件')]:
        add_fact(f'SYN044-EM{mi:02d}-{k.upper()}',msg[k],'email_message',f'§6; {msg["id"]}; {label}',f'完整原始郵件標頭、正文及原始附件',f'依原始郵件時間排序並核對寄收對象及附件版本。','實際郵件紀錄承辦/覆核角色（待核實）')
for ai,(aid,name,version,record_ref,note) in enumerate(attachments,1):
    for k,val,label in [('name',name,'附件名稱'),('version',version,'附件版次'),('record',record_ref,'所屬紀錄'),('note',note,'來源/限制')]:
        add_fact(f'SYN044-ATT{ai:02d}-{k.upper()}',val,'attachment_index',f'§7; {aid}; {label}',f'原始附件檔與寄送/會議來源',f'版次須由原始附件及其來源訊息交叉核對，不以檔名推定。')
for fid,value,loc,source in [
 ('SYN044-CALC-N','4筆示範紀錄','§3/§8 樣本分母','當期完整事件登錄清冊'),
 ('SYN044-CALC-COMPLETE','3筆示範欄位完整模型','§3/§8 樣本分子','逐筆欄位與原始來源核對結果'),
 ('SYN044-CALC-INCOMPLETE','1筆HOLD','§3/§8 缺件數','缺件追蹤與後續來源回收結果'),
 ('SYN044-CALC-RATE','3/4=75%','§3/§8 樣本完整度公式','分子/分母及指定統計期間的原始登錄資料')]:
    add_fact(fid,value,'synthetic_calculation',loc,source,'只限明確樣本母體與期間重算；REAL報告須重新計算，不能沿用示範比例。')
with REG.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['fact_id','fact_type','synthetic_value','body_locator','real_source_to_replace','verification_rule','responsible_role','boundary'])
    w.writeheader(); w.writerows(rows)

# Technical receipt binds checks to the exact candidate bytes.
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
with zipfile.ZipFile(OUT) as z: zip_ok=z.testzip() is None
check=Document(OUT)
receipt={'project_id':'TTQS_ONE','doc_id':'0044','requirement_id':'I09-E04','official_checkbox_sequence':'045','revision':'R01','candidate_path':'candidate/0044_R01.docx','candidate_sha256':sha(OUT),'bytes':OUT.stat().st_size,'docx_zip_integrity':'PASS' if zip_ok else 'FAIL','paragraph_count':len(check.paragraphs),'table_count':len(check.tables),'replacement_register_rows':len(rows),'unique_fact_ids':len({x['fact_id'] for x in rows}),'body_min_font_pt':10.5,'table_min_font_pt':9.5,'sample_boundary':'SAMPLE/SYNTHETIC only; no real association event, signoff, approval, or archive is claimed','historical_candidate_sha256':'427e9ccae8ebf0f3128571057b63602c728ea70c1ea911857fba941c3acfd1d1','method':'Fresh source-only authoring; legacy DOCX inspected for gap discovery and not used as a writing template.'}
(OUT.parents[1]/'technical_integrity_R01.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'docx':str(OUT),'docx_sha256':receipt['candidate_sha256'],'bytes':receipt['bytes'],'paragraphs':receipt['paragraph_count'],'tables':receipt['table_count'],'replacement_rows':len(rows),'unique_fact_ids':receipt['unique_fact_ids'],'zip_integrity':receipt['docx_zip_integrity']},ensure_ascii=False))
