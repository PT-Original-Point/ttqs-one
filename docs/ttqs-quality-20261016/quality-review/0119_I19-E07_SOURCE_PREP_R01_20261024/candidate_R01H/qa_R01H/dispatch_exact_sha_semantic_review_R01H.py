from pathlib import Path
import hashlib,json,datetime,time,subprocess
from docx import Document
from pypdf import PdfReader
base=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0119_I19-E07_SOURCE_PREP_R01_20261024')
root=base/'candidate_R01H'; qa=root/'qa_R01H'; bundle=qa/'review_bundle_R01H'; bundle.mkdir(parents=True,exist_ok=True)
candidate=root/'0119__目標市場及顧客價值部分提升證據分析表_R01H.docx'
expected='60169b73895fc24bb1a0397534aa0ede37776c1ca3b7631a848bf4b69a9d312a'
sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(candidate.read_bytes())==expected, 'candidate exact SHA drift; refusing dispatch'
src=base/'source'/'SOURCE_PACKET_0119_I19-E07_R01.md'; bp=base/'source'/'UNIQUE_BLUEPRINT_0119_I19-E07_R01.md'; mapping=base/'source'/'mapping_evidence_0119_R01.json'
pdf=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\official_source_0108_r11.pdf')
rawhash={'source_packet':sha(src.read_bytes()),'unique_blueprint':sha(bp.read_bytes()),'mapping':sha(mapping.read_bytes()),'official_pdf':sha(pdf.read_bytes())}
reader=PdfReader(str(pdf)); page8=reader.pages[7].extract_text() or ''
(bundle/'official_requirement_page8.txt').write_text(page8,encoding='utf-8')
doc=Document(str(candidate)); chunks=[]; table_no=0
for item in doc.iter_inner_content():
 if hasattr(item,'rows'):
  table_no+=1;chunks.append(f'\n[TABLE {table_no}]')
  for row in item.rows:chunks.append(' | '.join(cell.text.replace('\n',' / ') for cell in row.cells))
 else:
  t=item.text.strip()
  if t:chunks.append(t)
body='\n'.join(chunks)+'\n'; (bundle/'candidate_text_exact_R01H.md').write_text(body,encoding='utf-8')
for p,n in [(src,'SOURCE_PACKET_0119_I19-E07_R01.md'),(bp,'UNIQUE_BLUEPRINT_0119_I19-E07_R01.md'),(mapping,'mapping_evidence_0119_R01.json')]: (bundle/n).write_bytes(p.read_bytes())
files={p.name:{'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in bundle.iterdir() if p.is_file()}
manifest={'doc_id':'0119','requirement_id':'I19-E07','candidate':'R01H','candidate_sha256':expected,'candidate_text_sha256':sha(body.encode('utf-8')),'source_packet_sha256':rawhash['source_packet'],'unique_blueprint_sha256':rawhash['unique_blueprint'],'mapping_sha256':rawhash['mapping'],'official_pdf_sha256':rawhash['official_pdf'],'official_page8_text_sha256':sha(page8.encode('utf-8')),'bundle_files':files,'review_scope':'read-only semantic review of the complete extracted exact-SHA DOCX text against official I19-E07, source packet, unique Blueprint and mapping; visual verification is separately bound by local receipt; excludes real association evidence and formal acceptance'}
(bundle/'review_input_manifest_R01H.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
contents={n:(bundle/n).read_text(encoding='utf-8') for n in ['official_requirement_page8.txt','SOURCE_PACKET_0119_I19-E07_R01.md','UNIQUE_BLUEPRINT_0119_I19-E07_R01.md','mapping_evidence_0119_R01.json','candidate_text_exact_R01H.md']}
prompt='''READ-ONLY independent semantic review for TTQS ONE. All review inputs are embedded below. Do not call tools, browse, read or write files, run commands, use Computer Use, or infer external facts. Return one compact JSON object in Traditional Chinese, maximum 1800 Chinese words, with no markdown fences.

BINDING: doc_id=0119; official requirement=I19-E07; candidate=R01H; exact DOCX SHA-256='''+expected+'; extracted text SHA-256='+manifest['candidate_text_sha256']+'''. Review the complete candidate text against the embedded official requirement, source packet, unique Blueprint, and mapping. Verdict must be PASS, PARTIAL or FAIL. Include exact binding fields, overall verdict, title-blind genre verdict, a 10-row checklist (official alignment; correct genre; both construct definitions; valid n/N, exclusions, periods and comparability; all calculations; usable forms and small-association workflow; missing/negative/zero-denominator/permission/hold and rejection rules; evidence and replacement registers; cross-document boundaries; SAMPLE/REAL and candidate/approval boundaries), precise section/table locators, blockers, nonblocking findings, visual review marked OUT_OF_SCOPE_LOCAL_VISUAL_RECEIPT, formal_acceptance=NOT_GRANTED. Recompute values from shown numbers. Treat all demonstrations as synthetic; do not claim association performance, approvals, signatures, third-party sources, or TTQS acceptance. If any essential requirement is not supported, do not return PASS. Distinguish official page 8, candidate-list ordinal 131, seed row 119, crosswalk row 106, doc_id 0119, and official printed checkbox serial UNKNOWN_NOT_ASSERTED; never substitute one for another. For the nearest wrong-document risks compare I19-E05 receipt custody, I19-E08 training result, I19-E04 exam result, and I19-E03 employment status; do not use them as substitutes for I19-E07. The exact document bytes and layout are not within your independent recalculation scope; bind your verdict only to the provided exact extracted text SHA and preserve the given exact DOCX SHA as identifier.

=== OFFICIAL REQUIREMENT: VERIFIED SOURCE PDF PAGE 8 ===
'''+contents['official_requirement_page8.txt']+'\n=== SOURCE PACKET ===\n'+contents['SOURCE_PACKET_0119_I19-E07_R01.md']+'\n=== UNIQUE BLUEPRINT ===\n'+contents['UNIQUE_BLUEPRINT_0119_I19-E07_R01.md']+'\n=== SOURCE MAPPING ===\n'+contents['mapping_evidence_0119_R01.json']+'\n=== COMPLETE EXACT EXTRACTED CANDIDATE TEXT ===\n'+contents['candidate_text_exact_R01H.md']
(bundle/'review_prompt_R01H.txt').write_text(prompt,encoding='utf-8')
agy=Path(r'C:\Users\J\AppData\Local\agy\bin\agy.exe')
version=subprocess.run([str(agy),'--version'],capture_output=True,text=True,timeout=15,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
args=[str(agy),'--model','gemini-3.8-flash-high','--effort','high','--disable-slash-commands','--mode','plan','--input-format','stream-json','--output-format','stream-json']
out=bundle/'antigravity_stdout_R01H.ndjson';err=bundle/'antigravity_stderr_R01H.txt';resp=bundle/'antigravity_response_R01H.txt'
start=datetime.datetime.now().astimezone().isoformat();tick=time.monotonic();flags=getattr(subprocess,'CREATE_NO_WINDOW',0)
with out.open('wb') as fo,err.open('wb') as fe:
 proc=subprocess.Popen(args,cwd=str(bundle),stdin=subprocess.PIPE,stdout=fo,stderr=fe,creationflags=flags)
 pid=proc.pid;proc.stdin.write((json.dumps({'event':'user','message':{'content':prompt}},ensure_ascii=False)+'\n').encode('utf-8'));proc.stdin.close()
 try: rc=proc.wait(timeout=300);timed=False
 except subprocess.TimeoutExpired: proc.kill();rc=None;timed=True
raw=out.read_bytes();events=[];model='UNKNOWN';toolcalls=[];response='';usage={}
for line in raw.decode('utf-8','replace').splitlines():
 try:e=json.loads(line)
 except:continue
 events.append(e)
 if e.get('event')=='init': model=(e.get('init') or {}).get('model','UNKNOWN')
 if e.get('event')=='step_update':
  u=e.get('step_update') or {}
  if u.get('step_type')=='tool_call':toolcalls.append(u)
 if e.get('event')=='result':
  v=e.get('result') or {};response=v.get('response') or '';usage=v.get('usage') or {}
  if model=='UNKNOWN':model=v.get('model','UNKNOWN')
if response:resp.write_text(response,encoding='utf-8')
rec={'work_id':'TTQS_ONE-0119-I19-E07-R01H-EXACT-SHA-SEMANTIC-REVIEW','doc_id':'0119','requirement_id':'I19-E07','candidate':'R01H','candidate_sha256':expected,'candidate_text_sha256':manifest['candidate_text_sha256'],'source_packet_sha256':rawhash['source_packet'],'unique_blueprint_sha256':rawhash['unique_blueprint'],'mapping_sha256':rawhash['mapping'],'official_pdf_sha256':rawhash['official_pdf'],'official_page8_text_sha256':manifest['official_page8_text_sha256'],'prompt_sha256':sha(prompt.encode()),'cli_version':version.stdout.strip() or version.stderr.strip(),'worker':'Antigravity CLI','requested_model':'gemini-3.8-flash-high','actual_model_from_init':model,'pid':pid,'started_at_local':start,'elapsed_seconds':round(time.monotonic()-tick,3),'exit_code':rc,'timed_out':timed,'tool_call_count':len(toolcalls),'no_tool_calls_observed':len(toolcalls)==0,'ndjson_event_count':len(events),'stdout_bytes':len(raw),'stdout_sha256':sha(raw),'stderr_sha256':sha(err.read_bytes()),'response_path':str(resp) if response else None,'response_sha256':sha(response.encode()) if response else None,'usage':usage,'dispatch_integrity':'PASS' if response and not timed and rc==0 and model=='gemini-3.8-flash-high' and not toolcalls else 'FAIL_OR_UNKNOWN','semantic_verdict':'PENDING_MANUAL_ADJUDICATION','formal_acceptance':'NOT_GRANTED'}
(bundle/'dispatch_receipt_R01H.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:rec[k] for k in ['work_id','candidate_sha256','cli_version','requested_model','actual_model_from_init','pid','elapsed_seconds','exit_code','timed_out','tool_call_count','stdout_bytes','response_path','response_sha256','usage','dispatch_integrity']},ensure_ascii=True))
