actual_runs=[]
for mode,args in [('normal',[]),('optimized',['-O'])]:
    actual_runs.append(observed_child('actual-call-'+mode,[sys.executable,*args,str(ROOT/'validate348E_actual_colab.py'),
        'b74ab3e6e1d349aafe5ed42d984270e0ae1ee86ac158a1d9738dc6274f1b6e4b'],300))
summary={'hostname':platform.node(),'observed_at':datetime.now(timezone.utc).isoformat(),
         'runs':actual_runs,'accepted':False,'scope':'Validation only; original production348D and its PDF unchanged; not mathematical, visual or publication approval'}
try:
    require(all(r['actual_exit']==0 and r['timed_out'] is False and r['error'] is None for r in actual_runs),'Both actual-return modes must pass')
    results=[json.loads((ROOT/('actual-'+mode)/'result.json').read_bytes()) for mode in ('normal','optimized')]
    for key in ('source','PDF_sha256','PDF_bytes','pages','archive_sha256','raw_members_verified','source_input_members_verified','input_bundle_sha256','validator_sha256'):
        require(results[0][key]==results[1][key], 'Normal/-O actual-return agreement: '+key)
    require(results[0]['PDF_sha256']=='9f5d88b88321ca9ddc2afd284861a217cde0a37057362c1962a8cf988c42b29a' and
            results[0]['PDF_bytes']==345832 and results[0]['pages']==10,'Unchanged production PDF identity')
    summary.update(accepted=True,results=results)
finally:
    with (ROOT/'actual-summary.json').open('x',encoding='utf-8') as stream:
        json.dump(summary,stream,indent=2);stream.write('\n')
    print(json.dumps(summary))
