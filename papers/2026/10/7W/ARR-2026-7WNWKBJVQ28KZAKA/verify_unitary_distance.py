"""Independent identities for the unitary-distance/channel consequence.

This is finite numerical/exact algebra QA, not a test of undecidability.
All output is relative to this file, on D:.  Python -B avoids bytecode writes.
"""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parent
SEED = 2026101704
rng = np.random.default_rng(SEED)
errors = {}
counts = {}


def check(name, actual, expected=0, tol=5e-11):
    err = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
    errors[name] = max(errors.get(name, 0.0), err)
    counts[name] = counts.get(name, 0) + 1
    if not np.isfinite(err) or err > tol:
        raise AssertionError((name, err, tol))


def check_le(name, lhs, rhs, tol=5e-11):
    check(name, max(0.0, float(lhs-rhs)), tol=tol)


def unitary(n):
    z = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
    q, r = np.linalg.qr(z)
    return q @ np.diag(np.diag(r)/np.abs(np.diag(r)))


def basis(D, s):
    z = rng.normal(size=(D*D,s)) + 1j*rng.normal(size=(D*D,s))
    q, _ = np.linalg.qr(z)
    # Ordinary Euclidean orthonormal vec columns.  B_l=sqrt(D)*q_l.
    return q, [np.sqrt(D)*q[:,i].reshape(D,D) for i in range(s)]


def blocks(U, D, m):
    # rows=(i,a), columns=(j,b).  Return ((i,j),(a,b)).
    return U.reshape(D,m,D,m).transpose(0,2,1,3).reshape(D*D,m*m)


def from_blocks(V, D, m):
    return V.reshape(D,D,m,m).transpose(0,2,1,3).reshape(D*m,D*m)


def project(U, P, D, m):
    return from_blocks(P@blocks(U,D,m),D,m)


def norm2(X):
    return float(np.vdot(X,X).real/X.shape[0])


def choi(U, D, m):
    V=blocks(U,D,m)
    return V@V.conj().T/(D*m)


def channel(U, X, D, m):
    # Direct partial trace, independent of the Kraus/Choi routine.
    W=(U@np.kron(X,np.eye(m))@U.conj().T).reshape(D,m,D,m)
    return np.einsum('iaja->ij',W)/m


for D in [2,3,4]:
    for m in [1,2,3]:
        for trial in range(12):
            s=int(rng.integers(1,D*D))
            Q, B=basis(D,s)
            P=Q@Q.conj().T
            H=np.eye(D*D)-P
            U=unitary(D*m)
            X=project(U,P,D,m)
            d=norm2(U-X)
            rho=choi(U,D,m)
            check('projector_idempotent',P@P,P)
            check('projector_hermitian',H,H.conj().T)
            check('trace_choi',np.trace(rho),1)
            rr=rho.reshape(D,D,D,D)
            check('marginal_in',np.einsum('ijkj->ik',rr),np.eye(D)/D)
            check('marginal_out',np.einsum('ijil->jl',rr),np.eye(D)/D)
            check('choi_cost',np.trace(H@rho).real,d)
            check('reshuffled_cost',np.vdot(blocks(U,D,m),H@blocks(U,D,m)).real/(D*m),d)
            # Choi directly via channel applied to all E_jk.
            J=np.zeros((D*D,D*D),complex)
            for j in range(D):
                for k in range(D):
                    E=np.zeros((D,D)); E[j,k]=1
                    J+=np.kron(channel(U,E,D,m),E)
            check('choi_orientation',J/D,rho)
            check('projected_energy',norm2(X),1-d)
            W=X/np.sqrt(1-d)
            dist=norm2(W-U)
            check('normalization_identity',dist,2-2*np.sqrt(1-d))
            check_le('normalization_bound',dist,2*d)
            a,sv,bh=np.linalg.svd(W)
            polar=a@bh
            delta=norm2(W-polar)
            check('polar_identity',delta,2-2*np.mean(sv))
            check_le('polar_is_closer',delta,dist)
            check_le('gm_vs_schatten1',np.exp(2*np.mean(np.log(sv))),np.mean(sv)**2)
            # U -> U tensor I_k leaves normalized cost unchanged.
            k=2
            Urep=np.kron(U,np.eye(k))
            drep=norm2(Urep-project(Urep,P,D,m*k))
            check('amplified_witness_cost',drep,d)
            # Rebase S tensor M_k at dimension Dk, and ancillary dimension m.
            # Direct shuffle Urep from (i,a,c) to (i,c,a).
            Ush=Urep.reshape(D,m,k,D,m,k).transpose(0,2,1,3,5,4).reshape(D*k*m,D*k*m)
            extended=[]
            for Bj in B:
                for a0 in range(k):
                    for b0 in range(k):
                        E=np.zeros((k,k)); E[a0,b0]=np.sqrt(k)
                        extended.append(np.kron(Bj,E).reshape(-1)/np.sqrt(D*k))
            Qe=np.stack(extended,axis=1)
            Pe=Qe@Qe.conj().T
            ds=norm2(Ush-project(Ush,Pe,D*k,m))
            check('base_space_amplification_cost',ds,d)

# Symbolic rational certificate: antisymmetric subspace of M_3.
# This is a small exact check of the promises, not a hard reduction instance.
D=3
swap=sp.zeros(D*D)
for i in range(D):
    for j in range(D):
        swap[j*D+i,i*D+j]=1
P=(sp.eye(D*D)-swap)/2
H=sp.eye(D*D)-P
rho0=P/3
assert P*P==P and H*H==H and H.T==H
assert rho0.trace()==1 and H*rho0==sp.zeros(D*D)
assert rho0.rank()==P.rank()==3
assert sp.Matrix(D,D,lambda i,k:sum(rho0[i*D+j,k*D+j] for j in range(D)))==sp.eye(D)/D
assert sp.Matrix(D,D,lambda j,l:sum(rho0[i*D+j,i*D+l] for i in range(D)))==sp.eye(D)/D
assert all(x.is_Rational for x in P) and all(x.is_Rational for x in rho0)
# Rational channel T0(X)=(Tr(X)I-X^T)/2, normalized Choi exactly rho0.
J0=sp.zeros(D*D)
for j in range(D):
    for k in range(D):
        E=sp.zeros(D); E[j,k]=1
        T=(sp.trace(E)*sp.eye(D)-E.T)/2
        J0+=sp.kronecker_product(T,E)
assert J0/D==rho0

# All numerical coefficients in the soundness margin checked exactly.
gamma=Fraction(1,36288000000)
assert 1750*8000*gamma==Fraction(1,2592)
assert 1750*8000*gamma<Fraction(1,1296)
assert 9+6*sp.sqrt(2)<sp.Rational(35,2)
assert gamma/4+gamma/8<Fraction(5,8)*gamma<gamma-gamma/8
assert gamma/4+gamma/8+gamma/16==Fraction(7,16)*gamma
assert gamma-gamma/16==Fraction(15,16)*gamma
assert Fraction(7,16)*gamma<Fraction(3,4)*gamma<Fraction(15,16)*gamma

result={
    'status':'PASS',
    'seed':SEED,
    'random_cases':108,
    'checks':counts,
    'maximum_errors':errors,
    'maximum_identity_error':max(errors.values()),
    'exact_checks':{
        'rational_projector_and_choi_certificate':'PASS',
        'choi_orientation_and_marginals':'PASS',
        'support_equals_kernel':'PASS',
        'gamma':str(gamma),
        'soundness_upper_bound':str(1750*8000*gamma),
        'source_soundness_loss':str(Fraction(1,1296)),
        'decision_and_nonrecursive_thresholds':'PASS'},
    'limits':'Finite identity tests; no numerical proof of undecidability, global infima, or novelty.',
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
(ROOT/'unitary-distance-diagnostics.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
