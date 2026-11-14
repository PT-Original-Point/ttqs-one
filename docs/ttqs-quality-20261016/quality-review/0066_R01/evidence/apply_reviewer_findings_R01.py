from pathlib import Path
import csv,hashlib,json
root=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0066_R01')
p=root/'inputs'/'0066_SYNTHETIC_REPLACEMENT_REGISTER_R01.csv'
with p.open(encoding='utf-8-sig',newline='') as f:rd=csv.DictReader(f);fields=rd.fieldnames;rows=list(rd)
by={r['register_id']:r for r in rows}
if len(rows)!=22 or 'SYN-022' not in by:raise SystemExit('unexpected register basis')
r=by['SYN-022'];r['values_or_claims_in_document']='A-1至A-10為合成示範附件標籤、不是實際附件原件；A-11為空白工作表。';r['limits_and_controls']='A-1至A-10不得被誤認為實際附件存在或已驗證；A-11未填前不是完成佐證。'
for r in rows:
 if r['register_id'] in {'SYN-002','SYN-004','SYN-007','SYN-009','SYN-011','SYN-013','SYN-015','SYN-016','SYN-017','SYN-018','SYN-019','SYN-021','SYN-022'}:
  note='R01 Body／Blueprint／Writer／session 只作示範設計與產出追溯，不是 REAL 訓練事實或佐證。'
  if note not in r['basis_and_provenance']:r['basis_and_provenance']=(r['basis_and_provenance']+'；'+note).strip('；')
 if r['register_id']=='SYN-007':r['source_identity_or_hash']='0066_BODY_R01_HUMAN_READY.md SHA-256 e227a1966bdb5a1a59ed6f485c03fd9f19878c0b3945136e5c22247e9512f877（示範產出追溯，非個別時數原件）'
rows.append({
 'register_id':'SYN-023','scope':'非事件／個資邊界控制聲明',
 'values_or_claims_in_document':'真實出席／事故／個資事件為 UNKNOWN／HOLD；本示範不創造任何事故或個資事件。',
 'basis_and_provenance':'示範文件的證據邊界控制語句；不是事件未發生的證明；R01 Body／Blueprint 只作設計追溯，不是 REAL 訓練事實或佐證。',
 'source_identity_or_hash':'0066 BODY R01 SHA-256 e227a1966bdb5a1a59ed6f485c03fd9f19878c0b3945136e5c22247e9512f877；無外部事件原件。',
 'evidence_class':'SAMPLE CONTROL STATEMENT / UNKNOWN-HOLD',
 'required_real_replacement':'依實際事件紀錄及個資保護程序處理；若確認無事件，依授權的零事件申報方式留證；不得由本示範推定。',
 'document_locations':'第七節 REAL 未知狀態表',
 'limits_and_controls':'不得推論事件未發生；不含或生成任何個資；保留 UNKNOWN／HOLD 至正式來源查明。'
})
with p.open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows)
regsha=hashlib.sha256(p.read_bytes()).hexdigest()
manifestp=root/'evidence'/'source_manifest_R01.json';m=json.loads(manifestp.read_text(encoding='utf-8'));m['replacement_register_sha256']=regsha;m['replacement_register_rows']=len(rows);m['semantic_review']='PASS exact DOCX SHA; independent OpenCode beam-free review; optional replacement-register completeness notes applied without changing DOCX bytes';m['docx_app_properties']='WARN: Word package app.xml retained default Pages=1/Words=0 although Word-rendered PDF has 13 pages; reviewer found this non-semantic. Candidate DOCX not mutated to avoid metadata-only SHA churn.';manifestp.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qap=root/'evidence'/'technical_layout_receipt_R01.json';q=json.loads(qap.read_text(encoding='utf-8'));q['replacement_register_sha256']=regsha;q['replacement_register_rows']=len(rows);q['semantic_review']='PASS';q['semantic_review_docx_sha256']=m['candidate_docx_sha256'];q['reviewer_model']='opencode/beam-free';q['reviewer_session_id']='ses_eb05be946ffeR2JhXJbfgeMg0d';q['reviewer_findings_applied']=['Added SYN-023 for explicit no-event/no-personal-data claim as UNKNOWN/HOLD, not proof of absence.','Expanded SYN-022 to state A-1 through A-10 are synthetic labels, not supplied originals; A-11 remains an empty work form.','Clarified R01 model/session/body/Blueprint identifiers are production/design provenance only, not REAL evidence.'];q['known_non_body_metadata_limitation']='docProps/app.xml Pages=1 and Words=0 despite 13 rendered pages; independent reviewer says non-semantic; no DOCX mutation made.';qap.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
review=root/'review'/'opencode_beam_R01'/'independent_semantic_review_R01.md';rsha=hashlib.sha256(review.read_bytes()).hexdigest()
follow=root/'review'/'opencode_beam_R01'/'reviewer_finding_followup_R01.md';follow.write_text(f'''# 0066 R01 reviewer-finding follow-up\n\n- Independent verdict: PASS, bound to DOCX SHA-256 `{m['candidate_docx_sha256']}`.\n- Reviewer session/model: `ses_eb05be946ffeR2JhXJbfgeMg0d` / `opencode/beam-free`.\n- Original reviewer response SHA-256: `{rsha}`.\n- Applied two optional completeness notes to the separate replacement register only: SYN-022 explicitly classifies attachments A-1…A-10 as synthetic labels (A-11 is a blank form); new SYN-023 records the no-event/no-personal-data statement as UNKNOWN/HOLD, not proof that none occurred.\n- Marked R01 Builder/session/Blueprint references as design/production trace only, not REAL source evidence.\n- DOCX bytes were not changed; exact SHA remains `{m['candidate_docx_sha256']}`.\n- Reviewer did not inspect rendered pages; 13-page Word/PDF render was visually checked separately.\n- Stale OOXML app properties (`Pages=1`, `Words=0`) remain a non-semantic metadata limitation; body, PDF page count and rendered pages are 13.\n''',encoding='utf-8')
print(json.dumps({'register_sha256':regsha,'rows':len(rows),'reviewer_response_sha256':rsha,'docx_sha256':m['candidate_docx_sha256']},ensure_ascii=False))
