from pathlib import Path
from zipfile import ZipFile
from hashlib import sha256
import csv, json, datetime, textwrap
from docx import Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.text.paragraph import Paragraph
from docx.table import Table

BASE=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0104_I18-E11_SOURCE_PREP_20261022')
PKG=Path(r'E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0104_I18-E11_R15_20261022')
DOCX=BASE/'candidate'/'0104__證照獲取率_分析報告_R16.docx'
PDF=BASE/'visual'/'0104_R16'/'0104_R16_word_native.pdf'
RASTER=BASE/'evidence'/'raster_receipt_0104_R16.json'
VISUAL=BASE/'evidence'/'visual_qa_receipt_0104_R16.json'
REVIEW=PKG/'review'/'R16'
REVIEW.mkdir(parents=True,exist_ok=True)

def digest(path): return sha256(path.read_bytes()).hexdigest()

def extract_in_order(doc):
    parts=[]; ti=0
    for child in doc.element.body.iterchildren():
        if isinstance(child,CT_P):
            value=Paragraph(child,doc).text.strip()
            if value: parts.append(value)
        elif isinstance(child,CT_Tbl):
            ti+=1; table=Table(child,doc)
            parts.append(f'[[TABLE {ti}: {len(table.rows)} rows x {len(table.columns)} columns]]')
            for row in table.rows:
                parts.append(' | '.join(cell.text.replace('\n',' / ').strip() for cell in row.cells))
    return '\n'.join(parts),ti

raster=json.loads(RASTER.read_text(encoding='utf-8'))
assert len(raster['pages'])==36 and raster['pdf_sha256']==digest(PDF)
visual_findings={7:'Continuation text is readable; lower half is intentionally spacious.',13:'Two continuation bullets are readable; substantial whitespace remains.',25:'Three final rows of the fact register are readable; the page is sparse.',36:'Final two rows of the version table are readable; the page is sparse.'}
visual_pages=[]
for p in raster['pages']:
    visual_pages.append({
      'page':p['page'],'image_sha256':p['sha256'],'width_px':p['width_px'],'height_px':p['height_px'],
      'direct_full_page_inspection':True,
      'finding':visual_findings.get(p['page'],'Readable at rendered resolution; no clipping, overlap, cut-off table row, or unreadable text observed.')
    })
visual_receipt={
 'receipt_id':'TTQS-0104-VISUAL-QA-R16','observed_at_tpe':datetime.datetime.now().astimezone().isoformat(),
 'doc_id':'0104','requirement_id':'I18-E11','official_checkbox_serial':'112',
 'candidate_docx_sha256':digest(DOCX),'pdf_sha256':digest(PDF),'page_count':len(raster['pages']),
 'inspection_method':'All 36 page PNGs were opened and directly inspected at original rendered resolution in local image review; this is a visual layout check, not an independent semantic review.',
 'visual_result':'PASS_WITH_NONBLOCKING_WHITESPACE_OBSERVATIONS',
 'blocking_layout_defects':[],
 'nonblocking_observations':['Pages 7 and 13 contain short continuation text with large remaining whitespace.','Page 25 contains the final three register rows and is sparse.','Page 36 contains the final two version-table rows and is sparse.'],
 'pages':visual_pages,
 'scope_limit':'No human association usability trial; no REAL association evidence; no claim of formal acceptance.'
}
VISUAL.write_text(json.dumps(visual_receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

doc=Document(str(DOCX)); body,table_count=extract_in_order(doc)
source=PKG/'source'/'SOURCE_PACKET_0104_I18-E11_R01.md'
blueprint=PKG/'source'/'UNIQUE_BLUEPRINT_0104_I18-E11_R01.jsonl'
crosswalk=PKG/'source'/'crosswalk_row_0104_I18-E11.csv'
prior=PKG/'review'/'R15'/'opencode_review_final_R15.md'
inputs={
 'candidate_docx':DOCX,'candidate_extracted_text':None,'official_source_packet':source,
 'unique_blueprint':blueprint,'crosswalk_row':crosswalk,'prior_independent_review':prior,
 'technical_qa':BASE/'evidence'/'technical_qa_receipt_0104_R16.json',
 'visual_qa':VISUAL,'word_export':BASE/'evidence'/'word_export_receipt_0104_R16.json',
 'synthetic_register':BASE/'evidence'/'synthetic_replacement_register_0104_R16.csv'
}
packet_parts=[
 '# Independent semantic review packet — DOCX 0104 R16',
 f"work_id: TTQS-0104-I18-E11-R16-INDEPENDENT-REVIEW-20261022\ndoc_id: 0104\nrequirement_id: I18-E11\nofficial_checkbox_serial: 112\ncandidate_docx_sha256: {digest(DOCX)}\nreviewer_scope: TEXT_ONLY; the independent reviewer must not claim to inspect DOCX page images.",
 '''## Review instructions
You are an independent reviewer, not the Builder. Assess the exact candidate text below against the included official source packet and unique Blueprint. Return a concise structured result with PASS, PARTIAL, or FAIL; the exact candidate SHA; blocking defects with exact section/table/row locators; nonblocking findings; and explicit scope limits. Do not edit files, call tools, infer REAL facts, or trust any Builder self-report. Verify the document identity and genre; title-blind purpose; practical use by a volunteer training association and TTQS evaluator; definitions and denominators; arithmetic; cross-table and date consistency; complete SAMPLE/SYNTHETIC facts and replacement-register coverage; unknown REAL evidence boundary; and absence of invented approvals, signatures, participants, certificates, third-party originals, or association decisions. Compare the requirement with the available adjacent mapping for I18-E10 and I18-E12; if authoritative source for a neighbor is absent, state UNKNOWN rather than fabricate a comparison.

### Prior exact-SHA R15 findings to close
R15 verdict was PARTIAL with zero blocking findings and ten residual items. Check these exact changes in R16 without assuming they are fixed: (1) T-13 unique ranks/order/tie rule and F-GP-01..05 locators; (2) distinct fact keys for A/B multiplication chains; (3) fact key for sample retention suggestion; (4) T-12 judgment cells linked to cohort-rate and threshold keys, with optional yield clearly reference-only; (5) FN-2 points to T-10/P8, not T-12; (6) T-17 R-1 separates the official source locator from worked proof; (7) change propagation lists dependent locations and mandates recomputation; (8) the “three cases” conclusion distinguishes A from B; (9) SRC-C1 is an unformed-cohort synthetic control record, not an association or registration-system record; (10) the five fixed rates are named explicitly and optional yield separated. The prior report is provided below as history only; independently inspect the R16 content.

### Evidence limits
The provided technical receipt is deterministic checking only. The visual receipt records a separate direct 36-page visual inspection; this review is text-only and must not upgrade or restate that scope. All demonstration information remains synthetic; REAL facts and formal acceptance are unknown/ungranted.
''',
 '## Current official source packet\n'+source.read_text(encoding='utf-8-sig'),
 '## Current unique Blueprint row\n'+blueprint.read_text(encoding='utf-8-sig'),
 '## Crosswalk row\n'+crosswalk.read_text(encoding='utf-8-sig'),
 '## Prior independent R15 review (historical input; not authority)\n'+prior.read_text(encoding='utf-8'),
 '## Current R16 candidate text extracted from DOCX in document order\n'+body
]
packet='\n\n'.join(packet_parts)
packet_path=REVIEW/'review_packet_0104_R16.md'
packet_path.write_text(packet,encoding='utf-8')
manifest={
 'receipt_id':'TTQS-0104-REVIEW-INPUT-MANIFEST-R16','created_at_tpe':datetime.datetime.now().astimezone().isoformat(),
 'doc_id':'0104','requirement_id':'I18-E11','official_checkbox_serial':'112',
 'candidate_docx_sha256':digest(DOCX),'candidate_bytes':DOCX.stat().st_size,
 'candidate_table_count':table_count,'reviewer_scope':'TEXT_ONLY',
 'packet_path':str(packet_path),'packet_sha256':digest(packet_path),'packet_bytes':packet_path.stat().st_size,
 'inputs':{k:{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size} for k,p in inputs.items() if p is not None},
 'visual_pages':len(raster['pages']),'visual_result':visual_receipt['visual_result']
}
manifest_path=REVIEW/'review_input_manifest_0104_R16.json'
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'candidate_sha256':manifest['candidate_docx_sha256'],'packet_sha256':manifest['packet_sha256'],'packet_bytes':manifest['packet_bytes'],'manifest_sha256':digest(manifest_path),'visual_receipt_sha256':digest(VISUAL),'pages':len(raster['pages']),'tables':table_count},ensure_ascii=False,indent=2))
