from fractions import Fraction as Q
from pathlib import Path
import json
C=Path('.')
def dump(path,value): print(json.dumps(value,indent=2))
I=((Q(1),Q(0)),(Q(0),Q(1)));X=((Q(0),Q(1)),(Q(1),Q(0)));Z=((Q(1),Q(0)),(Q(0),Q(-1)));XZ=((Q(0),Q(-1)),(Q(1),Q(0)))
zero=((Q(0),Q(0)),(Q(0),Q(0)))
def add(a,b):return tuple(tuple(a[i][j]+b[i][j] for j in range(2)) for i in range(2))
def scale(s,a):return tuple(tuple(s*a[i][j] for j in range(2)) for i in range(2))
def mul(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def tr(a):return a[0][0]+a[1][1]
def trans(a):return tuple(tuple(a[j][i] for j in range(2)) for i in range(2))
def total(xs):
    result=zero
    for a in xs:result=add(result,a)
    return result
units=[tuple(tuple(Q(i==a and j==b) for j in range(2)) for i in range(2)) for a in range(2) for b in range(2)]
us=[I,X,Z,XZ]
def twirl(a):return scale(Q(1,4),total(mul(mul(u,a),trans(u)) for u in us))
for a in units:assert twirl(a)==scale(tr(a)/2,I)
assert scale(Q(1,4),total(mul(trans(u),u) for u in us))==I
pure0=((Q(1),Q(0)),(Q(0),Q(0)));pure1=((Q(0),Q(0)),(Q(0),Q(1)));mixed=scale(Q(1,2),I)
assert all(mul(mul(u,mixed),trans(u))==mixed for u in us)
assert all(mul(mul(u,pure0),trans(u)) in [pure0,pure1] for u in us)
assert scale(Q(1,2),add(pure0,pure1))==mixed
# Four-point planar preparation instrument; same channel as a uniform continuous circle.
directions=[X,scale(Q(-1),X),Z,scale(Q(-1),Z)]
effects=[scale(Q(1,4),add(I,n)) for n in directions]
prepared=[scale(Q(1,2),add(I,n)) for n in directions]
assert total(effects)==I
def prep(a):return total(scale(tr(mul(f,a)),t) for f,t in zip(effects,prepared))
assert prep(I)==I and prep(X)==scale(Q(1,2),X) and prep(Z)==scale(Q(1,2),Z)
assert prep(XZ)==zero
# The dual effect after one prefix: G_i=(I+direction_i/2)/4, eigenvalues3/8,1/8.
for f,n in zip(effects,directions):
    g=scale(Q(1,4),add(I,scale(Q(1,2),n)))
    for a in units:assert tr(mul(f,prep(a)))==tr(mul(g,a))
    assert tr(g)==Q(1,2)
    assert g[0][0]*g[1][1]-g[0][1]*g[1][0]==Q(3,64)
assert 4*Q(1,8)==1-(2-1)*Q(1,2)
depolarizing=[]
for L in range(1,21):
    qL=Q(1,2)**L;a=scale(Q(1,2),add(I,scale(qL,Z)));b=scale(Q(1,2),add(I,scale(-qL,Z)))
    assert a!=b and a[0][0]-b[0][0]==qL
    depolarizing.append({'L':L,'state_trace_distance':str(qL),'posterior_point_mass_TV':'1','posterior_W1_trace_metric':str(qL)})
dump(C/'EXACT1206.json',{'arithmetic':'fractions.Fraction, no floating solver','checks':{'pauli_twirl_all4_complex_matrix_basis_units_by_complex_linearity':True,'trace_preserving_Kraus_sum':True,'two_distinct_posterior_invariant_laws_same_barycenter':True,'four_point_POVM_and_preparations':True,'planar_channel_Bloch_singular_values':['1/2','0','1/2'],'all4_dual_effect_basis_identities':True,'dual_effect_eigenvalues':['1/8','3/8'],'common_mass':'1/2','qubit_dimension_bound_saturated':True},'depolarizing_point_mass_cases':depolarizing,'scope':'Finite exact checks and analytic component; no general theorem certification, continuum quadrature or main-source proof audit.'})
