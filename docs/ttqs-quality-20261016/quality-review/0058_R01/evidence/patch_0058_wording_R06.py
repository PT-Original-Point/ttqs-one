from pathlib import Path
import json, hashlib, shutil

PKG = Path(__file__).resolve().parents[1]
WORKER = PKG / 'worker' / 'antigravity'
EVIDENCE = PKG / 'evidence'
src_json = WORKER / '0058_CONTENT_R05.json'
src_blue = WORKER / '0058_UNIQUE_BLUEPRINT_R05.md'
src_csv = WORKER / '0058_SYNTHETIC_REPLACEMENT_REGISTER_R05.csv'
src_builder = WORKER / '0058_build_R05.py'
new_json = WORKER / '0058_CONTENT_R06.json'
new_blue = WORKER / '0058_UNIQUE_BLUEPRINT_R06.md'
new_csv = WORKER / '0058_SYNTHETIC_REPLACEMENT_REGISTER_R06.csv'
new_builder = WORKER / '0058_build_R06.py'
sha=lambda p: hashlib.sha256(p.read_bytes()).hexdigest().upper()
candidate_path=PKG/'candidate'/'0058_R06.docx'
rendered_pdf_path=EVIDENCE/'render_R06_final'/'0058_R06.pdf'
if not rendered_pdf_path.exists(): rendered_pdf_path=EVIDENCE/'render_R06'/'0058_R06.pdf'
superseded_candidate_sha=sha(candidate_path) if candidate_path.exists() else None
superseded_pdf_sha=sha(rendered_pdf_path) if rendered_pdf_path.exists() else None
source_json_sha=sha(src_json)
assert source_json_sha == '771A1B063933BB52A393A215B3CCD342B079A70D5121B68312243BD13F7AB30E'
data=json.loads(src_json.read_text(encoding='utf-8'))
old_warning='【操作防呆與真實邊界特別警告】本節所列之表 7-1 與表 7-2 均為「可直接複製之空白操作表」，其用途為現場作業之格式引導。本空白表格與前述各節已填列之完整示範資料截然有別。為落實個資保護，公開版表件一律使用受控代碼，不列真名；必要之內部姓名對照清冊依權限另行安全保存。在真實案件實施時，志工必須依據真實服務事件逐欄填寫，嚴禁出現「待填」、「待核」或空白交差之情事。'
new_warning='【操作防呆與真實邊界特別警告】本節所列之表 7-1 與表 7-2 均為「可直接複製之空白操作表」，其用途為現場作業之格式引導。本空白表格與前述各節已填列之完整示範資料截然有別。為落實個資保護，公開版表件一律使用受控代碼，不列真名；必要之內部姓名對照清冊依權限另行安全保存。在真實案件實施時，志工必須依據真實服務事件逐欄填寫；如有未記載、未完成查核或空白欄位，不得標示為完整紀錄或交付審查。'
paragraph_hits=0
for section in data['sections']:
    for i,text in enumerate(section.get('paragraphs', [])):
        if text == old_warning:
            section['paragraphs'][i]=new_warning; paragraph_hits+=1
assert paragraph_hits == 1, paragraph_hits
version_table=next(t for s in data['sections'] for t in s.get('tables',[]) if t.get('caption','').startswith('表 10-3'))
r00=[r for r in version_table['rows'] if r[0]=='R00']; r04=[r for r in version_table['rows'] if r[0]=='R04']
assert len(r00)==1 and len(r04)==1
assert r00[0][3]=='舊版規劃建置，正文存在主要紀錄待填缺陷，未具完整計算與四欄規範'
assert r04[0][3]=='修正 R03 仍殘留的既有行政/督導職務、特定核定機關及現行制度用語；明確標示表單與流程為待核定提案；未新增合成案例數據。'
r00[0][3]='舊版規劃建置，正文主要紀錄欄位未完成，未具完整計算與四欄規範'
r04[0][3]='修正 R03 仍殘留的既有行政/督導職務、特定核定機關及現行制度用語；明確標示表單與流程為審議中提案，尚未核准、未生效；未新增合成案例數據。'
assert not any(r[0]=='R06' for r in version_table['rows'])
version_table['rows'].append(['R06','2026-10-18','正文用語及版次標籤校正','調整操作警示與歷史缺陷敘述以符合 Blueprint 拒收條件；修正表 1-1 將本候選版次誤列 R05 的錯標；不變更案例數據、核權界線或表格操作要求。','PRE_BUILD_SYNTHETIC_DRAFT / 待建置與審查'])
table_1_1=next(t for s in data['sections'] for t in s.get('tables',[]) if t.get('caption','').startswith('表 1-1'))
version_label_hits=0
for row in table_1_1['rows']:
    for i,cell in enumerate(row):
        if cell == '0058（版次 R05）':
            row[i]='0058（版次 R06）'
            version_label_hits+=1
assert version_label_hits == 1, version_label_hits
data['metadata']['revision']='R06_FORBIDDEN_TERMS_AND_REVISION_LABEL_REPAIR'
assert data['metadata']['doc_id']=='0058' and data['metadata']['requirement_id']=='I13-E02' and data['metadata']['checkbox_serial']=='062'
assert data['metadata']['case_id']=='SYN-0058-202608'
serialized=json.dumps(data,ensure_ascii=False)
for forbidden in ('待填','待核','會後補填'):
    assert forbidden not in serialized, f'forbidden literal remains: {forbidden}'
assert len(data.get('synthetic_facts',[]))==41, len(data.get('synthetic_facts',[]))
new_json.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
blue=src_blue.read_text(encoding='utf-8')
old_top='| 文件版次 (revision) | R03（真實性與提案邊界校正版） |'
assert old_top in blue
blue=blue.replace(old_top,'| 文件版次 (revision) | R06（正文禁用字句修正；承接 R04/R05 邊界與版面修復） |',1)
blue += '''\n\n## R06 正文用語、版次標籤及表格分頁修正記錄（整合者）\n\n依 OpenCode v2 對 R05 exact SHA 的獨立審查，修正 §7 操作警示及表 10-3 歷史列中觸發 Blueprint 拒收掃描的字串；改以「未記載、未完成查核或空白欄位不得標示為完整紀錄」描述實際拒收狀況，歷史摘要改為欄位未完成及提案審議中。另修正表 1-1 將 R06 誤標為 R05 的版本標籤，並將表 3-1 標題與表頭移至新頁，避免其與資料列分離。沒有改動官方需求、治理權限界線、任何人物/日期/分母/計算/41 筆合成事實或操作表結構。新候選須重新建置、渲染、逐頁檢查及獨立 exact-SHA 審查；R05 的獨立審查維持 PARTIAL 歷史結果，不移轉為 R06 驗收。\n'''
new_blue.write_text(blue,encoding='utf-8',newline='\n')
shutil.copyfile(src_csv,new_csv)
builder=src_builder.read_text(encoding='utf-8')
assert '0058_build_R05.py' in builder and '0058_CONTENT_R05.json' in builder and 'candidate/0058_R05.docx' in builder
builder=builder.replace('R05','R06')
builder=builder.replace('R06 真實性與提案邊界校正版','R06 正文用語及版次標籤校正版').replace('R06（真實性與提案邊界校正版）','R06（正文用語及版次標籤校正版）')
keep_anchor='            cap_p.paragraph_format.keep_with_next = True'
assert builder.count(keep_anchor)==1
builder=builder.replace(keep_anchor, keep_anchor+'\n            if caption.startswith("表 3-1"):\n                cap_p.paragraph_format.page_break_before = True',1)
new_builder.write_text(builder,encoding='utf-8',newline='\n')
outputs=[new_json,new_blue,new_csv,new_builder]
receipt={
 'operation':'targeted_integrator_wording_repair',
 'source_revision':'R05', 'target_revision':'R06',
 'trigger':'Independent OpenCode v2 exact-SHA review R03 marked PARTIAL; literal banned placeholder wording in §7 and Table 10-3 conflicted with the document Blueprint rejection rule.',
 'review_session':'ses_eb4dcf052ffes9mG02pgpKHq5V',
 'reviewed_source_docx_sha256':'34DC48094F3260F65477BBD914F45966965A11D15D6A5FE7AA2666068310A020',
 'source_content_sha256':source_json_sha,
 'targeted_replacements':{'§7 warning':paragraph_hits,'Table10-3 R00':1,'Table10-3 R04':1,'revision_history_rows_added':1,'Table1-1 revision label R05 to R06':version_label_hits,'Table3-1 caption/header orphan page break':1},
 'synthetic_fact_count_before':41,'synthetic_fact_count_after':len(data.get('synthetic_facts',[])),
 'mapping':{'doc_id':'0058','requirement_id':'I13-E02','official_checkbox_serial':'062','case_id':'SYN-0058-202608'},
 'forbidden_literals_absent_from_content_json':True,
 'superseded_pre_fix_candidate_sha256':superseded_candidate_sha,
 'superseded_pre_fix_render_pdf_sha256':superseded_pdf_sha,
 'docx_built':False,'rendered':False,'independent_review':'PENDING exact R06 candidate SHA',
 'outputs':[{'path':p.relative_to(PKG).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in outputs]
}
receipt_path=EVIDENCE/'patch_0058_wording_R06.json'
receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'receipt':str(receipt_path),'receipt_sha256':sha(receipt_path),'outputs':receipt['outputs']},ensure_ascii=False,indent=2))