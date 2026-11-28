from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
from docx import Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph

root=Path(r'E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0076_R01')
docx=root/'candidate'/'0076_R01.docx'
visual_dir=root/'evidence'/'render_word_R01'
review_dir=root/'review'
review_dir.mkdir(parents=True,exist_ok=True)
def digest(p): return sha256(p.read_bytes()).hexdigest()
D=Document(docx)
lines=[f'# DOCX text extraction bound to SHA-256 {digest(docx)}','',f'File bytes: {docx.stat().st_size}','']
body=D.element.body
pnum=0; tnum=0
for child in body.iterchildren():
    if isinstance(child,CT_P):
        p=Paragraph(child,D)
        text=''.join(run.text for run in p.runs).strip()
        if text:
            pnum += 1
            style=p.style.name if p.style else ''
            if style.startswith('Heading') or style=='Title':
                lines.append(f'\n## [{style}] {text}\n')
            else:
                lines.append(text)
    elif isinstance(child,CT_Tbl):
        tnum += 1
        table=Table(child,D)
        lines.append(f'\n### TABLE {tnum}\n')
        for row in table.rows:
            cells=[' / '.join(c.text.splitlines()).strip().replace('|','\\|') for c in row.cells]
            lines.append('| '+' | '.join(cells)+' |')
text='\n'.join(lines)+'\n'
out=review_dir/'docx_extracted_R01.md'
out.write_text(text,encoding='utf-8')
extract_receipt={
 'schema':'TTQS_ONE_0076_DOCX_TEXT_EXTRACTION_R01.v1','document_id':'0076','requirement_id':'I17B-E01','official_checkbox_serial':'084',
 'docx_path':'candidate/0076_R01.docx','docx_sha256':digest(docx),'docx_bytes':docx.stat().st_size,
 'extracted_path':'review/docx_extracted_R01.md','extracted_sha256':digest(out),'extracted_bytes':out.stat().st_size,
 'paragraphs_extracted':pnum,'tables_extracted':tnum,'method':'python-docx ordered body traversal; paragraphs and tables preserved in document order',
 'status':'COMPLETE','created_utc':datetime.now(timezone.utc).isoformat()
}
(root/'evidence'/'docx_extraction_receipt_R01.json').write_text(json.dumps(extract_receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
pdf=visual_dir/'0076_R01_word_render.pdf'
pages=sorted((visual_dir/'pages').glob('page-*.png'))
contacts=sorted(visual_dir.glob('contact-*.jpg'))
visual={
 'schema':'TTQS_ONE_0076_VISUAL_REVIEW_R01.v1','document_id':'0076','requirement_id':'I17B-E01','official_checkbox_serial':'084',
 'docx_sha256':digest(docx),'docx_bytes':docx.stat().st_size,
 'render_method':'Microsoft Word COM, hidden read-only instance, PDF export; pypdfium2 rasterization at 1.8 scale',
 'render_pdf':{'path':'evidence/render_word_R01/0076_R01_word_render.pdf','sha256':digest(pdf),'bytes':pdf.stat().st_size},
 'page_count':len(pages),'page_pngs':[{'path':'evidence/render_word_R01/pages/'+p.name,'sha256':digest(p),'bytes':p.stat().st_size} for p in pages],
 'contact_sheets':[{'path':'evidence/render_word_R01/'+p.name,'sha256':digest(p),'bytes':p.stat().st_size} for p in contacts],
 'visual_scope':'All 26 pages inspected using seven contact sheets. Full-resolution spot inspections: pages 13, 14 (continued table and repeated header), 18, 19 (assessment table page break), 24, 25 (cross-document table and calculation annex continuation), and 26 (final page).',
 'observations':['No clipped text, overlap, broken table borders, missing glyphs, or unreadable page content observed.','Continuation tables remain identifiable and the Q11-Q20 table repeats its header on page 14.','Running header and page-number footer are consistent through pages 1-26.','Page 26 ends with a complete source-location table and adequate remaining whitespace.'],
 'limitations':['Digital Word export reviewed; physical printer output and accessibility tagging were not tested.'],
 'visual_status':'PASS','formal_acceptance':'NOT_GRANTED','real_status':'UNKNOWN/HOLD','created_utc':datetime.now(timezone.utc).isoformat()
}
(root/'evidence'/'visual_review_R01.json').write_text(json.dumps(visual,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'docx_sha256':digest(docx),'extracted_sha256':digest(out),'extracted_bytes':out.stat().st_size,'tables':tnum,'paragraphs':pnum,'visual_receipt_sha256':digest(root/'evidence'/'visual_review_R01.json'),'pdf_sha256':digest(pdf),'page_count':len(pages),'contact_sheets':len(contacts)},ensure_ascii=False))
