from pathlib import Path
from io import BytesIO
from datetime import datetime, timezone
import hashlib, json, os, platform, re, subprocess, sys, zipfile
import xml.etree.ElementTree as ET

DEPS = Path(os.environ.get("TTQS_PYTHON_DOCX_DEPS", r"C:\Users\J\AppData\Local\Temp\ttqs_one_0034_r02_builddeps_20261118"))
if DEPS.is_dir():
    sys.path.insert(0, str(DEPS))
import docx
from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph
from docx.table import Table

REPO = Path(r"E:\tqrepo")
ROOT = REPO / r"docs\ttqs-quality-20261016\quality-review\0034_I07-E02_SOURCE_PREP_R01_20261118"
SOURCE_MD = ROOT / r"candidate\qa\scoped_repair_r02_rawls\0034_I07-E02_R02_SCOPED_REPAIR.md"
REPAIR_RECEIPT = ROOT / r"candidate\qa\scoped_repair_r02_rawls\0034_I07-E02_R02_SCOPED_REPAIR_RECEIPT.json"
SOURCE_PACKET = ROOT / "SOURCE_PACKET_0034_I07-E02_R01.md"
BLUEPRINT = ROOT / "UNIQUE_BLUEPRINT_0034_I07-E02_R01.md"
OUTPUT = ROOT / r"candidate\0034_I07-E02_R02_RAWLS_SCOPED_REPAIR.docx"
RECEIPT = ROOT / r"candidate\qa\build_r02\BUILD_RECEIPT_0034_I07-E02_R02.json"
SCRIPT = Path(__file__).resolve()
EXPECTED_BODY_SHA = "8782518402DD26018F7FF0934944DCDEF4350EA6A7CCB4F16E295760303413FF"
EXPECTED_PACKET_SHA = "60D822319476A457A5814318F3C96C50E60005792C20BD92F47E9F0DEB89C934"
EXPECTED_BLUEPRINT_SHA = "C5FB6EC1552714E18EB2FF3C0363DDC2C57C4A5D953CC1D261193A84EA320845"
EXPECTED_BRANCH = "work/ttqs-one-document-quality-contract-20261016"
EXPECTED_HEAD = "03348e7811dfe57a5b6e46efed1598b929db563d"
FONT = "Microsoft JhengHei"
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

def sha_bytes(data):
    return hashlib.sha256(data).hexdigest().upper()

def sha_file(path):
    return sha_bytes(Path(path).read_bytes())

def git_read(*args):
    p = subprocess.run(
        ["git", "-c", "safe.directory=E:/tqrepo", "-C", str(REPO), *args],
        capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    return p.returncode, p.stdout.strip(), p.stderr.strip()

git_rc, git_head, git_err = git_read("rev-parse", "HEAD")
branch_rc, branch, branch_err = git_read("branch", "--show-current")
git_ver_rc, git_version, git_ver_err = git_read("--version")
if (git_rc, branch_rc, git_head, branch) != (0, 0, EXPECTED_HEAD, EXPECTED_BRANCH):
    raise RuntimeError(f"checkout mismatch: head={git_head!r} branch={branch!r}; errors={git_err!r} {branch_err!r}")
if not all(p.is_file() for p in (SOURCE_MD, REPAIR_RECEIPT, SOURCE_PACKET, BLUEPRINT)):
    missing = [str(p) for p in (SOURCE_MD, REPAIR_RECEIPT, SOURCE_PACKET, BLUEPRINT) if not p.is_file()]
    raise FileNotFoundError("required input missing: " + ", ".join(missing))
if OUTPUT.exists() or RECEIPT.exists():
    raise FileExistsError(f"refusing to overwrite R02 output or receipt: {OUTPUT} ; {RECEIPT}")

body_bytes = SOURCE_MD.read_bytes()
body_sha = sha_bytes(body_bytes)
packet_sha = sha_file(SOURCE_PACKET)
blueprint_sha = sha_file(BLUEPRINT)
repair_receipt_bytes = REPAIR_RECEIPT.read_bytes()
repair_sha = sha_bytes(repair_receipt_bytes)
repair = json.loads(repair_receipt_bytes.decode("utf-8-sig"))
if body_sha != EXPECTED_BODY_SHA:
    raise RuntimeError(f"R02 Markdown SHA mismatch: {body_sha}")
if packet_sha != EXPECTED_PACKET_SHA:
    raise RuntimeError(f"source packet SHA mismatch: {packet_sha}")
if blueprint_sha != EXPECTED_BLUEPRINT_SHA:
    raise RuntimeError(f"unique Blueprint SHA mismatch: {blueprint_sha}")
if repair.get("output", {}).get("sha256", "").upper() != body_sha:
    raise RuntimeError("R02 repair receipt does not bind the Markdown body SHA")
if int(repair.get("output", {}).get("bytes", -1)) != len(body_bytes):
    raise RuntimeError("R02 repair receipt byte count does not match the Markdown body")
if repair.get("inputs", {}).get("source_packet", {}).get("sha256", "").upper() != packet_sha:
    raise RuntimeError("repair receipt source packet SHA mismatch")
if repair.get("inputs", {}).get("unique_blueprint", {}).get("sha256", "").upper() != blueprint_sha:
    raise RuntimeError("repair receipt unique Blueprint SHA mismatch")

body = body_bytes.decode("utf-8-sig")
CODE = chr(96)
INLINE_RE = re.compile(r"(\*\*.*?\*\*|" + CODE + r"[^" + CODE + r"]+" + CODE + r"|\*[^*]+\*)")

def inline_text(text):
    result = []
    for token in INLINE_RE.split(text):
        if not token:
            continue
        if token.startswith("**") and token.endswith("**"):
            result.append(token[2:-2])
        elif token.startswith(CODE) and token.endswith(CODE):
            result.append(token[1:-1])
        elif token.startswith("*") and token.endswith("*"):
            result.append(token[1:-1])
        else:
            result.append(token)
    return "".join(result).replace("<br>", "\n")

def join_md_lines(parts):
    if not parts:
        return ""
    out = parts[0].strip()
    previous_hard = parts[0].endswith("  ") or parts[0].rstrip().endswith("\\")
    if parts[0].rstrip().endswith("\\"):
        out = out[:-1].rstrip()
    for raw in parts[1:]:
        content = raw.strip()
        hard = raw.endswith("  ") or raw.rstrip().endswith("\\")
        if raw.rstrip().endswith("\\") and content.endswith("\\"):
            content = content[:-1].rstrip()
        out += ("\n" if previous_hard else " ") + content
        previous_hard = hard
    return out

def parse_cells(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    parts = re.split(r"(?<!\\)\|", s)
    return [part.strip().replace(r"\|", "|") for part in parts]

def is_separator(line):
    cells = parse_cells(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells)

def is_hr(s):
    return s in ("---", "***", "___")

def structural(line):
    s = line.strip()
    return (
        not s or is_hr(s) or s.startswith("|")
        or re.match(r"^#{1,6}\s+", s) is not None
        or re.match(r"^>\s+", s) is not None
        or re.match(r"^[-*+]\s+", s) is not None
        or re.match(r"^\d+[.)]\s+", s) is not None
    )

def parse_markdown(text):
    lines = text.splitlines()
    blocks = []
    i = 0
    while i < len(lines):
        raw = lines[i]
        s = raw.strip()
        if not s or is_hr(s):
            i += 1
            continue
        if s.startswith("|"):
            raw_rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                if not is_separator(lines[i]):
                    raw_rows.append(parse_cells(lines[i]))
                i += 1
            if raw_rows:
                columns = max(len(row) for row in raw_rows)
                rows = [row + [""] * (columns - len(row)) for row in raw_rows]
                blocks.append({"kind": "table", "rows": rows})
            continue
        heading = re.match(r"^(#{1,6})\s+(.*)$", s)
        if heading:
            blocks.append({"kind": "heading", "level": len(heading.group(1)), "text": heading.group(2)})
            i += 1
            continue
        if s.startswith("> "):
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith("> "):
                quote_lines.append(lines[i].strip()[2:])
                i += 1
            blocks.append({"kind": "quote", "text": join_md_lines(quote_lines)})
            continue
        bullet = re.match(r"^([-*+])\s+(.*)$", s)
        numbered = re.match(r"^(\d+[.)])\s+(.*)$", s)
        if bullet or numbered:
            match = bullet or numbered
            kind = "bullet" if bullet else "numbered"
            marker = match.group(1)
            parts = [match.group(2)]
            i += 1
            while i < len(lines) and lines[i].strip():
                next_line = lines[i]
                if structural(next_line):
                    break
                indent = len(next_line) - len(next_line.lstrip())
                if indent < 2:
                    break
                parts.append(next_line.strip())
                i += 1
            item = join_md_lines(parts)
            blocks.append({"kind": kind, "marker": marker, "text": item})
            continue
        paragraph_lines = [raw]
        i += 1
        while i < len(lines) and lines[i].strip() and not structural(lines[i]):
            paragraph_lines.append(lines[i])
            i += 1
        blocks.append({"kind": "paragraph", "text": join_md_lines(paragraph_lines)})
    return blocks

blocks = parse_markdown(body)
paragraph_blocks = [b for b in blocks if b["kind"] != "table"]
tables = [b for b in blocks if b["kind"] == "table"]
if not paragraph_blocks or not tables:
    raise RuntimeError(f"unexpected empty document structure: paragraphs={len(paragraph_blocks)} tables={len(tables)}")
source_table_row_counts = [len(t["rows"]) for t in tables]
if len(tables) != 7:
    raise RuntimeError(f"unexpected Markdown table count: {len(tables)}")
if sum(source_table_row_counts) != 64:
    raise RuntimeError(f"unexpected Markdown table data/header row count: {sum(source_table_row_counts)}")

def set_run_font(run, size_pt, bold=None, color=None, italic=None):
    run.font.name = FONT
    run.font.size = Pt(size_pt)
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.rFonts
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    rfonts.set(qn("w:eastAsia"), FONT)
    rfonts.set(qn("w:ascii"), FONT)
    rfonts.set(qn("w:hAnsi"), FONT)
    if bold is not None:
        run.bold = bold
    if color is not None:
        run.font.color.rgb = RGBColor(*color)
    if italic is not None:
        run.italic = italic

def shade(cell, fill):
    tcpr = cell._tc.get_or_add_tcPr()
    shd = tcpr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tcpr.append(shd)
    shd.set(qn("w:fill"), fill)

def cell_margins(cell, top=80, start=90, bottom=80, end=90):
    tcpr = cell._tc.get_or_add_tcPr()
    mar = tcpr.first_child_found_in("w:tcMar")
    if mar is None:
        mar = OxmlElement("w:tcMar")
        tcpr.append(mar)
    for name, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = mar.find(qn("w:" + name))
        if node is None:
            node = OxmlElement("w:" + name)
            mar.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")

def add_inline(paragraph, text, size_pt=11, bold=False, color=None):
    for token in INLINE_RE.split(text):
        if not token:
            continue
        is_bold = token.startswith("**") and token.endswith("**")
        is_code = token.startswith(CODE) and token.endswith(CODE)
        is_italic = token.startswith("*") and token.endswith("*") and not is_bold
        value = token[2:-2] if is_bold else (token[1:-1] if is_code or is_italic else token)
        pieces = value.split("<br>")
        for index, piece in enumerate(pieces):
            if index:
                paragraph.add_run().add_break()
            run = paragraph.add_run(piece)
            set_run_font(run, size_pt, bold=(bold or is_bold), color=color, italic=is_italic)
            if is_code:
                run.font.name = "Consolas"
                run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), FONT)

def add_page_field(paragraph):
    run = paragraph.add_run()
    set_run_font(run, 9)
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    separate = OxmlElement("w:fldChar")
    separate.set(qn("w:fldCharType"), "separate")
    cached = OxmlElement("w:t")
    cached.text = "1"
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    for element in (begin, instr, separate, cached, end):
        run._r.append(element)

doc = Document()
section = doc.sections[0]
section.orientation = WD_ORIENT.LANDSCAPE
section.page_width = Inches(11.69)
section.page_height = Inches(8.27)
section.top_margin = Inches(0.62)
section.bottom_margin = Inches(0.62)
section.left_margin = Inches(0.58)
section.right_margin = Inches(0.58)
section.header_distance = Inches(0.28)
section.footer_distance = Inches(0.28)
normal = doc.styles["Normal"]
normal.font.name = FONT
normal.font.size = Pt(11)
normal._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
normal.paragraph_format.space_after = Pt(5)
normal.paragraph_format.line_spacing = 1.08
for name, size in (("Title", 18), ("Heading 1", 15), ("Heading 2", 13), ("Heading 3", 12)):
    style = doc.styles[name]
    style.font.name = FONT
    style.font.size = Pt(size)
    style.font.bold = True
    style._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    style.font.color.rgb = RGBColor(31, 66, 110)
    style.paragraph_format.keep_with_next = True
    style.paragraph_format.space_before = Pt(9)
    style.paragraph_format.space_after = Pt(4)
header = section.header.paragraphs[0]
header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
add_inline(header, "TTQS ONE  |  0034 / I07-E02  |  CANDIDATE · SAMPLE/SYNTHETIC", 9, color=(85, 100, 120))
footer = section.footer.paragraphs[0]
footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
add_inline(footer, "TTQS ONE candidate  •  ", 9, color=(100, 100, 100))
add_page_field(footer)

for block in blocks:
    kind = block["kind"]
    if kind == "table":
        columns = max(len(row) for row in block["rows"])
        table = doc.add_table(rows=0, cols=columns)
        table.style = "Table Grid"
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = True
        for row_index, rowdata in enumerate(block["rows"]):
            cells = table.add_row().cells
            for col_index in range(columns):
                cell = cells[col_index]
                cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
                cell_margins(cell)
                para = cell.paragraphs[0]
                para.paragraph_format.space_after = Pt(0)
                para.paragraph_format.line_spacing = 1.0
                value = rowdata[col_index] if col_index < len(rowdata) else ""
                add_inline(para, value, size_pt=9.5, bold=(row_index == 0), color=(255, 255, 255) if row_index == 0 else None)
                if row_index == 0:
                    shade(cell, "24476B")
                elif row_index % 2 == 0:
                    shade(cell, "F2F6FA")
            trpr = table.rows[row_index]._tr.get_or_add_trPr()
            if row_index == 0:
                repeat = OxmlElement("w:tblHeader")
                repeat.set(qn("w:val"), "true")
                trpr.append(repeat)
            cant_split = OxmlElement("w:cantSplit")
            trpr.append(cant_split)
        continue
    if kind == "heading":
        level = block["level"]
        style_name = "Title" if level == 1 else f"Heading {min(level - 1, 3)}"
        size = 18 if level == 1 else (15 if level == 2 else (13 if level == 3 else 12))
        para = doc.add_paragraph(style=style_name)
        add_inline(para, block["text"], size_pt=size, bold=True, color=(31, 66, 110))
    elif kind == "bullet":
        para = doc.add_paragraph(style="List Bullet")
        para.paragraph_format.space_after = Pt(3)
        add_inline(para, block["text"], size_pt=11)
    elif kind == "numbered":
        para = doc.add_paragraph(style="Normal")
        para.paragraph_format.left_indent = Inches(0.28)
        para.paragraph_format.first_line_indent = Inches(-0.28)
        para.paragraph_format.space_after = Pt(3)
        add_inline(para, block["marker"] + " " + block["text"], size_pt=11)
    elif kind == "quote":
        para = doc.add_paragraph(style="Normal")
        para.paragraph_format.left_indent = Inches(0.25)
        para.paragraph_format.right_indent = Inches(0.2)
        add_inline(para, block["text"], size_pt=11, color=(70, 80, 95))
    else:
        para = doc.add_paragraph(style="Normal")
        add_inline(para, block["text"], size_pt=11)
        if len(block["text"]) > 180:
            para.paragraph_format.widow_control = True

def expected_sequence(parsed_blocks):
    sequence = []
    for block in parsed_blocks:
        if block["kind"] == "table":
            sequence.append({"type": "table", "rows": [[inline_text(cell) for cell in row] for row in block["rows"]]})
        else:
            text = inline_text(block["text"])
            if block["kind"] == "numbered":
                text = block["marker"] + " " + text
            sequence.append({"type": "paragraph", "text": text})
    return sequence

def actual_sequence(document):
    sequence = []
    for child in document.element.body.iterchildren():
        if child.tag == qn("w:p"):
            paragraph = Paragraph(child, document)
            if paragraph.text:
                sequence.append({"type": "paragraph", "text": paragraph.text})
        elif child.tag == qn("w:tbl"):
            table = Table(child, document)
            sequence.append({"type": "table", "rows": [[cell.text for cell in row.cells] for row in table.rows]})
    return sequence

def ooxml_font_audit(blob):
    with zipfile.ZipFile(BytesIO(blob)) as archive:
        xml = ET.fromstring(archive.read("word/document.xml"))
    body = xml.find(qn("w:body"))
    table_nodes = [child for child in body if child.tag == qn("w:tbl")]
    body_sizes = []
    table_sizes = []
    table_row_counts = []
    missing_body_sizes = 0
    missing_table_sizes = 0

    def collect(container, sink, missing_counter):
        missing = 0
        for run in container.iter(qn("w:r")):
            text_value = "".join(node.text or "" for node in run.iter(qn("w:t")))
            if not text_value:
                continue
            rpr = run.find(qn("w:rPr"))
            size_node = rpr.find(qn("w:sz")) if rpr is not None else None
            if size_node is None or not size_node.get(qn("w:val")):
                missing += 1
            else:
                sink.append(int(size_node.get(qn("w:val"))) / 2.0)
        return missing

    for child in body:
        if child.tag == qn("w:p"):
            missing_body_sizes += collect(child, body_sizes, missing_body_sizes)
        elif child.tag == qn("w:tbl"):
            table_row_counts.append(len(child.findall(qn("w:tr"))))
            missing_table_sizes += collect(child, table_sizes, missing_table_sizes)
    return {
        "table_count": len(table_nodes),
        "table_row_counts": table_row_counts,
        "body_min_pt": min(body_sizes) if body_sizes else None,
        "table_min_pt": min(table_sizes) if table_sizes else None,
        "body_text_run_count": len(body_sizes),
        "table_text_run_count": len(table_sizes),
        "body_text_runs_missing_explicit_size": missing_body_sizes,
        "table_text_runs_missing_explicit_size": missing_table_sizes,
    }

memory = BytesIO()
doc.save(memory)
docx_bytes = memory.getvalue()
in_memory_doc = Document(BytesIO(docx_bytes))
expected = expected_sequence(blocks)
actual = actual_sequence(in_memory_doc)
if expected != actual:
    mismatch = next((i for i, pair in enumerate(zip(expected, actual)) if pair[0] != pair[1]), min(len(expected), len(actual)))
    raise RuntimeError(f"Markdown-to-DOCX content sequence mismatch at block {mismatch}; expected_blocks={len(expected)} actual_blocks={len(actual)}")
font_audit = ooxml_font_audit(docx_bytes)
if font_audit["table_count"] != len(tables):
    raise RuntimeError(f"OOXML table count mismatch: {font_audit['table_count']} != {len(tables)}")
if font_audit["table_row_counts"] != source_table_row_counts:
    raise RuntimeError(f"OOXML table row counts mismatch: {font_audit['table_row_counts']} != {source_table_row_counts}")
if font_audit["body_text_runs_missing_explicit_size"] or font_audit["table_text_runs_missing_explicit_size"]:
    raise RuntimeError(f"OOXML has text runs without explicit font sizes: {font_audit}")
if font_audit["body_min_pt"] is None or font_audit["body_min_pt"] < 10.5:
    raise RuntimeError(f"body font below 10.5 pt: {font_audit}")
if font_audit["table_min_pt"] is None or font_audit["table_min_pt"] < 9.5:
    raise RuntimeError(f"table font below 9.5 pt: {font_audit}")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_bytes(docx_bytes)
if sha_file(OUTPUT) != sha_bytes(docx_bytes):
    raise RuntimeError("output SHA changed after write")
saved_doc = Document(str(OUTPUT))
if expected_sequence(blocks) != actual_sequence(saved_doc):
    raise RuntimeError("saved DOCX reopen content sequence mismatch")

def package_version(name):
    try:
        from importlib.metadata import version
        return version(name)
    except Exception:
        return "UNKNOWN"

def read_tool_version(command):
    try:
        p = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace")
        return {"exit_code": p.returncode, "output": (p.stdout + p.stderr).strip()}
    except Exception as exc:
        return {"error": repr(exc)}

script_sha = sha_file(SCRIPT)
receipt_data = {
    "receipt_type": "TTQS_ONE_BUILD_RECEIPT",
    "work_id": "TTQS_ONE_0034_I07-E02_BUILD_R02_DOCX_20261118",
    "doc_id": "0034",
    "requirement_id": "I07-E02",
    "revision": "R02",
    "status": "CANDIDATE_BUILD_COMPLETE_OOXML_CHECKS_ONLY",
    "built_at_utc": datetime.now(timezone.utc).isoformat(),
    "content_source": {
        "path": str(SOURCE_MD),
        "sha256": body_sha,
        "bytes": len(body_bytes),
        "rule": "Complete R02 Markdown supplies all body paragraphs and table cells; source packet and unique Blueprint are hash-bound metadata only; R01 body/DOCX not read."
    },
    "inputs": {
        "repair_receipt": {"path": str(REPAIR_RECEIPT), "sha256": repair_sha},
        "source_packet": {"path": str(SOURCE_PACKET), "sha256": packet_sha},
        "unique_blueprint": {"path": str(BLUEPRINT), "sha256": blueprint_sha}
    },
    "checkout": {
        "repo": str(REPO),
        "branch": branch,
        "head": git_head,
        "branch_expected": EXPECTED_BRANCH,
        "head_expected": EXPECTED_HEAD,
        "git_version": git_version
    },
    "builder": {
        "path": str(SCRIPT),
        "sha256": script_sha,
        "python_executable": sys.executable,
        "python_version": sys.version,
        "python_docx_version": docx.__version__,
        "python_docx_module": str(Path(docx.__file__).resolve()),
        "lxml_version": package_version("lxml"),
        "typing_extensions_version": package_version("typing_extensions"),
        "pip_version": read_tool_version([sys.executable, "-m", "pip", "--version"]),
        "powershell_version": os.environ.get("TTQS_POWERSHELL_VERSION", "NOT_CAPTURED"),
        "platform": platform.platform(),
        "dependency_install_scope": "task-specific temporary target directory; no global/repo package install",
        "dependency_target": str(DEPS)
    },
    "structure": {
        "source_lines": len(body.splitlines()),
        "content_paragraphs": len(paragraph_blocks),
        "headings": sum(1 for b in blocks if b["kind"] == "heading"),
        "list_items": sum(1 for b in blocks if b["kind"] in ("bullet", "numbered")),
        "blockquotes": sum(1 for b in blocks if b["kind"] == "quote"),
        "table_count": len(tables),
        "table_row_counts_including_header": source_table_row_counts,
        "total_table_rows_including_headers": sum(source_table_row_counts)
    },
    "preservation": {
        "source_blocks_preserved_in_order": True,
        "normalized_content_sequence_sha256": sha_bytes(json.dumps(expected, ensure_ascii=False, separators=(",", ":")).encode("utf-8")),
        "output_blocks": len(actual),
        "output_content_paragraphs": sum(1 for b in actual if b["type"] == "paragraph"),
        "output_table_count": sum(1 for b in actual if b["type"] == "table")
    },
    "ooxml_checks": {
        **font_audit,
        "body_min_required_pt": 10.5,
        "table_min_required_pt": 9.5,
        "body_font_check": "PASS",
        "table_font_check": "PASS",
        "paragraph_table_row_preservation_check": "PASS",
        "check_method": "direct w:sz values in word/document.xml"
    },
    "output": {
        "path": str(OUTPUT),
        "sha256": sha_file(OUTPUT),
        "bytes": OUTPUT.stat().st_size
    },
    "execution": {
        "process_exit_code": "CAPTURED_BY_POWERSHELL_WRAPPER",
        "stdout": "CAPTURED_BY_POWERSHELL_WRAPPER",
        "stderr": "CAPTURED_BY_POWERSHELL_WRAPPER"
    },
    "not_performed": {
        "word_com": True,
        "render": True,
        "visual_acceptance": True,
        "semantic_review": True,
        "promotion_or_current_update": True,
        "commit": True,
        "push": True
    },
    "formal_acceptance": "NOT_CLAIMED"
}
RECEIPT.parent.mkdir(parents=True, exist_ok=True)
RECEIPT.write_text(json.dumps(receipt_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({
    "status": receipt_data["status"],
    "output": str(OUTPUT),
    "output_sha256": receipt_data["output"]["sha256"],
    "output_bytes": receipt_data["output"]["bytes"],
    "source_sha256": body_sha,
    "builder_sha256": script_sha,
    "tables": font_audit["table_count"],
    "table_row_counts": font_audit["table_row_counts"],
    "content_paragraphs": len(paragraph_blocks),
    "body_min_pt": font_audit["body_min_pt"],
    "table_min_pt": font_audit["table_min_pt"]
}, ensure_ascii=False))
