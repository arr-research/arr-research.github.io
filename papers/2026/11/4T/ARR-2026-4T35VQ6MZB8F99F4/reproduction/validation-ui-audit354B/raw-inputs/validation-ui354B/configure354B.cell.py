# Fill only with actual observations and reviewed raw evidence. Blank defaults cannot run.
ACTUAL={
 'validation_own_runtime':False,'validation_runtime_type':'',
 'validation_session_reference':'','validation_hostname':'','observed_at':'',
 'production_hostname':'','production_session_reference':'','production_runtime_closed':False,
 'production_closure_sha256':'','production_closure_base64':'',
 'return_bytes':None,'return_sha256':'','parts':[],
 'validator_B_review_accepted':False,'validator_B_review_sha256':'','validator_B_review_base64':'',
 'UI_review_accepted':False,'UI_review_sha256':'','UI_review_base64':'',
 'reviewed_UI_notebook_sha256':'','reviewed_UI_subject_verified':False
}
need(ACTUAL['validation_own_runtime'] is True and ACTUAL['validation_runtime_type']=='CPU','Own CPU observation required')
need(ACTUAL['validation_hostname']==platform.node(),'Observed validation host must match actual host')
for key in ('validation_session_reference','observed_at','production_hostname','production_session_reference'):
    need(isinstance(ACTUAL[key],str) and bool(ACTUAL[key].strip()),'Missing actual '+key)
need(ACTUAL['production_hostname']!=platform.node() and ACTUAL['production_session_reference']!=ACTUAL['validation_session_reference'],'Validation must use a separate own session')
need(ACTUAL['production_runtime_closed'] is True,'Production closure must be observed first')
need(ACTUAL['validator_B_review_accepted'] is True and ACTUAL['UI_review_accepted'] is True
     and ACTUAL['reviewed_UI_subject_verified'] is True,'Actual separate reviews and exact notebook subject verification required')
need(re.fullmatch('[0-9a-f]{64}',ACTUAL['reviewed_UI_notebook_sha256']) is not None,'Exact reviewed notebook hash required')
# This is an explicit operator observation, not a self-attestation of the notebook hash.
for row in PAYLOADS:
    path=BASE/row['path'];need(path.is_file() and not path.is_symlink(),'Frozen B regular file')
    b=path.read_bytes();need(len(b)==row['bytes'] and digest(b)==row['sha256'],'Frozen B unchanged before use')
sys.path.insert(0,str(BASE))
from atomic354A import publish_bytes,publish_exit,read_exit
for stem,out in [('production_closure',BASE/'production-closure354B.txt'),
                 ('validator_B_review',UI/'validator-B-review354B.raw'),('UI_review',UI/'UI-review354B.raw')]:
    raw=base64.b64decode(ACTUAL[stem+'_base64'],validate=True)
    need(0<len(raw)<16_000_000 and re.fullmatch('[0-9a-f]{64}',ACTUAL[stem+'_sha256']) is not None,'Actual bounded evidence')
    publish_bytes(out,raw,len(raw),ACTUAL[stem+'_sha256'])
need(type(ACTUAL['return_bytes']) is int and 0<ACTUAL['return_bytes']<512_000_000,'Actual return size')
need(re.fullmatch('[0-9a-f]{64}',ACTUAL['return_sha256']) is not None,'Actual return hash')
need(isinstance(ACTUAL['parts'],list) and 0<len(ACTUAL['parts'])<10000,'Actual ordered chunk plan')
parts=[]
for i,row in enumerate(ACTUAL['parts']):
    need(type(row['index']) is int and row['index']==i and type(row['bytes']) is int and row['bytes']>0,'Actual chunk index/size')
    need(re.fullmatch('[0-9a-f]{64}',row['sha256']) is not None,'Actual chunk hash')
    parts.append(dict(index=i,path=f'incoming354B/part-{i:04d}.b64',bytes=row['bytes'],sha256=row['sha256']))
need(sum(r['bytes'] for r in parts)==ACTUAL['return_bytes'],'Actual planned total')
config=dict(source=SOURCE,status='ACTUAL_INPUT_AND_OWN_RUNTIME_OBSERVED',bytes=ACTUAL['return_bytes'],sha256=ACTUAL['return_sha256'],
 validation_own_runtime=True,validation_hostname=platform.node(),validation_session_reference=ACTUAL['validation_session_reference'],
 observed_at=ACTUAL['observed_at'],production_runtime_closed=True,production_closure_evidence='production-closure354B.txt',
 production_closure_sha256=ACTUAL['production_closure_sha256'])
plan=dict(source=SOURCE,input_name='tep354D-return.zip',bytes=ACTUAL['return_bytes'],sha256=ACTUAL['return_sha256'],parts=parts)
for path,obj in [(BASE/'ACTUAL-INPUT.json',config),(BASE/'ACTUAL-CHUNKS.json',plan)]:
    raw=(json.dumps(obj,indent=2)+'\n').encode();publish_bytes(path,raw,len(raw),digest(raw))
put(UI/'actual-configuration354B.json',{k:v for k,v in ACTUAL.items() if not k.endswith('_base64')})
(BASE/'incoming354B').mkdir()
print('Actual configuration retained; paste each actual chunk in the next cell. No validation executed.')
