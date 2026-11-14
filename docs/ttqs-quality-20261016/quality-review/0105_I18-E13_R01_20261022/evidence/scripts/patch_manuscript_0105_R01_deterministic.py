from pathlib import Path
import hashlib,json,datetime
pkg=Path(r'E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0105_I18-E13_R01_20261022')
md=pkg/'writer'/'opencode_writer_manuscript_0105_R01.md'
text=md.read_text(encoding='utf-8')
before=hashlib.sha256(text.encode('utf-8')).hexdigest()
old_sop='⑧依 Form G 決策表判定.'
new_sop='⑧依第十四節「決策／HOLD 表」判定.'
# The source sentence ends with the Chinese full stop. Keep exact matching to prevent broad edits.
old_sop='⑧依 Form G 決策表判定。'; new_sop='⑧依第十四節「決策／HOLD 表」判定。'
assert text.count(old_sop)==1
text=text.replace(old_sop,new_sop)
old_q='2. 依您可觀察的情況，服務後續處理較順利。（共同題「依您可觀察的資料，訓練後工作／服務表現有改善」）'
new_q='2. 依您可觀察的資料，訓練後工作／服務表現有改善。（與學員共同計分題同題；無法觀察請選 N/A，不必推論因果）'
assert text.count(old_q)==1
text=text.replace(old_q,new_q)
old_period='- 收卷期間：〔起〕～〔止〕【SAMPLE / SYNTHETIC】'
new_period='- 收卷期間：`SYN-W1～SYN-W2`（虛構相對週次，非真實日期）【SAMPLE / SYNTHETIC】'
assert text.count(old_period)==1
text=text.replace(old_period,new_period)
start=text.index('| fact_id | case_id | 文件 | 位置 | 虛構值 | 需要的真實來源 | 負責角色 | 狀態 | 替換指示 |')
end=text.index('**禁止使用**：虛構姓名、雇主、簽名、核准、第三方紀錄。',start)
rows=[]
def add(location,value,source,owner,instruction):
    n=len(rows)+1; fid=f'SYN-0105-F{n:03d}'
    clean=lambda s: str(s).replace('|','／').replace('\n',' ')
    rows.append(f'| {fid} | SYN-0105-CASE-01 | 0105 | {clean(location)} | {clean(value)} | {clean(source)} | {clean(owner)} | SAMPLE/SYNTHETIC; HOLD | {clean(instruction)} |')
add('案例識別','SYN-0105-CASE-01','正式案件登錄來源','R1','替換為真實去識別案件碼')
add('課程識別','SYN-0105-COURSE-01','實際開課核准及課程紀錄','R6','替換並查核來源')
add('Form A 邀請總數','12','實際邀請清冊的去識別計數','R1','重新計數')
add('Form A 學員邀請數','7','實際邀請清冊的去識別計數','R1','重新計數')
add('Form A 目標客戶邀請數','5','實際邀請清冊的去識別計數','R1','重新計數')
add('Form A 收卷期間','SYN-W1～SYN-W2','實際發放／截止時間紀錄','R2','用真實時間戳替換')
add('Form D 有效總份數','10','去識別收卷登記表及有效性規則','R2','重新判定有效份數')
add('Form D 學員有效份數','6','去識別收卷登記表','R2','重新計數')
add('Form D 客戶有效份數','4','去識別收卷登記表','R2','重新計數')
add('Form D 整體回收率','10/12=83.3%','邀請及有效問卷原始計數','R4','依新分子分母重算')
add('Form D 學員回收率','6/7=85.7%','邀請及有效問卷原始計數','R4','依新分子分母重算')
add('Form D 客戶回收率','4/5=80.0%','邀請及有效問卷原始計數','R4','依新分子分母重算')
for group,counts in [('全體',[('非常同意',4),('同意',3),('普通',2),('不同意',1),('非常不同意',0),('N/A',0)]),('學員',[('非常同意',2),('同意',2),('普通',1),('不同意',1),('非常不同意',0),('N/A',0)]),('目標客戶',[('非常同意',2),('同意',1),('普通',1),('不同意',0),('非常不同意',0),('N/A',0)])]:
    for label,count in counts:
        add(f'Form D 共同題/{group}/{label}份數',count,'去識別問卷原始作答','R4','以逐題原始作答替換')
add('Form D 全體正向占比','7/10=70.0%','去識別原始作答及有效份數','R4','重新計算，定義正向為4或5')
add('Form D 學員正向占比','4/6=66.7%','去識別原始作答及有效份數','R4','重新計算')
add('Form D 客戶正向占比','3/4=75.0%','去識別原始作答及有效份數','R4','重新計算')
add('Form D 選項平均','40/10=4.0/5','去識別原始作答及有效份數','R4','重新計算或刪除')
for location,value,source in [('Form E 基準檢核總筆數','10筆','真實基準期抽樣及抽樣方法紀錄'),('Form E 基準完整筆數','5筆','真實基準期檢核表'),('Form E 基準完整率','5/10=50%','真實基準期檢核表'),('Form E 目標檢核總筆數','10筆','經核定的目標及抽樣設計'),('Form E 目標完整筆數','8筆','經核定的目標及計畫'),('Form E 目標完整率','8/10=80%','經核定的目標及計畫'),('Form F 追蹤檢核總筆數','10筆','真實追蹤樣本及抽樣方法紀錄'),('Form F 追蹤完整筆數','8筆','真實追蹤檢核表'),('Form F 追蹤完整率','8/10=80%','真實追蹤檢核表')]:
    add(location,value,source,'R2/R4','以真實且可追溯來源替換並重算')
add('Form F 絕對變化','+3筆/+30個百分點','真實基準與追蹤檢核表','R4','依同口徑比較重算')
add('Form F 相對變化','+60%','真實基準與追蹤檢核表','R4','基準為0時不得計算；本例基準非0')
for loc,val,src in [('Form E 第1週行動','採用統一檢核清單','實際課後行動紀錄'),('Form E 第2週行動','每案完成後雙人確認','實際課後行動紀錄'),('Form E 第3週行動','檢查執行差異並記錄障礙','實際追蹤紀錄'),('Form F 第4週追蹤期限','課後第4週','實際追蹤日程及執行紀錄')]:
    add(loc,val,src,'R1/R2','以實際核定計畫及執行證據替換')
for role,desc in [('R1','邀請者'),('R2','收集者'),('R3','去識別者'),('R4','分析者'),('R5','核准者'),('R6','保管者')]:
    add(f'角色代碼 {role}',desc,'經確認的實際職掌及授權紀錄','R5','核對真實職掌；未確認前不得對外代表授權')
for loc,val in [('Form F 其他可能因素1','同期人力調整'),('Form F 其他可能因素2','檢核清單本身簡化'),('Form F 其他可能因素3','紀錄習慣改變')]:
    add(loc,val,'同期變更紀錄或其他可核對來源','R4','只保留有來源支持的因素；否則標未知假設')
add('Form F 示範處置','CLOSED_FOR_SAMPLE','實際覆核及結案紀錄','R5','示範標籤不得移除；真實結案須由有權者核准')
add('Form F 示例來源定位','虛構示範行政清單','真實原始行政紀錄及受控檔案定位','R6','以正式來源路徑及檔案版本替換')
header='| fact_id | case_id | 文件 | 位置 | 虛構值 | 需要的真實來源 | 負責角色 | 狀態 | 替換指示 |'
separator='|---|---|---|---|---|---|---|---|---|'
table='每列只記一項合成值或一項計算結果；比例、分組計數、週次、角色及替代解釋分開登錄。所有列目前均為 SAMPLE/SYNTHETIC，狀態 HOLD。\n\n'+header+'\n'+separator+'\n'+'\n'.join(rows)+'\n\n'
text=text[:start]+table+text[end:]
md.write_text(text,encoding='utf-8',newline='\n')
after=hashlib.sha256(text.encode('utf-8')).hexdigest()
receipt={'receipt_id':'TTQS-0105-MANUSCRIPT-DETERMINISTIC-REPAIR-R01','observed_at_tpe':datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(),'doc_id':'0105','requirement_id':'I18-E13','input_writer_sha256':before,'repaired_manuscript_sha256':after,'repair_count':3,'repairs':['Fixed SOP reference to nonexistent Form G; it now points to the actual Section 14 decision/HOLD table.','Made the target-customer common item text exactly match the learner common item used for the shared response distribution.','Completed Form A synthetic collection-window example using relative weeks and expanded the replacement register to one synthetic value/calculation/role/alternative factor per row.'],'replacement_register_rows':len(rows),'candidate_docx_built':False,'semantic_acceptance':'PENDING_INDEPENDENT_REVIEW'}
rp=pkg/'evidence'/'manuscript_repair_receipt_0105_R01.json';rp.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False,indent=2))