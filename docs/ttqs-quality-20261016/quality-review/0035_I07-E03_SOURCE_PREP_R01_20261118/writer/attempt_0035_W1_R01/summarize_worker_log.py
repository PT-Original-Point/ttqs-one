import json,hashlib,sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
p=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0035_I07-E03_SOURCE_PREP_R01_20261118\writer\attempt_0035_W1_R01\stdout.jsonl')
counts={}; events=[]; calls=[]; texts=[]; errors=[]
for n,line in enumerate(p.read_text(encoding='utf-8-sig').splitlines(),1):
 try:o=json.loads(line)
 except Exception as e: print('BAD_JSON',n,str(e)); continue
 t=o.get('type'); counts[t]=counts.get(t,0)+1; events.append(o)
 if t=='text' and (o.get('part') or {}).get('text'): texts.append((n,o))
 if t=='tool_use':
  part=o.get('part') or {}; state=part.get('state') or {}; calls.append({'line':n,'tool':part.get('tool'),'status':state.get('status'),'input':state.get('input'),'output_tail':str(state.get('output') or '')[-400:]})
 if t=='error': errors.append(o.get('error'))
summary={'event_counts':counts,'line_count':len(events),'text_events':len(texts),'text_event_summaries':[{'line':n,'chars':len((o.get('part') or {}).get('text','')),'tail':(o.get('part') or {}).get('text','')[-800:]} for n,o in texts[-5:]],'tool_calls':calls[-12:],'errors':errors,'last_events':[{'type':o.get('type'),'timestamp':o.get('timestamp'),'reason':(o.get('part') or {}).get('reason')} for o in events[-5:]],'log_bytes':p.stat().st_size,'log_sha256':hashlib.sha256(p.read_bytes()).hexdigest().upper()}
print(json.dumps(summary,ensure_ascii=False))
