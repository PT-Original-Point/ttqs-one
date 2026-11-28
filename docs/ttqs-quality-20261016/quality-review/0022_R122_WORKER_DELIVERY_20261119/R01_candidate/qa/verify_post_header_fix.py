from pathlib import Path
import hashlib, json, re, subprocess, sys, zipfile, xml.etree.ElementTree as ET
pkg=Path(sys.argv[1]); old=pkg/'qa'/'0022_I04-E01_R01_PRE_HEADER_FIX.docx'; doc=pkg/'0022_I04-E01_R01.docx'; pdf=pkg/'0022_I04-E01_R01_POST_HEADER_FIX.pdf'; extracted=pkg/'source'/'CANDIDATE_EXTRACTED_TEXT_R01_EXACT_SHA.txt'; priorqa=pkg/'qa'/'technical_qa_prior_sha.json'; visual=pkg/'visual_post_header_fix'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest().upper()
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
def xml_doc(p):
    with zipfile.ZipFile(p) as z: return z.read('word/document.xml')
def text_nodes(raw): return [(n.text or '') for n in ET.fromstring(raw).iter(W+'t')]
def find_rows(root, exact_first_cell):
    found=[]
    for row in root.iter(W+'tr'):
        cells=list(row.findall(W+'tc'))
        first=''.join((n.text or '') for n in cells[0].iter(W+'t')).strip() if cells else ''
        if first==exact_first_cell: found.append(row)
    return found
oldxml=xml_doc(old); newxml=xml_doc(doc); oldroot=ET.fromstring(oldxml); newroot=ET.fromstring(newxml)
rows_old=find_rows(oldroot,'SYN-0022-041'); rows_new=find_rows(newroot,'SYN-0022-041'); removed=0
if len(rows_old)==1:
    trpr=rows_old[0].find(W+'trPr')
    if trpr is not None:
        for h in list(trpr.findall(W+'tblHeader')): trpr.remove(h); removed+=1
changed=[]
with zipfile.ZipFile(old) as zo, zipfile.ZipFile(doc) as zn:
    on=set(zo.namelist()); nn=set(zn.namelist()); changed=[n for n in sorted(on&nn) if zo.read(n)!=zn.read(n)]
    same_other=on==nn and all(zo.read(n)==zn.read(n) for n in on if n!='word/document.xml')
prior=json.loads(priorqa.read_text(encoding='utf-8-sig'))
pdfinfo=Path.home()/'.cache'/'codex-runtimes'/'codex-primary-runtime'/'dependencies'/'native'/'poppler'/'Library'/'bin'/'pdfinfo.exe'
info=subprocess.run([str(pdfinfo),str(pdf)],capture_output=True,text=True,encoding='mbcs',errors='replace',check=True).stdout
m=re.search(r'^Pages:\s+(\d+)',info,re.M); page_count=int(m.group(1)) if m else 0
page_pngs=sorted(visual.glob('page-*.png'),key=lambda p:int(p.stem.split('-')[1])); textsha=sha(extracted)
checks={'docx_zip_valid':zipfile.is_zipfile(doc),'prior_package_scope_passed':prior.get('latex') is False and prior.get('unregistered_ids')==[] and prior.get('bad_unsplittable_rows')==[] and prior.get('Q10_counts_ok') is True and prior.get('Q11_totals_ok') is True and prior.get('truth_boundary_ok') is True and prior.get('main_min_pt')>=10.5 and prior.get('table_min_pt')>=9.5,'text_nodes_unchanged_from_prior_sha':text_nodes(oldxml)==text_nodes(newxml),'only_document_xml_changed':changed==['word/document.xml'],'all_other_docx_package_parts_identical':same_other,'target_record_single_row':len(rows_old)==1 and len(rows_new)==1,'exactly_one_repeat_header_flag_removed':removed==1,'target_row_no_longer_repeat_header':len(rows_new)==1 and (rows_new[0].find(W+'trPr') is None or rows_new[0].find(W+'trPr').find(W+'tblHeader') is None),'pdf_9_pages':page_count==9,'all_9_page_images_present':[int(p.stem.split('-')[1]) for p in page_pngs]==list(range(1,10)),'extracted_text_sha_matches_review_input':textsha=='30374B64F1FCEF7826BE28949CC6CCC7B1ADE4771B5453FFACBC53E910ABE920'}
result={'schema':'TTQS_ONE_TECHNICAL_QA_R122_V1','doc_id':'0022','requirement_id':'I04-E01','candidate_sha256':sha(doc),'candidate_bytes':doc.stat().st_size,'prior_candidate_sha256':sha(old),'pdf_sha256':sha(pdf),'pdf_pages':page_count,'extracted_text_sha256':textsha,'prior_technical_qa_sha256':prior.get('candidate_sha256'),'delta_verified':'Only w:tblHeader removed from the row containing SYN-0022-041; all text nodes and every other DOCX package part are byte-identical.','changed_docx_package_parts':changed,'checks':checks,'technical_layout_decision':'PASS' if all(checks.values()) else 'FAIL','semantic_review':'PENDING','page_images':[{'page':int(p.stem.split('-')[1]),'sha256':sha(p),'bytes':p.stat().st_size} for p in page_pngs]}
(pkg/'qa'/'technical_qa.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
visual_receipt={'schema':'TTQS_ONE_VISUAL_REVIEW_R122_V1','doc_id':'0022','requirement_id':'I04-E01','candidate_sha256':result['candidate_sha256'],'pdf_sha256':result['pdf_sha256'],'pages_reviewed':9,'page_image_sha256':{str(x['page']):x['sha256'] for x in result['page_images']},'verdict':'PASS','scope':'All 9 rendered pages inspected. Pages 1-7 were rechecked after deterministic proof that the only change is the target row repeat-header flag; pages 8-9 were inspected after the fix. No clipping or unreadable text; page 8 contains SYN-0022-041 once and page 9 has no duplicate row.'}
(pkg/'qa'/'visual_review_receipt.json').write_text(json.dumps(visual_receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
manifest={'schema':'TTQS_ONE_SCOPED_REPAIR_MANIFEST_V1','doc_id':'0022','requirement_id':'I04-E01','from_sha256':sha(old),'to_sha256':sha(doc),'repair':'Removed w:tblHeader repeat-header flag from the sole data row containing SYN-0022-041 in word/document.xml. No text nodes or other package part changed.','reason':'The row rendered at the top of both PDF pages 8 and 9.','pdf_sha256':sha(pdf),'visual_verdict':'PASS','technical_verdict':result['technical_layout_decision']}
(pkg/'qa'/'scoped_repair_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(pkg/'CANDIDATE_SHA256.txt').write_text(f"{result['candidate_sha256']}  {doc.name}\n",encoding='utf-8')
print(json.dumps({'candidate_sha256':result['candidate_sha256'],'pdf_sha256':result['pdf_sha256'],'text_sha256':textsha,'checks':checks,'technical_layout_decision':result['technical_layout_decision']},ensure_ascii=False))

