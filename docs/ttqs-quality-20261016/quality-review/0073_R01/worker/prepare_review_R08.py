from pathlib import Path
import hashlib,json
from pypdf import PdfReader
root=Path(r'docs/ttqs-quality-20261016/quality-review/0073_R01')
ev=root/'evidence'; render=ev/'render_R08'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
docx=root/'candidate/0073_R08.docx'; pdf=render/'0073_R08_word_export.pdf'
imgs=sorted(render.glob('page-*.png'))
receipt={
 'document_id':'0073','requirement_id':'I17A-E01','official_checkbox_serial':'080',
 'docx_sha256':sha(docx),'pdf_sha256':sha(pdf),'page_count':len(PdfReader(str(pdf)).pages),'dpi':144,
 'method':'Microsoft Word COM PDF export; Poppler 144dpi page rasterization; direct visual inspection of pages 1–20',
 'page_image_sha256':{p.name:sha(p) for p in imgs},
 'inspection_scope':{'pages_1_10':'PASS; visually inspected at full page resolution; no clipping, overlaps, or unreadable body/table text','pages_11_20':'PASS; visually inspected at full page resolution; stakeholder record tables, analysis, recommendations, neighbor boundary, blank forms and replacement register readable; no clipping or overlaps'},
 'observation':'Section 5.2.2 table header is visible on page 11; continuation on page 12 begins with H01 without a repeated column header in Word PDF output, although the DOCX header row is marked repeatable and record IDs remain visible. Adjacent-page reading remains interpretable; recorded as a minor print-navigation note, not a content or clipping defect.',
 'visual_status':'PASS_WITH_MINOR_NOTE','acceptance':'CANDIDATE ONLY; REAL=UNKNOWN/HOLD'
}
(ev/'visual_review_R08.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Fresh exact-SHA semantic bundle, separated from builder and with primary sources/data.
text=(ev/'docx_extracted_R08.md').read_text(encoding='utf-8')
blue=(root/'inputs/UNIQUE_BLUEPRINT_0073_R01.md').read_text(encoding='utf-8')
pdftext='\n'.join(PdfReader(str(Path(r'docs/ttqs-quality-20261016/quality-review/0072_R01/inputs/official_source.pdf'))).pages[4].extract_text().splitlines())
parts=[
 '# Independent semantic review request — DOCX 0073 R08',
 f'\nReview exact DOCX SHA-256: `{sha(docx)}`',
 f'Extracted text SHA-256: `{sha(ev/"docx_extracted_R08.md")}`',
 'Review route: independent OpenCode v2 CLI model `opencode/beam-free`; builder used `opencode/deepseek-v4.1-flash-free`.',
 '\nAssess the artifact from the source-bound material below. The prior R07 review is included only as a specific regression check; independently decide the final R08 verdict. Do not treat receipts or this request as proof of PASS. Review semantic content; visual inspection is separately receipted.',
 '\n## Exact mapping and primary source',
 '- Project TTQS_ONE; DOCX 0073; requirement I17A-E01; official checkbox serial 080 (not the document ID).',
 '- Official source PDF page 5 SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`.',
 '- Official requirement text: 「課後滿意度調查分析與課後檢討講師、學員、人資、部門主管等利益關係人的建議回饋紀錄。」',
 '- Current official blueprint source blob `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`; document-local unique Blueprint is included below.',
 '- Neighbor boundaries: 0072=I16-E03/078 audit process; 0074=I17A-E02/081 course closure/planning/opening recommendations.',
 '\n## Exact R07 gap to verify in R08',
 'The R07 independent reviewer returned PARTIAL because section 5.2 stakeholder records did not tie each record_id to evidence basis, limitation, responsibility role, timing, and follow-up measure. R08 is intended to address this with paired record_id tables. Independently verify all four records T01/H01/M01/M02 and identify exact section/table/row locators. Do not rely on the summary.',
 '\n## Review criteria',
 '1. Exact official purpose, document genre, document ID, requirement and checkbox mapping. 2. Complete unique Blueprint coverage and direct usability. 3. Whether section 5.2.1 and 5.2.2 connect every stakeholder record to feedback, source/evidence basis, analysis, limitation, proposed response/status, responsible role, trigger/timing, and measurable follow-up. 4. Recompute supplied survey math and cross-check case identifiers/denominators. 5. Clear SAMPLE/SYNTHETIC versus REAL/UNKNOWN/HOLD; no invented association action or real evidence. 6. Correct distinction from 0072 and 0074. 7. Adequacy of replacement register and reusable forms. 8. Any remaining material omissions or misleading inference.',
 '\nReturn exactly one verdict PASS, PARTIAL, or FAIL, bound to the exact DOCX SHA. Include concise evidence with section/table/row locators and explain every material gap. Separate semantic verdict from the visual note. Do not promote formal acceptance.',
 '\n## Official page 5 text extracted from the primary PDF\n\n'+pdftext,
 '\n## Complete unique Blueprint\n\n'+blue,
 '\n## Calculation summary\n\n```json\n'+(root/'inputs/calculation_summary_R01.json').read_text(encoding='utf-8')+'\n```',
 '\n## Learner scores CSV\n\n```csv\n'+(root/'inputs/learner_scores_R01.csv').read_text(encoding='utf-8')+'\n```',
 '\n## Returned forms CSV\n\n```csv\n'+(root/'inputs/returned_forms_R01.csv').read_text(encoding='utf-8')+'\n```',
 '\n## Stakeholder feedback CSV\n\n```csv\n'+(root/'inputs/stakeholder_feedback_R01.csv').read_text(encoding='utf-8')+'\n```',
 '\n## Question summary CSV\n\n```csv\n'+(root/'inputs/question_summary_R01.csv').read_text(encoding='utf-8')+'\n```',
 '\n## Synthetic replacement register CSV\n\n```csv\n'+(root/'inputs/synthetic_replacement_register_R01.csv').read_text(encoding='utf-8')+'\n```',
 '\n## Candidate extracted text (complete)\n\n'+text
]
bundle='\n'.join(parts)
(ev/'semantic_review_bundle_R08.md').write_text(bundle,encoding='utf-8')
print(json.dumps({'docx_sha256':sha(docx),'pdf_sha256':sha(pdf),'pages':len(PdfReader(str(pdf)).pages),'pngs':len(imgs),'bundle_bytes':len(bundle.encode()),'visual_status':receipt['visual_status'],'bundle_sha256':sha(ev/'semantic_review_bundle_R08.md')},ensure_ascii=False,indent=2))
