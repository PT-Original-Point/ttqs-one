import sqlite3,pathlib,json,hashlib,datetime
from zoneinfo import ZoneInfo
pkg=pathlib.Path(r'E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0104_I18-E11_R15_20261022');db=pathlib.Path(r'C:\Users\J\.local\share\opencode\opencode.db');sid='ses_ea00e6c9bffeRq91HBDZl6RZBb';pid=55724
c=sqlite3.connect('file:'+str(db)+'?mode=ro',uri=True);c.row_factory=sqlite3.Row
s=c.execute('select * from session_v2 where id=?',(sid,)).fetchone();m=c.execute("select * from session_message where session_id=? and type='assistant' order by seq desc limit 1",(sid,)).fetchone();idle=c.execute("select data from session_message where session_id=? and type='idle' order by seq desc limit 1",(sid,)).fetchone()
if not s or not m or not idle: raise SystemExit('native session terminal evidence incomplete')
data=json.loads(m['data']);contents=data.get('content',[]);texts=[x.get('text','') for x in contents if x.get('type')=='text'];response='\n'.join(texts)
if not response: raise SystemExit('no response text in native session')
raw_message=m['data'].encode('utf-8');p_response=pkg/'writer/opencode_writer_R16_response.md';p_raw=pkg/'writer/opencode_writer_R16_native_message.json';p_response.write_text(response,encoding='utf-8');p_raw.write_bytes(raw_message)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def local(ms):return datetime.datetime.fromtimestamp(ms/1000,ZoneInfo('Asia/Taipei')).isoformat(timespec='milliseconds')
try: model=json.loads(s['model']).get('id','UNKNOWN')
except: model='UNKNOWN'
packet=pkg/'writer/TASK_PACKET_0104_R16_BOUNDED_REPAIR.md'
receipt={'receipt_id':'TTQS-0104-R16-OPENCODE-WRITER-NATIVE-RECOVERY','work_id':'TTQS-0104-I18-E11-R16-BOUNDED-REPAIR-20261022','doc_id':'0104','requirement_id':'I18-E11','checkbox':'112','input_candidate_sha256':'9bbb96da74ba9da845ab0e063421d04f035e79496209a02de1f04b0c98ec7eb8','packet_sha256':sha(packet),'worker':'OpenCode CLI v2.0.32','requested_model':'opencode/deepseek-v4.1-flash-free','native_session_selected_model':model,'actual_serving_model':'UNKNOWN','agent':s['agent'],'session_id':sid,'os_pid':pid,'process_created_observed_tpe':'2026-10-22T03:30:29+08:00','session_started_tpe':local(s['time_created']),'session_completed_tpe':local(s['time_idle']),'native_session_idle_outcome':json.loads(idle['data']).get('outcome'),'assistant_finish':data.get('finish'),'cli_process_exit_code':'UNKNOWN_NOT_CAPTURED','wrapper_error':'PowerShell wrapper tried assigning the automatic read-only variable $PID before beginning stream capture; task was already dispatched. No stdout/stderr capture file was opened. Recovered terminal assistant text and native session metadata from read-only OpenCode SQLite session records; no duplicate dispatch.','stdout_capture':'UNAVAILABLE; native session message JSON preserved instead','native_usage':{'input':s['tokens_input'],'output':s['tokens_output'],'reasoning':s['tokens_reasoning'],'cache_read':s['tokens_cache_read'],'cache_write':s['tokens_cache_write'],'local_cost':s['cost'],'vendor_billing':'UNKNOWN'},'response_path':str(p_response),'response_bytes':p_response.stat().st_size,'response_sha256':sha(p_response),'native_message_path':str(p_raw),'native_message_bytes':p_raw.stat().st_size,'native_message_sha256':sha(p_raw),'actual_output_status':'RECOVERED_FROM_NATIVE_SESSION; patch plan requires independent deterministic validation before adoption'}
(p_pkg:=pkg/'writer/opencode_writer_dispatch_recovery_R16.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('native_session',sid,'idle',receipt['native_session_idle_outcome'],'selected_model',model,'tokens',receipt['native_usage'])
print('response_bytes',p_response.stat().st_size,'response_sha256',sha(p_response),'raw_message_sha256',sha(p_raw))
print('dispatch_receipt_sha256',sha(p_pkg))
print('response_preview',response[:1600].replace('\n',' '))
