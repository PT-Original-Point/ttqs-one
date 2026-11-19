from pathlib import Path
from docx import Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.text.paragraph import Paragraph
from docx.table import Table
import csv,hashlib,json

REPO=Path(r"E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016")
ROOT=REPO/"docs/ttqs-quality-20261016/quality-review/0038_R03"
DOC=ROOT/"candidate/0038_R03.docx"
BLUEPRINT=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\BLUEPRINT_CURRENT.jsonl")
DOC_SHA=hashlib.sha256(DOC.read_bytes()).hexdigest()
PDF_SHA=hashlib.sha256((ROOT/"evidence/render_final/0038_R03.pdf").read_bytes()).hexdigest()
SPEC_HEAD="639b9eacce93f84f49ee20714f1bad337c6a961e"
SPEC_BRANCH="work/ttqs-one-document-quality-contract-20261016"
SPEC_BLOBS={"01":"538bedb9d87e8465f43151933b4a5c1bfa4bbc4e","02":"4ff863d9f534b6359fc1c7c1685bd8cce02da886","03":"8c2bbe7ca9dcbb03088a48934b9e57e7147ede63","04":"62e3dd7dfd8579b6bc97952ffa6236e7494f3b4d","05":"60ae010c58140e1710ed24016085c6dfaf6ffaee","06":"70449889fd464106fe204496004bee13018d4a51"}
rows=[json.loads(x) for x in BLUEPRINT.read_text(encoding="utf-8").splitlines() if x.strip()]
byid={x["deliverable_id"]:x for x in rows}
for id in ("0037","0038","0039"):
 if id not in byid:raise SystemExit("Missing current Blueprint row "+id)
(ROOT/"inputs/BLUEPRINT_NEIGHBORS_0037_0039.jsonl").write_text("\n".join(json.dumps(byid[x],ensure_ascii=False,separators=(",",":")) for x in ("0037","0039"))+"\n",encoding="utf-8")

source_map=f'''# 0038 R03 source map and lineage

- Project/doc: TTQS_ONE / DOCX 0038.
- Formal requirement mapping: Unique Blueprint `deliverable_id=0038`, `requirement_id=I08-E02`; official checkbox sequence **039**. DOCX 0039 is a different deliverable (`I08-E03`) and is only a negative neighbor here.
- Official requirement: 針對訓練方案的系統設計能適時檢討及改善，執行後有良好效果。
- Official source: 勞動力發展署《TTQS 查核佐證文件資料表—訓練機構版》，I08 p.2; p.3 is adjacent continuation context. Official PDF SHA-256: `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`. Page images are `official-2.png` and `official-3.png`.
- Unique Blueprint current file SHA-256: `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`; exact 0038 raw row SHA-256: `2504485c1698a5c83ac2205938c05b532edc8d697f2441ad1d6a0c324897b73e`.
- Current spec branch/head used for R03: `{SPEC_BRANCH}` / `{SPEC_HEAD}`. Spec blob IDs:
'''+"".join(f"  - `{k}` `{v}`\n" for k,v in SPEC_BLOBS.items())+f'''- Current complete 0038 row: `BLUEPRINT_CURRENT_0038.jsonl`. Neighbor rows: `BLUEPRINT_NEIGHBORS_0037_0039.jsonl`.
- Negative neighbors: 0037/I08-E01 concerns cross-period review of system design changes; 0039/I08-E03 concerns a course-planning/design-review meeting. This sample is a separate case and does not claim to represent either neighbor.
- Candidate lineage: R03 was made from exact R02 SHA `bdb6ef07c1aacd31f638cdad511012777d2f1b9d2c9f5f307252dd62de0170a4` by raising only 20 nonempty top-level body runs below the 10.5 pt Blueprint floor to 10.5 pt. All paragraph and table text remains identical; see `evidence/build/patch_receipt_R03.json`.
- R03 candidate DOCX SHA-256: `{DOC_SHA}`. Rendered PDF SHA-256: `{PDF_SHA}`.
- R02 semantic report is historical evidence for the R02 SHA only. It is not an R03 exact-SHA review. A new independent review of R03 is pending.
- No REAL association execution, approval, participant, measurement, or outcome has been authenticated. Dates, roles, course details, options, participant codes, scores, and decisions are SAMPLE/SYNTHETIC.
'''
(ROOT/"inputs/SOURCE_MAP.md").write_text(source_map,encoding="utf-8")

visual={"project_id":"TTQS_ONE","doc_id":"0038","requirement_id":"I08-E02","official_checkbox_sequence":"039","candidate":"0038_R03","candidate_sha256":DOC_SHA,"pdf_sha256":PDF_SHA,"page_count":14,"renderer":"Codex documents skill render_docx.py using project-controlled renderer recovery LibreOffice; Poppler rasterization","scope":"Direct visual inspection of all 14 latest R03 page PNGs at original resolution","status":"PASS","pages":[
{"page":1,"status":"PASS","observation":"封面、官方對應、完整示範結論、SAMPLE界線及使用方式清晰；正文行距、頁尾和留白正常。"},
{"page":2,"status":"PASS","observation":"官方要求對照、0037/0039負向鄰項與六步專屬流程圖完整，流程框及箭頭清晰。"},
{"page":3,"status":"PASS","observation":"設計假設、三方案加權比較及缺口到可驗證結果表完整，無溢出。"},
{"page":4,"status":"PASS","observation":"120分鐘課程安排與目標、活動、評量對應表格可讀，未拆壞。"},
{"page":5,"status":"PASS","observation":"D1-D4量尺、等難度情境、缺漏重複與保存控制完整，表格列項可讀。"},
{"page":6,"status":"PASS","observation":"樣本框、納排條件、日期渠道及流向分母呈現完整；有效率與N/A限制可讀。"},
{"page":7,"status":"PASS","observation":"A組12列分數、逐列判定及小計均完整，底部說明未裁切。"},
{"page":8,"status":"PASS","observation":"B組12列、B08未達標及異常覆核表完整，數據和文字可讀。"},
{"page":9,"status":"PASS","observation":"彙總表、比較圖、差異計算、因果限制及退件條件完整，圖表標籤可讀。"},
{"page":10,"status":"PASS","observation":"後續處理、REAL替換清單、官方來源索引及版本收據清楚，表格無截斷。"},
{"page":11,"status":"PASS","observation":"候選狀態及一次執行六階段角色與控制表完整，未產生不必要分頁。"},
{"page":12,"status":"PASS","observation":"附表A表頭及A01-A12、B01-B02逐筆追溯欄位清晰，表格完整。"},
{"page":13,"status":"PASS","observation":"附表A續頁表頭重複，B03-B12及狀態定義完整，行列無裁切。"},
{"page":14,"status":"PASS","observation":"附表B四個官方問題與欄位、SAMPLE/REAL來源、限制及覆核位置完整可讀。"}],"systematic_defects":[],"formal_acceptance":"NOT_GRANTED"}
(ROOT/"evidence/qa/visual_qa_R03.json").write_text(json.dumps(visual,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

# Extract Word body paragraphs and tables in document order for the independent exact-SHA review.
doc=Document(DOC);parts=[]
for child in doc.element.body.iterchildren():
 if isinstance(child,CT_P):
  text=Paragraph(child,doc).text.strip()
  if text:parts.append(text)
 elif isinstance(child,CT_Tbl):
  t=Table(child,doc); lines=[]
  for row in t.rows:
   lines.append(" | ".join(c.text.replace("\n"," / ").strip() for c in row.cells))
  parts.append("\n".join(lines))
text="\n\n".join(parts)
(ROOT/"review").mkdir(exist_ok=True)
(ROOT/"review/0038_R03_full_text_exact_sha.md").write_text(f"# DOCX text extraction for independent review\n\n- Candidate SHA-256: `{DOC_SHA}`\n- Extraction: python-docx in OOXML body order; paragraphs and table rows preserved.\n- This text accompanies, and is bound to, the candidate DOCX; reviewer must independently hash/open DOCX.\n\n---\n\n{text}\n",encoding="utf-8")

packet=f'''# Independent semantic review request — TTQS ONE 0038 R03

Review this candidate independently from its builder. Do not trust prior PASS statements. Read the exact candidate DOCX, the full ordered text extraction, current Unique Blueprint row, official source page images, current spec/source map, neighbor rows, synthetic replacement register, R02 historical review, and all R03 render pages if your tools permit.

## Exact identity
- DOCX: `{DOC_SHA}` (verify SHA-256 yourself before analysis)
- PDF render: `{PDF_SHA}`
- Project/doc/requirement/official sequence: TTQS_ONE / 0038 / I08-E02 / 039
- Current controlling spec commit: `{SPEC_HEAD}`
- Correct neighbors: 0037=I08-E01 and DOCX 0039=I08-E03. Do not confuse DOCX ID and checkbox sequence.

## Files
- Candidate: `candidate/0038_R03.docx`
- Ordered text: `review/0038_R03_full_text_exact_sha.md`
- Blueprint: `inputs/BLUEPRINT_CURRENT_0038.jsonl`
- Neighbors: `inputs/BLUEPRINT_NEIGHBORS_0037_0039.jsonl`
- Official source screenshots: `inputs/official-2.png`, `inputs/official-3.png`
- Replacement register: `evidence/SYNTHETIC_REPLACEMENT_REGISTER.csv`
- Rendered PDF and all 14 page images: `evidence/render_final/`
- Source map: `inputs/SOURCE_MAP.md`
- R02 previous semantic report: `../0038_R02/evidence/qa/independent_semantic_review_R02.md` (context only; exact SHA is R02, not this candidate)

## Required independent checks
1. Exact official wording and Unique Blueprint mapping; distinguish doc_id 0038 from official checkbox sequence 039 and from DOCX 0039/I08-E03.
2. Correct genre and title-blind specificity; distinguish I08-E01 multi-period review and I08-E03 planning meeting.
3. Mature operational usefulness to a small volunteer training association. Check that the document actually records design deficiency, alternative comparison, specific revision, implementation sample, result analysis, limitations, follow-up, and return conditions.
4. Review the 24-row A/B worked example, denominators, threshold, rates, mean gains, weighted option scores, B08 exception, and no causal overclaim.
5. Verify SAMPLE/SYNTHETIC versus REAL, association approval/execution, third-party and authority boundaries; no fabricated original evidence.
6. Exact link between each synthetic case row and the replacement register, the source/decision/review crosswalk, and candidate citations.
7. Review the text and pages with the title hidden. Do not treat a builder's technical QA as semantic acceptance.
8. Provide PASS / PARTIAL / FAIL. Every finding must cite section/page or exact wording. Explicitly distinguish semantic review from pixel inspection; if you cannot inspect pixels, say so. State blockers and any content defect requiring correction.

Return a concise but substantive report with candidate SHA, PDF SHA if verified, criterion-by-criterion verdict, findings with locations, and final verdict. Do not change any file. A PASS means the R03 content is semantically acceptable as a SAMPLE/CANDIDATE only; it does not grant association acceptance or formal promotion.
'''
(ROOT/"review/review_request_R03.md").write_text(packet,encoding="utf-8")

README=f'''# TTQS ONE 0038 R03 candidate package

- Document: **0038 — I08-E02 — official checkbox sequence 039**.
- Status: **CANDIDATE**; technical checks PASS; direct visual inspection of all 14 pages PASS; independent R03 semantic review pending; formal association acceptance NOT GRANTED.
- Candidate DOCX SHA-256: `{DOC_SHA}`.
- PDF SHA-256: `{PDF_SHA}`.
- R02 exact candidate SHA: `bdb6ef07c1aacd31f638cdad511012777d2f1b9d2c9f5f307252dd62de0170a4`.
- R03 fixes the only proven R02 technical defect: 20 body runs below 10.5 pt were raised to the Blueprint minimum. Paragraph and table text are identical between R02 and R03. The R02 semantic review remains bound to R02; it is not the R03 review.
- The 24 case-level A/B scores, all calculations, 37-row replacement register, source/decision crosswalk, and embedded diagrams are retained. Every case/date/role/course/score/decision is SAMPLE/SYNTHETIC, not authenticated association evidence.
- Rendered with the documents skill `render_docx.py`; all 14 current page images were directly inspected. Page images and PDF are QA evidence, not proof of Human acceptance.
- Controlling source map, Blueprint row, official requirement images, review packet, verification script, and exact-SHA receipts are included in this folder.

## Use boundary

This is a complete instructional example for a training-association administrator to understand and operate the review/improvement record. It does not claim original-point association execution, participant consent, approval, signature, real course delivery, or measured results. Before REAL use, replace every synthetic fact with a traceable lawful source and authorized reviewer. The file has not been formally accepted or promoted.
'''
(ROOT/"README.md").write_text(README,encoding="utf-8")

progress={"project_id":"TTQS_ONE","doc_id":"0038","requirement_id":"I08-E02","official_checkbox_sequence":"039","candidate":"0038_R03","candidate_sha256":DOC_SHA,"status":"CANDIDATE; technical=PASS; visual=PASS_ALL_14; independent_semantic_review=PENDING; formal_acceptance=NOT_GRANTED","source_spec_branch":SPEC_BRANCH,"source_spec_head":SPEC_HEAD,"blueprint_file_sha256":"406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e","blueprint_row_sha256":"2504485c1698a5c83ac2205938c05b532edc8d697f2441ad1d6a0c324897b73e","official_pdf_sha256":"805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709","pdf_sha256":PDF_SHA,"visual_pages_reviewed":14,"sample_case_id":"SYN-I08E02-2026-01","sample_boundary":"All dates, roles, course facts, options, participant codes, scores, calculations and decisions are SYNTHETIC.","change_from_R02":{"sha256":"bdb6ef07c1aacd31f638cdad511012777d2f1b9d2c9f5f307252dd62de0170a4","reason":"Raised 20 below-floor body runs from 9.5/10.0 pt to 10.5 pt; verified all paragraph/table text unchanged."},"next_action":"Fresh independent exact-SHA semantic review via OpenCode CLI v2; then final QA receipt, manifest, GitHub push, remote byte readback.","formal_acceptance":"NOT_GRANTED"}
(ROOT/"PROGRESS.json").write_text(json.dumps(progress,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"docx_sha256":DOC_SHA,"pdf_sha256":PDF_SHA,"review_packet_chars":len(packet),"candidate_text_chars":len(text),"pages":len(visual["pages"]),"files":["README.md","PROGRESS.json","inputs/SOURCE_MAP.md","inputs/BLUEPRINT_NEIGHBORS_0037_0039.jsonl","evidence/qa/visual_qa_R03.json","review/0038_R03_full_text_exact_sha.md","review/review_request_R03.md"]},ensure_ascii=False,indent=2))
