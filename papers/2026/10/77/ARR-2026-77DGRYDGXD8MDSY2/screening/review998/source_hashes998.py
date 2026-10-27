"""Hash version-pinned primary PDFs in RAM; retain no external full texts."""
import concurrent.futures, datetime, hashlib, io, json, urllib.request
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
IDS = ['1508.03551v1', '1904.06562v2', '2503.22823v3', '2411.19890v3',
       '2608.27171v1', '2608.19685v1', '2505.15281v3']

def one(identifier):
    url = 'https://arxiv.org/pdf/' + identifier
    try:
        request = urllib.request.Request(url, headers={'User-Agent':'AIRR manuscript review998 provenance'})
        with urllib.request.urlopen(request, timeout=45) as response:
            data = response.read()
            final_url = response.geturl()
        assert data[:5] == b'%PDF-', 'Non-PDF response'
        return {'id':identifier, 'url':url, 'resolved_url':final_url,
                'sha256':hashlib.sha256(data).hexdigest(), 'bytes':len(data),
                'pages':len(PdfReader(io.BytesIO(data)).pages), 'status':'ok',
                'fulltext_persisted':False}
    except Exception as exc:
        return {'id':identifier, 'url':url, 'status':'failed', 'error':repr(exc)}

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(one, IDS))
output = {'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'purpose':'Version and byte provenance only; downloaded full texts not retained.',
          'sources':results}
path = ROOT / 'SOURCE-HASHES998-run01.json'
with path.open('x', encoding='utf-8') as handle:
    json.dump(output, handle, ensure_ascii=False, indent=2)
print(json.dumps(output, ensure_ascii=False, indent=2))
