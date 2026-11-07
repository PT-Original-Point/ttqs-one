from docx import Document
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
from collections import Counter
from zipfile import ZipFile
import hashlib,json,re,sys,datetime
sys.stdout.reconfigure(encoding='utf-8')
base=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0122_I19-E10_SOURCE_PREP_R01_20261024\candidate_R01')
docx=base/'0122_課後追蹤與證照通過分析表_R01.docx'
receipt=base/'independent_technical_qa_R01.json'
raw=docx.read_bytes(); sha=hashlib.sha256(raw).hexdigest()
with ZipFile(docx) as z: bad_member=z.testzip()
d=Document(docx)
text='\n'.join(p.text for p in d.paragraphs)+'\n'+'\n'.join(c.text for t in d.tables for row in t.rows for c in row.cells)
checks={}; details={}; errors=[]
def check(name,ok,detail=None):
 checks[name]=bool(ok)
 if detail is not None: details[name]=detail
 if not ok: errors.append(name)
def dec(v):
 m=re.search(r'-?\d+(?:\.\d+)?',str(v).replace(',',''))
 return Decimal(m.group()) if m else None
def rounded(x,places): return x.quantize(Decimal('1').scaleb(-places),rounding=ROUND_HALF_UP)
# Artifact integrity and document identity
check('zip_integrity',bad_member is None,{'bad_member':bad_member})
check('requirement_identity',all(x in text for x in ['0122','I19-E10','課後追蹤調查與分析結果','證照通過情形']))
check('sample_boundary',all(x in text for x in ['SAMPLE','SYNTHETIC','NOT_PROVIDED','REAL 外部來源']))
check('no_local_uri_leak','file:///' not in text.lower())
check('no_unrendered_latex_markup', not any(mark in text for mark in (r'\text{', r'\frac{', '$$')))
check('survey_items_complete',set(f'Q{i:02}' for i in range(1,13)).issubset({row.cells[0].text.strip().split('.')[0] for row in d.tables[1].rows[1:]}))
check('hold_reopen_controls',all(x in text for x in ['HOLD','重啟','未核定']))
check('no_claimed_real_approval',not any(x in text for x in ['本協會已核准','協會正式核准本案','已取得外部檢定證書原件','已完成協會正式追蹤']))
# Recompute ordinal items from the embedded row-level matrices and compare item summaries.
item_results={}
for raw_idx,summary_idx,label in [(7,11,'30_day'),(9,12,'90_day')]:
 t=d.tables[raw_idx]; headers=[c.text.strip() for c in t.rows[0].cells]; rows=[[c.text.strip() for c in r.cells] for r in t.rows[1:]]
 got={}
 for j,h in enumerate(headers[1:],1):
  vals=[dec(row[j]) for row in rows if dec(row[j]) is not None]
  miss=sum(1 for row in rows if dec(row[j]) is None)
  n=len(vals); total=sum(vals,Decimal(0)); favorable=sum(v>=4 for v in vals)
  got[h]={'n':n,'missing':miss,'sum':int(total),'mean':str(rounded(total/Decimal(n),2)) if n else None,'favorable_n':favorable,'favorable_percent':str(rounded(Decimal(favorable)*100/Decimal(n),1)) if n else None}
 summary=d.tables[summary_idx]
 expected={r.cells[0].text.strip():[r.cells[2].text.strip(),r.cells[3].text.strip(),r.cells[4].text.strip(),r.cells[5].text.strip(),r.cells[6].text.strip(),r.cells[7].text.strip()] for r in summary.rows[1:]}
 mismatches=[]
 for q,v in got.items():
  e=expected.get(q)
  if not e: mismatches.append({'item':q,'error':'missing summary'}); continue
  n=int(dec(e[0])); miss=int(dec(e[1])); total=int(dec(e[2])); mean=dec(e[3].split('=')[-1]); m=re.search(r'(\d+)\s*/\s*(\d+)',e[4]); fav=int(m.group(1)) if m else -1; den=int(m.group(2)) if m else -1; pct=dec(e[5].replace('%',''))
  if (n,miss,total,mean,fav,den,pct)!=(v['n'],v['missing'],v['sum'],Decimal(v['mean']),v['favorable_n'],v['n'],Decimal(v['favorable_percent'])):
   mismatches.append({'item':q,'computed':v,'summary':e})
 item_results[label]=got
 check(label+'_ordinal_summary_match',not mismatches,{'computed_from_rows':got,'mismatches':mismatches})
# Recompute category distributions (Q08/Q09/Q12) against cross-wave summaries.
cat_results={}
for raw30,raw90,summary_idx,col,label in [(8,10,13,1,'Q08'),(8,10,14,2,'Q09'),(8,10,15,4,'Q12')]:
 r30=Counter(row.cells[col].text.strip() for row in d.tables[raw30].rows[1:]); r90=Counter(row.cells[col].text.strip() for row in d.tables[raw90].rows[1:]); t=d.tables[summary_idx]; mism=[]
 for row in t.rows[1:]:
  code=row.cells[0].text.strip(); c30=int(dec(row.cells[2].text)); den30=int(re.search(r'/\s*(\d+)',row.cells[2].text).group(1)); p30=dec(row.cells[3].text.replace('%','')); c90=int(dec(row.cells[4].text)); den90=int(re.search(r'/\s*(\d+)',row.cells[4].text).group(1)); p90=dec(row.cells[5].text.replace('%',''))
  actual30=r30.get(code,0); actual90=r90.get(code,0); ap30=rounded(Decimal(actual30)*100/Decimal(len(d.tables[raw30].rows)-1),1); ap90=rounded(Decimal(actual90)*100/Decimal(len(d.tables[raw90].rows)-1),1)
  if (c30,den30,p30,c90,den90,p90)!=(actual30,len(d.tables[raw30].rows)-1,ap30,actual90,len(d.tables[raw90].rows)-1,ap90): mism.append({'code':code,'computed':[actual30,len(d.tables[raw30].rows)-1,str(ap30),actual90,len(d.tables[raw90].rows)-1,str(ap90)],'summary':[c30,den30,str(p30),c90,den90,str(p90)]})
 cat_results[label]={'30_day_counts':dict(r30),'90_day_counts':dict(r90)}
 check(label+'_category_summary_match',not mism,{'computed':cat_results[label],'mismatches':mism})
# Validate split wave rosters and independently recalculate all cohort counts.
expected_ids=[f"P{i:02d}" for i in range(1,11)]
expected={
 "30_day":{
  "P01":("成功接觸","完成回卷","有效回卷"),"P02":("成功接觸","完成回卷","有效回卷"),
  "P03":("成功接觸","完成回卷","有效回卷"),"P04":("成功接觸","完成回卷","有效回卷"),
  "P05":("成功接觸","完成回卷","有效回卷"),"P06":("成功接觸","完成回卷","有效回卷"),
  "P07":("成功接觸","完成回卷","有效回卷"),"P08":("成功接觸","完成回卷","有效回卷"),
  "P09":("成功接觸","接觸後未回","無效（未回）"),"P10":("無法接觸","無法回卷","無效（失聯）")},
 "90_day":{
  "P01":("成功接觸","完成回卷","有效回卷"),"P02":("成功接觸","完成回卷","有效回卷"),
  "P03":("成功接觸","完成回卷","有效回卷"),"P04":("成功接觸","完成回卷","有效回卷"),
  "P05":("成功接觸","完成回卷","有效回卷"),"P06":("成功接觸","完成回卷","有效回卷"),
  "P07":("成功接觸","接觸後未回","無效（未回）"),"P08":("無法接觸","無法回卷","無效（失聯）"),
  "P09":("成功接觸","完成回卷","有效回卷"),"P10":("無法接觸","無法回卷","無效（失聯）")}}
rosters={}
for idx,label in [(4,"30_day"),(5,"90_day")]:
 t=d.tables[idx]; rows=[[c.text.strip() for c in r.cells] for r in t.rows[1:]]
 check(label+"_roster_identity",len(t.columns)==5 and [r[0] for r in rows]==expected_ids)
 actual={r[0]:(r[1],r[2],r[3]) for r in rows}
 check(label+"_roster_dispositions",actual==expected[label],{"actual":actual,"expected":expected[label]})
 rosters[label]=rows
flows={}
for label,rows in rosters.items():
 due=len(rows)
 attempted=sum(bool(r[1]) for r in rows)
 reached=sum(r[1]=="成功接觸" for r in rows)
 unreachable=sum(r[1]=="無法接觸" for r in rows)
 returned=sum(r[2]=="完成回卷" for r in rows)
 nonrespondent=sum(r[2]=="接觸後未回" for r in rows)
 valid=sum(r[3]=="有效回卷" for r in rows)
 flows[label]={"due":due,"attempted":attempted,"reached":reached,"unreachable":unreachable,"returned":returned,"reached_nonrespondent":nonrespondent,"valid_forms":valid,"valid_rate_percent":str(rounded(Decimal(valid)*100/Decimal(due),1))}
summary=d.tables[3]; summary_rows={r.cells[0].text.strip():[c.text.strip() for c in r.cells] for r in summary.rows[1:]}
summary_errors=[]
for label,row_name in [("30_day","第30天"),("90_day","第90天")]:
 r=summary_rows.get(row_name)
 f=flows[label]
 if not r or len(r)!=8:
  summary_errors.append({"wave":label,"error":"missing or malformed flow row"}); continue
 rate_match=re.search(r"(\d+)\s*[／/]\s*(\d+).*?(\d+(?:\.\d+)?)\s*%",r[7])
 vals=[int(dec(x)) for x in r[1:7]]
 expected_vals=[f["due"],f["attempted"],f["reached"],f["unreachable"],f["returned"],f["reached_nonrespondent"]]
 if vals!=expected_vals or not rate_match or (int(rate_match.group(1)),int(rate_match.group(2)),Decimal(rate_match.group(3)))!=(f["valid_forms"],f["due"],Decimal(f["valid_rate_percent"])):
  summary_errors.append({"wave":label,"actual":r,"recomputed":f})
check("cohort_status_accounting",not summary_errors,{"from_person_rows":flows,"summary_errors":summary_errors})
# Sample test rows, with no real credential evidence claim.
t=d.tables[6]; rr=[[c.text.strip() for c in r.cells] for r in t.rows[1:]]
completed=sum('已完成合成測驗' in r[2] for r in rr); met=sum('達示範門檻' in r[5] and '未達' not in r[5] for r in rr); below=sum('未達示範門檻' in r[5] for r in rr); not_attempted=len(rr)-completed
sample={'eligible':len(rr),'completed':completed,'met':met,'below':below,'not_attempted':not_attempted,'coverage':str(rounded(Decimal(completed)*100/Decimal(len(rr)),1)),'met_among_completed':str(rounded(Decimal(met)*100/Decimal(completed),1)),'met_among_eligible':str(rounded(Decimal(met)*100/Decimal(len(rr)),1))}
check('sample_assessment_math',sample=={'eligible':10,'completed':8,'met':6,'below':2,'not_attempted':2,'coverage':'80.0','met_among_completed':'75.0','met_among_eligible':'60.0'},sample)
# Font sizes from direct runs and style inheritance for readable body/table text.
font_sizes=[]
for p in d.paragraphs:
 for run in p.runs:
  if run.text.strip() and run.font.size: font_sizes.append(run.font.size.pt)
for t in d.tables:
 for row in t.rows:
  for cell in row.cells:
   for p in cell.paragraphs:
    for run in p.runs:
     if run.text.strip() and run.font.size: font_sizes.append(run.font.size.pt)
min_explicit=min(font_sizes) if font_sizes else None
check('explicit_font_floor_at_least_9pt',min_explicit is not None and min_explicit>=9,{'min_explicit_pt':min_explicit,'samples':len(font_sizes)})
result={'project_id':'TTQS_ONE','doc_id':'0122','requirement_id':'I19-E10','candidate_docx_path':str(docx),'candidate_docx_sha256':sha,'docx_bytes':len(raw),'paragraphs':len(d.paragraphs),'tables':len(d.tables),'zip_bad_member':bad_member,'checks':checks,'details':details,'item_results':item_results,'category_results':cat_results,'cohort_flows':flows,'sample_assessment':sample,'min_explicit_font_pt':min_explicit,'errors':errors,'verdict':'TECHNICAL_PASS' if all(checks.values()) else 'TECHNICAL_FAIL','review_scope':'DOCX internal structure, embedded row-level math, categorical summaries, cohort flow, synthetic test distributions, URI/claim markers and explicit font size; excludes independent semantic and visual review','reviewed_at_local':datetime.datetime.now().astimezone().isoformat()}
receipt.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'verdict':result['verdict'],'sha':sha,'errors':errors,'checks':checks,'cohort_flows':flows,'sample_assessment':sample,'min_explicit_font_pt':min_explicit,'receipt':str(receipt)},ensure_ascii=False))
