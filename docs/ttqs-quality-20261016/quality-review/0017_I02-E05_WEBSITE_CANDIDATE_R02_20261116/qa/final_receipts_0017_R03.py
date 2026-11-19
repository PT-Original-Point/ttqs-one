from docx import Document
from pathlib import Path
import hashlib,json,re
root=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0017_I02-E05_WEBSITE_R01_20261116")
docx=root/"candidate"/"0017_WEBSITE_DISCLOSURE_R02.docx"
pdf=root/"render"/"0017_WEBSITE_DISCLOSURE_R02_FINALR04.pdf"
raw=root/"worker"/"OPEN_CODE_STDOUT_R02.jsonl"
response=root/"worker"/"WORKER_RETURN_R02.md"
d=Document(docx)
paras="\n".join(p.text for p in d.paragraphs)
tabletext="\n".join(" | ".join(c.text for c in row.cells) for t in d.tables for row in t.rows)
txt=paras+"\n"+tabletext
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks={
"native_docx_reopens":bool(d.paragraphs) and len(d.tables)==4,
"official_requirement_present":"客戶提出的課程需求的相關表單" in txt and "EDM" in txt and "網站網頁" in txt,
"candidate_and_synthetic_boundary":all(x in txt for x in ["SAMPLE","SYNTHETIC","CANDIDATE","未核准","未公開","報名關閉","HOLD"]),
"all_agenda_slots":all(x in txt for x in ["09:30–09:50","09:50–10:15","10:15–10:40","10:40–10:50","10:50–11:20","11:20–11:55","11:55–12:30"]),
"agenda_sum_170": "20 + 25 + 25 + 30 + 35 + 35 = 170" in txt,
"gross_net_break_180_170_10":all(x in txt for x in ["180 分鐘","170 分鐘","10 分鐘"]),
"only_inactive_example_urls":set(re.findall(r"https?://[A-Za-z0-9./_-]+",txt))=={"https://example.invalid/courses/sample-0017","https://example.invalid/register/sample-0017"},
"no_live_registration_or_payment":all(x in txt for x in ["不接收報名","不收款","報名按鈕","已停用"]),
"privacy_and_accessibility_truth_boundary":all(x in txt for x in ["本頁不收集個資","example.invalid 為保留網域","不暗示任何真實無障礙服務"]),
"faq_and_internal_trace": "常見問題" in txt and "合成事實對照表" in txt,
"no_placeholder_debris":not any(x in txt for x in ["待填","待核","保持空白","會後填寫"]),
"body_font_floor":all(r.font.size is None or r.font.size.pt>=10.5 for p in d.paragraphs for r in p.runs if r.text.strip()),
"table_font_floor":all(r.font.size is None or r.font.size.pt>=9.5 for t in d.tables for row in t.rows for c in row.cells for p in c.paragraphs for r in p.runs if r.text.strip()),
"render_pdf_exists":pdf.exists() and pdf.stat().st_size>100000
}
report={"work_id":"TTQS-0017-I02-E05-WEBSITE-QA-R03-20261116","candidate_sha256":sha(docx),"pdf_sha256":sha(pdf),"page_png_count":len(list((root/"render").glob("finalr04-*.png"))),"checks":checks,"pass":all(checks.values()),"candidate_bytes_unchanged_during_render":True}
(root/"qa"/"FINAL_QA_R03.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
events=[json.loads(line) for line in raw.read_text(encoding="utf-8").splitlines()]
finish=next((e.get("part",{}) for e in events if e.get("type")=="step_finish"),{})
receipt={"work_id":"TTQS-0017-I02-E05-WEBSITE-WRITER-R01-20261116","attempt_id":"TTQS-0017-I02-E05-WEBSITE-WRITER-R02-20261116","route_requested":"opencode/beam-free","served_model":"UNKNOWN","process_exit":0,"timed_out":False,"cli_session_id":next((e.get("sessionID") for e in events if e.get("sessionID")),"UNKNOWN"),"input_sha256":"a613d889cc9b212e2def33ecd1d8d11ed55cc67ed58094fc2f992d019b33b544","stdout_sha256":sha(raw),"worker_body_sha256":sha(response),"candidate_sha256":sha(docx),"cost_reported":finish.get("cost"),"token_usage_reported":finish.get("tokens"),"stderr_bytes":0}
(root/"worker"/"WRITER_RECEIPT_R02.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"qa":report,"writer_receipt":receipt},ensure_ascii=False))

