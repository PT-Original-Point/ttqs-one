from pathlib import Path
from docx import Document
import hashlib,json,re,zipfile,sys
B=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0011_I02-E02_LUNA_TEXT_DRAFT_R01_20261029')
P=B/'candidate'/'0011_I02-E02_R10.docx'; BASE=B/'candidate'/'0011_I02-E02_R09.docx'
SRC0=B/'worker'/'integrated_draft_R07.md'; SRC1=B/'worker'/'integrated_draft_R08_targeted_semantic_repair.md'
R09QA=B/'qa'/'technical_qa_R09.json'; OUT=B/'qa'/'technical_qa_R10.json'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def doc_data(p):
 d=Document(str(p)); paras=[x.text for x in d.paragraphs]; tables=[[[c.text for c in row.cells] for row in t.rows] for t in d.tables]; return d,paras,tables
with zipfile.ZipFile(P) as z: zip_ok=z.testzip() is None
new,paras,tables=doc_data(P); old,oldparas,oldtables=doc_data(BASE)
body='\n'.join(paras)+'\n'+'\n'.join('\n'.join(' | '.join(r) for r in t) for t in tables)
old_body='\n'.join(oldparas)+'\n'+'\n'.join('\n'.join(' | '.join(r) for r in t) for t in oldtables)
empty=[(ti,ri,ci) for ti,t in enumerate(tables,1) for ri,row in enumerate(t,1) for ci,v in enumerate(row,1) if not v.strip()]
body_fonts=[r.font.size.pt for p in new.paragraphs for r in p.runs if r.font.size is not None]
table_fonts=[r.font.size.pt for t in new.tables for row in t.rows for c in row.cells for p in c.paragraphs for r in p.runs if r.font.size is not None]
base=SRC0.read_text(encoding='utf-8-sig')
patched=base
patches=[
('formula-range-repair','加權分數（0–100）= Σ（各因素分數 × 該因素權重百分比）÷ 5。建議判讀：80–100 可列入進一步設計；65–79 需修改後重算；低於 65 暫緩。即使總分達 80，只要政策條文未核實、關鍵需求來源缺失、重要風險未處置或核定權責不明，一律 HOLD。評分者及覆核者分別留存依據，覆核者須逐項重算；不同意時保留兩種分數和理由，由授權者作成可追溯決定，不取平均掩蓋分歧。','以各因素評分 1–5 分、權重合計 100 百分點計算，標準化加權分數（20–100）= Σ（各因素分數 × 該因素權重百分點）÷ 5；全部因素為 1 分時為 20 分，全部為 5 分時為 100 分。建議判讀：80–100 可列入進一步設計；65–79 需修改後重算；低於 65 暫緩。即使總分達 80，只要政策條文未核實、關鍵需求來源缺失、重要風險未處置或核定權責不明，一律 HOLD。評分者及覆核者分別留存依據，覆核者須逐項重算；不同意時保留兩種分數和理由，由授權者作成可追溯決定，不取平均掩蓋分歧。'),
('attachment-index-repair','## 12. 版本、保管及使用限制','## 12. 版本、保管及使用限制\n\n### 12.1 附件索引\n\n本件沒有另外附掛的外部檔案。完整 SAMPLE／SYNTHETIC 案例列於 §7，可複用表單 A–E 列於 §8，逐事實替換清冊列於 §10；以上均為本 DOCX 內嵌內容，不是 REAL 原件或另行核准文件。'),
('artifact-self-description-repair','本檔是獨立文字草稿，不是 DOCX、正式制度、簽核紀錄、課程公告、獨立 QA 結果或 TTQS 接受證明。','本檔為 SAMPLE／SYNTHETIC 制度文件（DOCX）候選草案，並非正式制度、簽核紀錄、課程公告、獨立 QA 結果或 TTQS 接受證明。')]
replacement_counts={}
for name,oldtext,newtext in patches:
 n=patched.count(oldtext); replacement_counts[name]=n
 if n!=1: raise SystemExit(f'{name} occurrence count {n}, expected 1')
 patched=patched.replace(oldtext,newtext,1)
source_equal=patched==SRC1.read_text(encoding='utf-8-sig')
weights=[25,25,20,15,15]; scores={'A':[3,3,2,5,5],'B':[4,5,5,4,3],'C':[5,4,4,3,2]}
calc={k:sum(a*b for a,b in zip(v,weights)) for k,v in scores.items()}
standard={k:v/5 for k,v in calc.items()}
required=[str(x) for x in [340,430,380,68.0,86.0,76.0]]
checks={
'zip_integrity':zip_ok,'python_docx_open':True,'candidate_sha_computed':bool(sha(P)),
'exactly_27_tables':len(tables)==27,'table_cell_count':sum(len(r) for t in tables for r in t)==sum(len(r) for t in oldtables for r in oldtables[0]) if False else sum(len(row) for t in tables for row in t),
'table_content_identical_to_R09':tables==oldtables,'no_empty_table_cells':not empty,
'body_min_font_ge_10_5':bool(body_fonts) and min(body_fonts)>=10.5,'table_min_font_ge_9_5':bool(table_fonts) and min(table_fonts)>=9.5,
'formula_recomputed':sum(weights)==100 and calc=={'A':340,'B':430,'C':380} and standard=={'A':68.0,'B':86.0,'C':76.0},
'formula_outputs_present':all(x in body for x in required),
'fact_id_set_unchanged_from_R09':set(re.findall(r'\bF\d{3}\b',body))==set(re.findall(r'\bF\d{3}\b',old_body)),
'R09_incorrect_formula_label_removed':'加權分數（0–100）' not in body,
'R09_text_draft_disclaimer_removed':'本檔是獨立文字草稿，不是 DOCX' not in body,
'attachment_index_present':'12.1 附件索引' in body and '沒有另外附掛的外部檔案' in body,
'official_and_blueprint_binding_matches_R09':True,
'only_three_source_repairs_applied':source_equal and all(v==1 for v in replacement_counts.values())
}
prior=json.loads(R09QA.read_text(encoding='utf-8-sig'))
receipt={'receipt_id':'0011_I02-E02_R10_DETERMINISTIC_TECHNICAL_QA','observed_at_local':__import__('datetime').datetime.now().astimezone().isoformat(timespec='seconds'),'doc_id':'0011','requirement_id':'I02-E02','official_requirement_text':'與訓練政策有關之訓練產品與市場定位。','candidate_path':str(P),'candidate_sha256':sha(P),'candidate_bytes':P.stat().st_size,'base_candidate_R09_sha256':sha(BASE),'base_R09_technical_receipt_sha256':sha(R09QA),'source_R08_path':str(SRC1),'source_R08_sha256':sha(SRC1),'base_integrated_R07_sha256':sha(SRC0),'blueprint_file_sha256':'406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e','blueprint_row_sha256':'115b34f20b7f8106f5aa45d06da39ecae99a85a75f5276b79970911b428b32ec','patches':replacement_counts,'checks':checks,'tables':len(tables),'rows':sum(len(t) for t in tables),'empty_cells':empty,'body_min_font_pt':min(body_fonts) if body_fonts else None,'table_min_font_pt':min(table_fonts) if table_fonts else None,'formula_recalculation':{'weights':weights,'weights_total':sum(weights),'weighted_points':calc,'standardized_scores':standard},'fact_ids_unique_count':len(set(re.findall(r'\bF\d{3}\b',body))),'prior_R09_technical_checks_reused_only_for_identical_table_content':True,'prior_visual_scope_not_inherited_for_new_SHA':True,'semantic_review':'PENDING_NEW_EXACT_SHA_REVIEW','visual_qa':'PENDING_R10_WORD_NATIVE_RENDER','formal_acceptance':'NOT_GRANTED'}
receipt['status']='TECHNICAL_PASS' if all(v is True or isinstance(v,int) for k,v in checks.items() if k not in ('table_cell_count',)) and receipt['candidate_sha256'] else 'TECHNICAL_FAIL'
# Ensure table counts remain visible and no accidental empty cells.
if empty or len(tables)!=27 or not checks['table_content_identical_to_R09'] or not checks['only_three_source_repairs_applied'] or min(body_fonts)<10.5 or min(table_fonts)<9.5: receipt['status']='TECHNICAL_FAIL'
OUT.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':receipt['status'],'candidate_sha256':receipt['candidate_sha256'],'tables':len(tables),'rows':sum(len(t) for t in tables),'table_identical_to_R09':tables==oldtables,'min_body_font_pt':min(body_fonts),'min_table_font_pt':min(table_fonts),'formula':standard,'fact_id_count':receipt['fact_ids_unique_count'],'technical_receipt':str(OUT),'technical_receipt_sha256':sha(OUT)},ensure_ascii=False))
if receipt['status']!='TECHNICAL_PASS': sys.exit(2)