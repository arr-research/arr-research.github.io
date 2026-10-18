"""Fresh referee checks; does not import the supplied verifier.
Exact Bareiss/Sylvester tests, exact Gram reconstruction, and a numerical
ordinary-circuit cross-check. Only local input packet is read.
"""
from pathlib import Path
from fractions import Fraction as F
from math import lcm, comb
import json, hashlib
import numpy as np
from scipy.linalg import null_space

ROOT = Path(__file__).resolve().parent
INPUT = ROOT.parent / 'input'
Q = [[F(v) for v in row] for row in json.loads((INPUT/'certificate/Q.json').read_text())]
R = [[F(v) for v in row] for row in json.loads((INPUT/'certificate/R.json').read_text())]
assert len(Q)==len(R)==32
assert all(len(row)==32 for row in Q+R)
assert all(A[i][j]==A[j][i] for A in (Q,R) for i in range(32) for j in range(32))

def pd_bareiss(A):
    """Exact leading principal minors of a positive multiple; Sylvester."""
    den = lcm(*(x.denominator for row in A for x in row))
    M = [[int(x*den) for x in row] for row in A]
    prev, minors = 1, []
    for k in range(len(M)):
        pivot = M[k][k]
        assert pivot>0, ('nonpositive leading minor',k,pivot)
        minors.append(str(pivot))
        if k+1 == len(M):
            break
        for i in range(k+1,len(M)):
            for j in range(k+1,len(M)):
                numerator = pivot*M[i][j]-M[i][k]*M[k][j]
                assert numerator%prev==0, 'non-exact Bareiss division'
                M[i][j] = numerator//prev
        for i in range(k+1,len(M)):
            M[i][k] = 0
        prev = pivot
    return {'positive_scale':str(den),'positive_leading_minors':minors}

checks = {'Q':pd_bareiss(Q), 'Q-R':pd_bareiss([[Q[i][j]-R[i][j] for j in range(32)] for i in range(32)])}
groups = [[i for i in range(32) if i.bit_count()==w] for w in range(6)]
assert all(sum(R[i][j] for j in g)==0 for i in range(32) for g in groups)
refs = [g[0] for g in groups]
keep = [i for i in range(32) if i not in refs]
B = [[F(int(i==j)-int(i==refs[j.bit_count()])) for j in keep] for i in range(32)]
S = [[R[i][j] for j in keep] for i in keep]
checks['R_reduced'] = pd_bareiss(S)
assert all(R[i][j]==sum(B[i][a]*S[a][b]*B[j][b] for a in range(26) for b in range(26) if B[i][a] and B[j][b]) for i in range(32) for j in range(32))

levels = {5:Q}
for k in range(5,0,-1):
    a=levels[k]
    assert all(a[i][j]==0 for i in range(2**k) for j in range(2**k) if i%2!=j%2)
    levels[k-1]=[[a[2*i][2*j]+a[2*i+1][2*j+1] for j in range(2**(k-1))] for i in range(2**(k-1))]
assert levels[0]==[[F(1)]]
checks['lower_level_PD']={str(k):pd_bareiss(levels[k]) for k in range(1,5)}

eta=F(7,10)
fourier={k:sum(R[i][j]*eta**((i^j).bit_count()) for i in range(32) for j in range(32) if i.bit_count()-j.bit_count()==k) for k in range(-5,6)}
success=fourier[0]+(fourier[-1]+fourier[1])/2
assert success==F(8547317228981067,16000000000000000)
# Multiplication by the calibration likelihood yields a degree-six Laurent
# polynomial. All surviving 7-grid frequencies are exactly its constant term.
weighted={k:fourier.get(k,F(0))+(fourier.get(k-1,F(0))+fourier.get(k+1,F(0)))/2 for k in range(-6,7)}
assert weighted[0]==success
assert [k for k in weighted if k%7==0]==[0]
per_weight=[sum(F(comb(w,j)*comb(5-w,j))*eta**(2*j) for j in range(min(w,5-w)+1))/comb(5,w) for w in range(6)]
assert min(per_weight)==F(46603,100000)
beta6=sum(F(comb(3,j)**2)*eta**(2*j) for j in range(4))/20
assert beta6==F(7688549,20000000)
branches=[]
for z in range(32):
    val=sum(R[i][j]*(-1)**((z&(i^j)).bit_count())*(F(1) if i.bit_count()==j.bit_count() else F(1,2) if abs(i.bit_count()-j.bit_count())==1 else F(0)) for i in range(32) for j in range(32))
    branches.append(val)
assert branches[0]==branches[-1]==0
assert all(0<=v<=1 for v in branches)
assert sum(F(17,20)**(5-z.bit_count())*F(3,20)**z.bit_count()*branches[z] for z in range(32))==success

# Numerical circuit reconstruction is a diagnostic, not the exact proof.
# Each last-symbol block is represented by 16 memory coordinates.
nf=lambda a:np.array([[float(x) for x in row] for row in a])
frames={0:np.eye(32,1)}
for k in range(1,6):
    a=nf(levels[k]); V=np.zeros((32,2**k))
    for b in (0,1):
        ids=np.arange(b,2**k,2)
        gram=a[np.ix_(ids,ids)]
        L=np.linalg.cholesky(gram).T
        V[np.ix_(np.arange(16*b,16*b+len(ids)),ids)]=L
    frames[k]=V
controls=[]
errors=[]
for k in range(1,6):
    A=frames[k-1]; T=frames[k][:,0::2]+frames[k][:,1::2]
    C=np.linalg.cholesky(A.T@A).T
    left=A@np.linalg.inv(C); right=T@np.linalg.inv(C)
    U=right@left.T+null_space(right.T)@null_space(left.T).T
    errors.append({'k':k,'isometry_error':float(np.max(np.abs(U@A-T))),'unitarity_error':float(np.max(np.abs(U.T@U-np.eye(32))))})
    controls.append(U)
V=frames[5]
inv=np.linalg.inv(V)
effect=inv.T@nf(R)@inv
ev=np.linalg.eigvalsh(effect)
assert ev.min()>-1e-8 and ev.max()<1+1e-8
assert max(e['isometry_error'] for e in errors)<1e-8
assert max(e['unitarity_error'] for e in errors)<1e-8
def run_phase(phases):
    state=frames[0][:,0].astype(complex)
    for U,t in zip(controls,phases):
        state=U@state
        state[16:]*=np.exp(1j*t)
    return state
null_points=np.linspace(0,2*np.pi,97,endpoint=False)
null_errors=[]
for theta in null_points:
    st=run_phase([theta]*5)
    null_errors.append(float(abs(np.vdot(st,effect@st))))
def noisy_success(delta):
    total=0.
    for z in range(32):
        phases=[delta+np.pi*((z>>(4-k))&1) for k in range(5)]
        st=run_phase(phases)
        total+=(.85**(5-z.bit_count())*.15**z.bit_count())*float(np.vdot(st,effect@st).real)
    return total
carrier_points=np.linspace(0,2*np.pi,41,endpoint=False)
calibrated=[]
for phi in carrier_points:
    calibrated.append(sum((1+np.cos(phi-2*np.pi*j/7))/7*noisy_success(phi-2*np.pi*j/7) for j in range(7)))
assert max(null_errors)<1e-8
assert max(abs(x-float(success)) for x in calibrated)<1e-8
published=json.loads((INPUT/'certificate/verification.json').read_text())
replayed=json.loads((ROOT/'scratch/certificate/verification.json').read_text())
report={'status':'all independent checks passed','exact_method':'Integer Bareiss leading minors plus Sylvester; R=B S B^T with 26-column B and positive-definite S',
    'exact_ranks':[32,26,32],'null_reference_indices':refs,'exact_checks':checks,
    'fourier_coefficients':{str(k):str(v) for k,v in fourier.items()},
    'rejection':str(success),'failure':str(1-success),'parallel_by_weight':list(map(str,per_weight)),
    'gap':str(min(per_weight)-(1-success)),'parallel_six':str(beta6),
    'noise_branch_rejections':list(map(str,branches)),
    'published_verification_json_matches_replay':published==replayed,
    'numerical_diagnostics':{'controls':errors,'effect_eigenvalue_min':float(ev.min()),'effect_eigenvalue_max':float(ev.max()),
        'null_phases_tested':len(null_points),'largest_null_rejection_magnitude':max(null_errors),
        'carrier_phases_tested':len(carrier_points),'largest_calibrated_success_error':max(abs(x-float(success)) for x in calibrated),
        'total_dimension':32,'query_dimension':2,'signal_memory_dimension':16}}
(ROOT/'independent-checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(report['status'])
print('Published verifier report identical:',published==replayed)
print('Exact ranks:',report['exact_ranks'])
print('Success Fourier coefficients:',report['fourier_coefficients'])
print('Numerical diagnostics:',json.dumps(report['numerical_diagnostics'],indent=2))
