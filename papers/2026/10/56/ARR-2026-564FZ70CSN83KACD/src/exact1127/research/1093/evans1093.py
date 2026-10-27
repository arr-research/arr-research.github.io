from pathlib import Path
import requests,fitz,hashlib,json,datetime,sys
sys.stdout.reconfigure(encoding='utf-8');P=Path(__file__).parent;url='https://users.cms.caltech.edu/~schulman/Papers/evansS99.pdf'
r=requests.get(url,timeout=40);r.raise_for_status();doc=fitz.open(stream=r.content,filetype='pdf')
for n in (1,2,3):print('PAGE',n,doc[n-1].get_text())
(P/'PRIMARY_Evans_Schulman_journal1093.json').write_text(json.dumps({'url':url,'version':'1999 journal reprint on author site','sha256':hashlib.sha256(r.content).hexdigest(),'bytes':len(r.content),'pages':len(doc),'pages_attempted_1based':[1,2,3],'foreign_corpus_saved':False},indent=2)+'\n',encoding='utf-8')
