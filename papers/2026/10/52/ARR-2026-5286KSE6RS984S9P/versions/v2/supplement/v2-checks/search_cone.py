import itertools, random, sys
from fractions import Fraction as Fr
def moments(nodes,K):
    # nodes: (x,y,m); returns list M_j j=1..K
    out=[Fr(0)]*(K+1)
    for (x,y,m) in nodes:
        z=(x,y)
        p=(Fr(1),Fr(0))
        for j in range(1,K+1):
            p=(p[0]*x-p[1]*y, p[0]*y+p[1]*x)
            out[j]+= m*(p[0] if y==0 else 2*p[0])
    return out
random.seed(int(sys.argv[2]))
K=int(sys.argv[1])
reals=[Fr(a,2) for a in range(1,13)]
pairs=[(Fr(a,2),Fr(b,2)) for a in range(1,9) for b in range(1,13)]
best=None
for it in range(400000):
    rn=random.sample(reals,K)
    np_=random.randint(1,K)
    pn=random.sample(pairs,np_)
    nodes=[(r,Fr(0),random.randint(1,4)) for r in rn]+[(x,y,random.randint(1,4)) for (x,y) in pn]
    M=moments(nodes,K)
    if all(M[j]==0 for j in range(2,K+1) if j!=3) and M[3]>0:
        tot=sum(n[2]*(1 if n[1]==0 else 2) for n in nodes)
        if best is None or tot<best[0]:
            best=(tot,nodes,M); print(tot,[(str(a),str(b),c) for a,b,c in nodes],[str(m) for m in M]); sys.stdout.flush()
