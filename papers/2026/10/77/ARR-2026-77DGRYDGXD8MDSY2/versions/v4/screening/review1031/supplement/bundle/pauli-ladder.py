"""Exact identities for the positive-weight Pauli extension; no novelty claim."""
from pathlib import Path
import sympy as s,json
p=Path(__file__).parent
A,u,v,e=s.symbols('A u v e',real=True);B=1-A;z=2*A-1
weights=[(A+u)/2,(B+v)/2,(B-v)/2,(A-u)/2]
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1)
us=[s.kronecker_product(t,s.eye(3)) for t in [I,X,Y,Z]]
a=s.Matrix([1,0,0,0,e,0]);b=s.Matrix([0,e,0,0,0,1])
sigma=(a*a.T+b*b.T)/(2*(1+e*e));P=2*sigma;Q=s.eye(6)-P
D=s.zeros(6)
for i,j,val in [(0,4,1),(4,0,1),(4,4,2*e),(1,1,-2*e),(1,5,-1),(5,1,-1)]:D[i,j]=val
N=lambda t:sum((w*U*t*U.conjugate().T for w,U in zip(weights,us)),s.zeros(6))
J=s.Matrix([[0,0,1],[0,1,0],[1,0,0]])
M=s.Matrix([[A,u*e,0],[u*e,e*e,v*e],[0,v*e,B]])
T=s.Matrix([[0,u,0],[u,2*e*z,-v],[0,-v,0]])
rows=[0,4,2];cols=[3,1,5]
def block(a,r):return a.extract(r,r)
def zero(t):return all(s.factor(x)==0 for x in t)
checks={
 'sigma_trace':s.factor(s.trace(sigma)-1)==0,
 'projector':zero(P*P-P),
 'zero_partial_trace_tangent':zero(D[:3,:3]+D[3:,3:]),
 'zero_kernel_kernel':zero(Q*D*Q),
 'input_metric':s.factor(4*s.trace(D*D)-2*s.trace((P*D*P)**2)-16*(1+e*e))==0,
 'output_base_block1':zero(block(N(sigma),rows)-M/(2*(1+e*e))),
 'output_base_block2':zero(block(N(sigma),cols)-J*M*J/(2*(1+e*e))),
 'output_tangent_block1':zero(block(N(D),rows)-T),
 'output_tangent_block2':zero(block(N(D),cols)+J*T*J),
 'offblock_zero_base':zero(N(sigma).extract(rows,cols)),
 'offblock_zero_tangent':zero(N(D).extract(rows,cols))}
x,y,c=s.symbols('x y c',real=True)
YY=s.Matrix([[-e*u*x/A,x,-e*(u*y+v*x)],[x,c/e,y],[-e*(u*y+v*x),y,-e*v*y/B]])
R=M*YY+YY*M-4*(1+e*e)*T
K=s.Matrix([[A+e*e*(1-u*u/A-v*v),-e*e*u*v,u],[-e*e*u*v,B+e*e*(1-v*v/B-u*u),v],[u,v,1]])
rhs=4*(1+e*e)*s.Matrix([u,-v,z]);res=K*s.Matrix([x,y,c])-rhs
checks.update({'elimination_diagonals':zero(s.Matrix([R[0,0],R[2,2],R[0,2]])),
 'elimination_offdiagonals':zero(s.Matrix([R[0,1]-res[0],R[1,2]-res[1],R[1,1]-2*e*res[2]])),
 'output_metric_trace':s.factor(2*s.trace(T*YY)-4*(u*x-v*y+z*c))==0})
U=u*u/A;V=v*v/B;k=1-U-V
c0=4*(z-U+V)/k;x0=u*(4-c0)/A;y0=v*(-4-c0)/B
checks.update({'limiting_system_solution':zero(K.subs(e,0)*s.Matrix([x0,y0,c0])-rhs.subs(e,0)),
 'limiting_determinant':s.factor(K.subs(e,0).det()-A*B*k)==0,
 'output_base_determinant':s.factor(M.det()-A*B*e*e*k)==0,
 'positive_schur_identity':s.factor(k-4*weights[0]*weights[3]/A-4*weights[1]*weights[2]/B)==0,
 'limiting_ratio':s.factor((u*x0-v*y0+z*c0)/4-(U+V+(z-U+V)**2/k))==0,
 'harmonic_identity':s.factor(U+V+(z-U+V)**2/k-1+16/sum(1/w for w in weights))==0})
assert all(checks.values()),checks
result={'scope':'Exact algebra of explicit A2 R3 ladder and positive-weight Pauli output; analytic limiting argument in PROOF997.txt, no external audit or worldwide novelty certificate','checks':checks,'count':len(checks),'failures':0,'candidate':'eta_SLD_complete = eta_chi2_min_complete = eta_Petz_triangle_complete = 1-16/sum_j(1/w_j), w_j>0 sum1','limits':'No BKM, actual-MI, arbitrary-f sharpness, boundary-weight theorem or all-unital extension asserted here.'}
(p/'VERIFIED997.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
