TTQS ONE R03 外包撰稿工作包
work_id=TTQS-0004-I01-E02-WRITER-R03-20261116
doc_id=0004
requirement=I01-E02
project_crosswalk_serial=002 (not official PDF number)
role=TEXT_ONLY_WRITER
requested_route=opencode/beam-free
source_packet_sha256=4535ac0b8275297ff60dabd7b4f7ada77bd8bd240b7200a6532ea32eec9aad0b
unique_blueprint_sha256=cdfaff45068df2c71bb582908c970ad67cd1a8a7ab973a8efd747cce66c4e375c
synthetic_register_plan_sha256=0e0748a80d512c9e49abea3c567838239db21510408570d84f0ecfdb7e10d0c9
corrected_source_prep_manifest_sha256=379dce4afd2a2701961804e48dc2c01925601f2990d3c79a8df6f2a99464befd
corrected_source_prep_qa_sha256=98af4a3262230eed0b89f7d3e11a63286328f6e255ffcb8b03df2e59b62ab41e
source_prep_qa_status=PASS_SOURCE_PREP_CANDIDATE_NOT_DOCX; 44/44 checks; zero failures
validator correction: two shared reference fields intentionally have distinct types (shared SAMPLE reference for date; shared SAMPLE reference code for anonymous response code); both are scope=shared_reference, status=SHARED_SAMPLE_REFERENCE_NOT_ACCEPTANCE; they are not independent acceptance or questionnaire answers. The old R02 work id inside source material is historical metadata and is superseded by this R03 assignment.

Task:
Write the complete, evaluator-usable Traditional Chinese document body in Markdown for 《目標市場調查執行與樣本紀錄》. This is a completed SAMPLE/SYNTHETIC worked example and workflow proposal, not an empty form or outline. Follow the attached official source packet, requirement, and Unique Blueprint. Use the corrected source QA and manifest as controlling validation for shared reference fields.

Required mechanics:
- clear opening explaining purpose, scope, and what reviewer should verify;
- target population and inclusion/exclusion, sampling frame and limits, all SAMPLE;
- sequential execution procedure with exception handling for ineligible, refusal, no response, incomplete/invalid return, duplicate, withdrawal, correction;
- fully populated synthetic invitation/event log;
- separate valid and invalid unique-return records, with reason and traceability;
- batch flow reconciliation and exact equations;
- response 2/4=50.0%; valid/unique-return efficiency 1/2=50.0%; valid yield 1/4=25.0%; eligibility pass 4/5=80.0%; one-decimal arithmetic and N/A rule for zero denominators;
- privacy and data-quality handling; actual association retention/authority/execution must remain UNKNOWN absent evidence;
- role separation labelled SAMPLE roles only;
- 0005 handoff limited to counts, valid anonymous reference, limitations; do not perform demand analysis;
- explicit accept/reject/HOLD/rework decisions and a REAL replacement checklist.

Use only the exact case facts and numbers in the attached register and source packet:
screened 5; ineligible 1; eligible invitations 4; unique returns 2 (one valid and one incomplete/invalid); refusal 1; no response 1; raw receipt events 3 including one duplicate extra.
Rates: response 2/4=50.0%; valid/unique-return efficiency 1/2=50.0%; valid-yield 1/4=25.0%; eligibility pass 4/5=80.0%. Reconcile all totals and equations. Attach the relevant synthetic fact IDs to every displayed synthetic date, code, status, count, rate and decision; IDs must match the attached register. Do not invent additional case facts, real names/contact data, real association execution, approvals, policy, representativeness, or results.

Genre boundaries:
0003 owns survey questions/options/scales/individual answers; do not reproduce them. 0004 owns execution/sample-flow records and process-quality rates. Do not analyze demand, compute per-question averages/ranks, infer representativeness, or recommend opening a course (0005 owns demand analysis). The serial 002 is a project crosswalk serial, not official PDF numbering.

Every procedure proposed here must be labelled as a SAMPLE workflow proposal pending authorized adoption. All worked-example content must be clearly SAMPLE/SYNTHETIC and the artifact status CANDIDATE. For unsupported REAL facts, write UNKNOWN and name the exact source needed and HOLD action. No fabricated third-party originals, signature, certificate, approval, or achievement. No empty sections, TODOs, unresolved placeholders, self-review, or PASS claims. Return ONLY the complete Markdown document body, with no preface or commentary.

Free text only: no tools, file writes, shell, browser, Computer Use, image, or external lookups. Stop after one complete body; never mutate repo or files.
