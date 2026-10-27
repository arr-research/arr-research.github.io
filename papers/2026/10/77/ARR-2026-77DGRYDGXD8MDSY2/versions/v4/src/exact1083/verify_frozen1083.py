"""Read-only verification of the explicitly enumerated manuscript freeze scope.
Auxiliary files are inventoried separately, not silently promoted into the seal.
"""
from pathlib import Path
import argparse,datetime,hashlib,json,re
from pypdf import PdfReader

def verify(manifest):
 manifest=Path(manifest).resolve();root=manifest.parent;j=json.loads(manifest.read_text(encoding='utf-8'))
 digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
 rows=[];paths=set()
 for item in j['files']:
  rel=item['path'];p=(root/rel).resolve();assert p.is_relative_to(root) and rel not in paths,(rel,'outside or duplicate')
  assert p.is_file() and p.stat().st_size==item['bytes'] and digest(p)==item['sha256'],rel
  paths.add(rel);rows.append(dict(path=rel,sha256=digest(p),bytes=p.stat().st_size))
 pdf=root/'main.pdf';assert pdf.is_file() and 'main.pdf' in paths
 assert digest(pdf)==j['canonical_pdf_sha256'] and pdf.stat().st_size==j['bytes']
 pages=len(PdfReader(pdf).pages);assert pages==j['pages']
 inputs=[]
 for rel in paths:
  if not rel.endswith('.tex'):continue
  text=(root/rel).read_text(encoding='utf-8')
  for filename in re.findall(r'\\(?:input|include)\s*\{([^}]+)\}',text):
   name=filename if Path(filename).suffix else filename+'.tex'
   target=(root/name).resolve();assert target.is_relative_to(root) and target.relative_to(root).as_posix() in paths,(rel,filename,'unbound source input')
   inputs.append(dict(source=rel,input=name))
 extras=[dict(path=p.relative_to(root).as_posix(),bytes=p.stat().st_size,sha256=digest(p)) for p in root.rglob('*') if p.is_file() and p!=manifest and p.relative_to(root).as_posix() not in paths]
 return dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),manifest=str(manifest),manifest_sha256=digest(manifest),scope='listed payloads plus manifest only; extras explicitly inventoried but not claimed sealed',verified_payloads=rows,canonical_pdf_sha256=digest(pdf),pages=pages,latex_inputs_verified=inputs,unlisted_files=extras,exact=True,manuscript_quality_or_originality_certified=False)

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('manifest');ap.add_argument('--out',required=True);args=ap.parse_args()
 out=verify(args.manifest);Path(args.out).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(dict(payloads=len(out['verified_payloads']),pages=out['pages'],unlisted=len(out['unlisted_files']),exact=True)))
