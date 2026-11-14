from __future__ import annotations
import csv, hashlib, io, json, subprocess
from pathlib import Path
from pypdf import PdfReader

REPO = Path(__file__).resolve().parents[5]
ROOT = REPO / "docs/ttqs-quality-20261016/quality-review/0076_R01"
INPUTS = ROOT / "inputs"
UPSTREAM = INPUTS / "upstream_snapshots"
HIST = INPUTS / "historical"
WORKER = ROOT / "worker"
CASE = "SYN-0073-2026-A01"
PRE = [45,50,60,55,50,65,40,55,60,45,70,50,55,65,45,60]
POST = [70,75,85,80,75,90,65,80,85,70,90,75,80,90,70,85]
PRACT = [(5,4,4,5),(4,4,3,4),(4,3,3,4),(4,4,4,4),(4,5,4,4),(5,5,4,5),(3,4,3,3),(5,4,4,5),(4,4,3,4),(4,3,3,4),(5,5,5,5),(4,4,3,4),(4,4,4,4),(4,5,4,4),(4,4,3,3),(3,3,3,3)]
KEYS = list("ACBDACBDCADBCADBACDB")
CONCEPTS = [
"先確認服務對象最急迫的問題與希望的協助","記錄敏感資訊前先說明目的並取得同意",
"以可核實事實描述，避免貼標籤或推測動機","只記錄完成服務與交接所需的最少資訊",
"超出志工角色權限的需求轉交有權責角色","錯誤更正保留理由與可追溯版本",
"對未核實安排不作承諾，說明回覆方式與期限","交接記錄事項、接手角色、下一步、期限與狀態",
"有立即安全風險時依既定程序優先升級","不同意敏感紀錄時記下拒絕狀態並提供替代方式",
"只由獲授權角色查閱必要服務紀錄","缺漏欄位退回核對，不猜測補值",
"交接取得接收角色確認並留下接手狀態","需求含糊時摘要並請對方確認",
"依核定保存期限與存取規則處理紀錄","超出角色範圍時清楚轉介並交代後續責任",
"使用錄音等敏感媒介前取得明確同意並依核定流程","說明可提供的服務範圍，不代表機構越權承諾",
"交接後確認責任人、期限與未結事項","錯誤紀錄可追溯更正，不刪痕跡或代簽"]

def git_bytes(p):
    return subprocess.run(["git","-C",str(REPO),"show","HEAD:"+p],check=True,capture_output=True).stdout
def blob(p):
    return subprocess.run(["git","-C",str(REPO),"rev-parse","HEAD:"+p],check=True,capture_output=True,text=True,encoding="utf-8").stdout.strip()
def putcsv(path, heads, rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8-sig",newline="") as f:
        w=csv.writer(f); w.writerow(heads); w.writerows(rows)

def main():
    for p in (INPUTS,UPSTREAM,HIST,WORKER,ROOT/"candidate",ROOT/"evidence",ROOT/"review"): p.mkdir(parents=True,exist_ok=True)
    pdfpath="docs/ttqs-quality-20261016/quality-review/0036_R13/inputs/official/TTQS_evidence_table_training_institution_source.pdf"
    mapath="docs/ttqs-quality-20261016/quality-review/0036_R13/inputs/mapping/checkbox_mapping_compact.json"
    pdf=git_bytes(pdfpath); (UPSTREAM/"official_evidence_table_source.pdf").write_bytes(pdf)
    oldpath="送審資料/04_全部文件與歷次版本/TTQS_ONE_CODEX_RUNTIME/22/2163_0076__指標17b_考試暨實作評量紀錄.docx"
    old=git_bytes(oldpath); (HIST/"2163_0076_legacy_candidate.docx").write_bytes(old)
    copied={}
    for name,src in {
        "0073_R08.docx":REPO/"docs/ttqs-quality-20261016/quality-review/0073_R01/candidate/0073_R08.docx",
        "0074_R01.docx":REPO/"docs/ttqs-quality-20261016/quality-review/0074_R01/candidate/0074_R01.docx",
        "0075_R02.docx":REPO/"docs/ttqs-quality-20261016/quality-review/0075_R01/candidate/0075_R02.docx",
    }.items():
        if not src.is_file(): raise FileNotFoundError(src)
        b=src.read_bytes(); (UPSTREAM/name).write_bytes(b)
        copied[name]={"sha256":hashlib.sha256(b).hexdigest(),"bytes":len(b),"source":str(src.relative_to(REPO))}
    correct_index={c:i for i,c in enumerate("ABCD")}
    rows=[]; counts=[0]*20
    for i,(pre,post,pr) in enumerate(zip(PRE,POST,PRACT),1):
        n=post//5; start=((i-1)*7+3)%20; correct={(start+j)%20 for j in range(n)}
        answers=[]
        for q in range(20):
            if q in correct: ans=KEYS[q]; counts[q]+=1
            else: ans="ABCD"[(correct_index[KEYS[q]]+1+((i+q)%3))%4]
            answers.append(ans)
        ptotal=sum(pr); wp=post>=70; pp=ptotal>=15
        rows.append([f"P{i:02d}",pre,post,n,post,*pr,ptotal,"PASS" if wp else "HOLD","PASS" if pp else "HOLD","PASS" if wp and pp else "HOLD",*answers])
    headers=["learner_code","pretest_total_from_0074_synthetic","posttest_total_from_0074_synthetic","correct_items","written_score_20x5","communication_0_5","privacy_boundary_0_5","record_accuracy_0_5","handoff_followup_0_5","practical_total_0_20","written_decision_sample_rule","practical_decision_sample_rule","overall_decision_sample_rule"]+[f"Q{i:02d}_response" for i in range(1,21)]
    putcsv(INPUTS/"SYNTHETIC_ASSESSMENT_DATA_0076_R01.csv",headers,rows)
    itemrows=[[f"Q{i:02d}",CONCEPTS[i-1],KEYS[i-1],counts[i-1],16,f"{counts[i-1]/16:.4f}","SAMPLE/SYNTHETIC; not validated psychometric evidence"] for i in range(1,21)]
    putcsv(INPUTS/"SYNTHETIC_ITEM_ANALYSIS_0076_R01.csv",["item_id","concept","answer_key_letter","correct_n","valid_n","facility_index","interpretation_limit"],itemrows)
    calc={"case_id":CASE,"course_title":"志工服務溝通與紀錄交接實務","sample_date":"2026-08-15","n":16,"pre_total":sum(PRE),"pre_mean":sum(PRE)/16,"post_total":sum(POST),"post_mean":sum(POST)/16,"mean_gain":(sum(POST)-sum(PRE))/16,"post_ge_80_n":sum(x>=80 for x in POST),"post_ge_80_rate":sum(x>=80 for x in POST)/16,"written_ge_70_n":sum(x>=70 for x in POST),"practical_sum":sum(sum(v) for v in PRACT),"practical_mean":sum(sum(v) for v in PRACT)/16,"practical_ge_15_n":sum(sum(v)>=15 for v in PRACT),"both_pass_n":sum(POST[i]>=70 and sum(PRACT[i])>=15 for i in range(16)),"item_correct_n":counts}
    (INPUTS/"SYNTHETIC_CALCULATION_CHECK_0076_R01.json").write_text(json.dumps(calc,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    mapping=json.loads(git_bytes(mapath)); linked=[x for x in mapping if x.get("deliverable_id") in {"0076","0077","0078","0079"}]
    if len(linked)!=4: raise ValueError("Mapping must include 0076-0079")
    blueprint=f"""# DOCX 0076 Unique Blueprint R01

Derived source snapshot only; not an official document or an acceptance decision.

## Exact mapping
- DOCX ID: 0076
- Unique requirement: I17B-E01
- Official checkbox serial: 084
- Indicator: 17b learning evaluation
- Document type: analysis_report; examination and practical assessment record
- Official evidence table: training institution version, page 6
- Source commit: e43dbf8da93b1738ecb30c591010d3ca123d2ab6
- 02_GENRE_WRITING_MANUAL.md Git blob: {blob("docs/ttqs-quality-20261016/02_GENRE_WRITING_MANUAL.md")}
- 03_157_CHECKBOX_BLUEPRINTS.md Git blob: {blob("docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md")}
- Compact mapping JSON Git blob: {blob(mapath)}
- Official PDF Git blob: {blob(pdfpath)}
- Official PDF SHA-256: {hashlib.sha256(pdf).hexdigest()}

## Official checkbox wording
考試紀錄、學員心得報告、照片與紀錄、訓後學員職涯規劃建議表。

## Four distinct functions required
| DOCX | requirement | unique function |
|---|---|---|
| 0076 | I17B-E01 | exam and practical assessment record |
| 0077 | I17B-E01 | learner reflection report |
| 0078 | I17B-E01 | real-photo and activity record index; never fabricate photos |
| 0079 | I17B-E01 | individual post-training career/learning guidance |
Checkbox 084 remains PARTIAL until all four functions and authentic source paths are addressed. 0076 cannot replace 0077-0079. Do not confuse these with adjacent checkbox 085 (course evaluation/recommendation review) or 086 (closeout/action-plan verification).

## Official 17b progression
0 not executed; 1 exam or practical assessment executed; 2 report/results and learning gaps analyzed into closeout and next-course planning; 3 improvement after a correction decision with concrete effects. This candidate is SAMPLE/SYNTHETIC only and claims no association execution, level, improvement, or effect.

## Same-case source constraints
- Case ID: SYN-0073-2026-A01 (synthetic only)
- Course: 志工服務溝通與紀錄交接實務
- Sample date: 2026-08-15; not a real class date
- P01-P16 are synthetic tokens. 0073 survey codes S01-S16 have no asserted P-to-S identity crosswalk.
- 0074 R01 pretest values: {','.join(map(str,PRE))}; total 870; mean 54.375.
- 0074 R01 posttest values: {','.join(map(str,POST))}; total 1265; mean 79.0625; 9/16 >=80 = 56.25%; mean gain 24.6875.
- 0073 R08 survey: issued 16, returned 16, valid 15, one invalid S16; Q5=54/15=3.60/5 and positive 8/15=53.33%. Survey denominator is distinct from test denominator.
- 0075 R02 proposes Option B only: +30 min guided practice, second handoff round, field-check card; PROPOSED/PENDING APPROVAL. No evidence it was executed or caused 0076 data.
- Historical 2163 DOCX SHA-256: {hashlib.sha256(old).hexdigest()}; old course/date/four-person synthetic sample conflicts with the current case and lacks complete keyed test form. Historical only, not accepted.
- Upstream local exact SHA: 0073 R08 {copied["0073_R08.docx"]["sha256"]}; 0074 R01 {copied["0074_R01.docx"]["sha256"]}; 0075 R02 {copied["0075_R02.docx"]["sha256"]}.

## Synthetic assessment rules only
20 multiple-choice items x 5 points. Fixed answer letters Q01-Q20: {','.join(KEYS)}. The response CSV is synthetic generated data that exactly reproduces the 0074 post-test totals; it is not an observed answer sheet.
Sample written threshold >=70/100 and practical threshold >=15/20 are not official or association policy. Practical criteria (0-5 each): communication/clarification, privacy/consent boundary, record accuracy, closed-loop handoff. A privacy, consent, safety, unauthorized promise, fabricated score, or traceability failure causes HOLD regardless of numerical score.
"""

    (INPUTS/"UNIQUE_BLUEPRINT_0076_R01.md").write_text(blueprint,encoding="utf-8")
    p_values="; ".join(f"P{i:02d} pre {PRE[i-1]} post {POST[i-1]} gain {POST[i-1]-PRE[i-1]} practical {'+'.join(map(str,PRACT[i-1]))}={sum(PRACT[i-1])}" for i in range(1,17))
    source=f"""# Source packet DOCX 0076 R01

All association evidence is REAL=UNKNOWN/HOLD. Candidate sources are not formal acceptance.

Official source: the attached official evidence-table PDF, page 6, says the 17b examples include exam records, learner reflections, photos/records, post-training career-planning suggestions, course evaluation review, and closeout follow-up. The official 17b levels are: 0 not executed; 1 exam or practical evaluation; 2 results/deficits analyzed and used in closeout/next planning; 3 concrete effects after a correction decision. Do not claim any level for this sample.

The current writing manual requires four different outputs for checkbox 084. This 0076 artifact is only the exam/practical component; 0077 reflections, 0078 real-photo/activity index, and 0079 individual guidance are separate. If any is absent or source evidence is not authentic, composite checkbox status stays PARTIAL/HOLD.

## Same-case candidates and known facts
- 0073 R08 exact local SHA {copied["0073_R08.docx"]["sha256"]}: synthetic course survey, issued 16, returned 16, valid 15, S16 excluded; Q5 54/15=3.60/5; positive 8/15=53.33%.
- 0074 R01 exact local SHA {copied["0074_R01.docx"]["sha256"]}: case SYN-0073-2026-A01, course 志工服務溝通與紀錄交接實務, sample date 2026-08-15, P01-P16 registration and pre/post totals.
- 0075 R02 exact SHA {copied["0075_R02.docx"]["sha256"]}: proposes +30 minutes guided practice, second group handoff round and field-check card, pending approval only.
- P01-P16 are synthetic sample codes; 0073 S01-S16 are survey-only tokens and no identity crosswalk is asserted.
- 0074 R01 says the practical check was not quantified in that version. This packet supplies a later synthetic demonstration, not proof of a historical or real practical exam.
- Historical candidate 2163 SHA {hashlib.sha256(old).hexdigest()} uses a different four-person equipment-operation course and 2026-08-11/12 dates. Do not reuse those facts.

## Source record values to preserve
0074 pre/post values in order: pre [{','.join(map(str,PRE))}], post [{','.join(map(str,POST))}].
{p_values}
Checks: pre sum 870/16=54.375; post sum 1265/16=79.0625; mean gain +24.6875; post >=80 is 9/16=56.25%. Synthetic practical total sum 253, mean 15.8125/20, >=15 is 11/16=68.75%. Both sample rules met 11/16=68.75%.
The 20-item response matrix is deterministically generated solely to reproduce posttest totals; not observed answers, not exam administration evidence, not validated item statistics.

## Operational sample task
A fictional volunteer-service inquiry asks about a scheduling conflict. Learner clarifies the need, protects consent/privacy, writes a factual minimum-necessary service note, and hands it over with next owner, next action, due event and status. No named person or real service recipient.
Use a 20-item x 5-point sample test and four practical criteria scored 0-5 each. Thresholds >=70/100 and >=15/20 are examples only, not approved policy. A privacy/consent/safety incident, unauthorized commitment, invented answer, or untraceable amendment triggers HOLD.

Historical candidate 2163 SHA-256: {hashlib.sha256(old).hexdigest()}.
"""

    (INPUTS/"SOURCE_PACKET_0076_R01.md").write_text(source,encoding="utf-8")
    concepts="\n".join(f"- Q{i:02d} key {KEYS[i-1]}: {CONCEPTS[i-1]}" for i in range(1,21))
    prompt=f"""# OpenCode v2 writer prompt DOCX 0076 R01

Use the attached Unique Blueprint, source packet, and synthetic CSVs to create a mature Traditional Chinese exam and practical assessment record. Identity is DOCX 0076 / I17B-E01 / checkbox 084 / indicator 17b. Do not confuse document ID and checkbox serial.

## Write exactly these two files
1. docs/ttqs-quality-20261016/quality-review/0076_R01/candidate/0076_R01_body.md
2. docs/ttqs-quality-20261016/quality-review/0076_R01/inputs/SYNTHETIC_REPLACEMENT_REGISTER_0076_R01.csv

Do not create a DOCX, render, receipt, report, commit, or GitHub change. Do not use Computer Use, browser/UI control, Antigravity, or another agent. Return paths, byte counts, section/table summary, and any source conflict.

## Source rules
- Use case SYN-0073-2026-A01, course 志工服務溝通與紀錄交接實務, sample date 2026-08-15, cohort P01-P16.
- Preserve 0074 pre/post totals exactly; the posttest item CSV is synthetic reconstruction for demonstration, not observed answers or proof an exam occurred.
- Link 0073 reaction evidence as distinct measurement: Q5 54/15=3.60 and positive 8/15=53.33%. Survey denominator is distinct from examination. 0073 S codes have no P-code identity crosswalk.
- 0075 Option B is proposed/pending only; never claim execution or causality.
- Do not reuse old 2163's different course, dates, or four-person data.
- Checkbox 084 requires four distinct outputs: 0076 assessment, 0077 reflections, 0078 real-photo/activity index, 0079 individual career guidance. State 0076 alone does not complete 084. Do not fabricate originals, photos, signatures, approval, credentials, or events.
- Keep 085 and 086 as separate neighboring requirements.

## Required sections
1. Specific title and immediate conclusion/status.
2. How a small volunteer association administrator, trainer, and evaluator use the record; prerequisites for REAL use.
3. Official source/page and exact 17b level sequence 0/1/2/3; no claim of association level.
4. Case and evidence chain 0073→0074→0075→0076 with facts, boundaries, and distinct 0077–79 functions.
5. 20-item full multiple choice test instrument: four plausible options, one unambiguous key, objective mapping, key, rationale. Use the answer-key letters exactly below.
6. Administration, versioning, eligibility, timing, scoring, missing/invalid rules, denominator, late/duplicate/illegible handling, regrade, privacy, retention, critical failure and hold.
7. Use every P01-P16 CSV row in full record; show responses in two readable tables Q01-Q10 and Q11-Q20, posttest total, and computed source-consistent results. Preserve 0074: pre total870/16=54.375; post1265/16=79.0625; mean gain24.6875; >=80 is9/16=56.25%.
8. Item analysis from supplied CSV: correct_n/16 and facility for all 20; synthetic only, not psychometric validation.
9. Full practical scenario, assessor instructions, four criteria and detailed 0-5 anchors, evidence notes, hold/critical fail rules, completed P01 sample.
10. Use every row for 16 practical records with four subscores, total /20, sample decision and concise synthetic observation; recompute sum253, mean15.8125, >=15=11/16=68.75%, both rules met=11/16.
11. Written/practical cross-tab, result decisions by sample ID; distinguish score from retention, behavior and outcomes.
12. Completed SAMPLE forms for exam record, practical score sheet, regrade/exception log, reconciliation and REAL replacement checklist. Any real unknown is explicitly REAL=UNKNOWN/HOLD with exact source to obtain.
13. Rejection/HOLD rules: missing official rule/version, incomplete denominator, missing raw response, mismatched total, critical privacy/safety event, unauthorized evaluator, consent gap, unapproved data linkage, uncontrolled amendment, missing siblings, or unverifiable real evidence.
14. Cross-document table with exact IDs, requirements, serials and distinct functions. Checkbox084 stays PARTIAL until 0077-79 and real evidence routes are handled.
15. Closing status: 0076 SAMPLE/SYNTHETIC candidate; formal acceptance NOT_GRANTED; real evidence UNKNOWN/HOLD.

## Fixed answer letters and item concepts
Write each question so the unique best option is exactly the specified letter:
{concepts}

## Output quality
- Human-facing Traditional Chinese, concise but usable. No engineering paths, hashes, model names, worker details, or internal receipt IDs in the document.
- Label all people/codes, dates, scores, responses, observations, thresholds and decisions SAMPLE/SYNTHETIC. REAL=UNKNOWN/HOLD.
- No empty forms as completed evidence; provide filled synthetic examples and separate replacement instructions.
- Split response matrix into two 10-item tables. Markdown tables must have consistent column counts, simple cells, no HTML/images/page breaks.
- Cross-check all numbers against both CSVs and calculation JSON.
- Replacement register must contain >=70 complete rows (excluding header), sequential unique IDs SYN-0076-FACT-0001 onward, with exact headers:
fact_id,case_id,document_locator,field_or_claim,synthetic_value_or_status,required_real_replacement,verification_role,hold_or_rejection_rule,source_link
- Each register row maps a concrete body fact/form/score/rule to authentic replacement evidence, verification role and hold rule; each row must state SAMPLE/SYNTHETIC; REAL=UNKNOWN/HOLD.
- Do not claim checkbox084 passed; 0077-79 remain distinct siblings.
"""
    (WORKER/"WRITE_PROMPT_0076_R01.md").write_text(prompt,encoding="utf-8")
    mapping=json.loads(git_bytes(mapath))
    siblings=[x for x in mapping if x.get("deliverable_id") in {"0076","0077","0078","0079"}]
    if len(siblings)!=4: raise ValueError("mapping rows 0076-0079 not found")
    receipt={"schema":"TTQS_ONE_0076_SOURCE_PACKET_R01.v1","source_commit":"e43dbf8da93b1738ecb30c591010d3ca123d2ab6","official_pdf_sha256":hashlib.sha256(pdf).hexdigest(),"legacy_2163_sha256":hashlib.sha256(old).hexdigest(),"upstream_snapshots":copied,"pre_sum":sum(PRE),"post_sum":sum(POST),"practical_sum":sum(sum(v) for v in PRACT),"item_correct_n":counts,"real_status":"UNKNOWN/HOLD","candidate_status":"NOT_BUILT"}
    (INPUTS/"SOURCE_PACKET_RECEIPT_0076_R01.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"root":str(ROOT),"source_receipt":receipt,"data_rows":len(rows)},ensure_ascii=False))

if __name__=="__main__":
    main()
