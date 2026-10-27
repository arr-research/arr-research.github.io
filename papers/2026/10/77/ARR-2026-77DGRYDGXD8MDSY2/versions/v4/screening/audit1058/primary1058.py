from pathlib import Path
import requests,fitz,json,hashlib,datetime,sys,re
sys.stdout.reconfigure(encoding='utf-8');P=Path(__file__).parent;ident=sys.argv[1];url='https://arxiv.org/pdf/'+ident;rec={'url':url,'version':ident,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'foreign_corpus_saved':False}
try:
 r=requests.get(url,timeout=40);r.raise_for_status();rec.update(sha256=hashlib.sha256(r.content).hexdigest(),bytes=len(r.content),status=r.status_code);doc=fitz.open(stream=r.content,filetype='pdf');rec['pages']=len(doc)
 if len(sys.argv)>2:
  pages=[int(x) for x in sys.argv[2].split(',')];rec['pages_read_1based']=pages
  for p in pages:print('PAGE',p,doc[p-1].get_text())
 else:
  rec['read_level']='locator only'
  for i,p in enumerate(doc):
   lines=p.get_text().splitlines();hits=[(j,x) for j,x in enumerate(lines) if re.search(r'^(I+\.|[A-Z]\.|[0-9]+\.|Theorem)|Dobrushin|unitary|Hamiltonian|Fisher|depolariz',x,re.I)]
   print(i+1,[(j,x) for j,x in hits][:14])
except Exception as ex:rec['error']=repr(ex)
(P/('PRIMARY_'+ident+'_'+datetime.datetime.now().strftime('%H%M%S%f')+'.json')).write_text(json.dumps(rec,indent=2)+'\n',encoding='utf-8');print(json.dumps(rec))
