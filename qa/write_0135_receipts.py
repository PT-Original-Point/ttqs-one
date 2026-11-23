from pathlib import Path
from hashlib import sha256
from zipfile import ZipFile
from lxml import etree
from docx import Document
from datetime import datetime
import json,sys
root=Path(sys.argv[1]); cand=root/'candidate'; qa=root/'qa'; worker=root/'worker'; render=root/'render'
def H(p): return sha256(p.read_bytes()).hexdigest()
def put(p,obj): p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
docx=next(cand.glob('0135__*.docx')); pdf=render/'word_native_final'/'0135_R01_WordNative.pdf'; pages=sorted((render/'pages_R01_final').glob('page-*.png'))
tech=json.loads((qa/'TECHNICAL_QA_0135_R01.json').read_text(encoding='utf-8-sig'))
assert tech['checks']['docx_sha256']==H(docx), 'technical QA does not bind final DOCX'
assert tech['checks']['docx_bytes']==docx.stat().st_size
assert len(pages)==10
with ZipFile(docx) as z:
    styles=etree.fromstring(z.read('word/styles.xml'))
    w='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    title=next(s for s in styles if s.get(w+'styleId')=='Title')
    style_ppr=title.find(w+'pPr')
    assert style_ppr is None or style_ppr.find(w+'pBdr') is None, 'Title style paragraph border remains'
    document=etree.fromstring(z.read('word/document.xml'))
    title_paras=document.xpath('.//w:p[w:pPr/w:pStyle[@w:val="Title"]]',namespaces={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'})
    assert title_paras, 'no title paragraph'
    direct=title_paras[0].find(w+'pPr')
    assert direct is None or direct.find(w+'pBdr') is None, 'direct title paragraph border remains'
vis={
 'project_id':'TTQS_ONE','doc_id':'0135','requirement_id':'I19-E25','project_157_item':140,
 'candidate_state':'CANDIDATE','docx_path':'candidate/'+docx.name,'docx_sha256':H(docx),'docx_bytes':docx.stat().st_size,
 'render_method':'Microsoft Word native ExportAsFixedFormat to PDF; Poppler rendered each exported page at 144 DPI',
 'pdf_sha256':H(pdf),'pdf_bytes':pdf.stat().st_size,'page_count':10,'pages_inspected':10,
 'page_images':[{'file':p.name,'sha256':H(p),'bytes':p.stat().st_size} for p in pages],
 'observed_checks':{'title_blue_rule_absent':True,'no_clipping_or_overflow_visible':True,'tables_readable_and_repeating_headers_visible':True,'headers_footers_page_numbers_readable':True,'large_whitespace_page_10':'observed; content remains readable; no clipping or blank page'},
 'visual_result':'PASS_WITH_SCOPE','scope':'Visual layout only, 10/10 pages inspected from latest Word-native PDF render. This does not establish semantic acceptance, REAL evidence, or formal acceptance.',
 'inspected_at_local':datetime.now().astimezone().isoformat(timespec='seconds')
}
put(qa/'VISUAL_QA_0135_R01.json',vis)
manifest={
 'project_id':'TTQS_ONE','doc_id':'0135','official_requirement_id':'I19-E25','project_157_item':140,'official_printed_checkbox_serial':'UNKNOWN',
 'blueprint':'source/UNIQUE_BLUEPRINT_0135_I19-E25_R01.md','source_commit':'8ff5f8cbe6df80be9ed60577ed324e5a0a18f382',
 'candidate_state':'CANDIDATE','formal_acceptance':'NOT_GRANTED','real_evidence':'UNKNOWN_UNTIL_SOURCE',
 'artifacts':{
   'docx':{'path':'candidate/'+docx.name,'sha256':H(docx),'bytes':docx.stat().st_size},
   'body_markdown':{'path':'candidate/0135_I19-E25_BODY_R01.md','sha256':H(cand/'0135_I19-E25_BODY_R01.md')},
   'replacement_register':{'path':'candidate/0135_SYNTHETIC_REPLACEMENT_REGISTER_R01.csv','sha256':H(cand/'0135_SYNTHETIC_REPLACEMENT_REGISTER_R01.csv')},
   'word_native_pdf':{'path':'render/word_native_final/0135_R01_WordNative.pdf','sha256':H(pdf),'bytes':pdf.stat().st_size},
   'technical_qa':{'path':'qa/TECHNICAL_QA_0135_R01.json','sha256':H(qa/'TECHNICAL_QA_0135_R01.json'),'status':tech['qa_status']},
   'visual_qa':{'path':'qa/VISUAL_QA_0135_R01.json','sha256':H(qa/'VISUAL_QA_0135_R01.json'),'status':'PASS_WITH_SCOPE'},
   'independent_semantic_review':{'status':'PENDING','exact_sha_required':H(docx),'result':'No usable independent review returned; one explicit OpenCode free-model attempt hit provider 429.'}
 },
 'source_data_boundary':'All outcome figures and case rows are SAMPLE/SYNTHETIC. Association REAL originals and formal checkbox serial remain UNKNOWN.',
 'builder':'Codex authored the replacement candidate after external Worker results were rejected or unavailable; do not attribute this candidate to Antigravity/OpenCode.',
 'created_at_local':datetime.now().astimezone().isoformat(timespec='seconds')
}
put(qa/'CANDIDATE_MANIFEST_0135_R01.json',manifest)
raw=worker/'OPENCODE_0135_SEMANTIC_REVIEW_R01_RAW.jsonl'
recon={
 'project_id':'TTQS_ONE','doc_id':'0135','work_id':'TTQS_ONE_0135_I19-E25_SEMANTIC_REVIEW_R01','worker':'OpenCode v2 CLI','cli_version':'2.1.4',
 'requested_model':'opencode/deepseek-v4.1-flash-free','model_catalog_observation':'listed by local `opencode models` immediately before dispatch; catalog listing is not proof of successful inference',
 'fallback_allowed':False,'computer_use':False,'tools_auto_approved':False,'input_packet_sha256':H(worker/'REVIEW_PACKET_0135_R01_EXACT_SHA.md'),
 'candidate_docx_sha256':H(docx),'pid':40988,'exit_code':1,'elapsed_seconds':1.2,'status':'FAILED_PROVIDER_FREE_LIMIT_429_NO_REVIEW',
 'raw_response_path':'worker/OPENCODE_0135_SEMANTIC_REVIEW_R01_RAW.jsonl','raw_response_sha256':H(raw),'raw_response_bytes':raw.stat().st_size,
 'error':'provider.free-limit / FreeUsageLimitError, HTTP 429; retryAfterMs=27461000',
 'adopted_content':False,'independent_verdict':'NONE','next_action':'Do not retry while free quota is exhausted; leave exact-SHA semantic review pending and continue other lawful READY lanes.'
}
put(worker/'OPENCODE_0135_SEMANTIC_REVIEW_R01_RECONCILIATION.json',recon)
print('DOCX',H(docx),docx.stat().st_size)
print('PDF',H(pdf),pdf.stat().st_size)
print('VISUAL_QA',H(qa/'VISUAL_QA_0135_R01.json'))
print('CANDIDATE_MANIFEST',H(qa/'CANDIDATE_MANIFEST_0135_R01.json'))
print('OPENCODE_RECON',H(worker/'OPENCODE_0135_SEMANTIC_REVIEW_R01_RECONCILIATION.json'))
print('PAGES',len(pages),'TECH_QA',tech['qa_status'])
