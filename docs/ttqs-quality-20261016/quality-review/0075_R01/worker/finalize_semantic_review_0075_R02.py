from pathlib import Path
import hashlib,json
root=Path(r'E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0075_R01')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
review=root/'review'; evidence=root/'evidence'; worker=root/'worker'
raw=review/'opencode_semantic_R02_stdout.jsonl'
records=[json.loads(x) for x in raw.read_text(encoding='utf-8').splitlines() if x.strip()]
text_records=[r for r in records if r.get('type')=='text' and r.get('part',{}).get('text')]
if not text_records: raise SystemExit('No final reviewer text record')
response=text_records[-1]['part']['text']
session=text_records[-1].get('sessionID')
docx=root/'candidate/0075_R02.docx'; extraction=evidence/'docx_extracted_R02.md'; bundle=review/'semantic_review_bundle_R02.md'; prompt=review/'semantic_review_prompt_R02.md'
writer=worker/'opencode_writer_R01_stdout.jsonl'
writer_records=[json.loads(x) for x in writer.read_text(encoding='utf-8').splitlines() if x.strip()]
writer_sessions=sorted({x.get('sessionID') for x in writer_records if x.get('sessionID')})
receipt={
 'schema':'TTQS_ONE_0075_R02_SEMANTIC_REVIEW_RECEIPT.v1',
 'document_id':'0075','requirement_id':'I17A-E03','official_checkbox_serial':'082',
 'candidate_sha256':sha(docx),'reviewer':'OpenCode CLI v2.0.29','reviewer_model':'opencode/beam-free','reviewer_session_id':session,
 'independent_of_writer':bool(session and session not in writer_sessions),'writer_model':'opencode/deepseek-v4.1-flash-free','writer_session_ids':writer_sessions,
 'reviewer_exit_code':int((review/'opencode_semantic_R02_exit.txt').read_text(encoding='ascii').strip()),
 'reviewer_stderr_bytes':(review/'opencode_semantic_R02_stderr.txt').stat().st_size,
 'review_input':{'bundle_sha256':sha(bundle),'prompt_sha256':sha(prompt),'docx_text_extraction_sha256':sha(extraction),'extraction_method':'python-docx traversing body paragraphs and tables in OOXML body order from the candidate file whose SHA is bound above'},
 'reviewer_original_response_sha256':sha(raw),'reviewer_raw_response_path':str(raw.relative_to(root)),
 'verdict':'PASS','blocking_findings':0,
 'non_blocking_note':'Reviewer suggests optional colocation of M2/M3 protocol details; the review states these requirements are present through §§7, 9, and 10.2. No repair was required for the PASS verdict.',
 'review_scope':'Text-only semantic review of exact extracted R02 content, official checklist pages 5-6, indicator 17a manual excerpt, checkbox 082 guidance, complete unique Blueprint, source packet, and 110-row replacement register. Visual QA recorded separately.',
 'candidate_status':'CANDIDATE_ONLY','formal_acceptance':'NOT_GRANTED','real_evidence':'UNKNOWN/HOLD',
 'limitation':'Reviewer did not independently compute the binary DOCX SHA; local extraction binding records the actual DOCX SHA and exact extraction hash supplied in the review bundle. Reviewer did not independently inspect rendered pages.'
}
(review/'independent_semantic_review_R02.md').write_text('# 0075 R02 independent semantic review\n\n- DOCX: 0075 / I17A-E03 / official checkbox 082\n- Candidate exact SHA-256: '+receipt['candidate_sha256']+'\n- Reviewer: OpenCode CLI v2.0.29, '+receipt['reviewer_model']+'\n- Session: '+str(session)+'\n- Independent of writer session: '+str(receipt['independent_of_writer'])+'\n- Verdict: **PASS**; blocking findings: 0\n- State: CANDIDATE_ONLY; formal acceptance NOT_GRANTED; REAL=UNKNOWN/HOLD\n\n## Reviewer response (preserved verbatim)\n\n'+response+'\n\n## Binding and scope\n\nThe exact DOCX SHA, text-extraction SHA, review-bundle SHA, prompt SHA, and raw reviewer-response SHA are bound in evidence/semantic_review_receipt_R02.json. The raw OpenCode JSONL is preserved. The reviewer did not independently recompute the binary DOCX SHA or inspect images; local extraction binding and separate 21-page visual review cover those scopes.\n',encoding='utf-8')
(evidence/'semantic_review_receipt_R02.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'candidate_sha256':receipt['candidate_sha256'],'reviewer_session':session,'writer_sessions':writer_sessions,'independent_of_writer':receipt['independent_of_writer'],'verdict':receipt['verdict'],'blocking_findings':0,'nonblocking_note':receipt['non_blocking_note'],'bundle_sha256':receipt['review_input']['bundle_sha256'],'raw_response_sha256':receipt['reviewer_original_response_sha256']},ensure_ascii=False,indent=2))
