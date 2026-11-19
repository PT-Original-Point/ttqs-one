from argparse import ArgumentParser
from pathlib import Path
from zipfile import ZipFile
from hashlib import sha256
from lxml import etree
from PIL import Image, ImageChops
from pypdf import PdfReader
import json

p=ArgumentParser()
p.add_argument('--source',required=True)
p.add_argument('--candidate',required=True)
p.add_argument('--pdf',required=True)
p.add_argument('--render-dir',required=True)
p.add_argument('--receipt',required=True)
a=p.parse_args()
source,candidate,pdf,render_dir,receipt=map(Path,(a.source,a.candidate,a.pdf,a.render_dir,a.receipt))
sha=lambda path: sha256(path.read_bytes()).hexdigest()
WURI='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
W='{%s}'%WURI
NS={'w':WURI}
def get_parts(path):
    with ZipFile(path) as z:
        bad=z.testzip()
        if bad: raise RuntimeError(f'Bad package member: {bad}')
        return {i.filename:z.read(i.filename) for i in z.infolist()}
def find_target(xml):
    doc=etree.fromstring(xml)
    body=doc.find('.//w:body',NS)
    for table in body.findall('./w:tbl',NS):
        rows=table.findall('./w:tr',NS)
        if not rows: continue
        head=''.join(rows[0].xpath('.//w:t/text()',namespaces=NS))
        text=''.join(table.xpath('.//w:t/text()',namespaces=NS))
        if all(s in head for s in ('觀察標準','關鍵錯誤')):
            return doc,body,table,rows
    raise RuntimeError('Exact service-record rubric table not found')
src_parts=get_parts(source); out_parts=get_parts(candidate)
if set(src_parts)!=set(out_parts): raise RuntimeError('DOCX package member list changed')
changed=[name for name in src_parts if src_parts[name]!=out_parts[name]]
if changed!=['word/document.xml']:
    raise RuntimeError(f'Unexpected package-part differences: {changed}')
s_doc,s_body,s_table,s_rows=find_target(src_parts['word/document.xml'])
o_doc,o_body,o_table,o_rows=find_target(out_parts['word/document.xml'])
if len(s_rows)!=9 or len(o_rows)!=8: raise RuntimeError('Unexpected source or output table row count')
break_p=o_table.getnext()
continuation=break_p.getnext() if break_p is not None else None
if break_p is None or break_p.tag!=W+'p' or not break_p.xpath('.//w:br[@w:type="page"]',namespaces=NS): raise RuntimeError('Expected explicit page break before continuation table')
if continuation is None or continuation.tag!=W+'tbl': raise RuntimeError('Continuation table missing')
c_rows=continuation.findall('./w:tr',NS)
if len(c_rows)!=2: raise RuntimeError('Continuation table must contain header and one data row')
header_nodes=c_rows[0].xpath('.//w:t',namespaces=NS)
if not continuation.xpath('./w:tr[1]/w:trPr/w:tblHeader',namespaces=NS): raise RuntimeError('Continuation header row not marked')
header_text=[n.text or '' for n in header_nodes]
if ''.join(header_text)!=''.join(s_rows[0].xpath('.//w:t/text()',namespaces=NS)): raise RuntimeError('Continuation heading mismatch')
if '8使用合適的受控交接方式' not in ''.join(c_rows[1].xpath('.//w:t/text()',namespaces=NS)): raise RuntimeError('Final rubric row missing')
def visible_text_without_duplicate_header(doc, duplicate_row=None):
    vals=[]
    for node in doc.iter(W+'t'):
        parent=node.getparent(); skip=False
        while parent is not None:
            if duplicate_row is not None and parent is duplicate_row:
                skip=True; break
            parent=parent.getparent()
        if not skip: vals.append(node.text or '')
    return vals
if visible_text_without_duplicate_header(s_doc)!=visible_text_without_duplicate_header(o_doc,c_rows[0]):
    raise RuntimeError('Text sequence changed beyond one duplicated table-header row')
images=[]
for i in range(1,20):
    old=source.parent.parent/'render'/'R08_final_review'/f'page-{i:02}.png'
    new=render_dir/f'page-{i:02}.png'
    if not new.exists(): raise RuntimeError(f'Missing render page {i}')
    im=Image.open(new).convert('RGB')
    images.append({'page':i,'path':f'evidence/render/page-{i:02}.png','sha256':sha(new),'size_px':list(im.size), 'inspected': 'DIRECT' if i>=12 else 'R08_VISUAL_DIRECT_PLUS_R09_PIXEL_IDENTITY'})
    if i<=11:
        if not old.exists(): raise RuntimeError(f'Missing baseline page {i}')
        prev=Image.open(old).convert('RGB')
        if prev.size!=im.size or ImageChops.difference(prev,im).getbbox() is not None:
            raise RuntimeError(f'Unexpected visual delta on unchanged page {i}')
reader=PdfReader(str(pdf))
if len(reader.pages)!=19: raise RuntimeError(f'Expected 19 pages, got {len(reader.pages)}')
if len(images)!=19: raise RuntimeError('Expected 19 rendered page images')
receipt_obj={
 'project_id':'TTQS_ONE','doc_id':'0036','requirement_id':'I07-E04','official_checkbox_serial':'036',
 'revision':'R09','status':'FULL_VISUAL_PASS_CANDIDATE_ONLY',
 'candidate_sha256':sha(candidate),'candidate_bytes':candidate.stat().st_size,
 'source_revision':'R08','source_candidate_sha256':sha(source),
 'render_engine':'Microsoft Word COM export, 144 dpi PNG; same renderer family as the R08 baseline',
 'render_pdf_sha256':sha(pdf),'render_pdf_bytes':pdf.stat().st_size,'page_count':len(reader.pages),'page_image_count':len(images),
 'package_diff_parts':changed,
 'package_integrity':'PASS','text_integrity':'PASS_AFTER_EXCLUDING_ONE_DUPLICATED_HEADER_ROW',
 'original_rubric_rows':len(s_rows),'output_rubric_rows_first_table':len(o_rows),'output_rubric_rows_continuation_table':len(c_rows),
 'visual_finding_fixed':{'page':13,'finding':'The final row of the 8-item service-record rubric was stranded on page 13 without visible column labels.','repair':'Split only the final row into a continuation table with the same four-column header; use the existing blank paragraph as a page break. No prose, sample values, calculations, or decisions changed.'},
 'visual_review':{'pages_01_11':'PASS; pixel-identical to R08 Word COM baseline and directly inspected from the source render; page 5 flowchart directly re-inspected after final render.','pages_12_19':'PASS; every page directly inspected after patch.','page_13':'PASS; continuation heading is visible above rubric item 8.','clipping_overlap_blank_page_or_footer_defect':'NONE_OBSERVED'},
 'semantic_review_status':'R08 exact-SHA independent semantic PASS_WITH_DECLARED_SCOPE remains linked to R08 SHA. R09 changes only table structure and duplicates the column heading; no fresh R09 exact-SHA semantic review is claimed.',
 'candidate_disposition':'CANDIDATE_ONLY_NOT_PROMOTED',
 'page_images':images
}
receipt.parent.mkdir(parents=True,exist_ok=True)
receipt.write_text(json.dumps(receipt_obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in receipt_obj.items() if k!='page_images'},ensure_ascii=False,indent=2))
print('PAGE_IMAGE_SHAS='+json.dumps(images,ensure_ascii=False))

