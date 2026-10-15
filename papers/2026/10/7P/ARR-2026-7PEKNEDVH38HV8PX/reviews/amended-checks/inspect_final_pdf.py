from pathlib import Path
import hashlib,json
import fitz

P=Path(__file__).resolve().parent
pdf=Path(r'D:\Entregas\airr\2026-10-15_aritmetica-del-muestreo\sampling-arithmetic.pdf')
expected='66b83edcef934f296dcfc63e55f8463b3cbd9187b37afe06c4ab3a49cb5dcc33'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==expected
doc=fitz.open(pdf)
assert len(doc)==10
texts=[]
for i,page in enumerate(doc):
    texts.append(f'\n=== PAGE {i+1} ===\n'+page.get_text())
    page.get_pixmap(matrix=fitz.Matrix(1.25,1.25)).save(P/f'final-page-{i+1:02}.png')
joined=''.join(texts)
(P/'final-pdf-extracted.txt').write_text(joined,encoding='utf8')
assert '53,000' in joined and 'Theorem 7.3' in joined
assert '9b9cccff' not in joined  # No source hash expected inside manuscript.
data={'pdf_path':str(pdf),'pdf_sha256':expected,'pages':len(doc),'tex_sha256':hashlib.sha256((P.parent/'sampling-arithmetic.tex').read_bytes()).hexdigest(),'rendered_pages':10,'render_scale':1.25}
(P/'final-pdf-inspection.json').write_text(json.dumps(data,indent=2),encoding='utf8')
print(json.dumps(data,indent=2))
