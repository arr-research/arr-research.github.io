# Glucose4 DRUP proofs. usage: proofcubes.py n6 | n7 k K cap_seconds
import sys,itertools,time,json,threading
from pysat.solvers import Solver
from pysat.card import CardEnc,EncType
from common import *
mode=sys.argv[1]
def run(name,n,mm,fixed,cap):
    T=list(itertools.product(range(1,n+1),repeat=3)); idx={t:i+1 for i,t in enumerate(T)}
    cs=set(fixed)|{u for u in T if all(lt2(f,u) for f in fixed)}
    assert all(lt2(fixed[i],fixed[j]) for i in range(len(fixed)) for j in range(i+1,len(fixed)))
    cl=[]
    for s,t in itertools.combinations(sorted(cs),2):
        if not lt2(s,t) and not lt2(t,s): cl.append([-idx[s],-idx[t]])
    cl+=[[idx[f]] for f in fixed]+[[-idx[u]] for u in T if u not in cs]
    lits=[idx[u] for u in sorted(cs) if u not in fixed]
    if len(lits)+len(fixed)<mm:
        return dict(name=name,result="UNSAT-trivial",note="too few candidates (no proof file needed: cardinality)")
    card=CardEnc.atleast(lits=lits,bound=mm-len(fixed),top_id=len(T),encoding=EncType.seqcounter)
    base=cl+card.clauses
    S=Solver(name='glucose4',bootstrap_with=base,with_proof=True)
    extra=[];t0=time.time()
    tm=threading.Timer(cap,lambda:S.interrupt()); tm.start()
    while True:
        r=S.solve_limited(expect_interrupt=True)
        if r is None: tm.cancel(); return dict(name=name,result="TIMEOUT",time=round(time.time()-t0,1))
        if r is False: tm.cancel();break
        sel=[T[l-1] for l in S.get_model() if 0<l<=len(T)]
        new=[]
        for a,b,c in itertools.permutations(sel,3):
            if a<b and a<c and lt2(a,b) and lt2(b,c) and lt2(c,a): new.append([-idx[a],-idx[b],-idx[c]])
        if not new: tm.cancel(); return dict(name=name,result="SAT",seq=sel,time=round(time.time()-t0,1))
        for c in new: S.add_clause(c)
        extra+=new
    proof=S.get_proof()
    allc=base+extra
    nv=max(abs(l) for c in allc for l in c)
    with open(f'proofs/{name}.cnf','w') as fh:
        fh.write(f'p cnf {nv} {len(allc)}\n')
        for c in allc: fh.write(' '.join(map(str,c))+' 0\n')
    with open(f'proofs/{name}.drup','w') as fh:
        for l in proof: fh.write(l.strip()+'\n' if l.strip().endswith('0') else l.strip()+' 0\n')
    return dict(name=name,result="UNSAT",time=round(time.time()-t0,1),cycle_clauses=len(extra),lemmas=len(proof))
if mode=='n6':
    print(json.dumps(run('n6_m15',6,15,[],2000)),flush=True)
elif mode=='one11':
    n=7;mm=18;cap=float(sys.argv[2]);g=tuple(int(c) for c in sys.argv[3].split(','))
    print(json.dumps(run('c11_'+'_'.join(map(str,g)),n,mm,[(1,1,1),g],cap)),flush=True)
elif mode=='sub11':
    n=7;mm=18;k=int(sys.argv[2]);K=int(sys.argv[3]);cap=float(sys.argv[4]);f=(1,1,1)
    T=list(itertools.product(range(1,n+1),repeat=3))
    jobs=[((f,g),'c11_'+'_'.join(map(str,g))) for g in T if lt2(f,g) and g[0]<=g[1]<=g[2]]
    jobs.sort(key=lambda j:len({u for u in T if lt2(j[0][0],u) and lt2(j[0][1],u)}))
    for i,(fx,name) in enumerate(jobs):
        if i%K!=k: continue
        print(json.dumps(run(name,n,mm,list(fx),cap)),flush=True)
elif mode=='sub':
    n=7;mm=18;k=int(sys.argv[2]);K=int(sys.argv[3]);cap=float(sys.argv[4]);f=tuple(int(c) for c in sys.argv[5].split(','))
    T=list(itertools.product(range(1,n+1),repeat=3))
    import glob
    done=set(json.loads(l)['name'] for fn in glob.glob('proof_sub112*.jsonl') for l in open(fn))
    jobs=[((f,g),'s'+'_'.join(map(str,f))+'__'+'_'.join(map(str,g))) for g in T if lt2(f,g)]
    jobs=[j for j in jobs if j[1] not in done]
    for i,(fx,name) in enumerate(jobs):
        if i%K!=k: continue
        print(json.dumps(run(name,n,mm,list(fx),cap)),flush=True)
else:
    n=7;mm=18;k=int(sys.argv[2]);K=int(sys.argv[3]);cap=float(sys.argv[4])
    T=list(itertools.product(range(1,n+1),repeat=3))
    jobs=[((f,),f"c1_{'_'.join(map(str,f))}") for f in T if f[0]<=f[1]<=f[2] and f!=(1,1,1)]
    f=(1,1,1)
    jobs+=[((f,g),f"c11_{'_'.join(map(str,g))}") for g in T if lt2(f,g) and g[0]<=g[1]<=g[2]]
    def size(j):
        return len(set(j[0])|{u for u in T if all(lt2(f,u) for f in j[0])})
    jobs.sort(key=size)
    for i,(fx,name) in enumerate(jobs):
        if i%K!=k: continue
        print(json.dumps(run(name,n,mm,list(fx),cap)),flush=True)
