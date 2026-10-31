import sqlite3, pathlib, datetime, json
from zoneinfo import ZoneInfo
pkg=pathlib.Path(r'E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0104_I18-E11_R15_20261022')
db=pathlib.Path(r'C:\Users\J\.local\share\opencode\opencode.db')
now=datetime.datetime.now(ZoneInfo('Asia/Taipei')); start=now-datetime.timedelta(hours=24); start_ms=int(start.timestamp()*1000)
c=sqlite3.connect('file:'+str(db)+'?mode=ro',uri=True); c.row_factory=sqlite3.Row
rows=c.execute("select id,title,directory,agent,model,cost,tokens_input,tokens_output,tokens_reasoning,tokens_cache_read,tokens_cache_write,time_created,time_updated,idle_outcome from session_v2 where (time_created>=? or time_updated>=?) and directory like 'E:/TTQS%' order by time_created",(start_ms,start_ms)).fetchall()
def dt(ms): return datetime.datetime.fromtimestamp(ms/1000,ZoneInfo('Asia/Taipei')).isoformat(timespec='milliseconds')
def modelid(s):
 try:return json.loads(s).get('id','UNKNOWN')
 except:return 'UNKNOWN'
records=[]; groups={}
for r in rows:
 d=dict(r); m=modelid(d['model']); g=groups.setdefault(m,{'sessions':0,'input':0,'output':0,'reasoning':0,'cache_read':0,'cache_write':0,'local_cost':0.0})
 g['sessions']+=1
 for src,dst in [('tokens_input','input'),('tokens_output','output'),('tokens_reasoning','reasoning'),('tokens_cache_read','cache_read'),('tokens_cache_write','cache_write')]:g[dst]+=d[src]
 g['local_cost']+=d['cost'] or 0.0
 records.append({'session_id':d['id'],'title':d['title'],'directory':d['directory'],'agent':d['agent'],'selected_model':m,'actual_serving_model':'UNKNOWN','local_cost':d['cost'],'tokens':{'input':d['tokens_input'],'output':d['tokens_output'],'reasoning':d['tokens_reasoning'],'cache_read':d['tokens_cache_read'],'cache_write':d['tokens_cache_write']},'started_at_tpe':dt(d['time_created']),'last_updated_at_tpe':dt(d['time_updated']),'idle_outcome':d['idle_outcome']})
total={k:sum(g[k] for g in groups.values()) for k in ('input','output','reasoning','cache_read','cache_write','local_cost')}
agg={'receipt_id':'TTQS_ONE_OPENCODE_SESSION_USAGE_ROLLING_24H','observed_at_tpe':now.isoformat(),'window_start_tpe':start.isoformat(),'window_end_tpe':now.isoformat(),'db_path':str(db),'db_read_only':True,'scope_filter':'session_v2 rows whose creation or update was inside the window and directory starts E:/TTQS','session_rows':len(records),'exact_cli_invocation_count':'UNKNOWN; native session rows are not invocation attempts','actual_serving_model_identity':'UNKNOWN; selected model IDs are recorded, provider serving/fallback not independently attested','groups':groups,'total':total,'records':records,'limitations':['A CLI invocation that created no session may be absent.','Local cost field is not a vendor invoice or billing proof.']}
(pkg/'evidence/worker_dispatch_24h_opencode.json').write_text(json.dumps({'observed_at_tpe':now.isoformat(),'window_start_tpe':start.isoformat(),'session_rows':len(records),'rows':records},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(pkg/'evidence/worker_dispatch_24h_opencode_aggregate.json').write_text(json.dumps(agg,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lines=[f'# Rolling 24-hour OpenCode v2 reconciliation','',f"Observed {now.isoformat()}; window {start.isoformat()} to {now.isoformat()} (Asia/Taipei).",'',f"- Native SQLite TTQS session rows: **{len(records)}**. These are not exact CLI launch attempts; invocation count remains **UNKNOWN**.",f"- Token totals from native `session_v2`: input {total['input']:,}; output {total['output']:,}; reasoning {total['reasoning']:,}; cache-read {total['cache_read']:,}; cache-write {total['cache_write']:,}.",f"- Local SQLite cost sum: {total['local_cost']:.2f}; vendor billing remains **UNKNOWN**.",'- Selected model IDs are recorded by OpenCode; actual serving-model identity/fallback is **UNKNOWN**.','', '| Selected model (not serving attestation) | Sessions | Input | Output | Reasoning | Cache read | Local cost |','|---|---:|---:|---:|---:|---:|---:|']
for m,g in sorted(groups.items()):lines.append(f"| {m} | {g['sessions']} | {g['input']:,} | {g['output']:,} | {g['reasoning']:,} | {g['cache_read']:,} | {g['local_cost']:.2f} |")
lines += ['', 'R15 review `ses_ea030cfffffeWft8qAw18cKX1E` is a terminal native session (`idle_outcome=succeeded`) on selected `mimo-v2.6-flash-free`, with 70,570 input / 8,130 output / 41,871 reasoning / 680,960 cache-read, local cost 0.00. Its shell CLI exit was 1; raw response was recovered, and the independent verdict is PARTIAL.', '']
(pkg/'evidence/worker_dispatch_24h_summary.md').write_text('\n'.join(lines),encoding='utf-8')
print('observed',now.isoformat(),'window_start',start.isoformat(),'rows',len(records),'total',json.dumps(total))
for m,g in sorted(groups.items()):print(m,g)
