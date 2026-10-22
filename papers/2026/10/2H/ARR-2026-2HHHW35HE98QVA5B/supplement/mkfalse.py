import itertools,sys
from pysat.card import CardEnc,EncType
from common import *
# CNF for n=6, m (default 14) with the same construction as proofcubes (no fixed terna)
n=6;mm=int(sys.argv[1])
T=list(itertools.product(range(1,n+1),repeat=3)); idx={t:i+1 for i,t in enumerate(T)}
cl=[[-idx[s],-idx[t]] for s,t in itertools.combinations(T,2) if not lt2(s,t) and not lt2(t,s)]
card=CardEnc.atleast(lits=list(idx.values()),bound=mm,top_id=len(T),encoding=EncType.seqcounter)
allc=cl+card.clauses;nv=max(abs(l) for c in allc for l in c)
with open(f'proofs/n6_m{mm}.cnf','w') as f:
    f.write(f'p cnf {nv} {len(allc)}\n')
    for c in allc: f.write(' '.join(map(str,c))+' 0\n')
