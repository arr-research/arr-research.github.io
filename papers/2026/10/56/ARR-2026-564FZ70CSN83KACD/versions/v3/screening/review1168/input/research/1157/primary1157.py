"""Foreign PDF bytes only in memory; retain URLs,hashes and selected reading receipts."""
from pathlib import Path
import requests,fitz,json,hashlib,datetime,sys
sys.stdout.reconfigure(encoding='utf-8');P=Path(__file__).parent
urls={'doeblin':'https://arxiv.org/pdf/2503.22823v3','conditional':'https://arxiv.org/pdf/2608.27171v1','lead':'https://arxiv.org/pdf/2610.03706v1'}
key=sys.argv[1];r=requests.get(urls[key],timeout=45);receipt={'url':urls[key],'status':r.status_code,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
if r.status_code==200:
 b=r.content;doc=fitz.open(stream=b,filetype='pdf');receipt.update(sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),pages=len(doc))
 if len(sys.argv)>2 and sys.argv[2]=='find':
  terms=sys.argv[3:];receipt['locator_terms']=terms;print(json.dumps([{'page':i+1,'terms':[x for x in terms if x.casefold() in page.get_text().casefold()]} for i,page in enumerate(doc) if any(x.casefold() in page.get_text().casefold() for x in terms)]))
 elif len(sys.argv)>2:
  pages=list(map(int,sys.argv[2:]));receipt['pages_requested']=pages
  for i in pages:print('\nPAGE',i,'\n',doc[i-1].get_text())
 else:print(json.dumps(receipt))
else:print('HTTP',r.status_code)
(P/('PRIMARY_'+key+'_'+datetime.datetime.now().strftime('%H%M%S%f')+'.json')).write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
