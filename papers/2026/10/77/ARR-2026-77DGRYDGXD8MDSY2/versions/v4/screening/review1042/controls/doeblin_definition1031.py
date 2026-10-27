"""Exact check of the source-definition objection; no source or manuscript edits."""
from pathlib import Path
import sympy as s,json
P0=s.diag(1,0);plus=s.ones(2)/2
X=s.Matrix([[s.Rational(3,8),s.Rational(1,4)],[s.Rational(1,4),-s.Rational(1,8)]])
assert X.det()<0 and s.trace(X)==s.Rational(1,4)
assert all(M[0,0]>0 and M.det()>0 for M in [P0-X,plus-X])
Gamma=s.diag(P0,plus)
assert Gamma-s.kronecker_product(s.eye(2),X)==s.diag(P0-X,plus-X)
# A PSD X dominated by both rank-one output states has support in their
# support intersection, which is zero. Thus alpha_+ of this CQ channel is0,
# whereas the Hermitian-X coefficient alpha is >=1/4 by this exact witness.
v=s.Matrix([1,0,0,-1]);Y=v*v.T;G=2*s.eye(4)/3-Y/3
pt=s.Matrix(2,2,lambda i,j:sum(Y[2*a+i,2*a+j] for a in range(2)))
assert pt==s.eye(2) and G*Y==s.zeros(4) and G.eigenvals()=={s.Rational(2,3):3,0:1}
out={'source':'arXiv:2503.22823v3, Definition4 Eq3.1, Proposition3 Eq3.3, Definition7 Eq3.25',
 'objection':'PDF1030 Section7 p9 gives alpha_+ primal and inequality dual while attributing them to alpha of Definition4. Correct alpha allows Hermitian X and has dual partial_trace(Y)=I.',
 'separating_CQ_example':{'Choi':str(Gamma),'Hermitian_indefinite_feasible_X':str(X),'trace_X':'1/4','alpha_lower_bound':'1/4','alpha_plus_exact':'0','PSD_slack_determinants':[str((P0-X).det()),str((plus-X).det())],'reason_alpha_plus_zero':'PSD X <= P0 and <= Pplus has support in intersection of two distinct rank-one ranges; intersection={0}.'},
 'manuscript_certificate_survives':{'Choi':str(G),'dual_Y':str(Y),'partial_trace_exactly_I':True,'dual_objective_zero':True,'primal_zero_feasible':True,'alpha_exact':'0','alpha_plus_exact':'0','ordinary_trace_contraction':'1/3'},
 'severity':'Correctable source-definition error. Does not invalidate Theorem4,5,7,Proposition6 or the stated counterexample conclusion.',
 'all_passed':True}
Path(__file__).with_name('DOEBLIN-DEFINITION1031.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'all_passed':True,'source_definition_error':True,'counterexample_conclusion_survives':True}))
