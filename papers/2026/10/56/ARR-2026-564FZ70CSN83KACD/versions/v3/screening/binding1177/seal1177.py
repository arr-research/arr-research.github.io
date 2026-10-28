from pathlib import Path
import json,hashlib,datetime,shutil,sys
R=Path(__file__).resolve().parent
D=Path(r'D:\Proyectos\airr-investigacion\2026-10-28_cq1177-binding')
OC=Path(r'C:\Trabajo\airr\2026-10-28_cq1168-review')
OD=Path(r'D:\Proyectos\airr-investigacion\2026-10-28_cq1168-review')
REPO=Path(r'C:\Trabajo\airr-publicacion\reviewed-publications-20261026')
V3=REPO/'papers/2026/10/56/ARR-2026-564FZ70CSN83KACD/versions/v3'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def dump(p,v): p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
def inv(root): return [{'path':p.relative_to(root).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(root.rglob('*')) if p.is_file()]
assert not D.exists(),'Inspect an existing archive; never overwrite a closure silently'
original_C,original_D=inv(OC),inv(OD)
initial=json.loads((R/'ORIGINALS-INITIAL1177.json').read_text(encoding='utf-8'))
assert original_C==original_D and len(original_C)==1070
digest=hashlib.sha256(json.dumps(original_C,sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert digest==initial['inventory_sha256']
for row in inv(R/'original1168'): assert row==next(x for x in original_C if x['path']==row['path'])
dump(R/'ORIGINALS-FINAL1177.json',{'utc':utc(),'status':'pass','files':1070,'C_D_identical':True,'all_original_bytes_unchanged':True,'inventory_sha256':digest,'attached_originals_byte_identical':True})
sys.path.insert(0,str(REPO/'scripts'))
from assessmentlib import normalize_model_response,validate_assessment,source_hash,canonical_json
from arrlib import Paper,sha256
response=json.loads((R/'model-response.json').read_text(encoding='utf-8'))
meta_raw=(V3/'metadata.json').read_bytes();meta=json.loads(meta_raw)
errors=validate_assessment(normalize_model_response(response),[Paper(V3,meta)])
assert not errors,errors
assert sha256(V3/'paper.pdf')==response['canonical_sha256']
assert (V3/'paper.pdf').stat().st_size==452673
assert canonical_json(response)==(R/'model-response.canonical.json').read_bytes()
binding=json.loads((R/'BINDING1177.json').read_text(encoding='utf-8'))
assert sha(R/'model-response.json')==binding['raw_response_sha256']
assert source_hash(response)==binding['canonical_response_sha256']
assert response['assessed_at']==binding['original_assessed_at']=='2026-10-28T01:14:36.368051+00:00'
assert response['millennium_score']==7.0 and response['overall_stars']==7
assert all(c['stars']==4 for c in response['criteria'].values())
assert response['provider']=='OpenAI' and response['model_id']=='unknown' and response['independence']=='involved_in_manuscript'
assert response['recommendation']=='accept' and response['unresolved_material_objections']==[]
for oid in ['O1','O2','O3','O4','O5']: assert any(x.startswith(oid+' ') for x in response['weaknesses'])
assert meta['record_id']==binding['local_record']['record_id'] and meta['version_id']==binding['local_record']['version_id']
guards=json.loads((R/'READONLY-SOURCES-INITIAL1177.json').read_text(encoding='utf-8'))
guard_result=[dict(x,current_sha256=sha(Path(x['path'])),unchanged=(x['sha256']==sha(Path(x['path'])))) for x in guards]
# These are read-only evidence snapshots, never substitute metadata fixtures in the repo.
(R/'local-record/metadata-v3.final.json').write_bytes(meta_raw)
dump(R/'VALIDATION-FINAL1177.json',{'utc':utc(),'status':'pass','errors':errors,'official_validator':'assessmentlib.validate_assessment against actual localv3 Paper','raw_response_sha256':sha(R/'model-response.json'),'canonical_response_sha256':source_hash(response),'assessed_at_original':response['assessed_at'],'actual_metadata_sha256':hashlib.sha256(meta_raw).hexdigest(),'actual_pdf_sha256':sha(V3/'paper.pdf'),'actual_pdf_bytes':452673,'source_guards':guard_result,'registry_write_performed':False,'no_new_scientific_review':True,'no_publication_or_native_receipt_inferred':True,'temporary_validator_generated_assessment_id_persisted':False})
for p in R.rglob('*.json'): json.loads(p.read_text(encoding='utf-8-sig'))
payloads=[x for x in inv(R) if x['path'] not in {'MANIFEST1177.json','C_D-CLOSURE1177.json'}]
dump(R/'MANIFEST1177.json',{'utc':utc(),'kind':'serialization1177 of original review1168, not new assessment','payload_count':len(payloads),'files':payloads,'excludes':['MANIFEST1177.json','C_D-CLOSURE1177.json'],'exclusion_reason':'Avoid self/circular hashing; closure binds manifest, and final direct C/D comparison includes closure.'})
files_before=inv(R)
D.mkdir(parents=True)
for row in files_before:
    dest=D/row['path'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(R/row['path'],dest)
assert files_before==inv(D)==inv(R)
assert original_C==inv(OC)==inv(OD)
closure={'utc':utc(),'status':'terminal','operation':'serialization only, same scientific review1168','C':str(R),'D':str(D),'C_D_identical':True,'total_files':len(files_before)+1,'manifest_payloads':len(payloads),'manifest_sha256':sha(R/'MANIFEST1177.json'),'response_raw_sha256':sha(R/'model-response.json'),'response_canonical_sha256':source_hash(response),'binding_sha256':sha(R/'BINDING1177.json'),'source_report_sha256':binding['source_report_sha256'],'source_verdict_sha256':binding['source_verdict_sha256'],'original1168_files_unchanged':1070,'original_C_D_identical_after_copy':True,'original_assessed_at':response['assessed_at'],'no_new_vote_or_evaluation':True,'no_registry_Git_or_publication_mutation':True,'no_new_native_receipt_claim':True,'closure_compared_in_final_direct_inventory':True}
dump(R/'C_D-CLOSURE1177.json',closure)
shutil.copyfile(R/'C_D-CLOSURE1177.json',D/'C_D-CLOSURE1177.json')
assert inv(R)==inv(D)
print(json.dumps({'status':'terminal','files':len(inv(R)),'payloads':len(payloads),'response_raw_sha256':sha(R/'model-response.json'),'response_canonical_sha256':source_hash(response),'binding_sha256':sha(R/'BINDING1177.json'),'manifest_sha256':sha(R/'MANIFEST1177.json'),'closure_sha256':sha(R/'C_D-CLOSURE1177.json'),'original1168_unchanged':1070,'readonly_sources_all_unchanged':all(x['unchanged'] for x in guard_result)}))
