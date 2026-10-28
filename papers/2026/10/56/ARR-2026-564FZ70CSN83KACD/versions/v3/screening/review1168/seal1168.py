from pathlib import Path
import json,hashlib,datetime,shutil
from prepare1168 import verify,inventory,sha
R=Path(__file__).resolve().parent
D=Path(r'D:\Proyectos\airr-investigacion\2026-10-28_cq1168-review')
def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def dump(path,obj): path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not D.exists(),'Destination exists; inspect rather than overwrite a prior closure'
initial=json.loads((R/'INPUT-INITIAL1168.json').read_text(encoding='utf-8'))
final=verify()
assert final['files']==initial['files']==inventory(R/'input')
final.pop('scientific_reading_started_before_check',None)
final.update(phase='final_after_scientific_work_before_archive',unchanged_from_initial=True,own_input_copy_identical=True,pdf_pages=21)
dump(R/'INPUT-FINAL1168.json',final)
v=json.loads((R/'verdict1168.json').read_text(encoding='utf-8'))
text=(R/'REVIEW1168.txt').read_text(encoding='utf-8')
assert v['report']['sha256']==sha(R/'REVIEW1168.txt')
assert v['manuscript']['pdf_sha256']==final['pdf_sha256']
assert v['manuscript']['bytes']==452673 and v['manuscript']['pages']==21
assert [v[x] for x in ['scientific_importance_airr_0_10','overall_millennium_0_10','technical_quality_0_10']]==[7.3,7.0,9.0]
assert all(x['rating_1_5']==4 for x in v['criteria'].values()) and len(v['criteria'])==5
assert [x['id'] for x in v['objections']]==['O1','O2','O3','O4','O5']
assert all(x in text for x in ['7.3/10','7.0/10','9.0/10','O1.','O2.','O3.','O4.','O5.'])
assert v['observed_configuration']['effective_model_id']=='unknown'
assert v['native_arr_paper_id'] is None and v['native_arr_version_id'] is None
assert sha(R/'RUBRIC1168.md')=='41829e068687a57afd35eaa9aa5afd99a1f09a8f651bc522dbd871f0b31ff750'
own=json.loads((R/'OWN1168.json').read_text(encoding='utf-8'))
assert own['status']=='pass' and len(own['rows'])==12 and all(x['pass'] for x in own['rows'])
replay=json.loads((R/'replay/REPLAY1167.json').read_text(encoding='utf-8'))
assert replay['status']=='pass' and replay['inputs_unchanged']==929
for p in R.glob('*.json'): json.loads(p.read_text(encoding='utf-8-sig'))
dump(R/'VALIDATION1168.json',dict(utc=utc(),status='pass',kind='internal report/verdict consistency and input-integrity validation; not a new scientific evaluation or native ARR validation',report_sha256=sha(R/'REVIEW1168.txt'),verdict_sha256=sha(R/'verdict1168.json'),pdf_sha256=final['pdf_sha256'],pdf_bytes=452673,pdf_pages=21,manifest1167_sha256=final['manifest_sha256'],initial_final_originals_and_localcopy_identical=True,input_files=929,criteria_count=5,objections=['O1','O2','O3','O4','O5'],own_controls=12,inherited_replay='pass',effective_identity_unknown=True,no_native_ids=True))
excluded={'MANIFEST1168.json','C_D-CLOSURE1168.json'}
payloads=[x for x in inventory(R) if x['path'] not in excluded]
manifest=dict(utc=utc(),kind='complete review1168 dossier manifest',payload_count=len(payloads),files=payloads,excludes=sorted(excluded),exclusion_reason='Manifest cannot hash itself; closure binds this manifest and is then compared byte-for-byte across C/D.',contains_frozen_input_copy=True,foreign_downloaded_corpus=False)
dump(R/'MANIFEST1168.json',manifest)
before=inventory(R)
D.mkdir(parents=True)
for row in before:
    dest=D/row['path'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(R/row['path'],dest)
assert before==inventory(D)==inventory(R)
after_inputs=verify()
assert after_inputs['files']==initial['files']==inventory(R/'input')
closure=dict(utc=utc(),status='terminal',C=str(R),D=str(D),identical=True,total_files=len(before)+1,manifest_payloads=len(payloads),manifest_sha256=sha(R/'MANIFEST1168.json'),report_sha256=sha(R/'REVIEW1168.txt'),verdict_sha256=sha(R/'verdict1168.json'),pdf_sha256=final['pdf_sha256'],input_manifest_sha256=final['manifest_sha256'],original_inputs_reverified_after_archive=True,original_input_files=929,original_input_C_D_identical_and_unchanged=True,own_input_copy_identical=True,comparison='Every relative file path, byte length and SHA256 identical; closure excluded from manifest to avoid circularity, written identically and included in final direct C/D comparison.',one_full_review=True,no_publication=True,no_editorial_acceptance=True)
dump(R/'C_D-CLOSURE1168.json',closure)
shutil.copyfile(R/'C_D-CLOSURE1168.json',D/'C_D-CLOSURE1168.json')
assert inventory(R)==inventory(D)
print(json.dumps(dict(status='terminal',files=len(inventory(R)),C_D_identical=True,report_sha256=sha(R/'REVIEW1168.txt'),verdict_sha256=sha(R/'verdict1168.json'),manifest_sha256=sha(R/'MANIFEST1168.json'),closure_sha256=sha(R/'C_D-CLOSURE1168.json'),inputs_unchanged=929)))
