# Launch only after the preceding cell recorded actual owner and separate-review evidence.
need((P/'gates'/'authorization.json').is_file(),'Actual ready gate absent')
auth=json.loads((P/'gates'/'authorization.json').read_bytes())
need(auth['source']==SOURCE and auth['status']=='READY_AFTER_ACTUAL_PARENT_REVIEW'
     and auth['owner_observation']['observed_hostname']==platform.node(),'Stale/mismatched ready gate')
def publish_exit_no_replace(path,actual):
    need(type(actual) is int and not path.exists() and not path.is_symlink(),'New actual native exit only')
    temp=path.with_name(path.name+'.tmp')
    with temp.open('xb') as f:
        f.write((str(actual)+'\n').encode('ascii'));f.flush();os.fsync(f.fileno())
    raw=temp.read_bytes()
    need(re.fullmatch(rb'-?[0-9]+\n',raw) is not None and int(raw)==actual,'Closed integer sentinel')
    libc=ctypes.CDLL(None,use_errno=True)
    rename=libc.renameat2
    rename.argtypes=[ctypes.c_int,ctypes.c_char_p,ctypes.c_int,ctypes.c_char_p,ctypes.c_uint]
    rename.restype=ctypes.c_int
    rc=rename(-100,os.fsencode(temp),-100,os.fsencode(path),1)
    if rc!=0:raise OSError(ctypes.get_errno(),'No-replace sentinel publication failed; retain temp')
    need(path.read_bytes()==raw,'Native exit readback')
label='outer-launch354D'
paths=[UI/(label+s) for s in ('.stdout','.stderr','.exit','.observation.json')]
need(all(not p.exists() and not p.is_symlink() for p in paths),'Fresh attempt only; preserve previous logs')
started=now();t0=time.monotonic();actual=None;timed_out=False;error=None
argv=[sys.executable,str(P/'launch354D.py')]
try:
    with paths[0].open('xb') as out,paths[1].open('xb') as err:
        child=subprocess.Popen(argv,cwd=P,stdout=out,stderr=err,start_new_session=True)
        try:actual=child.wait(timeout=3600)
        except subprocess.TimeoutExpired:
            timed_out=True;os.killpg(child.pid,signal.SIGKILL);actual=child.wait()
        out.flush();os.fsync(out.fileno());err.flush();os.fsync(err.fileno())
    publish_exit_no_replace(paths[2],actual)
except BaseException:
    error=traceback.format_exc()
    raise
finally:
    observation={'source':SOURCE,'argv':argv,'cwd':str(P),'started_at':started,'finished_at':now(),
      'actual_exit':actual,'timed_out':timed_out,'error':error,
      'stdout_sha256':sha(paths[0].read_bytes()) if paths[0].is_file() else None,
      'stderr_sha256':sha(paths[1].read_bytes()) if paths[1].is_file() else None,
      'exit_sha256':sha(paths[2].read_bytes()) if paths[2].is_file() else None,
      'observed_outer_wall_seconds':time.monotonic()-t0,'billing_units':None,
      'runtime_closure_observed':False,'return_validation_performed':False}
    put(paths[3],observation)
print(json.dumps(observation))
need(actual==0 and not timed_out,'Native launcher failed/timed out: preserve bytes and export surviving evidence; no blind rerun')