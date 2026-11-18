# -*- coding: utf-8 -*-
from pathlib import Path
from docx import Document
import hashlib, json, re, sys
src=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0032_I06-E03_SOURCE_PREP_R01_20261118\candidate\0032_I06-E03_R04_SCOPED_ARITHMETIC_REPAIR.docx')
out=src.with_name('0032_I06-E03_R05_SCOPED_CONTRACT_REPAIR.docx')
receipt_path=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\EXTERNAL_WORK\TTQS_ONE_0032_I06-E03_W2_SCOPED_WRITER_R05_GEMINI38_20261118\SCOPED_REPAIR_RECEIPT_R05.json')
expected='70334325BEFE6C438337977D345A0B539AD164A68108895D1547856A2D362E05'
sha=lambda b:hashlib.sha256(b).hexdigest().upper()
if not src.exists(): raise SystemExit('R04 candidate missing')
if sha(src.read_bytes())!=expected: raise SystemExit('R04 candidate SHA changed')
if out.exists(): raise SystemExit('Refusing to overwrite existing R05')
doc=Document(src)
changes=[]
def set_para(p,new,tag):
 old=p.text
 if not old: raise ValueError(f'empty paragraph {tag}')
 runs=p.runs
 if runs:
  runs[0].text=new
  for r in runs[1:]: r.text=''
 else: p.add_run(new)
 changes.append({'target':tag,'before':old,'after':new})
def p_once(pred,new,tag):
 hits=[p for p in doc.paragraphs if pred(p.text)]
 if len(hits)!=1: raise ValueError(f'{tag}: expected one paragraph, got {len(hits)}')
 set_para(hits[0],new,tag)
def cset(cell,new,tag):
 old=cell.text
 if len(cell.paragraphs)>1:
  p=cell.paragraphs[0]
  if p.runs:
   p.runs[0].text=new
   for r in p.runs[1:]:r.text=''
  else:p.add_run(new)
  for p2 in cell.paragraphs[1:]:
   for r in p2.runs:r.text=''
 else:
  p=cell.paragraphs[0]
  if p.runs:
   p.runs[0].text=new
   for r in p.runs[1:]:r.text=''
  else:p.add_run(new)
 changes.append({'target':tag,'before':old,'after':new})
def table_by_first_cell(value):
 hits=[t for t in doc.tables if t.rows and t.rows[0].cells[0].text.strip()==value]
 if not hits: raise ValueError(f'table header not found: {value}')
 return hits[0]
# Official identity and primary document genre.
p_once(lambda s:s=='訓練機構職能與對外訓練執行能力評核','訓練機構具備執行訓練業務相關職能的說明_完整工作稿','title')
p_once(lambda s:s.startswith('本文件提供一套可操作的內部能力評核'),'本文件說明訓練機構執行訓練業務所需的分工、人員職能、對外訓練服務流程，以及主管將發展方向轉為工作目標、資源安排與檢討的方式。第二至第五節為機構能力說明；第六至第十節是SAMPLE/SYNTHETIC內部能力檢視、改善與複核示例，僅協助讀者理解操作，不是官方評分標準、真實機構評核結果或核准。未經真實原件核實的組織、人員、授權、第三方師資與服務成果均維持UNKNOWN。','purpose_and_genre')
p_once(lambda s:s=='一 評核結論與操作規則','一 執行能力說明摘要與示例限制','section_1_heading')
p_once(lambda s:s.startswith('基準演練為61.25/100'),'SAMPLE/SYNTHETIC內部演練：基準加權61.25/100，低於本文件自訂75分示例門檻；關鍵職能主責覆蓋3/5=60%，備援覆蓋4/5=80%。主責C03、C06未達示例基準，備援C03無合格代理。改善後示例為75/100、主責與備援各5/5；僅說明本文示例規則，不表示真實機構能力或官方評核結果。','summary_statement')
headings={
 '評核步驟':'示例操作步驟',
 '角色能力評分':'示例角色能力評分',
 '六 評核題項與證據判讀':'附錄A SAMPLE/SYNTHETIC 內部能力檢視示例',
 '七 評核題項與證據判讀續':'附錄A SAMPLE/SYNTHETIC 內部能力檢視示例續',
 '一致性與評分錨點':'附錄A 內部示例評分錨點',
 '八 加權計分與基準判定':'附錄A 內部示例加權計算與基準判讀',
 '九 差距改善與責任追蹤':'附錄A 差距改善與責任追蹤示例',
 '十 複評與關閉判定':'附錄A 改善後示例複核',
 '複評操作':'示例複核操作'
}
for old,new in headings.items():p_once(lambda s,old=old:s==old,new,'heading:'+old)
p_once(lambda s:s.startswith('基準演練主責達標3/5=60%'),'基準示例：主責達標3/5=60%，備援達標4/5=80%。主責C03及C06未達示例基準；備援C03無合格代理。講師資格原件仍為UNKNOWN。缺合格師資、核准或資源時，ROLE-04停止流程、ROLE-01在授權內升級；不得因容量充足而承諾服務。','coverage_narrative')
p_once(lambda s:s.startswith('示例判讀：關鍵功能主責3/5=60%'),'示例判讀：主責達標3/5=60%，備援達標4/5=80%；主責C03及C06未達示例基準，備援C03無合格代理。','q02_example')
# Coverage table.
t2=table_by_first_cell('面向')
backup=[r for r in t2.rows if r.cells[0].text.strip()=='備援能力覆蓋']
if len(backup)!=1:raise ValueError('backup coverage row mismatch')
cset(backup[0].cells[1],'4/5=80%','coverage_table_baseline_backup')
# Decision and action tables.
t14=doc.tables[13]
keyroles=[r for r in t14.rows if r.cells[0].text.strip()=='關鍵角色']
if len(keyroles)!=1:raise ValueError('key roles decision row mismatch')
cset(keyroles[0].cells[2],'主責3/5=60%、備援4/5=80%；主責C03/C06及備援C03未達示例基準','decision_table_coverage')
t15=table_by_first_cell('ID')
a02=[r for r in t15.rows if r.cells[0].text.strip()=='A02']
a04=[r for r in t15.rows if r.cells[0].text.strip()=='A04']
if len(a02)!=1 or len(a04)!=1:raise ValueError('A02/A04 row count mismatch')
cset(a02[0].cells[1],'主責覆蓋3/5=60%、備援覆蓋4/5=80%；主責C03/C06及備援C03未達示例基準','A02_gap')
cset(a04[0].cells[1],'基準示例索引8筆中2筆缺本文定位；外部原件未取得','A04_gap')
cset(a04[0].cells[2],'為八筆SAMPLE/SYNTHETIC索引補本文章節定位；不編造外部來源、版本、日期或頁碼，未取得的真實資料維持UNKNOWN。','A04_action')
cset(a04[0].cells[5],'8/8筆示例索引均有本文定位；未取得的外部原件及頁碼維持UNKNOWN。','A04_acceptance')
# Existing registered coverage fact only; no new fact ID.
t20=table_by_first_cell('Fact ID')
cover=[r for r in t20.rows if r.cells[0].text.strip()=='SYN-COVER-01']
evreg=[r for r in t20.rows if r.cells[0].text.strip()=='SYN-EV-01至08']
if len(cover)!=1 or len(evreg)!=1:raise ValueError('fact register rows mismatch')
cset(cover[0].cells[1],'SAMPLE/SYNTHETIC：5項關鍵職能；主責3/5=60%、備援4/5=80%；複評主責及備援各5/5=100%。','SYN-COVER-01_register')
cset(evreg[0].cells[1],'SAMPLE/SYNTHETIC：八筆模擬證據索引及本文內定位；本文定位僅供查找示例，不是外部原件。','SYN-EV_register')
# Correct all residual coverage-only phrases and assert no other 2/5/40% coverage remains.
# Index: distinguish an internal sample anchor from an authentic external source locator.
p_once(lambda s:s.startswith('下列為模擬材料索引'),'下列索引列出SAMPLE/SYNTHETIC示例材料及本文件內部定位，僅供查找本文示例，不代表外部證據。真實原件名稱、版本、日期、責任角色及印刷頁碼未取得時維持UNKNOWN。','evidence_index_intro')
index=table_by_first_cell('索引')
anchors={
 'SYN-EV-01':'第二節「組織分工與代理安排」角色矩陣',
 'SYN-EV-02':'第三節「職能基準與能力矩陣」及附錄A Q02示例',
 'SYN-EV-03':'第四節「對外訓練服務執行能力鏈」師資與採購節點',
 'SYN-EV-04':'第四節「對外訓練服務執行能力鏈」資源準備與容量計算',
 'SYN-EV-05':'第十一節「證據索引與真實性界線」示例索引',
 'SYN-EV-06':'第四節「容量及訓後追蹤計算」',
 'SYN-EV-07':'第五節「訓練主管規劃與執行能力」',
 'SYN-EV-08':'附錄A「差距改善與責任追蹤示例」及「改善後示例複核」'
}
seen=[]
for row in index.rows:
 id=row.cells[0].text.strip()
 if id in anchors:
  seen.append(id)
  row.cells[3].add_paragraph('本文內定位：'+anchors[id]+'；外部REAL原件及頁碼：UNKNOWN。')
if set(seen)!=set(anchors) or len(seen)!=8:raise ValueError(f'evidence index ids mismatch: {seen}')
# Replace eight blank actual-record lines with filled SAMPLE/SYNTHETIC records; all IDs already registered.
records=[
 'SAMPLE/SYNTHETIC演練紀錄：來源ID SYN-EV-01；本文定位：第二節「組織分工與代理安排」；REAL原件與真實評核：UNKNOWN；示例分數3/4、權重15。理由：示例有角色分工及升級路徑，真實授權仍未核實。',
 'SAMPLE/SYNTHETIC演練紀錄：來源ID SYN-COVER-01、SYN-EV-02；本文定位：第三節「職能基準與能力矩陣」；REAL原件與真實評核：UNKNOWN；示例分數2/4、權重10。理由：主責達標3/5、備援達標4/5，但主責C03/C06及備援C03未達示例基準。',
 'SAMPLE/SYNTHETIC演練紀錄：來源ID SYN-EV-03；本文定位：第四節「對外訓練服務執行能力鏈」；REAL原件與真實評核：UNKNOWN；示例分數2/4、權重15。理由：示例流程有核驗及缺件停止點，但未提供第三方資格原件。',
 'SAMPLE/SYNTHETIC演練紀錄：來源ID SYN-FLOW-01至08、SYN-CASE-01；本文定位：第四節「對外訓練服務執行能力鏈」；REAL原件與真實評核：UNKNOWN；示例分數3/4、權重15。理由：八個模擬節點連成完整流程；12名模擬學員、16席及8小時均非實際執行紀錄。',
 'SAMPLE/SYNTHETIC演練紀錄：來源ID SYN-EV-05；本文定位：第十一節「證據索引與真實性界線」；REAL原件與真實評核：UNKNOWN；示例分數2/4、權重10。理由：基準示例曾有2筆索引缺本文定位；A04示例補齊後8/8有本文定位，外部原件仍未知。',
 'SAMPLE/SYNTHETIC演練紀錄：來源ID SYN-DIR-01、SYN-EV-07；本文定位：第五節「訓練主管規劃與執行能力」；REAL原件與真實評核：UNKNOWN；示例分數3/4、權重15。理由：示例以開課前5工作日及90%目標形成規劃鏈；真實策略與核准仍未知。',
 'SAMPLE/SYNTHETIC演練紀錄：來源ID SYN-EV-04、SYN-CASE-01；本文定位：第四節「容量及訓後追蹤計算」；REAL原件與真實評核：UNKNOWN；示例分數2/4、權重10。理由：12/16=75%可重算，但師資原件缺失時仍須停止，不得據此放行服務。',
 'SAMPLE/SYNTHETIC演練紀錄：來源ID SYN-ACT-01至05、SYN-REEVAL-01；本文定位：附錄A改善追蹤與複核示例；REAL原件與真實評核：UNKNOWN；示例分數2/4、權重10。理由：基準示例列有改善措施，須依同一規則完成複核；示例複評不代表外部核可。'
]
blank=[p for p in doc.paragraphs if p.text.startswith('實際評核紀錄：')]
if len(blank)!=8:raise ValueError(f'expected 8 blank record paragraphs, got {len(blank)}')
for i,(p,new) in enumerate(zip(blank,records),1):set_para(p,new,f'Q{i:02d}_completed_sample_record')
# Verify calculation/repair exhaustively over body and tables.
def all_text(d):
 vals=[p.text for p in d.paragraphs]
 for t in d.tables:
  for row in t.rows:
   vals.extend(c.text for c in row.cells)
 return '\n'.join(vals)
text_before=all_text(doc)
# Resolve residual occurrences only in explicitly targeted old expressions.
if '備援覆蓋2/5=40%' in text_before or '備援2/5=40%' in text_before or '9/9筆' in text_before:
 raise ValueError('residual blocking coverage/index count remains')
if '12-10=2' not in text_before and '未回覆2人' not in text_before:raise ValueError('R04 A03 correction was lost')
if '9/9' in text_before:raise ValueError('unsupported 9/9 remains')
if len([p for p in doc.paragraphs if p.text.startswith('SAMPLE/SYNTHETIC演練紀錄：')])!=8:raise ValueError('completed sample records missing')
if len(seen)!=8:raise ValueError('internal anchors missing')
# New candidate only; original R04 bytes remain untouched.
doc.save(out)
sha_out=sha(out.read_bytes())
receipt={'schema':'TTQS_ONE_0032_SCOPED_REPAIR_R05/1','work_id':'TTQS_ONE_0032_I06-E03_SCOPED_WRITER_R05_INTEGRATION_20261118','doc_id':'0032','requirement_id':'I06-E03','input_candidate_path':str(src),'input_candidate_sha256':expected,'output_candidate_path':str(out),'output_candidate_sha256':sha_out,'output_bytes':out.stat().st_size,'source_packet_sha256':'3540D60A59D0B11F53E45D73F25C2EDD53D8E0BCED015B39790530E902E5CED0','blueprint_sha256':'71CFFB64FDAE734A2DCEA333339BED77A6D15F471577EFBFDB60AD5694D80C46','repair_scope':['F1 backup coverage recalculation and gap wording','F3 eight index rows and internal locators','F4 capability-statement genre reframing','F9 eight completed SAMPLE/SYNTHETIC assessment records'],'preserved_existing_r04_a03_correction':True,'fact_ids_reused_only':True,'new_fact_ids':[],'table_index_ids':seen,'completed_q_record_count':len(blank),'residual_2_of_5_40_percent':False,'residual_9_of_9':False,'changes':changes,'candidate_status':'CANDIDATE_ONLY; technical, visual, and independent semantic QA not yet passed','recorded_at_tpe':'2026-11-18'}
receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'input_sha256':expected,'output_sha256':sha_out,'output_bytes':out.stat().st_size,'receipt_sha256':sha(receipt_path.read_bytes()),'changes':len(changes),'index_rows':len(seen),'completed_q_records':len(blank),'candidate_status':receipt['candidate_status']},ensure_ascii=True))