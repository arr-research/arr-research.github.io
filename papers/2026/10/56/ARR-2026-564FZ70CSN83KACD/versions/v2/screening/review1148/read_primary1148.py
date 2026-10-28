from pathlib import Path
import io,json,hashlib,urllib.request,argparse,datetime
from pypdf import PdfReader
p=argparse.ArgumentParser();p.add_argument('url');p.add_argument('--pages',default='');p.add_argument('--find',default='');a=p.parse_args()
root=Path(__file__).resolve().parent
try:
 data=urllib.request.urlopen(a.url,timeout=45).read();r=PdfReader(io.BytesIO(data));texts=[p.extract_text() or '' for p in r.pages]
 pages=[int(x) for x in a.pages.split(',') if x]
 rec={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':a.url,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'pages':len(texts),'requested_pages':pages,'find':a.find,'foreign_corpus_saved':False}
 with (root/'SOURCE_FETCHES1148.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(rec)+'\n')
 print(json.dumps(rec))
 if a.find:
  for i,t in enumerate(texts):
   j=t.lower().find(a.find.lower())
   if j>=0:print('MATCH_PAGE',i+1,t[max(0,j-140):j+450])
 for i in pages:print('\n--- PAGE',i,'---\n',texts[i-1])
except Exception as e:
 with (root/'SOURCE_FETCH_FAILURES1148.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':a.url,'error':repr(e)})+'\n')
 raise

