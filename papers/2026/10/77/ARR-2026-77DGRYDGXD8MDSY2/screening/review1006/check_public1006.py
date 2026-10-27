"""Anonymous byte verification of the version-pinned public supplement.
Only manuscript-relevant files are persisted; later extensions are not fetched.
"""
from pathlib import Path
import concurrent.futures,datetime,hashlib,json,urllib.request
ROOT=Path(__file__).resolve().parent
COMMIT='f0b3642b196b9de6d51b31cca49a69818522ee91'
BASE='https://raw.githubusercontent.com/lluiseriksson/physmath-knowledge-tree/'+COMMIT+'/integrations/research-radar/evidence/2026-10-27-pauli-audit/'
def sha(data):return hashlib.sha256(data).hexdigest()
def get(name):
    with urllib.request.urlopen(urllib.request.Request(BASE+name,headers={'User-Agent':'AIRR review1006 byte check'}),timeout=45) as response:
        data=response.read()
        return data,{'name':name,'url':BASE+name,'status':response.status,'resolved_url':response.geturl(),'bytes':len(data),'sha256':sha(data),'anonymous':True}
manifest_data,manifest_fetch=get('MANIFEST1001.json')
(ROOT/'public-supplement'/'MANIFEST1001.json').write_bytes(manifest_data)
manifest=json.loads(manifest_data)
index={x['path']:x for x in manifest['files']}
selected=['README.txt','requirements.txt','symbolic993.py','verify993.py','verify-certificates991.py',
          'PETZ-CERTIFICATE991.json','VARIANCE-CERTIFICATE991.json','SYMBOLIC993.json','VERIFY993.json','VERIFIED991.json',
          'AUDIT988.txt','INCIDENTS988.txt','verdict988.json']
results=[]
def one(name):
    try:
        data,row=get(name)
        entry=index[name]
        row['manifest_repository_hash']=entry['repository_sha256']
        row['public_hash_matches_manifest']=row['sha256']==entry['repository_sha256']
        row['manifest_original_hash']=entry['original_sha256']
        local=ROOT/'reproduction'/name
        if local.exists():
            original=local.read_bytes()
            row['local1005_sha256']=sha(original)
            row['sealed_original_hash_matches_local1005']=sha(original)==entry['original_sha256']
            row['local1005_LF_equivalent']=original.replace(b'\r\n',b'\n')==data
            row['readme_difference_expected']=name=='README.txt'
        if name in ['AUDIT988.txt','INCIDENTS988.txt','verdict988.json']:
            old=Path('D:/Proyectos/airr-investigacion/2026-10-27_harmonic988-audit')/name
            row['original988_sha256']=sha(old.read_bytes())
            row['original988_matches_manifest']=row['original988_sha256']==entry['original_sha256']
            row['body_read_for_scientific_assessment']=False
            row['persisted']=False
        else:
            (ROOT/'public-supplement'/name).write_bytes(data)
            row['persisted']=True
        return row
    except Exception as exc:return {'name':name,'failed':True,'error':repr(exc)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(one,selected))
report={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':COMMIT,
        'manifest_fetch':manifest_fetch,'manifest_total_entries':len(index),'selected_files':results,
        'later_extensions':'997/1003 bodies not read, downloaded or evaluated; names/hashes appear in the public listing and manifest only.',
        'scope':'Public availability and byte integrity of selected manuscript-related files, not a scientific endorsement of audit988 or a check of all public-manifest entries.'}
with (ROOT/'PUBLIC-VERIFIED1006-run01.json').open('x',encoding='utf-8') as f:json.dump(report,f,ensure_ascii=False,indent=2)
assert all(not x.get('failed') and x['public_hash_matches_manifest'] for x in results)
assert all(x.get('local1005_LF_equivalent',True) for x in results if x['name']!='README.txt')
assert all(x.get('original988_matches_manifest',True) for x in results)
print(json.dumps(report,ensure_ascii=False,indent=2))
