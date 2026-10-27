"""Pure-Python PDF inspection after retained PyMuPDF diagnostic failures."""
from pathlib import Path
import json
from pypdf import PdfReader
root=Path(__file__).resolve().parent
reader=PdfReader(root/'input'/'main.pdf')
rows=[]
for i,page in enumerate(reader.pages):
    links=[]
    for ref in page.get('/Annots',[]):
        annotation=ref.get_object()
        action=annotation.get('/A')
        if action and action.get('/URI'):links.append(str(action['/URI']))
    rows.append({'page':i+1,'text':page.extract_text(),'uri_links':links})
with (root/'PDF-TEXT1006-run03.json').open('x',encoding='utf-8') as f:json.dump(rows,f,ensure_ascii=False,indent=2)
assert len(rows)==8
target='https://github.com/lluiseriksson/physmath-knowledge-tree/tree/f0b3642b196b9de6d51b31cca49a69818522ee91/integrations/research-radar/evidence/2026-10-27-pauli-audit'
assert target in rows[6]['uri_links']
print(json.dumps({'pages':len(rows),'supplement_link_in_actual_pdf':True,'links_page7':rows[6]['uri_links'],'links_page8':rows[7]['uri_links']},indent=2))
