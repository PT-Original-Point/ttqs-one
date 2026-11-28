import hashlib,json
from pathlib import Path
from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table
root=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0031_SOURCE_PACKET_20261118')
candidate=root/'candidate'/'0031_I06_E02_CANDIDATE_R01.docx'
source=root/'SOURCE_PACKET.md'
blueprint=root/'UNIQUE_BLUEPRINT.md'
review=root/'qa'/'semantic'/'review_R01_OPENCODE_MIMO'
review.mkdir(parents=True,exist_ok=True)
doc=Document(str(candidate))
blocks=[]
for block in doc.iter_inner_content():
    if isinstance(block,Paragraph):
        if block.text.strip():
            blocks.append(block.text)
    elif isinstance(block,Table):
        blocks.append('')
        for row in block.rows:
            blocks.append(' | '.join(cell.text.replace('\n',' / ').strip() for cell in row.cells))
        blocks.append('')
body='\n'.join(blocks).strip()+'\n'
body_path=review/'EXTRACTED_BODY_R01.txt'
body_path.write_text(body,encoding='utf-8',newline='')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest().upper()
cand_sha=sha(candidate)
source_sha=sha(source)
blue_sha=sha(blueprint)
body_sha=sha(body_path)
text=f"""WORK_ID=TTQS_ONE_0031_I06-E02_INDEPENDENT_SEMANTIC_REVIEW_R01_20261118
DOC_ID=0031
REQUIREMENT_ID=I06-E02
REQUESTED_MODEL_ROUTE=opencode/mimo-v2.6-flash-free
ROLE=Independent semantic/usability reviewer; not Writer
CANDIDATE_DOCX_SHA256={cand_sha}
SOURCE_PACKET_SHA256={source_sha}
UNIQUE_BLUEPRINT_SHA256={blue_sha}
EXTRACTED_BODY_SHA256={body_sha}
REVIEW_SCOPE=Requirement alignment, operational usability, scoring/reassessment arithmetic, SAMPLE/REAL boundary, fact and replacement-register consistency, negative-neighbor distinction. Visual/layout review is separate.

INSTRUCTIONS
Independently review the exact candidate body below against the source packet and dedicated Blueprint. Verify these exact input hashes are repeated in your response. Do not trust Builder or deterministic QA claims as semantic proof. Do not edit files, call tools, or claim visual pass. Return RESULT=PASS/SCOPED_FAIL/FAIL/INSUFFICIENT_EVIDENCE; exact candidate SHA; REVIEWED_INPUT_SHA256 equal to extracted body SHA; findings with severity, section/table locator, short excerpt at most 25 Chinese characters, issue and minimal correction; confirm visibility and completeness of the SAMPLE/SYNTHETIC fact register and per-ID REAL replacement register; independently recompute any stated score, gap, average and reassessment values; report unverifiable real-world claims as UNKNOWN; check that 0031 is not a substitute for I06-E01 third-party experience originals or I06-E03 institution/manager capacity. Do not return ACK-only.

===== SOURCE PACKET =====
{source.read_text(encoding='utf-8')}

===== UNIQUE BLUEPRINT =====
{blueprint.read_text(encoding='utf-8')}

===== EXACT CANDIDATE EXTRACTED BODY =====
{body}
"""
packet_path=review/'REVIEW_PACKET_R01_OPENCODE_MIMO.md'
packet_path.write_text(text,encoding='utf-8',newline='')
receipt={
 'schema':'TTQS_ONE_0031_OPENCode_MIMO_REVIEW_PACKET',
 'work_id':'TTQS_ONE_0031_I06-E02_INDEPENDENT_SEMANTIC_REVIEW_R01_20261118',
 'requested_model_route':'opencode/mimo-v2.6-flash-free',
 'candidate_sha256':cand_sha,'source_packet_sha256':source_sha,'blueprint_sha256':blue_sha,
 'extracted_body_sha256':body_sha,'review_packet_sha256':sha(packet_path),
 'candidate_path':str(candidate),'body_path':str(body_path),'packet_path':str(packet_path),
 'text_blocks_in_document_order':len(blocks),'noninteractive_review_only':True
}
(review/'REVIEW_PACKET_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps(receipt,ensure_ascii=False,indent=2))