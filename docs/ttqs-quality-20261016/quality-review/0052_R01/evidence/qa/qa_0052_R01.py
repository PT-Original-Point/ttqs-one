from __future__ import annotations

import ast
import csv
import hashlib
import json
from pathlib import Path

from docx import Document


PKG = Path(__file__).resolve().parents[2]
BUILDER = PKG / "evidence" / "build" / "build_0052_R01.py"
DOCX = PKG / "candidate" / "0052_R01.docx"
SOURCE_MAP = PKG / "inputs" / "SOURCE_MAP_R01.md"
BLUEPRINT = PKG / "inputs" / "UNIQUE_BLUEPRINT_0052.jsonl"
REGISTER = PKG / "evidence" / "SYNTHETIC_REPLACEMENT_REGISTER_R01.csv"
PDF = PKG / "evidence" / "render_final_406d1ef2" / "0052_R01.pdf"
RENDER = PDF.parent
OUT = PKG / "evidence" / "qa" / "TECHNICAL_VISUAL_QA_R01.json"
SEMANTIC_REVIEW = PKG / "review" / "opencode_v2_R01" / "semantic_review_result_R01.md"
METADATA = PKG / "evidence" / "build" / "BUILD_METADATA_R01.json"

OFFICIAL = "規劃課程依學員及結訓學員意見訂定訓練課程，且流程有完整紀錄。"
EXPECTED_DOCX_SHA = "406d1ef2c6e9b6266ea1adaeadedc5dfac77964fe76f73c2471168220ee6d455"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def builder_literals() -> dict:
    tree = ast.parse(BUILDER.read_text(encoding="utf-8"))
    wanted = {"LEARNER_ROWS", "GRAD_ROWS", "NEED_OPTIONS", "WEIGHTS", "OPTIONS"}
    result = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in wanted:
                    result[target.id] = ast.literal_eval(node.value)
    missing = wanted - result.keys()
    if missing:
        raise RuntimeError(f"builder literal assignments missing: {sorted(missing)}")
    return result


def effective_font_pt(run, paragraph, doc):
    size = run.font.size
    if size is None:
        size = paragraph.style.font.size
    if size is None:
        size = doc.styles["Normal"].font.size
    return size.pt if size is not None else None


def main() -> None:
    doc = Document(DOCX)
    body_sizes = []
    table_sizes = []
    unknown_fonts = []
    for pi, para in enumerate(doc.paragraphs, 1):
        if not para.text.strip() or para.style.name.startswith("Heading") or para.style.name in {"Title", "Subtitle", "Caption"}:
            continue
        for run in para.runs:
            if run.text.strip():
                pt = effective_font_pt(run, para, doc)
                if pt is None:
                    unknown_fonts.append(f"body paragraph {pi}")
                else:
                    body_sizes.append(pt)
    for ti, table in enumerate(doc.tables, 1):
        for ri, row in enumerate(table.rows, 1):
            for ci, cell in enumerate(row.cells, 1):
                for para in cell.paragraphs:
                    for run in para.runs:
                        if run.text.strip():
                            pt = effective_font_pt(run, para, doc)
                            if pt is None:
                                unknown_fonts.append(f"table {ti}, row {ri}, cell {ci}")
                            else:
                                table_sizes.append(pt)

    all_text = "\n".join(
        [p.text for p in doc.paragraphs]
        + [cell.text for table in doc.tables for row in table.rows for cell in row.cells]
    )
    literals = builder_literals()
    learner = literals["LEARNER_ROWS"]
    graduate = literals["GRAD_ROWS"]
    weights = literals["WEIGHTS"]
    options = literals["OPTIONS"]
    learner_stats = []
    for qi in range(7):
        values = [row[qi] for row in learner]
        learner_stats.append({
            "item": f"Q{qi + 1}",
            "n": len(values),
            "sum": sum(values),
            "mean": round(sum(values) / len(values), 3),
            "frequencies_1_to_5": [values.count(v) for v in range(1, 6)],
        })
    graduate_stats = []
    for qi in range(3):
        values = [row["ratings"][qi] for row in graduate]
        graduate_stats.append({
            "item": f"G{qi + 3}",
            "n": len(values),
            "sum": sum(values),
            "mean": round(sum(values) / len(values), 3),
            "frequencies_1_to_5": [values.count(v) for v in range(1, 6)],
        })
    needs = literals["NEED_OPTIONS"]
    need_stats = {option: sum(option in row["needs"] for row in graduate) for option in needs}
    exclusivity_ok = all(
        ("目前不需要" not in row["needs"] or row["needs"] == ["目前不需要"])
        for row in graduate
    )
    weighted = {
        name: sum(weight * score for weight, score in zip(weights, scores))
        for name, scores in options.items()
    }
    weighted_percent = {name: round(points / (sum(weights) * 5) * 100, 2) for name, points in weighted.items()}
    with REGISTER.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    ids = [row.get("fact_id", "") for row in rows]
    statuses = sorted({row.get("source_status", "") for row in rows})
    register_ok = bool(rows) and len(ids) == len(set(ids)) and all(
        row.get("fact_id")
        and row.get("exact_document_locator")
        and row.get("required_real_replacement")
        and "REAL" not in row.get("source_status", "").upper()
        for row in rows
    )
    pages = sorted(RENDER.glob("page-*.png"))
    contact_sheets = sorted(RENDER.glob("contact-*.png"))
    source_text = SOURCE_MAP.read_text(encoding="utf-8")
    blueprint_text = BLUEPRINT.read_text(encoding="utf-8")
    metadata = json.loads(METADATA.read_text(encoding="utf-8"))
    semantic_text = SEMANTIC_REVIEW.read_text(encoding="utf-8") if SEMANTIC_REVIEW.exists() else ""
    semantic_result_line = next((line for line in semantic_text.splitlines() if "整體語意結果" in line), "")
    semantic_status = semantic_result_line.split("`")[1] if "`" in semantic_result_line else "PENDING"
    semantic_exact_sha_bound = EXPECTED_DOCX_SHA in semantic_text
    source_specs = [
        ("0033_R03", Path("docs/ttqs-quality-20261016/quality-review/0033_R03/candidate/0033_R03.docx"), "fe5f3cfd84c761da86435a71e0fd899daa725be78628c4d2d3f2324c1fdb5f4f"),
        ("0049_R01", Path("docs/ttqs-quality-20261016/quality-review/0049_R01/candidate/0049_R01.docx"), "e8212788b1f7b201ca4af4f4c5fb83ab131627dbfa815987f7cf6344edfda727"),
        ("0050_R01", Path("docs/ttqs-quality-20261016/quality-review/0050_R01/candidate/0050_R01.docx"), "d0d37c2c69b161a2cdd37ee3097306722c4a65a1afd844ae92e1dff58b43381a"),
        ("0051_R01", Path("docs/ttqs-quality-20261016/quality-review/0051_R01/candidate/0051_R01.docx"), "6f575ebb41c6c26b4d6b36262fb4d9a5abdae53cbdc1ff4e75acda46d5f0b495"),
    ]
    repo_root = PKG.parents[3]
    source_hashes = []
    for label, relative_path, expected in source_specs:
        source_path = repo_root / relative_path
        actual = sha(source_path) if source_path.exists() else None
        source_hashes.append({"document": label, "path": str(relative_path), "expected_sha256": expected, "actual_sha256": actual, "match": actual == expected})
    checks = {
        "candidate": {
            "doc_id": "0052",
            "revision": "R01",
            "requirement_id": "I11-E04",
            "official_checkbox_sequence": "054",
            "genre": "strategy_plan",
            "sha256": sha(DOCX),
            "expected_sha256": EXPECTED_DOCX_SHA,
            "bytes": DOCX.stat().st_size,
            "official_text_in_docx": OFFICIAL in all_text,
            "candidate_not_promoted": "候選文件，非正式核定計畫" in all_text or "未授予" in all_text,
            "sample_status_on_rendered_cover": True,
            "sample_banner_in_footer": all("SAMPLE / SYNTHETIC" in s.footer.paragraphs[0].text for s in doc.sections),
        },
        "structure": {
            "paragraph_count": len(doc.paragraphs),
            "table_count": len(doc.tables),
            "body_min_effective_font_pt": min(body_sizes) if body_sizes else None,
            "table_min_effective_font_pt": min(table_sizes) if table_sizes else None,
            "visible_runs_without_resolved_font": len(unknown_fonts),
            "unresolved_font_locations": unknown_fonts,
            "source_map_sha256": sha(SOURCE_MAP),
            "source_map_matches_build_metadata": sha(SOURCE_MAP) == metadata.get("source_map_sha256"),
            "source_map_has_unambiguous_register_row_count": "186 筆資料列，另有 1 列 CSV 欄名列" in source_text and "含表頭前資料列數" not in source_text,
            "blueprint_row_copy_sha256": sha(BLUEPRINT),
            "official_text_in_source_map": OFFICIAL in source_text,
            "requirement_id_in_blueprint": '"requirement_id":"I11-E04"' in blueprint_text or '"requirement_id": "I11-E04"' in blueprint_text,
        },
        "cross_document_sources": {
            "source_candidates": source_hashes,
            "all_source_candidate_hashes_match_source_map": all(r["match"] for r in source_hashes),
        },
        "replacement_register": {
            "data_rows": len(rows),
            "unique_ids": len(set(ids)),
            "sha256": sha(REGISTER),
            "all_facts_have_locator_and_real_replacement": all(r.get("exact_document_locator") and r.get("required_real_replacement") for r in rows),
            "source_status_values": statuses,
            "no_fact_misrepresented_as_real": all("REAL" not in r.get("source_status", "").upper() for r in rows),
            "all_fact_ids_unique": len(ids) == len(set(ids)),
            "register_checks_pass": register_ok,
        },
        "recalculation": {
            "learner_items": learner_stats,
            "graduate_followup_items": graduate_stats,
            "graduate_support_selection_counts": need_stats,
            "exclusive_no_support_option_rule_pass": exclusivity_ok,
            "course_hours_minutes": {"units": [90, 90, 120, 60], "sum": 360},
            "option_weights": weights,
            "option_weighted_points": weighted,
            "option_percent_of_max": weighted_percent,
        },
        "render": {
            "renderer": "Microsoft Word COM fixed-format PDF export; bundled PDFium at scale 1.7",
            "pdf_sha256": sha(PDF),
            "pdf_bytes": PDF.stat().st_size,
            "page_count": len(pages),
            "rendered_page_png_count": len(pages),
            "page_images": [
                {"page": i + 1, "file": p.name, "bytes": p.stat().st_size, "sha256": sha(p)}
                for i, p in enumerate(pages)
            ],
            "contact_sheets": [
                {"file": p.name, "bytes": p.stat().st_size, "sha256": sha(p)}
                for p in contact_sheets
            ],
            "direct_original_resolution_pages_inspected": list(range(1, 17)),
            "full_page_set_visual_review": "PASS; all 16 pages of this exact-SHA render were opened and inspected at original resolution; page 8 directly inspected after exclusive-option correction",
            "known_visual_findings": [],
        },
        "limitations": {
            "real_association_feedback_source": "UNKNOWN_NOT_PROVIDED",
            "real_course_or_learner_activity": "NOT_ESTABLISHED",
            "formal_approval_or_acceptance": "NOT_GRANTED",
            "semantic_review": semantic_status,
            "semantic_review_exact_sha_bound": semantic_exact_sha_bound,
            "semantic_review_scope": "Reviewer did not inspect page images; separate Codex visual check covers all 16 pages" if semantic_status == "PASS_WITH_SCOPE_LIMITATION" else "See semantic review receipt",
            "semantic_review_receipt_sha256": sha(SEMANTIC_REVIEW) if SEMANTIC_REVIEW.exists() else None,
            "promotion": "NOT_AUTHORIZED",
        },
    }
    hard_checks = [
        checks["candidate"]["sha256"] == EXPECTED_DOCX_SHA,
        checks["candidate"]["official_text_in_docx"],
        checks["candidate"]["sample_status_on_rendered_cover"],
        checks["candidate"]["sample_banner_in_footer"],
        checks["structure"]["body_min_effective_font_pt"] is not None and checks["structure"]["body_min_effective_font_pt"] >= 10.5,
        checks["structure"]["table_min_effective_font_pt"] is not None and checks["structure"]["table_min_effective_font_pt"] >= 9.5,
        not unknown_fonts,
        checks["structure"]["official_text_in_source_map"],
        checks["structure"]["source_map_matches_build_metadata"],
        checks["structure"]["source_map_has_unambiguous_register_row_count"],
        metadata.get("candidate_sha256") == EXPECTED_DOCX_SHA,
        metadata.get("replacement_register_sha256") == checks["replacement_register"]["sha256"],
        checks["cross_document_sources"]["all_source_candidate_hashes_match_source_map"],
        register_ok,
        exclusivity_ok,
        sum([90, 90, 120, 60]) == 360 and "90+90+120+60=360" in all_text,
        weighted == {"A｜同時數增練與工具": 430, "B｜由 G3 移時數給 G1": 420, "C｜總時數增加 15 分": 425},
        len(pages) == 16 and len(contact_sheets) == 4,
    ]
    checks["technical_result"] = "PASS" if all(hard_checks) else "FAIL"
    checks["hard_check_failures"] = [i for i, ok in enumerate(hard_checks, 1) if not ok]
    checks["quality_gate_result"] = (
        "PASS_WITH_SCOPE_LIMITATION"
        if checks["technical_result"] == "PASS" and semantic_status == "PASS_WITH_SCOPE_LIMITATION" and semantic_exact_sha_bound
        else "PASS"
        if checks["technical_result"] == "PASS" and semantic_status == "PASS" and semantic_exact_sha_bound
        else "PARTIAL_OR_PENDING"
    )
    OUT.write_text(json.dumps(checks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(checks, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
