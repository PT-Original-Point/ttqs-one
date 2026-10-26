from pathlib import Path
from datetime import datetime
import hashlib, json, subprocess, sys
run=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0121_I19-E09_SOURCE_PREP_R01_20261024\candidate_R02\evidence\antigravity_semantic_review_R02_20261026T0744_TPE')
base=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0121_I19-E09_SOURCE_PREP_R01_20261024\candidate_R02')
doc=base/'0121_學員滿意度與學習評量報告_R02.docx'
prompt_path=base/'evidence'/'semantic_review_request_R02.txt'
expected_doc='ae5da09e834f5a8e9097a85ac87d4fe2f76acf9626049d3b0bea7c5f35042efe'
expected_prompt='dbf4d1e8fac3cc591a021620906022c40f04b6ae0611ec71359cf5ed03cc387d'
pr_head='92970462155e4ad52bf25a27f483ffa7e7fcecc1'
remote_blob='369571cb73f1b674cf480196cf12f5fbc97ab684'
def h(b): return hashlib.sha256(b).hexdigest()
if (run/'DISPATCH_RECEIPT.json').exists() or (run/'ATTEMPT01_START.json').exists():
    raise SystemExit('ATTEMPT01_ALREADY_STARTED_NO_DUPLICATE')
doc_bytes=doc.read_bytes()
prompt_bytes=prompt_path.read_bytes()
doc_sha=h(doc_bytes); prompt_sha=h(prompt_bytes)
if doc_sha!=expected_doc or prompt_sha!=expected_prompt:
    raise SystemExit('PRE_DISPATCH_HASH_MISMATCH')
prompt=prompt_bytes.decode('utf-8-sig')
workspace=run/'empty_cli_workspace'
workspace.mkdir(exist_ok=True)
if any(workspace.iterdir()):
    raise SystemExit('CLI_WORKSPACE_NOT_EMPTY')
agy=Path(r'C:\Users\J\AppData\Local\agy\bin\agy.exe')
if not agy.exists():
    raise SystemExit('AGY_CLI_MISSING')
start={'attempt':'ATTEMPT01','work_id':'TTQS-0121-I19-E09-R02-EXACT-SHA-SEMANTIC-REVIEW-W2-20261026T0744',
       'started_local':datetime.now().astimezone().isoformat(),'doc_id':'0121','requirement_id':'I19-E09',
       'candidate_sha256':doc_sha,'prompt_sha256':prompt_sha,'requested_model':'gemini-3.8-flash-high',
       'pr_head':pr_head,'remote_candidate_blob':remote_blob,'transport':'Python subprocess.Popen.communicate; CREATE_NO_WINDOW',
       'tools_requested':False,'computer_use':'FORBIDDEN','fallback':'NOT_REQUESTED'}
(run/'ATTEMPT01_START.json').write_text(json.dumps(start,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
args=[str(agy),'--input-format','stream-json','--output-format','stream-json','--model','gemini-3.8-flash-high',
      '--effort','high','--mode','plan','--sandbox','--disable-slash-commands','--print-timeout','5m']
msg=json.dumps({'event':'user','message':{'content':prompt}},ensure_ascii=False,separators=(',',':'))+'\n'
started=datetime.now().astimezone().isoformat()
creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0)
proc=subprocess.Popen(args,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                      cwd=str(workspace),creationflags=creationflags)
pid=proc.pid
timeout=False
try:
    out,err=proc.communicate(msg.encode('utf-8'),timeout=310)
except subprocess.TimeoutExpired:
    proc.kill()
    out,err=proc.communicate()
    timeout=True
ended=datetime.now().astimezone().isoformat()
(run/'RAW_STDOUT.jsonl').write_bytes(out)
(run/'RAW_STDERR.txt').write_bytes(err)
events=[]; parse_errors=[]
for ix,line in enumerate(out.decode('utf-8','replace').splitlines(),1):
    try:
        events.append(json.loads(line))
    except Exception as e:
        parse_errors.append({'line':ix,'error':str(e),'sample':line[:240]})
init=next((e for e in events if e.get('event')=='init'),{})
result=next((e.get('result',{}) for e in reversed(events) if e.get('event')=='result'),{})
steps=[e.get('step_update',{}) for e in events if e.get('event')=='step_update']
tool_steps=[{'tool_name':s.get('tool_name'),'state':s.get('state')} for s in steps if s.get('step_type')=='tool']
response=result.get('response','')
response_bytes=response.encode('utf-8') if isinstance(response,str) else json.dumps(response,ensure_ascii=False).encode('utf-8')
(run/'RESPONSE.txt').write_bytes(response_bytes)
after_sha=h(doc.read_bytes())
cli_model=init.get('init',{}).get('model')
terminal=result.get('status','NO_TERMINAL_RESULT')
status='FAILED_OR_INCOMPLETE'
if proc.returncode==0 and not timeout and terminal=='success' and response and cli_model=='gemini-3.8-flash-high' and not tool_steps and after_sha==doc_sha:
    status='RESPONSE_RECOVERED_TEXT_ONLY_MODEL_SLUG_MATCH_CANDIDATE_UNCHANGED'
elif response and tool_steps:
    status='RESPONSE_RECOVERED_BUT_TOOL_USE_DETECTED_NOT_VALID_FOR_TEXT_ONLY_REVIEW'
stdout_sha=h(out); stderr_sha=h(err); response_sha=h(response_bytes)
receipt={'schema':'ttqs-one-external-semantic-review-dispatch-v1','attempt':'ATTEMPT01','project_id':'TTQS_ONE',
         'work_id':start['work_id'],'doc_id':'0121','requirement_id':'I19-E09','worker':'Antigravity CLI',
         'cli_path':str(agy),'cli_file_version':agy.stat().st_mtime,
         'requested_model':'gemini-3.8-flash-high','cli_init_model_reported':cli_model,
         'actual_serving_model_identity':'UNKNOWN','fallback':'NOT_REQUESTED; provider-side fallback UNKNOWN',
         'tools_requested':False,'tool_steps':tool_steps,'computer_use':'NOT_USED_BY_REQUEST; native attestation UNKNOWN',
         'pid':pid,'started_local':started,'ended_local':ended,
         'duration_seconds':round((datetime.fromisoformat(ended)-datetime.fromisoformat(started)).total_seconds(),3),
         'exit_code':proc.returncode,'timeout':timeout,'terminal_status':terminal,'dispatch_outcome':status,
         'pr_head_at_dispatch':pr_head,'remote_candidate_git_blob_at_dispatch':remote_blob,
         'candidate_sha256_before':doc_sha,'candidate_sha256_after':after_sha,'candidate_unchanged':after_sha==doc_sha,
         'prompt_sha256':prompt_sha,'prompt_bytes':len(prompt_bytes),'stdout_bytes':len(out),'stdout_sha256':stdout_sha,
         'stderr_bytes':len(err),'stderr_sha256':stderr_sha,'response_bytes':len(response_bytes),
         'response_sha256':response_sha,'json_parse_errors':parse_errors,
         'usage':result.get('usage','UNKNOWN'),'error':result.get('error'),
         'formal_acceptance':'NOT_GRANTED','real_evidence':'NOT_PROVIDED'}
(run/'DISPATCH_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ('attempt','doc_id','candidate_sha256_before','candidate_sha256_after','requested_model','cli_init_model_reported','actual_serving_model_identity','pid','exit_code','timeout','terminal_status','dispatch_outcome','duration_seconds','response_bytes','response_sha256','stdout_sha256','tool_steps','usage')},ensure_ascii=False))