"""UNEXECUTED actual UI return validator caller. Run separately in normal and -O Colab.
argv[1] is the parent's observed local-materialization SHA256 of ui-return348D.zip.
No allocation/download/release CLI status is inferred or synthesized.
"""
import hashlib, importlib.util, json, os, re, resource, stat, sys, time, traceback, zipfile
from pathlib import Path

def require(ok,message):
    if not ok: raise ValueError(message)
def h(path):
    with path.open('rb') as stream: return hashlib.file_digest(stream,'sha256').hexdigest()

require(os.name=='posix' and Path('/content').is_dir(),'Own Colab Linux only')
require(len(sys.argv)==2 and re.fullmatch('[0-9a-f]{64}',sys.argv[1]) is not None,'Actual observed local-materialization bundle SHA256 required')
code=Path(__file__).resolve().parent
require(code==Path('/content/ui-validation348E') and not code.is_symlink(),'Exact validation code location')
manifest_rows=json.loads((code/'RUNNER-HASHES348E.json').read_bytes())
self_rows=[r for r in manifest_rows if r['path']==Path(__file__).name]
require(len(self_rows)==1 and self_rows[0]['sha256']==h(Path(__file__)) and self_rows[0]['bytes']==Path(__file__).stat().st_size,'Current caller self binding')
validator=code/'validate_return348E.py'; sources=code/'SOURCE-INPUTS348.json'
require(h(validator)=='6703abe7ceedc6b9ad1ec05f3d6431c7e406d2bb5a8f055d928017c5658c46ae','Reviewed validator pin')
require(h(sources)=='d1b6be5a51570e564ae7da9dd01af6fc7a6fd4ace8a9a8a251f7e470c63a5221','Independent44-source manifest pin')
require(sys.flags.optimize in (0,1) and os.environ.get('PYTHONOPTIMIZE') is None,'Exact explicit normal or -O mode only')
mode='optimized' if sys.flags.optimize else 'normal'
root=code/('actual-'+mode); bundle=code/'ui-return348D.zip'
require(not root.exists() and not root.is_symlink(),'Fresh mode-specific result destination')
require(bundle.is_file() and not bundle.is_symlink() and bundle.stat().st_size<=512*1024*1024,'Actual bounded materialized return bundle')
require(h(bundle)==sys.argv[1]=='b74ab3e6e1d349aafe5ed42d984270e0ae1ee86ac158a1d9738dc6274f1b6e4b' and bundle.stat().st_size==5429697,'Exact unchanged production348D input required')
root.mkdir(); start=time.perf_counter()
try:
    require(h(code/'run_preflight348E.py')=='8e39e729c625627140af37b0797bfc84bd8232458cbda4e3877144493940cb74','Current addendum preflight checker pin')
    from run_preflight348E import check_preflight
    check_preflight(code)  # Mandatory current normal and -O predicates before accepting an actual return.
    expected={'production.zip','ui-observation.json','builder.stdout','builder.stderr','builder.exit','authority-gates.zip','synthetic-preflight.zip','marker.stdout','marker.stderr','marker.exit'}
    with zipfile.ZipFile(bundle) as z:
        infos=z.infolist(); names=[i.filename for i in infos]
        require(len(names)==len(set(names)) and set(names)==expected,'Exact ten regular UI success members')
        require(sum(i.file_size for i in infos)<=512*1024*1024,'Uncompressed input size limit')
        for i in infos:
            require(not i.is_dir() and not(i.flag_bits&1) and stat.S_IFMT(i.external_attr>>16) in (0,stat.S_IFREG),'Regular unencrypted member only')
        for i in infos:
            with (root/i.filename).open('xb') as out, z.open(i) as inp:
                while chunk:=inp.read(1024*1024): out.write(chunk)
    historical=root/'production-preflight';historical.mkdir()
    with zipfile.ZipFile(root/'synthetic-preflight.zip') as z:
        infos=z.infolist();names=[i.filename for i in infos]
        wanted={'report.json'}|{mode+ext for mode in ('normal','optimized') for ext in ('.stdout','.stderr','.exit')}
        require(len(names)==len(set(names)) and set(names)==wanted and sum(i.file_size for i in infos)<2*1024*1024,'Exact bounded production preflight receipts')
        require(all(not i.is_dir() and not(i.flag_bits&1) and stat.S_IFMT(i.external_attr>>16) in (0,stat.S_IFREG) for i in infos),'Regular production preflight members')
        for i in infos:
            with (historical/i.filename).open('xb') as stream: stream.write(z.read(i))
    legacy_code=code/'historical348D'
    require(h(legacy_code/'RUNNER-HASHES348D.json')=='e94203fe2d096bd138da5faef9496b14cf3ac3554891e7e8506aa1593c900853','Original production runner manifest')
    require(h(legacy_code/'run_preflight348D.py')=='2c33f3bdb2bb1d9aded0ac9635aefb8f6f0b8a0125e150ff2f1161d05f97644f','Original production preflight checker')
    legacy_spec=importlib.util.spec_from_file_location('historical_preflight348D',legacy_code/'run_preflight348D.py')
    require(legacy_spec is not None and legacy_spec.loader is not None,'Historical checker loader')
    legacy=importlib.util.module_from_spec(legacy_spec);legacy_spec.loader.exec_module(legacy)
    legacy.check_preflight(legacy_code,historical,Path('/content/ui-production348D'))
    spec=importlib.util.spec_from_file_location('reviewed_ui_validator348E',validator)
    require(spec is not None and spec.loader is not None,'Validator loader')
    v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
    result=v.validate(root/'production.zip',root,sources,[root/'uncreated-extraction',root/'uncreated-delivery'])
    result.update(validation_mode=mode,input_bundle_sha256=h(bundle),validator_sha256=h(validator),
                  caller_sha256=h(Path(__file__)),runner_manifest_sha256=h(code/'RUNNER-HASHES348E.json'),
                  preflight_checker_sha256=h(code/'run_preflight348E.py'),actual_command_fixture_sha256=h(code/'actual-production348D-report.json'),
                  wall_seconds=time.perf_counter()-start,max_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  execution_environment='Colab Linux',mathematical_test=False,visual_inspection=False,
                  transport_scope='Actual builder child/inner archive checked. No CLI lifecycle values exist for this route.',
                  lifecycle_scope='Parent must separately inspect saved runtime-type, opening/closing and Manage sessions UI receipts; these are not inferred by this validator.')
    with (root/'result.json').open('x',encoding='utf-8',newline='\n') as stream:
        json.dump(result,stream,indent=2);stream.write('\n')
    print(json.dumps(result))
except BaseException:
    with (root/'validation-failure.txt').open('x',encoding='utf-8') as stream: stream.write(traceback.format_exc())
    raise
