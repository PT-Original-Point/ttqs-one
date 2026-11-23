from pathlib import Path
import re,csv,json,hashlib,datetime,math
from docx import Document
from docx.shared import Inches,Pt,Cm,RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH,WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT,WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.section import WD_ORIENT,WD_SECTION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

BASE=Path(r'E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0105_I18-E13_R01_20261022')
WRITER=BASE/'writer'
MD=WRITER/'opencode_writer_manuscript_0105_R01.md'
OUT=BASE/'candidate'/'0105_I18-E13_績效改善調查與課後行動計畫追蹤套件_R01.docx'
CSV_OUT=BASE/'evidence'/'synthetic_replacement_register_0105_R01.csv'
BUILD_RECEIPT=BASE/'evidence'/'docx_build_receipt_0105_R01.json'
BLUE='#174B5A'
PALE='#EAF2F5'
PALE2='#F5F8FA'
INK='#000000'
WHITE='#FFFFFF'
GRAY='#52616B'
FONT='Microsoft JhengHei'
MONO='Consolas'
TICK=chr(96)
text=MD.read_text(encoding='utf-8')
lines=text.splitlines()

def set_run_font(run, size=10.5, bold=None, italic=None, color=INK, name=FONT):
    run.font.name=name
    run._element.get_or_add_rPr().rFonts.set(qn('w:ascii'),name)
    run._element.get_or_add_rPr().rFonts.set(qn('w:hAnsi'),name)
    run._element.get_or_add_rPr().rFonts.set(qn('w:eastAsia'),name)
    run.font.size=Pt(size)
    run.font.color.rgb=RGBColor.from_string(color.replace('#',''))
    if bold is not None: run.bold=bold
    if italic is not None: run.italic=italic

def rich(paragraph, value, size=10.5, color=INK):
    pat=re.compile(r'(\*\*.+?\*\*|\*[^*]+\*|'+re.escape(TICK)+r'[^'+re.escape(TICK)+r']+'+re.escape(TICK)+r')')
    for part in pat.split(value):
        if not part: continue
        if part.startswith('**') and part.endswith('**'):
            run=paragraph.add_run(part[2:-2]);set_run_font(run,size,bold=True,color=color)
        elif part.startswith('*') and part.endswith('*'):
            run=paragraph.add_run(part[1:-1]);set_run_font(run,size,italic=True,color=color)
        elif part.startswith(TICK) and part.endswith(TICK):
            run=paragraph.add_run(part[1:-1]);set_run_font(run,size,name=MONO,color='334E5C')
        else:
            run=paragraph.add_run(part);set_run_font(run,size,color=color)

def shade(cell, fill):
    tcPr=cell._tc.get_or_add_tcPr()
    shd=tcPr.find(qn('w:shd'))
    if shd is None: shd=OxmlElement('w:shd');tcPr.append(shd)
    shd.set(qn('w:fill'),fill.replace('#',''))

def margins(cell, top=75, start=85, bottom=75, end=85):
    tc=cell._tc;tcPr=tc.get_or_add_tcPr()
    tcMar=tcPr.first_child_found_in('w:tcMar')
    if tcMar is None: tcMar=OxmlElement('w:tcMar');tcPr.append(tcMar)
    for tag,val in [('top',top),('start',start),('bottom',bottom),('end',end)]:
        node=tcMar.find(qn('w:'+tag))
        if node is None: node=OxmlElement('w:'+tag);tcMar.append(node)
        node.set(qn('w:w'),str(val));node.set(qn('w:type'),'dxa')

def repeat_header(row):
    trPr=row._tr.get_or_add_trPr()
    tblHeader=OxmlElement('w:tblHeader');tblHeader.set(qn('w:val'),'true');trPr.append(tblHeader)

def dont_split(row):
    trPr=row._tr.get_or_add_trPr()
    el=OxmlElement('w:cantSplit');trPr.append(el)

def set_orientation(section, landscape):
    if landscape:
        section.orientation=WD_ORIENT.LANDSCAPE
        section.page_width=Cm(29.7);section.page_height=Cm(21.0)
        section.left_margin=Cm(1.35);section.right_margin=Cm(1.35)
        section.top_margin=Cm(1.45);section.bottom_margin=Cm(1.45)
    else:
        section.orientation=WD_ORIENT.PORTRAIT
        section.page_width=Cm(21.0);section.page_height=Cm(29.7)
        section.left_margin=Cm(1.75);section.right_margin=Cm(1.75)
        section.top_margin=Cm(1.55);section.bottom_margin=Cm(1.55)
    section.header_distance=Cm(0.7);section.footer_distance=Cm(0.7)

def ensure_orientation(landscape):
    current=doc.sections[-1]
    is_landscape=(current.orientation==WD_ORIENT.LANDSCAPE)
    if is_landscape!=landscape:
        if doc.paragraphs and not doc.paragraphs[-1].text.strip():
            orphan=doc.paragraphs[-1]._element
            orphan.getparent().remove(orphan)
        sec=doc.add_section(WD_SECTION.NEW_PAGE)
        set_orientation(sec,landscape)

def parse_cells(line):
    v=line.strip()
    if not v.startswith('|'): return []
    if v.endswith('|'): v=v[1:-1]
    else: v=v[1:]
    return [x.strip().replace(r'\|','|') for x in v.split('|')]

def is_sep(line):
    cells=parse_cells(line)
    return bool(cells) and all(re.fullmatch(r':?-{3,}:?',c.strip()) for c in cells)

def find_following_table_cols(ls, index):
    current = re.match(r'^(#{1,3})\s+', ls[index].strip())
    current_level = len(current.group(1)) if current else 3
    j=index+1
    scanned_sibling_heading=False
    scanned=0
    while j<len(ls):
        value=ls[j].strip()
        if not value or value in ('---','***','___'):
            j+=1;continue
        heading=re.match(r'^(#{1,3})\s+',value)
        if heading:
            if len(heading.group(1)) < current_level:
                return 0
            if len(heading.group(1)) == current_level:
                if scanned_sibling_heading:
                    return 0
                scanned_sibling_heading=True
                return 0
            j+=1;continue
        if value.startswith('|'):
            return len(parse_cells(ls[j]))
        # Keep a chapter heading and its short lead-in with the upcoming table.
        # Stop at a bounded distance so unrelated later tables do not rotate prose.
        scanned+=1
        if scanned>40:
            return 0
        j+=1
    return 0

def clean_heading(value):
    value=value.strip()
    value=re.sub(r'[_／/：:、，。；！？」『』「」（）()\[\]【】—–-]+',' ',value)
    value=re.sub(r'\s+',' ',value).strip()
    value=re.sub(r'(?<=\d)\.(?=\s)','',value)
    return value

def available_width(section):
    return section.page_width-section.left_margin-section.right_margin

def add_markdown_table(doc, rows):
    if not rows:return
    ncols=len(rows[0])
    if any(len(r)!=ncols for r in rows):
        raise ValueError('unequal column count: '+str([len(r) for r in rows]))
    table=doc.add_table(rows=1,cols=ncols)
    table.style='Table Grid';table.alignment=WD_TABLE_ALIGNMENT.CENTER;table.autofit=False
    for ri,row_data in enumerate(rows):
        row=table.rows[0] if ri==0 else table.add_row()
        if ri==0: repeat_header(row)
        maxrow=max((len(x) for x in row_data),default=0)
        if maxrow<220: dont_split(row)
        for ci,value in enumerate(row_data):
            cell=row.cells[ci];cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            margins(cell)
            if ri==0:shade(cell,BLUE)
            elif ri%2==0:shade(cell,PALE2)
            p=cell.paragraphs[0];p.paragraph_format.space_after=Pt(0);p.paragraph_format.space_before=Pt(0);p.paragraph_format.line_spacing=1.03; p.paragraph_format.keep_with_next=(ri==0)
            rich(p,value,size=9.5,color=WHITE if ri==0 else INK)
            if ri==0:
                for run in p.runs: run.bold=True
    sec=doc.sections[-1]
    width=available_width(sec)
    weights=[]
    for ci in range(ncols):
        colmax=max((len(r[ci]) for r in rows),default=1)
        weights.append(0.65 if colmax<=5 else min(3.0,max(1.0,math.sqrt(colmax)/2.0)))
    minw=0.7 if width>Cm(23) else 0.65
    if sum(weights)*minw>width:
        weights=[1.0]*ncols
    total=sum(weights)
    for ci,w in enumerate(weights):
        colw=width*w/total
        for row in table.rows:
            row.cells[ci].width=colw
        table.columns[ci].width=int(colw)
    doc.add_paragraph().paragraph_format.space_after=Pt(2)
    return table

doc=Document()
set_orientation(doc.sections[0],False)
sec=doc.sections[0]
sec.different_first_page_header_footer=False
# Professional readable base styles
styles=doc.styles
normal=styles['Normal'];normal.font.name=FONT;normal._element.rPr.rFonts.set(qn('w:ascii'),FONT);normal._element.rPr.rFonts.set(qn('w:eastAsia'),FONT);normal.font.size=Pt(10.5);normal.font.color.rgb=RGBColor(0,0,0)
normal.paragraph_format.space_after=Pt(5);normal.paragraph_format.line_spacing=1.13
for sty,size in [('Heading 1',16),('Heading 2',13),('Heading 3',11.5)]:
    s=styles[sty];s.font.name=FONT;s._element.rPr.rFonts.set(qn('w:ascii'),FONT);s._element.rPr.rFonts.set(qn('w:eastAsia'),FONT);s.font.size=Pt(size);s.font.bold=True;s.font.color.rgb=RGBColor(0,0,0);s.paragraph_format.space_before=Pt(13 if sty=='Heading 1' else 9);s.paragraph_format.space_after=Pt(5);s.paragraph_format.keep_with_next=True
title_style=styles['Title'];title_style.font.name=FONT;title_style._element.rPr.rFonts.set(qn('w:ascii'),FONT);title_style._element.rPr.rFonts.set(qn('w:eastAsia'),FONT);title_style.font.size=Pt(22);title_style.font.bold=True;title_style.font.color.rgb=RGBColor(0,0,0);title_style.paragraph_format.space_after=Pt(7)
# Header and footer
h=sec.header.paragraphs[0];h.alignment=WD_ALIGN_PARAGRAPH.RIGHT
r=h.add_run('DOCX 0105  |  I18-E13  |  SAMPLE / SYNTHETIC  |  REAL UNKNOWN');set_run_font(r,8.5,color=GRAY)
f=sec.footer.paragraphs[0];f.alignment=WD_ALIGN_PARAGRAPH.CENTER
r=f.add_run('候選工作稿  ·  非正式核准或第三方證明  ·  第 ');set_run_font(r,8.2,color=GRAY)
fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');f._p.append(fld)
r=f.add_run(' 頁');set_run_font(r,8.2,color=GRAY)
# Markdown parser
i=0;in_code=False;code_lines=[];title_seen=False;table_count=0;heading_counts={1:0,2:0,3:0}
while i<len(lines):
    line=lines[i];strip=line.strip()
    if strip.startswith(TICK*3):
        if not in_code:
            in_code=True;code_lines=[]
        else:
            p=doc.add_paragraph();p.paragraph_format.left_indent=Cm(0.45);p.paragraph_format.right_indent=Cm(0.35);p.paragraph_format.space_before=Pt(4);p.paragraph_format.space_after=Pt(8);p.paragraph_format.keep_together=True
            pPr=p._p.get_or_add_pPr();shd=OxmlElement('w:shd');shd.set(qn('w:fill'),PALE.replace('#',''));pPr.append(shd)
            r=p.add_run('\n'.join(code_lines));set_run_font(r,10.5,name=MONO,color='263238')
            in_code=False
        i+=1;continue
    if in_code:
        code_lines.append(line);i+=1;continue
    if not strip or strip in ('---','***','___'):
        i+=1;continue
    if strip.startswith('|'):
        block=[]
        while i<len(lines) and lines[i].strip().startswith('|'):
            block.append(parse_cells(lines[i]));i+=1
        if len(block)>1 and all(re.fullmatch(r':?-{3,}:?',c.strip()) for c in block[1]):
            block=[block[0]]+block[2:]
        if not block:continue
        ncols=len(block[0])
        ensure_orientation(ncols>=7)
        add_markdown_table(doc,block);table_count+=1
        continue
    m=re.match(r'^(#{1,3})\s+(.*)$',strip)
    if m:
        level=len(m.group(1));heading=m.group(2).strip()
        nextcols=find_following_table_cols(lines,i)
        ensure_orientation(nextcols>=7)
        if level==1 and not title_seen:
            p=doc.add_paragraph(style='Title');rich(p,clean_heading(heading),size=22);title_seen=True
            meta=doc.add_paragraph();meta.paragraph_format.space_after=Pt(8)
            rich(meta,'文件編號 0105　評核項目 I18-E13　專案157索引 114（非官方方框序號）　類型：績效改善調查與課後行動計畫追蹤表',size=10.5,color=GRAY)
        else:
            style='Heading '+str(level)
            p=doc.add_paragraph(style=style);rich(p,clean_heading(heading),size={1:16,2:13,3:11.5}[level])
            if level==2 and heading.startswith('13.') and '每個數字' in heading:
                p.paragraph_format.page_break_before=True
            if level==3 and heading.startswith('11.3 '):
                p.paragraph_format.page_break_before=True
            if level==3 and heading.startswith('19.4'):
                p.paragraph_format.page_break_before=True
            if level==3 and (re.match(r'^\*{0,2}表\s*T[-\s]*13\b',heading,re.I) or re.match(r'^\*{0,2}表\s*T[-\s]*18\b',heading,re.I) or re.match(r'^\*{0,2}表\s*T[-\s]*19\b',heading,re.I) or re.match(r'^\*{0,2}表\s*T[-\s]*19\.4\b',heading,re.I)):
                p.paragraph_format.page_break_before=True
            heading_counts[level]+=1
        i+=1;continue
    if strip.startswith('>'):
        p=doc.add_paragraph();p.paragraph_format.left_indent=Cm(0.4);p.paragraph_format.right_indent=Cm(0.25);p.paragraph_format.space_before=Pt(2);p.paragraph_format.space_after=Pt(6)
        rich(p,strip[1:].lstrip(),size=10.5,color='243B44')
        pPr=p._p.get_or_add_pPr();shd=OxmlElement('w:shd');shd.set(qn('w:fill'),'F0F5F7');pPr.append(shd)
        i+=1;continue
    if re.match(r'^[-*]\s+',strip):
        p=doc.add_paragraph(style='List Bullet');p.paragraph_format.left_indent=Cm(0.65);p.paragraph_format.first_line_indent=Cm(-0.25);p.paragraph_format.space_after=Pt(3);rich(p,re.sub(r'^[-*]\s+','',strip),size=10.5);i+=1;continue
    if re.match(r'^\d+\.\s+',strip):
        number=re.match(r'^(\d+)\.\s+',strip).group(1)
        p=doc.add_paragraph();p.paragraph_format.left_indent=Cm(0.65);p.paragraph_format.first_line_indent=Cm(-0.45);p.paragraph_format.space_after=Pt(3)
        rich(p,number+'. '+re.sub(r'^\d+\.\s+','',strip),size=10.5);i+=1;continue
    p=doc.add_paragraph();rich(p,strip,size=10.5)
    if re.match(r'^\*{0,2}表\s*T[-\s]?\d+',strip,re.I): p.paragraph_format.keep_with_next=True
    i+=1
if in_code and code_lines:
    p=doc.add_paragraph();r=p.add_run('\n'.join(code_lines));set_run_font(r,10.5,name=MONO,color='263238')
# Keep Word's required terminal paragraph on the last content page; it carries no visible content.
terminal=doc.paragraphs[-1] if doc.paragraphs else doc.add_paragraph()
terminal.paragraph_format.space_before=Pt(0)
terminal.paragraph_format.space_after=Pt(0)
terminal.paragraph_format.line_spacing=Pt(1)
terminal.paragraph_format.keep_together=False
terminal.paragraph_format.keep_with_next=False
terminal.paragraph_format.page_break_before=False
for run in terminal.runs: set_run_font(run,1)
# Refresh footer/header in every section (section breaks inherit, but make explicit)
for section in doc.sections:
    section.header.is_linked_to_previous=True
    section.footer.is_linked_to_previous=True
# File properties
props=doc.core_properties
props.title='績效改善調查與課後行動計畫追蹤套件'
props.subject='DOCX 0105 / I18-E13 / 專案157索引114（非官方方框序號）/ SAMPLE-SYNTHETIC candidate'
props.keywords='TTQS_ONE, 0105, I18-E13, project157-index114, SAMPLE, SYNTHETIC, REAL UNKNOWN'
props.comments='候選版本；非協會正式核准、非真實辦訓紀錄、非第三方證書。'
OUT.parent.mkdir(parents=True,exist_ok=True)
doc.save(OUT)
# Extract fact-level register tables from section 19 for separate replacement register.
start=text.find('## 十五、')
end=text.find('## 十六、',start)
if start<0 or end<0: raise SystemExit('fact register section boundaries missing')
section19=text[start:end].splitlines()
register_rows=[];subsection='';ii=0
while ii<len(section19):
    if section19[ii].startswith('###'):
        subsection=section19[ii].strip('# ').strip()
    if section19[ii].strip().startswith('|'):
        table=[]
        while ii<len(section19) and section19[ii].strip().startswith('|'):
            table.append(parse_cells(section19[ii]));ii+=1
        if len(table)>1 and all(re.fullmatch(r':?-{3,}:?',c.strip()) for c in table[1]): table=[table[0]]+table[2:]
        if table and 'fact_id' in table[0]:
            header=table[0]
            for row in table[1:]:
                if len(row)!=len(header): raise SystemExit('register row mismatch')
                register_rows.append([subsection]+row)
        continue
    ii+=1
if not register_rows: raise SystemExit('no fact register rows parsed')
CSV_OUT.parent.mkdir(parents=True,exist_ok=True)
with CSV_OUT.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f);w.writerow(['章節']+header);w.writerows(register_rows)
raw=OUT.read_bytes()
receipt={'receipt_id':'TTQS-0105-DOCX-BUILD-R01','created_at_tpe':datetime.datetime.now().astimezone().isoformat(),'source_markdown':str(MD),'source_markdown_sha256':hashlib.sha256(MD.read_bytes()).hexdigest(),'docx_path':str(OUT),'docx_sha256':hashlib.sha256(raw).hexdigest(),'docx_bytes':len(raw),'tables':table_count,'fact_register_rows':len(register_rows),'headings':heading_counts,'body_minimum_pt':10.5,'table_minimum_pt':9.5,'landscape_rule':'tables with 7 or more columns; orientation anticipated through bounded current/next-section lookahead and retained across ordinary paragraphs','synthetic_register_csv':str(CSV_OUT),'synthetic_register_sha256':hashlib.sha256(CSV_OUT.read_bytes()).hexdigest()}
receipt.update({'doc_id':'0105','official_requirement_id':'I18-E13','project_157_index':114,'official_checkbox_serial':'NOT_ASSERTED','source_packet_sha256':hashlib.sha256((BASE/'source'/'SOURCE_PACKET_0105_I18-E13_R01.md').read_bytes()).hexdigest(),'unique_blueprint_sha256':hashlib.sha256((BASE/'source'/'UNIQUE_BLUEPRINT_0105_I18-E13_R01.md').read_bytes()).hexdigest()})
BUILD_RECEIPT.parent.mkdir(parents=True,exist_ok=True)
BUILD_RECEIPT.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=True))
