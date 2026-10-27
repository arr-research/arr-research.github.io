from pathlib import Path
import fitz,json
root=Path(__file__).resolve().parent
p=fitz.open(root/'input'/'main.pdf')
rows=[]
for i,x in enumerate(p):
    links=[{k:(list(v) if isinstance(v,fitz.Rect) else v) for k,v in link.items()} for link in x.get_links()]
    rows.append({'page':i+1,'text':x.get_text(),'links':links})
with (root/'PDF-TEXT1006-run02.json').open('x',encoding='utf-8') as f:json.dump(rows,f,ensure_ascii=False,indent=2)
print('pages',len(p))
print('\n'.join('PAGE '+str(x['page'])+'\n'+x['text'] for x in rows))
