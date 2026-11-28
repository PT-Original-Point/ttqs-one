from pathlib import Path
from datetime import datetime
import json,hashlib,subprocess,os
BASE=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0100_0101_R08_SOURCE_BLUEPRINT_20261021\candidate_R09b\review\W2_DELTA_R01')
manifest=json.loads((BASE/'DISPATCH_MANIFEST_R01.json').read_text(encoding='utf-8'))
prompt_path=Path(manifest['prompt_path']); prompt=prompt_path.read_text(encoding='utf-8')
def sha(b):return hashlib.sha256(b).hexdigest()
agy=Path(r'C:\Users\J\AppData\Local\agy\bin\agy.exe')
docx=Path(manifest['candidate_docx_path'])
if sha(docx.read_bytes())!=manifest['candidate_docx_sha256']: raise SystemExit('PRE_DISPATCH_CANDIDATE_SHA_MISMATCH')
if sha(prompt.encode())!=manifest['prompt_sha256']: raise SystemExit('PRE_DISPATCH_PROMPT_SHA_MISMATCH')
if not agy.is_file(): raise SystemExit('AGY_CLI_MISSING')
cwd=BASE/'empty_cli_workspace'; cwd.mkdir(exist_ok=True)
if any(cwd.iterdir()): raise SystemExit('CLI_WORKSPACE_NOT_EMPTY')
args=[str(agy),'--input-format','stream-json','--output-format','stream-json','--model','gemini-3.8-flash-high','--effort','high','--mode','plan','--sandbox','--disable-slash-commands','--print-timeout','5m']
msg=json.dumps({'event':'user','message':{'content':prompt}},ensure_ascii=False,separators=(',',':'))+'\n'
started=datetime.now().astimezone().isoformat(); flags=getattr(subprocess,'CREATE_NO_WINDOW',0)
proc=subprocess.Popen(args,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,cwd=str(cwd),creationflags=flags)
pid=proc.pid; timeout=False
try: out,err=proc.communicate(msg.encode('utf-8'),timeout=310)
except subprocess.TimeoutExpired:
 timeout=True;proc.kill();out,err=proc.communicate()
ended=datetime.now().astimezone().isoformat()
(BASE/'AGY_STREAM_STDOUT_R01.jsonl').write_bytes(out);(BASE/'AGY_STDERR_R01.txt').write_bytes(err)
events=[];parse_errors=[]
for i,line in enumerate(out.decode('utf-8','replace').splitlines(),1):
 try:events.append(json.loads(line))
 except Exception as e:parse_errors.append({'line':i,'error':str(e),'sample':line[:200]})
init=next((x for x in events if x.get('event')=='init'),{})
res=next((x.get('result',{}) for x in reversed(events) if x.get('event')=='result'),{})
steps=[x.get('step_update',{}) for x in events if x.get('event')=='step_update']
tool_steps=[{'tool_name':s.get('tool_name'),'state':s.get('state'),'text':s.get('text_delta','')[:160]} for s in steps if s.get('step_type')=='tool']
response=res.get('response','');(BASE/'AGY_RESPONSE_R01.txt').write_text(response,encoding='utf-8')
init_model=init.get('init',{}).get('model')
receipt={'project_id':'TTQS_ONE','work_id':manifest['work_id'],'worker':'Antigravity CLI','cli_version':'1.4.7 (agy.exe --version, local)','requested_model':'gemini-3.8-flash-high','cli_args':args[1:],'cli_pid':pid,'cli_exit_code':proc.returncode,'started_local':started,'ended_local':ended,'timeout':timeout,'candidate_docx_sha256':manifest['candidate_docx_sha256'],'body_extraction_sha256':manifest['body_extraction_sha256'],'baseline_docx_sha256':manifest['baseline_docx_sha256'],'prompt_sha256':sha(prompt.encode()),'prompt_bytes':len(prompt.encode()),'requested_model_matches_cli_init':init_model=='gemini-3.8-flash-high','cli_init_model_reported':init_model,'backend_serving_model_identity':'UNKNOWN','fallback_policy':'PROHIBITED','fallback_event_observed_in_output':any('fallback' in line.lower() for line in out.decode('utf-8','replace').splitlines()),'init_cwd':init.get('init',{}).get('cwd'),'permission_mode':init.get('init',{}).get('permission_mode'),'terminal_status':res.get('status','NO_TERMINAL_RESULT'),'conversation_id':res.get('conversation_id'),'duration_seconds':res.get('duration_seconds'),'num_turns':res.get('num_turns'),'usage':res.get('usage'),'error':res.get('error'),'tool_steps':tool_steps,'browser_or_computer_tools_called':any(any(k in (t.get('tool_name') or '').lower() for k in ['browser','computer','screen','mouse','keyboard']) for t in tool_steps),'all_tool_usage_forbidden_by_prompt':True,'parse_errors':parse_errors,'stdout_sha256':sha(out),'stdout_bytes':len(out),'stderr_sha256':sha(err),'stderr_bytes':len(err),'response_sha256':sha(response.encode()),'response_bytes':len(response.encode()),'stdout_path':str(BASE/'AGY_STREAM_STDOUT_R01.jsonl'),'stderr_path':str(BASE/'AGY_STDERR_R01.txt'),'response_path':str(BASE/'AGY_RESPONSE_R01.txt'),'adjudication_status':'PENDING_LOCAL_INDEPENDENT_ADJUDICATION'}
recpath=BASE/'AGY_DISPATCH_RECEIPT_R01.json';recpath.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ['cli_pid','cli_exit_code','started_local','ended_local','timeout','requested_model_matches_cli_init','cli_init_model_reported','backend_serving_model_identity','terminal_status','conversation_id','duration_seconds','num_turns','usage','error','tool_steps','browser_or_computer_tools_called','fallback_event_observed_in_output','response_bytes','response_sha256','stdout_sha256','stderr_sha256','parse_errors']},ensure_ascii=False))
