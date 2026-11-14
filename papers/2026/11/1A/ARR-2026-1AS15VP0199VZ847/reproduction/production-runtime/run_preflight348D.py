"""UNEXECUTED mandatory normal/-O predicate preflight. No PDF or lifecycle claims."""
import hashlib, json, os, re, resource, signal, subprocess, sys, time
from pathlib import Path

def require(ok,message):
    if not ok: raise ValueError(message)
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def check_output(raw):
    value=json.loads(raw.decode('utf-8'))
    require(type(value['accepted']) is int and value['accepted']==5 and type(value['rejected']) is int and value['rejected']==58,'Explicit expected5/58 predicate counts')
    cases=value['cases']
    require(isinstance(cases,list) and len(cases)==63 and len({c['case'] for c in cases})==63,'Exact distinct predicate case count')
    require(sum(c['expected']=='accept' and c['observed']=='accept' for c in cases)==5 and sum(c['expected']=='reject' and c['observed']=='reject' for c in cases)==58,'Actual per-case decisions')
    return value

def check_preflight(code, receipts=None, recorded_code=None):
    receipts=receipts or code/'preflight'; recorded_code=recorded_code or code
    report=json.loads((receipts/'report.json').read_bytes())
    require(report['schema']=='tep348-required-normal-optimized-v1' and report['ready'] is True,'Mandatory actual preflight incomplete')
    require(report['runner_manifest_sha256']==sha(code/'RUNNER-HASHES348D.json'),'Preflight reviewed runner manifest differs')
    for name in ('validate_return348D.py','test_validate_return348D.py','run_preflight348D.py'):
        require(report['code_sha256'][name]==sha(code/name),'Preflight exact code binding')
    require([r['mode'] for r in report['runs']]==['normal','optimized'],'Both semantic modes required')
    for row in report['runs']:
        prefix=receipts/row['mode']
        require(isinstance(row['argv'],list) and row['argv'] and isinstance(row['argv'][0],str) and row['argv'][0].startswith('/'),'Observed absolute Python executable')
        expected=[row['argv'][0]]+(['-O'] if row['mode']=='optimized' else [])+[str(recorded_code/'test_validate_return348D.py')]
        require(row['argv']==expected and type(row['actual_exit']) is int and row['actual_exit']==0 and row['timed_out'] is False and row['result_accepted'] is True,'Real mode child success required')
        require(prefix.with_suffix('.exit').read_bytes()==b'0\n','Real mode zero sentinel')
        for ext in ('.stdout','.stderr','.exit'):
            path=prefix.with_suffix(ext)
            require(path.is_file() and not path.is_symlink() and row['files'][ext]=={'bytes':path.stat().st_size,'sha256':sha(path)},'Mode raw receipt binding')
        require(check_output(prefix.with_suffix('.stdout').read_bytes())==row['predicate_output'],'Mode counters must match actual stdout')
    return report

def main():
    code=Path(__file__).resolve().parent
    require(os.name=='posix' and code in (Path('/content/ui-production348D'),Path('/content/ui-validation348D')),'Owned Colab preflight only')
    root=code/'preflight'
    require(not root.exists() and not root.is_symlink(),'No overwrite or blind retry of preflight')
    rows=json.loads((code/'RUNNER-HASHES348D.json').read_bytes())
    for name in ('validate_return348D.py','test_validate_return348D.py','run_preflight348D.py'):
        matching=[r for r in rows if r['path']==name]
        require(len(matching)==1 and matching[0]['sha256']==sha(code/name) and matching[0]['bytes']==(code/name).stat().st_size,'Pinned preflight payload')
    root.mkdir()
    report={'schema':'tep348-required-normal-optimized-v1','ready':False,'runner_manifest_sha256':sha(code/'RUNNER-HASHES348D.json'),
            'code_sha256':{name:sha(code/name) for name in ('validate_return348D.py','test_validate_return348D.py','run_preflight348D.py')},'runs':[],
            'scope':'Synthetic predicate field regressions only, never production/PDF evidence'}
    try:
        for mode in ('normal','optimized'):
            argv=[sys.executable]+(['-O'] if mode=='optimized' else [])+[str(code/'test_validate_return348D.py')]
            prefix=root/mode; start=time.perf_counter(); timed_out=False
            with prefix.with_suffix('.stdout').open('xb') as out, prefix.with_suffix('.stderr').open('xb') as err:
                child=subprocess.Popen(argv,cwd=code,stdout=out,stderr=err,start_new_session=True)
                try: actual=child.wait(timeout=120)
                except subprocess.TimeoutExpired:
                    timed_out=True
                    try: os.killpg(child.pid,signal.SIGKILL)
                    except ProcessLookupError: pass
                    actual=child.wait()
                except BaseException:
                    try: os.killpg(child.pid,signal.SIGKILL)
                    except ProcessLookupError: pass
                    child.wait(); raise
                out.flush();os.fsync(out.fileno());err.flush();os.fsync(err.fileno())
            temporary=prefix.with_suffix('.exit.tmp')
            with temporary.open('x',encoding='ascii',newline='\n') as stream:
                stream.write(str(actual)+'\n');stream.flush();os.fsync(stream.fileno())
            require(re.fullmatch(rb'-?[0-9]+\n',temporary.read_bytes()) is not None and int(temporary.read_bytes())==actual,'Actual closed test exit')
            os.replace(temporary,prefix.with_suffix('.exit'))
            row={'mode':mode,'argv':argv,'actual_exit':actual,'timed_out':timed_out,'result_accepted':False,
                 'wall_seconds':time.perf_counter()-start,'children_max_rss_kib_cumulative':resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
                 'files':{ext:{'bytes':prefix.with_suffix(ext).stat().st_size,'sha256':sha(prefix.with_suffix(ext))} for ext in ('.stdout','.stderr','.exit')}}
            report['runs'].append(row)
            if actual==0 and not timed_out:
                row['predicate_output']=check_output(prefix.with_suffix('.stdout').read_bytes());row['result_accepted']=True
        report['ready']=len(report['runs'])==2 and all(r['result_accepted'] for r in report['runs'])
    finally:
        with (root/'report.json').open('x',encoding='utf-8',newline='\n') as stream:
            json.dump(report,stream,indent=2);stream.write('\n')
    check_preflight(code)
    print(json.dumps(report))

if __name__=='__main__': main()
