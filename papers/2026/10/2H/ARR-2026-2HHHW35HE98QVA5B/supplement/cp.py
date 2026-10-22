import sys,itertools,time,json
from ortools.sat.python import cp_model
from common import *
n=int(sys.argv[1]); tl=float(sys.argv[2]); lb=int(sys.argv[3]) if len(sys.argv)>3 else 0
T=list(itertools.product(range(1,n+1),repeat=3))
UB=n*n
m=cp_model.CpModel()
x={t:m.NewBoolVar(str(t)) for t in T}
r={t:m.NewIntVar(0,UB-1,'r'+str(t)) for t in T}
for s,t in itertools.combinations(T,2):
    a,b=lt2(s,t),lt2(t,s)
    if a: m.Add(r[s]<r[t]).OnlyEnforceIf([x[s],x[t]])
    elif b: m.Add(r[t]<r[s]).OnlyEnforceIf([x[s],x[t]])
    else: m.AddBoolOr([x[s].Not(),x[t].Not()])
# pigeonhole: <=1 triple per (a1,a2)
for a in range(1,n+1):
  for b in range(1,n+1):
    m.AddAtMostOne([x[(a,b,c)] for c in range(1,n+1)])
    m.AddAtMostOne([x[(a,c,b)] for c in range(1,n+1)])
    m.AddAtMostOne([x[(c,a,b)] for c in range(1,n+1)])
tot=sum(x.values())
if lb: m.Add(tot>=lb)
m.Maximize(tot)
s=cp_model.CpSolver(); s.parameters.max_time_in_seconds=tl; s.parameters.num_workers=8
t0=time.time(); st=s.Solve(m)
sel=[t for t in T if s.Value(x[t])] if st in(cp_model.OPTIMAL,cp_model.FEASIBLE) else []
seq=sorted(sel,key=lambda t:s.Value(r[t]))
print(json.dumps(dict(n=n,status=s.StatusName(st),value=len(seq),bound=s.BestObjectiveBound(),time=round(time.time()-t0,1),seq=seq,valid=check_seq(seq,n),n32=round(n**1.5,3))))
