from pathlib import Path
import subprocess,hashlib,json,datetime,os,sys
base=Path(__file__).resolve().parents[1]; worker=base/'worker'
exe=Path(r'C:\Users\J\AppData\Roaming\ai.opencode.desktop\cli\2.1.4-x64\opencode-cli.exe')
model='opencode/deepseek-v4.1-flash-free'; bundle=worker/'OPENCODE_WRITER_INPUT_0004_R02.md'; request=worker/'OPENCODE_WRITER_REQUEST_0004_R02.txt'
out=worker/'OPENCODE_WRITER_RAW_STDOUT_R02.txt'; err=worker/'OPENCODE_WRITER_RAW_STDERR_R02.txt'; receipt=worker/'OPENCODE_WRITER_DISPATCH_R02.json'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
started=datetime.datetime.now(datetime.timezone.utc)
args=[str(exe),'run','--model',model,'--format','json','--file',str(bundle),request.read_text(encoding='utf-8')]
proc=None; status='UNKNOWN'; exitcode=None; stdout=b''; stderr=b''; timed_out=False
try:
 proc=subprocess.Popen(args,cwd=r'E:\TTQS',stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0x08000000))
 try: stdout,stderr=proc.communicate(timeout=180); exitcode=proc.returncode; status='EXITED'
 except subprocess.TimeoutExpired:
  timed_out=True; proc.kill(); stdout,stderr=proc.communicate(); exitcode=proc.returncode; status='TIMEOUT_KILLED'
except Exception as e:
 stderr=(type(e).__name__+': '+str(e)).encode('utf-8'); status='LAUNCH_ERROR'
ended=datetime.datetime.now(datetime.timezone.utc)
out.write_bytes(stdout); err.write_bytes(stderr)
obj={'work_id':'TTQS-0004-I01-E02-WRITER-R02-20261030','doc_id':'0004','requirement_id':'I01-E02','worker':'OpenCode v2 CLI','cli_path':str(exe),'cli_version':'2.1.4','model_requested':model,'model_route_actual':'UNKNOWN_PENDING_RESPONSE_INSPECTION','input_bundle_path':str(bundle),'input_bundle_sha256':sha(bundle),'request_path':str(request),'request_sha256':sha(request),'pid':proc.pid if proc else None,'start_utc':started.isoformat(),'end_utc':ended.isoformat(),'duration_seconds':round((ended-started).total_seconds(),3),'process_result':status,'exit_code':exitcode,'timed_out':timed_out,'stdout_path':str(out),'stdout_bytes':len(stdout),'stdout_sha256':sha(out),'stderr_path':str(err),'stderr_bytes':len(stderr),'stderr_sha256':sha(err),'candidate_content_adopted':False,'candidate_sha256':None,'qa':'NOT_PERFORMED','note':'Single bounded, hidden, noninteractive text-only dispatch; no --auto and stdin closed.'}
receipt.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(obj,ensure_ascii=False,indent=2))
if status!='EXITED' or exitcode!=0 or not stdout.strip(): sys.exit(1)
