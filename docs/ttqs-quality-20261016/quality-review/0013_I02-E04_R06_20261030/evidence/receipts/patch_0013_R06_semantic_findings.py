from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph
from pathlib import Path
import csv, json, hashlib, shutil

root=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0013_I02-E04_LUNA_TEXT_DRAFT_R01_20261029')
src=root/'candidate'/'0013_I02-E04_R05.docx'
out=root/'candidate'/'0013_I02-E04_R06.docx'
csvsrc=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\GITHUB_STAGING\0013_I02-E04_R05_20261030\sidecar\0013_R05_SYNTHETIC_REPLACEMENT_REGISTER.csv')
csvout=root/'qa'/'0013_R06_SYNTHETIC_REPLACEMENT_REGISTER.csv'
assert src.exists() and csvsrc.exists()
doc=Document(src)

def set_p(p,text):
    if p.runs:
        p.runs[0].text=text
        for r in p.runs[1:]: r.text=''
    else: p.add_run(text)

def replace_para(needle,text):
    hits=[p for p in doc.paragraphs if needle in p.text]
    assert len(hits)==1,(needle,len(hits))
    set_p(hits[0],text)
    return hits[0]

replace_para('先看這裡：','先看這裡：本工作簿示範年度訓練課程如何編製、逐欄核對、送權責流程審查、公開並保存證據。四門 SAMPLE 課程均完整填入九項欄位，可重算欄位填入率、淨授課時數及規劃名額；但四個報名通路皆為 .invalid 保留網域，不是可用連結。示例沒有真實機構名稱、真人、實際訓練、核准、報名、成果或公開紀錄；正式發布維持 HOLD。')
replace_para('依第 7 節公式計算欄位完整度','3. 依第 7 節分別計算欄位填入率、報名通路可用性與規劃總量；這些數字不證明課程已辦理或有人報名。')
replace_para('7.1 公開欄位完整度','7.1 欄位填入率與通路可用性')
replace_para('定義：完整度 =','定義：欄位填入率 = 有值的必要欄位實例數 ÷ 應有必要欄位實例總數 × 100%。此比率只檢查是否填入，不代表內容符合真實來源、報名通路可用、版本已核實或已獲核准。')
replace_para('R-A 初版有值且通過形式檢查者為 35 個欄位實例；C04 報名通路欄缺失。','R-A 初版有值的欄位為 35 個欄位實例；SYN-C04 的報名通路欄缺值，其餘三門填入的網址也都是 .invalid 保留網域。')
replace_para('R-A 完整度 =','R-A 欄位填入率 = 35 ÷ 36 × 100% = 97.222...%，四捨五入至小數一位為 97.2%。SYN-C04 缺少必要通路，四門沒有任何已核實可用的正式通路，故示例狀態為 HOLD；比率不能抵銷缺項。')
replace_para('R-B 修正後有值且通過形式檢查者為 36 個欄位實例。','R-B 修正後 36 個欄位實例均有值；新增的 SYN-C04 網址仍為 .invalid 保留網域。')
replace_para('R-B 完整度 =','R-B 欄位填入率 = 36 ÷ 36 × 100% = 100%。這只表示 SAMPLE 欄位均有值，不表示連結可用、來源／版本已核實、取得真實核准或可發布。')

p72=next(p for p in doc.paragraphs if p.text.startswith('7.2 時數與名額加總'))
new_xml=OxmlElement('w:p')
p72._p.addprevious(new_xml)
usability=Paragraph(new_xml,p72._parent)
usability.style=next(p for p in doc.paragraphs if p.text.startswith('R-B 欄位填入率')).style
usability.add_run('通路可用性另計：可用通路數只計機構控制、由非編輯視角實際開啟並讀回相同課程版本的正式通路。四門課程應有四個通路；R-A 為一門缺值、三門使用 .invalid，R-B 四門均使用 .invalid，因此兩版均為 0/4 已核實可用（0%）。這是 SAMPLE 例示狀態，未執行真實網路連線測試；R-B 仍須 HOLD。')

# Explicitly separate presence from operational route verification.
t4=doc.tables[3]
assert len(t4.rows)==6
assert '2026-11-06' in t4.rows[4].cells[0].text
t4.rows[4].cells[2].text='欄位填入率 36/36 = 100%；已核實可用通路 0/4；發布仍 HOLD'
t4.rows[4].cells[3].text='只表示 SAMPLE 欄位有值；不得推定通路可用、來源已核實或可發布'
t5=doc.tables[4]
assert len(t5.rows)==10 and t5.rows[9].cells[0].text=='報名通路'
t5.rows[9].cells[4].text='填入率只看有無值。正式通路須由機構控制，逐一開啟並讀回相符課程版本，記錄測試時間、版本及覆核角色。缺值、.invalid、未測或錯頁均 HOLD，且不計為可用。'
t13=doc.tables[12]
assert 'SYN-0013-F018' in t13.rows[1].cells[0].text
t13.rows[1].cells[1].text='R-A 的 SYN-C04 通路欄缺值；R-B 補入 .invalid 示例值；四門仍無合格讀回通路'
t13.rows[1].cells[2].text='R-A HOLD；R-B 36/36 只代表欄位填入率；R-A/R-B 已核實可用通路皆為 0/4'
t13.rows[1].cells[3].text='R01 在 R-B 加入不可用保留網域示例值；真實作業須改用機構控制的正式通路並讀回相同課程版本'
t13.rows[1].cells[4].text='SAMPLE 欄位填入率重算為 36/36；通路可用性 0/4；正式發布仍 HOLD'

# The 67-row register now has a role assignment and exact structural locator for every fact.
loc={}
role={}
def add(fid,where,who):
    loc[fid]=where; role[fid]=who
add('F001','§6.1 首段，句「示範機構代號 O-001」','R01')
add('F002','§6.1 年度範圍句；§6.2–§6.5 表7–表10「日期與時段」欄','R01')
add('F003','表3 資料列 R01「示例責任」；§4.2 表4 2026-11-02 列','R01')
add('F004','表3 資料列 R02「示例責任」；§4.2 表4 2026-11-04、2026-11-06 列','R02')
add('F005','表3 資料列 R03「示例責任」；§4.2 表4 2026-11-09 列','R03')
add('F006','表3 資料列 R04「示例責任」；§4.2 表4 2026-11-09 列','R04')
add('F007','表3 資料列 R05「示例責任」；§12.2 原件索引與保管規則','R05')
add('F008','§4.2 表4 日期欄 2026-11-02／R01 初版列','R01')
add('F009','§4.2 表4 日期欄 2026-11-04／R02 檢查列','R02')
add('F010','§4.2 表4 日期欄 2026-11-05／R01 修正列','R01')
add('F011','§4.2 表4 日期欄 2026-11-06／R02 重算列','R02')
add('F012','§4.2 表4 日期欄 2026-11-09／R03、R04 權責檢查列','R03')
add('F013','§6.1 表7–表10「課程代碼」列 SYN-C01 至 SYN-C04','R02')
add('F014','§5 表5 資料列「課程名稱」至「報名通路」共九列','R02')
add('F015','§7.1 段落「本示例課程列數為 4」：4 × 9 = 36','R02')
add('F016','§4.2 表4 2026-11-04 列；§7.1 段落「R-A 初版有值的欄位」','R02')
add('F017','§7.1 段落「R-A 欄位填入率」：35 ÷ 36','R02')
add('F018','§4.2 表4 2026-11-04 列；§6.5 表10「報名通路」；§9 表13 SYN-0013-F018／F019 列','R02')
add('F019','§4.2 表4 2026-11-04 列；§8 表12 HOLD 列；§9 表13 SYN-0013-F018／F019 列','R02')
add('F020','§4.2 表4 2026-11-06 列；§7.1 段落「R-B 修正後 36 個」','R02')
add('F021','§7.1 段落「R-B 欄位填入率」：36 ÷ 36','R02')
add('F022','§7.2 段落「30 小時」；表7–表10「淨授課時數」列','R02')
add('F023','§7.2 段落「74 席」；表7–表10「規劃名額」列','R02')
add('F024','§7.1 段落「R-B 欄位填入率」；§8 表12 PASS（範圍限定）列','R02')
add('F025','§4.2 表4 2026-11-09 列；§8 表12 HOLD 列；§9 表13 REAL-HOLD-02 列','R03')
add('F026','§9 表13 SYN-0013-F026／F027 列；§8 表12 REJECT 列','R02')
add('F027','§9 表13 SYN-0013-F026／F027 列；§8 表12 REJECT 列','R02')

field_names=['課程代碼','課程名稱','適用對象','學習成果','課程內容','授課方式','日期與時段','淨授課時數','規劃名額','報名通路']
sections=['6.2','6.3','6.4','6.5']
tables=[7,8,9,10]
codes=['SYN-C01','SYN-C02','SYN-C03','SYN-C04']
for ci,(sec,tn,code,start) in enumerate(zip(sections,tables,codes,[101,111,121,131])):
    for fi,name in enumerate(field_names):
        fid=f'F{start+fi:03d}'
        who='R01' if fi in [0,1,2,3,4,5,6] else ('R04' if fi==9 else 'R02')
        add(fid,f'§{sec} 表{tn} 資料列「{code}」欄「{name}」',who)

assert len(loc)==67 and len(role)==67 and set(loc)==set(role)

table=doc.tables[18]
assert len(table.rows)==68 and len(table.columns)==4
table.add_column(Inches(0.8))
table.rows[0].cells[2].text='精確定位（章節／表格／資料列／欄位）'
table.rows[0].cells[4].text='SAMPLE 角色碼'
seen=set()
for row in table.rows[1:]:
    fid=row.cells[0].text.strip().replace('SYN-0013-','')
    assert fid in loc and fid not in seen,(fid)
    seen.add(fid)
    row.cells[2].text=loc[fid]
    row.cells[4].text=role[fid]
assert seen==set(loc)

widths=[1.50,2.80,3.15,2.30,0.80]
table.autofit=False
for ci,w in enumerate(widths):
    table.columns[ci].width=Inches(w)
    for row in table.rows: row.cells[ci].width=Inches(w)
for row_idx,row in enumerate(table.rows):
    if row_idx==0:
        trPr=row._tr.get_or_add_trPr()
        hdr=OxmlElement('w:tblHeader'); hdr.set(qn('w:val'),'true'); trPr.append(hdr)
    trPr=row._tr.get_or_add_trPr()
    cant=OxmlElement('w:cantSplit'); trPr.append(cant)
    for cell in row.cells:
        cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
        for p in cell.paragraphs:
            p.paragraph_format.space_before=Pt(0)
            p.paragraph_format.space_after=Pt(0)
            p.paragraph_format.line_spacing=1.0
            for run in p.runs:
                run.font.size=Pt(9.5)
                run.font.name='Microsoft JhengHei'
                rpr=run._element.get_or_add_rPr()
                rfonts=rpr.rFonts
                if rfonts is None:
                    rfonts=OxmlElement('w:rFonts'); rpr.append(rfonts)
                rfonts.set(qn('w:eastAsia'),'Microsoft JhengHei')

# The new fifth crosswalk column and rewritten third header lost the original header formatting.
header=table.rows[0]
source_shd=header.cells[0]._tc.get_or_add_tcPr().find(qn('w:shd'))
assert source_shd is not None
header_fill=source_shd.get(qn('w:fill'))
for cell in header.cells:
    tcPr=cell._tc.get_or_add_tcPr()
    old_shd=tcPr.find(qn('w:shd'))
    if old_shd is not None:
        tcPr.remove(old_shd)
    shd=OxmlElement('w:shd')
    shd.set(qn('w:val'),'clear')
    shd.set(qn('w:color'),'auto')
    shd.set(qn('w:fill'),header_fill)
    tcPr.append(shd)
    for p in cell.paragraphs:
        for run in p.runs:
            run.font.size=Pt(9.5)
            run.font.bold=True
            run.font.color.rgb=RGBColor(255,255,255)

# Compact paragraph padding only in the link-control and worked-course tables.
# This removes unnecessary 15 pt after-paragraph gaps without reducing table type below 9.5 pt.
for table_index in (4, 5):
    for row in doc.tables[table_index].rows:
        for cell in row.cells:
            for p in cell.paragraphs:
                p.paragraph_format.space_before=Pt(0)
                p.paragraph_format.space_after=Pt(0)
                p.paragraph_format.line_spacing=1.0

# Clarify the role and locator semantics beside the register.
replace_para('本表採一項合成事實一列。','本表採一項合成事實一列。精確定位標到章節及表格資料列／欄位，或能唯一辨認的段落句首；SAMPLE 責任角色代碼只表示示例流程槽位，須以實際職責及授權原件替換，不代表真實承辦或核准。SAMPLE 內容如要轉成 REAL，必須以真實來源逐項替換並保留本版歷史；計算結果須從真實明細重算，不直接複製示例數字。')

# Version and status
replace_para('版本： R05（Word 候選；SAMPLE/SYNTHETIC）','版本： R06（Word 候選；SAMPLE/SYNTHETIC）')
t20=doc.tables[19]
for row in t20.rows[1:]:
    if row.cells[0].text.strip()=='版本':
        row.cells[1].text='R06'
        break
else: raise AssertionError('Table20 version row missing')

# Write a fresh candidate; never overwrite R05.
doc.save(out)

# Sidecar: same 67 facts, exact locator and the sample role as separate fields.
with csvsrc.open('r',encoding='utf-8-sig',newline='') as f:
    rows=list(csv.DictReader(f))
assert len(rows)==67 and len({r['Fact ID'] for r in rows})==67
fieldnames=list(rows[0].keys())+['SAMPLE 責任角色代碼']
for r in rows:
    short=r['Fact ID'].replace('SYN-0013-','')
    assert short in loc
    r['本稿定位']=loc[short]
    r['SAMPLE 責任角色代碼']=role[short]
    if short=='F016': r['合成值／類型']='35；R-A 有值欄位數，35/36 為欄位填入率分子'
    elif short=='F017': r['合成值／類型']='97.2%；R-A 欄位填入率，35 ÷ 36，四捨五入至一位'
    elif short=='F018': r['合成值／類型']='R-A 的 SYN-C04 報名通路缺值；R-A/R-B 已核實可用通路 0/4'
    elif short=='F019': r['合成值／類型']='HOLD；R-A 缺少一項關鍵欄位，且無已核實可用通路'
    elif short=='F020': r['合成值／類型']='36；R-B 有值欄位數；四個 .invalid 通路不計為可用'
    elif short=='F021': r['合成值／類型']='100%；R-B 欄位填入率，36 ÷ 36；不代表通路可用或核准'
    elif short=='F024': r['合成值／類型']='SAMPLE_FIELD_COMPLETE；R-B 欄位有值狀態，不表示可發布'
with csvout.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fieldnames,lineterminator='\n')
    w.writeheader(); w.writerows(rows)

# Copy stable authoring inputs and return deterministic fingerprints.
sha=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(src)=='2bf0407de7f24ad580cbb39df8365cbf2bc69feef97d069575daa3012a1b16d6'
print(json.dumps({'status':'R06_BUILT','source_sha256':sha(src),'candidate':str(out),'candidate_sha256':sha(out),'candidate_bytes':out.stat().st_size,'register':str(csvout),'register_sha256':sha(csvout),'register_rows':len(rows),'mapped_facts':len(seen),'table19_columns':len(doc.tables[18].columns),'table19_rows':len(doc.tables[18].rows)},ensure_ascii=False))
