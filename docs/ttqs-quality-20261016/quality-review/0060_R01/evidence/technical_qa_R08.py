from __future__ import annotations

import csv
import hashlib
import json
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from docx import Document

BASE = Path(__file__).resolve().parents[1]
DOCX = BASE / "candidate/0060_R08.docx"
SIDE = BASE / "sidecar/0060_R08_SYNTHETIC_REPLACEMENT_REGISTER.csv"
CONTENT = BASE / "worker/antigravity/0060_R04_content_for_build.json"
EXPECTED = "92962DF774A7A16546829D8968DC274394FC1EFCC12421C1A355F45127E9B5C3"
CODES = [
    "TT-2026-SYN60A-P-NEE-INT-S3-001-V01", "TT-2026-SYN60A-P-NAN-INT-S3-002-V01",
    "TT-2026-SYN60A-D-PLN-INT-S3-003-V01", "TT-2026-SYN60A-D-LSN-INT-S3-004-V01",
    "TT-2026-SYN60A-D-RSC-INT-S3-005-V01", "TT-2026-SYN60A-DO-ATT-RST-S3-006-V01",
    "TT-2026-SYN60A-DO-DLG-INT-S3-007-V01", "TT-2026-SYN60A-R-ASM-RST-S3-008-V01",
    "TT-2026-SYN60A-R-FDB-INT-S3-009-V01", "TT-2026-SYN60A-O-FUP-INT-S3-010-V01",
    "TT-2026-SYN60A-R-EXC-INT-S3-011-V01", "TT-2026-SYN60A-O-IMP-INT-S3-012-V01",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def norm(text: str) -> str:
    return " ".join(text.split())


def main() -> None:
    before = sha(DOCX)
    assert before == EXPECTED, f"Candidate SHA mismatch: {before}"
    with zipfile.ZipFile(DOCX) as archive:
        zip_error = archive.testzip()
    doc = Document(DOCX)
    data = json.loads(CONTENT.read_text(encoding="utf-8"))
    texts = [p.text for p in doc.paragraphs if p.text.strip()]
    body = "\n".join(texts + [cell.text for table in doc.tables for row in table.rows for cell in row.cells])
    forbidden_terms = ("待填", "待核", "空白表", "保持空白", "會後填寫")
    forbidden_hits = [term for term in forbidden_terms if term in body]
    all_tables = [table for table in doc.tables if table.rows]
    table91 = next(t for t in doc.tables if "完整文件識別編碼" in norm(" ".join(c.text for c in t.rows[0].cells)))
    table92 = next(t for t in doc.tables if "形成方式" in norm(" ".join(c.text for c in t.rows[0].cells)))
    rows91 = [[norm(c.text) for c in row.cells] for row in table91.rows[1:]]
    rows92 = [[norm(c.text) for c in row.cells] for row in table92.rows[1:]]
    table12 = doc.tables[11]
    table12_row_widths_valid = len(table12.rows) == 13 and all(len(row.cells) == 5 for row in table12.rows)
    imp_formation = norm(table12.rows[12].cells[1].text)
    table12_imp_formation_cell_clean = imp_formation == "綜合09回饋、10追蹤及11三項桌面演練缺失，提出改善追蹤樣張；未核准、未執行。"
    correction_cells = {
        "RSC05_duplicate_code_corrected_004_to_005": "RSC樣張代碼流水號由004更正為005" in table12.rows[5].cells[3].text and "12筆代碼均唯一" in table12.rows[5].cells[3].text,
        "ATT06_INT_to_RST_label_correction": "原先誤標INT，已更正為RST" in table12.rows[6].cells[3].text,
        "DLG07_source_locator_added": "LOC-REC-2026-0815B" in table12.rows[7].cells[3].text,
        "ASM08_no_false_label_correction_claim": "未另設缺陷修正" in table12.rows[8].cells[3].text and "初始標籤不符已修正" not in table12.rows[8].cells[3].text,
        "EXC11_three_baselines_and_fixed_results": all(s in table12.rows[11].cells[3].text for s in ("11/12", "10/12", "11/12", "12/12")),
        "Table15_version_segment_V01": doc.tables[14].rows[5].cells[3].text.rstrip().endswith("-V01"),
        "zero_denominator_NA_rule": any("分母為0" in p.text and "標示 N/A" in p.text and "不得報100%" in p.text for p in doc.paragraphs),
    }
    codes = [next((value for value in row if value.startswith("TT-")), "") for row in rows91]
    code_count = {code: codes.count(code) for code in CODES}

    def contains(row: list[str], value: str) -> bool:
        return value in " | ".join(row)

    lineage = {
        "RSC_05_source_plan_and_lesson_03_04": contains(rows91[4], "依附003、004") and contains(rows92[4], "依附03、04"),
        "ATT_06_source_plan_03": contains(rows91[5], "依附003") and contains(rows92[5], "依附03"),
        "DLG_07_source_plan_and_lesson_03_04": contains(rows91[6], "依附003、004") and contains(rows92[6], "依附03、04"),
        "ASM_08_denominator_traces_to_attendance_06": contains(rows91[7], "依附003、004、006") and contains(rows92[7], "依附03、04、06") and "06簽到" in " | ".join(rows92[7]),
        "FDB_09_ten_forms_traces_to_attendance_06": contains(rows91[8], "依附003、006") and contains(rows92[8], "依附03、06") and "06簽到" in " | ".join(rows92[8]) and "03簽到" not in " | ".join(rows92[8]),
        "FUP_10_ten_person_cohort_traces_to_attendance_06": contains(rows91[9], "依附003、006") and contains(rows92[9], "依附03、06") and "06簽到" in " | ".join(rows92[9]),
        "EXC_11_links_duplicate_05_label_06_locator_07": contains(rows91[10], "依附005、006、007") and contains(rows92[10], "依附05、06、07"),
        "IMP_12_formation_and_source_links_09_10_11": contains(rows91[11], "依附009、010、011") and contains(rows92[11], "依附09、10、11") and all(token in " | ".join(rows92[11]) for token in ("09回饋", "10追蹤", "11三項")),
    }
    source_rows = data["sections"][8]["tables"][0]["rows"]
    # Compare the replacement register to the actual R08 DOCX, not the stale R04 source JSON.
    detail_rows = [[norm(c.text) for c in row.cells] for row in table12.rows[1:]]
    reg = {"all_doc_id_0060": True, "all_sample": True, "unique_fact_ids": True, "table9_2_values_match": True}
    with SIDE.open(encoding="utf-8-sig", newline="") as stream:
        register = list(csv.DictReader(stream))
    reg["all_doc_id_0060"] = all(row.get("doc_id") == "0060" for row in register)
    reg["all_sample"] = all(row.get("status", "").upper() == "SAMPLE" for row in register)
    reg["unique_fact_ids"] = len({row.get("fact_id") for row in register}) == len(register)
    by_fact = {row.get("fact_id"): row for row in register}
    for number, row in enumerate(detail_rows, start=55):
        rec = by_fact.get(f"SYN-0060-FACT-{number:03d}")
        if not rec or rec.get("value") != " | ".join(row):
            reg["table9_2_values_match"] = False

    rate_inputs = {"attendance_10_of_12": (10,12), "assessment_8_of_9": (8,9), "feedback_8_of_9": (8,9), "followup_8_of_10": (8,10), "self_report_6_of_8": (6,8), "unique_11_of_12": (11,12), "complete_10_of_12": (10,12), "label_11_of_12": (11,12)}
    rates = {name: round(a / b * 100, 1) for name, (a, b) in rate_inputs.items()}
    rate_text = {name: f"{rate:.1f}%" for name, rate in rates.items()}
    render_path = BASE / "evidence/render_R08/render_manifest_R08.json"
    render = json.loads(render_path.read_text(encoding="utf-8")) if render_path.exists() else None
    result = {
        "doc_id": "0060", "requirement": "I14-E01", "checkbox": "065",
        "candidate_sha256": before, "candidate_bytes": DOCX.stat().st_size,
        "docx_sha_unchanged_during_check": sha(DOCX) == before,
        "zip_testzip_error": zip_error, "python_docx_opened": True,
        "heading_1_count": sum(1 for p in doc.paragraphs if p.style and p.style.name == "Heading 1"),
        "title_style_present": any(p.style and p.style.name == "Title" for p in doc.paragraphs),
        "content_sections": len(data["sections"]), "content_data_tables": sum(len(section.get("tables", [])) for section in data["sections"]),
        "content_data_rows": sum(len(table.get("rows", [])) for section in data["sections"] for table in section.get("tables", [])),
        "rendered_body_tables": len(all_tables) - 1,
        "table9_1_rows": len(rows91), "table9_2_rows": len(rows92),
        "table12_row_widths_valid": table12_row_widths_valid,
        "table12_imp_formation_cell": imp_formation,
        "table12_imp_formation_cell_clean": table12_imp_formation_cell_clean,
        "R07_semantic_findings_repaired": correction_cells,
        "all_R07_semantic_findings_repaired": all(correction_cells.values()),
        "all_12_codes_exactly_once": all(value == 1 for value in code_count.values()),
        "table9_1_row_widths_valid": len(source_rows) == 12 and all(len(row) == 6 and all(cell.strip() for cell in row) for row in source_rows),
        "table9_2_row_widths_valid": len(detail_rows) == 12 and all(len(row) == 5 and all(cell.strip() for cell in row) for row in detail_rows),
        "lineage_checks": lineage, "all_lineage_checks_pass": all(lineage.values()),
        "register_sha256": sha(SIDE), "register_rows": len(register), "register_checks": reg, "all_register_checks_pass": all(reg.values()),
        "recomputed_percentages": rates, "recomputed_strings_all_present": all(value in body for value in rate_text.values()),
        "repository_hard_rule_literal_hits": forbidden_hits,
        "render_manifest": render,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Deterministic structural, exact code, row-level lineage, register, arithmetic-string checks; not independent semantic acceptance.",
    }
    out = BASE / "evidence/technical_qa_R08.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    failures = []
    if zip_error is not None: failures.append("zip_integrity")
    if not result["docx_sha_unchanged_during_check"]: failures.append("docx_sha_changed")
    if not result["title_style_present"] or result["heading_1_count"] != 12: failures.append("heading_styles")
    if result["content_sections"] != 12 or result["content_data_tables"] != 17 or result["content_data_rows"] != 129 or result["rendered_body_tables"] != 17: failures.append("document_structure")
    if len(rows91) != 12 or len(rows92) != 12 or not result["all_12_codes_exactly_once"] or not result["table9_1_row_widths_valid"] or not result["table9_2_row_widths_valid"]: failures.append("sample_record_tables")
    if not table12_row_widths_valid or not table12_imp_formation_cell_clean: failures.append("table12_imp_formation_cell")
    if not result["all_R07_semantic_findings_repaired"]: failures.append("R07_semantic_findings")
    if not result["all_lineage_checks_pass"]: failures.append("cross_reference_lineage")
    if len(register) != 66 or not result["all_register_checks_pass"]: failures.append("replacement_register")
    if not result["recomputed_strings_all_present"]: failures.append("arithmetic_strings")
    if forbidden_hits: failures.append("repository_hard_rule_literal")
    if failures: raise SystemExit("FAILED: " + ", ".join(failures))


if __name__ == "__main__":
    main()


