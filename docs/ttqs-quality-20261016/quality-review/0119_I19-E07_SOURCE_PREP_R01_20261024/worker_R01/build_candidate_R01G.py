from pathlib import Path
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH,WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT,WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import re,hashlib,json,datetime,zipfile

root=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0119_I19-E07_SOURCE_PREP_R01_20261024')
writer=root/'worker_R01'/'writer_R01_response.md'
source=root/'source'/'SOURCE_PACKET_0119_I19-E07_R01.md'
blueprint=root/'source'/'UNIQUE_BLUEPRINT_0119_I19-E07_R01.md'
mapping=root/'source'/'mapping_evidence_0119_R01.json'
outdir=root/'candidate_R01G'; outdir.mkdir(parents=True,exist_ok=True)
output=outdir/'0119__目標市場及顧客價值部分提升證據分析表_R01G.docx'
adopted=outdir/'adopted_manuscript_R01G.md'
sha=lambda b:hashlib.sha256(b).hexdigest()
raw=writer.read_text(encoding='utf-8')
original_sha=sha(writer.read_bytes())
assert original_sha=='2e91b0051ce09ea37bf0e1f74db3658c588c7fde7ea57682585ab8d41fd4fbdd'
lines=raw.splitlines()
changes=[]
for i,line in enumerate(lines):
    if '鴻' in line and '書寫' in line:
        lines[i]=line.replace('以本會實際問卷／鴻иру書寫','以本會實際問卷、訪談紀錄及課程資料書寫')
        if lines[i]==line: raise RuntimeError('mixed-script row found but exact typo not replaced')
        changes.append({'locator':f'line {i+1}','change':'replaced mixed-script typo with clear real-source writing instruction'})
s='\n'.join(lines)+'\n'
# R01E review found the section sequence skipped 4.2; restore a usable field-entry instruction.
heading_anchor='### 表4-1 指標規格表（欄位設計＋SAMPLE規格列）'
heading_block=('### 4.2 指標規格表與欄位填寫規則\n\n'
 '本表應在收集基線期或比較期資料之前完成。先逐一寫清楚指標名稱、構面、分子、分母、納入與排除條件、等長觀察期間、來源定位器、零分母處理及授權依據；兩個構面分開計算，不可把同一筆資料重複算入。示範數字只用於說明填表與重算，正式使用時須依第12節逐列替換或標記 UNKNOWN/NOT_PROVIDED。\n\n')
if s.count(heading_anchor)!=1: raise RuntimeError('Table 4-1 manuscript anchor missing/duplicated')
s=s.replace(heading_anchor,heading_block+heading_anchor,1)
changes.append({'locator':'§4.2 before Table 4-1','change':'restored missing numbered subsection and added pre-collection completion instructions'})
s=s.replace('之**有效**分母','之有效分母')
# Keep the source manuscript stage truthful after a candidate DOCX has been built.
status_old='\uff08\u76ee\u524d\u5c1a\u672a\u5efa\u7f6e\uff09'
status_new='\uff08\u6b63\u5f0f\u539f\u4ef6\u5c1a\u672a\u63d0\u4f9b\uff1b\u672c\u6a94\u70ba SAMPLE \u5019\u9078\uff09'
if status_old not in s: raise RuntimeError('stale Table 0-1 candidate status missing')
s=s.replace(status_old,status_new,1)
content_lines=s.splitlines();g4_changed=False
for ix,text in enumerate(content_lines):
    if text.startswith('- G4 '):
        content_lines[ix]='- G4 \u672c\u5de5\u4f5c\u7a3f\u70ba\u5019\u9078 DOCX\uff1b\u6b63\u5f0f\u5efa\u6a94\u524d\u4ecd\u9808\u5b8c\u6210\u6700\u7d42 Word \u7248\u9762\u3001\u9010\u9801\u8996\u89ba\u6aa2\u67e5\u3001SHA \u4fdd\u5b58\u53ca GitHub \u539f\u59cb\u4f4d\u5143\u8b80\u56de\u3002\u672c\u6e05\u55ae\u4e0d\u5f97\u5c07\u5019\u9078\u5efa\u7f6e\u8996\u70ba\u6b63\u5f0f\u5b8c\u6210.'
        g4_changed=True
if not g4_changed: raise RuntimeError('G4 status line missing')
s='\n'.join(content_lines)+'\n'
changes.append({'locator':'Table 0-1 / G4','change':'updated stale pre-build state while preserving formal acceptance gate'})

for old,new in [
 ('假想事后單題回饋','SAMPLE：假想事後單題回饋'),
 ('假想事後單題回號','SAMPLE：假想事後單題回覆'),
 ('工作稿別：R01（依來源包 R01＋Unique Blueprint R01 撰寫）','工作稿別：R01G（採用 Writer R01，經最小確定性修訂；來源包及 Unique Blueprint R01）'),
 ('**狀態：DRAFT／SAMPLE_ONLY — 文件尚未建置 DOCX、未覆核、未核准；本稿不含任何本會真實成果證據。**','**狀態：CANDIDATE／SAMPLE_ONLY — R01G DOCX 候選已建置，尚未獨立覆核或協會核准；本稿不含任何本會真實成果證據。**'),
 ('| 工作稿版別 | ＿＿＿ | SAMPLE：R01（本稿自訂代號） | 每次修改升版並記錄變更原因 |','| 工作稿版別 | ＿＿＿ | SAMPLE：R01G（本稿自訂代號） | 每次修改升版並記錄變更原因 |'),
 ('| 製作角色 | ＿＿＿（角色，不填人名） | SAMPLE：訓練行政承辦人 | 實際任命 UNKNOWN |','| 編製／記錄作者角色（author） | ＿＿＿（只填授權角色；個人姓名留受限紀錄） | SAMPLE：資料整理者 | 實際任命 UNKNOWN |'),
]:
    if old not in s: raise RuntimeError('required exact repair anchor missing: '+old[:50])
    s=s.replace(old,new,1); changes.append({'locator':'targeted text anchor','change':old+' -> '+new})
# Add explicit record classification and display-boundary controls to the document control form.
anchor='| 證據狀態標記 | ＿＿＿ | SAMPLE：SYNTHETIC_ALL | 填 `SYNTHETIC_ALL`、`SYNTHETIC+REAL_<已替換登錄編號>` 或 `REAL_ALL` |'
addition=anchor+'\n| record_class（記錄類別） | ＿＿＿ | SAMPLE：ANALYTIC_EVIDENCE_REGISTER | 分開標記分析登錄、原始問卷、原始名冊等類別；不得把分析表稱作原始證據 |\n| display_boundary（顯示界線） | ＿＿＿ | SAMPLE：SYNTHETIC_PUBLIC_SAMPLE／REAL_RESTRICTED_DETAILS | 公開版須去識別；真實個資、授權與來源索引存於受限位置 |'
if anchor not in s: raise RuntimeError('document control insertion anchor missing')
s=s.replace(anchor,addition,1);changes.append({'locator':'Table 1-1','change':'added record_class and display_boundary controls'})
# Add evidence author / class / public boundary / original-received matrix, tied to Table 10-1 by evidence ID.
anchor='**規則**：本冊每列僅承載一種構面；不允許「兩構面同行」；重算欄由覆核者填寫並簽角色；任何人不得人為補寫名冊或日期。\n\n---'
insert='''**規則**：本冊每列僅承載一種構面；不允許「兩構面同行」；重算欄由覆核者填寫並簽角色；任何人不得人為補寫名冊或日期。\n\n### 表10-2 證據列作者、記錄類別與顯示界線\n\n每筆表10-1證據均以登錄編號對應本表。作者欄填授權角色，不公開個人姓名；原始紀錄未實際隨工作包提供時，標示 `NOT_PROVIDED_IN_CANDIDATE_PACKET`，不得推論協會是否持有。\n\n| 登錄編號 | 記錄作者角色（author） | record_class | display_boundary | 原始紀錄實際收到 | 授權／公開處理 |\n|---|---|---|---|---|---|\n| EV-01 | SAMPLE：市場資料整理者 | SYNTHETIC_DEMO_ROW | SYNTHETIC_PUBLIC_SAMPLE | NOT_PROVIDED_IN_CANDIDATE_PACKET | SAMPLE：無真實授權資料 |\n| EV-02 | SAMPLE：市場資料整理者 | SYNTHETIC_DEMO_ROW | SYNTHETIC_PUBLIC_SAMPLE | NOT_PROVIDED_IN_CANDIDATE_PACKET | SAMPLE：無真實授權資料 |\n| EV-03 | SAMPLE：課程資料整理者 | SYNTHETIC_DEMO_ROW | SYNTHETIC_PUBLIC_SAMPLE | NOT_PROVIDED_IN_CANDIDATE_PACKET | SAMPLE：無真實授權資料 |\n| EV-04 | SAMPLE：課程資料整理者 | SYNTHETIC_DEMO_ROW | SYNTHETIC_PUBLIC_SAMPLE | NOT_PROVIDED_IN_CANDIDATE_PACKET | SAMPLE：無真實授權資料 |\n| （待填） | （待填授權角色） | （待填） | （待填） | （填 YES／NO／UNKNOWN） | （待填） |\n\n---'''
if anchor not in s: raise RuntimeError('evidence register insertion anchor missing')
s=s.replace(anchor,insert,1);changes.append({'locator':'Table 10-2','change':'added row-linked author, record_class, display_boundary and original_received controls'})
# Extend the replacement register to ensure the added ownership and boundary fields are replaced row-by-row.
anchor='| R-14 | 結案狀態（表15-2） | 未勾選、NOT_REVIEWED | 由覆核者勾選並簽角色 | 覆核者 | （待填） |'
addition=anchor+'\n| R-15 | 表1-1 編製／記錄作者角色、record_class、display_boundary | SAMPLE 角色及 SYNTHETIC/REAL 顯示界線 | 以協會授權角色、實際資料類別及去識別／受限規則替換；姓名不得公開 | 承辦＋資料權責角色 | （待填） |\n| R-16 | 表10-2 EV-01～EV-04 作者、類別、顯示界線、原始紀錄收到狀態 | 全部 SAMPLE/SYNTHETIC 及 NOT_PROVIDED_IN_CANDIDATE_PACKET | 逐筆連回表10-1真實來源；查無原始檔就保留 UNKNOWN／NOT_PROVIDED，不推論協會是否持有 | 資料整理者＋覆核者 | （待填） |'
if anchor not in s: raise RuntimeError('replacement register insertion anchor missing')
s=s.replace(anchor,addition,1);changes.append({'locator':'Table 12-1 R-15/R-16','change':'added replacement coverage for authorship, record class, display boundary, original-received status'})
# Ensure the specified malformed strings are gone and key terms exist.
for bad in ('鴻иру','假想事后','回號'):
    if bad in s: raise RuntimeError('known writer defect remains: '+bad)
for term in ('author','display_boundary','record_class','NOT_PROVIDED_IN_CANDIDATE_PACKET','SYNTHETIC_PUBLIC_SAMPLE'):
    if term not in s: raise RuntimeError('required field missing after repair: '+term)
def fix_once(old,new,label):
    global s
    if old not in s: raise RuntimeError('exact text anchor missing: '+label)
    s=s.replace(old,new,1);changes.append({'locator':label,'change':'corrected substantive cross-reference / workflow text'})
fix_once('正式使用前，所有示例必須整筆替換為有權限使用之原始資料（見第 13 節替換登錄冊）。','正式使用前，所有示例必須依第 12 節替換登錄冊逐列以有權限使用之資料替換或標記 UNKNOWN/NOT_PROVIDED；再依第 12.2 節檢查殘留。','§0.2 sample boundary')
fix_once('2. 依第 4 節把「目標市場」與「顧客價值」**分別**寫成可操作定義；兩構面共用一頁不得混寫。','2. 依第 3.1 與 3.2 節把「目標市場」與「顧客價值」**分別**寫成可操作定義；兩構面共用一頁不得混寫。','§0.3 step 2')
fix_once('3. 依第 5 節在**取得結果之前**定義指標（分子、分母、納入排除、期間、來源），再填第 6 節成對證據表。','3. 依第 4 節在**取得結果之前**定義指標（分子、分母、納入排除、期間、來源），再填第 5 節成對證據表。','§0.3 step 3')
fix_once('4. 逐列完成第 7 節來源與分母稽核；任何一格無法通過，即轉第 10 節判定矩陣，不得硬算趨勢。','4. 逐列完成第 6 節來源與分母稽核；任何一格無法通過，即轉第 9 節判定矩陣，不得硬算趨勢。','§0.3 step 4')
fix_once('5. 依第 15 節完成覆核與結案狀態勾選；填完後剝除全部 `SAMPLE/SYNTHETIC` 示例（第 13 節），再送覆核者。','5. 依第 12 節逐列完成 SAMPLE/SYNTHETIC 替換或標示 UNKNOWN/NOT_PROVIDED，並通過第 12.2 節殘留檢查；再由第二覆核者依第 14 節逐項勾選。','§0.3 step 5')
fix_once('事後修改需在表12-1 限制與登錄差異中揭露。','任何事後變更須逐次填表3-3；同時更新表12-1受影響的替換列，保留原定義與差異，不得覆寫。','§3.1 post-change instruction')
fix_once('**構face 澄清**','**構面澄清**','§3.2 mixed-script typo')
fix_once('表13-1 全列處理','表12-1 全列替換並通過第12.2節殘留檢查','Table 6-1 S7 sample residue cross-reference')
fix_once('填表11-2 全列並送第二覆核','完成表14-1全列覆核檢查並由第二覆核者依表14-2勾選一項結案狀態','Table 9-1 BOTH_PARTIAL_CANDIDATE action')
fix_once('見表14-1 分界','見表13-1跨文件分界','Table 9-1 external-document boundary')
fix_once('樣本排除規則、標記、結論與表13-1 未交代齊全','樣本排除規則、標記、結論與表12-1替換登錄／第12.2節殘留檢查未交代齊全','Table 9-1 sample completeness')
fix_once('| R-13 | 表14-1 引用欄位 |','| R-13 | 表13-1 相鄰文件分界欄位 |','Table 12-1 R-13')
fix_once('結案狀態（表15-2）','結案狀態（表14-2）','Table 12-1 R-14')
fix_once('| C-13 | 表15-2 結案狀態勾選完成 |','| C-13 | 表14-2 結案狀態勾選完成 |','Table 14-1 C-13')
caption_anchor='### 7.2 手算重算示範（覆核者可逐行驗證）\n\n| 算式'
caption_new='### 7.2 手算重算示範（覆核者可逐行驗證）\n\n#### 表7-2 手算重算表\n\n| 算式'
fix_once(caption_anchor,caption_new,'§7.2 Table 7-2 label')
form_lines = [
'### 表3-3 定義／口徑事後變更紀錄單（變更時逐次填寫）',
'',
'**使用規則：** 表3-1／表3-2先於收集資料前定義。若目標族群、管道、期間、題目、納入／排除或分母口徑在資料收集後變更，逐筆填本表；判斷兩期能否依新口徑回溯重算。不能回溯或影響未披露時，依表9-1輸出 `NO_COMPARABLE_BASELINE` 或 `HOLD`，不得只改本期定義。',
'',
'| 變更編號 | 構面／指標 | 變更欄位 | 原定義／版本 | 新定義／生效期間 | 變更原因／來源定位 | 兩期可回溯重算 | 處理結果／差異 | 編製角色 | 覆核狀態 |',
'|---|---|---|---|---|---|---|---|---|---|',
'| SAMPLE-CHG-01 | SAMPLE：M-01 | SAMPLE：目標族群條件 | SAMPLE：假想 R00 定義 | SAMPLE：假想 R01 定義 | SAMPLE：方法演練；非協會決議 | SAMPLE：NOT_RUN | SAMPLE：應先重算兩期；不能回溯即標 NO_COMPARABLE_BASELINE | SAMPLE：資料整理者 | SAMPLE：NOT_REVIEWED |',
'| （待填） | （待填） | （待填） | （填版本／日期） | （填生效期間） | （填原因與可回查來源） | （YES／NO／UNKNOWN） | （填回溯重算與限制） | （授權角色） | （NOT_REVIEWED／HOLD／完成） |',
'',
'---',
''
]
sec4='## 4. 測量規範與指標規格'
if sec4 not in s: raise RuntimeError('section 4 anchor missing')
s=s.replace(sec4,'\n'.join(form_lines)+sec4,1)
changes.append({'locator':'Table 3-3','change':'added usable post-collection definition/method change log with synthetic-only example and non-comparability hold rule'})
adopted.write_text(s,encoding='utf-8',newline='\n')

# Markdown-to-DOCX, purpose-built as a landscape evidence-analysis workbook.
doc=Document()
sec=doc.sections[0];sec.orientation=WD_ORIENT.LANDSCAPE;sec.page_width=Inches(11.69);sec.page_height=Inches(8.27)
sec.top_margin=Inches(.52);sec.bottom_margin=Inches(.5);sec.left_margin=Inches(.55);sec.right_margin=Inches(.55)
usable=sec.page_width-sec.left_margin-sec.right_margin
styles=doc.styles
for stylename in ('Normal','Title','Subtitle','Heading 1','Heading 2','Heading 3'):
    st=styles[stylename];st.font.name='Microsoft JhengHei';st._element.rPr.rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei')
styles['Normal'].font.size=Pt(10.5);styles['Normal'].font.color.rgb=RGBColor(35,43,52)
styles['Normal'].paragraph_format.space_after=Pt(3);styles['Normal'].paragraph_format.line_spacing=1.02
styles['Title'].font.size=Pt(22);styles['Title'].font.bold=True;styles['Title'].font.color.rgb=RGBColor(20,33,50);styles['Title'].paragraph_format.space_after=Pt(8)
styles['Subtitle'].font.size=Pt(11);styles['Subtitle'].font.color.rgb=RGBColor(77,93,110)
for name,size,color in [('Heading 1',16,'18344F'),('Heading 2',13,'245477'),('Heading 3',11,'376B8C')]:
    st=styles[name];st.font.size=Pt(size);st.font.bold=True;st.font.color.rgb=RGBColor.from_string(color);st.paragraph_format.space_before=Pt(8);st.paragraph_format.space_after=Pt(3);st.paragraph_format.keep_with_next=True
# Header/footer for usability and version control.
hp=sec.header.paragraphs[0];hp.alignment=WD_ALIGN_PARAGRAPH.RIGHT
r=hp.add_run('TTQS ONE  |  0119  |  I19-E07  |  SAMPLE 候選');r.font.name='Microsoft JhengHei';r.font.size=Pt(8);r.font.color.rgb=RGBColor(95,110,125)
fp=sec.footer.paragraphs[0];fp.alignment=WD_ALIGN_PARAGRAPH.CENTER
rr=fp.add_run('R01G 候選文件  •  正式接受未授予  |  第 ');rr.font.name='Microsoft JhengHei';rr.font.size=Pt(8);rr.font.color.rgb=RGBColor(95,110,125)
fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');fp._p.append(fld)
props=doc.core_properties;props.title='0119 目標市場及顧客價值部分提升證據分析表';props.subject='TTQS ONE I19-E07 SAMPLE候選';props.author='';props.keywords='0119; I19-E07; SAMPLE; SYNTHETIC'

def set_run_font(run,size=None,bold=None,color=None,italic=None,mono=False):
    run.font.name='Microsoft JhengHei' if not mono else 'Consolas';run._element.get_or_add_rPr().rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei')
    if size is not None: run.font.size=Pt(size)
    if bold is not None: run.bold=bold
    if italic is not None: run.italic=italic
    if color: run.font.color.rgb=RGBColor.from_string(color)

def add_inline(p,text,base_size=10):
    pat=re.compile(r'(\*\*.+?\*\*|`[^`]+`|\*[^*]+\*)')
    pos=0
    for m in pat.finditer(text):
        if m.start()>pos: set_run_font(p.add_run(text[pos:m.start()]),base_size)
        tok=m.group(0)
        if tok.startswith('**'): set_run_font(p.add_run(tok[2:-2]),base_size,bold=True)
        elif tok.startswith('`'): set_run_font(p.add_run(tok[1:-1]),base_size,color='245477',mono=True)
        else: set_run_font(p.add_run(tok[1:-1]),base_size,italic=True)
        pos=m.end()
    if pos<len(text): set_run_font(p.add_run(text[pos:]),base_size)

def set_cell_shading(cell,fill):
    tcPr=cell._tc.get_or_add_tcPr();shd=tcPr.find(qn('w:shd'))
    if shd is None: shd=OxmlElement('w:shd');tcPr.append(shd)
    shd.set(qn('w:fill'),fill)
def set_cell_margins(cell,top=60,start=65,bottom=60,end=65):
    tc=cell._tc;tcPr=tc.get_or_add_tcPr();mar=tcPr.first_child_found_in('w:tcMar')
    if mar is None: mar=OxmlElement('w:tcMar');tcPr.append(mar)
    for m,v in [('top',top),('start',start),('bottom',bottom),('end',end)]:
        node=mar.find(qn('w:'+m))
        if node is None:node=OxmlElement('w:'+m);mar.append(node)
        node.set(qn('w:w'),str(v));node.set(qn('w:type'),'dxa')
def repeat_table_header(row):
    trPr=row._tr.get_or_add_trPr();el=OxmlElement('w:tblHeader');el.set(qn('w:val'),'true');trPr.append(el)
def keep_table_row_together(row):
    trPr=row._tr.get_or_add_trPr();el=OxmlElement('w:cantSplit');trPr.append(el)
def parse_cells(line):return [x.strip() for x in line.strip().strip('|').split('|')]
def is_sep(line):return bool(re.fullmatch(r'\|[\s:|\-]+\|',line.strip()))
def add_md_table(rows):
    if not rows:return
    n=len(rows[0]);
    if any(len(x)!=n for x in rows):raise RuntimeError('Markdown table has inconsistent cell counts: '+repr([len(x) for x in rows]))
    if n<=8:groups=[list(range(n))]
    else:groups=[list(range(0,8)),[0]+list(range(8,n))]
    key=rows[0][0]
    for gi,cols in enumerate(groups):
        if len(groups)>1:
            p=doc.add_paragraph();p.paragraph_format.space_before=Pt(4);p.paragraph_format.space_after=Pt(2)
            label=chr(65+gi);p.add_run(f'欄位分段 {label}／{chr(65+len(groups)-1)}；依「{key}」欄位與另一分段合併同一資料列。').italic=True
            p.runs[0].font.size=Pt(10.5);p.runs[0].font.color.rgb=RGBColor(88,105,122)
        table=doc.add_table(rows=1,cols=len(cols));table.alignment=WD_TABLE_ALIGNMENT.CENTER;table.autofit=False
        try:table.style='Table Grid'
        except KeyError:pass
        # Split page width evenly within each repeated-key segment.
        colw=usable/len(cols)
        for ci,src_i in enumerate(cols):
            cell=table.rows[0].cells[ci];cell.width=colw;cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER;set_cell_shading(cell,'1F4563');set_cell_margins(cell,75,65,75,65)
            p=cell.paragraphs[0];p.paragraph_format.space_after=Pt(0);p.paragraph_format.keep_together=True
            add_inline(p,rows[0][src_i],9.5)
            for run in p.runs:set_run_font(run,9.5,bold=True,color='FFFFFF')
        repeat_table_header(table.rows[0]);keep_table_row_together(table.rows[0])
        for row in rows[1:]:
            cells=table.add_row().cells;keep_table_row_together(table.rows[-1])
            for ci,src_i in enumerate(cols):
                cell=cells[ci];cell.width=colw;cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER;set_cell_margins(cell)
                p=cell.paragraphs[0];p.paragraph_format.space_after=Pt(0);p.paragraph_format.line_spacing=1.0
                add_inline(p,row[src_i],9.5)
                if ci==0:set_cell_shading(cell,'EAF1F6')
                for run in p.runs:set_run_font(run,9.5,color='23313E')
        p=doc.add_paragraph();p.paragraph_format.space_after=Pt(1);p.paragraph_format.line_spacing=1.0

lines=s.splitlines();i=0;paragraph_count=0;table_count=0;max_cols=0
while i<len(lines):
    line=lines[i].rstrip()
    if not line.strip() or line.strip()=='---':i+=1;continue
    if line.startswith('|'):
        block=[]
        while i<len(lines) and lines[i].strip().startswith('|'):
            if not is_sep(lines[i]):block.append(parse_cells(lines[i]))
            i+=1
        if block:
            max_cols=max(max_cols,len(block[0]));add_md_table(block);table_count+=1
        continue
    m=re.match(r'^(#{1,6})\s+(.*)$',line)
    if m:
        level=len(m.group(1));txt=m.group(2).strip()
        if level==1: p=doc.add_paragraph(style='Title')
        else:p=doc.add_paragraph(style='Heading '+str(min(level-1,3)))
        add_inline(p,txt,22 if level==1 else {2:16,3:13,4:11,5:10.5,6:10.5}[level])
        if txt.startswith(('8. 負向／保留示例','9. 缺漏／負向／不可比判定矩陣')):
            p.paragraph_format.page_break_before=True
        paragraph_count+=1;i+=1;continue
    if line.startswith('>'):
        p=doc.add_paragraph();p.paragraph_format.left_indent=Inches(.22);p.paragraph_format.right_indent=Inches(.15);p.paragraph_format.space_before=Pt(3);p.paragraph_format.space_after=Pt(6)
        add_inline(p,line[1:].strip(),10.5)
        for r in p.runs:r.italic=True;r.font.color.rgb=RGBColor(61,76,91)
        paragraph_count+=1;i+=1;continue
    bullet=re.match(r'^\s*[-*]\s+(.*)$',line)
    numbered=re.match(r'^\s*\d+[.)]\s+(.*)$',line)
    if bullet:
        p=doc.add_paragraph(style='List Bullet');txt=bullet.group(1)
    elif numbered:
        p=doc.add_paragraph();p.paragraph_format.left_indent=Inches(.24);p.paragraph_format.first_line_indent=Inches(-.24);txt=line.strip()
    else:
        p=doc.add_paragraph();txt=line
    add_inline(p,txt,10.5)
    p.paragraph_format.widow_control=True
    paragraph_count+=1;i+=1

# Avoid a blank trailing page and ensure document has meaningful authored content.
if not paragraph_count or not table_count:raise RuntimeError('No content converted')
doc.save(output)
# Validate package and extracted body text presence.
with zipfile.ZipFile(output) as z:bad=z.testzip();xml=z.read('word/document.xml').decode('utf-8')
if bad:raise RuntimeError('DOCX zip integrity failed: '+bad)
for required in ['0119','I19-E07','SYNTHETIC_PUBLIC_SAMPLE','display_boundary','record_class','12.5']:
    if required not in xml and required not in s:raise RuntimeError('required content missing: '+required)
receipt={'work_id':'TTQS_ONE-0119-I19-E07-R01G-DOCX-BUILD','doc_id':'0119','requirement_id':'I19-E07','candidate_state':'CANDIDATE_SAMPLE_ONLY','source_writer_path':str(writer),'source_writer_sha256':original_sha,'adopted_manuscript_path':str(adopted),'adopted_manuscript_sha256':sha(adopted.read_bytes()),'source_packet_sha256':sha(source.read_bytes()),'unique_blueprint_sha256':sha(blueprint.read_bytes()),'mapping_sha256':sha(mapping.read_bytes()),'changes':changes,'builder':'bundled Python 3 / python-docx 1.2.0','layout':'A4 landscape; wide tables split into keyed column segments of at most 8 columns; repeated shaded headers; page number footer','paragraph_count':paragraph_count,'markdown_table_count':table_count,'maximum_source_table_columns':max_cols,'docx_path':str(output),'docx_sha256':sha(output.read_bytes()),'docx_bytes':output.stat().st_size,'zip_test':'PASS','formal_acceptance':'NOT_GRANTED','independent_semantic_review':'PENDING','visual_review':'PENDING'}
(outdir/'build_receipt_R01G.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
