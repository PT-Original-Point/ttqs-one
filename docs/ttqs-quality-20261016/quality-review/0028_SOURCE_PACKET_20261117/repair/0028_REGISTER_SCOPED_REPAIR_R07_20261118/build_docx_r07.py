from pathlib import Path
from hashlib import sha256
from decimal import Decimal
import json,re,os,sys
sys.path.append(r'C:\Users\J\AppData\Local\Temp\ttqs-html2docx-r05-py315')
from lxml import html as lhtml
from html2docx import HTML2Docx
from docx.shared import Mm,Pt
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.style import WD_STYLE_TYPE

BASE=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0028_SOURCE_PACKET_20261117\repair\0028_REGISTER_SCOPED_REPAIR_R07_20261118')
SRC=BASE/'candidate_0028_R07_20261118.html'
OUT=BASE/'candidate_0028_R07_20261118.docx'
TMP=BASE/'candidate_0028_R07_20261118.tmp.docx'
QA=BASE/'STATIC_QA_R07.json'
MATH=BASE/'MATH_QA_R07.json'
EXPECTED='0FBCE3F55EBCF87D4DD8D901ECCFBA3792D13159A8245BD22FDE149E2A949A14'
hexdigest=lambda b:sha256(b).hexdigest().upper()
raw=SRC.read_bytes()
if hexdigest(raw)!=EXPECTED: raise SystemExit('INPUT_SHA_MISMATCH')
if OUT.exists() or TMP.exists(): raise SystemExit('OUTPUT_EXISTS_REFUSE_OVERWRITE')
source=raw.decode('utf-8')
tree=lhtml.fromstring(source)
title=(tree.findtext('.//title') or '').strip()
body=tree.find('body')
if body is None: raise SystemExit('HTML_BODY_MISSING')
body_html=lhtml.tostring(body,encoding='unicode',method='html')
parser=HTML2Docx(title or 'TTQS ONE CANDIDATE')
parser.feed(body_html)
doc=parser.doc
sec=doc.sections[0]
sec.page_width=Mm(210);sec.page_height=Mm(297);sec.top_margin=Mm(10);sec.bottom_margin=Mm(10);sec.left_margin=Mm(10);sec.right_margin=Mm(10)

def font_east_asia(font, name='Microsoft JhengHei'):
    font.name=name
    el=font._element
    rpr=el.get_or_add_rPr()
    rfonts=rpr.rFonts
    if rfonts is None:
        rfonts=OxmlElement('w:rFonts');rpr.insert(0,rfonts)
    for key in ('ascii','hAnsi','eastAsia','cs'): rfonts.set(qn('w:'+key),name)

normal=doc.styles['Normal'];font_east_asia(normal.font);normal.font.size=Pt(11)
normal.paragraph_format.space_after=Pt(4);normal.paragraph_format.line_spacing=1.12
for nm,size,color in [('Heading 1',20,'183650'),('Heading 2',15,'183650'),('Heading 3',12,'183650'),('Heading 4',11,'183650')]:
    st=doc.styles[nm];font_east_asia(st.font);st.font.size=Pt(size);st.font.bold=True;st.font.color.rgb=__import__('docx').shared.RGBColor.from_string(color);st.paragraph_format.keep_with_next=True;st.paragraph_format.space_before=Pt(8);st.paragraph_format.space_after=Pt(3)
for p in doc.paragraphs:
    if p.style.name.startswith('Heading'):
        p.paragraph_format.keep_with_next=True
        for run in p.runs:
            font_east_asia(run.font);run.font.bold=True
    else:
        for run in p.runs:
            font_east_asia(run.font)
            if run.font.size is None or run.font.size.pt < 10.5: run.font.size=Pt(11)
        p.paragraph_format.line_spacing=1.12
for ti,table in enumerate(doc.tables):
    table.style='Table Grid';table.autofit=False
    cols=len(table.columns)
    if cols<1: raise SystemExit(f'EMPTY_TABLE_{ti}')
    usable=sec.page_width-sec.left_margin-sec.right_margin
    width=usable//cols
    for col in table.columns: col.width=width
    for row_i,row in enumerate(table.rows):
        trpr=row._tr.get_or_add_trPr()
        cant=OxmlElement('w:cantSplit');trpr.append(cant)
        if row_i==0:
            repeat=OxmlElement('w:tblHeader');repeat.set(qn('w:val'),'true');trpr.append(repeat)
        for cell in row.cells:
            cell.width=width;cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.TOP
            tcpr=cell._tc.get_or_add_tcPr()
            margins=tcpr.find(qn('w:tcMar'))
            if margins is None: margins=OxmlElement('w:tcMar');tcpr.append(margins)
            for side,val in [('top','55'),('start','65'),('bottom','55'),('end','65')]:
                node=margins.find(qn('w:'+side))
                if node is None: node=OxmlElement('w:'+side);margins.append(node)
                node.set(qn('w:w'),val);node.set(qn('w:type'),'dxa')
            for p in cell.paragraphs:
                p.paragraph_format.space_after=Pt(1);p.paragraph_format.line_spacing=1.02
                for run in p.runs:
                    font_east_asia(run.font);run.font.size=Pt(9.5)
                    if row_i==0: run.font.bold=True
        if row_i==0:
            for cell in row.cells:
                shd=OxmlElement('w:shd');shd.set(qn('w:fill'),'EAF0F4');cell._tc.get_or_add_tcPr().append(shd)

# Extract the saved document content for deterministic coverage and format verification.
doc.save(TMP)
from zipfile import ZipFile
from lxml import etree
with ZipFile(TMP) as z:
    xml=z.read('word/document.xml')
root=etree.fromstring(xml)
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
doc_text=''.join(root.xpath('.//w:t/text()',namespaces=ns))
source_text=' '.join(body.text_content().split())
ids=set(re.findall(r'SYN-0028-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d{3}',source_text));doc_ids=set(re.findall(r'SYN-0028-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d{3}',doc_text))
html_qa=json.loads(QA.read_text(encoding='utf-8'));math=json.loads(MATH.read_text(encoding='utf-8'))
expected_rows=html_qa['table_row_counts']
checks={
 'input_sha_exact':hexdigest(raw)==EXPECTED,
 'title_present_in_document':title in doc_text,
 'all_19_source_tables_preserved':len(doc.tables)==html_qa['table_count']==19,
 'table_row_counts_preserved':[len(t.rows) for t in doc.tables]==expected_rows,
 'all_91_registered_synthetic_ids_preserved':len(ids)==91 and ids==doc_ids,
 'same_sha_static_and_math_qa_pass':html_qa['candidate_html_sha256']==math['candidate_html_sha256']==EXPECTED,
 'static_qa_pass':html_qa['result']=='PASS_STATIC_HTML_ONLY',
 'math_qa_pass':math['result']=='PASS_DETERMINISTIC_MATH_AND_FACT_REGISTER_R07',
 'a4_page_geometry':round(sec.page_width.mm)==210 and round(sec.page_height.mm)==297,
 'body_font_floor_11pt':normal.font.size.pt>=11,
 'table_font_floor_9_5pt':all(run.font.size is None or run.font.size.pt>=9.5 for t in doc.tables for row in t.rows for cell in row.cells for p in cell.paragraphs for run in p.runs),
 'no_output_overwrite':not OUT.exists(),
}
result='PASS_CONVERSION_STRUCTURE_AND_FONT_CHECKS' if all(checks.values()) else 'FAIL'
if result!='PASS_CONVERSION_STRUCTURE_AND_FONT_CHECKS':
    TMP.unlink(missing_ok=True);raise SystemExit(json.dumps({'checks':checks,'result':result},ensure_ascii=False))
os.replace(TMP,OUT)
outbytes=OUT.read_bytes()
receipt={'schema':'TTQS_ONE_0028_HTML_TO_DOCX_CONVERSION_R07','work_id':'TTQS_ONE_0028_I05-E02_HTML_TO_DOCX_R07_20261118','input_html_path':str(SRC),'input_html_sha256':EXPECTED,'output_docx_path':str(OUT),'output_docx_bytes':len(outbytes),'output_docx_sha256':hexdigest(outbytes),'tool':'html2docx 1.6.0 + python-docx 1.2.0 + lxml 6.1.1, isolated under %TEMP%','word_com_status':'BLOCKED_UNRESPONSIVE_WORD_COM; no Word rendering receipt for DOCX','html_tables':html_qa['table_count'],'docx_tables':len(doc.tables),'html_row_counts':expected_rows,'docx_row_counts':[len(t.rows) for t in doc.tables],'synthetic_id_count':len(ids),'checks':checks,'result':result,'visual_review':'PENDING; LibreOffice/soffice is not installed and render_docx.py cannot import pdf2image; prior Word COM attempt was unresponsive and was not repeated','semantic_review_for_docx':'PENDING_EXACT_DOCX_SHA; builder does not grant semantic PASS','formal_acceptance':'NOT_CLAIMED'}
receipt_path=BASE/'DOCX_CONVERSION_R07.json';receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False))
print('conversion_receipt_sha256',hexdigest(receipt_path.read_bytes()))
