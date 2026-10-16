from pathlib import Path
import sympy as s
import json,datetime
r=Path(__file__).parent
x=s.symbols('x0:12')
V=s.Matrix(3,4,x)
Z=[s.Matrix(2,2,list(V.row(i))) for i in range(3)]
Q=s.zeros(3)
for i in range(3):
 for j in range(3):
  Q[i,j]=s.expand(((Z[i]+Z[j]).det()-Z[i].det()-Z[j].det())/2)
R=s.Matrix([[0,0,0,1],[0,0,-1,0],[0,-1,0,0],[1,0,0,0]])
assert Q==s.expand(V*R*V.T/2)
assert R*R.T==s.eye(4)
A=[]
for i,j in [(0,1),(0,2),(1,2)]:
 B=s.zeros(3); B[i,j]=1; B[j,i]=-1; A.append(B)
M=sum((s.kronecker_product(a,z) for a,z in zip(A,Z)),s.zeros(6))
assert s.expand(M.det(method='domain-ge')-4*Q.det())==0
pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
G=sum((s.kronecker_product(a,z) for a,z in zip(A,pauli)),s.zeros(6))/(2*s.sqrt(6))
assert G.det()==-s.Rational(1,3456)
report={'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'symbolic_det_M_equals_four_det_Q':True,'polarization_matrix_unitary':True,'pauli_saturation_det':str(G.det()),'exact_delta':'2^(2/3)/24','role':'Author-side alternative derivation using polarized determinant; developed alongside reviewer minors derivation, not an independent review.'}
(r/'verification-polarization.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report))
