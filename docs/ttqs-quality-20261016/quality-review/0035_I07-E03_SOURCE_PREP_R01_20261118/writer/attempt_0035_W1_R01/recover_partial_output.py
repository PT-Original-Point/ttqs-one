import json,hashlib,sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
p=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0035_I07-E03_SOURCE_PREP_R01_20261118\writer\attempt_0035_W1_R01\stdout.jsonl')
out=p.parent/'recovered_payloads'; out.mkdir(exist_ok=True)
counts={}; texts=[]; writes=[]; errs=[]
for n,line in enumerate(p.read_text(encoding='utf-8-sig').splitlines(),1):
 try:o=json.loads(line)
 except: continue
 t=o.get('type'); counts[t]=counts.get(t,0)+1; part=o.get('part') or {}
 if t=='text' and part.get('text'): texts.append((n,part['text']))
 if t=='tool_use' and part.get('tool')=='write':
  state=part.get('state') or {}; content=((state.get('input') or {}).get('content'))
  if isinstance(content,str):
   f=out/f'WRITE_INPUT_LINE_{n}.md';f.write_text(content,encoding='utf-8');writes.append({'line':n,'status':state.get('status'),'path':(state.get('input') or {}).get('path'),'chars':len(content),'sha256':hashlib.sha256(f.read_bytes()).hexdigest().upper(),'saved':str(f)})
 if t=='error': errs.append({'line':n,'error':o.get('error')})
for n,t in texts:
 f=out/f'TEXT_EVENT_LINE_{n}.md';f.write_text(t,encoding='utf-8')
summary={'event_counts':counts,'text_events':[{'line':n,'chars':len(t),'sha256':hashlib.sha256(t.encode()).hexdigest().upper(),'path':str(out/f'TEXT_EVENT_LINE_{n}.md'),'prefix':t[:320],'suffix':t[-320:]} for n,t in texts],'write_inputs':writes,'errors':errs,'stdout_sha256':hashlib.sha256(p.read_bytes()).hexdigest().upper(),'stdout_bytes':p.stat().st_size}
print(json.dumps(summary,ensure_ascii=False))
