"""Seal a format-only binding; preserve original reviews and repository state."""
from pathlib import Path
import datetime,hashlib,json,shutil
ROOT=Path(__file__).resolve().parent
REPO=Path('C:/Trabajo/airr-publicacion/reviewed-publications-20261026')
PAPER=REPO/'papers/2026/10/77/ARR-2026-77DGRYDGXD8MDSY2'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,data):
    with (ROOT/name).open('x',encoding='utf-8') as f:json.dump(data,f,ensure_ascii=False,indent=2);f.write('\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
validation=json.loads((ROOT/'VALIDATION1010-run01.json').read_text(encoding='utf-8'))
assert validation['actual_repository_record_validation']['passed']
assert validation['artifact_backed_in_memory_validation']['passed'] and not validation['json_schema_errors']
assert not validation['repo_files_changed_during_run'] and validation['all_faithfulness_checks_pass']
metadata=json.loads((PAPER/'metadata.json').read_text(encoding='utf-8'))
save('REGISTRY-SNAPSHOT1010-final.json',{'utc':now,'path':str(PAPER/'metadata.json'),'sha256':sha(PAPER/'metadata.json'),'metadata':metadata,'note':'Record populated externally by coordinator before successful validation; this binding process did not modify it.'})
binding=json.loads((ROOT/'BINDING1010.json').read_text(encoding='utf-8'))
shutil.copy2(ROOT/'BINDING1010.json',ROOT/'BINDING1010-initial.json')
binding['validation_result']={'file':'VALIDATION1010-run01.json','sha256':sha(ROOT/'VALIDATION1010-run01.json'),
 'native_actual_record_passed':True,'json_schema_passed':True,'faithfulness_passed':True,
 'actual_metadata_sha256_at_validation':validation['actual_repository_record_validation']['metadata_sha256'],
 'repository_unchanged_by_validator':True,'normalized_assessment_persisted':False,'new_assessment_vote_created':False}
binding['initial_record_snapshot_note']='Initial read saw template metadata. Coordinator populated metadata and exact PDF before native validation; initial and final read-only snapshots are both retained. No scientific reassessment occurred.'
with (ROOT/'BINDING1010.json').open('w',encoding='utf-8') as f:json.dump(binding,f,ensure_ascii=False,indent=2);f.write('\n')
source_checks=[]
for ident,expected_manifest in [('1006','6c26d3f926ada0834dfb237f040ced2035141a371fddccb1e2f7d5a0695422e4'),('998','c972b8f464d772b757661288bb8c4c984daa9d9c29e59d9d684193a8c346f5d3')]:
    for loc,base in [('C',Path(f'C:/Trabajo/airr/2026-10-27_sharp{ident}-review')),('D',Path(f'D:/Proyectos/airr-investigacion/2026-10-27_sharp{ident}-review'))]:
        m=base/f'MANIFEST{ident}.json';assert sha(m)==expected_manifest
        manifest=json.loads(m.read_text(encoding='utf-8'))
        valid=all(sha(base/x['path'])==x['sha256'] and (base/x['path']).stat().st_size==x['bytes'] for x in manifest['files'])
        source_checks.append({'review':ident,'location':loc,'payloads':len(manifest['files']),'all_valid':valid,'manifest_sha256':sha(m)})
        assert valid
copied_checks=[]
for x in binding['source_files_copied_unchanged']:
    valid=sha(ROOT/x['path'])==x['sha256']==sha(Path(x['original_path']))
    copied_checks.append({'path':x['path'],'sha256':x['sha256'],'identical_to_original':valid});assert valid
assert sha(ROOT/'model-response.json')==binding['model_response_file_sha256']
schema_checks=[]
for x in binding['schema_sources']:
    valid=sha(REPO/x['path'])==x['sha256'];schema_checks.append({'path':x['path'],'sha256':x['sha256'],'unchanged':valid});assert valid
save('CLOSING1010.json',{'utc':now,'source_reviews':source_checks,'copied_originals':copied_checks,'schema_sources':schema_checks,
 'model_response_unchanged_since_validation':True,'current_repository_pdf_sha256':sha(PAPER/'paper.pdf'),
 'scope':'Content integrity and format binding only; no publication or editorial acceptance.'})
assert sha(PAPER/'paper.pdf')==binding['public_binding']['canonical_sha256']
save('INCIDENTS1010.json',{'utc':now,'scientific_reassessment':False,'new_scores':False,'additional_vote':False,
 'schema_validation_errors':0,'native_actual_record_validation_errors':0,'faithfulness_errors':0,
 'observations':[{'event':'Initial public record metadata was still a template and lacked a PDF hash.','handling':'Coordinator informed; no repository edits by serializer. Coordinator populated the real record before the first validator run. That first run passed against the actual record. Both snapshots retained.'},
 {'event':'Native schema has no separate numeric fields for importance or technical quality and cannot contain the full report in its bounded summary.','handling':'All three axes and their verbatim bases retained in BINDING1010 and original verdict; all three values appear in response summary. Complete original report provided as mandatory public companion.'}],
 'runtime_attestation_invented':False,'operator_provenance_fields_invented':False,'mutators_run':False,
 'original_1006_998_modified':False,'publication_or_editorial_action':False,
 'binding_draft_retained':'BINDING1010-initial.json preserved before adding successful validation result.'})
excluded={'MANIFEST1010.json','COPY-RECEIPT1010.json'}
files=[{'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name not in excluded]
save('MANIFEST1010.json',{'binding':'1010','utc':now,'scope':'Format-only serialization of same review1006, with full unchanged report and distinct historical998. No new review/vote.','files':files,'excluded_to_avoid_self_reference':sorted(excluded)})
print(json.dumps({'files_manifested':len(files),'response_sha256':sha(ROOT/'model-response.json'),'binding_sha256':sha(ROOT/'BINDING1010.json'),'manifest_sha256':sha(ROOT/'MANIFEST1010.json')},indent=2))
