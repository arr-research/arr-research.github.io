import sys,hashlib
from pysat.solvers import Cadical153
def pairs(N):
    return [(x+y,x*y) for x in range(3,N) for y in range(x,N) if x*y<=N]
def sat(N,r):
    P=pairs(N); v=lambda n,c:(n-1)*r+c+1
    s=Cadical153(); cl=[]
    for n in range(1,N+1): cl.append([v(n,c) for c in range(r)])
    for a,b in P:
        for c in range(r): cl.append([-v(a,c),-v(b,c)])
    # symmetry: colour of 6 (x=y=3 gives 6,9) -> fix colour 0 on n=6 (if N>=6)
    if N>=6: cl.append([v(6,0)])
    for c in cl: s.add_clause(c)
    ok=s.solve(); m=s.get_model() if ok else None
    col=None
    if ok:
        col={n:next(c for c in range(r) if m[v(n,c)-1]>0) for n in range(1,N+1)}
    return ok,col
def check(N,r,col):
    return all(col[a]!=col[b] for a,b in pairs(N))
for r in (1,2,3):
    N=1
    while True:
        ok,col=sat(N,r)
        if not ok: print("r",r,"N0 =",N); break
        assert check(N,r,col); last=(N,col)
        N+=1
        if N>400: print("r",r,"no UNSAT up to 400"); break
    print(" last colourable N",last[0],"".join(str(last[1][n]) for n in range(1,last[0]+1)))
