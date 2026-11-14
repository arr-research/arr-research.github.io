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
require(code==Path('/content/ui-validation348D') and not code.is_symlink(),'Exact validation code location')
validator=code/'validate_return348D.py'; sources=code/'SOURCE-INPUTS348.json'
require(h(validator)=='82be204e8678ccc6716a1589794e0518d31c2209e3718b767ed05831d98ee100','Reviewed validator pin')
require(h(sources)=='d1b6be5a51570e564ae7da9dd01af6fc7a6fd4ace8a9a8a251f7e470c63a5221','Independent44-source manifest pin')
mode='optimized' if sys.flags.optimize else 'normal'
root=code/('actual-'+mode); bundle=code/'ui-return348D.zip'
require(not root.exists() and not root.is_symlink(),'Fresh mode-specific result destination')
require(bundle.is_file() and not bundle.is_symlink() and bundle.stat().st_size<=512*1024*1024,'Actual bounded materialized return bundle')
require(h(bundle)==sys.argv[1],'Materialized bytes differ from parent observation')
root.mkdir(); start=time.perf_counter()
try:
    from run_preflight348D import check_preflight
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
    check_preflight(code,historical,Path('/content/ui-production348D'))
    spec=importlib.util.spec_from_file_location('reviewed_ui_validator348D',validator)
    require(spec is not None and spec.loader is not None,'Validator loader')
    v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
    result=v.validate(root/'production.zip',root,sources,[root/'uncreated-extraction',root/'uncreated-delivery'])
    result.update(validation_mode=mode,input_bundle_sha256=h(bundle),validator_sha256=h(validator),
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
