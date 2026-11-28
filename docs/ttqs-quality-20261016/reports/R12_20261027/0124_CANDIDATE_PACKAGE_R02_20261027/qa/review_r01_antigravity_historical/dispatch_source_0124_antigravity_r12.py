import hashlib,json,os,subprocess,time
from datetime import datetime
from pathlib import Path
root=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0124_I19-E12_SOURCE_PREP_R01_20261024')
cand=root/'candidate_R01'/'0124__結訓學員雇用與雇主回饋佐證表_R01_candidate.docx'
review_input=root/'candidate_R01'/'independent_review_R01'/'0124_semantic_review_input_exact_sha_R01.md'
source=root/'SOURCE_PACKET_0124_I19-E12_R01.md'; blueprint=root/'UNIQUE_BLUEPRINT_0124_I19-E12_R01.md'
out=root/'candidate_R01'/'independent_review_R01'/'ANTIGRAVITY_R12_REVIEW_20261027'
exe=Path(r'C:\Users\J\AppData\Local\agy\bin\agy.exe')
def sha(b):return hashlib.sha256(b).hexdigest()
if out.exists():raise SystemExit('Refusing duplicate exact-scope reviewer directory')
for x in (cand,review_input,source,blueprint,exe):
 if not x.exists():raise SystemExit(f'Missing required input: {x.name}')
expected={'candidate':'0a6567c2779d9ad8014ab6d1c892779a98892351a38ceda0dea9fa8b24ff2988','source':'83a03deb7cbef3f07ef8b7ce0b2b25e1744baa6bc2e96b29e3259453558ccfee','blueprint':'d0d8b0990d96fb7dab5d02a34d9f507b6434e57778646c920c488f01c1ab0f42','review_input':'28fd462a35929895d283e82127bc32664ff94bd9fd882217533d6764f88d2c14'}
actual={'candidate':sha(cand.read_bytes()),'source':sha(source.read_bytes()),'blueprint':sha(blueprint.read_bytes()),'review_input':sha(review_input.read_bytes())}
if actual!=expected:raise SystemExit('Exact input SHA mismatch; no dispatch')
# Check there is no active Antigravity process before dispatch.
procs=subprocess.run(['powershell','-NoProfile','-Command',"Get-CimInstance Win32_Process | Where-Object {$_.Name -match 'agy|antigravity'} | Select-Object -ExpandProperty ProcessId"],capture_output=True,text=True,timeout=15).stdout.strip()
if procs:raise SystemExit('Antigravity process already active; do not duplicate: '+procs)
flags=getattr(subprocess,'CREATE_NO_WINDOW',0x08000000)
model_list=subprocess.run([str(exe),'models'],capture_output=True,timeout=25,creationflags=flags)
model_stdout=model_list.stdout; model_stderr=model_list.stderr
model_ok=model_list.returncode==0 and b'gemini-3.8-flash-high' in model_stdout
if not model_ok:raise SystemExit('Required Gemini model not confirmed in CLI model list; no dispatch')
out.mkdir(parents=True)
(out/'MODEL_CATALOG_STDOUT.txt').write_bytes(model_stdout)
(out/'MODEL_CATALOG_STDERR.txt').write_bytes(model_stderr)
inst=review_input.read_text(encoding='utf-8')
prompt=("You are an independent semantic reviewer for TTQS_ONE. Review ONLY the supplied exact-SHA packet below. Do not use tools, filesystem, network, computer control, plugins, or external sources; do not edit or create files; do not switch models. The packet contains its own review rubric and official source plus unique Blueprint. Assess the candidate as a text-only semantic review; do not claim visual or binary inspection. Return PASS, PARTIAL, or FAIL with concise section/table/question locators and concrete findings. Explicitly separate SAMPLE/SYNTHETIC from REAL and do not invent real association activity, approvals, employer originals, signatures, consent, or facts. If packet or source binding is insufficient, return PARTIAL/FAIL and state why. Include requested model identity only if the native service response itself exposes it; otherwise write UNKNOWN.\n\n"+inst)
cmd=[str(exe),'--model','gemini-3.8-flash-high','--mode','plan','--sandbox','--output-format=json','--print-timeout=4m','--print='+prompt]
cmdline=subprocess.list2cmdline(cmd)
units=len(cmdline.encode('utf-16le'))//2
if units>32000:raise SystemExit(f'Windows command-line bound exceeded ({units}); no dispatch')
request=out/'ANTIGRAVITY_R12_REVIEW_REQUEST.md';request.write_text(prompt,encoding='utf-8',newline='\n')
manifest={'project_id':'TTQS_ONE','doc_id':'0124','requirement_id':'I19-E12','work_id':'TTQS-0124-I19-E12-R01-ANTIGRAVITY-R12-EXACT-SHA-SEMANTIC-REVIEW','candidate_sha256':actual['candidate'],'source_packet_sha256':actual['source'],'unique_blueprint_sha256':actual['blueprint'],'review_input_sha256':actual['review_input'],'review_request_sha256':sha(prompt.encode('utf-8')),'requested_model':'gemini-3.8-flash-high','model_catalog_exit':model_list.returncode,'model_catalog_sha256':sha(model_stdout),'fallback_allowed':False,'computer_use':False,'files_or_network_tools_requested':False,'mode':'plan','sandbox':True,'cli_version':'1.4.7','cmdline_utf16_units':units,'dispatch_local':datetime.now().astimezone().isoformat()}
(out/'INPUT_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
so=(out/'RAW_STDOUT.json').open('wb');se=(out/'RAW_STDERR.txt').open('wb')
p=subprocess.Popen(cmd,cwd=r'E:\TTQS',stdin=subprocess.DEVNULL,stdout=so,stderr=se,creationflags=flags|0x00000200)
start={'schema':'TTQS_ONE_ANTIGRAVITY_R12_DISPATCH_START_V1','project_id':'TTQS_ONE','doc_id':'0124','requirement_id':'I19-E12','work_id':manifest['work_id'],'pid':p.pid,'candidate_sha256':actual['candidate'],'request_sha256':manifest['review_request_sha256'],'requested_model':'gemini-3.8-flash-high','actual_model':'UNKNOWN_PENDING_NATIVE_RESPONSE','fallback_allowed':False,'computer_use':False,'filesystem_network_tools':'PROHIBITED_BY_REQUEST_AND_PROMPT','mode':'plan','sandbox':True,'model_catalog_confirmed':True,'started_local':manifest['dispatch_local'],'stdout_path':str(out/'RAW_STDOUT.json'),'stderr_path':str(out/'RAW_STDERR.txt'),'process_window':'CREATE_NO_WINDOW','status':'RUNNING'}
(out/'DISPATCH_START.json').write_text(json.dumps(start,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'status':'RUNNING','pid':p.pid,'work_id':manifest['work_id'],'candidate_sha256':actual['candidate'],'model_requested':'gemini-3.8-flash-high','model_catalog_confirmed':True,'cmdline_utf16_units':units,'output_dir':str(out)},ensure_ascii=False),flush=True)
try: code=p.wait(timeout=255); timed=False
except subprocess.TimeoutExpired:
 p.kill(); code=None; timed=True
so.close();se.close()
raw=(out/'RAW_STDOUT.json').read_bytes();err=(out/'RAW_STDERR.txt').read_bytes()
actual_model='UNKNOWN'
usage='UNKNOWN'
tool_indicators=[]
try:
 obj=json.loads(raw.decode('utf-8'))
 for key in ('model','modelName','model_name','servingModel','serving_model'):
  if isinstance(obj,dict) and isinstance(obj.get(key),str): actual_model=obj[key]
 def walk(v):
  if isinstance(v,dict):
   for k,x in v.items():
    if k.lower() in ('model','modelname','model_name','servingmodel','serving_model') and isinstance(x,str):
     if x: tool_indicators.append(('model',x))
    if k.lower() in ('usage','usageMetadata'.lower(),'usage_metadata','tokenUsage'.lower(),'token_usage'):
     tool_indicators.append(('usage',x))
    if k.lower() in ('tool','toolname','tool_name','toolcall','tool_call','functioncall'):
     tool_indicators.append(('tool',x))
    walk(x)
  elif isinstance(v,list):
   for x in v:walk(x)
 walk(obj)
 for kind,val in tool_indicators:
  if kind=='model' and actual_model=='UNKNOWN':actual_model=str(val)
  if kind=='usage' and usage=='UNKNOWN':usage=val
except Exception: pass
if timed:status='TIMED_OUT'; code_txt='UNKNOWN_TERMINATED_AFTER_255S'
elif code==0:status='COMPLETED';code_txt=code
else:status='FAILED';code_txt=code
terminal={'schema':'TTQS_ONE_ANTIGRAVITY_R12_DISPATCH_TERMINAL_V1','project_id':'TTQS_ONE','doc_id':'0124','requirement_id':'I19-E12','work_id':manifest['work_id'],'pid':p.pid,'exit_code':code_txt,'status':status,'candidate_sha256':actual['candidate'],'review_request_sha256':manifest['review_request_sha256'],'requested_model':'gemini-3.8-flash-high','actual_serving_model':actual_model,'model_fallback':'UNKNOWN_NOT_VERIFIED; no fallback authorized','usage_or_token_count':usage,'stdout_bytes':len(raw),'stdout_sha256':sha(raw),'stderr_bytes':len(err),'stderr_sha256':sha(err),'tool_indicators_detected':[{'kind':k,'value':v} for k,v in tool_indicators if k=='tool'],'computer_use':'NOT_USED_BY_LAUNCH; verify response transcript for any tool claim','candidate_mutated':sha(cand.read_bytes())!=actual['candidate'],'timed_out':timed,'finished_local':datetime.now().astimezone().isoformat()}
(out/'DISPATCH_TERMINAL.json').write_text(json.dumps(terminal,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'status':status,'exit_code':code_txt,'stdout_bytes':len(raw),'stdout_sha256':terminal['stdout_sha256'],'stderr_bytes':len(err),'stderr_sha256':terminal['stderr_sha256'],'actual_model':actual_model,'usage':usage,'tool_call_indicators':len(terminal['tool_indicators_detected']),'candidate_mutated':terminal['candidate_mutated'],'output_dir':str(out)},ensure_ascii=False),flush=True)
