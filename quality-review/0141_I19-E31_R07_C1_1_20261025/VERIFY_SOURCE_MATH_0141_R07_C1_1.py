from pathlib import Path
import csv,hashlib,json,re
base=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0141_I19-E31_SOURCE_PREP_R01_20261025')
r=base/'R07'; man=r/'MANUSCRIPT_0141_R07_C1_1_CANDIDATE.md'; regp=r/'SAMPLE_REPLACEMENT_REGISTER_0141_R07_C1_1.csv'; resp=base/'SAMPLE_SURVEY_RESPONSES_0141_R01.csv'; quest=base/'QUESTIONNAIRE_ITEMS_0141_R01.csv'
sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(resp.read_bytes())=='723259199dd51973fc6473ec000234cc853fa1511be05864fdfd7b08bb452862'
assert sha(quest.read_bytes())=='310745e5be17980ca9c623b23e15605cb221c9cbbdf1886913cb54db1acdf0e7'
with resp.open(encoding='utf-8-sig',newline='') as f: data=list(csv.DictReader(f))
assert len(data)==36
stats={}
for q,col in [('Q2','Q2_content_applicability'),('Q5','Q5_admin_communication')]:
 stats[q]={}
 for y in ('2023','2024','2025'):
  vals=[int(x[col]) for x in data if x['period_year']==y and x[col] not in ('','NA','N/A')]
  assert len(vals)==12
  stats[q][y]={'n':12,'sum':sum(vals),'mean':sum(vals)/12,'top2':sum(v>=4 for v in vals),'top2_rate':sum(v>=4 for v in vals)/12}
assert [(stats['Q2'][y]['sum'],stats['Q2'][y]['top2']) for y in ('2023','2024','2025')]==[(41,5),(41,5),(47,9)]
assert [(stats['Q5'][y]['sum'],stats['Q5'][y]['top2']) for y in ('2023','2024','2025')]==[(42,6),(48,8),(51,10)]
t=man.read_text(encoding='utf-8')
assert '\ufffd' not in t
checks={
'construct separation':'Q1\u2013Q6 \u70ba\u516d\u500b\u69cb\u9762\u984c\u9805' in t and 'Q7 \u70ba\u7368\u7acb\u7684\u6574\u9ad4\u6eff\u610f\u5ea6\u984c' in t,
'ASCII source condition':'UNKNOWN-sourced' in t and ('UNKNOWN'+chr(0x2011)+'sourced') not in t and '\u539f\u59cb\u8cc7\u6599\u4f86\u6e90\u3001\u9069\u7528\u671f\u9593\u3001\u8cac\u4efb\u89d2\u8272\u8207\u5347\u7d1a\u689d\u4ef6\u5f85\u5354\u6703\u6388\u6b0a\u4eba\u54e1\u6838\u5be6' in t,
'five-step flow':'\u771f\u5be6\u8cc7\u6599\u66ff\u63db\u4e94\u6b65\u6aa2\u6838\u6d41\u7a0b' in t and '[\u6b65\u9a5f 5\uff1a\u6388\u6b0a\u89d2\u8272\u5be9\u67e5' in t and '5. **\u6388\u6b0a\u89d2\u8272\u5be9\u67e5\u8207\u5019\u9078\u63a7\u5236**' in t,
'strict threshold label':'\u9580\u6abb >75.00%\uff1bn=12 \u81f3\u5c11 10/12' in t and '\u76ee\u6a19 75%' not in t,
'legacy floors removed':'3.8000' not in t and '3.7000' not in t and '\u820a\u7248\u6240\u5217\u5206\u6790\u4e0b\u9650\u5df2\u81ea\u672c\u7248\u64a4\u9664' in t,
'arithmetic retained':'3.9167 + 1/12 \u91cf\u5c3a\u9ede = 4.0000' in t and '4.2500 + 1/12 \u91cf\u5c3a\u9ede = 4.3333' in t and '9/12 \u6070\u70ba 75.00%' in t and '\u81f3\u5c11\u9700 10/12 = 83.33%' in t,
'truth boundary':'SAMPLE / SYNTHETIC' in t and 'REAL = UNKNOWN / HOLD' in t and 'Human formal acceptance = NOT_GRANTED' in t,
'revision history':'R07-C1.1-SYN' in t and 'R07-C1-SYN' in t}
if not all(checks.values()): raise SystemExit(json.dumps({'checks':checks,'failed':[k for k,v in checks.items() if not v]},ensure_ascii=True))
with regp.open(encoding='utf-8-sig',newline='') as f: reg=list(csv.DictReader(f))
man_sha=sha(man.read_bytes());reg_sha=sha(regp.read_bytes())
assert len(reg)==44 and {x['source_manuscript_sha256'] for x in reg}=={man_sha}
resp_rows=[x for x in reg if x['source_artifact']=='SAMPLE_SURVEY_RESPONSES_0141_R01.csv']
man_rows=[x for x in reg if x['source_artifact']==man.name]
assert len(resp_rows)==36 and len(man_rows)==8
pattern=r'\u9644\u9304\u4e09\u7b2c(\d+)\u5217\uff1b\u00a7\u9678\u5168\u9ad4\u8da8\u52e2\u5f59\u7e3d\u4f9d36\u7b46\u56de\u8986\u8207\u5404\u5e74\u5ea6\u9080\u8acb\u6578\u8a08\u7b97\uff0c\u4e0d\u6b78\u56e0\u55ae\u4e00\u5217\u3002'
nums=[]
for x in resp_rows:
 m=re.fullmatch(pattern,x['docx_locator']);assert m,repr(x['docx_locator']);nums.append(int(m.group(1)))
assert sorted(nums)==list(range(1,37))
receipt={'schema':'ttqs-one-0141-r07-c1-1-source-math-qa-v1','work_id':'TTQS_ONE_0141_I19-E31_R07_C1_1_SOURCE_MATH_QA','doc_id':'0141','requirement_id':'I19-E31','status':'PASS','verifier_sha256':sha(Path(__file__).read_bytes()),'manuscript_sha256':man_sha,'replacement_register_sha256':reg_sha,'r01_response_csv_sha256':sha(resp.read_bytes()),'r01_questionnaire_csv_sha256':sha(quest.read_bytes()),'r01_response_rows':len(data),'replacement_register_rows':len(reg),'response_locators_chinese':len(resp_rows),'manuscript_pointer_rows':len(man_rows),'all_register_rows_bound_to_exact_manuscript_sha':True,'recalculated_item_stats':stats,'q2_target':'(47+1)/12=4.000000; strict Top-2 >75.00%, n=12 requires 10/12; 9/12 fails','q5_target':'(51+1)/12=4.333333','retired_legacy_floors':'Removed from this candidate; no analysis floor is set.','semantic_repair_checks':checks,'candidate_docx_sha256':None,'real_data_status':'UNKNOWN/HOLD','formal_acceptance':'NOT_GRANTED','official_score':'NOT_ASSIGNED'}
p=r/'R07_C1_1_SOURCE_MATH_QA_RECEIPT.json';p.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','manuscript_sha256':man_sha,'register_sha256':reg_sha,'receipt_sha256':sha(p.read_bytes()),'checks':checks,'q2_2025':stats['Q2']['2025'],'q5_2025':stats['Q5']['2025']},ensure_ascii=True,indent=2))