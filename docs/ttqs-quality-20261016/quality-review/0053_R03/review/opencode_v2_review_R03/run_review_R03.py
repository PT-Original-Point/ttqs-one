import datetime, hashlib, json, subprocess, sys
from pathlib import Path
out=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0053_R03\review\opencode_v2_review_R03')
packet=out/'packet_R03'/'independent_review_packet_R03.md'
prompt=(out/'packet_R03'/'review_prompt_R03.txt').read_text(encoding='utf-8')
exe=Path(r'C:\Users\J\AppData\Local\Programs\@opencode-aidesktop\resources\opencode-cli.exe')
root=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0053_R03')
files=[packet,root/'candidate'/'0053_R03.docx',root/'evidence'/'render_final_R03'/'0053_R03_Word_export.pdf',root/'SYNTHETIC_REPLACEMENT_REGISTER_0053_R03.csv',root/'evidence'/'visual_contact_sheet_R03_compact.jpg']
for n in [2,5,8,10,18]: files.append(root/'evidence'/'render_final_R03'/f'page-{n:02d}.png')
files.append(root/'inputs'/'official_evidence_table_page4.png')
args=[str(exe),'run','--standalone','--format','json','--model','opencode/nemotron-3.5-super-vl-free','--title','TTQS ONE 0053 R03 exact-SHA independent review']
for f in files: args.extend(['--file',str(f)])
args.append(prompt)
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
receipt={'schema':'ttqs.0053.opencode_v2_dispatch_receipt.v1','status':'RUNNING','started_utc':started,'requested_model':'opencode/nemotron-3.5-super-vl-free','cli_version':'opencode v2.0.29','cli_path':str(exe),'candidate_sha256':'cc75583238dba42eede61de990992770f8de75e96d1bcfe1313e57629551f8e8','packet_sha256':hashlib.sha256(packet.read_bytes()).hexdigest(),'files_attached':[str(x) for x in files],'stdout_path':str(out/'opencode_v2_stdout_R03.jsonl'),'stderr_path':str(out/'opencode_v2_stderr_R03.txt'),'exit_code_path':str(out/'exit_code_R03.txt')}
(out/'dispatch_receipt_R03.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (out/'opencode_v2_stdout_R03.jsonl').open('wb') as stdout, (out/'opencode_v2_stderr_R03.txt').open('wb') as stderr:
 p=subprocess.Popen(args,cwd=str(root.parents[2]),stdout=stdout,stderr=stderr)
 receipt['process_id']=p.pid
 (out/'dispatch_receipt_R03.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'status':'RUNNING','pid':p.pid,'start_utc':started,'attached_files':len(files),'model':receipt['requested_model']}),flush=True)
 rc=p.wait()
(receipt.update({'status':'COMPLETED' if rc==0 else 'FAILED','completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':rc}))
(out/'exit_code_R03.txt').write_text(str(rc)+'\n',encoding='ascii')
(out/'dispatch_receipt_R03.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':receipt['status'],'exit_code':rc,'completed_utc':receipt['completed_utc']}),flush=True)
