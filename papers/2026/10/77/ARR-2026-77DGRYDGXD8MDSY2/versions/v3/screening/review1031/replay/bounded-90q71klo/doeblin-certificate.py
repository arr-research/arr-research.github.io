"""Exact primal/dual and Bloch checks for a scoped source discrepancy."""
from pathlib import Path
import sympy as s,json
p=Path(__file__).parent;I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1)
vec=s.Matrix([1,0,0,1]);v=s.Matrix([1,0,0,-1]);dual=v*v.T
gamma=sum((s.kronecker_product(U,I)*vec*vec.T*s.kronecker_product(U,I).conjugate().T/s.Integer(3) for U in [I,X,Y]),s.zeros(4))
pt=s.Matrix(2,2,lambda i,j:sum(dual[2*a+i,2*a+j] for a in range(2)))
N=lambda b:(b+X*b*X+Y*b*Y)/3
checks={'choi_trace2':s.trace(gamma)==2,'choi_psd':gamma.eigenvals()=={s.Rational(2,3):3,s.Integer(0):1},'dual_psd_rank1':dual.eigenvals()=={s.Integer(2):1,s.Integer(0):3},'dual_partialtrace_I':pt==I,'dual_objective_zero':s.trace(dual*gamma)==0,'bloch_X':N(X)==X/3,'bloch_Y':N(Y)==Y/3,'bloch_Z':N(Z)==-Z/3}
assert all(checks.values())
result={'scope':'Parent exact counterexample to Theorem5 as printed in2503.22823v3/published Quantum2115, NOT a claim about the rest of that paper','channel':'(id+AdX+AdY)/3','weights':['1/3','1/3','1/3','0'],'unnormalized_choi':str(gamma),'dual_feasible_Y':str(dual),'primal_feasible_X':'zero2x2','alpha_exact':'0','ordinary_trace_distance_coefficient_exact':'1/3','checks':checks,'interpretation':'PrimalX0 gives alpha>=0; dualY gives alpha<=0. T=diag(1,1,-1)/3 has Euclidean norm ratio1/3 for every nonzero Bloch difference. Thus alpha>0 iff eta_Tr<1 fails in this example. No conclusion about complete SLD is needed for this counterexample.','external_review':None,'novelty_established':False}
(p/'DOEBLIN997.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
