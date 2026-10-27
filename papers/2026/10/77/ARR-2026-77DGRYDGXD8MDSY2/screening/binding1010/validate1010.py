"""Read-only validation of a format-only response; never record an assessment.
Imports the existing validator with bytecode disabled. Writes only own run logs.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import datetime,hashlib,json,copy
from decimal import Decimal
ROOT=Path(__file__).resolve().parent
REPO=Path('C:/Trabajo/airr-publicacion/reviewed-publications-20261026')
PAPER=REPO/'papers/2026/10/77/ARR-2026-77DGRYDGXD8MDSY2'
OLD=Path('D:/Proyectos/airr-investigacion/2026-10-27_sharp1006-review')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protected=[REPO/'scripts'/name for name in ['assessmentlib.py','prepare_model_assessment.py','arrlib.py','ratinglib.py']]
protected+=[REPO/'schema/model-assessment.schema.json',PAPER/'metadata.json',REPO/'registry/model-assessments.json']
before={str(p):sha(p) for p in protected}
sys.path.insert(0,str(REPO/'scripts'))
from arrlib import Paper
from assessmentlib import normalize_model_response,validate_assessment,source_hash
response=json.loads((ROOT/'model-response.json').read_text(encoding='utf-8'))
normalized=normalize_model_response(response)
actual=Paper(PAPER,json.loads((PAPER/'metadata.json').read_text(encoding='utf-8')))
actual_errors=validate_assessment(normalized,[actual])
assert sha(OLD/'input/main.pdf')==response['canonical_sha256']
artifact_metadata={'id':response['paper_id'],'version':response['version'],'version_id':response['version_id'],
 'source_of_truth':'external_pdf','integrity':{'canonical_sha256':response['canonical_sha256']}}
candidate=Paper(OLD/'input',artifact_metadata)
artifact_errors=validate_assessment(normalized,[candidate])
schema_errors=[]
try:
    import jsonschema
    schema=json.loads((REPO/'schema/model-assessment.schema.json').read_text(encoding='utf-8'),parse_float=Decimal)
    decimal_normalized=json.loads(json.dumps(normalized),parse_float=Decimal)
    validator=jsonschema.Draft202012Validator(schema,format_checker=jsonschema.FormatChecker())
    schema_errors=[{'path':list(e.absolute_path),'message':e.message} for e in validator.iter_errors(decimal_normalized)]
    schema_status='checked'
except ImportError as exc:
    schema_status='unavailable';schema_errors=[{'error':repr(exc)}]
v=json.loads((OLD/'verdict1006.json').read_text(encoding='utf-8'))
binding=json.loads((ROOT/'BINDING1010.json').read_text(encoding='utf-8'))
faithfulness=[]
for target,source in binding['criterion_key_mapping'].items():
    faithful=response['criteria'][target]=={'stars':v['five_criteria'][source]['stars_1_5'],'basis':v['five_criteria'][source]['basis']}
    faithfulness.append({'field':'criteria.'+target,'unchanged_value_and_basis':faithful})
for old_key,new_key in [('overall_millennium_0_10','millennium_score'),('overall_public_whole_stars','overall_stars')]:
    faithfulness.append({'field':new_key,'unchanged_value_and_basis':response[new_key]==v[old_key]})
for key in ['scientific_importance_airr_0_10','technical_quality_0_10']:
    faithfulness.append({'field':key,'unchanged_value_and_basis':binding['scores_preserved'][key]==v[key]})
after={str(p):sha(p) for p in protected}
changes=[p for p in before if before[p]!=after[p]]
report={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'response_file_sha256':sha(ROOT/'model-response.json'),'canonical_response_sha256':source_hash(response),
 'native_validator_source':str(REPO/'scripts/assessmentlib.py'),'schema_source':str(REPO/'schema/model-assessment.schema.json'),
 'json_schema_status':schema_status,'json_schema_errors':schema_errors,
 'artifact_backed_in_memory_validation':{'errors':artifact_errors,'passed':not artifact_errors,
  'scope':'Schema/response against operator-specified IDs and independently rehashed exact reviewed PDF. Synthetic in-memory Paper only; not a production-registry validation.'},
 'actual_repository_record_validation':{'metadata_sha256':before[str(PAPER/'metadata.json')],'errors':actual_errors,'passed':not actual_errors,
  'metadata_source_of_truth':actual.metadata.get('source_of_truth'),'recorded_integrity':actual.metadata.get('integrity',{})},
 'faithfulness_checks':faithfulness,'all_faithfulness_checks_pass':all(x['unchanged_value_and_basis'] for x in faithfulness),
 'repo_files_changed_during_run':changes,'repository_snapshots_before':before,'repository_snapshots_after':after,
 'normalization':'normalize_model_response created a transient validation-only UUID in memory. No normalized assessment or registry entry was saved. No new vote.',
 'bytecode_writes_disabled':True,'mutator_entrypoints_executed':False}
run=1
while (ROOT/f'VALIDATION1010-run{run:02d}.json').exists():run+=1
with (ROOT/f'VALIDATION1010-run{run:02d}.json').open('x',encoding='utf-8') as f:json.dump(report,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps({'run':run,'json_schema_errors':schema_errors,'artifact_backed_errors':artifact_errors,'actual_record_errors':actual_errors,'faithfulness_pass':report['all_faithfulness_checks_pass'],'repo_changed':changes},indent=2))
assert not artifact_errors and not schema_errors and not changes and report['all_faithfulness_checks_pass']
