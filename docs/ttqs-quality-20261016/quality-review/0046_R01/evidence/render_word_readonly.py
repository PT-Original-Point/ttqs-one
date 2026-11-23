from __future__ import annotations
import argparse
import json
from pathlib import Path

import pythoncom
import win32com.client

parser = argparse.ArgumentParser()
parser.add_argument("docx", type=Path)
parser.add_argument("pdf", type=Path)
args = parser.parse_args()
args.docx = args.docx.resolve()
args.pdf = args.pdf.resolve()
args.pdf.parent.mkdir(parents=True, exist_ok=True)

pythoncom.CoInitialize()
word = None
doc = None
try:
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    word.ScreenUpdating = False
    word.AutomationSecurity = 3
    word.Options.SaveNormalPrompt = False
    doc = word.Documents.Open(str(args.docx), False, True, False)
    doc.Repaginate()
    pages = int(doc.ComputeStatistics(2))
    doc.ExportAsFixedFormat(str(args.pdf), 17)
    print(json.dumps({"status": "RENDERED_READ_ONLY", "pages": pages, "docx": str(args.docx), "pdf": str(args.pdf)}, ensure_ascii=False))
finally:
    if doc is not None:
        doc.Close(False)
    if word is not None:
        word.Quit(False)
    pythoncom.CoUninitialize()
