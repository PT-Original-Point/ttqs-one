import re
import sys
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

BLUE = '17365D'
PALE = 'DCE6F1'

def set_run_font(run, size=11, bold=None, color=None, italic=None):
    run.font.name = 'Microsoft JhengHei'
    run._element.get_or_add_rPr().get_or_add_rFonts().set(qn('w:eastAsia'), 'Microsoft JhengHei')
    run.font.size = Pt(size)
    if bold is not None: run.bold = bold
    if italic is not None: run.italic = italic
    if color: run.font.color.rgb = RGBColor.from_string(color)

def set_cell_shading(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = tcPr.find(qn('w:shd'))
    if shd is None:
        shd = OxmlElement('w:shd'); tcPr.append(shd)
    shd.set(qn('w:fill'), fill)

def set_repeat_table_header(row):
    trPr = row._tr.get_or_add_trPr()
    tblHeader = OxmlElement('w:tblHeader'); tblHeader.set(qn('w:val'), 'true'); trPr.append(tblHeader)

def set_cell_margins(cell, top=70, start=80, bottom=70, end=80):
    tc = cell._tc; tcPr = tc.get_or_add_tcPr()
    tcMar = tcPr.first_child_found_in('w:tcMar')
    if tcMar is None:
        tcMar = OxmlElement('w:tcMar'); tcPr.append(tcMar)
    for m, v in [('top',top),('start',start),('bottom',bottom),('end',end)]:
        node = tcMar.find(qn('w:'+m))
        if node is None: node = OxmlElement('w:'+m); tcMar.append(node)
        node.set(qn('w:w'), str(v)); node.set(qn('w:type'), 'dxa')

def inline(p, text, size=11, color=None, bold=None):
    parts = re.split(r'(\*\*.*?\*\*|\*[^*].*?\*|`[^`]+`)', text)
    for part in parts:
        if not part: continue
        is_bold = part.startswith('**') and part.endswith('**')
        italic = (not is_bold) and part.startswith('*') and part.endswith('*')
        code = part.startswith('`') and part.endswith('`')
        value = part[2:-2] if is_bold else (part[1:-1] if italic or code else part)
        r = p.add_run(value)
        set_run_font(r, size=size, bold=True if (is_bold or bold) else None, italic=italic, color=('404040' if code else color))

def split_row(line):
    value = line.strip().strip('|').replace(r'\|', '\x00')
    cells = [c.strip().replace('\x00','|') for c in value.split('|')]
    return cells

def is_separator(line):
    cells = split_row(line)
    return bool(cells) and all(re.fullmatch(r':?-{3,}:?', c.replace(' ','')) for c in cells)

def add_table(doc, rows):
    if len(rows) < 2: return
    cols = max(len(r) for r in rows)
    table = doc.add_table(rows=len(rows), cols=cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True
    try: table.style = 'Table Grid'
    except KeyError: pass
    for ri, rowdata in enumerate(rows):
        row = table.rows[ri]
        trPr = row._tr.get_or_add_trPr(); cant = OxmlElement('w:cantSplit'); trPr.append(cant)
        if ri == 0: set_repeat_table_header(row)
        for ci in range(cols):
            cell = row.cells[ci]; cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            set_cell_margins(cell)
            if ri == 0: set_cell_shading(cell, PALE)
            cell.text = ''
            p = cell.paragraphs[0]; p.paragraph_format.space_after = Pt(0); p.paragraph_format.line_spacing = 1.0
            value = rowdata[ci] if ci < len(rowdata) else ''
            inline(p, value, size=9.5)
            for run in p.runs:
                if ri == 0: run.bold = True; run.font.color.rgb = RGBColor.from_string(BLUE)
    doc.add_paragraph().paragraph_format.space_after = Pt(1)

def add_page_field(paragraph):
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = paragraph.add_run('第 '); set_run_font(r, 9, color='666666')
    fld = OxmlElement('w:fldSimple'); fld.set(qn('w:instr'), 'PAGE')
    r2 = OxmlElement('w:r'); t = OxmlElement('w:t'); t.text = '1'; r2.append(t); fld.append(r2); paragraph._p.append(fld)
    r = paragraph.add_run(' 頁'); set_run_font(r, 9, color='666666')

def build(src, dst):
    text = open(src, 'r', encoding='utf-8-sig').read().replace('\r\n','\n')
    lines = text.split('\n')
    doc = Document()
    sec = doc.sections[0]
    sec.page_width = Inches(8.27); sec.page_height = Inches(11.69)
    sec.top_margin = Inches(0.68); sec.bottom_margin = Inches(0.68); sec.left_margin = Inches(0.72); sec.right_margin = Inches(0.72)
    sec.header_distance = Inches(0.3); sec.footer_distance = Inches(0.3)
    styles = doc.styles
    for name, size, color in [('Normal',11,'202020'),('Title',22,BLUE),('Heading 1',15,BLUE),('Heading 2',12,BLUE),('Heading 3',11,BLUE)]:
        st = styles[name]; st.font.name = 'Microsoft JhengHei'; st._element.rPr.rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei'); st.font.size = Pt(size); st.font.color.rgb = RGBColor.from_string(color)
    styles['Normal'].paragraph_format.space_after = Pt(6); styles['Normal'].paragraph_format.line_spacing = 1.12
    styles['Heading 1'].paragraph_format.space_before = Pt(13); styles['Heading 1'].paragraph_format.space_after = Pt(5); styles['Heading 1'].paragraph_format.keep_with_next = True
    styles['Heading 2'].paragraph_format.space_before = Pt(9); styles['Heading 2'].paragraph_format.space_after = Pt(4); styles['Heading 2'].paragraph_format.keep_with_next = True
    styles['Heading 3'].paragraph_format.space_before = Pt(7); styles['Heading 3'].paragraph_format.space_after = Pt(3); styles['Heading 3'].paragraph_format.keep_with_next = True
    foot = sec.footer.paragraphs[0]; add_page_field(foot)
    i = 0; title_done = False
    while i < len(lines):
        line = lines[i].strip()
        if not line or line in ('---','***'): i += 1; continue
        if line.startswith('|') and i+1 < len(lines) and lines[i+1].strip().startswith('|') and is_separator(lines[i+1]):
            rows=[]; rows.append(split_row(line)); i += 2
            while i < len(lines) and lines[i].strip().startswith('|'):
                rows.append(split_row(lines[i])); i += 1
            add_table(doc, rows); continue
        m = re.match(r'^(#{1,3})\s+(.+)$', line)
        if m:
            level=len(m.group(1)); value=m.group(2).strip()
            if level == 1 and not title_done:
                p=doc.add_paragraph(style='Title'); inline(p,value,size=22,bold=True,color=BLUE); title_done=True
            else:
                p=doc.add_paragraph(style=f'Heading {level}'); inline(p,value,size={1:15,2:12,3:11}[level],bold=True,color=BLUE)
            i += 1; continue
        if line.startswith('> '):
            p=doc.add_paragraph(); p.paragraph_format.left_indent=Inches(0.22); p.paragraph_format.right_indent=Inches(0.12); p.paragraph_format.space_before=Pt(3); p.paragraph_format.space_after=Pt(7); inline(p,line[2:],size=10.5,color='4B5563'); i+=1; continue
        bullet=re.match(r'^[-*]\s+(.+)$',line)
        numbered=re.match(r'^\d+[.)]\s+(.+)$',line)
        if bullet or numbered:
            p=doc.add_paragraph(style='List Bullet' if bullet else 'List Number'); inline(p,(bullet or numbered).group(1),size=11); i+=1; continue
        if line.startswith('```'):
            i+=1
            while i<len(lines) and not lines[i].strip().startswith('```'):
                p=doc.add_paragraph(); p.paragraph_format.left_indent=Inches(0.2); inline(p,lines[i],size=9.5)
                i+=1
            i+=1; continue
        p=doc.add_paragraph(); inline(p,line,size=11); i+=1
    if not title_done: raise ValueError('Markdown title missing')
    doc.core_properties.title = '訓練需求調查與需求配適報告'
    doc.core_properties.subject = '0033 I07-E01 SAMPLE SYNTHETIC 候選文件'
    doc.core_properties.author = 'TTQS ONE'
    doc.core_properties.keywords = '0033; I07-E01; SAMPLE; SYNTHETIC'
    doc.save(dst)

if __name__ == '__main__':
    if len(sys.argv) != 3: raise SystemExit('usage: build_markdown_docx.py input.md output.docx')
    build(sys.argv[1], sys.argv[2])