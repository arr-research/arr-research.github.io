import sys,time
from pysat.solvers import Cadical153
def run(N,r,distinct):
    P=[(x+y,x*y) for x in range(3,N) for y in range(x+(1 if distinct else 0),N) if x*y<=N]
    v=lambda n,c:(n-1)*r+c+1
    s=Cadical153()
    for n in range(1,N+1): s.add_clause([v(n,c) for c in range(r)])
    for a,b in P:
        for c in range(r): s.add_clause([-v(a,c),-v(b,c)])
    s.add_clause([v(6,0)] if N>=6 else [v(1,0)])
    ok=s.solve()
    if ok:
        m=s.get_model(); col=[next(c for c in range(r) if m[v(n,c)-1]>0) for n in range(1,N+1)]
        assert all(col[a-1]!=col[b-1] for a,b in P)
    return ok
mode=sys.argv[1]=="d"; r=int(sys.argv[2])
for N in map(int,sys.argv[3:]):
    t=time.time(); print(sys.argv[1],r,N,run(N,r,mode),round(time.time()-t,1),flush=True)
