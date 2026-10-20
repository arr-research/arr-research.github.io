from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import hashlib,json,warnings
import numpy as np
import sympy as sp
import cvxpy as cp

R=Path(__file__).parent
out=R/'hierarchy-checks-31.json'
assert not out.exists()
exact=0
# Arbitrary rational vector: the Toeplitz smoothing identity does not
# require a sine vector, and can be checked without floating arithmetic.
z=sp.Rational(3,5)+sp.I*sp.Rational(4,5)
for N in range(1,8):
    v=[sp.Rational(j+1,2*N+3) for j in range(N+1)]
    m=[sp.Integer(1)]+[sp.Rational(k+1,3*k+5)+sp.I*sp.Rational(1,k+4) for k in range(1,N+1)]
    T=sp.Matrix(N+1,N+1,lambda j,k:m[k-j] if k>=j else sp.conjugate(m[j-k]))
    zz=sp.Matrix([v[j]*z**j for j in range(N+1)])
    direct=sp.expand((sp.conjugate(zz.T)*T*zz)[0])
    kap=[sum(v[j]*v[j+k] for j in range(N+1-k)) for k in range(N+1)]
    fourier=kap[0]+sum(kap[k]*(m[k]*z**k+sp.conjugate(m[k])*z**(-k)) for k in range(1,N+1))
    assert sp.simplify(direct-fourier)==0
    exact+=1
kernel=[]
for N in [1,2,3,4,8,16,32,64]:
    t=np.pi/(N+2);v=np.sqrt(2/(N+2))*np.sin(np.arange(1,N+2)*t)
    kap=np.array([np.dot(v[:N+1-k],v[k:]) for k in range(N+1)])
    assert abs(kap[0]-1)<2e-14 and abs(kap[1]-np.cos(t))<2e-14
    for k in range(1,N+4):
        kk=kap[k] if k<=N else 0
        assert 1-kk<=k*k*(1-kap[1])+1e-12
    kernel.append(dict(N=N,mean=float(kap[0]),first=float(kap[1]),exact_first_formula=float(np.cos(t))))
# Midpoint quantiles of atomic measures, checked exactly on both sides
# of every jump of both cumulative functions.
quantile_cases=0
weights=[Fraction(1,7),Fraction(2,7),Fraction(4,7)]
cdf=[sum(weights[:j+1]) for j in range(3)]
for M in range(1,60):
    counts=[0,0,0]
    for j in range(M):
        t=Fraction(2*j+1,2*M)
        ix=next(k for k,x in enumerate(cdf) if x>=t);counts[ix]+=1
    for k in range(3):
        assert abs(Fraction(sum(counts[:k+1]),M)-cdf[k])<=Fraction(1,2*M)
    quantile_cases+=1
rows=[]
for case in ['single','two_harmonics','variable_rotation']:
    for N in [1,2,4,8,16]:
        if case=='single': q=[1.5 if k==1 else 0 for k in range(1,N+1)];d2=3.
        elif case=='two_harmonics':q=[1.5 if k==1 else .75 if k==2 else 0 for k in range(1,N+1)];d2=9.
        else:q=[-6.25*(-1/3)**k for k in range(1,N+1)];d2=18.75
        m=cp.Variable(N,complex=True);a=cp.Variable(nonneg=True)
        w=cp.hstack([1j*m[k]-q[k] for k in range(N)])
        def toeplitz(seq,mass):
            return cp.bmat([[mass if j==k else seq[k-j-1] if k>j else cp.conj(seq[j-k-1]) for k in range(N+1)] for j in range(N+1)])
        tm=toeplitz(m,1);tw=toeplitz(w,a)
        prob=cp.Problem(cp.Minimize(a),[tm>>0,tw>>0])
        with warnings.catch_warnings(record=True) as warns:
            prob.solve(solver='CLARABEL',max_iter=200)
        E=np.pi**2/4*(1-np.cos(np.pi/(N+2)))*d2
        row=dict(case=case,moment_order=N,solver_status=prob.status,approximate_a_N=float(a.value),theoretical_kernel_error_bound=float(E),min_eig_m=float(np.linalg.eigvalsh(tm.value).min()),min_eig_w=float(np.linalg.eigvalsh(tw.value).min()),warnings=[str(x.message) for x in warns])
        if case=='single':
            A=(3**(2/3)-1)**1.5
            row.update(exact_boundary_formula_float=A,diagnostic_gap=A-float(a.value))
            assert float(a.value)<=A+2e-6 and A-float(a.value)<=E+2e-6
        rows.append(row);print(json.dumps(row),flush=True)
res=dict(at=datetime.now(timezone.utc).isoformat(),script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),exact_toeplitz_identities=exact,exact_atomic_quantile_cases=quantile_cases,kernel_diagnostics=kernel,rows=rows,scope='Exact finite algebra checks and floating SDP diagnostics only. Solver optima are not certified brackets; analytic error bounds are conditional on the proved hierarchy. No universal result or priority established by these tests.')
out.write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8')
print(str(out))
