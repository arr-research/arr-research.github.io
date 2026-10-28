from pathlib import Path
import hashlib,json,shutil,datetime
ROOT=Path(__file__).resolve().parent
C=Path(r'C:\Trabajo\airr\2026-10-28_cq1167')
D=Path(r'D:\Proyectos\airr-investigacion\2026-10-28_cq1167')
MH='0614ff2eddca97659c85577629718c6c82c6a3cfe0203a0ca6fec2f848774100'
PH='6d4f64b0b9423852ad2831e551edf467a6fbca14d30991b517084978573455c5'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def inventory(p): return [{'path':x.relative_to(p).as_posix(),'bytes':x.stat().st_size,'sha256':sha(x)} for x in sorted(p.rglob('*')) if x.is_file()]
def verify():
 assert sha(C/'MANIFEST1167.json')==sha(D/'MANIFEST1167.json')==MH
 manifest=json.loads((C/'MANIFEST1167.json').read_text(encoding='utf-8-sig'))
 ic,id_=inventory(C),inventory(D)
 assert ic==id_ and len(ic)==929
 table={x['path']:x for x in ic}
 for r in manifest['files']: assert table[r['path']]==r,r['path']
 assert set(table)=={r['path'] for r in manifest['files']}|{'MANIFEST1167.json'}
 assert sha(C/'manuscript.pdf')==PH and (C/'manuscript.pdf').stat().st_size==452673
 return {'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'C':str(C),'D':str(D),'C_D_identical':True,'files':ic,'manifest_sha256':MH,'pdf_sha256':PH,'scientific_reading_started_before_check':False}
if __name__=='__main__':
 result=verify()
 (ROOT/'INPUT-INITIAL1168.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 for row in result['files']:
  dest=ROOT/'input'/row['path'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(C/row['path'],dest)
 assert inventory(ROOT/'input')==result['files']
 print(json.dumps({'integrity':'PASS','files':len(result['files']),'pdf':PH,'local_input_copy':'identical'}))
