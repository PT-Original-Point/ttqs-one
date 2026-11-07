import csv, hashlib, json, pathlib, datetime
from decimal import Decimal, ROUND_HALF_UP
ROOT=pathlib.Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0141_I19-E31_SOURCE_PREP_R01_20261025')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def fmt(x,n): return str(Decimal(str(x)).quantize(Decimal('1.'+'0'*n),rounding=ROUND_HALF_UP))
field={f'Q{i}':f'Q{i}_{name}' for i,name in enumerate(['need_fit','content_applicability','instructor_support','materials_resources','admin_communication','learning_environment','overall_satisfaction'],1)}
summary_keys={'Q1_need_fit':'Q1','Q2_content_applicability':'Q2','Q3_instructor_support':'Q3','Q4_materials_resources':'Q4','Q5_admin_communication':'Q5','Q6_learning_environment':'Q6','Q7_overall_satisfaction':'Q7'}
with (ROOT/'SAMPLE_SURVEY_RESPONSES_0141_R01.csv').open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
with (ROOT/'SAMPLE_PERIOD_SUMMARY_0141_R01.csv').open(encoding='utf-8-sig',newline='') as f: sums=list(csv.DictReader(f))
checks=[]; periods=[]
for s in sums:
    year=s['period_year']; rr=[r for r in rows if r['period_year']==year]
    values={q:[int(r[field[q]]) for r in rr] for q in field}
    pooled=sum(sum(values[q]) for q in ['Q1','Q2','Q3','Q4','Q5','Q6'])/(len(rr)*6)
    top=sum(v>=4 for v in values['Q7'])
    calc={'valid_n':len(rr),'return_pct':fmt(100*len(rr)/int(s['SAMPLE_invited_n']),2),'core_answers':len(rr)*6,'pooled_q1_q6':fmt(pooled,4),'q7_mean':fmt(sum(values['Q7'])/len(rr),4),'q7_top2_n':top,'q7_top2_pct':fmt(100*top/len(rr),2),'item_means':{q:fmt(sum(values[q])/len(rr),4) for q in field}}
    source_items=json.loads(s['item_means'])
    expected={'valid_n':int(s['SAMPLE_valid_n']),'return_pct':fmt(s['SAMPLE_return_rate_pct'],2),'core_answers':int(s['core_item_valid_n']),'pooled_q1_q6':fmt(s['six_item_mean_1_to_5'],4),'q7_mean':fmt(s['overall_Q7_mean_1_to_5'],4),'q7_top2_n':int(s['overall_Q7_top2_n']),'q7_top2_pct':fmt(s['overall_Q7_top2_pct'],2),'item_means':{summary_keys[k]:fmt(v,4) for k,v in source_items.items()}}
    for k,v in expected.items(): checks.append({'year':year,'metric':k,'match':calc[k]==v,'calculated':calc[k],'source':v})
    periods.append({'year':year,**calc})
r5=(ROOT/'MANUSCRIPT_0141_R05_CANDIDATE.md').read_text(encoding='utf-8'); r6p=ROOT/'MANUSCRIPT_0141_R06_CANDIDATE.md'; r6=r6p.read_text(encoding='utf-8')
def between(text,start,end):
    i=text.find(start); j=text.find(end,i+1)
    if i<0 or j<0: raise ValueError('section boundary not found')
    return text[i:j]
start='### \u9644\u9304\u4e09\uff1a\u4e09\u671f\u5b8c\u6574 36 \u7b46\u5408\u6210\u539f\u59cb\u56de\u8986\u8cc7\u6599\u96c6'
end='### \u9644\u9304\u56db\uff1a\u8cc7\u6599\u5b57\u5178\u8207\u8a08\u7b97\u516c\u5f0f\u624b\u518a'
a5=between(r5,start,end); a6=between(r6,start,end)
checks.append({'metric':'appendix_iii_text_equals_r05','match':a5==a6,'r05_section_sha256':hashlib.sha256(a5.encode()).hexdigest(),'r06_section_sha256':hashlib.sha256(a6.encode()).hexdigest()})
checks.append({'metric':'all_36_rows_synthetic_and_scores_1_to_5','match':len(rows)==36 and all(r['record_state']=='SAMPLE_SYNTHETIC' and r['customer_segment']=='TRAINING_PARTICIPANT_SYNTHETIC' and all(1<=int(r[field[q]])<=5 for q in field) for r in rows),'rows':len(rows)})
checks.append({'metric':'questionnaire_and_response_source_hashes_unchanged','match':sha(ROOT/'QUESTIONNAIRE_ITEMS_0141_R01.csv')=='310745e5be17980ca9c623b23e15605cb221c9cbbdf1886913cb54db1acdf0e7' and sha(ROOT/'SAMPLE_SURVEY_RESPONSES_0141_R01.csv')=='723259199dd51973fc6473ec000234cc853fa1511be05864fdfd7b08bb452862','questionnaire_sha256':sha(ROOT/'QUESTIONNAIRE_ITEMS_0141_R01.csv'),'responses_sha256':sha(ROOT/'SAMPLE_SURVEY_RESPONSES_0141_R01.csv')})
script=pathlib.Path(__file__); receipt={'schema':'ttqs-one-0141-r06-source-math-qa-v1','observed_at_local':datetime.datetime.now().astimezone().isoformat(timespec='seconds'),'doc_id':'0141','requirement_id':'I19-E31','candidate_manuscript_sha256':sha(r6p),'verifier_script_sha256':sha(script),'questionnaire_sha256':sha(ROOT/'QUESTIONNAIRE_ITEMS_0141_R01.csv'),'sample_responses_sha256':sha(ROOT/'SAMPLE_SURVEY_RESPONSES_0141_R01.csv'),'period_summary_sha256':sha(ROOT/'SAMPLE_PERIOD_SUMMARY_0141_R01.csv'),'replacement_register_sha256':sha(ROOT/'SAMPLE_REPLACEMENT_REGISTER_0141_R06.csv'),'response_rows':len(rows),'all_rows_sample_synthetic':all(r['record_state']=='SAMPLE_SYNTHETIC' for r in rows),'period_recalculations':periods,'checks':checks,'all_checks_pass':all(c['match'] for c in checks),'scope':'Independent deterministic recalculation; no REAL evidence or formal acceptance inferred'}
out=ROOT/'R06_SOURCE_MATH_QA_RECEIPT.json'; out.write_text(json.dumps(receipt,ensure_ascii=True,indent=2)+'\n',encoding='utf-8'); print(json.dumps({'all_checks_pass':receipt['all_checks_pass'],'failed':[c for c in checks if not c['match']],'receipt_sha256':sha(out),'periods':periods},ensure_ascii=True))
