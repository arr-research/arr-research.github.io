import sys,time
from pysat.solvers import Solver
from pysat.formula import CNF
f=sys.argv[1]; cnf=CNF(from_file=f)
s=Solver(name="glucose4",bootstrap_with=cnf.clauses,with_proof=True)
t=time.time(); ok=s.solve(); print(f,"sat" if ok else "unsat",round(time.time()-t,1))
if not ok:
    pr=s.get_proof(); open(f[:-4]+".drup","w").write("\n".join(l for l in pr if not l.startswith("d"))+"\n"); print(len(pr),"lines")
