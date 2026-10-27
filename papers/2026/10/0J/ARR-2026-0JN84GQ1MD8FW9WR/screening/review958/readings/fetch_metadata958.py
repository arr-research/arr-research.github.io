"""Fetch primary PDFs in memory only. Persist metadata/hashes, never a foreign corpus."""
import hashlib,json,urllib.request,concurrent.futures
from pathlib import Path
from datetime import datetime,timezone
ids=['2102.04146v3','quant-ph/9708015v3','quant-ph/9911117v4','2608.27171v1',
     '2011.05949v4','1102.5170v2','quant-ph/9904023v5','2206.05247v1',
     '1806.00019v2','1806.01298v2','2608.19685v1']
def get(i):
    url='https://arxiv.org/pdf/'+i
    rec=dict(arxiv_version=i,url=url,retrieved_utc=datetime.now(timezone.utc).isoformat())
    try:
      req=urllib.request.Request(url,headers={'User-Agent':'Academic manuscript reference verification'})
      with urllib.request.urlopen(req,timeout=35) as f:
        data=f.read();rec.update(final_url=f.url,status=f.status,content_type=f.headers.get('Content-Type'),
          bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),pdf_header=data[:5]==b'%PDF-')
      del data
    except Exception as e: rec['error']=repr(e)
    return rec
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool: rows=list(pool.map(get,ids))
Path(__file__).with_name('PRIMARY_FETCH_METADATA958.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
print(json.dumps(rows))
