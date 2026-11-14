#!/usr/bin/env python3
import hashlib, json, re, sys
from pathlib import Path

base=Path(__file__).resolve().parents[1]
body=Path(sys.argv[1]) if len(sys.argv)>1 else base/'candidate'/'0083_R02_body.md'
bp=base/'inputs'/'UNIQUE_BLUEPRINT_0083_R03.md'
text=body.read_text(encoding='utf-8-sig'); bpt=bp.read_text(encoding='utf-8-sig')
bl=text.splitlines(); bpl=bpt.splitlines()
def normalize(s): return s.replace('`','').replace('**','').replace('*','').replace('\\|','|').strip()
def pipe_cells(line): return [normalize(x) for x in line.strip().strip('|').split('|')]
def lines_between(lines,start,end):
 a=next((i for i,x in enumerate(lines) if start in x),-1)
 if a<0:return []
 z=next((i for i in range(a+1,len(lines)) if end in lines[i]),len(lines))
 return lines[a+1:z]
def register_groups(lines):
 groups=[]; g=[]
 for i,line in enumerate(lines+[""]):
  if re.match(r'^\|\s*R-\d{3}\s*\|',line): g.append((i+1,pipe_cells(line)))
  elif g: groups.append(g);g=[]
 return groups
def table_rows(lines,prefix):
 return [pipe_cells(x) for x in lines if re.match(r'^\|\s*'+prefix+r'-\d{2}\s*\|',x)]

bp_regs=[pipe_cells(x) for x in bpl if re.match(r'^\|\s*R-\d{3}\s*\|',x)]
body_groups=register_groups(bl)
body_regs=[g for g in body_groups if len(g)==81]
checks={}
checks['two_complete_register_tables']=len(body_regs)==2
checks['register_tables_match_blueprint']=len(bp_regs)==81 and len(body_regs)==2 and all([r[1] for r in group]==bp_regs for group in body_regs)
if len(body_regs)==2 and len(bp_regs)==81:
 checks['register_table_1_exact']= [r[1] for r in body_regs[0]]==bp_regs
 checks['register_table_2_exact']= [r[1] for r in body_regs[1]]==bp_regs
else:
 checks['register_table_1_exact']=False;checks['register_table_2_exact']=False
checks['sample_boundaries_permanent']='標籤永久保留' in text and '不得移除、覆寫、改標' in text
checks['general_applicability']='各類培訓機構' in text and '不把志工服務設為一般適用條件' in text
checks['no_real_association_claim']=not any(x in text for x in ['協會為志工基礎運作','本協會設有','協會實際設有','協會已採用','本會已核准'])
checks['cumulative_threshold_correct']='累計門檻不套用到 T1 或 T3 的本期' in text and '83.3% 通過' in text
checks['appendices_A_to_E']=all(f'Appendix {x}' in text for x in 'ABCDE')
neg_section=lines_between(bl,'### 13.2 負面測試 28 項','## 14. 隱私')
neg_rows=[pipe_cells(x) for x in neg_section if re.match(r'^\|\s*\d+\s*\|',x)]
checks['all_28_negative_tests']=[int(r[0]) for r in neg_rows]==list(range(1,29)) and all(r[2]=='FAIL' for r in neg_rows)
checks['appendix_sha_lock']=all(x in text for x in ['SRC-MIS','SRC-GEN','07c4b0beb30ebe9919818977d6eb0255e9f467955e9190e515ae3e2b963d1dd8','7fc23191efdb60ca4a9b48bc306799a9f15916b1160b63292d164bd4f4cf49aa'])
checks['no_remove_sample_instruction']=not re.search(r'(?:移除|刪除|去除).{0,12}SAMPLE.{0,12}(?:標籤|浮水印)',text)
checks['core_identity']=all(x in text for x in ['DOCX 0083','I17C-E02','checkbox 089','REAL=UNKNOWN/HOLD','FORMAL_ACCEPTANCE=NOT_GRANTED','NOT EXECUTED'])
checks['aid02_status_and_dates']=all(x in text for x in ['AID-02','REQUESTED','2026-05-29','2026-06-26','A1-04','A1-05'])
checks['required_calcs']=all(re.search(pat,text) for pat in [r'3\s*÷\s*4\s*=\s*75\.0%',r'3\s*÷\s*12\s*=\s*25\.0%',r'4\s*÷\s*4\s*=\s*100\.0%',r'7\s*÷\s*12\s*=\s*58\.3%',r'10\s*÷\s*12\s*=\s*83\.3%'])
# Exact field IDs in the Blueprint definition tables.
for key,start,end,lo,hi in [('G1','### 4.2 欄位定義','### 4.3 空白表單',1,14),('T1','### 5.2 欄位定義','### 5.3 空白表單',1,17),('A1','### 6.2 欄位定義','### 6.3 空白表單',0,7),('E1','### 7.2 欄位定義','### 7.3 空白表單',1,7)]:
 section=lines_between(bl,start,end)
 found=[int(m.group(1)) for line in section if (m:=re.match(r'^\|\s*'+key+r'-(\d{2})\s*\|',line))]
 checks[f'{key}_field_definition_ids_exact']=found==list(range(lo,hi+1))
checks['all_tables_same_columns']=True
table_findings=[]; group=[]
for i,line in enumerate(bl+[""]):
 if line.strip().startswith('|') and line.strip().endswith('|'):
  c=pipe_cells(line)
  if not all(re.fullmatch(r':?-{3,}:?',z.replace(' ','')) for z in c): group.append((i+1,len(c)))
 elif group:
  widths={w for _,w in group}
  if len(widths)>1: table_findings.append({'start':group[0][0],'end':group[-1][0],'widths':sorted(widths)})
  group=[]
checks['all_tables_same_columns']=not table_findings
report={'schema':'ttqs-0083-body-blueprint-qa-v1','document_id':'0083','requirement_id':'I17C-E02','checkbox':'089','body_sha256':hashlib.sha256(body.read_bytes()).hexdigest(),'blueprint_sha256':hashlib.sha256(bp.read_bytes()).hexdigest(),'body_bytes':body.stat().st_size,'register_groups':[(len(g),g[0][0],g[-1][0]) for g in body_groups],'blueprint_register_rows':len(bp_regs),'checks':checks,'failed_checks':[k for k,v in checks.items() if not v],'table_width_findings':table_findings,'scope':'Deterministic crosswalk/source text checks only; not semantic or visual acceptance.','result':'PASS_STRUCTURAL' if all(checks.values()) else 'FAIL'}
out=base/'evidence'/'body_blueprint_qa_R02.json';out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(report,ensure_ascii=True));sys.exit(0 if all(checks.values()) else 1)
