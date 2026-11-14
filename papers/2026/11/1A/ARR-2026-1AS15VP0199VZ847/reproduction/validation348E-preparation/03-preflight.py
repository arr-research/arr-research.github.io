import signal, time, resource, traceback
def observed_child(label,argv,timeout):
    require(platform.node()==OWNED_RUNTIME_NODE, 'Owned validation runtime changed')
    prefix=ROOT/label
    observation={'argv':argv,'hostname':platform.node(),'started_at':datetime.now(timezone.utc).isoformat(),
                 'actual_exit':None,'timed_out':False,'error':None}
    child=None;start=time.perf_counter()
    try:
        with prefix.with_suffix('.stdout').open('xb') as out, prefix.with_suffix('.stderr').open('xb') as err:
            child=subprocess.Popen(argv,cwd=ROOT,stdout=out,stderr=err,start_new_session=True)
            try: observation['actual_exit']=child.wait(timeout=timeout)
            except subprocess.TimeoutExpired:
                observation['timed_out']=True
                try: os.killpg(child.pid,signal.SIGKILL)
                except ProcessLookupError: pass
                observation['actual_exit']=child.wait()
            out.flush();os.fsync(out.fileno());err.flush();os.fsync(err.fileno())
    except BaseException:
        observation['error']=traceback.format_exc()
        if child is not None and child.poll() is None:
            try: os.killpg(child.pid,signal.SIGKILL)
            except ProcessLookupError: pass
            observation['actual_exit']=child.wait()
        raise
    finally:
        observation.update(finished_at=datetime.now(timezone.utc).isoformat(),wall_seconds=time.perf_counter()-start,
                           children_max_rss_kib_cumulative=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
        if observation['actual_exit'] is not None:
            with prefix.with_suffix('.exit').open('x',encoding='ascii') as stream: stream.write(str(observation['actual_exit'])+'\n')
        observation['files']={ext:{'bytes':prefix.with_suffix(ext).stat().st_size,'sha256':digest(prefix.with_suffix(ext).read_bytes())}
                              for ext in ('.stdout','.stderr','.exit') if prefix.with_suffix(ext).is_file()}
        with prefix.with_suffix('.observation.json').open('x',encoding='utf-8') as stream:
            json.dump(observation,stream,indent=2);stream.write('\n')
        print(json.dumps(observation))
    return observation
preflight=observed_child('preflight-call',[sys.executable,str(ROOT/'run_preflight348E.py')],300)
require(preflight['actual_exit']==0 and not preflight['timed_out'] and preflight['error'] is None,
        'Current 348E predicates failed: preserve files, stop actual validation, export evidence')
