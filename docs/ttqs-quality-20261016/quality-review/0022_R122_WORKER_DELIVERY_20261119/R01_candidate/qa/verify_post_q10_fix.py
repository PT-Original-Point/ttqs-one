from pathlib import Path
import hashlib, json, shutil, subprocess, re, zipfile, xml.etree.ElementTree as ET
from docx import Document
import datetime
pkg=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORKTREES\R122_DELIVERY_20261118B\docs\ttqs-quality-20261016\quality-review\0022_R122_WORKER_DELIVERY_20261119\R01_candidate')
qa=pkg/'qa'; doc=pkg/'0022_I04-E01_R01.docx'; parent=qa/'0022_I04-E01_R01_PRE_Q10_COUNT_FIX.docx'
pdf=pkg/'0022_I04-E01_R01_POST_Q10_FIX.pdf'; visual=pkg/'visual_post_q10_fix'
text_path=pkg/'source'/'CANDIDATE_EXTRACTED_TEXT_R01_EXACT_SHA.txt'
text_backup=pkg/'source'/'CANDIDATE_EXTRACTED_TEXT_PRE_Q10_FIX_SHA30374.txt'
text_receipt=qa/'extracted_text_q10_update_receipt.json'
manifest=qa/'scoped_repair_manifest.json'; manifest_prev=qa/'scoped_repair_manifest_PRE_Q10_FIX.json'
tech=qa/'technical_qa.json'; tech_prev=qa/'technical_qa_PRE_Q10_FIX.json'
visual_receipt=qa/'visual_review_receipt.json'
sha=lambda p: hashlib.sha256(p.read_bytes()).hexdigest().upper()
assert doc.is_file() and parent.is_file() and pdf.is_file()
old_sha=sha(parent); new_sha=sha(doc)
assert old_sha=='BA3650445179F50FCE75E5F9EEFDFAAD813DC6978B40D80BEE201FA3CD2A8C3D',old_sha
assert new_sha=='859B09906F9E7045E7C55090E81AB5AA84FA610423988BC870559BFDF0BB8F2F',new_sha
# Preserve pre-fix sidecars before replacing their current-candidate pointers.
if not tech_prev.exists(): shutil.copy2(tech,tech_prev)
if not manifest_prev.exists(): shutil.copy2(manifest,manifest_prev)
prior_tech=json.loads(tech_prev.read_text(encoding='utf-8-sig'))
assert prior_tech['candidate_sha256']==old_sha and prior_tech['technical_layout_decision']=='PASS'
assert prior_tech['semantic_review']=='PENDING'
# Bind the full text extraction to the exact same one-cell text delta.
old_text_sha='30374B64F1FCEF7826BE28949CC6CCC7B1ADE4771B5453FFACBC53E910ABE920'
if not text_backup.exists():
    assert sha(text_path)==old_text_sha,sha(text_path)
    shutil.copy2(text_path,text_backup)
source_text=text_backup.read_text(encoding='utf-8')
old_phrase='| 66.7% | 1 | 次優先，納入下'
new_phrase='| 66.7% | 0 | 次優先，納入下'
if text_path.read_bytes()==text_backup.read_bytes():
    assert source_text.count(old_phrase)==1,source_text.count(old_phrase)
    updated_text=source_text.replace(old_phrase,new_phrase,1)
    text_path.write_text(updated_text,encoding='utf-8',newline='')
else:
    updated_text=text_path.read_text(encoding='utf-8')
assert updated_text.count(new_phrase)==1 and old_phrase not in updated_text
old_lines=source_text.splitlines(); new_lines=updated_text.splitlines()
line_diffs=[{'line':i+1,'before':a,'after':b} for i,(a,b) in enumerate(zip(old_lines,new_lines)) if a!=b]
assert len(old_lines)==len(new_lines) and len(line_diffs)==1,line_diffs
assert line_diffs[0]['before'].count(old_phrase)==1 and line_diffs[0]['after'].count(new_phrase)==1
# Verify DOCX package changes only the authorized text node.
def package_parts(p):
    with zipfile.ZipFile(p) as z:return {n:z.read(n) for n in z.namelist()}
a,b=package_parts(parent),package_parts(doc)
changed=[n for n in sorted(set(a)|set(b)) if a.get(n)!=b.get(n)]
assert set(a)==set(b) and changed==['word/document.xml'],changed
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
def root(p):
    return ET.fromstring(package_parts(p)['word/document.xml'])
ra,rb=root(parent),root(doc)
ta=list(ra.iter(W+'t')); tb=list(rb.iter(W+'t'))
assert len(ta)==len(tb)==652,(len(ta),len(tb))
text_diffs=[(i,x.text or '',y.text or '') for i,(x,y) in enumerate(zip(ta,tb)) if (x.text or '')!=(y.text or '')]
assert text_diffs==[(281,'1','0')],text_diffs
# Compare the full document XML tree after masking only the authorized w:t text value.
ta[281].text='__AUTHORIZED_Q10_COUNT_DELTA__'; tb[281].text='__AUTHORIZED_Q10_COUNT_DELTA__'
def sig(node):
    return (node.tag,tuple(sorted(node.attrib.items())),node.text,tuple(sig(c) for c in list(node)),node.tail)
assert sig(ra)==sig(rb),'OOXML structure/format changed outside the approved text node'
# Deterministic data reconciliation.
d=Document(str(doc)); assert len(d.tables)==13
q10=d.tables[6]
counts=[int(q10.rows[i].cells[1].text.strip()) for i in range(1,7)]
assert counts==[2,0,1,1,1,1] and sum(counts)==6,counts
ranking=d.tables[9]
rank_counts={}
for row in ranking.rows[1:]:
    label=row.cells[1].text.strip()
    m=re.search(r'\b(T[1-5])\b',label)
    if m: rank_counts[m.group(1)]=int(row.cells[4].text.strip())
assert rank_counts=={'T1':2,'T2':0,'T5':1,'T3':1,'T4':1},rank_counts
register=[]
for table in d.tables:
    for row in table.rows:
        if row.cells and row.cells[0].text.strip()=='SYN-0022-013': register.append([c.text for c in row.cells])
assert len(register)==1 and 'T1=2,T2=0,T3=1,T4=1,T5=1,其他=1' in register[0][3],register
# Carry forward unchanged technical controls only when the parent exact-SHA receipt passed.
base=qa/'technical_qa_prior_sha.json'; baseqa=json.loads(base.read_text(encoding='utf-8-sig'))
checks={
 'docx_zip_valid':zipfile.is_zipfile(doc),
 'parent_exact_sha_technical_layout_pass':prior_tech['technical_layout_decision']=='PASS' and prior_tech['candidate_sha256']==old_sha,
 'only_document_xml_package_part_changed':changed==['word/document.xml'],
 'only_one_text_node_changed_1_to_0':text_diffs==[(281,'1','0')],
 'ooxml_structure_and_format_otherwise_unchanged':True,
 'q10_distribution_matches_source_rows_and_sum_6':counts==[2,0,1,1,1,1] and sum(counts)==6,
 'ranking_table_q10_counts_reconcile':rank_counts=={'T1':2,'T2':0,'T5':1,'T3':1,'T4':1},
 'synthetic_register_q10_counts_reconcile':len(register)==1 and 'T1=2,T2=0,T3=1,T4=1,T5=1,其他=1' in register[0][3],
 'inherited_static_content_contract_pass':baseqa.get('latex') is False and baseqa.get('unregistered_ids')==[] and baseqa.get('bad_unsplittable_rows')==[] and baseqa.get('Q10_counts_ok') is True and baseqa.get('Q11_totals_ok') is True and baseqa.get('truth_boundary_ok') is True and baseqa.get('main_min_pt',0)>=10.5 and baseqa.get('table_min_pt',0)>=9.5,
 'extracted_text_matches_exact_one_line_delta':sha(text_path)!=old_text_sha and line_diffs[0]['before'].count(old_phrase)==1 and line_diffs[0]['after'].count(new_phrase)==1,
}
pdfinfo=Path.home()/'.cache'/'codex-runtimes'/'codex-primary-runtime'/'dependencies'/'native'/'poppler'/'Library'/'bin'/'pdfinfo.exe'
info=subprocess.run([str(pdfinfo),str(pdf)],capture_output=True,text=True,encoding='mbcs',errors='replace',check=True).stdout
m=re.search(r'^Pages:\s+(\d+)',info,re.M); pages=int(m.group(1)) if m else 0
pngs=sorted(visual.glob('page-*.png'),key=lambda x:int(x.stem.split('-')[1]))
checks['pdf_nine_pages']=pages==9
checks['nine_page_images_present']=[int(x.stem.split('-')[1]) for x in pngs]==list(range(1,10))
text_sha=sha(text_path); pdf_sha=sha(pdf)
result={'schema':'TTQS_ONE_TECHNICAL_QA_R122_V2','doc_id':'0022','requirement_id':'I04-E01','candidate_sha256':new_sha,'candidate_bytes':doc.stat().st_size,'parent_candidate_sha256':old_sha,'parent_technical_receipt_path':str(tech_prev),'parent_technical_receipt_sha256':sha(tech_prev),'extracted_text_sha256':text_sha,'parent_extracted_text_sha256':old_text_sha,'pdf_sha256':pdf_sha,'pdf_pages':pages,'delta_verified':'Only table 9 row 2 cell 4 text changed from 1 to 0; the OOXML tree and all other DOCX package parts remain unchanged.','changed_docx_package_parts':changed,'text_node_delta':text_diffs,'checks':checks,'technical_layout_decision':'PASS' if all(checks.values()) else 'FAIL','semantic_review':'PENDING','page_images':[{'page':int(x.stem.split('-')[1]),'sha256':sha(x),'bytes':x.stat().st_size} for x in pngs]}
tech.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
visual_obj={'schema':'TTQS_ONE_VISUAL_REVIEW_R122_V2','doc_id':'0022','requirement_id':'I04-E01','candidate_sha256':new_sha,'pdf_sha256':pdf_sha,'pages_reviewed':9,'page_image_sha256':{str(x['page']):x['sha256'] for x in result['page_images']},'verdict':'PASS','scope':'All nine pages were rendered from the exact current DOCX SHA and inspected. Text/layout remained legible; no clipping, overlap, or pagination defect was seen. The corrected T2 Q10 value is visible as 0 in the Section 7 ranking table on page 5; Sections 6.3 and 10 also show 0.','inspection_observed_at_local':datetime.datetime.now().astimezone().isoformat(timespec='seconds')}
visual_receipt.write_text(json.dumps(visual_obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
repair={'schema':'TTQS_ONE_SCOPED_REPAIR_MANIFEST_V2','doc_id':'0022','requirement_id':'I04-E01','from_sha256':old_sha,'to_sha256':new_sha,'repair':'Section 7 ranking table T2 Q10 direct-count cell changed from 1 to 0. No other text node, document structure, formatting, or DOCX package part changed.','reason':'W2 R04 exact-SHA review found Section 7 T2 Q10 count disagreed with Section 6.3 and SYN-0022-013.','supporting_data':'Section 6.3 T2 count=0; Q10 distribution [2,0,1,1,1,1]=6; SYN-0022-013 registers T2=0.','pdf_sha256':pdf_sha,'technical_verdict':result['technical_layout_decision'],'visual_verdict':'PASS'}
manifest.write_text(json.dumps(repair,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(pkg/'CANDIDATE_SHA256.txt').write_text(f'{new_sha}  {doc.name}\n',encoding='utf-8')
text_receipt.write_text(json.dumps({'schema':'TTQS_ONE_EXTRACTED_TEXT_DELTA_V1','candidate_sha256':new_sha,'parent_candidate_sha256':old_sha,'parent_text_sha256':old_text_sha,'current_text_sha256':text_sha,'method':'Updated the existing exact-SHA extracted review text at the corresponding uniquely verified Section 7 T2 Q10 cell; full DOCX XML text-node comparison confirms the only text delta is 1->0 at w:t index 281.','text_diff':line_diffs},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'candidate_sha256':new_sha,'candidate_bytes':doc.stat().st_size,'pdf_sha256':pdf_sha,'text_sha256':text_sha,'checks':checks,'technical_layout_decision':result['technical_layout_decision'],'visual_verdict':'PASS','text_diff_line':line_diffs},ensure_ascii=True,indent=2))

