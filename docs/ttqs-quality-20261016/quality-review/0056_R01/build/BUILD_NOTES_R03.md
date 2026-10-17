# BUILD_NOTES_R03 — DOCX 0056

Build-only record. This is NOT semantic acceptance, NOT an independent review,
and NOT a statement of real-world compliance.

## Output files
- `0056_R03.docx` (task-directory root) — human-facing Traditional-Chinese package.
- `build/build_0056_R03.py` — deterministic builder (copied from R02 builder; layout/pagination edits).
- `build/BUILD_NOTES_R03.md` — this file.

## R01/R02 history preserved (not overwritten)
- `0056_R01.docx`; `build/build_0056_R01.py`; `build/BUILD_NOTES_R01.md`;
  `evidence/render_R01/0056_R01.pdf` + page-01..14.png; `evidence/history/R01_pre_layout_repair/`.
- `0056_R02.docx`; `build/build_0056_R02.py`; `build/BUILD_NOTES_R02.md`;
  `evidence/visual_review_R02.json`.

## R03 repairs (from evidence/visual_review_R02.json)
- (a) Status-dictionary tail page: the state-code column was widened so every code fits on
  one line, and the dictionary table uses explicit tight cell margins (tblCellMar). This
  removes the two-row tail page without lowering the >=9.5 pt font floor.
- (b) T5 tail page: T5 now keeps all its rows together (keep-with-next on every row except
  the last) so the complete table sits on one landscape page, and it was reduced to a single
  empty operational row (one is sufficient). No single-record tail page remains.
- (c) Hidden characters: U+200B is removed entirely. Underscore-boundary wrapping is now done
  with an explicit display line break (<w:br/>) inserted ONLY at '_' boundaries and only when
  a code token is wider than its column; the token text stays byte-exact. Code columns in the
  wide annex tables were widened where needed so no break falls between arbitrary letters.
- Retained: <w:cantSplit/> on all rows, header-row keep-with-next, repeating header rows.
- Unchanged: sample facts, decision logic, official mapping (or-semantics), schemas, formula,
  evidence boundaries, all T1-T9 columns and values.

## Source provenance (computed only for the two attached inputs)
- Packet   `inputs/0056_SOURCE_PACKET_R01.md`  SHA-256 `a85366f223c16a038832dbb8caf2f454a575ed0d9ae8fc943555ee939052c1c3`
- Blueprint `0056_UNIQUE_BLUEPRINT_R01.md`       SHA-256 `b3a66a78dac86dfe56f1c3747e044038ed675f13a4400cdd2417bbb255d80c35`
- Output   `0056_R03.docx`                       SHA-256 `1960c37ee335d0af4872d2c41100a26c3f0c38a4475ec2e185993708c3028f3d`

Internal identity kept OUT of the human body (sidecar-only):
- deliverable id 0056; official indicator I12-E04; official checkbox sequence 059;
  official PDF sha 805386b7…; page-4 image sha 0e00b465…; contract/genre/mission blobs.

## Document structure
Portrait narrative + a landscape annex for wide forms. Sections:
一 30 秒用途｜二 使用時機｜三 提案角色｜四 名詞與狀態對照｜五 官方「或」語意｜
六 決策樹｜七 狀態字典｜八 作業表單 T1–T5（landscape）｜九 決策軌跡 T6｜
十 合成示範 SYN-0056-SAFE-01｜十一 合成替換登錄 T9｜十二 完整度摘要｜
十三 未寄出索取範本｜十四 替換路徑與來源驗證｜十五 例外/到期/檢索/存取/更正/版本 T7,T8｜
十六 HOLD/退件條件｜十七 跨文件邊界與負向鄰居｜十八 審查者自我測試｜十九 來源定位。

## Tables (schema per Blueprint F)
- T1 適用性判定表 (13 cols)
- T2 資產／場域義務矩陣 (14 cols)
- T3 設備檢查與更正複核表 (15 cols)
- T4 場地保險正本索取／索引／驗證表 (16 cols)
- T5 證據狀態與到期追蹤表 (11 cols)
- T6 決策軌跡表 (8 cols)
- T7 例外／事件與矯正表 (9 cols)
- T8 版本軌跡表 (5 cols)
- T9 合成替換登錄表 (5 cols)
- plus: 文件識別, 提案角色, 名詞與狀態對照, 狀態字典, 跨文件邊界.

## Layout
- A4; portrait by default; landscape only for the 14–16 column annex (T1–T5) to avoid clipping.
- Body >= 10.5 pt; table cells >= 9.5 pt; repeating header rows on every table.
- Rows use cantSplit (no row splits across pages); header row kept with first data row;
  T5 additionally keeps all rows together on one landscape page.
- Long codes break only at '_' boundaries via explicit <w:br/> (no hidden characters).
- T1–T5 are the wide annex tables (landscape); other tables are portrait.
- Header (title) and footer (PAGE / NUMPAGES) on every section; Microsoft JhengHei.

## Synthetic-data boundary
- Worked case id: `SYN-0056-SAFE-01` (SAMPLE/SYNTHETIC; unrelated to any real course).
- All sample facts are tagged (SAMPLE) in-table and registered row-by-row in T9 (SF-01..SF-19).
- Damaged cable is a synthetic illustration only; no inspection is implied to have happened.
- Insurance request is a template, status `REQUEST_DRAFTED_NOT_SENT`, no policy attached;
  insurance type/coverage/insurer/policy number stay UNKNOWN (type is asked of the source;
  no specific line such as public liability is presumed).
- Roles are `PROPOSED`; every real-world fact absent from the packet stays
  `UNKNOWN / PENDING_REAL_SOURCE`.

## Known limitations
- No real inspection certificate, policy, issuer, policy number, coverage, limit, site,
  person, signature, sent request or approval exists in the source packet; none is invented.
- Completeness is `0 ÷ 2 = 0%` for the sample only; it is NOT a TTQS score and NOT policy.
- Result is `HOLD / PENDING_REAL_SOURCE`; `PASS` is deliberately not used.
- DOCX opens/parses with python-docx; visual pagination was not rendered here.

## Determinism
- No wall-clock values; fixed core properties (2026-10-17); zip entries rewritten with a
  fixed timestamp, so repeated runs produce identical bytes for identical inputs.

## Build self-check (content-level, not semantic acceptance)
- tables>=12                         OK tables=17
- table T1                           OK 
- table T2                           OK 
- table T3                           OK 
- table T4                           OK 
- table T5                           OK 
- table T6                           OK 
- table T7                           OK 
- table T8                           OK 
- table T9                           OK 
- official quote                     OK 
- case id                            OK 
- no SYN-0033 link                   OK 
- 0 / 2 = 0%                         OK 
- unsent request                     OK 
- PENDING_REAL_SOURCE                OK 
- HOLD present                       OK 
- T9 header                          OK 
- T9 has SF-01..SF-19                OK 
- two obligations                    OK 
- no public-liability presum         OK 
- no forbidden fill words            OK 
- no internal hash/path              OK 
- codes preserved (norm)             OK 
- no U+200B hidden char              OK zwsp=0
- breaks exist and only after '_'    OK br=25
- cantSplit on all rows              OK 
- repeated header rows               OK 
- header kept with data              OK 
- T5 kept together                   OK rows=4
- T5 one empty row                   OK empty=1 blank=0
- max code segment<=14               OK max=13
- no run < 9.5pt                     OK min=9.50
- body runs >= 10.5pt                OK min=10.50

## Truthful build result
- BUILD: completed; DOCX written and re-opened successfully.
- REVIEW: not performed here (an independent reviewer judges quality separately).
