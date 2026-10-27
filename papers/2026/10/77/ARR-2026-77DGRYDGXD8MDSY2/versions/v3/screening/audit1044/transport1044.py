from pathlib import Path
import json,hashlib
P=Path(__file__).parent;root=Path(r'C:\Trabajo\physmath-knowledge-tree\weyl-stability-20261024\integrations\research-radar\evidence\2026-10-27-principal-bkm');sha=lambda b:hashlib.sha256(b).hexdigest();rows=[]
for x in json.loads((root/'MANIFEST1036.json').read_text())['files']:
 f=root/x['path'];row={'path':x['path'],'present':f.is_file()}
 if f.is_file():b=f.read_bytes();row.update(bytes=len(b),sha256=sha(b),matches=sha(b)==x['sha256'] and len(b)==x['bytes'])
 rows.append(row)
trans=[]
for x in json.loads((root/'TRANSPORT1036.json').read_text())['files']:
 f=root/x['path'];dirname='2026-10-27_principal1033' if x['path'].startswith('principal1033/') else '2026-10-27_bkm1035';original=Path(r'D:\Proyectos\airr-investigacion')/dirname/Path(x['path']).name;row={'path':x['path'],'original_sha_matches':sha(original.read_bytes())==x['original_sha256'],'present':f.is_file()}
 if f.is_file():row.update(repository_sha_matches=sha(f.read_bytes())==x['repository_sha256'],LF_equal=original.read_bytes().replace(b'\r\n',b'\n')==f.read_bytes())
 trans.append(row)
out={'scope':'Read-only local selected-LF transport verification; no Git operation or remote PR/Pages/CI verification','manifest_sha256':sha((root/'MANIFEST1036.json').read_bytes()),'transport_sha256':sha((root/'TRANSPORT1036.json').read_bytes()),'manifest_rows':rows,'transport_rows':trans,'all_local_payloads_match':all(x.get('matches',False) for x in rows),'all_local_transport_match':all(x.get('repository_sha_matches',False) and x.get('original_sha_matches',False) and x.get('LF_equal',False) for x in trans),'public_PR_information':'Parent-reported source34400956487e21509b5196884caa320907b26f58,merge0ca8ab47e612e9f777ab6ac984ad074a77cca510; not independently reattested here'}
(P/'TRANSPORT_CHECK1044.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if not k.endswith('_rows')}))
