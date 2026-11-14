import hashlib, json
from pathlib import Path
root=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0053_R03')
ev=root/'evidence'; rev=root/'review'/'opencode_v2_review_R03'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def save(p,obj):
    with p.open('w',encoding='utf-8',newline='\n') as f:
        f.write(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
font=ev/'font_size_qa_receipt_R03.json'; fontj=load(font)
review_path=rev/'independent_semantic_review_R03.md'
review_receipt_path=rev/'independent_review_receipt_R03.json'
visual_path=ev/'visual_layout_receipt_R03.json'
tech_path=ev/'technical_integrity_receipt_R03.json'
status=root/'candidate_status_R03.md'
decision_path=ev/'candidate_quality_decision_R03.json'
review_receipt=load(review_receipt_path)
review_receipt['supplemental_font_floor_verification']={
 'result':'PASS',
 'method':'exact-SHA OOXML inspection of document.xml, styles.xml, paragraph style inheritance, run sizes, and table text runs',
 'receipt_path':'evidence/font_size_qa_receipt_R03.json',
 'receipt_sha256':sha(font),
 'body_floor_pt':10.5,
 'table_floor_pt':9.5,
 'independent_reviewer_subscope_preserved':'The reviewer itself marked exact font-size measurement PARTIAL/UNKNOWN from images; this separate deterministic check closes the technical criterion without altering the raw reviewer verdict.'}
review_receipt['candidate_quality_synthesis']='PASS_WITH_REVIEW_SCOPE_NOTE: independent semantic review PASS; exact-SHA OOXML body/table font checks PASS; operator full-size 18-page visual inspection PASS; reviewer exact-font sub-scope remains PARTIAL/UNKNOWN in the raw review.'
review_receipt['promotion_status']='NOT_PROMOTED'
review_receipt['formal_association_acceptance']='NOT_CLAIMED'
save(review_receipt_path,review_receipt)
tech=load(tech_path)
tech.update({
 'font_size_qa_receipt_path':'evidence/font_size_qa_receipt_R03.json',
 'font_size_qa_receipt_sha256':sha(font),
 'body_font_floor':'PASS; all non-kicker body runs at least 10.5 pt; Normal style is 10.5 pt',
 'table_font_floor':'PASS; minimum actual table text run is 9.5 pt',
 'section_kicker_scope':'16 numbered/appendix kicker runs at 8.5 pt; none are body or table content',
 'unused_smaller_style_definitions':['BodyText3 8 pt (unused)','Caption 9 pt (unused)'],
 'independent_review_status':'PASS substantive semantics; reviewer image-based exact-font subcriterion PARTIAL/UNKNOWN; separate exact-SHA OOXML font QA PASS',
 'independent_review_receipt_sha256':sha(review_receipt_path)})
save(tech_path,tech)
visual=load(visual_path)
visual['independent_visual_review_status']='Completed; reviewer found no anomaly in attached contact sheet and selected pages; reviewer exact point sizes PARTIAL/UNKNOWN; operator full-size inspection covers all 18 pages.'
visual['supplemental_font_receipt_sha256']=sha(font)
save(visual_path,visual)
status_text='''# DOCX 0053 R03 candidate quality status

- Candidate exact SHA-256: `cc75583238dba42eede61de990992770f8de75e96d1bcfe1313e57629551f8e8` (68,614 bytes).
- Requirement mapping: DOCX `0053` = Unique Blueprint `I12-E01`; official 157-grid sequence `056` (distinct numbering systems).
- Technical integrity: PASS; Word ZIP valid, 124 paragraphs, 29 tables, 40 unique replacement-register rows.
- Register rendered-page anchors: PASS 40/40; exact register SHA-256 `65c5c4c7c8b5393481102a5e8f961640701c264454fdd53233a0dc0692909e9d`.
- Font floor: PASS by exact-SHA OOXML inspection; body 10.5 pt minimum, table 9.5 pt minimum. Section kickers are 8.5 pt; unused BodyText3 8 pt and Caption 9 pt styles do not occur in the document body.
- Layout: PASS operator full-size inspection of pages 1–18; no clipping, overflow, or blank page found. Word-export PDF SHA-256 `ad9b3ce5cb6d87fb0c941635076fabb6e204ad304ce59dddbc4fd18ee92dc2e5`.
- Independent OpenCode CLI v2 exact-SHA semantic review: PASS; reviewer recomputed candidate SHA and verified the math, 40-row register, sample/real boundary, title-blind purpose, and adjacent-document distinctions. Raw review and receipt are in `review/opencode_v2_review_R03/`.
- Review-scope note: the reviewer marked its image-only exact font-size subcriterion PARTIAL/UNKNOWN. A separate OOXML size check bound to the same candidate SHA verifies the 10.5/9.5 pt floors; the raw reviewer result remains unchanged.
- Candidate quality synthesis: PASS_WITH_REVIEW_SCOPE_NOTE. Formal association acceptance is NOT CLAIMED; promotion remains NOT PROMOTED; REAL evidence remains UNKNOWN.
- R01 and R02 are retained as historical/superseded candidates; R02 was not independently reviewed. R01's 81/9-minute interpretation is superseded by exact 0052 source evidence and is invalid.
'''
with status.open('w',encoding='utf-8',newline='\n') as f: f.write(status_text)
decision={
 'schema':'ttqs.0053.candidate_quality_decision.v1',
 'doc_id':'0053','requirement_id':'I12-E01','official_checkbox_sequence':'056',
 'candidate_sha256':fontj['candidate_sha256'],
 'technical_integrity':'PASS',
 'replacement_register':'PASS 40 unique rows; exact candidate SHA binding',
 'register_rendered_page_anchors':'PASS 40/40',
 'body_font_floor':'PASS 10.5 pt minimum for non-kicker body text; Normal style 10.5 pt',
 'table_font_floor':'PASS 9.5 pt minimum',
 'visual_layout':'PASS_OPERATOR_FULL_PAGE_VISUAL pages 1-18',
 'independent_semantic_review':'PASS exact-SHA OpenCode CLI v2 review',
 'independent_reviewer_visual_scope':'Reviewer found text/tables legible and no anomaly in attached images; reviewer exact font floor marked PARTIAL/UNKNOWN because images cannot prove point sizes.',
 'supplemental_deterministic_font_review':'PASS exact candidate SHA OOXML style/run inspection; see font receipt.',
 'material_findings':'None. Reviewer notes Page 3 uses 分 as shorthand for minutes, but neighboring context disambiguates.',
 'overall_internal_candidate_quality':'PASS_WITH_REVIEW_SCOPE_NOTE',
 'promotion_status':'NOT_PROMOTED','formal_association_acceptance':'NOT_CLAIMED',
 'real_evidence_status':'UNKNOWN; all demonstrated facts remain SAMPLE/SYNTHETIC',
 'technical_receipt_sha256':sha(tech_path),'font_receipt_sha256':sha(font),
 'review_receipt_sha256':sha(review_receipt_path),'review_report_sha256':sha(review_path),
 'visual_receipt_sha256':sha(visual_path),'candidate_status_sha256':sha(status)}
save(decision_path,decision)
print(json.dumps({'font_receipt_sha256':sha(font),'body_font':'PASS','table_font':'PASS','reviewer_semantic':'PASS','reviewer_font_subscope':'PARTIAL/UNKNOWN preserved','decision':'PASS_WITH_REVIEW_SCOPE_NOTE','decision_sha256':sha(decision_path),'technical_receipt_sha256':sha(tech_path),'review_receipt_sha256':sha(review_receipt_path),'status_sha256':sha(status)},ensure_ascii=False,indent=2))
