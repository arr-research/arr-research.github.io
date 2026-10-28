import requests,fitz,hashlib,json,datetime,sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8');P=Path(__file__).parent
sources=[('Evans_Schulman1999_author','https://www.cs.ubc.ca/~will/papers/qdp.pdf',[1,2,3,4]),('Ordentlich_Polyanskiy_author','https://people.lids.mit.edu/yp/homepage/data/2020_binsdpi.pdf',[1,2])]
for name,url,pages in sources:
 rec={'url':url,'version':name,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'foreign_corpus_saved':False}
 try:
  r=requests.get(url,timeout=40);r.raise_for_status();doc=fitz.open(stream=r.content,filetype='pdf');rec.update(sha256=hashlib.sha256(r.content).hexdigest(),bytes=len(r.content),pages=len(doc),status=r.status_code,pages_read_1based=[])
  for p in pages:
   if p<=len(doc):rec['pages_read_1based'].append(p);print(name,'PAGE',p,doc[p-1].get_text())
 except Exception as e:rec['error']=repr(e)
 (P/('PRIMARY_'+name+'.json')).write_text(json.dumps(rec,indent=2)+'\n',encoding='utf-8');print(json.dumps(rec))
