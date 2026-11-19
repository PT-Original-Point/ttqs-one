import sys,hashlib,json,csv
from pathlib import Path
from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table
from docx.oxml.ns import qn
from pypdf import PdfReader
repo=Path(sys.argv[1]); runtime=Path(sys.argv[2]); out=Path(sys.argv[3]); base=repo/'docs/ttqs-quality-20261016/quality-review/0022_R122_WORKER_DELIVERY_20261119/R01_candidate'
docx=base/'0022_I04-E01_R01.docx'; pdf=base/'0022_I04-E01_R01_FINAL.pdf'; qa_path=base/'qa/technical_qa.json'
source=repo/'docs/ttqs-quality-20261016/quality-review/0026_R11_20261117/source/inputs'
cross=source/'CROSSWALK_129_TO_142_R01.csv'; blueprint=source/'BLUEPRINT_157_CHECKBOXES_LIVE_R01.md'; official=source/'OFFICIAL_TTQS_EVIDENCE_TABLE_R04.pdf'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest().upper()
D=Document(str(docx)); parts=[]
for child in D.element.body.iterchildren():
 if child.tag==qn('w:p'): parts.append(Paragraph(child,D).text)
 elif child.tag==qn('w:tbl'):
  for row in Table(child,D).rows: parts.append(' | '.join(c.text.replace('\n',' / ') for c in row.cells))
text='\n'.join(parts); text_path=base/'source/CANDIDATE_EXTRACTED_TEXT_R01_EXACT_SHA.txt'; text_path.parent.mkdir(parents=True,exist_ok=True); text_path.write_text(text,encoding='utf-8',newline='\n')
rows=list(csv.reader(cross.open(encoding='utf-8-sig',newline=''))); crow=next(r for r in rows if len(r)>3 and r[3].strip()=='0022')
blue_lines=blueprint.read_text(encoding='utf-8-sig').splitlines(); bline=next(x for x in blue_lines if x.startswith('019｜'))
pages=PdfReader(str(official)).pages; page_text=pages[0].extract_text() or ''
qa=json.loads(qa_path.read_text(encoding='utf-8-sig'))
sha_doc=sha(docx); shat=sha(text_path); shas={'official_pdf':sha(official),'crosswalk_csv':sha(cross),'blueprint_md':sha(blueprint)}
assert sha_doc==qa['candidate_sha256']
assert qa['Q10_counts_ok'] and qa['Q11_totals_ok'] and qa['Q4_in_doc'] and qa['truth_boundary_ok'] and not qa['unregistered_ids']
work_id='TTQS_ONE_0022_I04-E01_R01_EXACT_SHA_SEMANTIC_W2_R02_20261119'
packet=f'''# TTQS ONE exact-SHA 獨立語意審查工作包\n\nwork_id: {work_id}\nproject_id: TTQS_ONE\ndoc_id: 0022\nrequirement_id: I04-E01\nrepo/ref: PT-Original-Point/ttqs-one / work/ttqs-one-document-quality-contract-20261016\nsource HEAD: 045a9968acbd8d415e289519baebeb717359a0cc\nreviewer: W2 Antigravity CLI; review only, no file writes\nrequested route: gemini-3.8-flash-high; actual served model must be reported UNKNOWN unless native evidence proves otherwise\n\n## 固定候選身分\n- DOCX: 0022_I04-E01_R01.docx\n- DOCX SHA-256: {sha_doc}\n- DOCX bytes: {docx.stat().st_size}\n- extracted text SHA-256: {shat}\n- extracted text bytes: {len(text.encode('utf-8'))}\n- final PDF SHA-256: {sha(pdf)}\n\n## 權威來源與需求\n- Official R04 evidence PDF SHA-256: {shas['official_pdf']}; page 1 extracted text follows.\n- Exact crosswalk row: {','.join(crow)}\n- Crosswalk SHA-256: {shas['crosswalk_csv']}\n- 157 Blueprint item: {bline}\n- Blueprint SHA-256: {shas['blueprint_md']}\n\n### Official PDF page 1 text extract\n{page_text}\n\n## Deterministic QA receipt\n```json\n{json.dumps(qa,ensure_ascii=False,indent=2)}\n```\n\n## Prior bounded pre-DOCX review findings to specifically verify as corrected\nThe prior W2 review was explicitly text-only and not a final DOCX exact-SHA acceptance. It found: Q10 T2 phantom count; Q11 phantom workshop row; Q4 missing from response table/register; inaccurate Section 10 locators; missing synthetic register coverage. Current exact-SHA candidate must be independently checked for these corrections, current cross-table formulas, all factual synthetic IDs registered, SAMPLE/UNKNOWN boundary, usability and negative-neighbor scope. Do not reuse the prior verdict.\n\n## Review rules\n1. Recompute/verify both hashes above from the supplied candidate identity and extracted text; any mismatch means BINDING_FAIL.\n2. Inspect only semantic fit, complete mechanics, source alignment, arithmetic, synthetic register, truth boundary, and neighboring-document scope. This is not visual/layout or technical QA.\n3. Report exact DOCX SHA, extracted-text SHA, binding verdict, semantic verdict PASS/PARTIAL/FAIL, precise findings by section/table/row, and served model UNKNOWN unless proven.\n4. Do not edit files, create DOCX, request payment, or claim formal acceptance.\n5. Stop after this one bounded candidate review; no repair proposal requiring full rewrite when a scoped correction suffices.\n\n## Candidate extracted text\n{text}\n'''
packet_path=out/'WORK_PACKET.md'; packet_path.write_text(packet,encoding='utf-8',newline='\n')
print(json.dumps({'work_id':work_id,'candidate_sha256':sha_doc,'candidate_bytes':docx.stat().st_size,'extracted_text_sha256':shat,'pdf_sha256':sha(pdf),'source_hashes':shas,'text_path':str(text_path),'packet_path':str(packet_path),'packet_sha256':sha(packet_path),'packet_bytes':packet_path.stat().st_size,'crosswalk_row':crow,'blueprint_item':bline},ensure_ascii=False))
