{
  "binding": {
    "doc_id": "0106",
    "requirement_id": "I18-E14",
    "project_157_index": 115,
    "candidate_sha256": "204bc47e1d7049b872c667a07b1f9fe7d9148bb867ca13b59c89ccaad36d515e",
    "text_snapshot_sha256": "eed0cfe267d12c8d253f209f63294b5a7c3c7e2ab3c72c420dd73b997e452894",
    "candidate_state": "CANDIDATE_NOT_FORMALLY_ACCEPTED",
    "hashes_recomputed_by_reviewer": false,
    "basis": "supplied text snapshot bound to the candidate by the supplied technical receipt"
  },
  "overall_verdict": "PASS_TEXT_SEMANTIC_ONLY",
  "verdict_note": "No blocking content, arithmetic, SAMPLE/REAL, genre, authority or form-completeness defect found in the supplied snapshot. Attempt-06 F07R/F08R/F09/F15 are repaired; F13/F14 are non-blocking residuals; one new LOW navigation locator. Not formal acceptance, not CURRENT promotion, not REAL upgrade, not visual or remote verification.",
  "checks": [
    {
      "id": "C1_requirement_mapping_identity",
      "verdict": "PASS",
      "locator": "cover; T01 §1; §13.1",
      "note": "0106 / I18-E14 / index 115 / official p.7 / case SYN-0106-FIN-01 stated; T01 explicitly denies being the printed 核取欄序號; seed title preserved verbatim in T01 while cover adds （財務面）."
    },
    {
      "id": "C2_genre_distinctiveness",
      "verdict": "PASS_TEXT",
      "locator": "§3–§6, §8–§10, §13.1",
      "note": "Blind-read core is 10 paired baskets → index 0.98 → 8,000 cost → negative net → break-even/sensitivity, i.e. recognisably a training→organisational-finance analysis, not a survey report, voucher, financial statement or publicity piece. Formal blind test not executed and correctly marked UNKNOWN (T13 row 11)."
    },
    {
      "id": "C3_blueprint_coverage_T01_T13",
      "verdict": "PASS",
      "locator": "T01 §1; T02 §2; T03 §3; T04 §4; T05 §5; T06 §6; T07 §7.1; T08 §7.2; T09 §8; T10 §9; T11 §10; T13 §11.5; T12 §12",
      "note": "All 13 tables present with Blueprint-minimum columns. T03 carries 序號/前期/後期/名目差/指數/標準化值/標準化差額/fact_id plus a separate 來源欄與證據狀態 block. T04 separates cash vs non-cash; both figures carry unit/period/n/SYN labels and 圖1 has a reader-facing value table."
    },
    {
      "id": "C4_survey_instrument",
      "verdict": "PASS",
      "locator": "§7.1 T07; §7.2 T08",
      "note": "Six learner items + C1 client item; 1–5 anchors spelled out; 不適用 excluded from means; single-item <8 → UNKNOWN/HOLD; 12 invited / 10 valid / 83.33%; low scorers L05/L08/L10 retained; C1 n=1 explicitly non-inferential."
    },
    {
      "id": "C5_calc_trail_sensitivity_conclusion_actions",
      "verdict": "PASS",
      "locator": "T05 16 rows; T06 6 rows; §10.1; T11 8 rows; §11.4; §13.2",
      "note": "Every formula substituted and cross-checked; negative net retained in all four conclusion points; sensitivity band all-negative; actions carry SAMPLE role/date/evidence/HOLD trigger."
    },
    {
      "id": "C6_math_and_cross_table_consistency",
      "verdict": "PASS",
      "locator": "T03, T05, T06, T08, §4, §10.1",
      "note": "Independently recomputed; only the declared column-rounding Δ0.01 and the 7-dp threshold display remain, both inside the document's own ≤NT$0.05 policy."
    },
    {
      "id": "C7_cross_document_separation",
      "verdict": "PASS_DECLARED_BODY_SCREEN_UNKNOWN",
      "locator": "§0 item 4; §1.2; §13.1",
      "note": "0105 / 0104 / 0103 / item 120 boundaries stated in four places; unique case_id, IDs and codes; no shared respondents or numerators declared. Actual peer-body duplication screening is UNKNOWN (peer bodies not supplied)."
    },
    {
      "id": "C8_sample_real_boundary",
      "verdict": "PASS",
      "locator": "cover banner; header; footer; §11.1–11.4; §12; §13.3",
      "note": "SAMPLE/SYNTHETIC + REAL=UNKNOWN/HOLD repeated at cover, header, footer and §13; SYN-ROLE roles; §11.3 forbids 代簽; 決策狀態 不升格; no fabricated letter, certificate, quote, approval or signature; causal verbs confined to the banned-wording list."
    },
    {
      "id": "C9_human_facing_boundary",
      "verdict": "PASS_WITH_INFO_RESIDUAL",
      "locator": "§11.5 preamble; §11.5 分項判定原則; §13.4; T13 rows 12–14",
      "note": "exact-SHA / GitHub ref / raw-DOCX phrasing is gone from reader rows, and §11.5 now uses 發布檔案取回一致性查核. Residual: T13 row 14 keeps the gate label 遠端原始位元組讀回, which Blueprint §G itself mandates naming, and its 判定標準 column explains it plainly."
    },
    {
      "id": "C10_small_nonprofit_usability",
      "verdict": "PASS_WITH_LOW_RESIDUAL",
      "locator": "§0 導讀表 + 使用說明; §10.1; T11; §11.4; §13.2",
      "note": "Reader path, four-step workflow and HOLD triggers are usable. 使用說明 item 2 now consistently cites 第 3 章. One 導讀 locator imprecision remains (see N01)."
    },
    {
      "id": "C11_prior_F07_F09",
      "verdict": "F07R RESOLVED; F08R RESOLVED; F09 RESOLVED; F13/F14/F15/F16 as in findings",
      "locator": "§0 使用說明 item 2; §11.5; T05 row 14; T06 last row; T05 覆核 column; cover vs T01; T11 row 8; [FOOTER 0]",
      "note": "See findings."
    },
    {
      "id": "C12_visual_layout",
      "verdict": "UNKNOWN",
      "locator": "n/a",
      "note": "Out of scope. No page, figure, footer-field or font rendering inspected; the supplied visual receipt is a different QA scope and is neither endorsed nor re-derived here."
    },
    {
      "id": "C13_remote_readback",
      "verdict": "UNKNOWN",
      "note": "No remote bytes fetched."
    },
    {
      "id": "C14_formal_acceptance_real_promotion",
      "verdict": "NOT_GRANTED",
      "note": "Reviewer holds no acceptance authority; candidate remains CANDIDATE_NOT_FORMALLY_ACCEPTED, REAL=UNKNOWN/HOLD."
    }
  ],
  "findings": [
    {
      "id": "F07R",
      "severity": "INFO",
      "status": "RESOLVED",
      "locators": [
        "§11.5 preamble",
        "§11.5 分項判定原則",
        "§13.4",
        "T13 row 14"
      ],
      "evidence": "The two former residual phrases are repaired: §11.5 now reads 不等於獨立審查、全頁視覺、標題盲測、發布檔案取回一致性查核或 REAL 核准已完成, and the separation sentence uses 發布檔案取回一致性查核. §13.4 keeps the plain four-scope wording. Only T13 row 14 still carries the 遠端原始位元組讀回 gate label, which Blueprint §G mandates naming and which the row's 判定標準 explains in plain language.",
      "repair": "None required. Optional: retitle T13 row 14 to 發布檔案取回一致性查核 and keep 遠端原始位元組讀回 as an explanatory parenthetical."
    },
    {
      "id": "F08R",
      "severity": "INFO",
      "status": "RESOLVED",
      "locators": [
        "§0 使用說明 item 2"
      ],
      "evidence": "The sentence now reads 重算結果須依第 3 章四捨五入政策判定才算技術通過（列示差額 ≤ NT$0.05 依第 3 章政策）. Both halves point to 第 3 章, matching §3, §11.4, T13 row 2 and §13.2, so the prior internal referent contradiction is gone.",
      "repair": "None."
    },
    {
      "id": "F09",
      "severity": "INFO",
      "status": "RESOLVED",
      "locators": [
        "T05 row 14",
        "T06 last row"
      ],
      "evidence": "Exact threshold is 94,000 ÷ 92,000 = 1.0217391304. Substituting the printed 1.0217391 gives 94,000 ÷ 1.0217391 ≈ 92,000.0027, i.e. Δ ≈ 0.0027 matching the stated ~NT$0.003 and inside the ≤NT$0.05 policy; 92,000.00 / 8,000.00 / 0.00 / 0.00% all reproduce at 2 dp and the row is correctly flagged as a theoretical value outside 0.96–1.00.",
      "repair": "None."
    },
    {
      "id": "F13",
      "severity": "INFO",
      "status": "PERSISTS_FROM_ATTEMPT_06",
      "locators": [
        "T05 覆核 column rows 1–9 「待雙人重算」",
        "rows 10–16 advisory text"
      ],
      "evidence": "Column still mixes status with instruction. All substantive cells are filled, 待雙人重算 is an honest UNKNOWN consistent with §11.3 remaining blank and T13 row 2, so anti-placeholder rule 7 is not breached.",
      "repair": "Optional tidy-up only; no number change."
    },
    {
      "id": "F14",
      "severity": "INFO",
      "status": "PERSISTS_FROM_ATTEMPT_06",
      "locators": [
        "cover title",
        "T01 文件標題 row"
      ],
      "evidence": "Cover reads …之說明（財務面）分析報告 while T01 preserves the seed title …之說明_分析報告 verbatim, so identity stays traceable.",
      "repair": "None."
    },
    {
      "id": "F15",
      "severity": "INFO",
      "status": "RESOLVED",
      "locators": [
        "T11 row 8 期限欄"
      ],
      "evidence": "Now reads 依第 11 章替換完成日（SAMPLE）, replacing 依替代進度; §11 is in fact the replacement chapter, and the completion evidence cell still holds a verifiable condition (T12 全列狀態非 UNKNOWN/HOLD).",
      "repair": "None."
    },
    {
      "id": "F16",
      "severity": "INFO_TECHNICAL_NOT_SEMANTIC",
      "status": "UNKNOWN",
      "locators": [
        "[FOOTER 0] 原始點協會 TTQS ONE｜候選稿，未正式接受｜第 1 頁"
      ],
      "evidence": "A text snapshot cannot separate a live PAGE field from a static string; the receipt and visual receipt both assert footer page fields, but neither was reproduced in this scope.",
      "repair": "Confirm in the native page gate; no semantic action."
    },
    {
      "id": "N01",
      "severity": "LOW",
      "status": "NEW",
      "locators": [
        "§0 導讀表 rows 用什麼案例 and 結果是正是負"
      ],
      "evidence": "案例 ID, 期間, 10 組配對與納入／排除規則 sit in 第 2 章 (T02), yet the 導讀 row points readers to 第 3 章; the net −3,918.37 / −48.98% is first derived in 第 5 章 (T05 rows 8–9) while the row points to 第 6 章. Both destinations do restate fragments of the content, so this is misdirection, not a missing section, and no number is affected.",
      "repair": "Minimal: change 第 3 章 → 第 2–3 章 and 第 6 章 → 第 5–6 章 in those two 導讀 cells. Non-blocking."
    },
    {
      "id": "N02",
      "severity": "INFO",
      "locators": [
        "T05 row 14 公式欄",
        "T13 rows 7 and 12"
      ],
      "evidence": "The break-even formula is printed as 100,000 - 94,000 ÷ x = 8,000 without parentheses; it yields the correct x only under standard precedence, and the algebra is restated correctly in T06. Separately, T13 rows 7/12 still record page/visual status as UNKNOWN while a native visual receipt now exists in a different QA scope; the document's conservative self-statement is legitimate but will be stale at promotion time.",
      "repair": "Optional: write 100,000 −（94,000 ÷ x）= 8,000; refresh T13 rows 7/12 when the promotion gate records its actual status."
    }
  ],
  "recomputation": {
    "t03_rows": "All 10 rows reproduce to 2 dp: 7,653.06/346.94; 11,734.69/265.31; 8,775.51/224.49; 10,612.24/387.76; 6,938.78/61.22; 14,285.71/714.29; 9,693.88/306.12; 7,755.10/244.90; 9,591.84/408.16; 8,877.55/1,122.45. Column sums 100,000 / 94,000 / 6,000; rounded standardized sum 95,918.36 and rounded-difference sum 4,081.64, i.e. the documented Δ0.01 against totals 95,918.37 / 4,081.63.",
    "core": "94,000 ÷ 0.98 = 95,918.3673 → 95,918.37; gross 4,081.63; rate 4.08163% → 4.08%; net −3,918.37; ROI −48.9796% → −48.98%; gross return 51.02%; nominal net −2,000; break-even gross 8,000; gap 3,918.37; cost cap 4,081.63; break-even index 94,000 ÷ 92,000 = 1.02173913; monthly 680.27; 8,000 ÷ 680.27 = 11.76 (~11.8 months).",
    "t06": "0.96 → 97,916.67 / 2,083.33 / −5,916.67 / −73.96%; 0.97 → 96,907.22 / 3,092.78 / −4,907.22 / −61.34%; 0.98 → 95,918.37 / 4,081.63 / −3,918.37 / −48.98%; 0.99 → 94,949.49 / 5,050.51 / −2,949.49 / −36.87%; 1.00 → 94,000.00 / 6,000.00 / −2,000.00 / −25.00%; critical row 92,000.00 / 8,000.00 / 0.00 / 0.00%. All observed-band scenarios negative; none break-even.",
    "cost": "4,500 + 1,000 + 2,500 = 8,000; the three non-cash rows are unquantified and excluded from the ROI denominator, consistent with §4, §10.1 and §12.",
    "survey": "Item sums 39/37/38/40/33/36 = 223; means 3.9/3.7/3.8/4.0/3.3/3.6; personal totals 26/24/22/24/18/29/24/19/22/15 = 223; 4–5 counts 8/6/7/8/5/6; 1–2 counts 1/1/1/0/2/1; Q5 residual split 3分 = L02/L04/L05, 2分 = L08/L10; response rate 10 ÷ 12 = 83.33%.",
    "fixed_input_fidelity": "All 10 basket amounts, index 0.98, cost split 4,500/1,000/2,500, the 12-invited/10-valid design and all 60 item scores match SOURCE_PACKET §4.1–4.3 exactly; no fixed input was rewritten and no new synthetic amount was introduced.",
    "calendar_and_units": "前期 2025-09-01～2026-02-28 and 後期 2026-04-11～2026-10-10 are each six months; training 2026-04-10 precedes the post window by one day; cutoff 2026-10-15 is five days after window close. No unit, period or pairing ambiguity found in T02/T03.",
    "agreement_with_technical_receipt": "Independently recomputed survey and finance figures agree with the receipt's survey_recalculation, finance_recalculation, t03_pair_rows_recomputed and figure1_data fields; agreement is corroborative only, not an endorsement of the receipt's other checks."
  },
  "authorized_blank_areas": "§11.1 replacement form, §11.2 source list and §11.3 double-recompute record are explicitly labelled REAL replacement blanks with filled SAMPLE companions, and T05 待雙人重算 is an honest UNKNOWN status, so anti-placeholder rule 7 is not engaged.",
  "review_scope": {
    "kind": "text-only independent semantic/content review on the two stated hashes",
    "read": [
      "supplied current candidate text snapshot",
      "technical receipt",
      "official page-7 extraction",
      "crosswalk row",
      "SOURCE_PACKET 0106 R01",
      "UNIQUE_BLUEPRINT 0106",
      "attempt-06 review and findings"
    ],
    "performed": [
      "arithmetic recomputation",
      "fixed-input fidelity check",
      "table/form completeness check",
      "SAMPLE/REAL and authority scan",
      "causal-wording scan",
      "cross-reference and locator check",
      "resolution test of F07R/F08R/F09/F13–F16",
      "new-defect probe"
    ],
    "not_performed": [
      "no file edits",
      "no DOCX/ZIP opening",
      "no SHA recomputation",
      "no rendering, page, figure or footer-field inspection",
      "no font measurement",
      "no peer-body duplication run",
      "no remote fetch",
      "no other model consulted"
    ]
  },
  "explicit_exclusions": [
    "Visual/layout, figure legibility, chart rendering, header/footer page-field behaviour, pagination and per-run font floors are OUT of scope; the supplied visual receipt is a separate QA scope and is not endorsed, re-derived or contradicted here.",
    "Remote raw-byte readback is not verified.",
    "Second-person signed recompute and reconciliation are not established.",
    "Actual cross-document body-duplication outcome against 0105 / 0104 / 0103 / item 120 is UNKNOWN.",
    "Official corrected page-7 wording is corroborated only by the bundle extraction, not by the PDF itself.",
    "Client evidence in this candidate is a single synthetic respondent (n=1); it supports no generalisation and none is made here.",
    "No REAL source exists or was authorised; nothing here asserts association facts, third-party evidence, approval, signature or achieved effect.",
    "No formal acceptance, no CURRENT promotion, no REAL=APPROVED and no evaluator-facing certification is granted or implied."
  ]
}
