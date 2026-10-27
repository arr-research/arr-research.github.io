"""Final input recheck and identical archival copy; only owns review1048 paths."""
from pathlib import Path
import json,hashlib,datetime,shutil
P=Path(__file__).resolve().parent
D=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_complete1048-review')
assert str(P)==r'C:\Trabajo\airr\2026-10-27_complete1048-review'
assert not D.exists(),'Archive already exists; preserve and inspect instead of overwriting.'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(n,x):
    q=P/n;assert not q.exists(),str(q)
    q.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def files(base):
    for p in sorted(base.rglob('*')):
        assert not p.is_symlink() and not p.is_junction(),str(p)
        if p.is_file():yield p
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
checks=[]
extras=[]
fsha='406dcccd5be71ac41d6c96a54fe3e415349b64d8c89a29d7fe043801661d835e'
for base in [Path(r'C:\Trabajo\airr\2026-10-27_complete1047'),Path(r'D:\Proyectos\airr-investigacion\2026-10-27_complete1047')]:
    assert sha(base/'FROZEN1047.json')==fsha
    m=json.loads((base/'FROZEN1047.json').read_text(encoding='utf-8'))
    expected={x['path'].replace('\\','/') for x in m['files']}|{'FROZEN1047.json'}
    actual={p.relative_to(base).as_posix() for p in files(base)}
    assert expected <= actual
    extras.append({'root':str(base),'nonmanifest_files':[{'path':n,'bytes':(base/n).stat().st_size,'sha256':sha(base/n)} for n in sorted(actual-expected)]})
    for f in m['files']:
        p=base/f['path'];ok=sha(p)==f['sha256'] and p.stat().st_size==f['bytes'];assert ok
        checks.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p),'pass':ok})
        assert sha(P/'input'/f['path'])==f['sha256']
put('INPUT-FINAL1048.json',{'utc':now,'all_passed':True,'all_input_payloads_unchanged':True,'payloads_per_copy':10,'frozen_files_per_copy':11,'nonmanifest_inventory':extras,'frozen_sha256':fsha,'checks':checks})
initial=json.loads((P/'AUDIT1044-INITIAL1048.json').read_text(encoding='utf-8'))
auditchecks=[]
for base in [Path(r'C:\Trabajo\airr\2026-10-27_principal1044-audit'),Path(r'D:\Proyectos\airr-investigacion\2026-10-27_principal1044-audit')]:
    assert {p.relative_to(base).as_posix() for p in files(base)}=={x['path'] for x in initial['files']}
    for f in initial['files']:
        p=base/f['path'];assert sha(p)==f['sha256'] and p.stat().st_size==f['bytes']
        assert sha(P/'audit1044'/f['path'])==f['sha256']
    auditchecks.append({'root':str(base),'44_original_files_unchanged':True})
am=json.loads((P/'audit1044/MANIFEST1044.json').read_text(encoding='utf-8'))
for f in am['files']:
    q=P/'audit1044'/f['path'];assert sha(q)==f['sha256'] and q.stat().st_size==f['bytes']
assert len(am['files'])==41
put('AUDIT1044-FINAL1048.json',{'utc':now,'all_passed':True,'checks':auditchecks,'manifest_payloads_verified':41,'not_independent_manuscript_vote':True})
v=json.loads((P/'verdict1048.json').read_text(encoding='utf-8'))
assert v['evidence']['report_sha256']==sha(P/'REVIEW1048.txt')
assert json.loads((P/'ARR-VALIDATION1048.json').read_text(encoding='utf-8'))['content_subset_valid']
assert (P/'EXTRACTED1048.txt').read_bytes()==(P/'input/PAPER1047.txt').read_bytes()
for q in files(P):
    if q.suffix=='.json':json.loads(q.read_text(encoding='utf-8-sig'))
payloads=[{'path':q.relative_to(P).as_posix(),'bytes':q.stat().st_size,'sha256':sha(q)} for q in files(P)]
put('MANIFEST1048.json',{'review':'1048','utc':now,'algorithm':'SHA256','manuscript_sha256':v['manuscript_sha256'],'excluded':['MANIFEST1048.json','ARCHIVE1048.json'],'payload_count':len(payloads),'files':payloads,'foreign_corpus_included':False,'scope':'Own report/scripts/outputs, authorized manuscript/supplement/component evidence and own prior reading records.'})
D.mkdir(parents=True)
for q in files(P):
    r=D/q.relative_to(P);r.parent.mkdir(parents=True,exist_ok=True);assert not r.exists();shutil.copy2(q,r)
for q in files(P):assert sha(q)==sha(D/q.relative_to(P))
assert {q.relative_to(P).as_posix() for q in files(P)}=={q.relative_to(D).as_posix() for q in files(D)}
receipt={'review':'1048','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':str(P),'archive':str(D),'all_files_byte_identical':True,'payload_count':len(payloads),'total_files_each_including_manifest_and_receipt':len(payloads)+2,'manifest_sha256':sha(P/'MANIFEST1048.json'),'report_sha256':sha(P/'REVIEW1048.txt'),'verdict_sha256':sha(P/'verdict1048.json'),'pdf_sha256':v['manuscript_sha256'],'inputs_1047_and_audit1044_unchanged':True,'no_publication_or_editorial_acceptance':True}
put('ARCHIVE1048.json',receipt);shutil.copy2(P/'ARCHIVE1048.json',D/'ARCHIVE1048.json')
assert sha(P/'ARCHIVE1048.json')==sha(D/'ARCHIVE1048.json')
assert len(list(files(P)))==len(list(files(D)))==len(payloads)+2
print(json.dumps(receipt,ensure_ascii=False,indent=2))
