from pathlib import Path
from fractions import Fraction
import csv, hashlib, json, re
root=Path(__file__).resolve().parents[1]
body_path=root/'candidate'/'0132_I19-E21_BODY_R01.md'
body=body_path.read_text(encoding='utf-8')
source=(root/'source'/'SOURCE_PACKET_0132_I19-E21_R01.md').read_text(encoding='utf-8')
blueprint=(root/'source'/'UNIQUE_BLUEPRINT_0132_I19-E21_R01.md').read_text(encoding='utf-8')
batches=[('B1',20,4,(2,1,1)),('B2',24,5,(2,2,1)),('B3',22,4,(2,1,1)),('A1',21,3,(1,1,1)),('A2',25,3,(1,1,1)),('A3',24,2,(1,1,0))]
pre_n=sum(x[1] for x in batches[:3]); pre_d=sum(x[2] for x in batches[:3])
post_n=sum(x[1] for x in batches[3:]); post_d=sum(x[2] for x in batches[3:])
pre=Fraction(pre_d,pre_n); post=Fraction(post_d,post_n)
delta=(post-pre)*100
rel=(pre-post)/pre*100
checks={
 'mapping_docid_requirement_index': all(x in source and x in blueprint for x in ['0132','I19-E21']),
 'official_exact_text': '個人產品不良件數有下降趨勢。' in source and '個人產品不良件數有下降趨勢。' in blueprint,
 'official_page8_index145': 'index 145' in source and '第 8 頁' in source,
 'printed_checkbox_unknown': 'UNKNOWN' in source and 'printed_official_checkbox_serial' in blueprint,
 'negative_neighbors': all(x in body for x in ['0131／I19-E20','0133／I19-E22']),
 'synthetic_real_boundary': all(x in body for x in ['SAMPLE／SYNTHETIC','REAL 證據目前 UNKNOWN','REAL 原件替換區']),
 'defect_rate_and_point_formulas': all(x in body for x in ['不良率(%) =','前後差（百分點）=','相對下降率(%) =']),
 'data_scope_and_confounds': all(x in body for x in ['紙型裁切導板','材料批號改變','不能歸因於訓練']),
 'writer_receipt_not_accepted': 'CANDIDATE' in body and '未經獨立語意審查' in body,
 'expected_period_totals': (pre_n,pre_d,post_n,post_d)==(66,13,70,8),
 'all_batch_primary_cause_sums': all(sum(x[3])==x[2] for x in batches),
 'all_batch_numerators_le_denominator': all(x[2]<=x[1] for x in batches),
 'pooled_rates': round(float(pre)*100,1)==19.7 and round(float(post)*100,1)==11.4,
 'percentage_point_difference': round(float(delta),2)==-8.27,
 'relative_decline': round(float(rel),1)==42.0,
 'count_and_volume_change': round((post_d-pre_d)/pre_d*100,1)==-38.5 and round((post_n-pre_n)/pre_n*100,1)==6.1,
 'synthetic_batch_facts_registered': all(re.search(r'\| SYN-'+name+r' \|[^\n]*SYN-LOG-'+name+r'[^\n]*\|',body) for name in ['B1','B2','B3','A1','A2','A3']),
 'synthetic_totals_registered': all(x in body for x in ['SYN-TOTAL-VOLUME','SYN-EXCLUDED-01','SYN-PRE-TOTAL','SYN-POST-TOTAL','SYN-DELTA-PP','SYN-REL-DECLINE','SYN-COUNT-CHANGE','SYN-VOLUME-CHANGE']),
 'no_nonreal_acceptance_claim': all(x in body for x in ['未正式接受','REAL 證據目前 UNKNOWN','不能稱統計顯著']),
 'chart_markers': body.count('[[CHART:')==2,
 'complete_usable_sections': all(x in body for x in ['操作流程與控制點','逐批記錄表','HOLD','REJECT','使用前複核清單']),
}
# Extract the 4-column replacement register from §10 to a standalone CSV.
section=body.split('## 10. SAMPLE／SYNTHETIC 逐事實替換簿',1)[1].split('## 11.',1)[0]
rows=[]
for line in section.splitlines():
    if not line.startswith('| SYN-'): continue
    cols=[c.strip() for c in line.strip().strip('|').split('|')]
    if len(cols)==4: rows.append(cols)
reg=root/'evidence'/'SYNTHETIC_REPLACEMENT_REGISTER_0132_R01.csv'
with reg.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f); w.writerow(['synthetic_id','synthetic_fact_or_value','document_locator','required_real_source']); w.writerows(rows)
receipt={'doc_id':'0132','requirement_id':'I19-E21','body_sha256':hashlib.sha256(body_path.read_bytes()).hexdigest(),'body_characters':len(body),'replacement_register_rows':len(rows),'math':{'pre_n':pre_n,'pre_d':pre_d,'pre_rate_exact':str(pre),'pre_rate_percent':float(pre*100),'post_n':post_n,'post_d':post_d,'post_rate_exact':str(post),'post_rate_percent':float(post*100),'delta_pp':float(delta),'relative_decline_percent':float(rel),'raw_count_change_percent':(post_d-pre_d)/pre_d*100,'inspection_volume_change_percent':(post_n-pre_n)/pre_n*100},'checks':checks,'passed':all(checks.values()),'independent_semantic_review':'NOT_PERFORMED','formal_acceptance':'NOT_GRANTED','real_evidence':'UNKNOWN'}
out=root/'qa'/'CONTENT_QA_0132_R01.json'; out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'status':'PASS' if receipt['passed'] else 'FAIL','body_sha256':receipt['body_sha256'],'register_rows':len(rows),'failed':[k for k,v in checks.items() if not v],'math':receipt['math'],'register_sha256':hashlib.sha256(reg.read_bytes()).hexdigest()},ensure_ascii=False))
if not receipt['passed']: raise SystemExit(1)