import hashlib,json
from pathlib import Path
root=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0053_R03')
ev=root/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,obj):
 with p.open('w',encoding='utf-8',newline='\n') as f:f.write(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
layout_path=ev/'visual_layout_receipt_R03.json'; layout=json.loads(layout_path.read_text(encoding='utf-8'))
layout['all_pages_directly_inspected_full_size']=list(range(1,19))
layout['full_size_pages_directly_inspected']=list(range(1,19))
layout['observations']=[
 'All 18 page PNGs were opened and visually inspected at full-size resolution; page sequence, tables, margins, headers/footers, and readability were checked.',
 'No blank or near-blank page, visible clipping, text overlap, table overflow, or broken page furniture was found in the 18-page sequence.',
 'Pages 2, 5, 8, 10, and 18 were given additional targeted inspection for P0-SYN, P2 SAMPLE-only threshold, F1 venue row, 90-minute recalculation, and Appendix C locators.',
 'The 40-row replacement register page anchors were checked against extracted text from the Word-export PDF; 40/40 pass.'
]
layout['status']='PASS_OPERATOR_FULL_PAGE_VISUAL'
layout['independent_visual_review_status']='PENDING OpenCode v2 exact-SHA review; operator inspection is not represented as independent reviewer evidence'
layout['limitations']=['This receipt documents the producing agent operator visual inspection; the independent reviewer must provide its own visual scope or mark it PARTIAL/UNKNOWN.']
save(layout_path,layout)
tech_path=ev/'technical_integrity_receipt_R03.json'; tech=json.loads(tech_path.read_text(encoding='utf-8'))
tech['visual_layout_receipt_sha256']=sha(layout_path); tech['visual_page_inspection']='PASS operator full-size inspection pages 1-18; independent visual review pending'; save(tech_path,tech)
build_path=ev/'build_receipt_R03.json'; build=json.loads(build_path.read_text(encoding='utf-8'))
build['visual_layout_receipt_path']='evidence/visual_layout_receipt_R03.json'; build['visual_layout_receipt_sha256']=sha(layout_path); save(build_path,build)
status=root/'candidate_status_R03.md'
text='''# DOCX 0053 R03 candidate status

- Candidate exact SHA-256: `cc75583238dba42eede61de990992770f8de75e96d1bcfe1313e57629551f8e8` (68,614 bytes).
- Requirement mapping: DOCX `0053` = Unique Blueprint `I12-E01`; official 157-grid sequence `056` (distinct numbering systems).
- Technical integrity: PASS; Word ZIP valid, 124 paragraphs, 29 tables, 40 unique replacement-register rows.
- Register page anchors: PASS 40/40 against the 18-page Microsoft Word PDF; register SHA-256 `65c5c4c7c8b5393481102a5e8f961640701c264454fdd53233a0dc0692909e9d`.
- Layout: `PASS_OPERATOR_FULL_PAGE_VISUAL`; all 18 pages were directly inspected at full size. PDF SHA-256 `ad9b3ce5cb6d87fb0c941635076fabb6e204ad304ce59dddbc4fd18ee92dc2e5`.
- Independent exact-SHA review: RUNNING via OpenCode CLI v2.0.29, session `ses_eb7205a43ffea89n6HYraELcwl`, requested model `opencode/nemotron-3.5-super-vl-free`; no result is claimed yet.
- Promotion / association acceptance: NOT PROMOTED; no formal association acceptance is claimed.
- R01 and R02 are retained as historical/superseded candidates with their review/build evidence. R02 was not independently reviewed. R01's 81/9-minute interpretation is superseded by the exact 0052 source and is not valid.
'''
with status.open('w',encoding='utf-8',newline='\n') as f:f.write(text)
print(json.dumps({'candidate_sha256':sha(root/'candidate'/'0053_R03.docx'),'visual_receipt_sha256':sha(layout_path),'technical_receipt_sha256':sha(tech_path),'build_receipt_sha256':sha(build_path),'status_sha256':sha(status),'full_size_pages':len(layout['full_size_pages_directly_inspected'])},indent=2))
