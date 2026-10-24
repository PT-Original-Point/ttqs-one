from pathlib import Path
import json, re, hashlib
from docx import Documen
from pypdf import PdfReader
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "candidate" / "0134__會員人數及會費收入逐年變化分析報告_R01.docx"
PDF = ROOT / "render" / "word_native_R06" / "0134_R01_WordNative.pdf"
PAGES = ROOT / "render" / "word_native_R06"
QA = ROOT / "qa"

doc = Document(DOCX)
paras = [p.text for p in doc.paragraphs if p.text.strip()]
tables = []
for t in doc.tables:
    tables.append([[c.text.replace("\n", " / ") for c in row.cells] for row in t.rows])
body_text = "\n".join(paras + ["\n".join(" | ".join(row) for row in t) for t in tables])
assert "會員人數及會費收入均逐年增加。" in body_tex
assert "SAMPLE／SYNTHETIC" in body_tex
assert "UNKNOWN" in body_text and "NOT_GRANTED" in body_tex
assert "0133" in body_text and "0135" in body_tex
assert "42" in body_text and "48" in body_text and "54" in body_tex
assert "102,000" in body_text and "111,000" in body_text and "126,000" in body_tex
assert "30＋7－1＝36" in body_text and "36＋6－2＝40" in body_tex
assert "SYN-0134-055" in body_tex
assert not re.search(r"表\s+[0-9]+", body_text), "Stale or unbound table number reference found"

body_sizes, table_sizes = [], []
for p in doc.paragraphs:
    if p.text.strip():
        for r in p.runs:
            if r.text.strip():
                body_sizes.append(r.font.size.pt if r.font.size else doc.styles[p.style.name].font.size.pt if doc.styles[p.style.name].font.size else 10.5)
for t in doc.tables:
    for row in t.rows:
        for cell in row.cells:
            for p in cell.paragraphs:
                for r in p.runs:
                    if r.text.strip():
                        table_sizes.append(r.font.size.pt if r.font.size else 10.5)
assert body_sizes and min(body_sizes) >= 10.5, f"body minimum font={min(body_sizes) if body_sizes else 'none'}"
assert table_sizes and min(table_sizes) >= 9.5, f"table minimum font={min(table_sizes) if table_sizes else 'none'}"
assert len(tables) >= 20, f"expected detailed report tables, got {len(tables)}"
register = next((t for t in tables if t and t[0][0] == "Register key"), None)
assert register is not None and len(register) == 56, f"replacement register rows={len(register)-1 if register else 'missing'}"
for t in doc.tables:
    assert t.rows[0]._tr.trPr is not None and t.rows[0]._tr.trPr.find("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tblHeader") is not None

docx_sha = hashlib.sha256(DOCX.read_bytes()).hexdigest()
pdf_sha = hashlib.sha256(PDF.read_bytes()).hexdigest()
page_count = len(PdfReader(str(PDF)).pages)
page_images = sorted(PAGES.glob("page-*.png"))
assert len(page_images) == page_count, f"PNG pages={len(page_images)} PDF pages={page_count}"

# Make four labeled contact sheets; every Word-native page is included once.
for ix in range(0, len(page_images), 5):
    group = page_images[ix:ix+5]
    thumb_w, thumb_h, label_h, gap, cols = 530, 685, 34, 24, 2
    rows = (len(group) + cols - 1) // cols
    sheet = Image.new("RGB", (cols*thumb_w+(cols+1)*gap, rows*(thumb_h+label_h)+(rows+1)*gap), "#e5e9ec")
    draw = ImageDraw.Draw(sheet)
    for j, path in enumerate(group):
        im = Image.open(path).convert("RGB")
        im.thumbnail((thumb_w, thumb_h))
        x = gap + (j % cols)*(thumb_w+gap) + (thumb_w-im.width)//2
        y = gap + (j // cols)*(thumb_h+label_h+gap) + label_h
        sheet.paste(im, (x,y))
        draw.text((gap + (j % cols)*(thumb_w+gap), y-label_h+8), f"Page {ix+j+1}", fill="#1d2830")
    sheet.save(QA / f"contact_{ix+1:02d}_{ix+len(group):02d}.png")

receipt = {
    "doc_id":"0134", "requirement_id":"I19-E23", "status":"CANDIDATE",
    "docx_path":str(DOCX), "docx_sha256":docx_sha,
    "word_native_pdf_path":str(PDF), "word_native_pdf_sha256":pdf_sha,
    "word_native_pdf_pages":page_count, "rendered_page_png_count":len(page_images),
    "paragraph_count":len(paras), "table_count":len(tables),
    "replacement_register_rows":len(register)-1,
    "body_min_font_pt":min(body_sizes), "table_min_font_pt":min(table_sizes),
    "math_checks":{
      "member_counts":[42,48,54], "member_yoy_pct":[14.3,12.5],
      "sample_net_receipts":[102000,111000,126000], "net_receipt_yoy_pct":[8.8,13.5],
      "2024_membership_rollforward":"42+10-4=48", "2025_membership_rollforward":"48+10-4=54",
      "2024_member_fee_cash_reconciliation":"34*3000+8*1500-3000=111000",
      "2025_member_fee_cash_reconciliation":"38*3000+9*1500-1500=126000"
    },
    "sample_real_boundary":"SAMPLE/SYNTHETIC throughout; REAL source records UNKNOWN",
    "semantic_review":"PENDING independent exact-SHA review",
    "formal_acceptance":"NOT_GRANTED"
}
(QA / "TECHNICAL_QA_0134_R01.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False, indent=2))
