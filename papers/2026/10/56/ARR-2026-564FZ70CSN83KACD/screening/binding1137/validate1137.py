"""Read-only official-schema and exact-record linkage validation; output only in this binding dossier."""
from pathlib import Path
import json,hashlib,sys,datetime
P=Path(__file__).resolve().parent
R=Path(r'C:\Trabajo\airr-publicacion\reviewed-publications-20261026')
RP=R/'papers/2026/10/56/ARR-2026-564FZ70CSN83KACD'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def put(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def inv(root):return {p.relative_to(root).as_posix():dict(bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(root.rglob('*')) if p.is_file()}
b=read(P/'BINDING1137.json');v=read(P/'source1128/verdict1128.json');resp=read(P/'model-response.json')
assert sha(P/'model-response.json')==b['model_response_raw_sha256']
assert sha(P/'source1128/REVIEW1128.txt')==b['source_report_sha256']=='213033661031a8ea1f9b5c278d1faaadf9e267ae5abe59a2509a130a17ae152d'
assert sha(P/'source1128/verdict1128.json')==b['source_verdict_sha256']=='c7c7aa0fae70ed8d8d436507358a64911d74fcd79ae9e89a6e53a5de97741f65'
sys.dont_write_bytecode=True
sys.path.insert(0,str(P/'schema-snapshot'))
from assessmentlib import normalize_model_response,validate_assessment,source_hash
from arrlib import Paper
for n,row in b['schema_files'].items():
    assert sha(P/'schema-snapshot'/n)==sha(R/'scripts'/n)==row['sha256']
beforemeta=(RP/'metadata.json').read_bytes();meta=json.loads(beforemeta)
metasha=hashlib.sha256(beforemeta).hexdigest()
assert meta['id']==resp['paper_id']==b['paper_id']
assert meta['version']==resp['version']==b['version']
assert meta['version_id']==resp['version_id']==b['version_id']
assert meta['record_id']==b['record_id']
assert meta['source_of_truth']=='paper.pdf'
assert meta['integrity']['canonical_sha256']==resp['canonical_sha256']
actualsha=sha(RP/'paper.pdf')
assert actualsha==resp['canonical_sha256']=='3a08346e76b1a168aa3759921ae336aa6d97bd739eb61f8b42fa800b3b18f783'
assert (RP/'paper.pdf').stat().st_size==383617
assert resp['model_id']=='unknown' and resp['independence']=='involved_in_manuscript'
assert resp['recommendation']=='accept' and resp['millennium_score']==6.3 and resp['overall_stars']==6
assert 'AIRR6.5/10' in resp['summary'] and 'quality8.8/10' in resp['summary']
assert resp['unresolved_material_objections']==v['unresolved_material_objections']==[]
assert all(any(t.startswith('O'+str(i)+' ') for t in resp['weaknesses']) for i in range(1,6))
assert all(any(t.startswith('I'+str(i)+' ') for t in resp['potential_errors']) for i in range(1,7))
for target,source in b['criterion_key_mapping'].items():
    assert resp['criteria'][target]==dict(stars=v['criteria_1_5'][source]['rating_1_5'],basis=v['criteria_1_5'][source]['basis'])
assert all(resp['criteria'][x]['stars']==4 for x in resp['criteria'])
norm=normalize_model_response(resp) # transient official envelope; UUID never persisted
errors=validate_assessment(norm,[Paper(RP,meta)])
assert not errors,errors
assert source_hash(resp)==b['model_response_structured_sha256']
for root in [Path(b['source_review']['C']),Path(b['source_review']['D'])]:
    assert inv(root)==b['source_review']['full_source_inventory']
assert (RP/'metadata.json').read_bytes()==beforemeta and sha(RP/'paper.pdf')==actualsha
(P/'metadata-current1137.json').write_bytes(beforemeta)
initial=read(P/'metadata-initial1137.json')
put('validation1137.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),all_passed=True,official_validate_assessment_errors=errors,actual_record_linkage_pass=True,actual_metadata_sha256=metasha,initial_metadata_sha256=sha(P/'metadata-initial1137.json'),metadata_changed_since_snapshot=metasha!=sha(P/'metadata-initial1137.json'),metadata_changes_scope='Operator populated/updated public record independently; this task only read snapshots and validated unchanged IDs and exact reviewed PDF.',locked_identifiers_unchanged=all(initial[k]==meta[k] for k in ['id','version','version_id','record_id']),actual_PDF_sha256=actualsha,actual_PDF_bytes=383617,model_response_raw_sha256=sha(P/'model-response.json'),model_response_structured_sha256=source_hash(resp),original1128_C_D_325files_unchanged=True,all_three_scores_preserved=True,five_original_criteria_and_bases_preserved=True,O1_O5_and_I1_I6_preserved=True,new_scientific_review=False,additional_vote=False,transient_assessment_id_persisted=False,operator_provenance_fabricated=False,repository_mutated=False,publication=False))
print(json.dumps(dict(all_passed=True,actual_linkage=True,metadata_sha256=metasha,model_response_sha256=sha(P/'model-response.json'),source_response_sha256=source_hash(resp),original1128_unchanged=True)))
