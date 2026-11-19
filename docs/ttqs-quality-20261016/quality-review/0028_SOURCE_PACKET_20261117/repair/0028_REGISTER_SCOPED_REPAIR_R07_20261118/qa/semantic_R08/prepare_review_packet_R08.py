from pathlib import Path
from hashlib import sha256
from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table
from docx.oxml.ns import qn
import json
root=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0028_SOURCE_PACKET_20261117')
folder=root/'repair'/'0028_REGISTER_SCOPED_REPAIR_R07_20261118'
candidate=folder/'candidate_0028_R08_20261118.docx'
source_path=root/'source'/'SOURCE_PACKET_0028_I05-E02_R01.md'
blueprint_path=root/'blueprint'/'UNIQUE_BLUEPRINT_0028_I05-E02_R01.md'
qa=folder/'qa'/'semantic_R08'
qa.mkdir(parents=True,exist_ok=True)
packet_path=qa/'W1_REVIEW_PACKET_R08.md';extracted_path=qa/'DOCX_EXTRACTED_TEXT_R08.txt';receipt_path=qa/'PACKET_BUILD_R08.json'
if any(p.exists() for p in (packet_path,extracted_path,receipt_path)): raise SystemExit('SEMANTIC_R08_OUTPUT_EXISTS_REFUSE_OVERWRITE')
doc=Document(candidate);parts=[]
for child in doc.element.body.iterchildren():
    if child.tag==qn('w:p'):
        p=Paragraph(child,doc)
        if p.text.strip(): parts.append(p.text.strip())
    elif child.tag==qn('w:tbl'):
        table=Table(child,doc);parts.append('[TABLE]')
        for row in table.rows: parts.append(' | '.join(' '.join(p.text for p in cell.paragraphs).strip() for cell in row.cells))
        parts.append('[/TABLE]')
body='\n'.join(parts)+'\n'
source=source_path.read_text(encoding='utf-8');blueprint=blueprint_path.read_text(encoding='utf-8')
sha=lambda b:sha256(b).hexdigest().upper()
candidate_sha=sha(candidate.read_bytes());body_sha=sha(body.encode('utf-8'));source_sha=sha(source_path.read_bytes());blueprint_sha=sha(blueprint_path.read_bytes())
prompt=[
'# W1 獨立語意審查｜0028 R08',
'work_id: TTQS_ONE_0028_I05-E02_W1_SEMANTIC_REVIEW_R08_20261118',
'doc_id: 0028','requirement_id: I05-E02',
'requested_model: opencode/nemotron-3.5-lightning-free',
'candidate_docx_sha256: '+candidate_sha,'extracted_text_sha256: '+body_sha,
'source_packet_sha256: '+source_sha,'blueprint_sha256: '+blueprint_sha,
'review_role: fresh independent semantic/usability review; read-only; do not modify files',
'visual_scope: excluded; exact-SHA Word visual review is separately recorded',
'',
'Return exactly one JSON object, no Markdown, with keys work_id, candidate_docx_sha256, extracted_text_sha256, requested_model, served_model, decision (PASS/FAIL_REPAIRABLE/FAIL), findings[{severity,locator,evidence,required_action}], scope_checks, rationale. Bind this review to the exact candidate and extracted-text SHA above. Do not infer served_model from requested_model; report UNKNOWN unless independently observable.',
'',
'Evaluate only the supplied official packet, unique Blueprint, and full extracted R08 DOCX body:',
'1. Does the document directly satisfy exact I05-E02 and the strategy/course-system genre, with operational steps, owners, timing, measures, decisions, and traceable evidence?',
'2. Does title-blind identification distinguish 0028/I05-E02 from negative neighbors 0027/I05-E01 and 0029/I05-E03? Reject copied or merged peer scope.',
'3. Are SAMPLE/SYNTHETIC facts, dates, counts, ratios, owners, and decisions coherent and registered/replacement-mapped? Recalculate KPI 2=2/3=66.7%; KPI 3=5/6=83.3%, with exact minimum threshold 833/1000 and monthly measurement cadence. Confirm DATE-006 is absent from active facts and history.',
'4. Are institution-specific unknowns honestly marked, with no invented association approval, signature, external proof, or actual performance?',
'5. Is the document complete and usable without blank/placeholder-only sections, with clear replacement steps and evaluator-facing language?',
'6. Give precise heading/table-row locators. A blocking finding must materially impair correct use or evidence acceptance. Do not repeat prior findings unless the exact defect persists in R08.',
'',
'## OFFICIAL SOURCE PACKET (SHA-256 '+source_sha+')',source,
'',
'## UNIQUE BLUEPRINT (SHA-256 '+blueprint_sha+')',blueprint,
'',
'## FULL EXTRACTED R08 DOCX BODY (SHA-256 '+body_sha+')',body,''
]
packet='\n'.join(prompt)
extracted_path.write_text(body,encoding='utf-8');packet_path.write_text(packet,encoding='utf-8')
receipt={'schema':'TTQS_ONE_0028_W1_REVIEW_PACKET_R08','work_id':'TTQS_ONE_0028_I05-E02_W1_SEMANTIC_REVIEW_R08_20261118','candidate_docx_sha256':candidate_sha,'extracted_text_sha256':body_sha,'source_packet_sha256':source_sha,'blueprint_sha256':blueprint_sha,'review_packet_sha256':sha(packet.encode('utf-8')),'review_packet_path':str(packet_path),'extracted_text_path':str(extracted_path),'review_packet_bytes':len(packet.encode('utf-8')),'review_packet_chars':len(packet),'extracted_text_chars':len(body),'requested_model':'opencode/nemotron-3.5-lightning-free','served_model':'UNKNOWN_PENDING_PROVIDER_RECEIPT','review_scope':'single requirement I05-E02; exact R08 candidate; no cross-document corpus','decision':'PENDING_DISPATCH'}
receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False))

