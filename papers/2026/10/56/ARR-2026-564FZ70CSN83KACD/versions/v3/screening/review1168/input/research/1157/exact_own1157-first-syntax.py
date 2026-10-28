"""Own deterministic exact controls. No input files are modified."""
import sympy as s,json
from pathlib import Path
P=Path(__file__).parent
I=s.I; R=s.Rational
def simp(M): return M.applyfunc(s.simplify)
def pure(v):
 v=s.Matrix(v);return v*v.H/(v.H*v)[0]
def zero(M): return simp(M)==s.zeros(*M.shape)
def tensor(A,B): return s.kronecker_product(A,B)
def case(name,ts):
 n=len(ts);d=ts[0].rows;S=sum(ts,s.zeros(d));us=[s.eye(n)[:,i]-s.ones(n,1)/n for i in range(n)]
 T=sum([tensor(u*u.H,t) for u,t in zip(us,ts)],s.zeros(n*d));Z=sum([tensor(u,t) for u,t in zip(us,ts)],s.zeros(n*d,d))
 Y,par=T.gauss_jordan_solve(Z);Y=Y.subs({a:0 for a in par});res=simp(Z.H*Y-S)
 constraints=s.Matrix.vstack(*[(s.eye(d)-t*t.pinv()) for t in ts]);common=d-constraints.rank()
 assert T.rank()==sum(t.rank() for t in ts)-common
 assert zero(T*Y-Z)
 assert zero(res)==(common==0)
 return dict(name=name,n=n,B=d,ranks=[t.rank() for t in ts],common_support_dimension=common,rank_T=T.rank(),kernel_T_in_P=(n-1)*d-T.rank(),quadratic_residual_zero=zero(res),residual=str(res))
rows=[case('binary_complex_pure',[pure([1,0]),pure([1,2*I/3])]),case('mixed_rank_1_2_1',[pure([1,0]),s.eye(2)/2,pure([1,I])]),case('three_complex_B3_kernel_T',[pure([1,0,0]),pure([1,1,0]),pure([1,I,1])]),case('duplicate_allowed',[pure([1,0]),pure([1,0]),pure([1,I])]),case('common_line_rank_two',[(s.eye(3)-pure(v))/2 for v in [[1,0,0],[0,1,0],[1,I,0]]]),case('full_rank_noncommuting',[s.diag(R(3,4),R(1,4)),s.Matrix([[R(1,2),I/4],[-I/4,R(1,2)]])])]
t,r=s.symbols('t r',positive=True);S=pure([1,0])+pure([1,t]);D=pure([1,0])-pure([1,t]);J=simp(S.inv()*D)
h=s.factor(s.trace((s.eye(2)+r*J.H*J).inv()*S));assert s.simplify(h-2*t*t*(1+r)/(t*t*(1+r)**2+4*r))==0
assert zero(D*S.inv()*D-S)
# n=2 implies T=G=S in the one-dimensional simplex sector, hence T0=I.
# A^-1 Z=J/alpha is unbounded as t->0 although whitened mu_min=1.
k=16;beta=R(1,8*k);delta=R(1,2**k);alpha=R(1,2)-beta;c2=alpha*beta*(1-delta);gamma=s.sqrt(c2)/alpha
S=pure([1,0])+pure([1,2*I/3]);D=pure([1,0])-pure([1,2*I/3]);J=simp(S.inv()*D);C=simp((s.eye(2)+(c2/alpha**2)*J.H*J).inv());H=(gamma*J).col_join(s.eye(2));E=simp(H*C*H.H)
Mp=(alpha*S).row_join(s.sqrt(c2)*D).col_join((s.sqrt(c2)*D).row_join(beta*S));Mm=(alpha*S).row_join(-s.sqrt(c2)*D).col_join((-s.sqrt(c2)*D).row_join(beta*S))
q=s.simplify(s.trace(E*Mm));p=s.simplify(s.trace(E*Mp));hh=s.simplify(s.trace(C*S))
assert zero(E*E-E) and zero(E-E.H) and s.trace(E)==2
assert q==beta*delta*hh and p==beta*(4-3*delta)*hh and 0<q<p<1
minors=[s.factor(Mp[:j,:j].det()) for j in range(1,5)];assert all(x>0 for x in minors)
PT=s.Matrix(4,4,lambda a,b:E[(a//2)*2+b%2,(b//2)*2+a%2]);ptdet=s.factor(PT.det())
# Local change of R basis does not affect PPT; this is the physical P,f ordering.
out={'exact_geometry_cases':rows,'binary_symbolic':{'J':str(simp((pure([1,0])+pure([1,t])).inv()*(pure([1,0])-pure([1,t]))),'h':str(h),'whitened_T0':'I_B for every distinct binary pair','nonuniform_t_k':'t=1/k implies h~2/k and measured retention->0'},'finite_complex_graph':{'n':2,'k':k,'pure_parameter':'2i/3','p':str(p),'q':str(q),'h':str(hh),'projector_exact':True,'rank':2,'output_Sylvester_minors':list(map(str,minors)),'partial_transpose_determinant':str(ptdet),'NPT_effect':bool(ptdet<0)},'congruence_warning':'Quadratic equality verified by factorization/solve; no general congruence rule for Moore-Penrose inverse used.'}
(P/'EXACT_OWN1157.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
