from pathlib import Path
import urllib.request,hashlib,json,datetime,concurrent.futures
ROOT=Path(__file__).parent
base='https://raw.githubusercontent.com/lluiseriksson/physmath-knowledge-tree/34400956487e21509b5196884caa320907b26f58/integrations/research-radar/evidence/2026-10-27-principal-bkm/'
def digest(b):return hashlib.sha256(b).hexdigest()
raw=urllib.request.urlopen(base+'MANIFEST1036.json',timeout=60).read()
assert digest(raw)=='0a9f83c16d368466b28b59fdbb545f11bf10758c3b3c7f8f224b011218762122'
m=json.loads(raw);dest=ROOT/'public-supplement';dest.mkdir(exist_ok=True);(dest/'MANIFEST1036.json').write_bytes(raw)
def one(f):
 b=urllib.request.urlopen(base+f['path'],timeout=60).read();q=dest/f['path'];q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(b)
 return {'path':f['path'],'bytes':len(b),'sha256':digest(b),'pass':len(b)==f['bytes'] and digest(b)==f['sha256']}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(one,m['files']))
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_head':'34400956487e21509b5196884caa320907b26f58','manifest_sha256':digest(raw),'payload_count':len(rows),'total_remote_files_checked':len(rows)+1,'all_passed':all(x['pass'] for x in rows),'checks':rows,'not_reverified':'Parent campaign31 files and5Pages/CI; this check covers24manifest payloads and manifest,25files only.'}
(ROOT/'PUBLIC-VERIFIED1048.json').write_text(json.dumps(out,indent=2)+'\n');assert out['all_passed'];print('25 public files verified against pinned manifest; no Git or publication operation.')
u='https://arxiv.org/html/2610.29373v1';b=urllib.request.urlopen(u,timeout=60).read()
(ROOT/'HAN-LI-HTML1048.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':u,'sha256':digest(b),'bytes':len(b),'read_via_web_tool':'Abstract and section2.2 definitions/Lemma1/Eqs29-32, not whole paper or AD proof','foreign_corpus_saved':False},indent=2)+'\n')
