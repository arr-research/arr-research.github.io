# independent method: pure SAT with lazy transitivity clauses
import sys,itertools,time,json
from pysat.solvers import Cadical153
from pysat.card import CardEnc,EncType
from common import *
n=int(sys.argv[1]); mm=int(sys.argv[2])
T=list(itertools.product(range(1,n+1),repeat=3)); idx={t:i+1 for i,t in enumerate(T)}
cl=[]
for s,t in itertools.combinations(T,2):
    if not lt2(s,t) and not lt2(t,s): cl.append([-idx[s],-idx[t]])
card=CardEnc.atleast(lits=list(idx.values()),bound=mm,top_id=len(T),encoding=EncType.seqcounter)
S=Cadical153(bootstrap_with=cl+card.clauses)
t0=time.time();it=0;added=0
while True:
    if not S.solve(): print(json.dumps(dict(n=n,m=mm,result="UNSAT",cycle_clauses=added,iters=it,time=round(time.time()-t0,1)))); break
    mod=set(l for l in S.get_model() if 0<l<=len(T)); sel=[T[l-1] for l in mod]
    # find 3-cycles
    new=0
    for a,b,c in itertools.permutations(sel,3):
        if a<b and a<c and lt2(a,b) and lt2(b,c) and lt2(c,a):
            S.add_clause([-idx[a],-idx[b],-idx[c]]);new+=1
    it+=1;added+=new
    if new==0:
        # transitive tournament -> order by topological sort
        import functools
        seq=sorted(sel,key=functools.cmp_to_key(lambda p,q:-1 if lt2(p,q) else 1))
        print(json.dumps(dict(n=n,m=mm,result="SAT",size=len(seq),valid=check_seq(seq,n),seq=seq,iters=it,time=round(time.time()-t0,1)))); break
