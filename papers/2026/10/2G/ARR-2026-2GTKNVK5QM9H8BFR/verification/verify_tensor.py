from pathlib import Path
import sympy as sp,numpy as np,json,math
ROOT=Path(__file__).parent
# An orthogonal basis of 3x3 skew matrices, with Frobenius norm sqrt(2).
A=[]
for i,j in [(0,1),(0,2),(1,2)]:
 a=sp.zeros(3);a[i,j]=1;a[j,i]=-1;A.append(a)
s=sp.symbols('s0:3')
H=sum((s[i]*sp.kronecker_product(A[i],A[i])/2 for i in range(3)),sp.zeros(9))
det=sp.factor(H.det())
assert det==-(s[0]*s[1]*s[2])**3/256,det
rng=np.random.default_rng(15102026);err=0.
An=[np.array(a,dtype=complex) for a in A]
for _ in range(100):
 Z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3));Z/=np.linalg.norm(Z)
 G=sum(Z[i,j]*np.kron(An[i],An[j])/2 for i in range(3) for j in range(3))
 e=abs(np.linalg.det(G)+np.linalg.det(Z)**3/256);err=max(err,e)
 assert e<1e-12
 assert abs(np.linalg.det(G))**(2/9)<=2**(2/9)/12+1e-12
report=dict(diagonal_determinant=str(det),random_complex_identity_checks=100,max_absolute_error=err,delta_tensor=2**(2/9)/12,exponent=math.log(12)-2*math.log(2)/9,individual_delta=0,individual_perfect_queries=3,tensor_perfect_queries=None,scope='Exact symbolic diagonal identity and numerical general identity; the manuscript supplies the unitary-congruence reduction.')
(ROOT/'verification-tensor.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
