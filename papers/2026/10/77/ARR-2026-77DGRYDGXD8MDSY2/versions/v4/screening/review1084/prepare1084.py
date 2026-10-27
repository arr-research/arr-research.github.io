from pathlib import Path
import json,hashlib,datetime,shutil,difflib
P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
C=Path(r'C:\Trabajo\airr\2026-10-27_complete1060')
D=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_combined1083')
fs='6f43e3d85b5d781f5f47b57aa7a439f5e1afad4294f70d67fa969ae27968ef04'
receipts=[]
for root in [C,D]:
 assert sha(root/'FROZEN1083.json')==fs
 m=json.loads((root/'FROZEN1083.json').read_text(encoding='utf-8'))
 names={f['path'] for f in m['files']}|{'FROZEN1083.json'}
 checks=[]
 for f in m['files']:
  q=root/f['path'];assert sha(q)==f['sha256'] and q.stat().st_size==f['bytes']
  checks.append(f)
 extras=[q.relative_to(root).as_posix() for q in root.rglob('*') if q.is_file() and q.relative_to(root).as_posix() not in names]
 receipts.append({'root':str(root),'all16_payloads_passed':True,'frozen_sha256':fs,'checks':checks,'nonmanifest_names_only':sorted(extras),'auxiliary_contents_not_used':True})
put('INPUT-INITIAL1084.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'16payloads+self, not entire Cdirectory','receipts':receipts})
for f in m['files']+[{'path':'FROZEN1083.json'}]:
 q=P/'input'/f['path'];q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(D/f['path'],q)
deps=json.loads((D/'SOURCE-INPUTS1083.json').read_text(encoding='utf-8'))
dc=[]
for dep in deps['inputs']:
 root=Path(dep['path']);mf=root/dep['manifest'];assert sha(mf)==dep['manifest_sha256']
 dm=json.loads(mf.read_text(encoding='utf-8'));checks=[]
 for f in dm.get('files',dm.get('payloads',[])):
  q=root/f['path'];assert sha(q)==f['sha256'] and q.stat().st_size==f['bytes']
  checks.append(f)
 dc.append({**dep,'payloads_verified':len(checks),'files':checks})
 # Preserve project reports/metadata in own dossier; do not duplicate huge render sets.
 dest=P/'dependencies'/root.name;dest.mkdir(parents=True,exist_ok=True)
 for q in root.iterdir():
  if q.is_file() and (q.name.startswith(('AUDIT','REVIEW','MANIFEST','INCIDENT','READINGS','PROVENANCE','VERDICT','verdict','SOURCE_FETCH')) or q.name==dep['manifest']):shutil.copy2(q,dest/q.name)
put('DEPENDENCIES-INITIAL1084.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'all_passed':True,'dependencies':dc,'independent_review_claim':False})
policy=Path(r'C:\Trabajo\airr-publicacion\reviewed-publications-20261026\docs\MODEL_ASSESSMENT_POLICY.md')
shutil.copy2(policy,P/'RUBRIC1084.md')
old=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_complete1047');diff=[]
for f in m['files']:
 if f['path'].endswith('.tex'):
  a=old/f['path'];b=D/f['path']
  diff.extend(difflib.unified_diff(a.read_text(encoding='utf-8').splitlines(True) if a.exists() else [],b.read_text(encoding='utf-8').splitlines(True),fromfile='1047/'+f['path'],tofile='1083/'+f['path']))
(P/'SOURCE-DIFF1084.txt').write_text(''.join(diff),encoding='utf-8')
print(json.dumps({'input_payloads':len(m['files']),'extra_counts':[len(x['nonmanifest_names_only']) for x in receipts],'dependency_counts':[(x['manifest'],x['payloads_verified']) for x in dc],'rubric_sha256':sha(P/'RUBRIC1084.md')},indent=2))
