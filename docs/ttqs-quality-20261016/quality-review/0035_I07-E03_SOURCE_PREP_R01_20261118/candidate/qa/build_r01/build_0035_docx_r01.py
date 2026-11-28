from pathlib import Path
import hashlib, json, re, sys
from datetime import datetime, timezone
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

src = Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0035_I07-E03_SOURCE_PREP_R01_20261118\writer\attempt_0035_W1_R01\WORKER_BODY_R01_RECOVERED.md')
root = Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0035_I07-E03_SOURCE_PREP_R01_20261118')
source = root / 'SOURCE_PACKET_0035_I07-E03_R01.md'
blueprint = root / 'UNIQUE_BLUEPRINT_0035_I07-E03_R01.md'
work_input = root / 'writer' / 'attempt_0035_W1_R01' / 'WORKER_INPUT_R01.md'
worker_log = root / 'writer' / 'attempt_0035_W1_R01' / 'stdout.jsonl'
out = root / 'candidate' / '0035_I07-E03_R01_W1_NEMOTRON.docx'
receipt = root / 'candidate' / 'qa' / 'build_r01' / 'BUILD_RECEIPT_0035_I07-E03_R01.json'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest().upper()
def set_run_font(run, size_pt, bold=None, color=None, italic=None):
    run.font.name = 'Microsoft JhengHei'
    run._element.get_or_add_rPr().rFonts.set(qn('w:eastAsia'), 'Microsoft JhengHei')
    run._element.get_or_add_rPr().rFonts.set(qn('w:ascii'), 'Microsoft JhengHei')
    run._element.get_or_add_rPr().rFonts.set(qn('w:hAnsi'), 'Microsoft JhengHei')
    run.font.size = Pt(size_pt)
    if bold is not None: run.bold = bold
    if color is not None: run.font.color.rgb = RGBColor(*color)
    if italic is not None: run.italic = italic

def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = tcPr.find(qn('w:shd'))
    if shd is None:
        shd = OxmlElement('w:shd'); tcPr.append(shd)
    shd.set(qn('w:fill'), fill)

def cell_margins(cell, top=80, start=90, bottom=80, end=90):
    tc = cell._tc; tcPr = tc.get_or_add_tcPr()
    mar = tcPr.first_child_found_in('w:tcMar')
    if mar is None:
        mar = OxmlElement('w:tcMar'); tcPr.append(mar)
    for m,v in [('top',top),('start',start),('bottom',bottom),('end',end)]:
        node = mar.find(qn('w:'+m))
        if node is None: node=OxmlElement('w:'+m); mar.append(node)
        node.set(qn('w:w'), str(v)); node.set(qn('w:type'),'dxa')

def add_inline(paragraph, text, size_pt=11, bold=False, color=None, italic=False):
    # Compact Markdown inline styling, preserving all literal text.
    tokens = re.split(r'(\*\*.*?\*\*|`[^`]+`|\*[^*]+\*)', text)
    for token in tokens:
        if token == '': continue
        is_bold = token.startswith('**') and token.endswith('**')
        is_code = token.startswith('`') and token.endswith('`')
        is_italic = token.startswith('*') and token.endswith('*') and not is_bold
        value = token[2:-2] if is_bold else (token[1:-1] if is_code or is_italic else token)
        pieces = value.split('<br>')
        for idx,piece in enumerate(pieces):
            if idx: paragraph.add_run().add_break()
            run = paragraph.add_run(piece)
            set_run_font(run, size_pt, bold=(bold or is_bold), color=color, italic=(italic or is_italic))
            if is_code:
                run.font.name = 'Consolas'; run._element.get_or_add_rPr().rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei')

def parse_cells(line):
    s=line.strip()
    if s.startswith('|'): s=s[1:]
    if s.endswith('|'): s=s[:-1]
    return [x.strip().replace(r'\|','|') for x in s.split('|')]

def is_separator(line):
    cells=parse_cells(line)
    return bool(cells) and all(re.fullmatch(r':?-{3,}:?', c.replace(' ','')) for c in cells)

def add_page_field(paragraph):
    run=paragraph.add_run(); set_run_font(run,9)
    begin=OxmlElement('w:fldChar'); begin.set(qn('w:fldCharType'),'begin')
    instr=OxmlElement('w:instrText'); instr.set(qn('xml:space'),'preserve'); instr.text=' PAGE '
    separate=OxmlElement('w:fldChar'); separate.set(qn('w:fldCharType'),'separate')
    text=OxmlElement('w:t'); text.text='1'
    end=OxmlElement('w:fldChar'); end.set(qn('w:fldCharType'),'end')
    for el in (begin,instr,separate,text,end): run._r.append(el)

if not all(p.exists() for p in (src,source,blueprint,work_input,worker_log)):
    raise SystemExit('Required input file missing')
body=src.read_text(encoding='utf-8-sig')
source_hash, blueprint_hash, body_hash = sha(source), sha(blueprint), sha(src)
doc=Document()
sec=doc.sections[0]
sec.orientation=WD_ORIENT.LANDSCAPE
sec.page_width=Inches(11.69); sec.page_height=Inches(8.27)
sec.top_margin=Inches(.62); sec.bottom_margin=Inches(.62); sec.left_margin=Inches(.58); sec.right_margin=Inches(.58)
sec.header_distance=Inches(.28); sec.footer_distance=Inches(.28)
normal=doc.styles['Normal']; normal.font.name='Microsoft JhengHei'; normal.font.size=Pt(11)
normal._element.rPr.rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei')
normal.paragraph_format.space_after=Pt(5); normal.paragraph_format.line_spacing=1.08
for name,size in [('Title',18),('Heading 1',15),('Heading 2',13),('Heading 3',11.5)]:
    st=doc.styles[name]; st.font.name='Microsoft JhengHei'; st.font.size=Pt(size); st.font.bold=True
    st._element.rPr.rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei')
    st.font.color.rgb=RGBColor(31,66,110)
    st.paragraph_format.keep_with_next=True; st.paragraph_format.space_before=Pt(9); st.paragraph_format.space_after=Pt(4)
header=sec.header.paragraphs[0]; header.alignment=WD_ALIGN_PARAGRAPH.RIGHT
add_inline(header,'TTQS ONE  |  0035 / I07-E03  |  CANDIDATE · SAMPLE/SYNTHETIC',9,color=(85,100,120))
footer=sec.footer.paragraphs[0]; footer.alignment=WD_ALIGN_PARAGRAPH.CENTER
add_inline(footer,'TTQS ONE candidate  •  ',9,color=(100,100,100)); add_page_field(footer)

lines=body.splitlines(); i=0; paragraph_count=0; table_count=0; synthetic_ids=set()
while i<len(lines):
    raw=lines[i]; s=raw.strip()
    if not s or s in ('---','***','___'):
        i+=1; continue
    if s.startswith('|'):
        rows=[]
        while i<len(lines) and lines[i].strip().startswith('|'):
            if not is_separator(lines[i]): rows.append(parse_cells(lines[i]))
            i+=1
        if not rows: continue
        cols=max(len(r) for r in rows)
        table=doc.add_table(rows=0, cols=cols)
        table.style='Table Grid'; table.alignment=WD_TABLE_ALIGNMENT.CENTER; table.autofit=True
        table.allow_autofit=True
        for ri,rowdata in enumerate(rows):
            cells=table.add_row().cells
            for ci in range(cols):
                cell=cells[ci]; cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER; cell_margins(cell)
                para=cell.paragraphs[0]; para.paragraph_format.space_after=Pt(0); para.paragraph_format.line_spacing=1.0
                value=rowdata[ci] if ci<len(rowdata) else ''
                add_inline(para,value,size_pt=9.5,bold=(ri==0),color=(255,255,255) if ri==0 else None)
                if ri==0: shade(cell,'24476B')
                elif ri%2==0: shade(cell,'F2F6FA')
            if ri==0:
                trPr=table.rows[ri]._tr.get_or_add_trPr(); repeat=OxmlElement('w:tblHeader'); repeat.set(qn('w:val'),'true'); trPr.append(repeat)
            trPr=table.rows[ri]._tr.get_or_add_trPr(); cant=OxmlElement('w:cantSplit'); trPr.append(cant)
        doc.add_paragraph().paragraph_format.space_after=Pt(0)
        table_count+=1
        continue
    heading=re.match(r'^(#{1,3})\s+(.*)$',s)
    if heading:
        level=len(heading.group(1)); text=heading.group(2)
        p=doc.add_paragraph(style='Title' if level==1 else f'Heading {level-1}')
        add_inline(p,text,size_pt=18 if level==1 else (15 if level==2 else 13),bold=True,color=(31,66,110))
        paragraph_count+=1; i+=1; continue
    if s.startswith('> '):
        p=doc.add_paragraph(); p.paragraph_format.left_indent=Inches(.25); p.paragraph_format.right_indent=Inches(.2)
        add_inline(p,s[2:],size_pt=11,italic=True if False else False,color=(70,80,95)); paragraph_count+=1; i+=1; continue
    bullet=re.match(r'^[-*+]\s+(.*)$',s)
    numbered=re.match(r'^\d+[.)]\s+(.*)$',s)
    if bullet or numbered:
        content=(bullet or numbered).group(1)
        p=doc.add_paragraph(style='List Bullet' if bullet else 'List Number')
        p.paragraph_format.space_after=Pt(3); add_inline(p,content,size_pt=11)
        paragraph_count+=1; i+=1; continue
    p=doc.add_paragraph(); add_inline(p,s,size_pt=11)
    if len(s)>180: p.paragraph_format.widow_control=True
    paragraph_count+=1; i+=1

# Register all visibly used synthetic identifiers; this is a build metric, not a QA pass.
synthetic_ids=sorted(set(re.findall(r'SYN-0035-[A-Za-z0-9-]+',body)))
props=doc.core_properties
props.title='0035 I07-E03 職能分析與運用方法檢討改進｜SAMPLE/SYNTHETIC CANDIDATE'
props.subject='TTQS ONE evidence document candidate; not formal acceptance'
props.author='TTQS ONE candidate workflow'
props.keywords='TTQS, 0035, I07-E03, SAMPLE, SYNTHETIC, CANDIDATE'
out.parent.mkdir(parents=True,exist_ok=True); doc.save(out)
receipt_data={
 'receipt_type':'TTQS_ONE_BUILD_RECEIPT','doc_id':'0035','requirement_id':'I07-E03','status':'CANDIDATE_BUILD_COMPLETE_VISUAL_QA_PENDING',
 'built_at_utc':datetime.now(timezone.utc).isoformat(),'worker_id':'W1_OpenCode_v2.2.5','work_id':'TTQS_ONE_0035_I07-E03_WRITER_R01_NEMOTRON_20261118',
 'requested_route':'opencode/nemotron-3.5-lightning-free','provider_served_model':'UNKNOWN','worker_exit_code':'UNKNOWN_NOT_CAPTURED',
 'worker_markdown_path':str(src),'worker_markdown_sha256':body_hash,'work_input_path':str(work_input),'work_input_sha256':sha(work_input),
 'source_packet_path':str(source),'source_packet_sha256':source_hash,'unique_blueprint_path':str(blueprint),'unique_blueprint_sha256':blueprint_hash,
 'output_path':str(out),'output_sha256':sha(out),'output_bytes':out.stat().st_size,'body_paragraphs':paragraph_count,'tables':table_count,
 'synthetic_identifier_count':len(synthetic_ids),'synthetic_identifier_values':synthetic_ids,
 'format_policy':{'page':'A4 landscape','body_min_pt':11,'table_min_pt':9.5,'status':'VISUAL_RENDER_PENDING'},
 'github_sync':'NOT_ATTEMPTED','formal_acceptance':'NOT_CLAIMED'
}
receipt.parent.mkdir(parents=True,exist_ok=True); receipt.write_text(json.dumps(receipt_data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Reopen and confirm structural integrity before reporting success.
verify=Document(out)
if len(verify.tables)!=table_count: raise SystemExit('table count mismatch after reopen')
print(json.dumps({'output':str(out),'sha256':sha(out),'bytes':out.stat().st_size,'tables':table_count,'body_paragraphs':paragraph_count,'synthetic_ids':len(synthetic_ids),'receipt':str(receipt),'receipt_sha256':sha(receipt)},ensure_ascii=False))


