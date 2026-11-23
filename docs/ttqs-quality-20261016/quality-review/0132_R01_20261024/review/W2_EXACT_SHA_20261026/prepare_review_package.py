from pathlib import Path
from hashlib import sha256,sha1
import json
root=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0132_I19-E21_SOURCE_PREP_R01_20261024')
rev=root/'review'/'W2_EXACT_SHA_20261026'
read=lambda p:(root/p).read_text(encoding='utf-8')
source={
 'source_packet':root/'source'/'SOURCE_PACKET_0132_I19-E21_R01.md',
 'unique_blueprint':root/'source'/'UNIQUE_BLUEPRINT_0132_I19-E21_R01.md',
 'official_extract':root/'source'/'OFFICIAL_PAGE8_I19-L3_EXTRACT_R01.txt',
 'neighbor_crosswalk':root/'source'/'INTERNAL_CROSSWALK_I19-E21_NEIGHBORS_R01.csv',
}
qa={
 'content_qa':root/'qa'/'CONTENT_QA_0132_R01.json',
 'technical_qa':root/'qa'/'TECHNICAL_QA_0132_R01.json',
 'visual_qa':root/'qa'/'WORD_RENDER_VISUAL_QA_0132_R01.json',
 'remote_readback':root/'qa'/'GITHUB_RAW_BYTE_READBACK_0132_R01.json',
}
docx=root/'candidate'/'0132_I19-E21_CANDIDATE_R01.docx'
payload=rev/'0132_R01_EXACT_SHA_SEMANTIC_PAYLOAD_V2.txt'
media=[rev/'embedded_media'/'image1.png',rev/'embedded_media'/'image2.png']
sha=lambda b:sha256(b).hexdigest()
gitblob=lambda b:sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
source_hashes={k:{'path':str(v),'sha256':sha(v.read_bytes()),'git_blob':gitblob(v.read_bytes())} for k,v in source.items()}
qa_hashes={k:{'path':str(v),'sha256':sha(v.read_bytes()),'git_blob':gitblob(v.read_bytes())} for k,v in qa.items()}
chart_notes='''\n\n[VISUALLY INSPECTED EMBEDDED CHARTS; TRANSCRIBED FROM DOCX MEDIA]\nimage1.png SHA-256='''+sha(media[0].read_bytes())+''': title Pooled defective-unit rate; Before n=66, D=13/N=66, 19.7%; After n=70, D=8/N=70, 11.4%; footer SAMPLE/SYNTHETIC — not association performance.\nimage2.png SHA-256='''+sha(media[1].read_bytes())+''': title Batch trend (SAMPLE); B1 20.0%, B2 20.8%, B3 18.2%, A1 14.3%, A2 12.0%, A3 8.3%; vertical annotation “training + tool/material change”; footer SAMPLE/SYNTHETIC — boundary is not evidence of causality.\n'''
intro='''TTQS ONE | INDEPENDENT TEXT-SEMANTIC REVIEW | EXACT CANDIDATE SHA\nReview one unchanged artifact only. Do not edit or rebuild files. Do not invoke tools, Computer Use, external actions, or another model. This is a text-semantic review; separate existing Word visual QA is evidence context, not your own visual review.\n\nLIVE SOURCE/ARTIFACT BINDING\nPR #92 branch live HEAD at dispatch preparation: 1db5e97bd173cfe802aba752198204d97bf90270 (also read with native git ls-remote). doc_id=0132; internal requirement I19-E21; project 157 index 145, I19-L3; official PDF p.8; printed checkbox serial UNKNOWN. Exact candidate DOCX SHA-256=e2f263c2c130d1939ebdaab1a253700935c54c8a26c937b8a77e7000a9a2d925; GitHub candidate Git blob 7ada5d133193314794700661ad7ca309da9c02dc. The DOCX is 157,427 bytes locally. Candidate status only; formal acceptance NOT_GRANTED; REAL evidence UNKNOWN.\nSource packet, unique Blueprint, official extract and neighbor crosswalk are reproduced below from local files whose Git blobs were freshly matched to the same live branch head. The source packet records an older build-base commit 59614bf... as historical provenance; do not treat it as current HEAD.\n\nCHECK EXACT DOC_ID/REQUIREMENT/GENRE; official literal and source page; distinguish 0132 from 0131 (student credential/employment) and 0133 (training sessions/attendees); apply the unique Blueprint rather than generic “outcome rate” rules. Determine if title-blind content unmistakably concerns individual product defective-unit trend.\n\nREVIEW THE COMPLETE CANDIDATE BODY BELOW. Assess usable procedures, actual forms and filled examples, data definitions, denominator/coverage, deduplication, defective-unit versus defect-event distinction, trend and confounders, concrete follow-up, HOLD/REJECT gates, full SAMPLE/SYNTHETIC replacement register and clear empty REAL slots. Recalculate every headline result and batch/reason sums. Do not infer training causality, association performance, approval, statistical significance, or official pass threshold. Identify each finding with exact section/table/row locator and severity. Verdict must be PASS, PARTIAL, or FAIL for semantic scope, with concise evidence. No generic approval language.\n\nNUMERIC CHECKPOINTS (recalculate independently): pre 13/66=19.69697% (19.7%); post 8/70=11.42857% (11.4%); post−pre = −8.26840 percentage points (−8.27 pp); relative decline = 41.9780% (42.0%); D changes 13→8 (−38.5%); N changes 66→70 (+6.1%). Primary-reason totals must equal 13 pre and 8 post. All values remain SYNTHETIC. Tool and material batch changed post-training, so no causal claim. Chart images were separately opened and visually transcribed; image hashes and text are below.\n\nRESPONSE FORMAT\n1) Verdict PASS/PARTIAL/FAIL and exact candidate SHA.\n2) Requirement identity and genre.\n3) Findings table: severity | exact locator | evidence/impact | correction needed. If none, say none.\n4) Math/cross-document/SAMPLE-REAL checks.\n5) Limitations: text-semantic only; do not assert visual inspection or true model identity.\n\n[OFFICIAL EXTRACT]\n'''+read(Path('source/OFFICIAL_PAGE8_I19-L3_EXTRACT_R01.txt'))+'\n[NEIGHBOR CROSSWALK]\n'+read(Path('source/INTERNAL_CROSSWALK_I19-E21_NEIGHBORS_R01.csv'))+'\n[SOURCE PACKET]\n'+read(Path('source/SOURCE_PACKET_0132_I19-E21_R01.md'))+'\n[UNIQUE BLUEPRINT]\n'+read(Path('source/UNIQUE_BLUEPRINT_0132_I19-E21_R01.md'))+'\n[EXACT CANDIDATE TEXT AND EXTRACTION METADATA]\n'+payload.read_text(encoding='utf-8')+chart_notes
prompt=intro
units=len(prompt.encode('utf-16-le'))//2
if units>28500: raise SystemExit(f'Prompt too long for safe Windows argv: {units} UTF-16 units')
pp=rev/'REVIEW_PROMPT.txt'; pp.write_text(prompt,encoding='utf-8',newline='\n')
manifest={
 'project_id':'TTQS_ONE','doc_id':'0132','requirement_id':'I19-E21','review_scope':'independent exact-SHA text-semantic review only',
 'candidate_sha256':sha(docx.read_bytes()),'candidate_bytes':docx.stat().st_size,'candidate_git_blob':'7ada5d133193314794700661ad7ca309da9c02dc',
 'source_branch':'work/ttqs-one-document-quality-contract-20261016','source_commit':'1db5e97bd173cfe802aba752198204d97bf90270','source_files':source_hashes,
 'qa_files':qa_hashes,'semantic_payload_sha256':sha(payload.read_bytes()),'chart_media_sha256':[sha(p.read_bytes()) for p in media],
 'requested_model':'gemini-3.8-flash-high','actual_model_identity':'UNKNOWN until native attestation','fallback':'forbidden','computer_use':'forbidden',
 'formal_acceptance':'NOT_GRANTED','real_evidence':'UNKNOWN','candidate_mutation':'forbidden','prompt_sha256':sha(prompt.encode()),'prompt_utf16_units':units,
 'current_candidate_sha_verified_before_dispatch':True
}
mp=rev/'INPUT_MANIFEST.json'; mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'prompt_path':str(pp),'prompt_sha256':sha(prompt.encode()),'prompt_utf16_units':units,'payload_sha256':sha(payload.read_bytes()),'candidate_sha256':manifest['candidate_sha256'],'manifest_path':str(mp),'source_git_blobs':{k:v['git_blob'] for k,v in source_hashes.items()},'qa_git_blobs':{k:v['git_blob'] for k,v in qa_hashes.items()},'chart_media_sha256':manifest['chart_media_sha256']},ensure_ascii=False))