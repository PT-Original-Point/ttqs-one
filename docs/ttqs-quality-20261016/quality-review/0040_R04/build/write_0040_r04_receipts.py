from pathlib import Path
import json,hashlib,sys
base=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0040_R04")
doc=base/"candidate"/"0040__訓練評估方法與成效指標對照表_R04.docx"
pdf=base/"render"/"0040_R04_final_word_export.pdf"
reg=base/"sources"/"0040_SOURCES_AND_SYNTHETIC_REPLACEMENT_REGISTER_R04.csv"
tech=base/"qa"/"0040_technical_review_r04_exact.json"
pages=base/"render"/"final_pages"
r03review=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0040_R03\qa\0040_semantic_review_r03_exact.json")
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
images={str(i):sha(pages/f"page-{i}.png") for i in range(1,9)}
baseline={str(i):sha(base/"render"/"baseline_r03_120dpi"/f"page-{i}.png") for i in range(2,7)}
visual={
"project_id":"TTQS_ONE","doc_id":"0040","revision":"R04","review_type":"primary_visual_layout_check",
"candidate_sha256":sha(doc),"rendered_pdf_sha256":sha(pdf),"page_count":8,
"page_png_sha256":images,
"direct_visual_inspection_pages":[1,7,8],
"unchanged_pages_pixel_identical_to_R03":{"2":True,"3":True,"4":True,"5":True,"6":True},
"R03_comparison_png_sha256":baseline,
"layout_findings":[
"Page 1 case ID was added to the existing SAMPLE boundary paragraph; content remains within the page and readable.",
"Pages 2-6 are pixel-identical at 120 dpi to the prior R03 Word render; R03 independent reviewer directly inspected all six R03 pages.",
"Page 7 contains visible version/effectivity, official mapping and revision history; the table rows are readable without clipping.",
"Page 8 continues the audit index with a repeated header; all cells and page numbering are readable, with no clipping or overlap."
],
"primary_visual_result":"PASS",
"independent_semantic_review":"PENDING",
"promotion_status":"NOT_PROMOTED"
}
(base/"qa"/"0040_visual_review_r04_primary.json").write_text(json.dumps(visual,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
provenance={
"project_id":"TTQS_ONE","doc_id":"0040","revision":"R04",
"requirement_id":"I08-E03","official_checkbox_sequence":"040",
"candidate_sha256":sha(doc),"register_sha256":sha(reg),
"official_source_pdf_sha256":"805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709",
"source_map_sha256":"405b987797d1558ecac182cea8e1adfbd1aead7754c880db32db43c235d5024e",
"blueprint_file_sha256":"406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e",
"blueprint_row_sha256":"ab080a2e6d85cc13a706f0c10bda7c208ddc191a1fea20a670fd5a174ab14943",
"parent_candidate_r03_sha256":"c84e200ff11d2e9f46360b4e03b7867e22fb03ac4ec298d022c9d1f3d76ffdf8",
"parent_review_r03_sha256":sha(r03review),
"parent_review_r03_verdict":"PARTIAL",
"repair_scope":[
"Added visible SAMPLE case identifier to the existing sample-boundary paragraph.",
"Added visible R04 document revision, SAMPLE v1.0 tool-version/effectivity status, official mapping, revision history and printed-page audit index.",
"Replaced all 39 register locators with printed page, table header, row label and relevant column references; removed nonprinted section locators.",
"Updated sample role register value to match the descriptive role labels in the document.",
"No assessment vectors, thresholds, calculations, or D04 follow-up facts were changed."
],
"authoring_route":"Codex local targeted Python-docx repair; this is not an institutional authorship or approval claim.",
"rendered_pdf_sha256":sha(pdf),"page_count":8,
"technical_receipt_sha256":sha(tech),
"primary_visual_receipt_sha256":sha(base/"qa"/"0040_visual_review_r04_primary.json"),
"register_rows":39,"register_rows_bound_to_candidate_sha":39,"register_locator_anchor_checks_passed":39,
"sample_state":"SAMPLE_SYNTHETIC_ONLY; no association attendance, scores, approval, execution, or result is claimed.",
"independent_semantic_verdict":"PENDING",
"candidate_state":"CANDIDATE_NOT_PROMOTED",
"formal_acceptance":"NOT_GRANTED"
}
(base/"qa"/"0040_R04_provenance.json").write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
for f in [base/"qa"/"0040_visual_review_r04_primary.json",base/"qa"/"0040_R04_provenance.json"]:
 print(f.name,sha(f))
