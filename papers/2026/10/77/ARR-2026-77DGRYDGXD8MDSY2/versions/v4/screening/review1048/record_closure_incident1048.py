from pathlib import Path
import json,hashlib,datetime,shutil
P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
H=P/'closure-history';H.mkdir(exist_ok=False)
for n in ['REVIEW1048.txt','verdict1048.json','PROVENANCE1048.json','ARR-BINDING-LIMITS1048.json','INCIDENTS1048.json']:
    shutil.copy2(P/n,H/n)
receipt=[]
for base in [Path(r'C:\Trabajo\airr\2026-10-27_complete1047'),Path(r'D:\Proyectos\airr-investigacion\2026-10-27_complete1047')]:
    m=json.loads((base/'FROZEN1047.json').read_text(encoding='utf-8'))
    expected={x['path'].replace('\\','/') for x in m['files']}|{'FROZEN1047.json'}
    assert sha(base/'FROZEN1047.json')=='406dcccd5be71ac41d6c96a54fe3e415349b64d8c89a29d7fe043801661d835e'
    assert all(sha(base/x['path'])==x['sha256'] for x in m['files'])
    extra=[{'path':q.relative_to(base).as_posix(),'bytes':q.stat().st_size,'sha256':sha(q)} for q in sorted(base.rglob('*')) if q.is_file() and q.relative_to(base).as_posix() not in expected]
    receipt.append({'root':str(base),'frozen_payloads_unchanged':True,'nonmanifest_files':extra})
incident={'id':'I6','type':'closure_assertion_too_strict','status':'retained_and_corrected_without_scientific_restart',
 'detail':'close1048.py failed at line23 asserting the entire input directory file set equals the frozen manifest. C contains15 additional build/source-helper files; D contains exactly the11 frozen files. All10payload hashes and FROZEN match in both roots. Initial1048 verification covered frozen files, not an exhaustive C-directory baseline, so no claim is made about when extras appeared. Extras were only inventoried/hashed, not read as scientific input or executed. No input was edited. The closure script now verifies the declared frozen set and explicitly records auxiliary files. Scientific conclusions and all grades are unchanged.',
 'failed_script':'close1048.py','failure_record':'CLOSURE-FAILED1048.txt','corrected_closure':'close1048_v2.py','history':'closure-history/ preserves pre-closure outputs; these are not separate reviews or votes.'}
write('CLOSURE-INCIDENT1048.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'incident':incident,'checks':receipt})
(P/'CLOSURE-FAILED1048.txt').write_text('Transcripción del resultado de herramienta, primer intento de cierre1048:\nexit_code: 1\nFile close1048.py, line23:\nassert {p.relative_to(base).as_posix() for p in files(base)}==expected\nAssertionError\nNo output files or archive had been written at this point. The failing original script is retained unchanged.\n',encoding='utf-8')
inc=json.loads((P/'INCIDENTS1048.json').read_text(encoding='utf-8'));inc['incidents'].append(incident);write('INCIDENTS1048.json',inc)
with (P/'REVIEW1048.txt').open('a',encoding='utf-8') as f:
    f.write('\nADENDA OPERATIVA DE CIERRE — SIN CAMBIO DE JUICIO\n\nEl primer cierre falló por una aserción demasiado estricta: comparaba todo el directorio C con el conjunto del manifiesto. C conserva15 archivos auxiliares fuera del congelado y D contiene los11 archivos congelados. Se verificó que los diez payloads y FROZEN1047 siguen idénticos a los hashes esperados en ambas ubicaciones. No había inventario exhaustivo inicial de auxiliares de C y no se afirma cuándo aparecieron. Se inventariaron y hashificaron sin leerlos como entrada científica ni ejecutarlos. Se conserva el guion fallido, la transcripción, el inventario y los documentos anteriores a esta adenda en closure-history. El cierre corregido verifica el conjunto congelado y registra los auxiliares aparte. Ningún original se modificó, ninguna comprobación científica se reinició y ninguna nota o recomendación cambió. Véase CLOSURE-INCIDENT1048.json e I6.\n')
rh=sha(P/'REVIEW1048.txt')
v=json.loads((P/'verdict1048.json').read_text(encoding='utf-8'));v['evidence']['report_sha256']=rh;write('verdict1048.json',v)
v=json.loads((P/'PROVENANCE1048.json').read_text(encoding='utf-8'));v['full_review_sha256']=rh;v['closure_incident']='CLOSURE-INCIDENT1048.json';write('PROVENANCE1048.json',v)
v=json.loads((P/'ARR-BINDING-LIMITS1048.json').read_text(encoding='utf-8'));v['source_report_sha256']=rh;v['source_verdict_sha256']=sha(P/'verdict1048.json');write('ARR-BINDING-LIMITS1048.json',v)
src=(P/'close1048.py').read_text(encoding='utf-8')
src=src.replace('checks=[]\n','checks=[]\nextras=[]\n',1)
old="    assert {p.relative_to(base).as_posix() for p in files(base)}==expected"
new="    actual={p.relative_to(base).as_posix() for p in files(base)}\n    assert expected <= actual\n    extras.append({'root':str(base),'nonmanifest_files':[{'path':n,'bytes':(base/n).stat().st_size,'sha256':sha(base/n)} for n in sorted(actual-expected)]})"
assert old in src;src=src.replace(old,new,1)
src=src.replace("'files_per_copy_including_frozen':11,","'frozen_files_per_copy':11,'nonmanifest_inventory':extras,",1)
assert not (P/'close1048_v2.py').exists()
(P/'close1048_v2.py').write_text(src,encoding='utf-8')
print(json.dumps({'incident_recorded':True,'scientific_verdict_unchanged':True,'nonmanifest_counts':[len(x['nonmanifest_files']) for x in receipt],'final_report_sha256':rh},indent=2))
