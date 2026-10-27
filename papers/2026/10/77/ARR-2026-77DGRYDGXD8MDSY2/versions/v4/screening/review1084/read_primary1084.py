from pathlib import Path
import io, json, hashlib, urllib.request, sys, argparse
from datetime import datetime, timezone
from pypdf import PdfReader
p=argparse.ArgumentParser();p.add_argument('url');p.add_argument('--pages',default='');p.add_argument('--find',default='');a=p.parse_args()
data=urllib.request.urlopen(a.url,timeout=60).read()
reader=PdfReader(io.BytesIO(data));texts=[p.extract_text() or '' for p in reader.pages]
pages=[int(x) for x in a.pages.split(',') if x]
rec={'utc':datetime.now(timezone.utc).isoformat(),'url':a.url,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'pages':len(texts),'requested_pages':pages,'find':a.find,'foreign_corpus_saved':False}
root=Path(__file__).resolve().parent
with (root/'SOURCE_FETCHES1084.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps(rec)+'\n')
print(json.dumps(rec))
if a.find:
    for i,t in enumerate(texts):
        if a.find.lower() in t.lower(): print('MATCH_PAGE',i+1, t[max(0,t.lower().find(a.find.lower())-150):t.lower().find(a.find.lower())+500])
for i in pages: print('\n--- PAGE',i,'---\n',texts[i-1])
