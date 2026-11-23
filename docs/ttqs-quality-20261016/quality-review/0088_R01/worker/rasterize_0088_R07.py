from pathlib import Path
from pdf2image import convert_from_path
root=Path(__file__).resolve().parents[1]
pdf=root/'evidence'/'render_R07_final3'/'0088_R07.pdf'
out=pdf.parent
poppler=r'C:\Users\J\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin'
images=convert_from_path(str(pdf),dpi=150,poppler_path=poppler)
for i,image in enumerate(images,1):
    image.save(out/f'page-{i:02d}.png',format='PNG',optimize=True)
print({'pdf_pages':len(images),'png_pages':len(list(out.glob('page-*.png'))),'pdf':str(pdf)})

