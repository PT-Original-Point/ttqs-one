from pathlib import Path
import hashlib, json

ROOT=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review')
R05=ROOT/'0040_R05'; P=ROOT/'0040_R06'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
doc=P/'candidate/0040_R06.docx'; pdf=P/'evidence/render/candidate.pdf'
register=P/'evidence/SYNTHETIC_REPLACEMENT_REGISTER_R06.csv'
tech=P/'evidence/qa/0040_technical_review_r06_exact.json'
render=P/'evidence/render'; candidate_sha=sha(doc); pdf_sha=sha(pdf); register_sha=sha(register)
tech_obj=json.loads(tech.read_text(encoding='utf-8'))
visual={
 'project_id':'TTQS_ONE','doc_id':'0040','revision':'R06','review_type':'primary_visual_layout_review',
 'candidate_sha256':candidate_sha,'rendered_pdf_sha256':pdf_sha,'page_count':9,
 'direct_visual_inspection_pages':[1,2,3,4,5,6,7,8,9],
 'renderer':'Microsoft Word COM ExportAsFixedFormat followed by bundled Poppler pdftoppm at 140 dpi; canonical render_docx.py could not resolve soffice.exe in this Windows environment.',
 'render_receipt_path':'evidence/render/export_receipt.json','render_receipt_sha256':sha(render/'export_receipt.json'),
 'page_png_sha256':{str(i):sha(render/f'page-{i}.png') for i in range(1,10)},
 'page_findings':{
  '1':'Opening explains intended users, use timing, official requirement, example boundary and five-step work sequence; all text and table cells visible.',
  '2':'Source boundaries and six-step evaluation flow are clear; no clipped rows or missing glyphs.',
  '3':'K1-K4 matrix now has a synthetic evidence index and fillable controlled file/attachment/page/version fields; the dense cells remain readable.',
  '4':'K3-K4 matrix continuation and scoring rule are visible under the repeated header; no overlap or truncation.',
  '5':'Five paired examples and calculations remain readable; all case rows and denominator notes are present.',
  '6':'D04 example includes a bordered original-evidence-location row; exception table starts below with its own header.',
  '7':'Exception and handoff tables continue with repeated headers; the D04 follow-up status is legible and explicitly unexecuted.',
  '8':'User-facing effectivity, authority and sample boundaries remain clear.',
  '9':'Operating guide continuation repeats the table header and remains readable; no clipping or overlap.'
 },
 'layout_findings':['Page 4 is intentionally a short continuation of the K1-K4 matrix and scoring rule after the enlarged evidence-locator cells; it contains no blank page or clipped content.'],
 'primary_visual_result':'PASS','candidate_state':'CANDIDATE_NOT_PROMOTED','formal_acceptance':'NOT_GRANTED'
}
visual_path=P/'evidence/qa/0040_visual_review_r06_primary.json'
visual_path.write_text(json.dumps(visual,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
prov={
 'project_id':'TTQS_ONE','doc_id':'0040','revision':'R06','requirement_id':'I08-E03','official_checkbox_sequence':'040',
 'candidate_sha256':candidate_sha,'parent_r05_candidate_sha256':sha(R05/'candidate/0040_R05.docx'),
 'parent_r05_verdict':'PARTIAL','parent_r05_raw_review_sha256':sha(R05/'evidence/qa/0040_semantic_review_r05_crossreview_raw.md'),
 'official_source_pdf_sha256':sha(P/'inputs/inputs/official_evidence_table.pdf'),
 'blueprint_row_sha256':'ab080a2e6d85cc13a706f0c10bda7c208ddc191a1fea20a670fd5a174ab14943',
 'source_map_sha256':sha(P/'inputs/inputs/source_requirement_map.csv'),
 'synthetic_register_sha256':register_sha,'synthetic_register_rows':40,
 'rendered_pdf_sha256':pdf_sha,'page_count':9,'technical_receipt_sha256':sha(tech),'visual_receipt_sha256':sha(visual_path),
 'repair_scope':[
  'R05-F01: added a synthetic-only evidence index and explicit controlled file ID, attachment/page and version fields to each K1-K4 matrix row and the filled D04 form.',
  'R05-F02: separated the optional 30-day authorization rule (printed p.1) from the D04 rescore-not-executed status (printed p.7) in the replacement register.',
  'R05-F03: updated docProps/core.xml description to R06 and revision to 6.'
 ],
 'unchanged_scope':'The five paired synthetic score vectors, thresholds, formulas and case dates are unchanged from reviewed R05. The R06 candidate adds the evidence-location instructions and corrects metadata only at the specific reviewed loci.',
 'source_audit':{
  'command':'TTQS_ONE_EXTERNAL_AUDIT_FINDINGS_20261016_CONTINUE',
  'path':'docs/ttqs-quality-20261016/06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md',
  'observed_live_commit':'0c0a3f283bd78af37d22355a4ed9e0b5c49fd49d',
  'live_blob_sha':'70449889fd464106fe204496004bee13018d4a51',
  'disposition':'APPLIED_PARTIAL; R05 semantic PARTIAL recorded; R06 repairs applied; other 06 findings remain subject to their own live evidence checks.'
 },
 'authoring_route':'Local targeted python-docx repair plus a single-element OOXML core-properties patch by the current task; no institutional authorship or approval is claimed.',
 'renderer':'Microsoft Word COM ExportAsFixedFormat plus bundled Poppler pdftoppm at 140 dpi; render_docx.py could not use the canonical LibreOffice route because soffice.exe is unavailable.',
 'technical_status':'PASS_TECHNICAL','primary_visual_status':'PASS','independent_semantic_verdict':'PENDING',
 'independent_semantic_review_route':'Separate read-only cross-review agent, to be bound to the exact R06 SHA after GitHub readback.',
 'sample_state':'SAMPLE_SYNTHETIC_ONLY; SYN-EV-0039-01 is a synthetic index and no external original is attached.',
 'candidate_state':'CANDIDATE_NOT_PROMOTED','formal_acceptance':'NOT_GRANTED'
}
(P/'evidence/qa/0040_R06_provenance.json').write_text(json.dumps(prov,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
progress={
 'project_id':'TTQS_ONE','doc_id':'0040','revision':'R06','requirement_id':'I08-E03','official_checkbox_sequence':'040',
 'status':'CANDIDATE_TECHNICAL_AND_PRIMARY_VISUAL_PASS_PENDING_INDEPENDENT_SEMANTIC_REVIEW',
 'candidate_path':'candidate/0040_R06.docx','candidate_sha256':candidate_sha,
 'parent_candidate_path':'../0040_R05/candidate/0040_R05.docx','parent_candidate_sha256':sha(R05/'candidate/0040_R05.docx'),'parent_semantic_verdict':'PARTIAL',
 'register_path':'evidence/SYNTHETIC_REPLACEMENT_REGISTER_R06.csv','register_sha256':register_sha,'register_rows':40,'register_rows_bound_to_candidate_sha':40,
 'register_rows_with_validated_printed_anchors':'See technical receipt; all 40 facts are hash-bound; all page-bound facts have corrected printed-page locators and rendered-page anchor checks.',
 'rendered_pdf_path':'evidence/render/candidate.pdf','rendered_pdf_sha256':pdf_sha,'page_count':9,
 'technical_status':'PASS','technical_receipt_path':'evidence/qa/0040_technical_review_r06_exact.json','technical_receipt_sha256':sha(tech),
 'primary_visual_status':'PASS','visual_receipt_path':'evidence/qa/0040_visual_review_r06_primary.json','visual_receipt_sha256':sha(visual_path),
 'independent_semantic_verdict':'PENDING','independent_semantic_review_path':None,'independent_semantic_review_sha256':None,
 'sample_state':'SAMPLE_SYNTHETIC_ONLY','candidate_state':'CANDIDATE_NOT_PROMOTED','formal_acceptance':'NOT_GRANTED',
 'repair_summary':'Applied only R05-F01 usable evidence locators, R05-F02 split register facts and R05-F03 R06 metadata. The user-facing evidence pointer is synthetic and no original is fabricated.',
 'known_limitations':['Independent exact-SHA semantic review has not yet returned.','Original evidence files are absent by design; the SAMPLE locator is not an attached record.'],
 'source_audit':prov['source_audit'],
 'github_sync_status':'PENDING_INITIAL_R06_SYNC'
}
(P/'PROGRESS.json').write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
readme=f'''# DOCX 0040 R06 — targeted semantic repairs

**State:** candidate only. Technical and direct primary visual checks pass. Independent semantic review on this exact SHA is pending; no promotion or formal acceptance is granted.

- Official requirement: I08-E03 / evidence-table sequence 040; unique Blueprint row SHA-256 `ab080a2e6d85cc13a706f0c10bda7c208ddc191a1fea20a670fd5a174ab14943`.
- Candidate SHA-256: `{candidate_sha}`. Parent R05 SHA-256: `{sha(R05/'candidate/0040_R05.docx')}`; R05 remains preserved with its PARTIAL review.
- Repairs are limited to the three R05 findings: usable evidence ID/location fields in the p.3 matrix and p.6 D04 example; separate locators for the p.1 optional 30-day rule and the p.7 D04 rescore status; R06 document properties (description and revision 6).
- The visible index `SYN-EV-0039-01` is a SAMPLE/SYNTHETIC pointer inside this tool and is not an external file. The form instructs users to enter a controlled file ID, attachment/page and version only when an authorized original exists.
- Register: 40 unique facts, all bound to the R06 candidate SHA; file `evidence/SYNTHETIC_REPLACEMENT_REGISTER_R06.csv`, SHA-256 `{register_sha}`.
- Technical: PASS — ZIP/XML integrity, 9 rendered pages, font minima 10.5 pt body / 9.5 pt tables, exact register binding, separated locators and recalculated figures (17/5, 31/5, 14/5, 4/5 = 80%). See `evidence/qa/0040_technical_review_r06_exact.json`.
- Primary visual: PASS — all nine page images directly inspected at 140 dpi. PDF SHA-256 `{pdf_sha}`. Page 4 is a short continuation after the expanded evidence matrix; no blank page, clipping, overlap or broken table is present.
- Independent semantic review: PENDING, to be bound to the exact R06 SHA after remote byte readback.

All case facts remain SAMPLE/SYNTHETIC. No association approval, actual assessment, attendance, real outcome, signature or third-party original is claimed.
'''
(P/'README.md').write_text(readme,encoding='utf-8')

# Mark the already-read R05 semantic review synchronization as exact-readback verified.
r05_progress_path=R05/'PROGRESS.json'
r05_progress=json.loads(r05_progress_path.read_text(encoding='utf-8'))
r05_progress['github_sync_status']='REMOTE_READBACK_PASS_FOR_R05_PARTIAL_REVIEW'
r05_progress['remote_readback']={
 'commit':'0c0a3f283bd78af37d22355a4ed9e0b5c49fd49d',
 'verified_paths':[
  'quality-review/0040_R05/evidence/qa/0040_semantic_review_r05_crossreview_raw.md',
  'quality-review/0040_R05/evidence/qa/0040_semantic_review_r05_exact.json',
  'quality-review/0040_R05/PROGRESS.json'
 ],
 'method':'Fresh fetch, resolve Git blob and compare exact raw bytes and SHA-256; all equal.'
}
r05_progress_path.write_text(json.dumps(r05_progress,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

manifest_path=P/'artifact_manifest.json'; files=[]
for f in sorted(P.rglob('*')):
    if f.is_file() and f not in {manifest_path,P/'PROGRESS.json'}:
        files.append({'path':f.relative_to(P).as_posix(),'bytes':f.stat().st_size,'sha256':sha(f)})
manifest={'project_id':'TTQS_ONE','bundle':'0040_R06','manifest_scope':'All R06 files except top-level artifact_manifest.json and mutable PROGRESS.json.','hash_method':'SHA-256 over exact file bytes and Git blobs; no real or protected source records are included.','files':files}
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'candidate_sha256':candidate_sha,'pdf_sha256':pdf_sha,'register_sha256':register_sha,'technical_receipt_sha256':sha(tech),'visual_receipt_sha256':sha(visual_path),'provenance_sha256':sha(P/'evidence/qa/0040_R06_provenance.json'),'manifest_files':len(files),'semantic':'PENDING'},ensure_ascii=False,indent=2))
