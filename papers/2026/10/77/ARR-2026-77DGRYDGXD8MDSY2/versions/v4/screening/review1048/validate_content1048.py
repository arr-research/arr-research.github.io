"""Read-only content validation; writes only its own result, never a registry."""
from pathlib import Path
import json,hashlib,datetime,re
from decimal import Decimal
P=Path(__file__).resolve().parent
a=json.loads((P/'ARR-CONTENT-UNBOUND1048.json').read_text(encoding='utf-8'))
v=json.loads((P/'verdict1048.json').read_text(encoding='utf-8'))
errors=[]
def check(value,message):
    if not value: errors.append(message)
criteria={'correctness_confidence','rigor','novelty','significance','reproducibility'}
lists={'strengths','weaknesses','potential_errors','strong_novelty_candidates','unresolved_material_objections'}
fields={'canonical_sha256','provider','model_id','assessed_at','prompt_version','independence','recommendation','millennium_score','overall_stars','criteria','summary'}|lists
check(set(a)==fields,'content-only field set mismatch')
check(re.fullmatch('[0-9a-f]{64}',a['canonical_sha256']) is not None,'PDF hash format')
check(a['canonical_sha256']==v['manuscript_sha256'],'PDF binding differs from verdict')
check(2<=len(a['provider'])<=100 and 2<=len(a['model_id'])<=160,'provider/model length')
check('unattested' in a['model_id'],'effective identity must not be attested')
check(datetime.datetime.fromisoformat(a['assessed_at']).tzinfo is not None,'timestamp needs offset')
check(a['prompt_version']=='ARR-ASSESS-1.0','content format version')
check(a['independence']=='involved_in_manuscript','context involvement must be explicit')
check(a['recommendation'] in {'accept','minor_revision','major_revision','reject'},'recommendation enum')
score=Decimal(str(a['millennium_score']))
check(0<=score<=10 and score.as_tuple().exponent>=-2,'score bounds/precision')
check(a['overall_stars']==max(1,min(10,int(score+Decimal('.5')))),'whole-star conversion')
check(a['millennium_score']==v['overall_millennium_0_10'],'global score differs from verdict')
check(a['criteria']==v['criteria_1_5'],'criteria differ from verdict')
check(set(a['criteria'])==criteria,'criterion set')
for k,c in a['criteria'].items():
    check(set(c)=={'stars','basis'} and type(c['stars']) is int and 1<=c['stars']<=5,'criterion format:'+k)
    check(15<=len(c['basis'].strip())<=600,'criterion basis length:'+k)
check(40<=len(a['summary'].strip())<=1600,'summary length')
for k in lists:
    check(isinstance(a[k],list) and len(a[k])<=12,'list size:'+k)
    for x in a[k]:check(isinstance(x,str) and 8<=len(x.strip())<=800,'finding length:'+k)
check(not a['unresolved_material_objections'],'no unlisted material objection may be omitted')
check(a['recommendation']!='accept' or a['millennium_score']>=3,'scientific acceptable floor')
check('6.1/10' in a['summary'] and '8.7/10' in a['summary'],'separate scores omitted')
check(a['weaknesses']==[x['id']+': '+x['finding'] for x in v['findings_and_limits']],'findings must all be projected')
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'content_subset_valid':not errors,'errors':errors,
 'native_registry_validation_performed':False,'native_record_importable':False,
 'reason':'No paper/version/assessment identity supplied. No IDs or synthetic Paper object were invented. This validates only the content constraints read from assessmentlib.py.',
 'repository_mutated':False,'content_sha256':hashlib.sha256((P/'ARR-CONTENT-UNBOUND1048.json').read_bytes()).hexdigest()}
q=P/'ARR-VALIDATION1048.json';assert not q.exists();q.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))
assert not errors,errors
