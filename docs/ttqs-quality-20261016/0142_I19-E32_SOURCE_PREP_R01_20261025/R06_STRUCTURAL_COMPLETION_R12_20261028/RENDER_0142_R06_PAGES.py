from pathlib import Path
from pypdfium2 import PdfDocument
from PIL import Image, ImageDraw
import hashlib,json
root=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0142_I19-E32_SOURCE_PREP_R01_20261025\R06_STRUCTURAL_COMPLETION_R12_20261028")
pdf=root/"R06_REVIEW"/"0142_I19-E32_R06_WordNative.pdf"
docx=root/"0142_I19-E32_CANDIDATE_R06.docx"
pages_dir=root/"R06_REVIEW"/"pages"
sheets_dir=root/"R06_REVIEW"/"contact_sheets"
pages_dir.mkdir(parents=True,exist_ok=True); sheets_dir.mkdir(parents=True,exist_ok=True)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
doc=PdfDocument(str(pdf)); rows=[]; imgs=[]
for i,page in enumerate(doc):
    img=page.render(scale=1.6666667).to_pil().convert("RGB")
    out=pages_dir/f"page-{i+1:02d}.png"; img.save(out,format="PNG",optimize=True)
    rows.append({"page":i+1,"file":out.name,"sha256":sha(out),"bytes":out.stat().st_size,"width":img.width,"height":img.height})
    imgs.append(img.copy()); page.close()
doc.close(); sheets=[]
for start in range(0,len(imgs),3):
    batch=imgs[start:start+3]; thumbs=[]
    for im in batch:
        w=720; thumbs.append(im.resize((w,round(im.height*w/im.width))))
    margin=24; canvas=Image.new("RGB",(max(x.width for x in thumbs)+margin*2,sum(x.height for x in thumbs)+margin*(len(thumbs)+1)),"white")
    y=margin; draw=ImageDraw.Draw(canvas)
    for j,im in enumerate(thumbs):
        canvas.paste(im,(margin,y)); draw.text((margin+8,y+8),f"PAGE {start+j+1}",fill="red"); y+=im.height+margin
    out=sheets_dir/f"contact-{start//3+1:02d}.jpg"; canvas.save(out,format="JPEG",quality=90,optimize=True)
    sheets.append({"file":out.name,"sha256":sha(out),"bytes":out.stat().st_size})
manifest={"doc_id":"0142","requirement_id":"I19-E32","candidate_sha256":sha(docx),"pdf_sha256":sha(pdf),"page_count":len(rows),"render":"Microsoft Word PDF at 120 dpi","pages":rows,"contact_sheets":sheets}
out=root/"R06_REVIEW"/"PAGE_IMAGE_MANIFEST_0142_R06.json"; out.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"page_count":len(rows),"manifest":str(out),"manifest_sha256":sha(out),"sheets":[str(sheets_dir/s["file"]) for s in sheets],"pages":[str(pages_dir/r["file"]) for r in rows]},ensure_ascii=False))
