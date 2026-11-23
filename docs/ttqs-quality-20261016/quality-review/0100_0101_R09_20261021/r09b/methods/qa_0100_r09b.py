from pathlib import Path
from datetime import datetime
import hashlib, json, re, zipfile, xml.etree.ElementTree as ET, csv
from docx import Document
import pypdfium2

ROOT = Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0100_0101_R08_SOURCE_BLUEPRINT_20261021')
CAND = ROOT / 'candidate_R09b'
DOCX = CAND / '0100_I18-E08_R09b.docx'
PDF = CAND / '0100_I18-E08_R09b_LAYOUT2_WORD_NATIVE.pdf'
PNG_DIR = CAND / 'rendered' / 'layout2'
PACKET = ROOT / 'SOURCE_PACKET_I18-E08_0100_0101_R09.md'
BLUEPRINT = ROOT / 'UNIQUE_BLUEPRINT_0100_I18-E08_R09.md'
OFFICIAL = Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\INPUTS\R04\06_OFFICIAL_SOURCES\TTQS查核佐證文件資料表-訓練機構版 (2).pdf')
REGISTER = ROOT / 'candidate_R09' / 'synthetic_replacement_register_0100_R09.csv'
EXPECTED_DOCX = '0262d68826181a4b5f6209c3422a2d5c61a0b9820790c4e43a2e483b94de884c'
EXPECTED_REGISTER = '889c202a6e49435d9100e3bf906883410b4ae7160166126f24d9af27c876dbd8'

def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024), b''): h.update(b)
    return h.hexdigest()
def require(condition, detail):
    if not condition: raise AssertionError(detail)
def cell(t, r, c): return t.rows[r].cells[c].text.strip()

for p in [DOCX, PDF, PACKET, BLUEPRINT, OFFICIAL, REGISTER]: require(p.is_file(), f'MISSING {p}')
doc_sha=sha(DOCX); require(doc_sha==EXPECTED_DOCX, f'DOCX SHA changed: {doc_sha}')
reg_sha=sha(REGISTER); require(reg_sha==EXPECTED_REGISTER, f'register SHA changed: {reg_sha}')
with zipfile.ZipFile(DOCX) as z:
    require(z.testzip() is None, 'DOCX ZIP integrity failure')
    xml=ET.fromstring(z.read('word/document.xml'))
    w={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    require(xml.find('.//w:body',w) is not None,'missing Word body XML')

doc=Document(str(DOCX))
require(len(doc.tables)==17, f'unexpected table count {len(doc.tables)}')
text='\n'.join(p.text for p in doc.paragraphs)+'\n'+'\n'.join(c.text for t in doc.tables for row in t.rows for c in row.cells)
flat=' '.join(text.split())
checks={
    'document_id_and_requirement': '0100' in flat and 'I18-E08' in flat,
    'internal_index_not_misrepresented': 'UNKNOWN' in flat,
    'revision_r09b': 'R09b' in flat,
    'sample_synthetic_boundary': 'SAMPLE' in flat and 'SYNTHETIC' in flat,
    'formal_acceptance_not_granted': 'NOT_GRANTED' in flat,
    'no_real_learner_response': '無真實學員填答' in flat,
    'four_digit_wording': '四位數字' in flat and '4 碼' not in flat,
    'employer_privacy_term': '雇主' in flat,
    'client_privacy_term': '客戶' in flat,
    'service_recipient_privacy_term': '服務對象' in flat,
    'no_zero_or_mean_imputation': '不得以 0 代入' in flat and '不得以平均數' in flat,
}
for name, ok in checks.items(): require(ok, f'failed content check: {name}')

pairrow=doc.tables[11].rows[5]
pair=' | '.join(c.text.strip() for c in pairrow.cells)
for phrase in ['HOLD','同一人','同版本','日期順序','REJECT','有效分母','不得只因代碼相同']:
    require(phrase in pair, f'pairing rule missing {phrase}: {pair}')

# Reconcile each A01-A08 pair against the authoritative R09 source packet.
packet=PACKET.read_text(encoding='utf-8')
source_rows={}
for line in packet.splitlines():
    m=re.fullmatch(r'\|(A0[1-8])\|([0-4](?:/[0-4]){4})\|(\d+)\|([0-4](?:/[0-4]){4})\|(\d+)\|\+?(\d+)\|', line.strip())
    if m:
        code, pre_s, pre_total, post_s, post_total, delta=m.groups()
        source_rows[code]={'pre':[int(x) for x in pre_s.split('/')], 'pre_total':int(pre_total), 'post':[int(x) for x in post_s.split('/')], 'post_total':int(post_total), 'delta':int(delta)}
require(list(source_rows)==[f'A{i:02d}' for i in range(1,9)], f'source packet rows {list(source_rows)}')
score_table=doc.tables[12]
require(len(score_table.rows)==9 and len(score_table.columns)==14, 'score matrix shape mismatch')
observed=[]
for row in score_table.rows[1:]:
    vals=[c.text.strip() for c in row.cells]
    code=vals[0]
    actual={'pre':[int(x) for x in vals[1:6]], 'pre_total':int(vals[6]), 'post':[int(x) for x in vals[7:12]], 'post_total':int(vals[12]), 'delta':int(vals[13].replace('+',''))}
    require(code in source_rows and actual==source_rows[code], f'score row differs from source packet: {code} {actual}')
    require(len(actual['pre'])+len(actual['post'])==10 and all(0<=x<=4 for x in actual['pre']+actual['post']), f'invalid score range: {code}')
    require(sum(actual['pre'])==actual['pre_total'], f'pre total mismatch: {code}')
    require(sum(actual['post'])==actual['post_total'], f'post total mismatch: {code}')
    require(actual['post_total']-actual['pre_total']==actual['delta'], f'delta mismatch: {code}')
    observed.append({'code':code,**actual})
pre_sum=sum(sum(x['pre']) for x in observed); post_sum=sum(sum(x['post']) for x in observed)
require(pre_sum==75 and post_sum==117 and post_sum-pre_sum==42, f'aggregate totals {pre_sum}/{post_sum}')
require(pre_sum/8==9.375 and post_sum/8==14.625 and (post_sum-pre_sum)/8==5.25, 'mean calculations')
# Verify dimension summary table against the raw 8x5 matrix.
dim_table=doc.tables[14]
expected_dims=[('A',17,25,1.0),('B',16,24,1.0),('C',13,22,1.125),('D',14,24,1.25),('E',15,22,0.875)]
require(len(dim_table.rows)==6, 'dimension summary shape')
for i,(letter, pre, post, delta) in enumerate(expected_dims, start=1):
    row=dim_table.rows[i]
    require(row.cells[0].text.strip().startswith(letter+' '), f'dimension order {i}')
    require(int(row.cells[1].text)==pre and int(row.cells[3].text)==post, f'dimension sums {letter}')
    require(abs(float(row.cells[5].text.replace('+',''))-delta)<0.00051, f'dimension mean delta {letter}')

with REGISTER.open(encoding='utf-8-sig',newline='') as f: register=list(csv.DictReader(f))
require(len(register)==145, f'register row count {len(register)}')
require(all(r.get('evidence_class')=='SAMPLE/SYNTHETIC' for r in register), 'non-synthetic register row found')
register_text=' '.join(c.text for row in doc.tables[16].rows for c in row.cells)
require(reg_sha in register_text, 'DOCX does not bind exact replacement register SHA')

# Native Word PDF export and exact render inventory.
pdf=pypdfium2.PdfDocument(str(PDF)); page_count=len(pdf)
require(page_count==16, f'Word PDF page count {page_count}')
pngs=sorted(PNG_DIR.glob('page-*.png'), key=lambda p:int(re.search(r'(\d+)',p.stem).group(1)))
require(len(pngs)==16 and [p.name for p in pngs]==[f'page-{i}.png' for i in range(1,17)], 'rendered page image inventory mismatch')
inputs={k:{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for k,p in {'source_packet':PACKET,'unique_blueprint_0100':BLUEPRINT,'official_evidence_pdf':OFFICIAL,'synthetic_replacement_register':REGISTER,'word_native_pdf':PDF}.items()}
receipt={
 'receipt_id':'TTQS-0100-I18-E08-R09B-TECHNICAL-QA', 'generated_local':datetime.now().astimezone().isoformat(),
 'doc_id':'0100','official_requirement_id':'I18-E08','project_internal_index':109,'official_printed_checkbox_serial':'UNKNOWN',
 'revision':'R09b','artifact_state':'CANDIDATE','formal_acceptance':'NOT_GRANTED','real_evidence':'UNKNOWN/HOLD',
 'candidate':{'path':str(DOCX),'sha256':doc_sha,'bytes':DOCX.stat().st_size,'zip_integrity':'PASS','word_paragraphs':len(doc.paragraphs),'word_tables':len(doc.tables),'word_sections':len(doc.sections)},
 'inputs':inputs,'content_checks':checks,'pairing_rule_text':pair,
 'sample_math':{'respondent_pairs':len(observed),'dimensions':5,'phases':2,'original_score_cells':80,'range':[0,4],'pre_total':pre_sum,'post_total':post_sum,'delta':post_sum-pre_sum,'pre_mean':pre_sum/8,'post_mean':post_sum/8,'mean_delta':(post_sum-pre_sum)/8,'rows':observed,'dimension_rows':expected_dims},
 'replacement_register':{'rows':len(register),'all_rows_sample_synthetic':True,'sha256':reg_sha},
 'word_render':{'method':'Microsoft Word native COM PDF export (existing PDF; no re-export in this QA run)','pdf_sha256':sha(PDF),'page_count':page_count,'page_image_count':len(pngs),'page_image_sha256':{p.name:sha(p) for p in pngs}},
 'semantic_review':'PENDING','scope_limit':'Deterministic technical and consistency checks only; does not establish semantic acceptance or association approval.',
 'result':'TECHNICAL_PASS_FOR_EXACT_SHA; VISUAL_REVIEW_RECORDED_SEPARATELY; CANDIDATE_NOT_FORMALLY_ACCEPTED'
}
out=CAND/'TECHNICAL_QA_0100_R09B.json'
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')

visual={
 'receipt_id':'TTQS-0100-I18-E08-R09B-VISUAL-QA','generated_local':datetime.now().astimezone().isoformat(),
 'doc_id':'0100','official_requirement_id':'I18-E08','revision':'R09b','candidate_sha256':doc_sha,
 'rendered_pdf_sha256':sha(PDF),'rendered_page_count':page_count,'rendered_page_image_count':len(pngs),
 'pages_inspected':'1-16 individually at rendered page size; current layout2 set',
 'observations':['Cover maps to 0100/I18-E08 and labels R09b and SAMPLE/SYNTHETIC.','Respondent form, 0-4 scale, paired sample matrix, arithmetic, intake/hold/reject guidance, 0101 handoff, and replacement register are legible.','No visible clipping, overlapping text, truncated table rows, orphan checkboxes, or broken continuations in the inspected 16-page render.','Page 13 contains a short calculation interpretation section and substantial white space before section 9 starts on page 14; recorded as non-blocking whitespace, not a content or readability failure.'],
 'method':'Existing Microsoft Word native COM PDF export rendered to PNG; each page visually inspected; exact artifact/PDF/page image hashes listed in technical QA receipt.',
 'limitations':['This visual review is separate from semantic review.','No physical print test.','No formal association acceptance.'],
 'result':'VISUAL_PASS_WITH_NONBLOCKING_WHITESPACE_FOR_EXACT_SHA; CANDIDATE_NOT_FORMALLY_ACCEPTED'
}
vout=CAND/'VISUAL_QA_0100_R09B.json'
vout.write_text(json.dumps(visual,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'candidate_sha256':doc_sha,'technical_receipt':str(out),'technical_receipt_sha256':sha(out),'visual_receipt':str(vout),'visual_receipt_sha256':sha(vout),'pdf_sha256':sha(PDF),'page_count':page_count,'score_cells':80,'pre_total':pre_sum,'post_total':post_sum,'delta':post_sum-pre_sum,'register_rows':len(register),'checks':checks},ensure_ascii=False))
