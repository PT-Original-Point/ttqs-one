# 0137 R03 front-matter version label correction

work_id: TTQS_ONE_0137_R03_VERSION_LABEL_FIX_20261108
role: bounded Writer correction; one exact front-matter cell only

Input DOCX: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0137_I19-E27_CANDIDATE_R03_20261108\candidate\0137_I19-E27_媒體採訪與正面報導原件查驗表_R03.docx
Input SHA-256: 66577936e66ab74d94831f36028577c68f88d008219aa882b069b5dd1513dc7d
Output DOCX: same path, overwrite only after the input is fully read; this is the sole active writer for this candidate.

Authorized exact change: in python-docx tables[0], row 2, cell 1 (zero-based), replace only the leading `R02` with `R03` in the exact cell text `R02；候選文件，不是協會正式核定或 TTQS 評分`. Preserve the remainder, all other paragraphs and tables, styles, layout, SAMPLE/SYNTHETIC facts, and the replacement register. Make no other edits.

Create a new receipt at `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\OPEN_CODE_REPAIR_0137_R03_VERSION_LABEL_20261108\label_fix_writer_receipt.json` recording input/output SHA-256, exact cell locator, old/new text, changed-cell count=1, no other content changes, and success/failure. Do not overwrite the earlier worker receipt or QA records.
