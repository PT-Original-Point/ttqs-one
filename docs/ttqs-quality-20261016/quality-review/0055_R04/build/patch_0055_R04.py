#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bounded, reproducible R04 patch for TTQS_ONE document 0055.

Scope (see inputs/REVISION_PACKET_R04.md):
  * Inputs : inputs/0055_R03.docx  and
             inputs/SYNTHETIC_REPLACEMENT_REGISTER_0055_R03.csv
  * Outputs: candidate/0055_R04.docx
             evidence/SYNTHETIC_REPLACEMENT_REGISTER_0055_R04.csv
             evidence/patch_receipt_R04.json

Properties guaranteed by this script:
  * Python standard library only; fully deterministic (no timestamps, no RNG).
  * Fail closed on any input hash, anchor, or register-schema mismatch.
  * Refuses to overwrite any existing output.
  * Writes only inside this task directory.
  * Surgical ZIP/OOXML edit: only word/document.xml changes; every other
    package member is preserved byte-for-byte (decompressed content equal).
  * Inserts exactly one SAMPLE/SYNTHETIC tie-break paragraph immediately after
    the exact ranking-verification paragraph, cloning that paragraph's
    paragraph-properties and run-properties so formatting is preserved.
  * Updates only register row FAC-0055-010; preserves UTF-8/BOM, LF line
    endings, header, column order, exactly 52 data rows, and every other row
    and field byte-for-byte. evidence_status stays SYNTHETIC.
  * Emits a receipt with candidate_only=true and explicit QA-not-run flags.

This script does NOT claim any PASS, approval, real authority, or activity.

ASSUMPTION (confirmed by the dispatcher clarification for this task):
  The outer Chinese quotation marks 「 」 that wrap the proposed paragraph in
  REVISION_PACKET_R04.md are the packet's delimiters and are NOT part of the
  paragraph text. The inner 『 』 marks around the rubric labels ARE part of the
  text and are reproduced exactly.
"""

import csv
import hashlib
import io
import json
import os
import re
import sys
import zipfile

# --------------------------------------------------------------------------
# Static, verified constants
# --------------------------------------------------------------------------

TASK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IN_DOCX = os.path.join(TASK, "inputs", "0055_R03.docx")
IN_CSV = os.path.join(TASK, "inputs", "SYNTHETIC_REPLACEMENT_REGISTER_0055_R03.csv")

OUT_DOCX = os.path.join(TASK, "candidate", "0055_R04.docx")
OUT_CSV = os.path.join(TASK, "evidence", "SYNTHETIC_REPLACEMENT_REGISTER_0055_R04.csv")
OUT_RECEIPT = os.path.join(TASK, "evidence", "patch_receipt_R04.json")

BUILD_TMP_DOCX = OUT_DOCX + ".building"

EXPECTED_DOCX_SHA = "747218b1ac4deb1e4ffc49b788eabd095e04f0cae894e4491bd2822e93898f71"
EXPECTED_CSV_SHA = "a0f0dcfb67ce6097f54f2c662cc261886441b95c3f5b12ab7e8b700223c85c23"

# Declared upstream provenance (from REVISION_PACKET_R04.md; not re-read here).
DECLARED_BLUEPRINT = {
    "path": "inputs/UNIQUE_BLUEPRINT_0055_R02.md",
    "sha256": "e255a2397b47868e3c0a740320bda0bd022b9e540f7adeb7211f66d32840c45b",
}
DECLARED_SOURCE_MAP = {
    "path": "inputs/SOURCE_MAP_R02.md",
    "sha256": "4dc7807d921848e3b47f5d1d28eb06e99124fdb32ef0c26286fc6ca4348b37c4",
}

# Exact ranking-verification paragraph text (section 7) present in R03.
ANCHOR_TEXT = (
    "排序核對：C-03 87.6 > C-01 82.6 > C-02 81.0。"
    "各候選的專業內容正確性、教學示範與引導、成人志工適配與可近性，"
    "以及個資、角色與安全界線均達示例門檻；"
    "若真實原件或權限有任何一項無法核驗，該候選立即 HOLD，不因排序高而例外。"
)

# Exact paragraph to insert immediately after ANCHOR_TEXT.
# The outer 「 」 from the packet are delimiters and are excluded;
# the inner 『 』 marks are content and are kept verbatim.
INSERT_TEXT = (
    "同分處理（SAMPLE / SYNTHETIC，提案規則）："
    "若加權總分相同，先比較『專業內容正確性』加權點數，"
    "再比較『教學示範與引導』加權點數；"
    "仍同分時，安排相同題目、準備時間、時長及量尺的第二次試教，記錄評審觀察與分數。"
    "若仍同分，或無法核實具權限者與已核定的後續規則，立即 HOLD，"
    "依真實章程與授權處理，不另創規則。"
    "本例三組加權總分互異，未觸發此程序。"
    "此提案須由具權限者核定後始得正式採用。"
)

DOCUMENT_XML_MEMBER = "word/document.xml"

# --------------------------------------------------------------------------
# Register schema and the single permitted row delta
# --------------------------------------------------------------------------

CSV_COLUMNS = [
    "register_id",
    "fact_id",
    "case_id",
    "doc_id",
    "docx_locator",
    "synthetic_value_or_field",
    "assumption_rationale",
    "cross_doc_reference",
    "real_source_to_obtain",
    "responsible_verifier",
    "evidence_status",
    "hold_condition",
]

EXPECTED_DATA_ROWS = 52
TARGET_ROW_ID = "FAC-0055-010"

OLD_ROW = (
    "FAC-0055-010",
    "FAC-0055-010",
    "SYN-0033-PLAN-01",
    "0055",
    "第 4 節量尺表「權重」欄；第 7 節各候選分解表「權重%」欄",
    "合成評選權重 25/25/20/20/10",
    "示範可重算的加權量尺，權重合計 100%",
    "無（本件新增合成，無跨文件事實引用）",
    "正式核定遴選辦法",
    "權責主管／委員會",
    "SYNTHETIC",
    "未核定不得用於正式遴選",
)

NEW_ROW = (
    "FAC-0055-010",
    "FAC-0055-010",
    "SYN-0033-PLAN-01",
    "0055",
    "第 4 節量尺表「權重」欄；第 7 節排序核對與同分處理。",
    "合成評選權重 25/25/20/20/10；同分處理（未核定 SAMPLE／SYNTHETIC 提案）："
    "加權總分相同時，先比較『專業內容正確性』加權點數，再比較『教學示範與引導』加權點數；"
    "仍同分時，安排相同題目、準備時間、時長及量尺的第二次試教，記錄評審觀察與分數；"
    "仍同分或無法核實具權限者與已核定之後續規則，即 HOLD，依真實章程與授權處理。",
    "示範事前公告、可重算的遴選與同分處理程序；非協會已核定採用之政策。",
    "無（本件新增合成，無跨文件事實引用）",
    "權責治理單位與正式核定之遴選辦法，以及（如使用）第二次試教評分表。",
    "權限經核實後之具權限者／權責單位。",
    "SYNTHETIC",
    "權限與同分規則核定前不得正式使用；已觸發但缺證據或權限即 HOLD。",
)


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: str) -> str:
    with open(path, "rb") as fh:
        return sha256_bytes(fh.read())


def fail(message: str):
    raise RuntimeError("PATCH0055R04_FAIL: " + message)


def require(condition: bool, message: str):
    if not condition:
        fail(message)


def xml_escape_text(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def assert_within_task(path: str):
    task = os.path.realpath(TASK)
    target = os.path.realpath(path)
    if target != task and not target.startswith(task + os.sep):
        fail("output escapes task directory: " + target)


def require_absent(path: str):
    if os.path.exists(path):
        fail("refusing to overwrite existing path: " + os.path.relpath(path, TASK))


# --------------------------------------------------------------------------
# DOCX build
# --------------------------------------------------------------------------

PARA_OPEN_RE = re.compile(rb"<w:p(?: [^>]*)?>")


def build_candidate_docx():
    """Return (candidate_bytes, changed_members) for the patched DOCX."""
    require(os.path.isfile(IN_DOCX), "missing input DOCX: " + IN_DOCX)
    actual_sha = sha256_file(IN_DOCX)
    require(
        actual_sha == EXPECTED_DOCX_SHA,
        "DOCX hash mismatch: expected %s got %s" % (EXPECTED_DOCX_SHA, actual_sha),
    )

    with zipfile.ZipFile(IN_DOCX, "r") as zin:
        if zin.testzip() is not None:
            fail("input DOCX is not a valid ZIP archive")
        names = zin.namelist()
        require(DOCUMENT_XML_MEMBER in names, "document.xml member missing")
        require(
            names.count(DOCUMENT_XML_MEMBER) == 1,
            "document.xml must appear exactly once in the package",
        )
        src_members = {n: zin.read(n) for n in names}
        src_infos = zin.infolist()

    src_xml = src_members[DOCUMENT_XML_MEMBER]

    anchor_bytes = xml_escape_text(ANCHOR_TEXT).encode("utf-8")
    require(
        src_xml.count(anchor_bytes) == 1,
        "ranking-verification anchor must occur exactly once in document.xml",
    )

    anchor_pos = src_xml.find(anchor_bytes)

    # Enclosing <w:p> ... </w:p>
    open_matches = [m for m in PARA_OPEN_RE.finditer(src_xml, 0, anchor_pos + 1)]
    require(open_matches, "could not locate enclosing paragraph open tag")
    p_start = open_matches[-1].start()
    p_end = src_xml.find(b"</w:p>", anchor_pos)
    require(p_end != -1, "could not locate enclosing paragraph close tag")
    p_end += len(b"</w:p>")

    para = src_xml[p_start:p_end]
    require(
        PARA_OPEN_RE.match(para) is not None and para.endswith(b"</w:p>"),
        "anchor paragraph is not a single well-formed <w:p>",
    )

    # Clone paragraph properties.
    pps = para.find(b"<w:pPr>")
    require(pps != -1, "anchor paragraph has no <w:pPr> to clone")
    ppe = para.find(b"</w:pPr>", pps)
    require(ppe != -1, "anchor <w:pPr> is malformed")
    ppe += len(b"</w:pPr>")
    ppr = para[pps:ppe]

    # Clone the run properties of the anchor run.
    rrs = para.find(b"<w:rPr>", ppe)
    require(rrs != -1, "anchor run has no <w:rPr> to clone")
    rre = para.find(b"</w:rPr>", rrs)
    require(rre != -1, "anchor <w:rPr> is malformed")
    rre += len(b"</w:rPr>")
    rpr = para[rrs:rre]

    insert_bytes = xml_escape_text(INSERT_TEXT).encode("utf-8")
    new_para = (
        b"<w:p>" + ppr + b"<w:r>" + rpr + b"<w:t>" + insert_bytes + b"</w:t></w:r></w:p>"
    )

    dst_xml = src_xml[:p_end] + new_para + src_xml[p_end:]

    # Prove the edit is exactly the insertion of one paragraph.
    require(dst_xml[:p_end] == src_xml[:p_end], "unexpected change before insertion point")
    tail_off = p_end + len(new_para)
    require(dst_xml[tail_off:] == src_xml[p_end:], "unexpected change after insertion point")
    require(dst_xml.count(anchor_bytes) == 1, "anchor text no longer unique after edit")
    require(dst_xml.count(insert_bytes) == 1, "inserted text must occur exactly once")
    require(
        len(PARA_OPEN_RE.findall(new_para)) == 1,
        "inserted block must contain exactly one paragraph",
    )
    require(
        len(PARA_OPEN_RE.findall(dst_xml))
        == len(PARA_OPEN_RE.findall(src_xml)) + 1,
        "exactly one paragraph must have been added",
    )

    # Rebuild the package preserving every ZipInfo (order, dates, attrs).
    require_absent(OUT_DOCX)
    require_absent(BUILD_TMP_DOCX)
    os.makedirs(os.path.dirname(OUT_DOCX), exist_ok=True)

    with zipfile.ZipFile(BUILD_TMP_DOCX, "w", zipfile.ZIP_DEFLATED) as zout:
        for info in src_infos:
            data = src_members[info.filename]
            if info.filename == DOCUMENT_XML_MEMBER:
                data = dst_xml
            zout.writestr(info, data)

    # Verify the produced package.
    with zipfile.ZipFile(BUILD_TMP_DOCX, "r") as znew:
        require(znew.testzip() is None, "candidate DOCX failed Zip integrity test")
        require(znew.namelist() == names, "package member order/list changed")
        new_members = {n: znew.read(n) for n in znew.namelist()}

    changed = sorted(n for n in names if new_members[n] != src_members[n])
    require(
        changed == [DOCUMENT_XML_MEMBER],
        "only word/document.xml may change, changed=%r" % (changed,),
    )
    require(new_members[DOCUMENT_XML_MEMBER] == dst_xml, "candidate document.xml differs")

    candidate_bytes = open(BUILD_TMP_DOCX, "rb").read()
    kept = len(names) - 1
    os.remove(BUILD_TMP_DOCX)
    return candidate_bytes, kept


# --------------------------------------------------------------------------
# CSV build
# --------------------------------------------------------------------------

def build_candidate_csv():
    """Return (candidate_bytes, target_row_dict) for the patched register."""
    require(os.path.isfile(IN_CSV), "missing input CSV: " + IN_CSV)
    actual_sha = sha256_file(IN_CSV)
    require(
        actual_sha == EXPECTED_CSV_SHA,
        "CSV hash mismatch: expected %s got %s" % (EXPECTED_CSV_SHA, actual_sha),
    )

    raw = open(IN_CSV, "rb").read()
    require(raw.startswith(b"\xef\xbb\xbf"), "register must start with a UTF-8 BOM")
    require(b"\r" not in raw, "register must use LF line endings only")
    require(raw.endswith(b"\n"), "register must end with a newline")

    text = raw.decode("utf-8-sig")
    parsed = list(csv.reader(io.StringIO(text)))
    require(
        len(parsed) == EXPECTED_DATA_ROWS + 1,
        "register must hold 1 header + %d data rows, got %d"
        % (EXPECTED_DATA_ROWS, len(parsed)),
    )
    require(list(parsed[0]) == CSV_COLUMNS, "register header/column order changed")
    for idx, row in enumerate(parsed[1:], start=1):
        require(len(row) == len(CSV_COLUMNS), "row %d has %d fields" % (idx, len(row)))

    matches = [r for r in parsed[1:] if r and r[0] == TARGET_ROW_ID]
    require(len(matches) == 1, "target register row %s must be unique" % TARGET_ROW_ID)
    require(
        tuple(matches[0]) == OLD_ROW,
        "target register row does not match the expected R03 content",
    )

    # Byte-level replacement so every other line stays byte-for-byte identical.
    lines = raw.split(b"\n")
    require(lines[-1] == b"", "register must end with a single trailing newline")
    lines = lines[:-1]
    require(
        len(lines) == EXPECTED_DATA_ROWS + 1,
        "unexpected physical line count in register",
    )

    old_row_bytes = ",".join(OLD_ROW).encode("utf-8")
    new_row_bytes = ",".join(NEW_ROW).encode("utf-8")
    require(
        old_row_bytes.count(b'"') == 0 and old_row_bytes.count(b",") == len(CSV_COLUMNS) - 1,
        "unexpected quoting/commas in expected old row",
    )
    require(
        new_row_bytes.count(b'"') == 0
        and new_row_bytes.count(b",") == len(CSV_COLUMNS) - 1,
        "new row must contain exactly %d commas and no quotes"
        % (len(CSV_COLUMNS) - 1),
    )

    hit_indexes = [i for i, ln in enumerate(lines) if ln == old_row_bytes]
    require(
        len(hit_indexes) == 1,
        "expected exactly one byte-identical target row, found %d" % len(hit_indexes),
    )
    target_idx = hit_indexes[0]

    new_lines = list(lines)
    new_lines[target_idx] = new_row_bytes
    new_raw = b"\n".join(new_lines) + b"\n"

    # Prove nothing but the single target row changed.
    require(new_raw.startswith(b"\xef\xbb\xbf"), "candidate lost the UTF-8 BOM")
    require(b"\r" not in new_raw, "candidate must not introduce CR bytes")
    require(
        new_raw.count(b"\n") == EXPECTED_DATA_ROWS + 1,
        "candidate line count changed",
    )
    for i, (a, b) in enumerate(zip(lines, new_lines)):
        if i != target_idx:
            require(a == b, "unexpected byte change on register line %d" % i)
    require(len(new_raw) != len(raw), "candidate register must differ from R03")

    new_parsed = list(csv.reader(io.StringIO(new_raw.decode("utf-8-sig"))))
    require(len(new_parsed) == EXPECTED_DATA_ROWS + 1, "candidate row count changed")
    new_target = [r for r in new_parsed[1:] if r and r[0] == TARGET_ROW_ID]
    require(len(new_target) == 1, "candidate target row not unique")
    require(tuple(new_target[0]) == NEW_ROW, "candidate target row content mismatch")
    require(
        new_target[0][CSV_COLUMNS.index("evidence_status")] == "SYNTHETIC",
        "evidence_status must remain SYNTHETIC",
    )

    row_dict_before = dict(zip(CSV_COLUMNS, OLD_ROW))
    row_dict_after = dict(zip(CSV_COLUMNS, NEW_ROW))
    return new_raw, row_dict_before, row_dict_after


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    for path in (OUT_DOCX, OUT_CSV, OUT_RECEIPT):
        assert_within_task(path)
        require_absent(path)

    docx_bytes, kept_members = build_candidate_docx()
    csv_bytes, row_before, row_after = build_candidate_csv()

    require_absent(OUT_DOCX)
    with open(OUT_DOCX, "wb") as fh:
        fh.write(docx_bytes)

    require_absent(OUT_CSV)
    os.makedirs(os.path.dirname(OUT_CSV), exist_ok=True)
    with open(OUT_CSV, "wb") as fh:
        fh.write(csv_bytes)

    candidate_docx_sha = sha256_bytes(docx_bytes)
    candidate_csv_sha = sha256_bytes(csv_bytes)

    receipt = {
        "project_id": "TTQS_ONE",
        "document_id": "0055",
        "revision": "R04",
        "status": "SAMPLE_SYNTHETIC_CANDIDATE_ONLY",
        "candidate_only": True,
        "official_requirement_id": "I12-E03",
        "official_evidence_table_location": "page 4, indicator 12c",
        "official_checkbox_sequence": "058",
        "builder": "opencode-v2-writer",
        "role": "BUILD_OWNER (isolated candidate; no acceptance authority)",
        # --- explicit QA-not-run / safety flags ---
        "qa_not_run": True,
        "static_qa_run": False,
        "technical_layout_qa_run": False,
        "layout_qa_run": False,
        "visual_qa_run": False,
        "semantic_qa_run": False,
        "review_run": False,
        "pdf_png_render_run": False,
        "word_com_run": False,
        "pass_claim": False,
        "approval_claim": False,
        "real_authority_claim": False,
        "actual_activity_claim": False,
        "human_acceptance": "NOT_GRANTED",
        # --- exact hashes ---
        "predecessor_docx_path": os.path.relpath(IN_DOCX, TASK).replace(os.sep, "/"),
        "predecessor_docx_sha256": EXPECTED_DOCX_SHA,
        "candidate_docx_path": os.path.relpath(OUT_DOCX, TASK).replace(os.sep, "/"),
        "candidate_docx_sha256": candidate_docx_sha,
        "predecessor_register_path": os.path.relpath(IN_CSV, TASK).replace(os.sep, "/"),
        "predecessor_register_sha256": EXPECTED_CSV_SHA,
        "candidate_register_path": os.path.relpath(OUT_CSV, TASK).replace(os.sep, "/"),
        "candidate_register_sha256": candidate_csv_sha,
        "declared_upstream": {
            "unique_blueprint": DECLARED_BLUEPRINT,
            "source_map": DECLARED_SOURCE_MAP,
        },
        # --- changed members / row ---
        "docx_changed_package_members": [DOCUMENT_XML_MEMBER],
        "docx_unchanged_package_members_count": kept_members,
        "csv_changed_row_id": TARGET_ROW_ID,
        "csv_data_row_count": EXPECTED_DATA_ROWS,
        "csv_column_count": len(CSV_COLUMNS),
        # --- the change itself ---
        "insertion_locator": "Section 7 ranking check (immediately after ranking-verification paragraph)",
        "anchor_text": ANCHOR_TEXT,
        "inserted_text": INSERT_TEXT,
        "inserted_text_note": (
            "Outer packet quotation marks excluded as delimiters; inner rubric-label "
            "marks reproduced verbatim."
        ),
        "register_row_before": row_before,
        "register_row_after": row_after,
        "ooxml_edit": (
            "Only word/document.xml changed: one <w:p> (cloned pPr + cloned rPr) inserted "
            "immediately after the ranking-verification paragraph; every other ZIP member "
            "kept byte-for-byte (decompressed content identical, member order preserved)."
        ),
        "csv_edit": (
            "Only row FAC-0055-010 replaced; UTF-8 BOM, LF line endings, header, column "
            "order, all 52 data rows and all other bytes preserved."
        ),
        "synthetic_status_of_change": "SAMPLE/SYNTHETIC, unapproved proposed rule",
    }

    receipt_bytes = (json.dumps(receipt, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    require_absent(OUT_RECEIPT)
    with open(OUT_RECEIPT, "wb") as fh:
        fh.write(receipt_bytes)

    sys.stdout.write(receipt_bytes.decode("utf-8"))


if __name__ == "__main__":
    main()
