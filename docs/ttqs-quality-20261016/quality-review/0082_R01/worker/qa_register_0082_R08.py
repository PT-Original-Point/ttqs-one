from pathlib import Path
import csv,json,hashlib,re,sys,datetime
sys.stdout.reconfigure(encoding='utf-8')
bodyp=Path(sys.argv[1]); csvp=Path(sys.argv[2]); regp=Path(sys.argv[3]); receiptp=Path(sys.argv[4])
body=bodyp.read_text(encoding='utf-8')
raw=csvp.read_text(encoding='utf-8-sig')
rows=list(csv.DictReader(raw.splitlines()))
issues=[]
def need(cond,msg):
 if not cond: issues.append(msg)
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
items=['B1','B2','B3','B4','B5','B6']
by={}
for r in rows: by.setdefault(r['respondent_id'],{})[r['item_id']]=r
need(len(rows)==72,'CSV must contain 72 item rows')
need(len(by)==12,'CSV must contain 12 respondents')
# Compare matrix against the locked source. N/O is the defined shorthand for NO opportunity; em dash means missing, incomplete, or not returned.
start=body.find('## 8. 合成群體回收矩陣'); end=body.find('## 9.',start)
need(start>=0 and end>start,'matrix section not found')
mat={}
for line in body[start:end].splitlines():
 if not line.startswith('| BTR-'): continue
 c=[x.strip() for x in line.strip('|').split('|')]
 mat[c[0]]={'status':c[1],'cells':dict(zip(items,c[2:8]))}
need(set(mat)==set(by),'matrix respondent IDs differ from CSV')
for rid,rec in mat.items():
 for item,val in rec['cells'].items():
  src=by[rid][item]
  need(rec['status']==src['return_status'],f'{rid} status mismatch')
  pre=src['pre_recall_score']; cur=src['current_period_score']; opp=src['opportunity_status']
  if opp=='NO' and pre=='' and cur=='': expected='N/O'
  elif opp=='MISSING' and pre=='' and cur=='': expected='—'
  elif pre=='' and cur=='': expected='—'
  elif pre!='' and cur!='': expected=f'{pre}→{cur}'
  else: expected='—'
  need(val==expected,f'{rid}/{item}: matrix {val!r} != CSV representation {expected!r}')
# Independently recompute item statistics from VALID records.
expected_stats={
'B1':(9,0,0,13,26),'B2':(8,1,0,13,23),'B3':(7,2,0,12,24),
'B4':(9,0,0,13,25),'B5':(8,1,0,11,21),'B6':(5,3,1,7,14)}
stats={}
valid_ids=[rid for rid,ir in by.items() if next(iter(ir.values()))['return_status']=='VALID']
for item in items:
 valid=[by[rid][item] for rid in valid_ids]
 scored=[r for r in valid if r['pre_recall_score'].isdigit() and r['current_period_score'].isdigit()]
 no=sum(r['opportunity_status']=='NO' for r in valid)
 missing=sum(r['opportunity_status']=='MISSING' for r in valid)
 ps=sum(int(r['pre_recall_score']) for r in scored); cs=sum(int(r['current_period_score']) for r in scored)
 stats[item]=(len(scored),no,missing,ps,cs)
 need(stats[item]==expected_stats[item],f'{item} stats {stats[item]} != locked tuple {expected_stats[item]}')
need(len(valid_ids)==9,'valid respondent count mismatch')
need(sum(r['return_status']!='NOT_RETURNED' for r in rows[::6])==10,'returned count mismatch')
need(sum(r['return_status']=='INVALID' for r in rows[::6])==1,'invalid count mismatch')
need(sum(r['return_status']=='NOT_RETURNED' for r in rows[::6])==2,'not-returned count mismatch')
need('目前期間：☐0 ☐1 ☐2 ☐3 ☐4 ☐N/O' in body and body.count('目前期間：☐0 ☐1 ☐2 ☐3 ☐4 ☐N/O')==6,'current-period N/O choice must appear in all six questions')
need('SAMPLE/SYNTHETIC' in body and 'PROPOSED' in body and 'NOT_EXECUTED' in body and 'REAL=UNKNOWN/HOLD' in body and 'NOT_GRANTED' in body,'candidate truth-state markers incomplete')
need('DOCX 0082' in body and 'I17C-E01' in body and '088' in body and '0083' in body and '089' in body,'document/requirement/checkbox separation missing')
need('SYN-0073-2026-A01' in body and 'BTR-01' in body and 'S01–S16' in body and 'P01–P16' in body,'synthetic case boundary missing')
need('R08' in body and '僅反應回饋' in body and 'PROPOSED／PENDING APPROVAL' in body,'cross-document boundary missing')
need('2026-08-15' in body and '2026-09-14' in body and '2026-09-15' in body and '2026-09-21' in body,'sample dates incomplete')
need('寄送後 +7 日' in body and '寄送後 +14 日' in body and '2026-09-21' in body and '2026-09-28' in body,'reminder dates do not match Blueprint R02 §5.3')
# Ensure sample date arithmetic is coherent.
need((datetime.date(2026,9,14)-datetime.date(2026,8,15)).days==30,'30-day send date arithmetic')
need((datetime.date(2026,9,21)-datetime.date(2026,9,14)).days==7,'due-date arithmetic')
# Replacement register, with row-level references for every locked respondent/item record plus synthetic facts cited in the body.
fields=['fact_id','group_id','doc_id','requirement_id','official_checkbox_serial','case_id','source_locator','data_type','synthetic_value','required_real_replacement','verification_role','hold_rule','status']
register=[]
seq=1
STATE='SAMPLE/SYNTHETIC; REAL=UNKNOWN/HOLD'
def add(group,loc,typ,value,required,role='訓練行政＋第二位覆核者',rule='缺少授權真實原件或核對時維持 HOLD'):
 global seq
 register.append({'fact_id':f'SYN-0082-FACT-{seq:04d}','group_id':f'{group:04d}','doc_id':'0082','requirement_id':'I17C-E01','official_checkbox_serial':'088','case_id':'SYN-0073-2026-A01','source_locator':loc,'data_type':typ,'synthetic_value':str(value),'required_real_replacement':required,'verification_role':role,'hold_rule':rule,'status':STATE}); seq+=1
# Identity and cross-document facts
add(1,'§1','文件識別','DOCX 0082 = I17C-E01 = checkbox 088','正式來源核對及文件編號登錄')
add(2,'§合成聲明','文件狀態','PROPOSED; NOT_EXECUTED; CANDIDATE_ONLY; formal acceptance NOT_GRANTED','合法正式接受及實際執行證據')
add(3,'§14','跨文件參照','0073 R08 is reaction feedback only; not behavior-transfer evidence','0073 已授權之正式原件與獨立驗證')
add(4,'§14','跨文件參照','0074 R01 recommendation is PROPOSED/PENDING APPROVAL','正式核准及實際執行資料')
add(5,'§14','跨文件參照','0083 = I17C-E02 = checkbox 089; separate follow-up record; existence/completion unclaimed','0083 真實候選、核准及追蹤原件')
add(6,'§7.1 A2','課程名稱','志工服務溝通與紀錄交接實務（synthetic label）','真實課程計畫與班級紀錄')
add(7,'§7.1 A3','課程日期','2026-08-15','真實簽到/課程紀錄與授權版本')
add(8,'§7.1 A4-A6','追蹤時程','INT-30; send 2026-09-14; response 2026-09-15; due 2026-09-21','真實寄送/回收時間戳與間隔核定紀錄')
add(9,'§9.1','發放回收狀態','12 issued; 10 returned; 9 valid; 1 invalid; 2 not returned','真實發放名單、回收原件、排除理由')
add(10,'§7.1 A7','匿名代碼','BTR-01; distinct from 0073 S01-S16 and 0074 P01-P16','授權去識別對照資料；不得以合成代碼冒充')
add(25,'§7.1 A10-A11','同意及隱私','Synthetic consent=yes; stats and anonymous quote; not a real consent record','真實同意原件、使用範圍及撤回依據')
add(26,'§12','保存規定','current retention rule UNKNOWN/HOLD','現行經核准保存及撤回規定')
# One row for every locked data record; covers all respondent answers and evidence types.
for rid in sorted(by):
 for item in items:
  r=by[rid][item]
  group=10+items.index(item)+1
  value={'status':r['return_status'],'opportunity':r['opportunity_status'],'pre_recall_score':r['pre_recall_score'] or None,'current_period_score':r['current_period_score'] or None,'reported_evidence_type':r['respondent_reported_evidence_type'] or 'NONE_RECORDED','evidence_original_attached':r['evidence_original_attached']}
  add(group,f'§8 row {rid} / {item}','合成逐題回覆',json.dumps(value,ensure_ascii=False,separators=(',',':')),'真實原始問卷、回覆時間與分類理由；無機會/缺答須有來源紀錄')
# BTR-01 additional form fields not represented by the per-item CSV.
for loc,typ,val,real in [
 ('§7.1 A8','服務角色','交接','真實角色資料及最小化依據'),('§7.1 A9','案件連結','SYN-0073-2026-A01','真實班別連結與課程紀錄'),('§7.1 A12-A13','回覆方式','online; learner self-completed','真實回收方式與本人核對紀錄'),
 ('§7.3 C1-C2','情境','6 handoffs in 30 days; service handoff and telephone referral','真實受測者自陳及必要情境紀錄'),('§7.3 C3','行為實例','de-identified synthetic example of handoff confirmation','真實、去識別且授權的回覆'),('§7.3 C4','證據可調閱','yes, respondent-reported only','授權可調閱的原始來源'),('§7.3 D1','障礙','time shortage; limited feedback','真實問卷回覆'),('§7.3 D2','協助需求','quick reference card; supervisor feedback','真實問卷回覆及核准行動'),('§7.3 D3','自陳移轉程度','4/5 synthetic','真實問卷回覆；不得作客觀成效'),('§7.3 E1-E4','後續意見','INT-30; refer to 0083/089; no completion claimed','真實回覆及已授權後續文件')]:
 add(22 if typ in ('障礙','協助需求') else (21 if typ=='自陳移轉程度' else (20 if typ=='證據可調閱' else (23 if typ=='後續意見' else 10))),loc,typ,val,real)
# Computed summary facts, independently derived from CSV.
valid=[by[rid][item] for rid in valid_ids for item in items]
no_total=sum(r['opportunity_status']=='NO' for r in valid)
missing_total=sum(r['opportunity_status']=='MISSING' for r in valid)
for item in items:
 n,no,missing,ps,cs=stats[item]
 opp=(n/(n+no+missing))*100
 add(19,f'§9.2 {item}','彙總統計',json.dumps({'n':n,'N/O':no,'missing':missing,'pre_sum':ps,'current_sum':cs,'pre_mean':round(ps/n,3),'current_mean':round(cs/n,3),'change':round(cs/n-ps/n,3),'opportunity_rate_pct':round(opp,2)},ensure_ascii=False,separators=(',',':')),'真實回覆資料、清理規則及可重現計算')
 add(17,f'§9.2 {item}','N/O count',no,'真實問卷機會狀態與分母核對')
 add(18,f'§9.2 {item}','missing count',missing,'真實問卷完整性記錄')
add(19,'§9.2 total','合計統計',json.dumps({'scored':sum(x[0] for x in stats.values()),'N/O':no_total,'missing':missing_total,'pre_sum':sum(x[3] for x in stats.values()),'current_sum':sum(x[4] for x in stats.values()),'pre_mean':1.5,'current_mean':round(133/46,3),'change':round(133/46-1.5,3)},ensure_ascii=False,separators=(',',':')),'可核對之真實回覆及獨立覆算')
add(24,'§10','示範門檻','proposed only: opportunity rate >=60%, current mean >=3.0, change >=+1.0','如欲採用須有正式核准政策；否則只作示範')
add(23,'§10','示範判定','B3 conditionally meets; B6 HOLD 55.56% opportunity; 1/6 meets; overall HOLD/REVERIFY','真實分母、經核准門檻與有權決策者決議')
need(all(x in body for x in ['服務紀錄完整記錄','交接閉環','敏感資訊前明確同意','事實與推論區分','交接前必要欄位核對','錯誤更正軌跡更新']),'B1-B6 behavior labels do not align with UNIQUE_BLUEPRINT_0082_R02 section 6.1')
need(not any(x in body for x in ['服務需求釐清','紀錄完整性','安全交接','個人資料保護','需求者後續追蹤／結案','異常通報／升級']),'obsolete B1-B6 behavior label remains')
need(all(x in body for x in ['| N-10 |','| N-11 |']),'negative-test list must include N-10 and N-11')
need('PASS-SAMPLE' in body and 'DEMO_MEETS' not in body,'decision term must match Blueprint R02')
need('| A8 服務角色類別 | 交接 |' in body,'synthetic A8 must use a listed role option')
need('過去 30 天執行「交接閉環」' in body and 'C1＝**6 次交接閉環**' in body,'C1 must align with blueprint handoff-closure behavior')
need('**C1**　過去 30 天，您實際執行「交接閉環」' in body and '實際執行「敏感資訊前明確同意」約' not in body,'blank-form C1 must match Blueprint handoff-closure behavior')
need('該題標記 PASS-SAMPLE' in body and '| B3 | ✔ | ✔（3.429） | ✔ | PASS-SAMPLE |' in body and '`PASS-SAMPLE`' not in body[body.find('## 10.')-1:body.find('## 11.')],'§10 PASS-SAMPLE label must not print Markdown delimiters')
# Write CSV and receipt.
regp.parent.mkdir(parents=True,exist_ok=True)
with regp.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(register)
item_text=body[body.find('### 9.2 逐題彙總'):body.find('### 9.3')]
for item,(n,no,missing,ps,cs) in expected_stats.items():
 expected=f'{item} | {ps}／{n}'
 need(expected in item_text,f'summary table missing {expected}')
need('69 ÷ 46 = 1.500' in body and '133 ÷ 46 = 2.891' in body and '+1.391' in body,'overall math values missing')
need('N/O' in body and '不得' in body,'N/O guard missing')
need(not any(t.lower() in body.lower() for t in ['opencode','antigravity','sha-256','git commit']),'internal worker/build metadata leaked into evaluator body')
need(len(register)==115,'replacement register row count mismatch')
need({f'{i:04d}' for i in range(1,27)}.issubset({r['group_id'] for r in register}),'replacement register does not cover all 26 blueprint groups')
need(len({r['fact_id'] for r in register})==len(register),'replacement register fact IDs are not unique')
checks={'csv_72_rows_12_respondents':len(rows)==72 and len(by)==12,'matrix_exactly_matches_locked_csv':not any('matrix' in x for x in issues),'item_math_exact':all(stats[k]==expected_stats[k] for k in items),'answer_form_current_NO_option_all_6':body.count('目前期間：☐0 ☐1 ☐2 ☐3 ☐4 ☐N/O')==6,'dates_and_reminders_consistent':(datetime.date(2026,9,14)-datetime.date(2026,8,15)).days==30 and (datetime.date(2026,9,21)-datetime.date(2026,9,14)).days==7 and (datetime.date(2026,9,28)-datetime.date(2026,9,14)).days==14 and '寄送後 +7 日' in body and '寄送後 +14 日' in body,'truth_boundaries_and_identity':all(x in body for x in ['SAMPLE/SYNTHETIC','PROPOSED','NOT_EXECUTED','REAL=UNKNOWN/HOLD','NOT_GRANTED','DOCX 0082','I17C-E01','088','0083','089']),'replacement_register_complete':len(register)==115 and {f'{i:04d}' for i in range(1,27)}.issubset({r['group_id'] for r in register}) and len({r['fact_id'] for r in register})==len(register)}
result={'document_id':'0082','requirement_id':'I17C-E01','official_checkbox_serial':'088','body_sha256':digest(bodyp),'locked_csv_sha256':digest(csvp),'matrix_cell_mismatches':sum(1 for x in issues if 'matrix' in x),'register_path':str(regp),'register_rows':len(register),'register_sha256':digest(regp),'checks':checks,'status':'PASS' if not issues and all(checks.values()) else 'FAIL','issues':issues,'computed_stats':{k:{'n':v[0],'N/O':v[1],'missing':v[2],'pre_sum':v[3],'current_sum':v[4]} for k,v in stats.items()}}
receiptp.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'issues':issues,'register_rows':len(register),'register_sha256':result['register_sha256'],'checks':result['checks']},ensure_ascii=False))
if result['status']!='PASS': raise SystemExit(1)
