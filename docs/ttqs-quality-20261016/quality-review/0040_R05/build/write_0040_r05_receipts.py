from pathlib import Path
import hashlib,json
P=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0040_R05')
R04=P.parent/'0040_R04'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
candidate=P/'candidate/0040_R05.docx'; pdf=P/'evidence/render/candidate.pdf'; register=P/'evidence/SYNTHETIC_REPLACEMENT_REGISTER_R05.csv'
render=P/'evidence/render'; tech=P/'evidence/qa/0040_technical_review_r05_exact.json'
tech_obj=json.loads(tech.read_text(encoding='utf-8'))
visual={
 'project_id':'TTQS_ONE','doc_id':'0040','revision':'R05','review_type':'primary_visual_layout_review',
 'candidate_sha256':sha(candidate),'rendered_pdf_sha256':sha(pdf),'page_count':8,
 'direct_visual_inspection_pages':[1,2,3,4,5,6,7,8],
 'renderer':'Microsoft Word COM ExportAsFixedFormat followed by bundled Poppler pdftoppm at 140 dpi; canonical render_docx.py could not resolve soffice.exe in this Windows environment.',
 'render_receipt_path':'evidence/render/export_receipt.json','render_receipt_sha256':sha(render/'export_receipt.json'),
 'page_png_sha256':{str(i):sha(render/f'page-{i}.png') for i in range(1,9)},
 'page_findings':{
  '1':'Title, official requirement and source, SAMPLE boundary and five-step workflow readable; no clipping.',
  '2':'Adjacent document boundaries, design flow and coverage formula readable; no table overflow.',
  '3':'Four-dimension matrix and 0/1/2 behavior anchors readable; all columns visible.',
  '4':'Five synthetic paired score rows and calculation table readable; all columns visible.',
  '5':'Completed D04 example, exception handling and handoff tables readable; no overlap.',
  '6':'Synthetic D04 follow-up, authority boundary and course-design context readable; no clipping.',
  '7':'User-facing version/effectivity guidance and one-row revision summary readable; internal hashes, IDs and reviewer history are absent.',
  '8':'Task-based operating guide continues under a repeated table header; rows and footer are visible with no clipping or overlap.'
 },
 'layout_findings':[], 'primary_visual_result':'PASS','promotion_status':'NOT_PROMOTED'
}
(P/'evidence/qa/0040_visual_review_r05_primary.json').write_text(json.dumps(visual,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
prov={
 'project_id':'TTQS_ONE','doc_id':'0040','revision':'R05','requirement_id':'I08-E03','official_checkbox_sequence':'040',
 'candidate_sha256':sha(candidate),'parent_candidate_r04_sha256':sha(R04/'candidate/0040_R04.docx'),
 'official_source_pdf_sha256':'805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709',
 'blueprint_file_sha256':'406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e',
 'blueprint_row_sha256':'ab080a2e6d85cc13a706f0c10bda7c208ddc191a1fea20a670fd5a174ab14943',
 'source_map_sha256':'405b987797d1558ecac182cea8e1adfbd1aead7754c880db32db43c235d5024e',
 'register_sha256':sha(register),'register_rows':39,'rendered_pdf_sha256':sha(pdf),'technical_receipt_sha256':sha(tech),
 'visual_receipt_sha256':sha(P/'evidence/qa/0040_visual_review_r05_primary.json'),
 'parent_r04_verdict':'PARTIAL','repair_scope':['Replace evaluator-facing internal control and line-by-line audit tables on printed pages 7-8 with user-facing effectivity guidance and task-based operating navigation.','Correct official source locator and three synthetic register locator precision issues; bind all 39 rows to the new exact candidate SHA.'],
 'unchanged_scope':'R04 substantive pages 1-6 have identical normalized extracted text in R05; R04 assessment vectors, thresholds, calculations, sample dates and D04 follow-up facts are unchanged.',
 'authoring_route':'Local targeted python-docx edit by the current Codex task; no institutional authorship or approval claim.',
 'renderer':'Microsoft Word COM ExportAsFixedFormat plus bundled Poppler pdftoppm at 140 dpi; render_docx.py attempt could not run because soffice.exe is absent from PATH.',
 'technical_status':'PASS_TECHNICAL','primary_visual_status':'PASS','independent_semantic_verdict':'PENDING',
 'independent_semantic_review_route':'Not yet dispatched; separate reviewer must inspect this exact SHA after GitHub sync.',
 'sample_state':'SAMPLE_SYNTHETIC_ONLY; no association approval, course execution, attendance, learner scores, outcomes, signatures or third-party originals claimed.',
 'candidate_state':'CANDIDATE_NOT_PROMOTED','formal_acceptance':'NOT_GRANTED'
}
(P/'evidence/qa/0040_R05_provenance.json').write_text(json.dumps(prov,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
progress={
 'project_id':'TTQS_ONE','doc_id':'0040','revision':'R05','requirement_id':'I08-E03','official_checkbox_sequence':'040',
 'status':'CANDIDATE_TECHNICAL_AND_PRIMARY_VISUAL_PASS_PENDING_INDEPENDENT_SEMANTIC_REVIEW',
 'candidate_path':'candidate/0040_R05.docx','candidate_sha256':sha(candidate),
 'parent_candidate_path':'../0040_R04/candidate/0040_R04.docx','parent_candidate_sha256':sha(R04/'candidate/0040_R04.docx'),
 'register_path':'evidence/SYNTHETIC_REPLACEMENT_REGISTER_R05.csv','register_sha256':sha(register),'register_rows':39,'register_rows_bound_to_candidate_sha':39,'register_rows_with_validated_printed_anchors':tech_obj['register_rows_with_validated_printed_anchors'],
 'rendered_pdf_path':'evidence/render/candidate.pdf','rendered_pdf_sha256':sha(pdf),'page_count':8,
 'technical_status':'PASS','technical_receipt_path':'evidence/qa/0040_technical_review_r05_exact.json','technical_receipt_sha256':sha(tech),
 'primary_visual_status':'PASS','visual_receipt_path':'evidence/qa/0040_visual_review_r05_primary.json','visual_receipt_sha256':sha(P/'evidence/qa/0040_visual_review_r05_primary.json'),
 'independent_semantic_verdict':'PENDING','independent_semantic_review_path':None,'independent_semantic_review_sha256':None,
 'sample_state':'SAMPLE_SYNTHETIC_ONLY','candidate_state':'CANDIDATE_NOT_PROMOTED','formal_acceptance':'NOT_GRANTED',
 'repair_summary':'P.7-8 user-facing rewrite; official source and register locators corrected; p.1-6 score data, thresholds and D04 facts retained.',
 'known_limitations':['Fresh independent semantic exact-SHA review has not yet been dispatched or completed.','Writer identity is the current Codex task; reviewer must be a separate active agent.'],
 'github_sync_status':'PENDING_INITIAL_R05_SYNC'
}
(P/'PROGRESS.json').write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
readme=f'''# DOCX 0040 R05 — targeted repair

**State:** candidate only. Technical and primary visual checks passed; independent semantic exact-SHA review is pending. No promotion or formal acceptance is granted.

- Official requirement: I08-E03 / evidence-table sequence 040; training-institution evidence table PDF p.3.
- Unique Blueprint row SHA-256: `ab080a2e6d85cc13a706f0c10bda7c208ddc191a1fea20a670fd5a174ab14943`.
- R05 candidate SHA-256: `{sha(candidate)}`.
- Parent R04 candidate SHA-256: `{sha(R04/'candidate/0040_R04.docx')}`; R04 is preserved at `../0040_R04/` with exact-SHA PARTIAL review and raw reviewer reply.
- Synthetic replacement register: 39/39 rows bound to the R05 exact SHA; register SHA-256 `{sha(register)}`.
- Word render: 8 pages; PDF SHA-256 `{sha(pdf)}`. All eight page images were directly inspected. Pages 1–6 have identical normalized extracted text to R04. Technical receipt reports 39/39 current printed-page anchors.
- The R04 repair was limited to pages 7–8 and the documented locator gaps. Scores, thresholds, formulas and D04 sample facts remain unchanged.
- The body now provides use/effectivity guidance and a task-based operating index. Internal hashes, item IDs, reviewer history and line-by-line audit mappings stay in sidecars.
- The example is SAMPLE/SYNTHETIC only. No association approval, actual course execution, attendance, learner scores, outcomes, signature or third-party original is claimed.

**Quality evidence**

- Technical: PASS — `evidence/qa/0040_technical_review_r05_exact.json`.
- Primary visual: PASS — `evidence/qa/0040_visual_review_r05_primary.json`; direct inspection covered printed pages 1–8 at 140 dpi.
- Independent semantic: PENDING — must review the exact candidate SHA above after GitHub synchronization.
- Candidate state: CANDIDATE_NOT_PROMOTED; formal acceptance NOT_GRANTED.

The canonical LibreOffice renderer was unavailable because `soffice.exe` is not installed on PATH. Rendering used Microsoft Word COM `ExportAsFixedFormat` and bundled Poppler `pdftoppm`; the source DOCX SHA remained unchanged during rendering.
'''
(P/'README.md').write_text(readme,encoding='utf-8')
manifest_path=P/'artifact_manifest.json'; files=[]
for f in sorted(P.rglob('*')):
 if f.is_file() and f not in {manifest_path,P/'PROGRESS.json'}:
  files.append({'path':f.relative_to(P).as_posix(),'bytes':f.stat().st_size,'sha256':sha(f)})
manifest={'project_id':'TTQS_ONE','bundle':'0040_R05','manifest_scope':'All files except top-level artifact_manifest.json and mutable PROGRESS.json.','hash_method':'SHA-256 over exact files and Git blobs; .gitattributes prevents text normalization.','files':files}
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'candidate_sha256':sha(candidate),'pdf_sha256':sha(pdf),'register_sha256':sha(register),'technical_sha256':sha(tech),'visual_sha256':sha(P/'evidence/qa/0040_visual_review_r05_primary.json'),'manifest_entries':len(files),'status':progress['status']},ensure_ascii=False,indent=2))
