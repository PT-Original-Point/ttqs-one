from pathlib import Path
import hashlib, os, tempfile, zipfile
from lxml import etree

R13 = Path(__file__).resolve().parents[1]
R12 = R13.parent / "0036_R12"
SOURCE = next((R12 / "candidate").glob("*.docx"))
TARGET = R13 / "candidate" / SOURCE.name.replace("_R12.docx", "_R13.docx")
EXPECTED_SOURCE_SHA = "e2be3928f96d45bdee6d18762b169c92e7817d10d0c0f87e4854bd16756febbb"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}

actual_source_sha = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
if actual_source_sha != EXPECTED_SOURCE_SHA:
    raise SystemExit(f"R12 source SHA mismatch: {actual_source_sha}")

with zipfile.ZipFile(SOURCE, "r") as zin:
    entries = [(info, zin.read(info.filename)) for info in zin.infolist()]
xml_name = "word/document.xml"
xml_data = next(data for info, data in entries if info.filename == xml_name)
tree = etree.fromstring(xml_data)
body = tree.find("w:body", NS)
tables = body.findall("w:tbl", NS)
if len(tables) != 38:
    raise SystemExit(f"Unexpected table count: {len(tables)}")

# Repeat the first row on both tables that continued without headers in R12.
for index in (28, 31):
    first_row = tables[index].find("w:tr", NS)
    if first_row is None:
        raise SystemExit(f"Missing first row in table {index}")
    trpr = first_row.find("w:trPr", NS)
    if trpr is None:
        trpr = etree.Element(f"{{{W}}}trPr")
        first_row.insert(0, trpr)
    if trpr.find("w:tblHeader", NS) is None:
        etree.SubElement(trpr, f"{{{W}}}tblHeader").set(f"{{{W}}}val", "true")

# Expand the blank direct-use handoff fields without adding or implying real data.
form = None
for paragraph in body.findall("w:p", NS):
    text = "".join(node.text or "" for node in paragraph.findall(".//w:t", NS))
    if "項目：" in text and "原件名稱及頁／表／欄位定位" in text and "暫停措施" in text:
        form = paragraph
        break
if form is None:
    raise SystemExit("Handoff form paragraph not found")
lines = [
    "逐項填寫，每個交接項目各一筆。",
    "項目：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿",
    "結果：□完成　□未完成",
    "核對日期：＿＿＿＿＿＿＿＿＿＿＿＿",
    "原件名稱及頁／表／欄位定位：",
    "＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿",
    "未完成時責任角色：＿＿＿＿＿＿＿＿＿＿　期限：＿＿＿＿＿＿＿＿",
    "暫停措施：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿",
    "未取得可核實原件或授權，不得勾選完成。本欄為空白格式，不代表協會已完成交接。",
]
ppr = form.find("w:pPr", NS)
old_run = form.find("w:r", NS)
old_rpr = old_run.find("w:rPr", NS) if old_run is not None else None
rpr_bytes = etree.tostring(old_rpr) if old_rpr is not None else None
for child in list(form):
    if child is not ppr:
        form.remove(child)
for i, line in enumerate(lines):
    run = etree.SubElement(form, f"{{{W}}}r")
    if rpr_bytes:
        run.append(etree.fromstring(rpr_bytes))
    text_node = etree.SubElement(run, f"{{{W}}}t")
    text_node.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    text_node.text = line
    if i != len(lines) - 1:
        etree.SubElement(run, f"{{{W}}}br").set(f"{{{W}}}type", "textWrapping")

# Remove the original standalone page-break paragraph before Appendix A-1.
# After enlarging the preceding form, Word can defer that empty break paragraph
# to its own page; natural flow keeps the appendix on the next content page.
paragraphs = body.findall("w:p", NS)
removed_break = False
for i, paragraph in enumerate(paragraphs[:-1]):
    text = "".join(node.text or "" for node in paragraph.findall(".//w:t", NS))
    breaks = paragraph.findall(".//w:br", NS)
    if text == "" and any(br.get(f"{{{W}}}type") == "page" for br in breaks):
        following_text = "".join(node.text or "" for node in paragraphs[i + 1].findall(".//w:t", NS))
        if following_text.startswith("附表 A-1"):
            paragraph.getparent().remove(paragraph)
            removed_break = True
            break
if not removed_break:
    raise SystemExit("Expected standalone page break before Appendix A-1 was not found")

new_xml = etree.tostring(tree, xml_declaration=True, encoding="UTF-8", standalone=True)
fd, temp_name = tempfile.mkstemp(dir=str(TARGET.parent), suffix=".tmp")
os.close(fd)
try:
    with zipfile.ZipFile(temp_name, "w") as zout:
        for info, data in entries:
            zout.writestr(info, new_xml if info.filename == xml_name else data)
    os.replace(temp_name, TARGET)
finally:
    if os.path.exists(temp_name):
        os.remove(temp_name)
with zipfile.ZipFile(TARGET) as check:
    if check.testzip() is not None:
        raise SystemExit("DOCX ZIP integrity failed")
print({"source_sha256": actual_source_sha, "candidate": str(TARGET), "candidate_sha256": hashlib.sha256(TARGET.read_bytes()).hexdigest(), "table_header_rows": [28, 31], "form_lines": len(lines), "removed_standalone_appendix_break": removed_break, "zip_test": "PASS"})

