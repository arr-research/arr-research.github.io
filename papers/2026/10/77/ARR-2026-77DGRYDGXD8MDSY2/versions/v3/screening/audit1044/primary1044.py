from pathlib import Path
import requests,fitz,json,hashlib,datetime,sys
sys.stdout.reconfigure(encoding='utf-8');P=Path(__file__).parent;ident=sys.argv[1];kind=sys.argv[2] if len(sys.argv)>2 else 'pdf';url='https://arxiv.org/'+kind+'/'+ident;rec={'url':url,'version':ident,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'foreign_corpus_saved':False}
try:
 r=requests.get(url,timeout=40);r.raise_for_status();rec.update(sha256=hashlib.sha256(r.content).hexdigest(),bytes=len(r.content),status=r.status_code)
 if kind=='pdf':
  doc=fitz.open(stream=r.content,filetype='pdf');rec['pages']=len(doc)
  if len(sys.argv)>3:
   pages=[int(x) for x in sys.argv[3].split(',')];rec['pages_read_1based']=pages
   for p in pages:print('PAGE',p,doc[p-1].get_text())
  else:
   rec['read_level']='locator only'
   for i,p in enumerate(doc):
    txt=p.get_text();hits=[q for q in ['Lemma 1','Lemma 4.1','Lemma IV.1','7.1','Example 1','depolariz'] if q in txt]
    if hits:print(i+1,hits)
except Exception as ex:rec['error']=repr(ex)
(P/('PRIMARY_'+ident.replace('/','_')+'_'+kind+'_'+datetime.datetime.now().strftime('%H%M%S%f')+'.json')).write_text(json.dumps(rec,indent=2)+'\n',encoding='utf-8');print(json.dumps(rec))
