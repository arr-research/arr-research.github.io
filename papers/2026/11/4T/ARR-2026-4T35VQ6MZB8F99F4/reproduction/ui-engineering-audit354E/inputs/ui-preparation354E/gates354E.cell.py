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
ci=json.loads(attached['gate-evidence/source-ci-premerge.json'])
need(ci['headRefOid']==SOURCE,'Wrong required-CI source')
checks={c['name']:c for c in ci['statusCheckRollup']}
for name in ('honesty','lake build YangMillsCore + oracle'):
    need(name in checks and checks[name]['status']=='COMPLETED' and checks[name]['conclusion']=='SUCCESS','Actual required CI not successful')
merged=json.loads(attached['gate-evidence/source-merged-readback.json'])
need(merged['headRefOid']==SOURCE and merged['state']=='MERGED'
     and merged['mergeCommit']['oid']=='a0ee5c3a8734fdce200f353795f13f81ffa6a19a','Actual source merge mismatch')
source_accept=json.loads(attached['gate-evidence/parent-source-integration-acceptance.json'])
need(source_accept['source']==SOURCE and source_accept['verdict']=='ACCEPT_SOURCE_INTEGRATION'
     and source_accept['full_source_report_read'] is True and source_accept['full_pin_closure_read'] is True,'Actual parent source acceptance absent')
producer_accept=json.loads(attached['gate-evidence/parent-production-static-acceptance.json'])
need(producer_accept['source']==SOURCE and producer_accept['full_report_and_context_read'] is True
     and producer_accept['report_sha256']==sha(attached['gate-evidence/production-engineering-full.md'])
     and producer_accept['verdict']=='ACCEPT_FOR_PROSPECTIVE_OWN_COLAB_PRODUCTION_AFTER_REAL_GATES','Actual producer acceptance mismatch')
# Earlier producer-parent JSON retains its historically pending CI/pin fields;
# the separately captured later source acceptance and actual successful CI close those conditions.
# Originals are staged outside the producer's exact four-file gates namespace.
# Preserve every raw attachment; do not remove originals or relax reader membership.
evidence=P/'gate-evidence'
with (evidence/'notebook-engineering-review.txt').open('xb') as f:f.write(review)
need((evidence/'notebook-engineering-review.txt').read_bytes()==review,'Future review raw readback')
need(not (P/'gates').exists() and not (P/'gates').is_symlink(),'Fresh narrow gate namespace')
(P/'gates').mkdir()
def write_verified_bundle(path,names,kind):
    need(len(names)==len(set(names)) and 'GATE-BUNDLE-MANIFEST.json' not in names,'Unique bundle members')
    raw_members={}
    for name in names:
        safe(name);target=evidence/name
        need(target.is_file() and not target.is_symlink() and target.resolve().is_relative_to(evidence.resolve()),'Unsafe bundle source')
        raw_members[name]=target.read_bytes()
    payload_manifest={'source':SOURCE,'kind':kind,'files':[
        {'path':name,'bytes':len(raw),'sha256':sha(raw)} for name,raw in sorted(raw_members.items())]}
    raw_members['GATE-BUNDLE-MANIFEST.json']=(json.dumps(payload_manifest,indent=2)+'\n').encode('utf-8')
    with zipfile.ZipFile(path,'x',zipfile.ZIP_DEFLATED) as z:
        for name,raw in sorted(raw_members.items()):
            zi=zipfile.ZipInfo(name,date_time=(1980,1,1,0,0,0));zi.create_system=3
            zi.external_attr=0o100644<<16;zi.compress_type=zipfile.ZIP_DEFLATED
            z.writestr(zi,raw)
    # No extraction: check exact member universe, regular type, bytes and hashes.
    with zipfile.ZipFile(path,'r') as z:
        infos=z.infolist();member_names=[i.filename for i in infos]
        need(len(member_names)==len(set(member_names)) and set(member_names)==set(raw_members),'Exact bundle membership')
        for info in infos:
            safe(info.filename)
            need(not info.is_dir() and not (info.flag_bits&1) and ((info.external_attr>>16)&0o170000)==0o100000,
                 'Bundle must contain regular unencrypted files')
            expected=raw_members[info.filename]
            need(info.file_size==len(expected) and z.read(info)==expected and sha(z.read(info))==sha(expected),'Bundle raw readback')
    return payload_manifest
source_members=['source-integration-full.txt','source-integration-context.txt','source-integration-objections.txt',
 'pin-closure-full.txt','pin-closure-context.txt','pin-closure-objections.txt',
 'source-merged-readback.json','parent-source-integration-acceptance.json']
producer_members=['production-engineering-full.md','production-engineering-context.json','parent-production-static-acceptance.json',
 'old-wrapper354D-full.txt','old-wrapper354D-context.txt','old-wrapper354D-objections.txt','notebook-engineering-review.txt']
source_bundle=write_verified_bundle(P/'gates'/'source-integration-evidence.zip',source_members,'complete-source-and-pin-evidence')
producer_bundle=write_verified_bundle(P/'gates'/'production-engineering-evidence.zip',producer_members,'complete-producer-and-wrapper-evidence')
ci_raw=attached['gate-evidence/source-ci-premerge.json']
with (P/'gates'/'source-ci-premerge.json').open('xb') as f:f.write(ci_raw)
need((P/'gates'/'source-ci-premerge.json').read_bytes()==ci_raw,'CI raw readback')
covered=set(source_members)|set(producer_members)|{'source-ci-premerge.json'}
need(covered=={r['path'].split('/',1)[1] for r in gate_attachments}|{'notebook-engineering-review.txt'},'Every original/new report retained exactly')
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
 'source_integration_review':gate_receipt('source-integration-evidence.zip'),
 'production_engineering_review':gate_receipt('production-engineering-evidence.zip'),
 'required_ci':gate_receipt('source-ci-premerge.json'),
 'owner_observation':owner,
 'notebook_review':{'bundle_path':'production-engineering-evidence.zip','member':'notebook-engineering-review.txt','sha256':sha(review),
    'reviewed_notebook_sha256':REVIEWED_NOTEBOOK_SHA256,'parent_complete_report_read_and_accepted':True},
 'bundled_full_reports':{'source':source_bundle,'production':producer_bundle},
 'gate_meaning':'Prospective production only; not mathematical acceptance, valid return, exact-PDF assessment or publication'}
put(P/'gates'/'authorization.json',gate)
need({p.name for p in (P/'gates').iterdir()}=={'authorization.json','source-integration-evidence.zip','production-engineering-evidence.zip','source-ci-premerge.json'}
     and all(p.is_file() and not p.is_symlink() for p in (P/'gates').iterdir()),'Exact four native gate files')
print(json.dumps({'ready_for_reviewed_launcher':True,'actual_hostname':platform.node(),'source':SOURCE,
 'exact_pdf_assessment':None,'return_validation_performed':False,'runtime_closure_observed':False}))