from pathlib import Path
import hashlib,json,subprocess,time,datetime,re,os,sys
from docx import Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.text.paragraph import Paragraph
from docx.table import Table

base=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0012_I02-E03_LUNA_TEXT_DRAFT_R01_20261029")
qa=base/"qa"
cand=base/"candidate"/"0012_I02-E03_R06.docx"
old=base/"candidate"/"0012_I02-E03_R05.docx"
pkg=base/"package"/"0012_I02-E03_R05"
work=qa/"W1_SEMANTIC_REVIEW_R06_DOCX_20261030"
work.mkdir(parents=True,exist_ok=True)
sha=lambda b:hashlib.sha256(b).hexdigest()
now=lambda:datetime.datetime.now().astimezone().isoformat()
expected="f4c7a8242cb5ae0c4c038d546b2d45cac938028a521ea6ffcb5cc02334c03d13"
docbytes=cand.read_bytes()
if sha(docbytes)!=expected: raise SystemExit("R06 candidate SHA changed; refusing dispatch")
oldsha="a90340289d360a7705fad8137db3a33b648a126ca67b1454d66c0b9288f9d9b5"
if sha(old.read_bytes())!=oldsha: raise SystemExit("R05 baseline SHA changed; refusing delta review")
mapping=json.loads((pkg/"evidence"/"official_blueprint_mapping.json").read_text(encoding="utf-8"))
tech=json.loads((qa/"technical_qa_R06.json").read_text(encoding="utf-8"))
visual=json.loads((qa/"visual_qa_R06.json").read_text(encoding="utf-8"))
regpath=qa/"R06_SCOPED_REPAIR_20261030"/"SYNTHETIC_REPLACEMENT_REGISTER_R06.csv"
reg=regpath.read_text(encoding="utf-8-sig")
prior=qa/"W1_SEMANTIC_REVIEW_R06_20261030"/"REVIEW_RESPONSE.md"
prior_text=prior.read_text(encoding="utf-8")
blueprint=mapping.get("blueprint_exact_row",{})
def get_blocks(path):
    d=Document(str(path)); out=[]
    for child in d.element.body.iterchildren():
        if isinstance(child,CT_P):
            t=Paragraph(child,d).text.strip()
            if t: out.append(("P",t))
        elif isinstance(child,CT_Tbl):
            t=Table(child,d)
            rows=[[" ".join(c.text.replace("\n"," / ").split()) for c in row.cells] for row in t.rows]
            out.append(("T",rows))
    return out
blocks=get_blocks(cand)
def section(n):
    start=None
    for i,(kind,x) in enumerate(blocks):
        if kind=="P" and re.match(rf"^{n}[.、．\s]",x):
            start=i; break
    if start is None: raise SystemExit(f"section {n} not found")
    end=len(blocks)
    for i in range(start+1,len(blocks)):
        kind,x=blocks[i]
        if kind=="P" and re.match(r"^\d{1,2}[.、．\s]",x):
            end=i; break
    out=[]
    for kind,x in blocks[start:end]:
        if kind=="P": out.append(x)
        else: out.append("[TABLE]\n"+"\n".join(" | ".join(row) for row in x)+"\n[/TABLE]")
    return "\n\n".join(out)
def relevant_map():
    keys=["document_id","requirement_id","official_checkbox_text","official_requirement_text","official_evidence_table_page","official_source_readback_status","official_requirement_pdf_sha256","unique_blueprint_row_sha256","blueprint_file_sha256","negative_neighbors"]
    base_map={k:mapping.get(k) for k in keys}
    bpkeys=["document_genre","document_purpose","evidence_role","required_sections","required_tables_or_figures","required_fields_or_questions","required_calculations_or_analysis","required_cross_references","real_data_required","third_party_evidence_required","prohibited_fabrication","title_blind_test","negative_choice_neighbors","acceptance_tests"]
    base_map["unique_blueprint_row"]={k:blueprint.get(k) for k in bpkeys}
    return base_map
parts=[
"# 0012 / I02-E03 R06 獨立語意差異審查包",
f"R06 candidate DOCX SHA-256: {sha(docbytes)}",
f"R05 baseline DOCX SHA-256: {oldsha}",
"審查範圍：僅針對 R05 已獨立語意 PASS 但有明示 Finding 的修補差異，以及這些差異在 R06 的定位與一致性；其餘未改正文只有在差異證據支持時才可沿用 R05 範圍。請明確判定能否沿用，不能則標 PARTIAL，不得自行擴大成全文件 PASS。",
"## 官方要求與唯一 Blueprint 對照\n"+json.dumps(relevant_map(),ensure_ascii=False,indent=2),
"## R05 既有獨立審查原始回覆\n"+prior_text,
"## R06 §5（期限修補定位）\n"+section(5),
"## R06 §12（完整示例及合成事實清冊）\n"+section(12),
"## R06 §13（控制資料與接受狀態）\n"+section(13),
"## R06 synthetic replacement register（完整）\n"+reg,
"## R06 deterministic technical receipt（僅背景，不代替語意判斷）\n"+json.dumps(tech,ensure_ascii=False,indent=2),
"## R06 full-page visual receipt（僅版面範圍）\n"+json.dumps(visual,ensure_ascii=False,indent=2),
"## R06 source draft copy SHA-256\n"+json.dumps({"source_path":str(base/"worker"/"luna_subagent_draft_R01_R06_scoped_repair.md"),"source_sha256":sha((base/"worker"/"luna_subagent_draft_R01_R06_scoped_repair.md").read_bytes()),"register_sha256":sha(reg.encode("utf-8"))},ensure_ascii=False,indent=2)
]
packet="\n\n".join(parts)
packetpath=work/"REVIEW_PACKET_R06.md"
packetpath.write_text(packet,encoding="utf-8")
packetsha=sha(packet.encode("utf-8"))
cli=Path(r"C:\Users\J\AppData\Roaming\npm\node_modules\@opencode\cli\bin\opencode.exe")
if not cli.is_file(): raise SystemExit("OpenCode CLI executable missing")
vr=subprocess.run([str(cli),"--version"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=15,creationflags=getattr(subprocess,"CREATE_NO_WINDOW",0))
version=(vr.stdout or vr.stderr).strip()
if "2.2.3" not in version: raise SystemExit(f"CLI version changed; current version is {version}")
# Recheck processes; the known desktop resident service is not an active task writer.
ps="$ErrorActionPreference='SilentlyContinue'; Get-CimInstance Win32_Process | Where-Object { $_.Name -match 'opencode' } | Select-Object ProcessId,Name,ExecutablePath,CommandLine | ConvertTo-Json -Compress"
pr=subprocess.run(["powershell.exe","-NoProfile","-Command",ps],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=15,creationflags=getattr(subprocess,"CREATE_NO_WINDOW",0))
proc_text=pr.stdout.strip()
try: proc_list=json.loads(proc_text) if proc_text else []
except Exception: proc_list=[]
if isinstance(proc_list,dict): proc_list=[proc_list]
task_procs=[]
for item in proc_list:
    path=(item.get("ExecutablePath") or "").lower()
    cmd=(item.get("CommandLine") or "").lower()
    if "ai.opencode.desktop\\cli\\" in path and "serve --service" in cmd: continue
    if "ai.opencode.desktop\\cli\\" in path and not cmd: continue
    if "opencode" in path or ("opencode" in cmd and "serve --service" not in cmd): task_procs.append(item)
if task_procs: raise SystemExit("active OpenCode task process detected; refusing duplicate dispatch")
model="opencode/glm-5.3-flash-free"
work_id="TTQS-0012-W1-SEMANTIC-R06-DELTA-20261030-01"
prompt=("Act as an independent semantic/usability reviewer of the supplied exact-SHA review packet. Do not use tools, edit files, browse, or claim visual inspection. Bind every finding to R06 SHA-256 f4c7a8242cb5ae0c4c038d546b2d45cac938028a521ea6ffcb5cc02334c03d13. "
"Review whether prior R05 PASS can be inherited for unchanged scope, and directly inspect R06 sections 5, 12 and 13 plus the full synthetic register. Specifically adjudicate prior F1 service-time locators for SYN-037/038/039, F2 terminology consistency, residual F3 required-table schema and F4 evaluator-facing hash/control language; verify no change creates arithmetic, SAMPLE/REAL, fabricated-approval, requirement/Blueprint or negative-neighbor defect. "
"Return concise Markdown: overall PASS/PARTIAL/FAIL for this bounded semantic delta only; exact doc_id/requirement_id/candidate SHA; inherited prior scope and its basis; each finding with section/table/row locator and severity; arithmetic/real-boundary checks; unresolved UNKNOWN/HOLD; formal acceptance NOT_GRANTED. If packet evidence is insufficient, say so.")
promptpath=work/"PROMPT_R06.txt"
promptpath.write_text(prompt,encoding="utf-8")
stdout=work/"RAW_STDOUT.jsonl"; stderr=work/"RAW_STDERR.txt"
startpath=work/"DISPATCH_START.json"; termpath=work/"DISPATCH_TERMINAL.json"
start={"project_id":"TTQS_ONE","work_id":work_id,"doc_id":"0012","requirement_id":"I02-E03","stage":"READY_INDEPENDENT_SEMANTIC_DELTA","candidate_sha256":expected,"baseline_candidate_sha256":oldsha,"review_packet_sha256":packetsha,"review_packet_path":str(packetpath),"requested_model":model,"actual_model":"UNKNOWN_PENDING_SESSION_METADATA","cli_path":str(cli),"cli_version":version,"pre_dispatch_processes":proc_list,"active_task_writer_detected":False,"started_at_local":now(),"process_window":"HIDDEN_CREATE_NO_WINDOW","agent":"plan","timeout_seconds":480}
startpath.write_text(json.dumps(start,ensure_ascii=False,indent=2),encoding="utf-8")
args=[str(cli),"run","--standalone","--format","json","--model",model,"--agent","plan","--file",str(packetpath),prompt]
t0=time.monotonic()
with stdout.open("wb") as so, stderr.open("wb") as se:
    p=subprocess.Popen(args,cwd=r"E:\TTQS",stdin=subprocess.DEVNULL,stdout=so,stderr=se,creationflags=getattr(subprocess,"CREATE_NO_WINDOW",0))
    start["pid"]=p.pid; startpath.write_text(json.dumps(start,ensure_ascii=False,indent=2),encoding="utf-8")
    try: code=p.wait(timeout=480); timed=False
    except subprocess.TimeoutExpired:
        timed=True; p.terminate()
        try: code=p.wait(timeout=5)
        except subprocess.TimeoutExpired: p.kill(); code=p.wait()
elapsed=round(time.monotonic()-t0,3)
raw=stdout.read_bytes(); err=stderr.read_bytes(); texts=[]; models=set(); sessions=set(); usage=[]
def walk(x):
    if isinstance(x,dict):
        for k,v in x.items():
            kl=k.lower()
            if kl in ("model","modelid","model_id","actual_model") and isinstance(v,str): models.add(v)
            if kl in ("sessionid","session_id") and isinstance(v,str): sessions.add(v)
            if kl in ("usage","tokens","cost") and isinstance(v,(dict,int,float)): usage.append({k:v})
            if kl in ("text","content") and isinstance(v,str) and len(v)>40: texts.append(v)
            walk(v)
    elif isinstance(x,list):
        for y in x: walk(y)
for line in raw.splitlines():
    try: walk(json.loads(line))
    except Exception: pass
response="\n".join(dict.fromkeys(texts)).strip()
if response: (work/"REVIEW_RESPONSE.md").write_text(response,encoding="utf-8")
after=sha(cand.read_bytes())
term={"project_id":"TTQS_ONE","work_id":work_id,"doc_id":"0012","requirement_id":"I02-E03","candidate_sha256_before":expected,"candidate_sha256_after":after,"candidate_unchanged":expected==after,"body_scope":"§5, §12, §13 and full synthetic register; unchanged scope inheritance explicitly conditioned on R05 exact-SHA review and R05-to-R06 diff","review_packet_sha256":packetsha,"requested_model":model,"observed_model_fields":sorted(models),"actual_model":sorted(models)[0] if len(models)==1 else ("UNKNOWN" if not models else "AMBIGUOUS:"+",".join(sorted(models))),"session_ids":sorted(sessions),"usage_metadata":usage,"pid":p.pid,"cli_version":version,"started_at_local":start["started_at_local"],"finished_at_local":now(),"duration_seconds":elapsed,"timed_out":timed,"exit_code":code,"stdout_path":str(stdout),"stdout_bytes":len(raw),"stdout_sha256":sha(raw),"stderr_path":str(stderr),"stderr_bytes":len(err),"stderr_sha256":sha(err),"response_path":str(work/"REVIEW_RESPONSE.md") if response else None,"response_sha256":sha(response.encode("utf-8")) if response else None,"response_classification":"TEXT_RESPONSE" if response and not timed and code==0 else ("TIMEOUT" if timed else ("EMPTY_RESPONSE" if not response else "CLI_ERROR")),"candidate_bytes_unchanged":expected==after}
termpath.write_text(json.dumps(term,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(term,ensure_ascii=False))