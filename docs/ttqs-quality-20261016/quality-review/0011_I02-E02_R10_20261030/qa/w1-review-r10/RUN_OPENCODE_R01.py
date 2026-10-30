from pathlib import Path
import hashlib,json,os,subprocess,sys,time,datetime
root=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0011_I02-E02_LUNA_TEXT_DRAFT_R01_20261029')
outdir=root/'qa'/'W1_SEMANTIC_REVIEW_R10_20261030'
exe=Path(r'C:\Users\J\AppData\Roaming\npm\node_modules\@opencode\cli\bin\opencode.exe')
packet=outdir/'REVIEW_INPUT_R10_DELTA.md'; prompt=(outdir/'PROMPT_R01.txt').read_text(encoding='utf-8')
candidate=root/'candidate'/'0011_I02-E02_R10.docx'
model='opencode/glm-5.3-flash-free'; timeout_s=300
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.datetime.now().astimezone().isoformat()
stdout=outdir/'RAW_STDOUT_R01.jsonl'; stderr=outdir/'RAW_STDERR_R01.txt'
start_path=outdir/'DISPATCH_START_R01.json'; terminal_path=outdir/'DISPATCH_TERMINAL_R01.json'
if not exe.is_file() or not packet.is_file() or not candidate.is_file(): raise SystemExit('required input missing')
ps=r"Get-CimInstance Win32_Process | Where-Object { $_.Name -match 'opencode' -and $_.CommandLine -notmatch 'serve --service' } | Select-Object ProcessId,Name,CommandLine | ConvertTo-Json -Compress"
existing=subprocess.run(['powershell.exe','-NoProfile','-Command',ps],capture_output=True,text=True,timeout=10,creationflags=subprocess.CREATE_NO_WINDOW)
try: found=json.loads(existing.stdout) if existing.stdout.strip() else []
except Exception: found=[]
if found: raise SystemExit('refusing duplicate W1 dispatch; non-service OpenCode process exists: '+json.dumps(found))
before=sha(candidate); packet_sha=sha(packet); started=now()
ver=subprocess.run([str(exe),'--version'],capture_output=True,text=True,timeout=10,creationflags=subprocess.CREATE_NO_WINDOW)
start={'work_id':'TTQS-0011-W1-SEMANTIC-R10-DELTA-20261030-01','worker':'W1 OpenCode v2 CLI','stage':'READY_INDEPENDENT_SEMANTIC_DELTA','doc_id':'0011','requirement_id':'I02-E02','candidate_sha256_before':before,'review_packet_path':str(packet),'review_packet_sha256':packet_sha,'requested_model':model,'actual_model':'UNKNOWN_PENDING_SESSION_METADATA','cli_path':str(exe),'cli_version':ver.stdout.strip() or 'UNKNOWN','windows_identity':subprocess.check_output(['whoami.exe'],text=True,creationflags=subprocess.CREATE_NO_WINDOW).strip(),'pid':'PENDING','started_at_local':started,'process_window':'HIDDEN_CREATE_NO_WINDOW','tools':'NO_AUTO_APPROVE; reviewer prompt prohibits tools/writes; packet-only input','timeout_seconds':timeout_s}
start_path.write_text(json.dumps(start,ensure_ascii=False,indent=2),encoding='utf-8')
args=[str(exe),'run','--standalone','--format','json','--model',model,'--file',str(packet),prompt]
creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0)
p=None; exitcode=None; timed=False; err=''
t0=time.monotonic()
with stdout.open('wb') as so, stderr.open('wb') as se:
 p=subprocess.Popen(args,cwd=r'E:\TTQS',stdin=subprocess.DEVNULL,stdout=so,stderr=se,creationflags=creationflags)
 start['pid']=p.pid; start_path.write_text(json.dumps(start,ensure_ascii=False,indent=2),encoding='utf-8')
 try: exitcode=p.wait(timeout=timeout_s)
 except subprocess.TimeoutExpired:
  timed=True
  p.terminate()
  try: exitcode=p.wait(timeout=5)
  except subprocess.TimeoutExpired: p.kill(); exitcode=p.wait()
elapsed=round(time.monotonic()-t0,3); after=sha(candidate)
raw=stdout.read_bytes(); errraw=stderr.read_bytes()
models=set(); usage=[]; answer_parts=[]
for line in raw.splitlines():
 try: ev=json.loads(line)
 except Exception: continue
 def walk(x):
  if isinstance(x,dict):
   for k,v in x.items():
    if k.lower() in ('model','modelid','model_id','actual_model') and isinstance(v,str): models.add(v)
    if k.lower() in ('tokens','cost','usage') and isinstance(v,(dict,int,float)): usage.append({k:v})
    if k in ('text','content') and isinstance(v,str) and len(v)>20: answer_parts.append(v)
    walk(v)
  elif isinstance(x,list):
   for y in x: walk(y)
 walk(ev)
response='\n'.join(dict.fromkeys(answer_parts))
(outdir/'REVIEW_RESPONSE_R01.txt').write_text(response,encoding='utf-8')
status=('TIMEOUT' if timed else ('EXIT_ZERO_TEXT' if exitcode==0 and raw.strip() else ('EMPTY_OR_NO_TEXT' if exitcode==0 else 'CLI_ERROR')))
terminal={'work_id':start['work_id'],'worker':start['worker'],'started_at_local':started,'finished_at_local':now(),'duration_seconds':elapsed,'pid':p.pid if p else None,'process_created_hidden':True,'timed_out':timed,'exit_code':exitcode,'requested_model':model,'observed_model_fields':sorted(models),'actual_model':sorted(models)[0] if len(models)==1 else ('UNKNOWN' if not models else 'AMBIGUOUS:'+','.join(sorted(models))),'usage_metadata':usage,'stdout_path':str(stdout),'stdout_bytes':len(raw),'stdout_sha256':hashlib.sha256(raw).hexdigest(),'stderr_path':str(stderr),'stderr_bytes':len(errraw),'stderr_sha256':hashlib.sha256(errraw).hexdigest(),'review_response_path':str(outdir/'REVIEW_RESPONSE_R01.txt'),'review_response_sha256':sha(outdir/'REVIEW_RESPONSE_R01.txt'),'review_packet_sha256':packet_sha,'candidate_sha256_before':before,'candidate_sha256_after':after,'candidate_unchanged':before==after,'result_classification':status,'process_window':'HIDDEN_CREATE_NO_WINDOW'}
terminal_path.write_text(json.dumps(terminal,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(terminal,ensure_ascii=False))
