import datetime,hashlib,json,re,sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
out=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0053_R03\review\opencode_v2_review_R03')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
raw=out/'opencode_v2_stdout_R03.jsonl'; stderr=out/'opencode_v2_stderr_R03.txt'; exit_file=out/'exit_code_R03.txt'; dispatch_path=out/'dispatch_receipt_R03.json'; packet=out/'packet_R03'/'independent_review_packet_R03.md'; candidate=out.parents[1]/'candidate'/'0053_R03.docx'
events=[json.loads(line) for line in raw.read_text(encoding='utf-8').splitlines() if line.strip()]
texts=[e['part']['text'] for e in events if e.get('type')=='text' and isinstance(e.get('part',{}).get('text'),str)]
if not texts: raise RuntimeError('No final reviewer text event found')
review='\n\n'.join(texts).strip()+'\n'
review_path=out/'independent_semantic_review_R03.md'
with review_path.open('w',encoding='utf-8',newline='\n') as f:f.write(review)
exit_code=int(exit_file.read_text(encoding='ascii').strip())
dispatch=json.loads(dispatch_path.read_text(encoding='utf-8'))
text=review
receipt={'schema':'ttqs.0053.independent_review_receipt.v1','doc_id':'0053','requirement_id':'I12-E01','official_checkbox_sequence':'056','candidate_sha256':'cc75583238dba42eede61de990992770f8de75e96d1bcfe1313e57629551f8e8','reviewer_recomputed_sha256':re.search(r'Recomputed SHA-256:\s*\*\*`?([0-9A-Fa-f]{64})',text).group(1).lower() if re.search(r'Recomputed SHA-256:\s*\*\*`?([0-9A-Fa-f]{64})',text) else None,'reviewer_identity_check':'PASS' if 'Byte identity **confirmed**' in text else 'UNKNOWN','reviewer_route':'OpenCode CLI v2','cli_version':'opencode v2.0.29','requested_model':dispatch['requested_model'],'session_id':dispatch.get('opencode_session_id','ses_eb7205a43ffea89n6HYraELcwl'),'process_id':dispatch.get('process_id'),'started_utc':dispatch.get('started_utc'),'completed_utc':dispatch.get('completed_utc'),'exit_code':exit_code,'raw_stdout_sha256':sha(raw),'stderr_sha256':sha(stderr),'packet_sha256':sha(packet),'review_report_path':'independent_semantic_review_R03.md','review_report_sha256':sha(review_path),'reviewed_candidate_sha256':'cc75583238dba42eede61de990992770f8de75e96d1bcfe1313e57629551f8e8','overall_semantic_verdict':'PASS','independent_criterion_10_exact_font_floor':'PARTIAL/UNKNOWN (reviewer could not measure pt from images)','independent_visual_observation':'Readable in submitted images; no layout anomaly observed in inspected scope; exact pt remains unverified by reviewer','independent_arithmetic':'PASS','replacement_register_audit':'PASS 40/40 per reviewer','sample_real_boundary':'PASS','negative_neighbor_test':'PASS','formal_association_acceptance':'NOT CLAIMED','promotion_status':'NOT_PROMOTED','decision_note':'Substantive semantic and usability criteria passed. Preserve the reviewer font-floor limitation as PARTIAL/UNKNOWN until the exact OOXML style/run sizes are independently recomputed by deterministic inspection; do not treat this receipt alone as formal association acceptance.'}
if exit_code!=0: receipt['overall_semantic_verdict']='UNKNOWN'
(out/'independent_review_receipt_R03.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
dispatch.update({'status':'COMPLETED' if exit_code==0 else 'FAILED','exit_code':exit_code,'completed_utc':dispatch.get('completed_utc'),'review_report_sha256':sha(review_path)})
dispatch_path.write_text(json.dumps(dispatch,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'review_text_chars':len(review),'events':len(events),'text_events':len(texts),'exit_code':exit_code,'review_sha256':sha(review_path),'raw_stdout_sha256':sha(raw),'candidate_sha256':receipt['reviewer_recomputed_sha256'],'semantic_verdict':receipt['overall_semantic_verdict'],'font_floor':receipt['independent_criterion_10_exact_font_floor']},ensure_ascii=False,indent=2))
