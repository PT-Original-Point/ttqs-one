from pathlib import Path
import pypdfium2 as pdfium
root=Path(r'E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0067_R01\evidence\render_R02')
pdf=pdfium.PdfDocument(root/'0067_R02_word_export.pdf')
for i in range(len(pdf)):
    page=pdf[i]
    pil=page.render(scale=2.2).to_pil()
    out=root/f'page-{i+1:02}.png'
    pil.save(out)
    print(f'{out.name}\t{pil.width}x{pil.height}\t{out.stat().st_size}')
print(f'PAGES={len(pdf)}')
