# Independent semantic review packet — 0113 / I18-E22 final R01
- Candidate filename: 0113_I18-E22_會員人數年度變化追蹤分析表_R01.docx
- Candidate exact SHA-256: `5f6d86a11ff884f7d0f1c251bf9b0dd4aa10b41defc68e2d1ea51b1afb329821`
- Candidate bytes: 82863
- Document ID: 0113; official requirement: I18-E22; official printed checkbox serial: UNKNOWN_NOT_ASSERTED. Do not confuse with 157 index 123.
- State: SAMPLE/SYNTHETIC ONLY; not association REAL evidence; formal acceptance NOT_GRANTED.
## Source hashes and review basis
- official requirement/source packet: `SOURCE_PACKET_0113_I18-E22_R01.md`, SHA-256 `5596e508240bc7995fb69181433756da11e9a0af02923620fc5490f49ea4a99b`, 2517 bytes.
- unique Blueprint: `UNIQUE_BLUEPRINT_0113_I18-E22_R01.md`, SHA-256 `15871b0ace40420c33b4a883c3f0f6dd2f2afa685fa47a1b36d3f66ca514c334`, 5733 bytes.
- synthetic dataset: `SYNTHETIC_DATASET_0113_R01.csv`, SHA-256 `6fe0928cc6100eae0ed6245f6866668e230276d51c8451a0a6197d90a3990d1f`, 659 bytes.
- synthetic replacement register: `SYNTHETIC_REPLACEMENT_REGISTER_0113_R01.csv`, SHA-256 `d25abbc9de8e941f3e7a35b7e6da197e7c49c4dc51dd51157a83e1c2ecbe03fd`, 2336 bytes.
- technical and visual QA receipt: `docx_technical_visual_qa_R01.json`, SHA-256 `e1690656a2840c8126f24e3619720871ab7102b24d64c3c7335ac872ee738961`, 6292 bytes.

## Official source packet (verbatim)

# 0113／I18-E22 來源包 R01

**狀態：SOURCE_PREPARED；僅候選施工來源，不代表協會實際會員資料或正式接受。**

## 文件身分與防止編號混用

- `doc_id`: 0113（142 文件歷史序列）
- `requirement_id`: I18-E22
- 157 專案對照位置：第 123 項（會員成長）；這是對照索引，不當成 Word 文件編號。
- 官方文件實際印製的 checkbox 序號：`UNKNOWN_NOT_ASSERTED`。
- 142 crosswalk 第 101 行：`I18-E22,1,0,0113,會員人數年度變化追蹤分析表`。
- Blueprint seed 將 0113 對應到「會員人數年度變化追蹤分析表」。

## 官方原始佐證

來源為訓練機構版 TTQS 查核佐證文件資料表 PDF，第 7 頁、指標 18、4 分常見參考佐證資料。與本文件直接對應的原文是：**「會員人數逐年增加。」** 這是 4 分層級的常見參考例示，不代表原始點協會已有該成果，也沒有指定成長百分比、最低會員數、必備會員類別或統計顯著門檻。

同頁 3 分的例示另提到「會員人數及會費收入均逐年增加」。0113 的 142 文件 crosswalk 專屬題名是會員人數年度變化追蹤表；本件必須把會員人數作為主指標，不把會費收入混入人數分子、分母或合併總分。除非另有授權來源，會費只可列為不同指標或排除於本件。

## 157 項寫作方向

157 寫作規格第 123 項為「會員成長：真實會員數來源與多期比較」。其要求是具體來源定位、核心正文／示範、分析或結果及與其他文件的事實連結。此段是專案的語意改寫，官方原文仍以 PDF 第 7 頁為準。

## 目前證據界線

這個 SOURCE_PREP 沒有提供原始點協會的會員名冊、年度快照、入會／退會紀錄、會員資格規章或實際會員數。所有成員數、期間、分類、來源代碼、變化率與結果只能用清楚標註的 `SAMPLE / SYNTHETIC ONLY` 完整示範。任何 REAL 欄位仍須取得有權限的原始資料、核准的會員定義與可稽核來源後才能替換。

不得宣稱會員實際逐年增加、不得代協會核定會員資格或保存期限、不得假造會員、簽章、會議決議或會員名冊。真實定義或來源缺失時標示 `UNKNOWN / HOLD`，並列出待取得的來源。

## 單一案例界線

後續示範使用獨立案例代碼 `SYN-0113-CASE-01`，只供 0113 的會員數趨勢計算。不得沿用 0112 的考照／回訓數字或 0100／0101 的學員評量數字。


## Unique Blueprint (verbatim)

# 0113／I18-E22 專屬 Blueprint R01

**文類：會員人數年度變化追蹤分析表。**
**候選定位：CANDIDATE／SAMPLE；不得標示 REAL、正式績效或 TTQS 已接受。**

## 1. 目的、用戶及操作結果

讓有權查閱會員資料的行政人員按一致的年度截點，計算每年符合核定定義的去重會員人數，核對增減、說明資料來源及作出誠實趨勢判讀。使用者要能依文件知道要找哪類來源、填哪一列、如何算、何時 HOLD／退回及如何追蹤差異。實際負責人姓名、職稱、會員資格規章與保留期限均為 UNKNOWN，不得自行指定。

## 2. 官方範圍與相似項區隔

- 唯一對應：doc_id 0113／I18-E22；官方 PDF p.7 指標 18 的 4 分參考例「會員人數逐年增加」。
- 本件核心是可重算的年度會員數，不是招生行銷、會員招募計畫、滿意度調查、會費收入分析、社會績效或學員考照／回訓分析。
- 157 專案第 123 項是會員成長／真實來源／多期比較方向；不得把 123 當成 0113。
- 4 分例示不提供目標數、成長百分比或會員政策；不可自行聲稱滿足正式評分。

## 3. 必備文件結構

1. 首頁與 30 秒使用指引：用途、期間、資料狀態、誰按權限操作、如何標記 HOLD。
2. 官方要求、範圍及 SAMPLE／REAL 界線；明示 checkbox 序號 UNKNOWN。
3. 會員定義與年度截點：列出「本示範」採用的合成定義；REAL 版必須引用協會正式有效定義及核准來源，不可把示範定義當成協會政策。
4. 四期趨勢表：2022–2025 年度截點、合成的去重會員數、前期數、淨增減、同比百分比、來源事實 ID、核對狀態。四列全部完整。
5. 期間變動核對：逐年顯示期初 + 本期淨新增 − 本期退出 = 期末；轉類及重複會員不可重複計數。基期不計同比。
6. 趨勢圖：同一會員定義、同一截點，縱軸為會員人數，標明 SYNTHETIC；圖上數值須與表格完全相同。
7. 判讀與處置示範：報告方向、基期、逐期差異、限制、可查的下一步；不得推論訓練因果、統計顯著或正式評核得分。若合成數下降也須如實展示，不得隱藏不利期間。
8. 資料品質、HOLD／REJECT 及重新核對步驟。
9. SAMPLE 事實替換清冊與來源索取清單。
10. REAL 替換檢核表：定義核定、來源定位、權限、去重證據、同截點、公式複核、責任角色均有證據後才可解除 HOLD；不得自動升格。

## 4. 合成案例與固定算式

案例 ID：`SYN-0113-CASE-01`。下列值全為合成示範，不代表協會現況。

| 年度截點 | 期初 | 合成新增 | 合成退出 | 期末唯一會員數 | 對前期淨變動 | 同比變化 |
|---|---:|---:|---:|---:|---:|---:|
| 2022-12-31 | 基期 | - | - | 42 | 基期 | N/A（基期） |
| 2023-12-31 | 42 | 8 | 4 | 46 | +4 | +9.5% |
| 2024-12-31 | 46 | 9 | 4 | 51 | +5 | +10.9% |
| 2025-12-31 | 51 | 10 | 4 | 57 | +6 | +11.8% |

公式：`期末 = 期初 + 新增 - 退出`；`同比淨變動 = 本期期末 - 前期期末`；`同比變化率 = 同比淨變動 ÷ 前期期末 × 100%`，四捨五入至小數 1 位。總變動 2022→2025 為 +15 人、+35.7%。若前期為 0，百分比列 N/A，不得除以零或寫無限大。合成會員代碼不可對應真實自然人。

## 5. 表格欄位與來源

至少包含：年度截點、會員定義／類別、去重後期末數、期初數、有效新增、退出、變動核對式、同比增減、同比百分比、來源事實 ID、證據類型、來源位置、覆核狀態、未知／例外說明、責任角色（實名欄不得假造）。公開報告不得放姓名、電話、身分證號、地址或原始會員 ID；原始名冊留在有權限的正式位置，報告只呈現聚合值及安全的來源定位。

## 6. HOLD／REJECT 條件

- `HOLD`：年度截點未對齊；會員資格定義未核定；來源檔／頁／報表日期缺失；權限不明；實際值尚未取得；匿名化／去重證據不足；前期分母為零；類別變更尚未重述可比資料；覆核人或來源責任未知。欄位寫 `UNKNOWN / HOLD` 並寫明待補資料，不留無說明空白。
- `REJECT`：同一人重複計數；將會費金額當會員數；期間口徑不一致仍硬接趨勢；算式不平；表／圖／結論不一致；把 SYNTHETIC 寫成 REAL；隱去下降期；或聲稱協會核准、官方得分／因果但無來源。
- 只有核對來源、定義、截點、公式、去重與授權俱全，才可把資料列由 HOLD 轉為可覆核；仍不代表 Human 正式接受。

## 7. 跨文件連結與替換規則

可在「關聯文件用途」說明 0112 是考照／回訓，0111 是特殊績效／社會成果，0100／0101 是學員自評與能力雷達；它們不能代替 0113 的會員名冊來源，也不得把其數字挪用至本案例。每個事實採 `SYN-0113-F01` 起始的唯一 ID，替換清冊記來源、授權、期間、欄位、驗證人角色、狀態及未解缺口。缺真實會員來源時，保留合成示範與完整索取路徑，REAL 狀態為 UNKNOWN／HOLD。

## 8. Word 與獨立驗收

正文須繁體中文、第一頁可直接操作、表格與圖使用相同 case ID；每頁明確標 SAMPLE／SYNTHETIC ONLY。正文不放 GitHub 路徑、SHA 或工程欄位。技術驗收檢查 OOXML、數學、表圖一致、正文至少 10.5pt、表格至少 9.5pt、可讀的 A4 版面及全頁渲染。獨立 reviewer 必須綁定最終 DOCX exact SHA，分別回報語意、數據及視覺範圍；Builder 自報不得當 PASS。此 Blueprint 不代表已實際建立 Word 或通過驗收。


## Synthetic dataset

```csv
fact_id,case_id,period_end,synthetic_membership_definition,opening_count,synthetic_additions,synthetic_exits,closing_unique_member_count,net_change_vs_prior,net_change_formula,yoy_percent_change_1dp,evidence_status
SYN-0113-F01,SYN-0113-CASE-01,2022-12-31,BASELINE,42,N/A_BASELINE,N/A_BASELINE,42,BASELINE,N/A_BASELINE,N/A_BASELINE,SYNTHETIC_ONLY
SYN-0113-F02,SYN-0113-CASE-01,2023-12-31,ACTIVE_UNIQUE_AT_CUTOFF,42,8,4,46,+4,46-42,9.5,SYNTHETIC_ONLY
SYN-0113-F03,SYN-0113-CASE-01,2024-12-31,ACTIVE_UNIQUE_AT_CUTOFF,46,9,4,51,+5,51-46,10.9,SYNTHETIC_ONLY
SYN-0113-F04,SYN-0113-CASE-01,2025-12-31,ACTIVE_UNIQUE_AT_CUTOFF,51,10,4,57,+6,57-51,11.8,SYNTHETIC_ONLY
```

## Synthetic replacement register

```csv
fact_id,synthetic_value,real_source_required,real_authorization_required,data_minimization,verification_required,status,hold_reason
SYN-0113-F01,42,Authorized dated membership roster snapshot for the same cutoff; source locator and duplicate-control evidence,Proof of lawful access plus organization-approved membership definition and reporting purpose,"Aggregate count only in public Word; never copy names, phone, government ID or raw member ID",Recompute distinct eligible members; tie opening + additions - exits to closing; independent second-person/role check,SYNTHETIC_ONLY; REAL UNKNOWN/HOLD,No association source or policy supplied; replace only with authorized real source
SYN-0113-F02,46,Authorized dated membership roster snapshot for the same cutoff; source locator and duplicate-control evidence,Proof of lawful access plus organization-approved membership definition and reporting purpose,"Aggregate count only in public Word; never copy names, phone, government ID or raw member ID",Recompute distinct eligible members; tie opening + additions - exits to closing; independent second-person/role check,SYNTHETIC_ONLY; REAL UNKNOWN/HOLD,No association source or policy supplied; replace only with authorized real source
SYN-0113-F03,51,Authorized dated membership roster snapshot for the same cutoff; source locator and duplicate-control evidence,Proof of lawful access plus organization-approved membership definition and reporting purpose,"Aggregate count only in public Word; never copy names, phone, government ID or raw member ID",Recompute distinct eligible members; tie opening + additions - exits to closing; independent second-person/role check,SYNTHETIC_ONLY; REAL UNKNOWN/HOLD,No association source or policy supplied; replace only with authorized real source
SYN-0113-F04,57,Authorized dated membership roster snapshot for the same cutoff; source locator and duplicate-control evidence,Proof of lawful access plus organization-approved membership definition and reporting purpose,"Aggregate count only in public Word; never copy names, phone, government ID or raw member ID",Recompute distinct eligible members; tie opening + additions - exits to closing; independent second-person/role check,SYNTHETIC_ONLY; REAL UNKNOWN/HOLD,No association source or policy supplied; replace only with authorized real source
```

## Deterministic technical/layout QA summary

```json
{
  "project_id": "TTQS_ONE",
  "document_id": "0113",
  "requirement_crosswalk": "I18-E22",
  "official_checkbox_serial": "UNKNOWN",
  "candidate_state": "CANDIDATE_NOT_FORMALLY_ACCEPTED",
  "sample_real_state": "SAMPLE_SYNTHETIC_ONLY; all REAL replacement fields remain UNKNOWN/HOLD",
  "official_source": {
    "path": "training institution TTQS evidence guide, printed page 7, indicator 18 example 會員人數逐年增加。",
    "source_pdf_sha256": "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709",
    "source_excerpt_sha256": "47F4F8AAFD086906F52A5653AD8A0429656DDD2F0EC6CCE9AAADAB2B110623DB"
  },
  "source_packet_sha256": "5596E508240BC7995FB69181433756DA11E9A0AF02923620FC5490F49EA4A99B",
  "unique_blueprint_sha256": "15871B0ACE40420C33B4A883C3F0F6DD2F2AFA685FA47A1B36D3F66CA514C334",
  "synthetic_dataset_sha256": "6FE0928CC6100EAE0ED6245F6866668E230276D51C8451A0A6197D90A3990D1F",
  "docx": {
    "file": "0113_I18-E22_會員人數年度變化追蹤分析表_R01.docx",
    "sha256": "5f6d86a11ff884f7d0f1c251bf9b0dd4aa10b41defc68e2d1ea51b1afb329821",
    "bytes": 82863
  },
  "word_render_pdf": {
    "file": "0113_I18-E22_R01_final_v4_render.pdf",
    "sha256": "a73576b03babdbdefde1eb91351410c6369a7252d54054445daac2fcd8648a94",
    "bytes": 588590,
    "word_pages": 10
  },
  "structure": {
    "heading1_chapters": 12,
    "heading2_subsections": 27,
    "tables": 13,
    "table_font_pt": [
      9.5
    ],
    "embedded_images": 1,
    "rendered_page_pngs": 10
  },
  "arithmetic": {
    "rows": [
      {
        "fact_id": "SYN-0113-F02",
        "balance": 46,
        "closing": 46,
        "net": 4,
        "reported_net": "+4",
        "yoy": 9.5,
        "reported_yoy": 9.5
      },
      {
        "fact_id": "SYN-0113-F03",
        "balance": 51,
        "closing": 51,
        "net": 5,
        "reported_net": "+5",
        "yoy": 10.9,
        "reported_yoy": 10.9
      },
      {
        "fact_id": "SYN-0113-F04",
        "balance": 57,
        "closing": 57,
        "net": 6,
        "reported_net": "+6",
        "yoy": 11.8,
        "reported_yoy": 11.8
      }
    ],
    "period_total_change": 15,
    "period_percent_change_1dp": 35.7
  },
  "checks": {
    "doc_id_0113": true,
    "crosswalk_I18_E22": true,
    "checkbox_serial_not_invented": true,
    "sample_synthetic": true,
    "hold_reject": true,
    "real_replacement_register": true,
    "cross_document_boundaries": true,
    "math_consistent": true,
    "no_horizontal_rule_artifacts": true,
    "all_tables_min_9_5pt": true,
    "chapter7_starts_page": true,
    "real_todo_starts_page": true,
    "all_pages_rendered": true,
    "all_table_headers_have_repeat_metadata": true,
    "docx_archive_integrity": true,
    "chart_embedded": true
  },
  "technical_layout_result": "PASS",
  "visual_scope": "All 10 Word-rendered pages inspected through the complete final_v4 page-image set and contact sheets. Fixes include Markdown separator removal, independent numbered-list restart, table text raised to 9.5 pt, Chapter 7 moved with section 7.1, and complete 12.2 REAL to-do table on page 10.",
  "page_images": [
    {
      "file": "page-01.png",
      "sha256": "b6a2e02c962638e28bc46e10fbaf5eeafd1725689e8b595c1c58139da3606c6e",
      "bytes": 343929
    },
    {
      "file": "page-02.png",
      "sha256": "c61fa764baab47b243ccafe84a1902ccf59ea21a0297b198574b549a40bec2cb",
      "bytes": 247236
    },
    {
      "file": "page-03.png",
      "sha256": "b05ab49656fc4309aa81e27e7e029fa4774828c1a1f37c6a0495e2f3a761cb9f",
      "bytes": 211496
    },
    {
      "file": "page-04.png",
      "sha256": "12b560df6dda06bb3e2b616b0d1ef6c4f885e9652b395a9e01d52a3ba62068e9",
      "bytes": 164496
    },
    {
      "file": "page-05.png",
      "sha256": "41c65ca8edef778fce9ddd15d74f97d43962d1c47b3499bd484d8dce9d88c910",
      "bytes": 281764
    },
    {
      "file": "page-06.png",
      "sha256": "14b84dd4779e07dabaa2596b2a86cda1e7ca183ba0fab14e863259fe5d4eb41c",
      "bytes": 238353
    },
    {
      "file": "page-07.png",
      "sha256": "49636e9f33f4605df03e08129ab2e2dcde053db0ab4f63105ac5886dc0a9dedb",
      "bytes": 242853
    },
    {
      "file": "page-08.png",
      "sha256": "e1ab7aee9b4ee6f04b0469e120b6474aa409dc99b6ada1fde2e3b1512c15fea5",
      "bytes": 281684
    },
    {
      "file": "page-09.png",
      "sha256": "687be84dca81c68e7ee51a496385101de4a32fdca96649c8df09f101699f5180",
      "bytes": 116730
    },
    {
      "file": "page-10.png",
      "sha256": "f959606cb1704aec27ba997ecce82095f5fb0bf535e41d46658eed4213e6d869",
      "bytes": 120856
    }
  ],
  "independent_semantic_review": {
    "status": "BLOCKED_NOT_RUN_ON_FINAL_SHA",
    "final_candidate_sha256": "5f6d86a11ff884f7d0f1c251bf9b0dd4aa10b41defc68e2d1ea51b1afb329821",
    "reason": "OpenCode v2 free route returned provider.quota 429 Free usage limit reached on a prior exact-SHA review attempt. That error is not a semantic verdict. No review result exists for this final SHA.",
    "prior_attempt_sha256": "c058c1af2ca416eb8c10c953924eeab3ef82465d461cf3c8aefa49afca56ae1a",
    "requested_model": "opencode/glm-5.3-flash-free",
    "actual_review_model": "NONE; no reviewer response generated"
  },
  "writer_provenance": {
    "worker": "Antigravity CLI",
    "requested_model": "gemini-3.8-flash-high",
    "served_model": "UNKNOWN",
    "adopted_manuscript_sha256": "24a496ce239c1a01d657f9fb2a68ac811f64d80af5d5cd0cfb9b84899d87187b",
    "raw_success_json_sha256": "d5cd71236eec8552a9d6d86a49e06da66353abcd0e0bf6b5b99b4a481d0a71d0",
    "raw_success_output_bytes": 25494,
    "reported_usage_cumulative_two_turns": {
      "input_tokens": 38158,
      "output_tokens": 24522,
      "thinking_tokens": 4134,
      "total_tokens": 62680
    },
    "note": "Usage is cumulative for two conversation turns, not exact single-invocation cost. Output was independently corrected/adopted after unsupported role, threshold, and inference claims were removed."
  },
  "source_prep_remote_commit": "01eee96dd5809fdb6b564a865df27c99240bc18b",
  "created_at_local": "2026-10-24 Asia/Taipei"
}
```

## Final DOCX extracted paragraphs in order

P1: 《會員人數年度變化追蹤分析表暨判讀紀錄》

P2: 文件編號： 0113 專案需求對照碼： I18-E22（專案 crosswalk 代碼；不是官方 Checkbox 流水號） 官方佐證依據： 訓練機構版 TTQS 查核佐證文件資料表第 7 頁指標 18 的四分參考例示「會員人數逐年增加。」（僅為官方參考例示，不保證評分，也不代表本會已達成） 官方印製 Checkbox 序號： UNKNOWN（現有官方來源未證實此表的印刷流水號，不自行編列） 文件狀態： SAMPLE / SYNTHETIC ONLY（合成示範案例，非真實協會運作現況；REAL 欄位缺漏一律記為 UNKNOWN / HOLD）

P3: 第一章 30 秒快速指引與使用範圍

P4: 本表用來按一致的會員資格定義與年度截點，記錄期初、有效新增、有效退出和期末唯一會員數，再檢查數字能否對帳。下列四年數據全部是 SAMPLE／SYNTHETIC ONLY，不是原始點協會的會員實績。

P5: 1.1 三十秒操作指引

P6: 1. 先確認協會目前有效的會員定義、會員計量單位、年度截點及授權來源。任何一項尚未確認，真實資料標記 UNKNOWN／HOLD。

P7: 2. 本合成案例使用各年 12 月 31 日作為示範截點。真實資料必須依協會核定的期間口徑；不同截點不可直接拼成趨勢。

P8: 3. 在受權限控管的正式來源中依協會核准的唯一會員鍵去重。報表只記聚合數，不匯出姓名、聯絡資料、證件號或原始會員識別碼。沒有可覆核的去重證據時，標記 HOLD。

P9: 4. 逐年計算「期末＝期初＋有效新增－有效退出」，再計算「淨變動＝本期期末－前期期末」及「同比＝淨變動÷前期期末×100%」。基期或分母為零時記 N/A；真實資料的分母為零另標 HOLD 並說明。

P10: 5. 記錄每列的事實 ID、受限來源位置、覆核狀態和例外。公開版本只呈現必要的加總結果與合成標記。

P11: 1.2 適用範圍

P12: 本件聚焦會員數的年度變化。此 SAMPLE 將一筆符合示範口徑的唯一會員單位計為一人；這是計算示範，不是協會的會員類別或政策定義。正式作業須先確認協會對個人、團體或其他會員單位的有效定義。

P13: 會費金額、招募活動參與人次、課程學員、考照或回訓人次，以及社會服務受益人次都不是本表的會員人數。即使某人參加過課程，也須有符合正式會員定義的來源證據，才可計入會員統計。會費金額應留在其適用的財務指標，不折算為會員人數。

P14: 1.3 資料狀態

P15: SAMPLE／SYNTHETIC ONLY 表示數字只供示範公式和操作。REAL 表示來自獲授權的協會來源且完成必要核對。來源、定義、期間、權限或去重證據缺一時，真實欄位不得解除 UNKNOWN／HOLD。

P16: 第二章 會員定義與年度截點

P17: 2.1 合成示範口徑

P18: SYN-0113-CASE-01 僅示範如何追蹤同一口徑下的年度期末會員數。合成資料把每個年度截點仍符合示範資格的唯一會員單位計入期末數。案例沒有實際名冊、入會決議、繳費紀錄或退出文件，因此不能據此證明任何人的資格或去重結果。

P19: 2.2 真實作業開始前的確認項目

P20: 真實作業者須從協會現行有效來源確認會員種類、資格生效日、退會或停權如何影響期末計數、是否允許團體會員，以及統計的計量單位。把來源名稱、版本、生效日、可用的核准依據與受權確認角色記入下表；資料不足時維持 HOLD，不以本示範定義代替協會規則。

P22: 2.3 截點與期間

P23: 本案例以 2022 至 2025 各年 12 月 31 日作為 SAMPLE 截點。真實資料應採正式確認的年度期間和截點；若政策變更，須記錄變更前後口徑、是否需要重述可比期間，以及負責核對的授權角色。未能證明各期可比時，不得把數字串成同一條趨勢。

P24: 第三章 四年會員數趨勢

P25: 以下數據僅屬 SAMPLE／SYNTHETIC ONLY。SYN-0113-CASE-01 的四個事實 ID 對應同一組合成列。合成資料沒有會員名冊，無法驗證個人資格或真實去重。

P26: 3.1 年度趨勢表

P27: 年度人數對帳

P29: 淨變動、同比與證據狀態（以相同事實 ID 對照）

P31: 3.2 來源與覆核紀錄

P33: 3.3 計算規則

P34: 期末數＝期初數＋有效新增－有效退出。淨變動＝本期期末－前期期末。同比分母為前一期期末，計算至小數點後一位。若前一期為零，不進行除法，標示 N/A；真實資料同時保留 HOLD，直到期間基礎及報告方式經授權確認。

P35: 第四章 趨勢圖與呈現規則

P36: 圖表資料必須直接取自第三章同一案例，標題和頁面標記均須清楚顯示 SAMPLE／SYNTHETIC ONLY。縱軸以人數表示，橫軸依年度截點排序。若真實數據下降，圖表也須如實顯示，不得省略該年度或截斷座標誇大變化。

P38: 圖說：SYN-0113-CASE-01 合成案例的年度期末唯一會員數，2022 年 42 人、2023 年 46 人、2024 年 51 人、2025 年 57 人。此圖不代表協會實績。

P40: 第五章 計算示範與判讀

P41: 5.1 逐年計算

P42: 2022 基期：期末 42 人；沒有前期可比較，淨變動與同比均記為基期／N/A。

P43: 2023：42＋8－4＝46；淨變動為 46－42＝+4；同比為 4÷42×100%＝9.5%。

P44: 2024：46＋9－4＝51；淨變動為 51－46＝+5；同比為 5÷46×100%＝10.9%。

P45: 2025：51＋10－4＝57；淨變動為 57－51＝+6；同比為 6÷51×100%＝11.8%。

P46: 2022 至 2025：57－42＝+15；累積變化率為 15÷42×100%＝35.7%。

P47: 5.2 SAMPLE 判讀

P48: 在這組合成數字中，期末人數由 42 增至 57，三個年度的淨變動依序為 +4、+5、+6；合成退出數每年為 4。這是對示範數據的描述，不是協會實績或經會員來源核實的結果。

P49: 5.3 判讀限制

P50: 本表是描述性統計，沒有抽樣或推論設計，因此不聲稱統計顯著性。人數變化本身不能證明變化由訓練課程、服務或任何單一原因造成。官方來源所列「會員人數逐年增加」是參考例示，不保證正式得分或接受。

P51: 5.4 後續操作

P52: 真實作業時先取得有效會員定義、各期可比的來源快照、增減依據及去重核對紀錄，再填寫真實版本。若希望了解退出原因，須先確認有正當且授權的蒐集目的；本表不要求蒐集個人原因。

P53: 第六章 受限工作底稿與去重作業

P54: 原始名冊只留在協會核准、設有存取控制的正式來源。對外文件只呈現聚合數；不得把姓名、證件號、電話、地址、私人聯絡方式或原始會員識別碼複製到本表或公開附件。

P55: 6.1 受限底稿建議欄位

P57: 6.2 去重與資格核對步驟

P58: 1. 確認使用者有權限查看名冊與執行統計；權限不明時停止處理真實個資。

P59: 2. 依正式會員規則和核准的唯一識別方式，在受限來源系統內判定資格及去重，不把識別資料帶到公開報表。

P60: 3. 依正式生效日和同一年度截點核對新增、退出及期末狀態。不能確認者列為例外，不任意計入或刪除。

P61: 4. 將聚合期末數與期初＋新增－退出對帳。請另一名獲授權角色覆核；角色或覆核結果未知時維持 HOLD。

P62: 5. 對外只輸出彙總表、非敏感來源位置及狀態。不得用姓名雜湊或未核准的個人鍵取代正式去重措施。

P63: 第七章 資料字典與來源索取

P64: 7.1 資料字典

P66: 7.2 真實來源索取清單

P67: 真實替換前，依協會正式來源和權限取得下列最小必要資料：

P68: 有效會員資格定義、適用版本及生效期間。

P69: 各年度相同截點的會員狀態快照或可重算的受限來源。

P70: 各期新增、退出的有效日期及其來源定位。

P71: 受限來源內的去重方法、重複例外及聚合對帳紀錄。

P72: 資料提供、檢視、覆核和對外使用的授權依據。

P73: 協會確認的保存期限、修訂程序和覆核角色。

P74: 不預設協會一定使用特定會議、收據或財務系統。實際來源名稱及定位必須從獲授權的原始文件確認。

P75: 7.3 版本追溯

P77: 更正時保留舊版和更正原因，另記更正日期、來源依據及獲授權的覆核角色；不得覆寫歷史來源或假填核准資訊。

P78: 第八章 HOLD 與 REJECT 處置

P80: 8.1 判定順序

P81: 先檢查來源、定義、權限與期間，再檢查去重證據和算式。未知條件列 HOLD；已證實資料相互矛盾或數學錯誤則 REJECT。若同時存在兩種狀況，先拒收有錯資料並保留其他未決欄位的 HOLD 標記。不得因欄位有數字就視為已完成。

P82: 第九章 REAL 替換流程

P83: 真實資料必須另立 REAL 版本，不得在 SAMPLE 表中只替換一兩個年度，避免同一張表混合真實和合成數字。替換前封存這份示範版本並建立新的來源及核對紀錄。

P84: 9.1 REAL 替換清冊

P86: 9.2 不公開個資的聚合核對

P87: 1. 在獲授權的原始系統內按正式定義執行去重；公開報表只顯示加總數、期間、非敏感來源定位和覆核狀態。

P88: 2. 覆核角色在受限來源內重新計算或抽查必要紀錄。抽查範圍依協會核准程序決定，不在本示範中假定固定筆數。

P89: 3. 對帳期初＋新增－退出與期末，記錄差異、補正依據及版本。

P90: 4. 任何人都不得把含個資的名冊上傳公開儲存庫。無法安全取得或核對時，維持 UNKNOWN／HOLD。

P91: 第十章 年度結帳與異常更正

P92: 10.1 年度結帳

P93: 依協會正式年度管理時程，在核定截點後執行：確認資格定義與資料權限、取得相同口徑的來源快照、核對新增及退出、完成來源內去重、檢算總表、由獲授權角色覆核，最後保存版本及來源位置。協會完成期限未提供，本文不設定固定結帳日期。

P94: 10.2 歷史錯誤更正

P95: 發現錯誤時先保留原值、錯誤原因和來源，再建立新版本及更正紀錄。依協會正式權限規則決定由誰核准重述；在責任角色未確認前標 UNKNOWN／HOLD，不擅自指定治理機關或聲稱已追認。

P96: 10.3 異常增加或下降

P97: 遇到大幅增加、下降或不尋常的逐期差異，先查期間、會員定義、重複紀錄、異動生效日及來源版本。若協會有正式警示門檻，按該門檻啟動查核並保存依據；沒有核准門檻時，不自行創造百分比界線。圖表完整呈現所有年度。

P98: 10.4 權限與保存

P99: 原始名冊的存取角色、保存期限及更正規則均 UNKNOWN，須由協會正式來源確認並遵循適用要求。公開文件不保存個人識別資料。未確認權限或保存規則前，不移轉、公開或複製原始名冊。

P100: 第十一章 跨文件用途界線

P102: 若參訓者後來成為會員，只有在正式會員定義下取得有效資格並能由獲授權來源核對時，才可計入對應期間的會員數。其他文件的樣本、個案或彙總值不得移作本表來源。

P103: 第十二章 SAMPLE 判讀紀錄與 REAL 待辦

P104: 12.1 已填妥的 SAMPLE 判讀紀錄

P106: 12.2 REAL 開工前待辦

P108: 本文件目前只能作為合成作業示範。任何真實會員數、協會制度、簽核、正式採納或評核結果，都必須由相應正式來源另行證明。


## Final DOCX tables in order

### Table 1 — 6 rows × 6 columns
R1: 待確認事項 | 正式來源及版本 | 生效或適用期間 | 授權依據位置 | 確認角色 | 狀態
R2: 會員資格及計量單位 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN／HOLD
R3: 入會、退會及停權生效規則 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN／HOLD
R4: 年度報表截點 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN／HOLD
R5: 去重方法及受限來源系統 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN／HOLD
R6: 資料存取及保存規則 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN／HOLD

### Table 2 — 5 rows × 6 columns
R1: 事實 ID | 年度截點 | 期初 | 有效新增 | 有效退出 | 期末唯一會員數
R2: SYN-0113-F01 | 2022-12-31 | 基期 | 基期 | 基期 | 42
R3: SYN-0113-F02 | 2023-12-31 | 42 | 8 | 4 | 46
R4: SYN-0113-F03 | 2024-12-31 | 46 | 9 | 4 | 51
R5: SYN-0113-F04 | 2025-12-31 | 51 | 10 | 4 | 57

### Table 3 — 5 rows × 4 columns
R1: 事實 ID | 淨變動 | 同比 | 證據狀態
R2: SYN-0113-F01 | 基期 | N/A | SAMPLE／SYNTHETIC ONLY
R3: SYN-0113-F02 | +4 | +9.5% | SAMPLE／SYNTHETIC ONLY
R4: SYN-0113-F03 | +5 | +10.9% | SAMPLE／SYNTHETIC ONLY
R5: SYN-0113-F04 | +6 | +11.8% | SAMPLE／SYNTHETIC ONLY

### Table 4 — 5 rows × 6 columns
R1: 事實 ID | 示範來源位置 | 可核對的內容 | 本稿覆核狀態 | 未解限制 | 責任角色
R2: SYN-0113-F01 | 合成資料集第 1 列 | 基期值 42 | 算式資料重算一致 | 無真實快照或名冊 | UNKNOWN
R3: SYN-0113-F02 | 合成資料集第 2 列 | 42＋8－4＝46 | 算式資料重算一致 | 無新增／退出原始憑證 | UNKNOWN
R4: SYN-0113-F03 | 合成資料集第 3 列 | 46＋9－4＝51 | 算式資料重算一致 | 無新增／退出原始憑證 | UNKNOWN
R5: SYN-0113-F04 | 合成資料集第 4 列 | 51＋10－4＝57 | 算式資料重算一致 | 無新增／退出原始憑證 | UNKNOWN

### Table 5 — 5 rows × 5 columns
R1: 年度截點 | 期末唯一會員數 | 淨變動 | 同比變化率 | 資料狀態
R2: 2022-12-31 | 42 | 基期 | N/A | SAMPLE／SYNTHETIC ONLY
R3: 2023-12-31 | 46 | +4 | +9.5% | SAMPLE／SYNTHETIC ONLY
R4: 2024-12-31 | 51 | +5 | +10.9% | SAMPLE／SYNTHETIC ONLY
R5: 2025-12-31 | 57 | +6 | +11.8% | SAMPLE／SYNTHETIC ONLY

### Table 6 — 6 rows × 4 columns
R1: 欄位 | 記錄方式 | 使用目的 | 公開文件處理
R2: 受限來源位置 | 記錄系統名稱、檔案版本或受限資料夾定位 | 讓授權人可回查來源 | 只呈現非敏感的聚合來源說明
R3: 會員狀態及生效日期 | 依正式規則記入受限系統 | 判斷截點時是否符合資格 | 僅呈現加總結果
R4: 新增或退出類別 | 只記必要的異動分類與有效日期 | 對帳期初、新增、退出、期末 | 不公開個人異動資料或不必要原因
R5: 去重核對狀態 | 記錄協會核准的來源內去重程序及結果 | 確認同一會員未重複計數 | 報告核對狀態，不匯出識別鍵
R6: 覆核角色及日期 | 依正式分工登錄；未確認寫 UNKNOWN | 留下責任軌跡 | 不填未授權實名或簽章

### Table 7 — 8 rows × 4 columns
R1: 欄位 | 定義 | 必要檢查 | 缺漏處置
R2: 年度截點 | 該報告年度使用的正式截止日 | 各期口徑一致且有來源 | UNKNOWN／HOLD
R3: 期初人數 | 前一期已核對的期末唯一會員數 | 必須與前期結帳值銜接 | 無前期基準時說明基期
R4: 有效新增 | 本期依正式規則取得資格的會員單位數 | 檢查生效日期、資格和重複 | UNKNOWN／HOLD
R5: 有效退出 | 本期依正式規則失去資格的會員單位數 | 檢查生效日期及狀態變更 | UNKNOWN／HOLD
R6: 期末唯一會員數 | 截點符合定義且依核准方法去重的聚合數 | 期初＋新增－退出＝期末 | 算式不平則 REJECT
R7: 同比 | 淨變動除以前期期末 | 前期為零則不計算百分比 | N/A／HOLD
R8: 證據及覆核狀態 | 來源是否可回查、權限與覆核是否完成 | 標明 SAMPLE、REAL 或 UNKNOWN | 不得留白或自動升格

### Table 8 — 3 rows × 5 columns
R1: 版本 | 範圍 | 資料類型 | 來源與修改角色 | 採納狀態
R2: SAMPLE R01 | 2022 至 2025 年示範表及判讀 | 全數 SYNTHETIC ONLY | 撰稿／覆核角色 UNKNOWN | 未代表協會採納
R3: REAL 後續版本 | 依協會核准期間填寫 | 尚無真實資料 | UNKNOWN／HOLD | 待權限與來源核對

### Table 9 — 3 rows × 4 columns
R1: 狀態 | 觸發條件 | 處理方式 | 解除或重做條件
R2: HOLD | 正式定義、截點、來源位置、資料權限、去重證據或覆核角色尚未確認；前期分母為零；期間口徑改變而可比性未確認 | 標 UNKNOWN／HOLD，列明缺件和受限來源位置；真實數字不對外宣告 | 取得正式來源及授權，完成同口徑去重、算式複核並記錄獲授權角色；解除 HOLD 不等於 Human 或評核委員接受
R3: REJECT | 重複會員計數、把收入當人數、期間口徑不一致仍比較、算式不平、表圖結論矛盾、SAMPLE 冒充 REAL、隱藏下降年度或無來源聲稱核准／正式得分 | 退回該筆計算，保留原始版本和錯誤原因，不公開錯誤值 | 依正式來源重算並核對表格、圖表和判讀；修正版本留下可追溯紀錄

### Table 10 — 5 rows × 8 columns
R1: REAL 事實 ID | 年度截點 | 會員定義版本 | 期初／新增／退出／期末 | 來源位置 | 去重及對帳 | 覆核角色 | 狀態
R2: REAL-0113-F01 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN／HOLD
R3: REAL-0113-F02 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN／HOLD
R4: REAL-0113-F03 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN／HOLD
R5: REAL-0113-F04 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN／HOLD

### Table 11 — 5 rows × 3 columns
R1: 文件編號 | 本件以外的資料用途 | 與會員數的關係
R2: 0113 本件 | 年度會員資格及聚合會員數 | 只採正式會員來源；本案例全部合成
R3: 0112／I18-E21 | 考照及學員回訓追蹤 | 考照或回訓人次不能當會員數
R4: 0111 | 社會服務或績效佐證 | 服務及受益人次不能當會員數
R5: 0100／0101 | 學員調查、自評或能力分析 | 問卷數、訓練成效或能力分數不能當會員數

### Table 12 — 11 rows × 2 columns
R1: 項目 | SAMPLE 結果
R2: 案例 | SYN-0113-CASE-01
R3: 期間 | 2022-12-31 至 2025-12-31
R4: 資料狀態 | SAMPLE／SYNTHETIC ONLY
R5: 年度期末數 | 42、46、51、57
R6: 年度淨變動 | 基期、+4、+5、+6
R7: 年度同比 | N/A、+9.5%、+10.9%、+11.8%
R8: 全期變化 | +15 人、+35.7%
R9: 算式核對 | 三個年度平衡式均重算一致；沒有真實名冊或去重證據
R10: 判讀 | 本組合成數字逐年增加；不得推論訓練因果、統計顯著或正式得分
R11: 實際協會覆核者及核准 | UNKNOWN／HOLD；本示範不含協會簽核

### Table 13 — 7 rows × 5 columns
R1: 缺口 | 待取得或確認資料 | 完成條件 | 責任角色 | 狀態
R2: 會員定義 | 協會有效規則及適用版本 | 確認會員計量單位及生效條件 | UNKNOWN | HOLD
R3: 年度截點 | 正式年度報表期間 | 各期採同一可比較口徑或完成重述 | UNKNOWN | HOLD
R4: 四年來源 | 各年度受限來源快照或可重算紀錄 | 定位來源並可核對期初、新增、退出、期末 | UNKNOWN | HOLD
R5: 去重核對 | 協會核准的來源內去重方式 | 獲授權覆核者確認聚合數 | UNKNOWN | HOLD
R6: 存取及保存 | 適用授權、保存和修訂規則 | 完成權限與保存條件確認 | UNKNOWN | HOLD
R7: 官方 Checkbox 序號 | 官方原件可辨識的流水號 | 只按原件記錄，不由本稿推定 | UNKNOWN | HOLD
