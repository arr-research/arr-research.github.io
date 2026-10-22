# verify DRUP proofs with the Go RUP checker. usage: verifyall.py k K per_proof_timeout wall_budget_s prefix_regex
import sys,json,glob,subprocess,time,re,os
k,K,cap,wall=int(sys.argv[1]),int(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]); pat=re.compile(sys.argv[5])
r={}
for f in glob.glob('proof_n7_*.jsonl')+glob.glob('proof_n7_0.old')+glob.glob('proof_sub11_*.jsonl')+glob.glob('proof_sub112*.jsonl')+glob.glob('proof_one11*.jsonl')+glob.glob('proof_n6.jsonl'):
    for l in open(f):
        x=json.loads(l)
        if x['result']=='UNSAT' and pat.match(x['name']) and x.get('lemmas',0)>0: r[x['name']]=x['lemmas']
names=sorted(r,key=lambda n:r[n])
t0=time.time()
for i,n in enumerate(names):
    if i%K!=k: continue
    if time.time()-t0>wall: print(json.dumps(dict(name=n,result="NOT-RUN(budget)",lemmas=r[n])),flush=True); continue
    s=time.time()
    try:
        p=subprocess.run([os.path.abspath('rupgo/rup.exe'),f'proofs/{n}.cnf',f'proofs/{n}.drup'],capture_output=True,text=True,timeout=cap)
        out=p.stdout.strip()
        res="VERIFIED" if p.returncode==0 and out.startswith("VERIFIED") else "FAIL"
    except subprocess.TimeoutExpired:
        out="";res="TIMEOUT"
    print(json.dumps(dict(name=n,result=res,lemmas=r[n],time=round(time.time()-s,1),out=out)),flush=True)
