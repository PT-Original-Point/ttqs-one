from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from lxml import etree
from docx import Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.text.paragraph import Paragraph
from docx.table import Table
from datetime import datetime
import hashlib,json
base=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0032_I06-E03_SOURCE_PREP_R01_20261118')
candidate_dir=base/'candidate'
src=candidate_dir/'0032_I06-E03_R02_FONT_REPAIR.docx'
dst=candidate_dir/'0032_I06-E03_R03_LAYOUT_FLOW_REPAIR.docx'
receipt_path=base/'candidate'/'qa'/'scoped_repair_r03'/'SCOPED_REPAIR_RECEIPT_R03.json'
if dst.exists() or receipt_path.exists(): raise SystemExit('R03 output exists; refusing overwrite')
def sha(b): return hashlib.sha256(b).hexdigest().upper()
def body_text(doc):
    parts=[]; ti=0
    for el in doc.element.body.iterchildren():
        if isinstance(el,CT_P):
            p=Paragraph(el,doc)
            if p.text.strip(): parts.append(p.text)
        elif isinstance(el,CT_Tbl):
            ti+=1; t=Table(el,doc); parts.append(f'\n[TABLE {ti}]')
            for row in t.rows: parts.append(' | '.join(' / '.join(p.text.strip() for p in c.paragraphs if p.text.strip()) for c in row.cells))
            parts.append(f'[/TABLE {ti}]\n')
    return '\n'.join(parts).strip()+'\n'
def table_text(doc):
    rows=[]
    for t in doc.tables:
        for row in t.rows: rows.append(tuple(c.text for c in row.cells))
    return hashlib.sha256(json.dumps(rows,ensure_ascii=False,separators=(',',':')).encode('utf-8')).hexdigest().upper()
old=src.read_bytes(); old_sha=sha(old)
expected='0094D7D72654A072076325BD7F69237C059B87BCC248314D623CDAC074B038B2'
if old_sha!=expected: raise SystemExit(f'R02 SHA changed: {old_sha}')
prior_doc=Document(src); body_before=body_text(prior_doc); body_sha_before=sha(body_before.encode('utf-8')); table_sha_before=table_text(prior_doc)
if body_sha_before!='BADBC5E8CC0101B5CA3C84B0AA5AA7F27BCEF0ABAF357E677FC86ACB2E40E378': raise SystemExit(f'body hash mismatch: {body_sha_before}')
headings=['四 對外訓練服務執行能力鏈','五 訓練主管規劃與執行能力','七 評核題項與證據判讀續','八 加權計分與基準判定']
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
removed=[]
with ZipFile(src,'r') as zin, ZipFile(dst,'w',ZIP_DEFLATED) as zout:
    for info in zin.infolist():
        data=zin.read(info.filename)
        if info.filename=='word/document.xml':
            parser=etree.XMLParser(remove_blank_text=False)
            root=etree.fromstring(data,parser); body=root.find('w:body',ns)
            if body is None: raise SystemExit('document body missing')
            children=list(body)
            for heading in headings:
                found=[i for i,node in enumerate(children) if node.tag=='{%s}p'%ns['w'] and ''.join(node.xpath('.//w:t/text()',namespaces=ns)).strip()==heading]
                if len(found)!=1: raise SystemExit(f'heading count for {heading}: {len(found)}')
                idx=found[0]
                if idx==0: raise SystemExit('heading has no previous sibling')
                prev=children[idx-1]
                prev_text=''.join(prev.xpath('.//w:t/text()',namespaces=ns)).strip()
                pagebreaks=prev.xpath('.//w:br[@w:type="page"]',namespaces=ns) if prev.tag=='{%s}p'%ns['w'] else []
                if prev_text or len(pagebreaks)!=1: raise SystemExit(f'expected one empty hard-page-break paragraph before {heading}; got text={prev_text!r}, breaks={len(pagebreaks)}')
                body.remove(prev)
                removed.append({'heading':heading,'body_child_index_before':idx-1,'page_break_paragraph_removed':True})
                children=list(body)
            if removed and len(removed)!=4: raise SystemExit('unexpected removal count')
            after_text=''.join(root.xpath('.//w:t/text()',namespaces=ns))
            before_text=''.join(etree.fromstring(data,parser).xpath('.//w:t/text()',namespaces=ns))
            if before_text!=after_text: raise SystemExit('OOXML text nodes changed')
            data=etree.tostring(root,encoding='UTF-8',xml_declaration=True,standalone=True)
        zout.writestr(info,data)
new=dst.read_bytes(); new_sha=sha(new)
new_doc=Document(dst); body_after=body_text(new_doc); body_sha_after=sha(body_after.encode('utf-8')); table_sha_after=table_text(new_doc)
if body_sha_after!=body_sha_before or table_sha_after!=table_sha_before: raise SystemExit('body/table text changed')
with ZipFile(dst,'r') as z: bad=z.testzip(); changed_member_check=(z.read('word/document.xml')!=ZipFile(src,'r').read('word/document.xml'))
if bad is not None: raise SystemExit(f'bad zip member: {bad}')
receipt={'schema':'TTQS_ONE_0032_SCOPED_PAGEFLOW_REPAIR_R03','work_id':'TTQS_ONE_0032_I06-E03_SCOPED_PAGEFLOW_REPAIR_R03_20261118','doc_id':'0032','requirement_id':'I06-E03','created_at_tpe':datetime.now().astimezone().isoformat(timespec='seconds'),'repair_scope':'Removed four forced page-break-only paragraphs before sections 4, 5, 7 and 8 to prevent sparse continuation pages; no wording, tables, source facts, or sample data changed. Existing nine-run R02 font repair remains in the candidate.','input_candidate':str(candidate_dir/'0032_I06-E03_R01.docx'),'input_candidate_sha256':sha((candidate_dir/'0032_I06-E03_R01.docx').read_bytes()),'intermediate_candidate':str(src),'intermediate_candidate_sha256':old_sha,'output_candidate':str(dst),'output_candidate_sha256':new_sha,'removed_page_breaks':removed,'removed_page_break_count':len(removed),'content_text_nodes_identical':True,'body_text_sha256_before':body_sha_before,'body_text_sha256_after':body_sha_after,'body_text_identical':True,'table_text_sha256_before':table_sha_before,'table_text_sha256_after':table_sha_after,'table_text_identical':True,'zip_integrity':'PASS','candidate_status':'CANDIDATE_LAYOUT_REPAIR_UNREVIEWED'}
receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'candidate':str(dst),'candidate_sha256':new_sha,'bytes':len(new),'body_sha256':body_sha_after,'table_sha256':table_sha_after,'removed_page_breaks':removed,'changed_zip_member':'word/document.xml'},ensure_ascii=False))