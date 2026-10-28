"""Fetch primary PDF into memory only; retain metadata/hashes, never a foreign corpus."""
from pathlib import Path
import argparse,datetime,hashlib,json,re
import requests,fitz
p=argparse.ArgumentParser();p.add_argument('url');p.add_argument('--pages',default='');p.add_argument('--find',default='');a=p.parse_args()
root=Path(__file__).resolve().parent
rec={'url':a.url,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'retained_foreign_corpus':False}
try:
 r=requests.get(a.url,timeout=45);rec.update(status=r.status_code,final_url=r.url,bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest(),content_type=r.headers.get('content-type'))
 r.raise_for_status();doc=fitz.open(stream=r.content,filetype='pdf');rec['pages']=len(doc)
 texts=[pg.get_text() for pg in doc]
 if a.find:
  patterns=a.find.split('|');matches=[]
  for no,t in enumerate(texts,1):
   for pattern in patterns:
    for match in list(re.finditer(re.escape(pattern),t,re.I))[:6]:
     matches.append({'page':no,'pattern':pattern,'context':t[max(0,match.start()-100):match.end()+220].replace('\n',' ')})
  print(json.dumps({'machine_search_matches':matches},ensure_ascii=False,indent=2));rec['machine_search_patterns']=patterns
 if a.pages:
  nums=[]
  for s in a.pages.split(','):
   if '-' in s:
    l,h=map(int,s.split('-'));nums.extend(range(l,h+1))
   else:nums.append(int(s))
  rec['selected_pages_presented']=nums
  for n in nums:print(f'\n===== PRIMARY PDF PAGE {n} =====\n'+texts[n-1])
 rec['success']=True
except Exception as e:
 rec.update(success=False,error=repr(e));print(json.dumps(rec,ensure_ascii=False));raise
finally:
 with (root/'PRIMARY-FETCHES1168.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
