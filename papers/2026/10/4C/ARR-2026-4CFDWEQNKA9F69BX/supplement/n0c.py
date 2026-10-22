import sys,hashlib
from pysat.solvers import Solver
def build(N,r,distinct):
    P=[(x+y,x*y) for x in range(3,N) for y in range(x+(1 if distinct else 0),N) if x*y<=N]
    v=lambda n,c:(n-1)*r+c+1
    cl=[[v(n,c) for c in range(r)] for n in range(1,N+1)]
    cl+=[[-v(a,c),-v(b,c)] for a,b in P for c in range(r)]
    cl.append([v(6,0)])
    return cl,P,v
def sat(N,r,d,name):
    cl,P,v=build(N,r,d)
    s=Solver(name=name,bootstrap_with=cl); ok=s.solve()
    if ok:
        m=s.get_model(); col=[next(c for c in range(r) if m[v(n,c)-1]>0) for n in range(1,N+1)]
        assert all(col[a-1]!=col[b-1] for a,b in P)
    return ok
if __name__!="__main__": sys.exit  # noqa
r=None
lo,hi=int(sys.argv[3]),int(sys.argv[4])  # lo SAT, hi UNSAT
for nm in("glucose4","maplechrono"):
    assert sat(lo,r,d,nm) and not sat(hi,r,d,nm)
    a,b=lo,hi
    while b-a>1:
        m=(a+b)//2
        if sat(m,r,d,nm): a=m
        else: b=m
    print(nm,"r",r,sys.argv[2],"N0 =",b,"(max colourable",a,")",flush=True)
