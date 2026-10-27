"""Only this review dossier is written/copied. Inputs are read and hashed twice."""
from pathlib import Path
import hashlib,json,datetime,shutil
ROOT=Path(__file__).resolve().parent
TARGET=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_complete1031-review')
assert ROOT.resolve()==Path(r'C:\Trabajo\airr\2026-10-27_complete1031-review').resolve()
assert TARGET.resolve()==Path(r'D:\Proyectos\airr-investigacion\2026-10-27_complete1031-review').resolve()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,obj):p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
expected_manifest='720d64a12bd1847a33fbfe0d581bda4d4fa37d0e43f5684996449a968b5a07eb'
checks=[]
for base in [Path(r'C:\Trabajo\airr\2026-10-27_complete1030'),Path(r'D:\Proyectos\airr-investigacion\2026-10-27_complete1030')]:
    assert sha(base/'FROZEN1030.json')==expected_manifest
    m=json.loads((base/'FROZEN1030.json').read_text(encoding='utf-8'))
    for f in m['files']:
        p=base/f['path'];observed=sha(p)
        row={'path':str(p),'expected_sha256':f['sha256'],'observed_sha256':observed,'bytes':p.stat().st_size,'pass':observed==f['sha256'] and p.stat().st_size==f['bytes']}
        checks.append(row);assert row['pass'],row
put(ROOT/'FINAL-INPUT-VERIFIED1031.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'manifest_sha256_C_and_D':expected_manifest,'all_22_payload_checks_passed':True,'inputs_unchanged':True,'checks':checks})
excluded={'MANIFEST1031.json','ARCHIVE1031.json'}
files=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_symlink():raise RuntimeError('Unexpected symlink '+str(p))
    if p.is_file() and p.name not in excluded:
        files.append({'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
put(ROOT/'MANIFEST1031.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'All review1031 files except manifest itself and archive receipt; inputs included as exact copies.','reviewed_pdf_sha256':'50db4efe067fb88a0bef955d4e5b5779bc31a6afe4c1b78b0c16c9f518b89ab3','files':files,'payload_count':len(files),'exclusions':sorted(excluded)})
if TARGET.exists() and any(TARGET.iterdir()):raise RuntimeError('Archive destination unexpectedly nonempty; no overwrite.')
TARGET.mkdir(parents=True,exist_ok=True)
for p in sorted(ROOT.rglob('*')):
    q=TARGET/p.relative_to(ROOT)
    if p.is_dir():q.mkdir(parents=True,exist_ok=True)
    elif p.is_file():shutil.copy2(p,q)
for f in files:assert sha(ROOT/f['path'])==sha(TARGET/f['path'])==f['sha256']
assert sha(ROOT/'MANIFEST1031.json')==sha(TARGET/'MANIFEST1031.json')
receipt={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_C':str(ROOT),'archive_D':str(TARGET),'payload_count':len(files),'total_files_including_manifest_and_receipt':len(files)+2,'all_payloads_identical_C_D':True,'manifest_sha256':sha(ROOT/'MANIFEST1031.json'),'review_sha256':sha(ROOT/'REVIEW1031.txt'),'verdict_sha256':sha(ROOT/'verdict1031.json'),'provenance_sha256':sha(ROOT/'PROVENANCE1031.json'),'input_final_unchanged':True,'no_publication_or_editorial_acceptance':True,'scope':'Exact1030 only;1033 excluded; shared context, independence and effective runtime identity unattested.'}
put(ROOT/'ARCHIVE1031.json',receipt);shutil.copy2(ROOT/'ARCHIVE1031.json',TARGET/'ARCHIVE1031.json')
src={p.relative_to(ROOT).as_posix():sha(p) for p in ROOT.rglob('*') if p.is_file()}
dst={p.relative_to(TARGET).as_posix():sha(p) for p in TARGET.rglob('*') if p.is_file()}
assert src==dst and len(src)==len(files)+2
print(json.dumps(receipt,ensure_ascii=False,indent=2))
