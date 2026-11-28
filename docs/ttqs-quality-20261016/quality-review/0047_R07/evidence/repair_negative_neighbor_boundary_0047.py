from __future__ import annotations
import hashlib,json,shutil
from pathlib import Path
from docx import Document
from docx.oxml import OxmlElement
from docx.text.paragraph import Paragraph
from docx.shared import Pt

pkg=Path(__file__).resolve().parents[1]
parent=Path(__file__).resolve().parents[2]/'0047_R06'/'candidate'/'0047_R06.docx'
out=pkg/'candidate'/'0047_R07.docx'
if out.exists():
    if hashlib.sha256(out.read_bytes()).hexdigest().upper() != '7E0607B91AA2FEFE83A8064017909EB0ACA911771C6B25769E544FD96273E3A4': raise FileExistsError(f'Refusing to replace changed candidate: {out}')
    out.unlink()
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def body_tokens(doc,excluded_texts=()):
 result=[]
 for el in doc._body._body.iterchildren():
  if el.tag.endswith('}p'):
   txt=''.join(x.text or '' for x in el.iter() if x.tag.endswith('}t'))
   if txt in excluded_texts: continue
   result.append(('p',txt))
  elif el.tag.endswith('}tbl'):
   for row in el.iterchildren():
    if row.tag.endswith('}tr'):
     vals=[]
     for cell in row.iterchildren():
      if cell.tag.endswith('}tc'): vals.append(''.join(x.text or '' for x in cell.iter() if x.tag.endswith('}t')))
     result.append(('row',tuple(vals)))
 return result
if not parent.is_file(): raise FileNotFoundError(parent)
parent_sha=sha(parent)
shutil.copy2(parent,out)
doc=Document(out)
base_tokens=body_tokens(Document(parent))
heading_text='\u76f8\u90bb\u8981\u6c42\u908a\u754c\u8207\u8ca0\u5411\u8fd1\u9130\u62d2\u6536\u898f\u5247'
intro='\u672c\u4ef6\u5b9a\u4f4d\uff1a0047 / I10-E02\uff08\u5b98\u65b9\u4f86\u6e90\u683c P03-B09\uff09\u3002\u4ee5\u4e0b\u6839\u64da\u5404\u4ef6\u552f\u4e00 Blueprint \u7684\u8981\u6c42\u3001\u6587\u985e\u8207\u6b04\u4f4d\u8fa8\u8b58\u932f\u4ef6\uff1b\u6838\u5c0d\u9ede\u4e0d\u4ee3\u66ff\u8a72\u76f8\u9130\u6587\u4ef6\u672c\u8eab\u3002'
items=[
 ('0045 / I10-E01\uff5c\u300a\u8a13\u7df4\u8cc7\u6e90\u63a1\u8cfc\u8207\u7504\u9078\u7ba1\u7406\u8fa6\u6cd5\u300b',
  '\u5b98\u65b9\u5c08\u5c6c\u6587\u4ef6\u662f\u4e8b\u524d\u8207\u57f7\u884c\u7a0b\u5e8f\uff1a\u8ab2\u7a0b\u8a2d\u8a08\u6642\u5e2b\u8cc7\u3001\u6559\u6750\u6216\u5ee0\u5546\u7684\u8a55\u4f30\u9078\u64c7\uff0c\u4ee5\u53ca\u8a55\u4f30\u3001\u63a1\u8cfc\u3001\u7c3d\u7d04\u3001\u5f8c\u7e8c\u7ba1\u7406\u4f5c\u696d\u6d41\u7a0b\u3002\u53ef\u6838\u5c0d\u5b83\u7684\u5c08\u5c6c\u6b04\u4f4d\u662f\u555f\u52d5\u689d\u4ef6\u3001\u8f38\u5165\u4f86\u6e90\u3001\u89d2\u8272\u8207\u8986\u6838\u3001\u9580\u6abb\u5206\u652f\u3001\u63a7\u5236\u9ede\u3001\u7570\u5e38\u5347\u7d1a\u3001\u7d00\u9304\u7de8\u865f\u8207\u4ea4\u63a5\u3002\u672c\u4ef6 0047 \u4e0d\u5236\u5b9a\u6216\u53d6\u4ee3\u9019\u4e9b\u7a0b\u5e8f\uff1b\u672c\u5831\u544a\u53ea\u5206\u6790\u5e74\u5ea6\u8ab2\u7a0b\u6848\u4f8b\u7684\u9078\u524d\u898f\u6e96\u3001\u9078\u64c7\u7406\u7531\u3001\u5951\u7d04\u9a57\u6536\u3001\u5c65\u7d04\u6aa2\u6838\u5206\u5b50\u5206\u6bcd\u8207\u6539\u5584\u8ffd\u8e64\uff08\u6b63\u6587\u7b2c 5\u20136 \u9801\uff09\u3002\u82e5\u5f85\u8b49\u7684\u662f\u7a0b\u5e8f\u672c\u8eab\u6216\u5176\u6b0a\u8cac\u6838\u51c6\uff0c\u4e0d\u5f97\u4ee5 0047 \u4ee3\u66ff\u3002'),
 ('0048 / I10-E03\uff5c\u300a\u5927\u578b\u63a1\u8cfc\u5747\u8fa6\u7406\u6703\u8b70\u901a\u904e\u3001\u5e2b\u8cc7\u9074\u8058\u5f8c\u4ea6\u7d93\u904e\u6703\u8b70\u6216\u5be9\u67e5\u901a\u904e\u4e26\u7559\u6709\u7d00\u9304\u300b',
  '\u5b98\u65b9\u5c08\u5c6c\u4f50\u8b49\u662f\u5927\u578b\u63a1\u8cfc\u6216\u5e2b\u8cc7\u9074\u8058\u7d93\u6703\u8b70\uff0f\u5be9\u67e5\u901a\u904e\u4e26\u7559\u7d00\u9304\uff1b\u53ef\u6838\u5c0d\u7684\u6b04\u4f4d\u5305\u62ec\u65e5\u671f\u3001\u89d2\u8272\u4ee3\u78bc\u3001\u4f86\u6e90\uff0f\u9644\u4ef6\u5b9a\u4f4d\u3001\u5224\u5b9a\u8207\u7406\u7531\u3001\u8986\u6838\u53ca\u5f8c\u7e8c\u884c\u52d5\u3002\u672c\u4ef6 0047 \u7684\u7b2c 5\u20137 \u9801\u662f\u5e74\u5ea6\u5206\u6578\u3001\u5c65\u7d04\u9054\u6210\u7387\u3001\u5dee\u7570\u5206\u6790\u8207\u6539\u5584\u5efa\u8b70\uff0c\u4e0d\u662f\u6703\u8b70\u7d00\u9304\u3001\u5e2b\u8cc7\u9074\u8058\u6838\u51c6\u6216\u5927\u578b\u63a1\u8cfc\u901a\u904e\u4e4b\u539f\u4ef6\u3002\u82e5\u67d0\u500b\u6848\u7d50\u8ad6\u9700\u4ee5\u6703\u8b70\u6c7a\u8b70\u6216\u5be9\u67e5\u901a\u904e\u70ba\u4f9d\u64da\uff0c\u5fc5\u9808\u53e6\u53d6 0048 \u4e4b\u771f\u5be6\u539f\u4ef6\uff0c\u4e0d\u5f97\u5f9e\u672c\u5831\u544a\u7684\u5408\u6210\u6578\u64da\u63a8\u5b9a\u3002')
]
items[0]=(items[0][0]+' (official source box P03-B07)',items[0][1])
items[1]=(items[1][0]+' (official source box P03-B10)',items[1][1])
# Verify the neighbor texts against the live unique Blueprint rows supplied by the project source.
bp=Path(r'E:/TTQS/TTQS_ONE_CODEX_RUNTIME/CONTROL/BLUEPRINT_CURRENT.jsonl')
blue={}
for line in bp.read_text(encoding='utf-8').splitlines():
 try: x=json.loads(line)
 except Exception: continue
 if str(x.get('deliverable_id')) in {'0045','0048'}: blue[str(x['deliverable_id'])]=x
if set(blue)!={'0045','0048'}: raise AssertionError('neighbor Blueprint rows not both found')
if blue['0045'].get('requirement_id')!='I10-E01' or blue['0048'].get('requirement_id')!='I10-E03': raise AssertionError('neighbor requirement IDs mismatch')
if '師資' not in blue['0048'].get('official_requirement_text','') or '簽約' not in blue['0045'].get('official_requirement_text',''): raise AssertionError('neighbor official text incomplete')
# Insert immediately after the official scope section and before the next section.
paras=doc.paragraphs
scope_idx=next(i for i,p in enumerate(paras) if p.text.strip()=='\u5b98\u65b9\u8981\u6c42\u53ca\u5206\u6790\u7bc4\u570d')
next_idx=next(i for i in range(scope_idx+1,len(paras)) if paras[i].style.name.startswith('Heading'))
anchor=paras[next_idx-1]._p
h_el=OxmlElement('w:p'); anchor.addnext(h_el)
h=Paragraph(h_el,paras[next_idx-1]._parent); h.style=doc.styles['Heading 2']; h.add_run(heading_text)
h.paragraph_format.keep_with_next=True
h.paragraph_format.space_before=Pt(8); h.paragraph_format.space_after=Pt(3)
anchor=h._p
intro_el=OxmlElement('w:p'); anchor.addnext(intro_el)
intro_p=Paragraph(intro_el,h._parent); intro_p.style=doc.styles['Normal']; intro_p.add_run(intro)
intro_p.paragraph_format.keep_with_next=True; intro_p.paragraph_format.space_after=Pt(2)
for label,content in items:
 el=OxmlElement('w:p'); intro_p._p.addnext(el)
 p=Paragraph(el,intro_p._parent); p.style=doc.styles['List Bullet']
 p.paragraph_format.keep_together=True; p.paragraph_format.keep_with_next=False
 p.paragraph_format.space_after=Pt(3); p.paragraph_format.line_spacing=1.0
 r=p.add_run(label+'：'); r.bold=True; r.font.size=Pt(10.5)
 r2=p.add_run(content); r2.font.size=Pt(10.5)
 intro_p=p

doc.core_properties.comments='R07: targeted substantive addition distinguishing official negative neighbors 0045/I10-E01 and 0048/I10-E03; names their distinct evidence fields and states rejection boundaries. No synthetic calculations or existing case values changed.'
doc.save(out)
check=Document(out)
added=[heading_text,intro]+[label+'：'+content for label,content in items]
new_tokens=body_tokens(check,excluded_texts=tuple(added))
if base_tokens!=new_tokens: raise AssertionError('Existing R06 body/table content changed outside the added boundary section')
text='\n'.join(p.text for p in check.paragraphs)
for phrase in ['0045 / I10-E01','0048 / I10-E03','P03-B07','P03-B09','P03-B10']:
 if phrase not in text: raise AssertionError(f'missing explicit mapping token: {phrase}')
if any(run.font.size is not None and run.font.size.pt<10.5 for p in check.paragraphs for run in p.runs if run.text.strip() and p.text in added): raise AssertionError('added body text below 10.5 pt')
receipt={
 'doc_id':'0047','revision':'R07','status':'CANDIDATE_ONLY','parent_revision':'R06','parent_sha256':parent_sha,
 'candidate':'0047_R07/candidate/0047_R07.docx','candidate_sha256':sha(out),
 'change_scope':'TARGETED_SUBSTANTIVE_NEGATIVE_NEIGHBOR_BOUNDARY_SECTION',
 'official_mapping':{'doc_id':'0047','requirement_id':'I10-E02','checkbox_sequence':48,'source_box':'P03-B09'},
 'neighbor_source_rows':{'0045':{'requirement_id':blue['0045']['requirement_id'],'source_box':'P03-B07','other_category':True,'official_text':blue['0045']['official_requirement_text']},'0048':{'requirement_id':blue['0048']['requirement_id'],'source_box':'P03-B10','official_text':blue['0048']['official_requirement_text']}},
 'new_section':heading_text,'body_change':True,'existing_text_and_table_values_unchanged':True,
 'purpose':'Respond to the independent R06 PARTIAL finding by naming both negative neighbors and giving their distinct, checkable evidence fields and rejection boundaries.',
 'calculation_values_changed':False,'sample_real_status':'All numeric cases remain SAMPLE/SYNTHETIC; no real meeting, purchase, approval, or association decision claimed.',
 'semantic_review':'PENDING exact R07 SHA','visual_review':'PENDING full-page render.'
}
(pkg/'evidence'/'R07_NEIGHBOR_BOUNDARY_REPAIR_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=True,indent=2))
