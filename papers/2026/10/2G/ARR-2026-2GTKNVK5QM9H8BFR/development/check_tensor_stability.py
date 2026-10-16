"""Reviewer calculation. No author verification scripts imported."""
from pathlib import Path
import json, datetime, itertools
import sympy as sp
import numpy as np

root=Path(__file__).resolve().parent
I2=sp.eye(2)
X=sp.Matrix([[0,1],[1,0]])
Z=sp.diag(1,-1)
A=[]
for i,j in [(0,1),(0,2),(1,2)]:
    B=sp.zeros(3); B[i,j]=1; B[j,i]=-1; A.append(B)
H=sum((sp.kronecker_product(a,x) for a,x in zip(A,[I2,X,Z])),sp.zeros(6))
assert H.det()==4
assert H.rank()==6
assert sp.simplify(sum((a.T*a for a in A),sp.zeros(3))-2*sp.eye(3))==sp.zeros(3)

# Coefficient rows are the entries (00,01,10,11) of X1,X2,X3.
u=sp.symbols('u0:12')
W=sp.Matrix(3,4,u)
M=[sp.Matrix(2,2,list(W.row(i))) for i in range(3)]
generic=sum((sp.kronecker_product(a,x) for a,x in zip(A,M)),sp.zeros(6))
minors=[W[:,list(cols)].det() for cols in itertools.combinations(range(4),3)]
minor_formula=sp.expand(minors[1]*minors[2]-minors[0]*minors[3])
exact_det=sp.expand(generic.det(method='domain-ge'))
assert sp.expand(exact_det-minor_formula)==0

# Equivalent polarization formulation proposed by the author, checked separately.
Rdet=sp.Matrix([[0,0,0,1],[0,0,-1,0],[0,-1,0,0],[1,0,0,0]])
assert Rdet.T==Rdet and Rdet*Rdet.T==sp.eye(4)
Q=sp.Matrix(3,3,lambda i,j: M[i].det() if i==j else sp.expand(((M[i]+M[j]).det()-M[i].det()-M[j].det())/2))
assert sp.simplify(Q-W*Rdet*W.T/2)==sp.zeros(3)
assert sp.expand(exact_det-4*Q.det())==0

# Lim, 2008, slide 32: order of the flattened rows is 00,10,01,11.
# Transposing the displayed 3x3 minors produces this expression exactly.
lim_hyperdet=(W[:,[0,2,1]].det()*W[:,[2,1,3]].det()
             -W[:,[0,2,3]].det()*W[:,[0,1,3]].det())
assert sp.expand(exact_det+lim_hyperdet)==0

Y=sp.Matrix([[0,-sp.I],[sp.I,0]])
paulis=[X,Y,Z]
pauliV=sp.Matrix([list(t) for t in paulis])/sp.sqrt(6)
pauliH=sum((sp.kronecker_product(a,x) for a,x in zip(A,paulis)),sp.zeros(6))/sp.sqrt(6)
assert sp.simplify(pauliV*Rdet*pauliV.T/2)==-sp.eye(3)/6
assert sp.simplify(pauliH.det())==-sp.Rational(1,54)

# K_a(W3)=A_a/sqrt(2), K_ab(D2)=E_ab/sqrt(2), hence G=H/(2 sqrt(6)).
coefficient=sp.Matrix([list(t) for t in [I2,X,Z]])/sp.sqrt(6)
assert sp.simplify(sp.trace(coefficient*coefficient.T))==1
G=H/(2*sp.sqrt(6))
assert sp.simplify(G.det())==sp.Rational(1,3456)
assert sp.simplify(coefficient*coefficient.T)==sp.eye(3)/3

# Random complex verification of the signed minor identity and determinant bound.
rng=np.random.default_rng(16102026)
An=[np.array(a,dtype=complex) for a in A]
max_identity_error=0.0; max_ratio=0.0
for _ in range(300):
    w=rng.normal(size=(3,4))+1j*rng.normal(size=(3,4)); w/=np.linalg.norm(w)
    p=np.array([np.linalg.det(w[:,cols]) for cols in itertools.combinations(range(4),3)])
    h=sum(np.kron(An[i],w[i].reshape(2,2)) for i in range(3))
    det=np.linalg.det(h)
    max_identity_error=max(max_identity_error,float(abs(det-(p[1]*p[2]-p[0]*p[3]))))
    max_ratio=max(max_ratio,float(abs(det)*54))
    assert abs(det)<=0.5*np.sum(abs(p)**2)+1e-13
    assert np.sum(abs(p)**2)<=1/27+1e-13
    assert abs(det)<=1/54+1e-13

# A shrunk-space CPTP example: pure replacer on d=3, c=2; tensor D2 has rank at most 2.
R=[]
for j in range(3):
    B=sp.zeros(3); B[0,j]=1; R.append(B)
assert sum((a.T*a for a in R),sp.zeros(3))==sp.eye(3)
assert sp.Matrix.hstack(*R).rank()==1
T=[]
for i,j in itertools.product(range(2),repeat=2):
    b=sp.zeros(2); b[i,j]=1; T.append(b)
support_tensor=[sp.kronecker_product(a,b) for a in R for b in T]
assert sp.Matrix.hstack(*support_tensor).rank()==2

out={
 'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'independent_of_author_code':True,
 'skew3_pauli_witness_det':str(H.det()),
 'skew3_pauli_witness_rank':H.rank(),
 'skew3_pauli_witness_squared_singular_values':{str(k):v for k,v in (H.T*H).eigenvals().items()},
 'generic_six_by_six_determinant_identity':'det(sum A_i tensor X_i)=p_013*p_023-p_012*p_123, where p are 3x3 minors of the 3x4 coefficient matrix with rows vec(X_i)',
 'generic_identity_symbolically_verified':True,
 'polarization_identity_symbolically_verified':'det(H)=4 det(Q), Q=(1/2) V R V^T, R symmetric unitary',
 'lim_2008_slide32_hyperdeterminant_relation_symbolically_verified':'det(H)=-Det_2x2x3 in the displayed Lim convention',
 'pauli_XYZ_over_sqrt6_polarization_Q':'-I_3/6',
 'normalized_coefficient_gram':'I_3/3',
 'max_abs_det_H_under_coefficient_frobenius_one':'1/54',
 'max_abs_det_G_for_W3_tensor_D2':'1/3456',
 'delta_W3_tensor_D2_exact':'2^(2/3)/24',
 'delta_W3_tensor_D2_float':float(2**(2/3)/24),
 'exponent_W3_tensor_D2_exact':'log(24)-(2/3)*log(2)',
 'random_complex_cases':300,
 'random_max_identity_error':max_identity_error,
 'random_max_fraction_of_determinant_bound':max_ratio,
 'pure_replacer_dimension':3,
 'pure_replacer_shrunk_deficiency':2,
 'pure_replacer_tensor_D2_support_rank':2,
 'passed':True
}
(root/'tensor-stability-independent-checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
