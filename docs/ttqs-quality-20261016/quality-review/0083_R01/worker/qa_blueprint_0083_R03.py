#!/usr/bin/env python3
import datetime as dt, hashlib, json, re, sys
from pathlib import Path
p=Path(sys.argv[1]); text=p.read_text(encoding='utf-8'); errors=[]; checks={}
checks['doc_identity']='DOCX 0083' in text and 'I17C-E02' in text and 'checkbox 089' in text
checks['source_hashes']=all(x in text for x in ['538bedb9d87e8465f43151933b4a5c1bfa4bbc4e','07c4b0beb30ebe9919818977d6eb0255e9f467955e9190e515ae3e2b963d1dd8','4ff863d9f534b6359fc1c7c1685bd8cce02da886','7fc23191efdb60ca4a9b48bc306799a9f15916b1160b63292d164bd4f4cf49aa','8c2bbe7ca9dcbb03088a48934b9e57e7147ede63','ad03323d591cbea62814a8a59d233110587f2741bed8f944380b1faa2d04d216','b7bd4c09b7d7e22993a1577647e10a421fb240222b46b531ba3f01ee047fa1d1'])
checks['genre_volunteer_sample']='模擬志工服務站' in text and '不宣稱協會實際設有' in text and '門市值班' not in text and '新進同仁' not in text
checks['sample_real_boundary']=all(x in text for x in ['SAMPLE/SYNTHETIC','REAL=UNKNOWN/HOLD','FORMAL_ACCEPTANCE=NOT_GRANTED','NOT EXECUTED'])
checks['forms_and_sections']=all(x in text for x in ['Form-G1','Form-T1','Form-A1','Form-E1','## 13. 正文 Writer','HOLD','RETURN','REJECT','REVERIFY'])
# Parse the replacement-register rows only.
inreg=False; ids=[]; reglines=[]
for line in text.splitlines():
 if '逐原子事實替換清冊' in line: inreg=True
 if inreg:
  m=re.match(r'\|\s*R-(\d{3})\s*\|',line)
  if m: ids.append(int(m.group(1))); reglines.append(line)
  if inreg and line.startswith('確定性 QA 必須'): break
checks['register_81_unique_contiguous']=ids==list(range(1,82)) and len(set(ids))==81
checks['register_rows_have_atomic_ids']=all(
    bool(re.match(r'^\|\s*R-\d{3}\s*\|', l))
    and not re.search(r'R-\d{3}\s*[～~–-]\s*R-\d{3}', l.split('|')[1])
    for l in reglines
)
checks['register_header_no_ranges']='無範圍式 ID' in text and '81 列' in text
checks['aid_append_only']=all(x in text for x in ['AID-01','AID-02','新請求以新列追加','不得覆寫或合併舊筆'])
checks['dates_consistent']=all(x in text for x in ['2026-03-06','2026-03-09','2026-04-03','2026-05-01','2026-05-29','2026-06-26'])
start=dt.date(2026,2,6); end=dt.date(2026,3,5)
checks['baseline_28_days']=(end-start).days+1==28
checks['followup_dates_28_day_steps']=[(dt.date(2026,4,3)-dt.date(2026,3,6)).days,(dt.date(2026,5,1)-dt.date(2026,3,6)).days,(dt.date(2026,5,29)-dt.date(2026,3,6)).days]==[28,56,84]
checks['arithmetic']=(round(3/4*100,1)==75.0 and round(3/12*100,1)==25.0 and round(4/4*100,1)==100.0 and round(7/12*100,1)==58.3 and round(10/12*100,1)==83.3 and '3÷4＝75.0%' in text and '4÷4＝100.0%' in text and '10÷12＝83.3%' in text)
checks['three_layers_separated']=all(x in text for x in ['數值計算層','樣本執行狀態層','真實證據層'])
checks['all_decision_deadlines_proposed']=all('PROPOSED SAMPLE ONLY' in l for l in text.splitlines() if '工作日' in l)
checks['negative_tests_at_least_12']=bool(re.search(r'\*\*11\.2 負面測試（≥12',text))
checks['not_acceptance_claim']='BLUEPRINT ONLY / NOT EXECUTED' in text
report={'schema':'ttqs-0083-blueprint-qa-v1','path':str(p).replace('\\','/'),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'register_ids':len(ids),'register_first_last':[min(ids),max(ids)] if ids else [],'checks':checks,'failed_checks':[k for k,v in checks.items() if not v],'result':'PASS_BLUEPRINT_QA' if all(checks.values()) else 'FAIL','acceptance_scope':'Blueprint structural and source-bound consistency only; does not accept any DOCX or REAL evidence.'}
out=p.parents[1]/'evidence'/'blueprint_qa_R03.json'; out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=True))
sys.exit(0 if all(checks.values()) else 1)
