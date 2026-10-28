from pathlib import Path
import sympy as s,json,itertools
P=Path(__file__).parent;Q=s.Rational;I=s.I
x=s.symbols('x',positive=True);F=lambda aa,bb: s.factor(x*(1-x)*sum((a-b)**2/(b+(a-b)*x) for a,b in zip(aa,bb)))
channels=[('binary',[Q(9,10),Q(1,10)],[Q(1,5),Q(4,5)],Q(1,2),Q(4,7)),('ternary_symmetric',[Q(1,2),Q(1,3),Q(1,6)],[Q(1,6),Q(1,3),Q(1,2)],Q(1,6),Q(1,2)),('four_flags',[Q(3,10),Q(3,5),Q(1,20),Q(1,20)],[Q(1,15),Q(2,15),Q(2,5),Q(2,5)],Q(1,2),Q(4,7))]
scalars=[]
for name,aa,bb,c,xx in channels:
 f=F(aa,bb);assert s.simplify(f.subs(x,xx)-c)==0
 assert s.simplify(s.diff(f,x,2)+2*sum((a-b)**2*a*b/(b+(a-b)*x)**3 for a,b in zip(aa,bb)))==0
 scalars.append({'channel':name,'a':list(map(str,aa)),'b':list(map(str,bb)),'c':str(c),'maximizer':str(xx),'gap_factor':str(s.factor(c-f)),'strict_concavity_identity':True})
rows=[]
for n in (2,3,4):
 G=s.Matrix(n,n,lambda i,j: Q((i+2)*(j+1)%5-2,5)+I*Q((i+3*j)%4-1,7));H=s.Matrix(n,n,lambda i,j: Q((2*i+j+1)%7-3,6)+I*Q((3*i+j)%5-2,8))
 A=G*G.conjugate().T+s.eye(n)/7;B=H*H.conjugate().T+s.eye(n)/5
 assert A*B!=B*A
 for name,aa,bb,c,xx in channels:
  M=s.simplify(c*(A.inv()+B.inv())-sum(((a-b)**2*(a*A+b*B).inv() for a,b in zip(aa,bb)),s.zeros(n)))
  assert M==M.conjugate().T
  minors=[s.factor(M[:j,:j].det()) for j in range(1,n+1)];assert all(v>0 for v in minors)
  z=s.Matrix([1+j*I for j in range(n)]);assert (z.conjugate().T*M*z)[0].simplify()>0
  rows.append({'n':n,'channel':name,'A':str(A),'B':str(B),'complex_noncommuting':True,'full_HS_operator_gap_positive':True,'leading_principal_minors':list(map(str,minors))})
# Semidefinite equality: cannot demand strictly positive Sylvester minors universally.
S=s.Matrix([[3,1+I],[1-I,2]]);A=Q(4,7)*S;B=Q(3,7)*S
aa,bb=channels[0][1:3];M=s.simplify(Q(1,2)*(A.inv()+B.inv())-sum(((a-b)**2*(a*A+b*B).inv() for a,b in zip(aa,bb)),s.zeros(2)));assert M==s.zeros(2)
# Finite classical quadratic pair refutes the old49/99 upper exactly.
sigma=[Q(4,7),Q(3,7)];rho=[Q(4,7)+Q(1,100),Q(3,7)-Q(1,100)]
chisq=lambda p,q:sum((a-b)**2/b for a,b in zip(p,q))
K=s.Matrix([[Q(9,10),Q(1,5)],[Q(1,10),Q(4,5)]]);ratio=s.factor(chisq(K*s.Matrix(rho),K*s.Matrix(sigma))/chisq(rho,sigma));assert ratio==Q(1,2)
# Wrong normalization: x=1/2 fixed Fisher is49/99, while global1/2.
assert F(*channels[0][1:3]).subs(x,Q(1,2))==Q(49,99)
# Sharp assumption failures: nonzero f(1) and arbitrary convex generators.
# TV ratio for any distinctbinaryprobabilities=.7; f(t)=abs(t-1) is not operatorconvex.
result={'scalar_controls':scalars,'operator_controls':rows,'equality_gap_zero':True,'old_guess_finite_falsifier':{'rho':list(map(str,rho)),'sigma':list(map(str,sigma)),'quadratic_and_minchi_ratio':str(ratio),'old_bound':'49/99','gap':'1/198'},'scope_falsifiers':{'TV_coefficient':'7/10 >1/2; abs(t-1) not operator convex','nonzero_f1':'f(t)=(t-1)^2+1 gives divergence1+chi2, ratio tends1 as rho tends sigma','unequal_reference':'rho=p_A tensor r, sigma=p_A tensor s gives ratio1 for every channel when r!=s','affine_f':'normalized affine f gives identically0 divergence; no positive denominator'},'passed':True}
(P/'EXACT1093.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print('9 exact complex operator checks, scalar identities, equality case and old-guess falsifier passed.')
