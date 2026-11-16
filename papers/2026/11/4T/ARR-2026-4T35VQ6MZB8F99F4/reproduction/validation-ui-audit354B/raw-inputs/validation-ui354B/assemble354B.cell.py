# Only the frozen existing materializer is called. Its strict decoding and readback are authoritative.
def observed_child354B(script,stem,seconds):
    prefix=UI/stem;started=now();child=None;error=None;timed_out=False;code=None
    with prefix.with_suffix('.stdout').open('xb') as so,prefix.with_suffix('.stderr').open('xb') as se:
        try:
            child=subprocess.Popen([sys.executable,str(BASE/script)],cwd=str(BASE),stdout=so,stderr=se,start_new_session=True)
            try:code=child.wait(timeout=seconds)
            except subprocess.TimeoutExpired:
                timed_out=True;os.killpg(child.pid,signal.SIGKILL);code=child.wait()
        except BaseException:
            error=traceback.format_exc()
            if child is not None and child.poll() is None:
                os.killpg(child.pid,signal.SIGKILL);code=child.wait()
            elif child is not None:code=child.returncode
    record=dict(script=script,argv=[sys.executable,str(BASE/script)],started_at=started,finished_at=now(),
                actual_exit=code,timeout=timed_out,error=error,hostname=platform.node())
    put(prefix.with_suffix('.json'),record)
    if code is not None:publish_exit(prefix,code)
    need(error is None and not timed_out and code is not None,'Native child failed; retain observations, do not infer success')
    read_exit(prefix.with_suffix('.exit'),require_success=True)
    return record
materialization_child=observed_child354B('materialize354A.py','input-materialization354B',300)
print(json.dumps(materialization_child))
