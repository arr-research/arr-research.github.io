"""UNEXECUTED predicate regressions: retained343 field cases plus348 UI author cases. Colab normal and -O only; not production evidence."""
import copy, json, tempfile
from pathlib import Path
import validate_return348E as v

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
report={'source':v.SOURCE,'tex_raw_sha256':v.TEX,'support_raw_sha256':v.SUPPORT,'tex_argument':v.TEX_ARG,'status':v.STATUS,'builds':[dict(build,mode=m) for m in ('a','b')],'commands':[{'name':n,'actual_exit':0,'timed_out':False,'argv':['fixture']} for n in v.COMMANDS],'cleanup':[{'path':'/content/tep348D-build-a/clone-'+m,'removed':True} for m in ('a','b')],'pages':2}
good('report-positive-synthetic',lambda:v.check_report(report))
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
mutated('348-wrong-included-source',lambda r:r.update(support_raw_sha256='wrong'))
mutated('348-wrong-metadata-argument',lambda r:r.update(tex_argument='wrong'))
with tempfile.TemporaryDirectory() as d:
    root=Path(d); archive=root/'production.zip'; archive.write_bytes(b'SYNTHETIC ONLY, NOT A PDF OR PRODUCTION RETURN')
    for name,raw in [('builder.stdout',b'synthetic stdout\n'),('builder.stderr',b''),('builder.exit',b'0\n'),('authority-gates.zip',b'synthetic gate bytes; not authority'),('synthetic-preflight.zip',b'synthetic preflight bytes'),('marker.stdout',b''),('marker.stderr',b''),('marker.exit',b'0\n')]:
        (root/name).write_bytes(raw)
    fixture={'schema':'tep348-ui-inner-transport-v1','source':v.SOURCE,
             'builder_sha256':'bf93b063004f3dcb811af97e1585114508d0cd4d47cbb3dae48bf0ae7bad30b2',
             'source_manifest_sha256':'d1b6be5a51570e564ae7da9dd01af6fc7a6fd4ace8a9a8a251f7e470c63a5221',
             'started_at':'2026-01-01T00:00:00+00:00','finished_at':'2026-01-01T00:00:01+00:00',
             'child':{'argv':['/usr/bin/python3','/content/ui-production348D/build348.py'],'actual_exit':0,'termination_observed':True,'timed_out':False,'interrupted':False,'launch_or_wait_error':None},
             'marker':{'argv':['/usr/bin/node','/content/ui-production348D/mark_artifact_operation_started.mjs','--operation-kind','create','--expected-output-count','1','--output-format','pdf'],'script_sha256':'968d66a7b491c7728f2ab009dcb54ac0025d6f474de6f3734f66b8809f6c18a8','actual_exit':0,'completed_without_interruption':True},
             'files':{name:{'bytes':(root/name).stat().st_size,'sha256':v.digest((root/name).read_bytes())} for name in ('builder.stdout','builder.stderr','builder.exit','authority-gates.zip','synthetic-preflight.zip','marker.stdout','marker.stderr','marker.exit')},
             'archive':{'remote_path':'/content/tep348D-build-a-results.zip','bytes':archive.stat().st_size,'sha256':v.digest(archive.read_bytes())}}
    good('ui-positive-SYNTHETIC-predicate-only',lambda:v.check_ui_observation(fixture,archive,root))
    def ui_bad(name,edit):
        row=copy.deepcopy(fixture);edit(row)
        bad(name,lambda:v.check_ui_observation(row,archive,root))
    ui_bad('ui-wrong-source',lambda r:r.update(source='wrong'))
    ui_bad('ui-wrong-builder',lambda r:r.update(builder_sha256='wrong'))
    ui_bad('ui-wrong-source-manifest',lambda r:r.update(source_manifest_sha256='wrong'))
    ui_bad('ui-fabricated-cli-fields',lambda r:r.update(actual_cli_exits={'execution':0}))
    ui_bad('ui-boolean-child-exit',lambda r:r['child'].update(actual_exit=False))
    ui_bad('ui-nonzero-child',lambda r:r['child'].update(actual_exit=1))
    ui_bad('ui-unobserved-child',lambda r:r['child'].update(termination_observed=False))
    ui_bad('ui-timeout',lambda r:r['child'].update(timed_out=True))
    ui_bad('ui-interruption',lambda r:r['child'].update(interrupted=True))
    ui_bad('ui-launch-error',lambda r:r['child'].update(launch_or_wait_error='spawn failed'))
    ui_bad('ui-wrong-argv',lambda r:r['child'].update(argv=['/usr/bin/python3','/content/other.py']))
    ui_bad('ui-omitted-file',lambda r:r['files'].pop('builder.stderr'))
    ui_bad('ui-altered-stdout-binding',lambda r:r['files']['builder.stdout'].update(sha256='0'*64))
    ui_bad('ui-missing-archive',lambda r:r.update(archive=None))
    ui_bad('ui-wrong-archive-hash',lambda r:r['archive'].update(sha256='0'*64))
    ui_bad('ui-boolean-archive-size',lambda r:r['archive'].update(bytes=True))
    ui_bad('ui-reversed-time',lambda r:r.update(finished_at='2025-12-31T00:00:00+00:00'))
    ui_bad('ui-missing-marker',lambda r:r.update(marker=None))
    ui_bad('ui-boolean-marker-exit',lambda r:r['marker'].update(actual_exit=False))
    ui_bad('ui-wrong-marker-bytes',lambda r:r['marker'].update(script_sha256='0'*64))
    ui_bad('ui-wrong-marker-command',lambda r:r['marker'].update(argv=['/usr/bin/node','other.js']))
    (root/'builder.exit').write_bytes(b'1\n')
    bad('ui-real-file-exit-changed',lambda:v.check_ui_observation(fixture,archive,root))


# This is the exact captured actual production command sequence, checked as data.
# No command is executed by these regression cases.
native = json.loads((Path(__file__).parent/'actual-production348D-report.json').read_bytes())['commands']
good('E-actual27-command-sequence',lambda:v.check_native_tex_commands(native))
def native_bad(name, edit):
    rows=copy.deepcopy(native);edit(rows)
    bad(name,lambda:v.check_native_tex_commands(rows))
native_bad('E-version-argv-changed',lambda rows:next(c for c in rows if c['name']=='tex-version').update(argv=['pdflatex','--help']))
native_bad('E-missing-compile',lambda rows:rows.pop(next(i for i,c in enumerate(rows) if c['name']=='tex-a-pass1')))
native_bad('E-shell-escape-enabled',lambda rows:next(c for c in rows if c['name']=='tex-b-pass1')['argv'].__setitem__(1,'-shell-escape'))
native_bad('E-wrong-compile-argument',lambda rows:next(c for c in rows if c['name']=='tex-a-pass2')['argv'].__setitem__(-1,'wrong-source.tex'))

if accepted!=6 or rejected!=62:raise RuntimeError(f'Unexpected counters {accepted}/{rejected}')
print(json.dumps({'scope':'Synthetic field-derived predicate regression only, not a production return or execution certificate','accepted':accepted,'rejected':rejected,'cases':cases}))
