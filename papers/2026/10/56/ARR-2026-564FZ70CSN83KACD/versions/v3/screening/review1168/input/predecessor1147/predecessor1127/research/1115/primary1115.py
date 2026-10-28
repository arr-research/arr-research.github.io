from pathlib import Path
import requests,fitz,json,hashlib,datetime,sys,re
sys.stdout.reconfigure(encoding='utf-8');P=Path(__file__).parent;key=sys.argv[1]
url={'journal':'https://d-nb.info/1265446733/34','cohen1993':'https://lab.rockefeller.edu/cohenje/assets/file/205CohenIwasaRautuRuskaiSenetaZbaganuRelativeEntropyMappingsStochasticMatricesLAA1993.pdf'}.get(key,'https://arxiv.org/pdf/'+key)
rec=dict(url=url,version=key,utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),foreign_corpus_saved=False)
try:
 r=requests.get(url,timeout=45);rec['status']=r.status_code;r.raise_for_status();rec.update(sha256=hashlib.sha256(r.content).hexdigest(),bytes=len(r.content));doc=fitz.open(stream=r.content,filetype='pdf');rec['pages']=len(doc)
 if len(sys.argv)>2:
  pages=list(map(int,sys.argv[2].split(',')));rec['pages_read_1based']=pages
  for p in pages:print('PAGE',p,doc[p-1].get_text())
 else:
  rec['level']='locatoronly'
  for i,p in enumerate(doc):
   s=p.get_text();lines=s.splitlines();hits=[x for x in lines if re.search(r'Theorem|Problem|primitive|contraction|Definition',x,re.I)];print(i+1,hits[:8])
except Exception as e:rec['error']=repr(e)
(P/('PRIMARY_'+key.replace('/','_')+'_'+datetime.datetime.now().strftime('%H%M%S%f')+'.json')).write_text(json.dumps(rec,indent=2)+'\n',encoding='utf-8');print(json.dumps(rec))
