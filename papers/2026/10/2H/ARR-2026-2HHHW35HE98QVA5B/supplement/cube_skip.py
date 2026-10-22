# cube-and-conquer: cube = first terna of the sequence (WLOG sorted coords by S3 symmetry; see INFORME)
import sys,itertools,time,json,functools
from pysat.solvers import Solver
from pysat.card import CardEnc,EncType
from common import *
n=int(sys.argv[1]); mm=int(sys.argv[2]); sname=sys.argv[3]; k=int(sys.argv[4]); K=int(sys.argv[5])
T=list(itertools.product(range(1,n+1),repeat=3)); idx={t:i+1 for i,t in enumerate(T)}
cubes=[t for t in T if t[0]<=t[1]<=t[2]]
cubes.sort(key=lambda f:-sum(1 for u in T if lt2(f,u)))   # big cubes first? keep deterministic
cubes=[c for i,c in enumerate(cubes) if i%K==k]
pairs=[]
for s,t in itertools.combinations(T,2):
    if not lt2(s,t) and not lt2(t,s): pairs.append([-idx[s],-idx[t]])
for a in range(1,n+1):
  for b in range(1,n+1):
    pass
for f in [c for c in cubes if c!=(1,1,1)]:
    cand=[u for u in T if lt2(f,u)]
    if len(cand)+1<mm: print(json.dumps(dict(first=f,result="UNSAT",why="too few candidates",cand=len(cand))),flush=True); continue
    cs=set(cand)|{f}
    cl=[c for c in pairs if all(T[abs(l)-1] in cs for l in c)]
    cl+=[[idx[f]]]+[[-idx[u]] for u in T if u not in cs]
    lits=[idx[u] for u in cand]
    card=CardEnc.atleast(lits=lits,bound=mm-1,top_id=len(T),encoding=EncType.seqcounter)
    S=Solver(name=sname,bootstrap_with=cl+card.clauses)
    t0=time.time();it=0;added=0
    while True:
        if not S.solve(): print(json.dumps(dict(first=f,result="UNSAT",cycles=added,iters=it,time=round(time.time()-t0,1))),flush=True);break
        sel=[T[l-1] for l in S.get_model() if 0<l<=len(T)]
        new=0
        for a,b,c in itertools.permutations(sel,3):
            if a<b and a<c and lt2(a,b) and lt2(b,c) and lt2(c,a):
                S.add_clause([-idx[a],-idx[b],-idx[c]]);new+=1
        it+=1;added+=new
        if new==0:
            seq=sorted(sel,key=functools.cmp_to_key(lambda p,q:-1 if lt2(p,q) else 1))
            print(json.dumps(dict(first=f,result="SAT",size=len(seq),valid=check_seq(seq,n),seq=seq,time=round(time.time()-t0,1))),flush=True);break
    S.delete()
