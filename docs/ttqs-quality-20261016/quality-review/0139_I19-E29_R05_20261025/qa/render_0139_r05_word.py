from pathlib import Path
from hashlib import sha256
from datetime import datetime
import json, gc, time
import pythoncom
import win32com.client
import win32process
import pypdfium2 as pdfium

folder=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0139_I19-E29_CANDIDATE_R05_20261025")
docx=folder/"0139__證照通過率與就業率跨年度改善分析報告.docx"
out=folder/"render_word_native"
out.mkdir(exist_ok=True)
pdf=out/"0139_word_native.pdf"
before=sha256(docx.read_bytes()).hexdigest()
pythoncom.CoInitialize()
app=None
doc=None
pid=None
word_version=None
try:
    app=win32com.client.DispatchEx("Word.Application")
    app.Visible=False
    app.DisplayAlerts=0
    app.ScreenUpdating=False
    try:
        app.AutomationSecurity=3
    except Exception:
        pass
    word_version=str(app.Version)
    try:
        pid=win32process.GetWindowThreadProcessId(int(app.Hwnd))[1]
    except Exception:
        pid=None
    doc=app.Documents.Open(FileName=str(docx), ConfirmConversions=False, ReadOnly=True, AddToRecentFiles=False, Visible=False, OpenAndRepair=False, NoEncodingDialog=True)
    doc.ExportAsFixedFormat(OutputFileName=str(pdf),ExportFormat=17,OpenAfterExport=False,OptimizeFor=0,Range=0,From=1,To=1,Item=0,IncludeDocProps=True,KeepIRM=True,CreateBookmarks=1,DocStructureTags=True,BitmapMissingFonts=True,UseISO19005_1=False)
finally:
    if doc is not None:
        try: doc.Close(SaveChanges=0)
        except Exception: pass
    if app is not None:
        try: app.Quit(SaveChanges=0)
        except Exception: pass
    doc=None
    app=None
    gc.collect()
    pythoncom.CoUninitialize()
time.sleep(2)
after=sha256(docx.read_bytes()).hexdigest()
if before!=after: raise RuntimeError("DOCX bytes changed during native rendering")
if not pdf.is_file(): raise RuntimeError("Word did not create PDF")
pdfdoc=pdfium.PdfDocument(str(pdf))
for p in out.glob("page-*.png"): p.unlink()
for i,page in enumerate(pdfdoc,1):
    image=page.render(scale=1.65).to_pil()
    image.save(out/f"page-{i:02d}.png")
receipt={
 "renderer":"Microsoft Word COM ExportAsFixedFormat; pypdfium2 raster",
 "word_version":word_version,"word_com_process_id":pid,"word_visible":False,
 "candidate_docx_sha256_before":before,"candidate_docx_sha256_after":after,
 "pdf_path":str(pdf),"pdf_bytes":pdf.stat().st_size,"pdf_sha256":sha256(pdf.read_bytes()).hexdigest(),
 "page_count":len(pdfdoc),"raster_scale":1.65,"png_count":len(list(out.glob("page-*.png"))),
 "created_local":datetime.now().astimezone().isoformat(),"visual_review":"PENDING"
}
(out/"R05_WORD_RENDER_RECEIPT.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(receipt,ensure_ascii=False,indent=2))

