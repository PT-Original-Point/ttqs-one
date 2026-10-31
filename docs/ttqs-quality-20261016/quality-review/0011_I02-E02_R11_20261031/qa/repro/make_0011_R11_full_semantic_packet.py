from pathlib import Path
from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
import hashlib,json,csv,datetime
B=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0011_I02-E02_LUNA_TEXT_DRAFT_R01_20261029')
P=B/'candidate'/'0011_I02-E02_R11.docx'; PDF=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\INPUTS\R04\06_OFFICIAL_SOURCES\TTQS查核佐證文件資料表-訓練機構版 (2).pdf')
BP=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\BLUEPRINT_CURRENT.jsonl'); CW=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\TTQS_ONE_129_REQUIREMENT_TO_142_DELIVERABLE_CROSSWALK_R01.csv')
TECH=B/'qa'/'technical_qa_R11.json'; OLD1=B/'qa'/'W1_SEMANTIC_REVIEW_R09_20261030'/'DISPATCH_TERMINAL.json'; OLD2=B/'qa'/'W1_SEMANTIC_REVIEW_R09_20261030'/'GLM_R02_20261030'/'DISPATCH_TERMINAL_R02.json'; OLD3=B/'qa'/'W1_SEMANTIC_REVIEW_R10_20261030'/'DISPATCH_TERMINAL_R01.json'; OLD3R=B/'qa'/'W1_SEMANTIC_REVIEW_R10_20261030'/'REVIEW_RESPONSE_R01.txt'; OLD3I=B/'qa'/'W1_SEMANTIC_REVIEW_R10_20261030'/'REVIEW_INPUT_R10_DELTA.md'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
rows={}
for line in BP.read_text(encoding='utf-8-sig').splitlines():
 try:
  r=json.loads(line)
  if r.get('deliverable_id') in ('0011','0010','0012'): rows[r['deliverable_id']]=(line,r)
 except Exception: pass
with CW.open(encoding='utf-8-sig',newline='') as f: cross=[x for x in csv.DictReader(f) if x.get('requirement_id')=='I02-E02']
if len(rows)!=3 or len(cross)!=1: raise SystemExit('SOURCE_ROWS_NOT_UNIQUE')
doc=Document(P); pieces=[]; para_index=0; table_index=0
for el in doc.element.body.iterchildren():
 if isinstance(el,CT_P):
  p=Paragraph(el,doc); t=p.text
  if t.strip(): pieces.append(t)
  para_index+=1
 elif isinstance(el,CT_Tbl):
  tb=Table(el,doc); table_index+=1
  pieces.append(f'\n[TABLE {table_index}]')
  for ri,row in enumerate(tb.rows,1):
   pieces.append(' | '.join(cell.text.replace('\n',' / ').strip() for cell in row.cells))
body='\n'.join(pieces)
if not body or '版本：R11' not in body: raise SystemExit('CANDIDATE_EXTRACTION_OR_VERSION_FAILED')
tech=json.loads(TECH.read_text(encoding='utf-8-sig'))
old1=json.loads(OLD1.read_text(encoding='utf-8-sig')); old2=json.loads(OLD2.read_text(encoding='utf-8-sig')); old3=json.loads(OLD3.read_text(encoding='utf-8-sig'))
row_text=[]
for did in ('0011','0010','0012'):
 line,r=rows[did]
 row_text.append(f"### {did} / {r.get('requirement_id')}\n- raw JSONL line SHA-256: {hashlib.sha256(line.encode('utf-8')).hexdigest()}\n- canonical sorted compact JSON SHA-256: {hashlib.sha256(json.dumps(r,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()}\n- complete unique Blueprint row JSON:\n```json\n{json.dumps(r,ensure_ascii=False,indent=2)}\n```")
packet=f'''# Independent full semantic review request — TTQS ONE 0011 R11

## Review identity and evidence binding
- work_id: TTQS-0011-W1-SEMANTIC-R11-FULL-20261031-01
- Worker: W1 OpenCode v2 CLI; requested model opencode/glm-5.3-flash-free; actual serving model must be UNKNOWN unless provider/session evidence proves it.
- Candidate state: CANDIDATE / SAMPLE-SYNTHETIC; no formal acceptance or REAL evidence is asserted.
- DOCX ID: 0011. Official requirement ID / checkbox: I02-E02. These identifiers are distinct.
- Candidate filename: {P.name}
- Candidate DOCX SHA-256: {sha(P)}
- Candidate bytes: {P.stat().st_size}
- Candidate exact text extraction SHA-256 (document order, paragraphs and tables): {hashlib.sha256(body.encode('utf-8')).hexdigest()}
- Official source PDF: {PDF.name}; SHA-256: {sha(PDF)}; page 1.
- Official requirement exact text: 與訓練政策有關之訓練產品與市場定位。
- Current Blueprint file SHA-256: {sha(BP)}
- 129-to-142 crosswalk file SHA-256: {sha(CW)}; the row maps I02-E02 to exactly one deliverable, 0011.
- R11 deterministic technical receipt SHA-256: {sha(TECH)}; status {tech.get('status')}; exact candidate SHA bound.
- Word-native visual render is a separate gate and is currently being produced; do not infer visual PASS from this packet.

## Important correction to prior semantic history
Do NOT inherit any full semantic PASS from R09. R09's first W1 attempt failed before a review result (HTTP 429; terminal SHA {sha(OLD1)}). Its later W1 response returned PARTIAL, not PASS (terminal SHA {sha(OLD2)}; raw response SHA {old2.get('stdout_sha256')}). The R09 input binding explicitly recorded no prior exact-SHA semantic receipt. The R10 review was only a scoped delta; its response claimed an R09 full PASS, which contradicts the R09 PARTIAL receipt and the R10 review input itself. R10 delta PASS therefore cannot establish full semantic acceptance. R10 SHA was {old3.get('candidate_sha256_before')}; R11 is a new exact SHA and the only subject of this review. Relevant R10 delta response SHA: {sha(OLD3R)}; R10 input packet SHA: {sha(OLD3I)}; terminal receipt SHA: {sha(OLD3)}.

## Reviewer task
Perform a fresh, complete, independent semantic/usability review of the entire R11 candidate text below against the official requirement and the complete unique Blueprint row. Do not review or edit files, do not use tools, do not infer facts from filenames, and do not treat prior reviews as a semantic baseline. This is text-only semantic scope; it does not replace native Word visual QA or formal association acceptance.

Check at minimum:
1. Exact requirement binding, correct document genre and association-specific use; title-blind identification from body mechanics.
2. Complete, usable operational policy for connecting verified training policy → target learners/needs/competencies → product positioning → course design/review → update/exception/HOLD. Determine whether major tables/forms are actionable, not template-only.
3. Whether form fields, instructions, decision roles, inputs, validation, outputs, exception/return/reject/HOLD criteria and attachment index are complete.
4. Every showcased score and ratio is mathematically consistent with visible weights, scales and denominators. Distinguish a design suggestion from an official TTQS rule.
5. Every sample case, date, role, number, decision and claimed result is clearly SAMPLE/SYNTHETIC; no association approval, real course, real survey, third-party evidence, signature or performance is fabricated. Check whether replacement register is complete enough to replace synthetic facts.
6. Cross-section consistency, fact IDs, internal document references and relationship to adjacent requirements I02-E01/0010 and I02-E03/0012. Reject near-neighbor misclassification.
7. Human readability and direct use by association staff and evaluators. Identify exact section/table/paragraph locators for every defect.
8. The front-page version label must agree with R11; do not claim any formal or REAL status.

Return one JSON object with keys: verdict (PASS/PARTIAL/FAIL), candidate_sha256, extracted_text_sha256, doc_id, requirement_id, official_checkbox_serial (UNKNOWN unless established from source), blueprint_file_sha256, blueprint_row_sha256_raw_line, blueprint_row_sha256_canonical_sorted_compact, reviewed_scope, checks (each PASS/PARTIAL/FAIL with locator and rationale), findings (severity, locator, concrete defect, required minimal repair), sample_real_boundary, title_blind_result, negative_neighbor_result, calculation_recheck, usability_result, limitations, actual_model_identity (UNKNOWN unless proven), formal_acceptance (NOT_GRANTED). A PASS is allowed only if the whole provided R11 body was reviewed and no material semantic/usability defect remains. Do not state that you independently opened or hashed the DOCX; exact file SHA and extraction SHA are bound by this packet.

## Authoritative unique Blueprint rows
{chr(10).join(row_text)}

## Official source and mapping
The official source is the PDF/page named above, hash-bound above; exact requirement text is reproduced above. The crosswalk file maps requirement I02-E02 to deliverable ID 0011 only. Do not infer the official checkbox serial from document ID.

## Full extracted R11 candidate body and all tables in document order
{body}
'''
out=B/'qa'/'W1_SEMANTIC_REVIEW_R11_FULL_20261031'/'REVIEW_INPUT_R11_FULL.md'
out.parent.mkdir(parents=True,exist_ok=True); out.write_text(packet,encoding='utf-8')
binding={'schema':'ttqs-one-review-input-binding-v1','work_id':'TTQS-0011-W1-SEMANTIC-R11-FULL-20261031-01','worker':'W1 OpenCode v2 CLI','requested_model':'opencode/glm-5.3-flash-free','actual_model':'UNKNOWN_UNLESS_SESSION_METADATA_PROVES','stage':'READY_INDEPENDENT_SEMANTIC','status':'READY_FOR_SINGLE_DISPATCH','doc_id':'0011','requirement_id':'I02-E02','candidate_docx_path':str(P),'candidate_docx_sha256':sha(P),'candidate_docx_bytes':P.stat().st_size,'extracted_text_sha256':hashlib.sha256(body.encode('utf-8')).hexdigest(),'review_input_path':str(out),'review_input_sha256':sha(out),'review_scope':'full body + all tables in document order; official requirement + unique Blueprint row + crosswalk + negative neighbors; text-only semantic/usability review','official_source_pdf_sha256':sha(PDF),'blueprint_file_sha256':sha(BP),'blueprint_row_sha256_raw_line':hashlib.sha256(rows['0011'][0].encode('utf-8')).hexdigest(),'blueprint_row_sha256_canonical_sorted_compact':hashlib.sha256(json.dumps(rows['0011'][1],ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest(),'negative_neighbor_rows':{'0010':hashlib.sha256(json.dumps(rows['0010'][1],ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest(),'0012':hashlib.sha256(json.dumps(rows['0012'][1],ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()},'crosswalk_file_sha256':sha(CW),'technical_receipt_sha256':sha(TECH),'prior_R09_semantic_status':'PARTIAL; first attempt provider 429','prior_R10_delta_status':'PASS_FOR_DELTA_ONLY_BUT_BASELINE_PREMISE_CONTRADICTED; not full semantic acceptance','formal_acceptance':'NOT_GRANTED'}
bp=out.parent/'REVIEW_INPUT_BINDING_R11.json'; bp.write_text(json.dumps(binding,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'packet_path':str(out),'packet_sha256':sha(out),'packet_chars':len(packet),'packet_bytes':out.stat().st_size,'extracted_text_sha256':binding['extracted_text_sha256'],'candidate_sha256':binding['candidate_docx_sha256'],'blueprint_file_sha256':binding['blueprint_file_sha256'],'blueprint_row_raw_sha':binding['blueprint_row_sha256_raw_line'],'blueprint_row_canonical_sha':binding['blueprint_row_sha256_canonical_sorted_compact'],'binding_sha256':sha(bp)},ensure_ascii=True))
