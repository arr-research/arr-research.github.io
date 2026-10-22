# Independent verification of N0(r) via OR-tools CP-SAT (integer colour vars, no symmetry breaking)
# and a pure-python witness checker. Writes CNFs, witnesses and SHA-256 hashes.
import hashlib,json
from ortools.sat.python import cp_model
def pairs(N,distinct=False):
    return [(x+y,x*y) for x in range(3,N) for y in range(x+(1 if distinct else 0),N) if x*y<=N]
def cp(N,r):
    m=cp_model.CpModel(); c=[None]+[m.NewIntVar(0,r-1,f"c{n}") for n in range(1,N+1)]
    for a,b in pairs(N): m.Add(c[a]!=c[b])
    s=cp_model.CpSolver(); s.parameters.max_time_in_seconds=2400; s.parameters.num_workers=8
    st=s.Solve(m)
    if st==cp_model.OPTIMAL: return True,[s.Value(c[n]) for n in range(1,N+1)]
    if st==cp_model.INFEASIBLE: return False,None
    raise RuntimeError(s.StatusName(st))
out={}
for r,Ns in((2,(53,54)),(3,(773,774))):
    for N in Ns:
        ok,col=cp(N,r); print("CP-SAT",r,N,ok,flush=True)
        if ok:
            assert all(col[a-1]!=col[b-1] for a,b in pairs(N))
            s="".join(map(str,col)); open(f"witness_r{r}_N{N}.txt","w").write(s+"\n")
            out[f"witness_r{r}_N{N}"]=hashlib.sha256(s.encode()).hexdigest()
        out[f"cpsat_r{r}_N{N}"]=ok
        # DIMACS
        v=lambda n,k:(n-1)*r+k+1
        cl=[[v(n,k) for k in range(r)] for n in range(1,N+1)]+[[-v(a,k),-v(b,k)] for a,b in pairs(N) for k in range(r)]
        txt=f"p cnf {N*r} {len(cl)}\n"+"".join(" ".join(map(str,c))+" 0\n" for c in cl)
        open(f"n0_r{r}_N{N}.cnf","w").write(txt); out[f"cnf_r{r}_N{N}"]=hashlib.sha256(txt.encode()).hexdigest()
json.dump(out,open("hashes.json","w"),indent=1)
