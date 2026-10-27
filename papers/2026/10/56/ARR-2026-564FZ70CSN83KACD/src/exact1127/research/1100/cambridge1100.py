from pathlib import Path
import requests,fitz,json,hashlib,sys,datetime
sys.stdout.reconfigure(encoding='utf-8');P=Path(__file__).parent
url='https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7270B6BBA7891B612C00FAB066F1A380/S2050509424001178a.pdf/complete-positivity-order-and-relative-entropy-decay.pdf'
rec=dict(url=url,version='Forum Mathematics Sigma13:e31(2025), DOI10.1017/fms.2024.117',foreign_corpus_saved=False,utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
try:
 r=requests.get(url,timeout=45);r.raise_for_status();rec.update(sha256=hashlib.sha256(r.content).hexdigest(),bytes=len(r.content));doc=fitz.open(stream=r.content,filetype='pdf');rec['pages']=len(doc)
 if len(sys.argv)>1:
  pages=list(map(int,sys.argv[1].split(',')));rec['pages_read_1based']=pages
  for p in pages:print('PAGE',p,doc[p-1].get_text())
 else:
  for i,p in enumerate(doc):
   s=p.get_text()
   if any(x in s for x in ['Definition 5.1','Theorem 5.','contraction coefficient','depolarizing','depolarization']):print('LOCATOR',i+1,s[:160],s.find('Definition 5.1'))
except Exception as e:rec['error']=repr(e)
(P/('PRIMARY_CAMBRIDGE_'+datetime.datetime.now().strftime('%H%M%S%f')+'.json')).write_text(json.dumps(rec,indent=2)+'\n',encoding='utf-8');print(json.dumps(rec))
