from pathlib import Path
from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table
import hashlib
base = Path(r'E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0070_R01')
docx = base / 'candidate' / '0070_R01.docx'
out = base / 'evidence' / 'docx_extracted_R03.md'
sha = hashlib.sha256(docx.read_bytes()).hexdigest()
doc = Document(docx)
lines = [f'# Exact candidate extraction\n\nDOCX SHA-256: `{sha}`\n']
for node in doc.element.body.iterchildren():
    if node.tag.endswith('}p'):
        p = Paragraph(node, doc)
        text = p.text.strip()
        if text:
            lines.append(text)
    elif node.tag.endswith('}tbl'):
        table = Table(node, doc)
        lines.append('\n[TABLE]')
        for row in table.rows:
            lines.append(' | '.join(' '.join(cell.text.split()) for cell in row.cells))
        lines.append('[/TABLE]\n')
out.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(f'extracted={out} chars={sum(map(len, lines))} sha256={sha}')
