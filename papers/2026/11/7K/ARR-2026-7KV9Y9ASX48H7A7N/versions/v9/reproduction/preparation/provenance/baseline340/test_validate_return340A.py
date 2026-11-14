"""Synthetic predicate regressions from collector322 auditor B1-B3; not production evidence."""
import copy, json, tempfile
from pathlib import Path
import validate_return340A as v

accepted=0;rejected=0;cases=[]
def good(name, fn):
    global accepted
    fn(); accepted+=1;cases.append({'case':name,'expected':'accept','observed':'accept'})
def bad(name, fn):
    global rejected
    try: fn()
    except (ValueError,KeyError,TypeError):
        rejected+=1;cases.append({'case':name,'expected':'reject','observed':'reject'});return
    raise RuntimeError('False acceptance: '+name)

build={'source':v.SOURCE,'input_files_verified':v.EXPECTED_INPUT_COUNT,'pdf_bytes':10,'pdf_sha256':'0'*64,'epoch':'123'}
report={'source':v.SOURCE,'tex_raw_sha256':v.TEX,'status':v.STATUS,'builds':[dict(build,mode=m) for m in ('a','b')],'commands':[{'name':n,'actual_exit':0,'timed_out':False,'argv':['fixture']} for n in v.COMMANDS],'cleanup':[{'path':'/content/tep340-build-a/clone-'+m,'removed':True} for m in ('a','b')],'pages':2}
outer={'source':v.SOURCE,'failure':None,'actual_cli_exits':dict.fromkeys(('allocation','execution','download','release'),0)}
good('report-positive-synthetic',lambda:v.check_report(report))
good('outer-positive-synthetic',lambda:v.check_outer(outer))
def mutated(name, edit):
    r=copy.deepcopy(report);edit(r);bad(name,lambda:v.check_report(r))
mutated('B1-empty-builds',lambda r:r.update(builds=[]))
mutated('B1-one-build',lambda r:r.update(builds=r['builds'][:1]))
mutated('B1-duplicate-mode',lambda r:r['builds'][1].update(mode='a'))
mutated('B1-wrong-source',lambda r:r['builds'][1].update(source='wrong'))
mutated('B1-wrong-epoch',lambda r:r['builds'][1].update(epoch='124'))
mutated('B1-wrong-pdf-length',lambda r:r['builds'][1].update(pdf_bytes=11))
mutated('B1-wrong-tex',lambda r:r.update(tex_raw_sha256='wrong'))
mutated('B3-duplicate-commands',lambda r:r.update(commands=[r['commands'][0]]*27))
mutated('B3-boolean-exit',lambda r:r['commands'][0].update(actual_exit=False))
mutated('B3-string-timeout',lambda r:r['commands'][0].update(timed_out='false'))
mutated('B3-duplicate-cleanup',lambda r:r.update(cleanup=[r['cleanup'][0]]*2))
mutated('B3-string-cleanup',lambda r:r['cleanup'][0].update(removed='yes'))
mutated('B3-boolean-pages',lambda r:r.update(pages=True))
for name,exits in [('B3-wrong-outer-keys',dict.fromkeys(('a','b','c','d'),0)),('B3-outer-boolean-exit',dict(outer['actual_cli_exits'],execution=False))]:
    o=copy.deepcopy(outer);o['actual_cli_exits']=exits;bad(name,lambda o=o:v.check_outer(o))
row={'path':'evidence/a','bytes':1,'sha256':'0'*64};names=['evidence/a','evidence/manifest.json']
good('manifest-positive-synthetic',lambda:v.check_manifest([row],names))
bad('B3-empty-manifest',lambda:v.check_manifest([],names))
bad('B3-duplicate-manifest',lambda:v.check_manifest([row,row],names))
bad('B3-omitted-manifest-member',lambda:v.check_manifest([row],names+['evidence/b']))
for name,paths in [('duplicate-zip',['a','a']),('case-alias',['a','A']),('traversal',['a/../x']),('backslash',['a\\x']),('empty-part',['a//x']),('trailing-dot',['a.']),('reserved',['CON.txt']),('file-directory',['a','a/b']),('absolute',['/a']),('colon',['a:b'])]:
    bad(name,lambda paths=paths:v.safe_names(paths))
with tempfile.TemporaryDirectory() as d:
    p=Path(d)/'validation.json';good('fresh-destination',lambda:v.fresh([p]))
    p.write_bytes(b'ORIGINAL');bad('B2-existing-output',lambda:v.fresh([p]))
    if p.read_bytes()!=b'ORIGINAL':raise RuntimeError('Prior output changed')
    bad('B2-repeated-destination',lambda:v.fresh([Path(d)/'new',Path(d)/'new']))
good('C1-exact-single-line-zero',lambda:v.check_zero(b'0\n'))
for name,raw in [('leading-blank',b'\n0\n'),('trailing-blank',b'0\n\n'),('leading-space',b' 0\n'),('empty',b''),('noninteger',b'x\n'),('nonzero',b'1\n')]:
    bad('C1-'+name,lambda raw=raw:v.check_zero(raw))
if accepted!=5 or rejected!=36:raise RuntimeError(f'Unexpected counters {accepted}/{rejected}')
print(json.dumps({'scope':'Synthetic field-derived predicate regression only, not a production return or execution certificate','accepted':accepted,'rejected':rejected,'cases':cases}))
