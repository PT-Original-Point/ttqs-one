from pathlib import Path
import subprocess, hashlib, json, datetime, time, sys
PKG=Path(r'E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0104_I18-E11_R15_20261022')
REVIEW=PKG/'review'/'R16'
EXE=Path(r'C:\Users\J\AppData\Roaming\ai.opencode.desktop\cli\2.0.32-x64\opencode-cli.exe')
PACKET=REVIEW/'review_packet_0104_R16.md'
MODELS=REVIEW/'opencode_models_snapshot_R16.txt'
OUT=REVIEW/'opencode_review_stdout_R16.jsonl'
ERR=REVIEW/'opencode_review_stderr_R16.bin'
RECEIPT=REVIEW/'opencode_review_execution_receipt_R16.json'
START=REVIEW/'dispatch_started_R16.json'
def h(b): return hashlib.sha256(b).hexdigest()
if RECEIPT.exists() or START.exists():
    raise SystemExit('Refusing duplicate R16 reviewer dispatch: marker or receipt already exists')
if not EXE.is_file() or not PACKET.is_file() or not MODELS.is_file():
    raise SystemExit('Missing exact CLI, packet, or model-catalog snapshot')
if 'opencode/mimo-v2.6-flash-free' not in MODELS.read_text(encoding='utf-8',errors='replace'):
    raise SystemExit('Selected free SKU is absent from current CLI model list; dispatch not started')
model='opencode/mimo-v2.6-flash-free'
prompt=('Independently review the attached R16 packet for DOCX 0104 / I18-E11 / official checkbox 112. '
        'Use only the provided packet. Do not use tools, read/write files, or infer facts. '
        'Return concise JSON with verdict PASS/PARTIAL/FAIL, exact candidate SHA, blocking findings with precise locators, '
        'nonblocking findings, closure results for RF-1 through RF-10, and scope limitations. '
        'This is TEXT_ONLY; do not claim visual inspection, actual human usability testing, REAL association evidence, or formal acceptance.')
args=[str(EXE),'run','--model',model,'--agent','plan','--format','json','--title','TTQS 0104 R16 exact-SHA independent semantic review','--file',str(PACKET),prompt]
started=datetime.datetime.now().astimezone().isoformat()
marker={'work_id':'TTQS-0104-I18-E11-R16-INDEPENDENT-REVIEW-20261022','attempt_id':'TTQS-0104-R16-REVIEW-ATTEMPT-01','started_at_tpe':started,'cli_path':str(EXE),'requested_model':model,'packet_sha256':h(PACKET.read_bytes()),'candidate_sha256':'9a074b207e7a57f1448cf96868f3cc3f30a72834a021f9b04392909ea3183d7b','models_snapshot_sha256':h(MODELS.read_bytes()),'agent':'plan','format':'json','auto_approval':False,'tools_authorized':False}
START.write_text(json.dumps(marker,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
t0=time.monotonic(); proc=subprocess.Popen(args,cwd=str(PKG),stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=False)
try:
    stdout,stderr=proc.communicate(timeout=2700); timed_out=False
except subprocess.TimeoutExpired:
    proc.kill(); stdout,stderr=proc.communicate(); timed_out=True
ended=datetime.datetime.now().astimezone().isoformat()
OUT.write_bytes(stdout); ERR.write_bytes(stderr)
receipt={**marker,'ended_at_tpe':ended,'elapsed_seconds':round(time.monotonic()-t0,3),'os_pid':proc.pid,'cli_exit_code':proc.returncode,'timed_out':timed_out,'stdout_path':str(OUT),'stdout_bytes':len(stdout),'stdout_sha256':h(stdout),'stderr_path':str(ERR),'stderr_bytes':len(stderr),'stderr_sha256':h(stderr),'actual_serving_model':'UNKNOWN pending native OpenCode session/provider evidence','native_session_id':'UNKNOWN pending native session reconciliation','native_usage':'UNKNOWN pending native session reconciliation','vendor_billing':'UNKNOWN','terminal_verdict':'PENDING_NATIVE_OUTPUT_RECONCILIATION'}
RECEIPT.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ['work_id','attempt_id','requested_model','os_pid','cli_exit_code','timed_out','elapsed_seconds','stdout_bytes','stdout_sha256','stderr_bytes','stderr_sha256','packet_sha256','candidate_sha256','terminal_verdict']},ensure_ascii=False,indent=2))
