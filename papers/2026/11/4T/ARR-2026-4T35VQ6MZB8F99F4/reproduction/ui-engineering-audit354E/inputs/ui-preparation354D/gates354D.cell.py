# STOP HERE until a DIFFERENT agent has reviewed this exact notebook.
# Fill ONLY from that complete accepted report and an actually observed own CPU session.
NOTEBOOK_REVIEW_ACCEPTED = False
NOTEBOOK_REVIEW_REPORT_BASE64 = ''
NOTEBOOK_REVIEW_REPORT_SHA256 = ''
REVIEWED_NOTEBOOK_SHA256 = ''
OWN_RUNTIME_OBSERVED = False
OWN_CPU_KIND = ''
OWN_SESSION_REFERENCE = ''
OWNER_OBSERVED_AT = ''
OWNER_OBSERVED_HOSTNAME = ''
need(NOTEBOOK_REVIEW_ACCEPTED is True and OWN_RUNTIME_OBSERVED is True,'Unfulfilled actual review/ownership gates')
need(OWN_CPU_KIND=='CPU' and bool(OWN_SESSION_REFERENCE.strip()),'Actually observed own CPU session required')
need(OWNER_OBSERVED_HOSTNAME==platform.node() and bool(OWNER_OBSERVED_HOSTNAME),'Observed runtime hostname mismatch')
parsed=datetime.fromisoformat(OWNER_OBSERVED_AT.replace('Z','+00:00'))
need(parsed.tzinfo is not None and parsed.utcoffset() is not None,'Actual observation must have timezone')
need(re.fullmatch('[0-9a-f]{64}',NOTEBOOK_REVIEW_REPORT_SHA256 or '') is not None
     and re.fullmatch('[0-9a-f]{64}',REVIEWED_NOTEBOOK_SHA256 or '') is not None,'Review and notebook hashes required')
review=base64.b64decode(NOTEBOOK_REVIEW_REPORT_BASE64,validate=True)
need(len(review)>0 and sha(review)==NOTEBOOK_REVIEW_REPORT_SHA256,'Complete separate notebook report bytes required')
need(not (P/'gates'/'authorization.json').exists(),'Never overwrite prior authorization')
for name,raw in {**prepared,**attached}.items():
    target=P/name
    need(target.is_file() and not target.is_symlink() and target.resolve().is_relative_to(P)
         and target.read_bytes()==raw,'Materialized input changed')
ci=json.loads(attached['gates/source-ci-premerge.json'])
need(ci['headRefOid']==SOURCE,'Wrong required-CI source')
checks={c['name']:c for c in ci['statusCheckRollup']}
for name in ('honesty','lake build YangMillsCore + oracle'):
    need(name in checks and checks[name]['status']=='COMPLETED' and checks[name]['conclusion']=='SUCCESS','Actual required CI not successful')
merged=json.loads(attached['gates/source-merged-readback.json'])
need(merged['headRefOid']==SOURCE and merged['state']=='MERGED'
     and merged['mergeCommit']['oid']=='a0ee5c3a8734fdce200f353795f13f81ffa6a19a','Actual source merge mismatch')
source_accept=json.loads(attached['gates/parent-source-integration-acceptance.json'])
need(source_accept['source']==SOURCE and source_accept['verdict']=='ACCEPT_SOURCE_INTEGRATION'
     and source_accept['full_source_report_read'] is True and source_accept['full_pin_closure_read'] is True,'Actual parent source acceptance absent')
producer_accept=json.loads(attached['gates/parent-production-static-acceptance.json'])
need(producer_accept['source']==SOURCE and producer_accept['full_report_and_context_read'] is True
     and producer_accept['report_sha256']==sha(attached['gates/production-engineering-full.md'])
     and producer_accept['verdict']=='ACCEPT_FOR_PROSPECTIVE_OWN_COLAB_PRODUCTION_AFTER_REAL_GATES','Actual producer acceptance mismatch')
# Earlier producer-parent JSON retains its historically pending CI/pin fields;
# the separately captured later source acceptance and actual successful CI close those conditions.
with (P/'gates'/'notebook-engineering-review.txt').open('xb') as f:f.write(review)
owner={'own_runtime':True,'runtime_kind':OWN_CPU_KIND,'session_reference':OWN_SESSION_REFERENCE,
 'observed_at':OWNER_OBSERVED_AT,'observed_hostname':OWNER_OBSERVED_HOSTNAME,
 'materialized_hostname':platform.node(),'consumption_units':None,
 'basis':'Actual operator observation; not inferred from Python hostname alone'}
put(UI/'owner-observation.json',owner)
def gate_receipt(name):
    return {'source':SOURCE,'status':'ACCEPTED','path':name,'sha256':sha((P/'gates'/name).read_bytes())}
gate={'source':SOURCE,'status':'READY_AFTER_ACTUAL_PARENT_REVIEW',
 'reviewed_builder_sha256':sha((P/'build354D.py').read_bytes()),
 'reviewed_launcher_sha256':sha((P/'launch354D.py').read_bytes()),
 'source_integration_review':gate_receipt('parent-source-integration-acceptance.json'),
 'production_engineering_review':gate_receipt('production-engineering-full.md'),
 'required_ci':gate_receipt('source-ci-premerge.json'),
 'owner_observation':owner,
 'notebook_review':{'path':'notebook-engineering-review.txt','sha256':sha(review),
    'reviewed_notebook_sha256':REVIEWED_NOTEBOOK_SHA256,'parent_complete_report_read_and_accepted':True},
 'historical_full_reports_and_contexts':[r['path'] for r in gate_attachments],
 'gate_meaning':'Prospective production only; not mathematical acceptance, valid return, exact-PDF assessment or publication'}
put(P/'gates'/'authorization.json',gate)
print(json.dumps({'ready_for_reviewed_launcher':True,'actual_hostname':platform.node(),'source':SOURCE,
 'exact_pdf_assessment':None,'return_validation_performed':False,'runtime_closure_observed':False}))