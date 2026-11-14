"""UNEXECUTED Colab UI launcher. Preserves exact build348.py; no CLI lifecycle claims."""
import hashlib, json, os, re, shutil, signal, subprocess, sys, traceback, zipfile
from datetime import datetime, timezone
from pathlib import Path

SOURCE = 'a27c28cbfd506b7ad06aeebb8b141df89d6a0cba'
BUILDER_SHA = 'bf93b063004f3dcb811af97e1585114508d0cd4d47cbb3dae48bf0ae7bad30b2'
INPUTS_SHA = 'd1b6be5a51570e564ae7da9dd01af6fc7a6fd4ace8a9a8a251f7e470c63a5221'
ROOT = Path('/content/ui-production348D')
ATTEMPT = ROOT / 'attempt'
ARCHIVE = Path('/content/tep348D-build-a-results.zip')
RETURN = ROOT / 'ui-return348D.zip'
MARKER_SHA = '968d66a7b491c7728f2ab009dcb54ac0025d6f474de6f3734f66b8809f6c18a8'
ROLES = ('mathematical', 'engineering348A_failure', 'engineering348D', 'source_ci', 'ui_transport_authorization')

def require(ok, message):
    if not ok: raise ValueError(message)

def sha(raw): return hashlib.sha256(raw).hexdigest()
def utc(): return datetime.now(timezone.utc).isoformat()
def details(path): return {'bytes': path.stat().st_size, 'sha256': sha(path.read_bytes())}
def write_json(path, obj):
    with path.open('x', encoding='utf-8', newline='\n') as stream:
        json.dump(obj, stream, indent=2); stream.write('\n')

def atomic_exit(path, actual):
    require(type(actual) is int and not path.exists(), 'Real new child exit required')
    temporary = path.with_suffix(path.suffix + '.tmp')
    with temporary.open('x', encoding='ascii', newline='\n') as stream:
        stream.write(str(actual)+'\n'); stream.flush(); os.fsync(stream.fileno())
    raw = temporary.read_bytes()
    require(re.fullmatch(rb'-?[0-9]+\n', raw) is not None and int(raw)==actual, 'Closed exit readback')
    os.replace(temporary, path)

def check_gates():
    manifest = ROOT/'RUNNER-HASHES348D.json'
    rows = json.loads(manifest.read_bytes())
    require(isinstance(rows,list) and len(rows)==8, 'Eight runner payload bindings required')
    expected = {'build348.py','SOURCE-INPUTS348.json','ui_launch348D.py',
                'validate_return348D.py','test_validate_return348D.py','validate348_ui_actual_colab.py','run_preflight348D.py','mark_artifact_operation_started.mjs'}
    require(len({r['path'] for r in rows})==8 and {r['path'] for r in rows}==expected, 'Runner inventory')
    for row in rows:
        path = ROOT/row['path']
        require(path.is_file() and not path.is_symlink(), 'Regular runner payload')
        require(type(row['bytes']) is int and details(path)=={'bytes':row['bytes'],'sha256':row['sha256']}, 'Runner binding differs')
    require(sha((ROOT/'build348.py').read_bytes())==BUILDER_SHA, 'Repinned builder pin')
    require(sha((ROOT/'SOURCE-INPUTS348.json').read_bytes())==INPUTS_SHA, 'Exact44 source manifest pin')
    require(sha((ROOT/'mark_artifact_operation_started.mjs').read_bytes())==MARKER_SHA, 'Official PDF marker raw pin')
    bundle = ROOT/'parent-ui-gates.zip'
    require(bundle.is_file() and not bundle.is_symlink() and bundle.stat().st_size<32*1024*1024, 'Real parent gate bundle required')
    with zipfile.ZipFile(bundle) as z:
        infos=z.infolist(); names=[i.filename for i in infos]
        require(len(names)==len(set(names))==6 and set(names)=={'parent-ui-authority-relay.json'}|{role+'.receipt' for role in ROLES}, 'Exact six gate members')
        require(sum(i.file_size for i in infos)<32*1024*1024 and all(not i.is_dir() and not(i.flag_bits&1) and (i.external_attr>>16)&0o170000 in (0,0o100000) for i in infos), 'Bounded regular gate members')
        relay=json.loads(z.read('parent-ui-authority-relay.json'))
        require(relay['schema']=='tep348-ui-authority-v1' and relay['source']==SOURCE and relay['source_ci_head']==SOURCE, 'Exact source authority')
        require(relay['runner_manifest_sha256']==sha(manifest.read_bytes()), 'Exact reviewed runner manifest')
        for key in ('parent_full_mathematical_report_read','parent_full_engineering348A_report_read',
                    'parent_full_engineering348D_report_read','mathematical_accepted','engineering348A_failure_preserved',
                    'engineering348D_accepted','source_ci_verified','ui_transport_authorized','pdf_marker_required_before_builder'):
            require(relay[key] is True, 'Unpaid gate: '+key)
        require(relay['windows_math_execution'] is False, 'No Windows execution authorization inferred')
        require(relay['engineering348A_accepted'] is False, 'Failed348A gate must not be relabelled accepted')
        require(set(relay['receipts'])==set(ROLES), 'All actual report/receipt roles')
        for role in ROLES:
            raw=z.read(role+'.receipt'); row=relay['receipts'][role]
            require(raw and type(row['bytes']) is int and len(raw)==row['bytes'] and sha(raw)==row['sha256'], 'Actual receipt binding: '+role)
        require(sha(z.read('engineering348A_failure.receipt'))=='5e2d849add3b2e29724b779c50572011186137c68cf97be6e5aad0cd8771f74d','Preserve exact348A failed review')
    from run_preflight348D import check_preflight
    check_preflight(ROOT)  # Mandatory actual normal and -O receipts, before any builder dispatch.
    return bundle

def main():
    require(os.name=='posix' and Path('/content').is_dir() and Path(__file__).resolve().parent==ROOT, 'Owned Colab Linux path only')
    require(not ROOT.is_symlink() and not ATTEMPT.exists() and not ATTEMPT.is_symlink() and not RETURN.exists() and not RETURN.is_symlink(), 'Fresh UI attempt required')
    require(not ARCHIVE.exists() and not ARCHIVE.is_symlink() and not Path('/content/tep348D-build-a').exists(), 'No reuse of earlier builder attempt')
    gates=check_gates()  # No child is launched until all genuine parent bindings pass.
    ATTEMPT.mkdir()
    (ATTEMPT/'authority-gates.zip').write_bytes(gates.read_bytes())
    with zipfile.ZipFile(ATTEMPT/'synthetic-preflight.zip','x',zipfile.ZIP_DEFLATED) as z:
        for path in sorted((ROOT/'preflight').iterdir()):
            if path.is_file() and not path.is_symlink(): z.write(path,path.name)
    observation={'schema':'tep348-ui-inner-transport-v1','source':SOURCE,'builder_sha256':BUILDER_SHA,
                 'source_manifest_sha256':INPUTS_SHA,'started_at':utc(),'finished_at':None,
                 'child':{'argv':[sys.executable,str(ROOT/'build348.py')],'actual_exit':None,
                          'termination_observed':False,'timed_out':False,'interrupted':False,'launch_or_wait_error':None},
                 'files':{},'archive':None,'marker':None}
    child=None
    try:
        with (ATTEMPT/'builder.stdout').open('xb') as out, (ATTEMPT/'builder.stderr').open('xb') as err:
            try:
                node=shutil.which('node')
                require(node is not None, 'Node missing; no marker or builder execution')
                marker_argv=[node,str(ROOT/'mark_artifact_operation_started.mjs'),'--operation-kind','create','--expected-output-count','1','--output-format','pdf']
                with (ATTEMPT/'marker.stdout').open('xb') as mout, (ATTEMPT/'marker.stderr').open('xb') as merr:
                    marker_child=subprocess.Popen(marker_argv,cwd=ROOT,stdout=mout,stderr=merr)
                    try: marker_exit=marker_child.wait(timeout=30)
                    except BaseException:
                        marker_child.kill(); marker_exit=marker_child.wait()
                        atomic_exit(ATTEMPT/'marker.exit',marker_exit)
                        observation['marker']={'argv':marker_argv,'script_sha256':MARKER_SHA,'actual_exit':marker_exit,'completed_without_interruption':False}
                        raise
                atomic_exit(ATTEMPT/'marker.exit',marker_exit)
                observation['marker']={'argv':marker_argv,'script_sha256':MARKER_SHA,'actual_exit':marker_exit,'completed_without_interruption':True}
                require(marker_exit==0, 'Real PDF marker failed; builder not dispatched')
                # Exactly one successful official marker invocation immediately precedes the builder.
                child=subprocess.Popen(observation['child']['argv'],cwd=ROOT,stdout=out,stderr=err,start_new_session=True)
                try:
                    actual=child.wait(timeout=4200)
                except subprocess.TimeoutExpired:
                    observation['child']['timed_out']=True
                    os.killpg(child.pid,signal.SIGKILL); actual=child.wait()
                observation['child']['actual_exit']=actual
                observation['child']['termination_observed']=True
            except BaseException:
                observation['child']['interrupted']=True
                observation['child']['launch_or_wait_error']=traceback.format_exc()
                if child is not None:
                    if child.poll() is None:
                        try: os.killpg(child.pid,signal.SIGKILL)
                        except ProcessLookupError: pass
                    observation['child']['actual_exit']=child.wait()
                    observation['child']['termination_observed']=True
            finally:
                out.flush(); os.fsync(out.fileno()); err.flush(); os.fsync(err.fileno())
    finally:
        if observation['child']['termination_observed']:
            atomic_exit(ATTEMPT/'builder.exit',observation['child']['actual_exit'])
        for name in ('builder.stdout','builder.stderr','builder.exit','authority-gates.zip','synthetic-preflight.zip','marker.stdout','marker.stderr','marker.exit'):
            path=ATTEMPT/name
            if path.is_file(): observation['files'][name]=details(path)
        if ARCHIVE.is_file() and not ARCHIVE.is_symlink():
            observation['archive']={'remote_path':str(ARCHIVE),**details(ARCHIVE)}
        observation['finished_at']=utc()
        write_json(ATTEMPT/'ui-observation.json',observation)
        # A failed builder's archive is preserved unchanged, never replaced with a synthetic success.
        with zipfile.ZipFile(RETURN,'x',zipfile.ZIP_DEFLATED) as z:
            for path in sorted(ATTEMPT.iterdir()):
                if path.is_file() and not path.is_symlink(): z.write(path,path.name)
            if observation['archive'] is not None: z.write(ARCHIVE,'production.zip')
        print(json.dumps({'ui_return':str(RETURN),**details(RETURN),'builder_child':observation['child'],
                          'archive':observation['archive'],'scope':'Inner child observation only. Rendered-byte reception and runtime closure unobserved here.'}))
    require(observation['child']['actual_exit']==0 and observation['child']['termination_observed'] and
            not observation['child']['timed_out'] and not observation['child']['interrupted'] and
            observation['archive'] is not None, 'Builder failed or incomplete; preserve UI return and inspect, no blind retry')

if __name__=='__main__': main()
