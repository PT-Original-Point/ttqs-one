#!/usr/bin/env python3
from pathlib import Path

base=Path(__file__).resolve().parents[1]
p=base/'candidate'/'0083_R02_body.md'
text=p.read_text(encoding='utf-8-sig')
replacements={
"下列識別與 SHA-256 照錄 Blueprint R03。本次為文字候選，未持有原始二進位檔，重算欄一律標 PENDING；重算完成前，來源驗證狀態為 HOLD。":"下列來源已依分支 719ac6a9bec41a25092abd2509df977e02ecab88 的遠端 Git blob 重算六項；本地與遠端 SHA-256、位元組數一致。0083 的 Blueprint 與來源包尚待本候選同步，先記本地 SHA，遠端欄明示待同步。",
"| SRC-157 | quality-review/0077_R01/inputs/upstream_snapshots/03_157_CHECKBOX_BLUEPRINTS.md | 8c2bbe7ca9dcbb03088a48934b9e57e7147ede63 | ad03323d591cbea62814a8a59d233110587f2741bed8f944380b1faa2d04d216 | PENDING |":"| SRC-157 | quality-review/0077_R01/inputs/upstream_snapshots/03_157_CHECKBOX_BLUEPRINTS.md | 8c2bbe7ca9dcbb03088a48934b9e57e7147ede63 | ad03323d591cbea62814a8a59d233110587f2741bed8f944380b1faa2d04d216 | VERIFIED_REMOTE |",
"| SRC-P6 | quality-review/0078_R01/evidence/official_evidence_table_page6-6.png | － | b7bd4c09b7d7e22993a1577647e10a421fb240222b46b531ba3f01ee047fa1d1 | PENDING |":"| SRC-P6 | quality-review/0078_R01/evidence/official_evidence_table_page6-6.png | 7cce2401a3230cb86875df79396538d0adea41d5 | b7bd4c09b7d7e22993a1577647e10a421fb240222b46b531ba3f01ee047fa1d1 | VERIFIED_REMOTE |",
"| SRC-MIS | quality-review/0077_R01/inputs/upstream_snapshots/01_HUMAN_MISSION_AND_ACCEPTANCE.md | 538bedb9d87e8465f43151933b4a5c1bfa4bbc4e | 07c4b0beb30ebe9919818977d6eb0255e9f467955e9190e515ae3e2b963d1dd8 | PENDING |":"| SRC-MIS | quality-review/0077_R01/inputs/upstream_snapshots/01_HUMAN_MISSION_AND_ACCEPTANCE.md | 538bedb9d87e8465f43151933b4a5c1bfa4bbc4e | 07c4b0beb30ebe9919818977d6eb0255e9f467955e9190e515ae3e2b963d1dd8 | VERIFIED_REMOTE |",
"| SRC-GEN | quality-review/0077_R01/inputs/upstream_snapshots/02_GENRE_WRITING_MANUAL.md | 4ff863d9f534b6359fc1c7c1685bd8cce02da886 | 7fc23191efdb60ca4a9b48bc306799a9f15916b1160b63292d164bd4f4cf49aa | PENDING |":"| SRC-GEN | quality-review/0077_R01/inputs/upstream_snapshots/02_GENRE_WRITING_MANUAL.md | 4ff863d9f534b6359fc1c7c1685bd8cce02da886 | 7fc23191efdb60ca4a9b48bc306799a9f15916b1160b63292d164bd4f4cf49aa | VERIFIED_REMOTE |",
"| SRC-0082C | 0082 R08 候選 | － | 2a4b2aadf2a1ee9e1dce47247b91aa4bd150d83770fda1708bca0c722a07e20d | PENDING |":"| SRC-0082C | quality-review/0082_R01/candidate/0082_R08.docx | a113eaee53b18776e1dfc9665fc5a557b685a19a | 2a4b2aadf2a1ee9e1dce47247b91aa4bd150d83770fda1708bca0c722a07e20d | VERIFIED_REMOTE |",
"| SRC-0082B | 0082_R01/inputs/UNIQUE_BLUEPRINT_0082_R02.md | － | 451acd1e197b916f2d14c03bd2651653892a4a7955119291e9628bdc5e27e602 | PENDING |":"| SRC-0082B | quality-review/0082_R01/inputs/UNIQUE_BLUEPRINT_0082_R02.md | 3679bfa41ef88ca1792234049f49f0127a923ed5 | 451acd1e197b916f2d14c03bd2651653892a4a7955119291e9628bdc5e27e602 | VERIFIED_REMOTE |",
"| SRC-BR | work/ttqs-one-document-quality-contract-20261016／PR #92／head | 719ac6a9bec41a25092abd2509df977e02ecab88 | － | 不適用（head 非 SHA-256） |":"| SRC-083BP | quality-review/0083_R01/inputs/UNIQUE_BLUEPRINT_0083_R03.md | PENDING_UNTIL_SYNC | 21f76376621c5dd22d002a62202f41ea7335bbf872a965b0bbf8fb86955d0178 | VERIFIED_LOCAL_ONLY |\n| SRC-083PKT | quality-review/0083_R01/inputs/SOURCE_PACKET_0083_R01.md | PENDING_UNTIL_SYNC | 2c2f2947961abd93c0b36ce1269519e8db9c9e1c4e352d5f15aa71c5c5450783 | VERIFIED_LOCAL_ONLY |\n| SRC-BR | work/ttqs-one-document-quality-contract-20261016／PR #92／head at R02 draft | 719ac6a9bec41a25092abd2509df977e02ecab88 | － | VERIFIED_REMOTE_COMMIT_SNAPSHOT |",
"R02 body SHA-256 | PENDING（本文字候選尚未計算）":"R02 body SHA-256 | 由 exact-SHA 審查收據記錄；不在正文自我嵌入",
"DOCX SHA-256 | PENDING（尚無實際檔案）":"DOCX SHA-256 | 由建置收據記錄；不在正文自我嵌入",
"遠端推送 SHA | PENDING（尚無實際推送）":"遠端推送與讀回 | 由 GitHub 遠端讀回收據記錄",
"Appendix E 是本文件完整的 81 列 R-001 至 R-081 清冊，也是替換與 QA 的正式文字版本；sidecar CSV 應由 Blueprint 機械重建，不得以未附 CSV 取代本表。":"Appendix E 是本文件完整的 81 列 R-001 至 R-081 清冊，也是替換與 QA 的正式文字版本。配套 SYNTHETIC_REPLACEMENT_REGISTER_0083_R03.csv 由 Blueprint 機械重建，兩者須逐列一致；不得以未附 CSV 取代本表。",
}
for old,new in replacements.items():
    n=text.count(old)
    if n!=1: raise SystemExit(f"Expected one exact occurrence, got {n}: {old[:90]}")
    text=text.replace(old,new)
p.write_text(text,encoding='utf-8')
print('PATCHES_APPLIED',len(replacements))
