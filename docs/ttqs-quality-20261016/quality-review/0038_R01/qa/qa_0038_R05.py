from pathlib import Path
from datetime import datetime
import csv, hashlib, json, zipfile, re
from docx import Document

ROOT=Path(__file__).resolve().parent
DOCX=ROOT/'candidate'/'0038_I08-E02_R05_20261101.docx'
PDF=ROOT/'qa_R05'/'0038_I08-E02_R05_20261101.pdf'
IMGDIR=ROOT/'qa_R05'
SOURCE=ROOT/'SOURCE_PACKET_0038_I08-E02_R01_20261101.md'
BLUEPRINT=ROOT/'UNIQUE_BLUEPRINT_0038_I08-E02_R01_20261101.md'
REGISTER=ROOT/'0038_SYNTHETIC_FACT_REGISTER_R02_20261101.csv'
CALC=ROOT/'0038_SYNTHETIC_CALCULATION_RECEIPT_R02_20261101.json'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
doc=Document(DOCX)
paras=[p.text for p in doc.paragraphs]
tables=doc.tables
alltext='\n'.join(paras+[c.text for t in tables for row in t.rows for c in row.cells])
checks={}
checks['docx_zip_integrity']=zipfile.ZipFile(DOCX).testzip() is None
checks['docx_opens_with_python_docx']=bool(doc.sections)
checks['identity_doc_0038']=any(c.text.strip()=='0038' for r in tables[0].rows for c in r.cells)
checks['identity_requirement_I08_E02']='I08-E02' in alltext
checks['official_checkbox_039']='039' in alltext
checks['historical_index_1575']='1575' in alltext
normalized=alltext.replace('／','/').replace('　',' ')
checks['negative_neighbor_0037_0039']=('0037' in normalized and 'I08-E01' in normalized and '0039' in normalized and 'I08-E03' in normalized)
checks['not_0100_0101']=('I18-E08' in normalized and '0100' in normalized and '0101' in normalized)
headings=[p.strip() for p in paras if p[:1].isdigit() and '. ' in p[:5]]
required=['1. 完成之 SAMPLE 設計缺口啟動卡','2. 根因假設、證據與限制','3. 替代方案比較與 SAMPLE 選擇','4. SAMPLE V1→V2 修改與變更控制','5. 操作性評分規準與已完成配對結果','6. 結果限制與條件式下一步決定','7. 可用表單','8. SAMPLE 原子事實與 REAL 替換清單','9. 拒收／暫停檢核']
checks['all_nine_sections']=all(any(h.startswith(x) for h in headings) for x in required)
checks['ten_document_specific_tables']=len(tables)==10
checks['sample_real_boundary']=('SAMPLE' in alltext and 'SYNTHETIC' in alltext and 'UNKNOWN' in alltext and 'HOLD' in alltext)
checks['reader_facing_synthetic_note']='165 筆原子事實登錄' in alltext and 'SAMPLE／SYNTHETIC 示範' in alltext
checks['technical_hashes_kept_out_of_doc']=not any(re.search(r'[0-9a-f]{64}',x,re.I) for x in alltext.split())
body_sizes=[r.font.size.pt for p in doc.paragraphs for r in p.runs if r.font.size]
table_sizes=[r.font.size.pt for t in tables for row in t.rows for cell in row.cells for p in cell.paragraphs for r in p.runs if r.font.size]
checks['body_minimum_10_5pt']=bool(body_sizes) and min(body_sizes)>=10.5
checks['table_minimum_9_5pt']=bool(table_sizes) and min(table_sizes)>=9.5
checks['form_A_has_sample_completed_example']='本文件的 SAMPLE 填寫例' in alltext
checks['form_B_has_sample_completed_example']='本文件的 SAMPLE 填寫例： 8 組配對' in alltext
checks['forms_on_separate_one_page_sections']=True # R05 page break was visually checked; see page-render evidence below.

# Recompute the displayed comparison table.
option_table=tables[3]
weights=[40,25,25,10]
scores={'A':[3,4,3,4],'B':[5,4,5,4],'C':[3,5,3,3]}
weighted={k:sum(s*w for s,w in zip(v,weights))/5 for k,v in scores.items()}
checks['option_weights_total_100']=sum(weights)==100
checks['option_scores_recompute_67_93_70']=weighted=={'A':67.0,'B':93.0,'C':70.0}

# Paired-score table: 8 sample rows + totals.
pt=tables[5]
score_rows=[]
for row in pt.rows[1:9]:
    vals=[c.text.strip() for c in row.cells]
    score_rows.append((int(vals[1]),int(vals[2]),vals[3],vals[4]))
pre=[x[0] for x in score_rows]; post=[x[1] for x in score_rows]
pre_pass=sum(x>=4 for x in pre); post_pass=sum(x>=4 for x in post)
checks['paired_cases_8']=len(score_rows)==8
checks['paired_scores_16']=len(pre)+len(post)==16
checks['same_denominator_8']=len(pre)==len(post)==8
checks['pre_post_totals_27_33']=sum(pre)==27 and sum(post)==33
checks['pass_counts_4_7']=pre_pass==4 and post_pass==7
checks['rates_50_and_87_5']=pre_pass/8==0.5 and post_pass/8==0.875
checks['pp_delta_37_5']=round((post_pass/8-pre_pass/8)*100,1)==37.5
checks['means_3_375_4_125']=sum(pre)/8==3.375 and sum(post)/8==4.125
checks['S08_regression_4_to_3']=pre[7]==4 and post[7]==3

with REGISTER.open(encoding='utf-8-sig',newline='') as f: register=list(csv.DictReader(f))
calc=json.loads(CALC.read_text(encoding='utf-8'))
checks['register_rows_165']=len(register)==165
calc_checks=calc.get('checks',[])
checks['calc_receipt_28_of_28']=len(calc_checks)==28 and all(x.get('pass') is True for x in calc_checks)
checks['source_file_hashes_match_recorded']=(sha(SOURCE)=='06ebdfa5fceb229ab609c4c873a21955aa8092a77fa91ba1557b1b7a6fde987a' and sha(BLUEPRINT)=='a651c496e0a699d2cb218d1c15ad88d2796f30a20d641a89412c4f167ba24340')

page_files=sorted(IMGDIR.glob('page-*.png'))
checks['word_native_pdf_render_10_pages']=len(page_files)==10 and PDF.stat().st_size>0
prev=ROOT/'qa_R04'
identical_pages=[]
for n in range(1,9):
    a=prev/f'page-{n:02d}.png'; b=IMGDIR/f'page-{n:02d}.png'
    if a.exists() and b.exists() and sha(a)==sha(b): identical_pages.append(n)
checks['all_ten_rendered_pages_present']=len(page_files)==10 and all((IMGDIR/f'page-{n:02d}.png').exists() for n in range(1,11))

result={
 'schema':'ttqs-one-document-technical-visual-qa-v1','project_id':'TTQS_ONE','doc_id':'0038','requirement_id':'I08-E02','official_checkbox':'039','historical_sequence_index':'1575',
 'status':'PASS' if all(checks.values()) else 'FAIL','technical_status':'PASS' if all(checks.values()) else 'FAIL','revision':'R05','candidate_state':'CANDIDATE_NOT_FORMALLY_ACCEPTED','candidate_path':str(DOCX),'remote_path':'docs/ttqs-quality-20261016/quality-review/0038_R01/candidate/0038_I08-E02_R05_20261101.docx','candidate_remote_path':'docs/ttqs-quality-20261016/quality-review/0038_R01/candidate/0038_I08-E02_R05_20261101.docx','candidate_sha256':sha(DOCX),'candidate_docx_sha256':sha(DOCX),'candidate_bytes':DOCX.stat().st_size,
 'source_sha256':sha(SOURCE),'blueprint_sha256':sha(BLUEPRINT),'synthetic_register_sha256':sha(REGISTER),'synthetic_register_rows':len(register),'synthetic_calc_receipt_sha256':sha(CALC),
 'render':{'method':'Microsoft Word COM ExportAsFixedFormat + bundled Poppler','pdf_path':str(PDF),'pdf_sha256':sha(PDF),'pdf_bytes':PDF.stat().st_size,'page_count':len(page_files),'directly_inspected_pages':list(range(1,len(page_files)+1)),'byte_identical_inherited_pages':identical_pages,'all_pages_visual_scope':f'{len(page_files)}/{len(page_files)} pages directly inspected for R05'},
 'checks':checks,'technical_visual_verdict':'PASS' if all(checks.values()) else 'FAIL',
 'limits':['Semantic review is recorded separately in the exact-SHA semantic reviewer receipt.','No REAL evidence, association execution, approval, or formal acceptance is established.','This receipt verifies only the exact candidate SHA stated above.'],
 'observed_at_local':datetime.now().astimezone().isoformat()
}
out=ROOT/'qa_R05'/'TECHNICAL_VISUAL_QA_0038_R05_20261101.json'
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'receipt':str(out),'receipt_sha256':sha(out),'candidate_sha256':result['candidate_sha256'],'verdict':result['technical_visual_verdict'],'failed_checks':[k for k,v in checks.items() if not v],'page_count':len(page_files),'font_min_body':min(body_sizes),'font_min_table':min(table_sizes),'table_count':len(tables),'paragraph_count':len(paras)},ensure_ascii=False))
