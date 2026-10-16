"""Reproducible checks for the capacity-bridge manuscript; not a proof."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import math
import sys
import numpy as np
import sympy as sp

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source',type=Path,required=True)
parser.add_argument('--out',type=Path,required=True)
args=parser.parse_args()
OUT=args.out.resolve(); SOURCE=args.source.resolve()
OUT.mkdir(parents=True,exist_ok=True)
rng = np.random.default_rng(20261016)

def energy(ys):
    return sum(np.vdot(y, y).real / len(y) for y in ys)

def pencil(aa, ys):
    return sum(np.kron(a, y) for a, y in zip(aa, ys))

def objective(h, total_energy=1.):
    return float(np.exp(2 * np.linalg.slogdet(h)[1] / len(h)) / total_energy)

def cn(shape):
    return (rng.normal(size=shape) + 1j*rng.normal(size=shape))/np.sqrt(2)

# Rational example: all equalities are exact. A zero pencil is checked separately.
I = sp.I
aa = [sp.eye(2), sp.Matrix([[0,1],[1,0]]), sp.Matrix([[0,-I],[I,0]])]
ys = [sp.Matrix([[1,I],[0,2]]), sp.Matrix([[0,2],[1,I]]),
      sp.Matrix([[I,0],[1,1]])]
ep = sp.Rational(2,5)
bb = [1,0,0]
zz = [sp.BlockMatrix([[sp.zeros(2), y],[y.H,sp.zeros(2)]]).as_explicit()
      + I*ep*b*sp.eye(4) for y,b in zip(ys,bb)]
hh = sum((sp.kronecker_product(a,y) for a,y in zip(aa,ys)), sp.zeros(4))
hhz = sum((sp.kronecker_product(a,z) for a,z in zip(aa,zz)),sp.zeros(8))
ee = sum(sp.trace(y*y.H)/2 for y in ys)
eez = sum(sp.trace(z*z.H)/4 for z in zz)
rhs = (hh.H*hh+ep**2*sp.eye(4)).det()
detz = sp.simplify(hhz.det())
assert sp.simplify(eez-ee-ep**2)==0
assert sp.simplify(detz*sp.conjugate(detz)-rhs**2)==0
assert sp.simplify((I*ep*sp.eye(8)).det()*sp.conjugate((I*ep*sp.eye(8)).det())-(ep**2*sp.eye(4)).det()**2)==0
exact = dict(energy=str(ee), shifted_energy=str(eez),
             regularized_determinant=str(rhs), determinant=str(detz), passed=True)

# Identity and upper bound with complex covariance. Negative controls deliberately
# omit the shift cost or break Hermiticity; they must fail the corresponding identity.
errors = dict(energy=0., determinant=0., congruence=0., jensen_violation=0.,
              direct_hermitian=0., normality=0., covariance_adjoint=0.)
cases = 0
negative_controls = dict(energy_cost_detected=False, nonhermitian_detected=False)
for d in [1,2,3,4]:
    for n in [1,2,4,8]:
        for trial in range(3):
            aa = [np.eye(d)]
            for _ in range(3):
                w=cn((d,d)); aa.append((w+w.conj().T)/2)
            ys = [cn((n,n))/np.sqrt(n) for _ in aa]
            ep = [0.03,0.2,0.7][trial]
            bb = [1.,0.,0.,0.]
            zz = [np.block([[np.zeros((n,n)),y],[y.conj().T,np.zeros((n,n))]])
                  +1j*ep*b*np.eye(2*n) for y,b in zip(ys,bb)]
            h=pencil(aa,ys); hz=pencil(aa,zz)
            ee=energy(ys); eez=energy(zz)
            reg=np.linalg.slogdet(h.conj().T@h+ep**2*np.eye(d*n))[1]/(d*n)
            predicted=np.exp(reg)/(ee+ep**2)
            actual=objective(hz,eez)
            errors['energy']=max(errors['energy'],abs(eez-ee-ep**2))
            errors['determinant']=max(errors['determinant'],abs(actual-predicted)/max(1.,abs(predicted)))
            yh=[(y+y.conj().T)/np.sqrt(2) for y in ys]
            eh=energy(yh)
            wh=[(y+1j*ep*b*np.eye(n))/np.sqrt(eh+ep**2) for y,b in zip(yh,bb)]
            hh=pencil(aa,yh)
            direct=np.exp(np.linalg.slogdet(hh@hh+ep**2*np.eye(d*n))[1]/(d*n))/(eh+ep**2)
            errors['direct_hermitian']=max(errors['direct_hermitian'],abs(objective(pencil(aa,wh))-direct)/max(1.,abs(direct)),abs(energy(wh)-1))
            errors['normality']=max(errors['normality'],max(np.linalg.norm(w@w.conj().T-w.conj().T@w) for w in wh))
            l=cn((4,4)); qc=l@l.conj().T; qc/=np.trace(qc)
            superq=sum(qc[i,j]*np.kron(b.T,a) for i,a in enumerate(aa) for j,b in enumerate(aa))
            superbar=sum(qc[i,j].conjugate()*np.kron(b.T,a) for i,a in enumerate(aa) for j,b in enumerate(aa))
            errors['covariance_adjoint']=max(errors['covariance_adjoint'],np.linalg.norm(superq.conj().T-superbar))
            negative_controls['energy_cost_detected'] |= abs(np.exp(reg)/ee-actual)>1e-6
            # Positive congruence: A_original = T A_identity T, D=T^2.
            t=np.diag(np.linspace(0.6,1.8,d))
            original=[t@a@t for a in aa]
            ratio=np.linalg.det(t)**(4/d)
            scaled=objective(pencil(original,zz),eez)
            errors['congruence']=max(errors['congruence'],abs(scaled-ratio*actual)/max(1.,abs(scaled)))
            # Jensen upper bound at an arbitrary determinant-one X, arbitrary tuple.
            nonherm=[cn((d,d)) for _ in aa]
            yn=[y/np.sqrt(ee) for y in ys]
            q=np.array([[np.trace(y@z.conj().T)/n for z in yn] for y in yn])
            v=cn((d,d)); x=v@v.conj().T+np.eye(d)
            x=x/np.exp(np.linalg.slogdet(x)[1]/d)
            phi=sum(q[i,j]*a@x@b.conj().T for i,a in enumerate(nonherm) for j,b in enumerate(nonherm))
            upper=np.exp(np.linalg.slogdet(phi)[1]/d)
            val=objective(pencil(nonherm,yn))
            errors['jensen_violation']=max(errors['jensen_violation'],val-upper)
            if d>1:
                nh=pencil(nonherm,ys); nhz=pencil(nonherm,zz)
                wrong=np.exp(np.linalg.slogdet(nh.conj().T@nh+ep**2*np.eye(d*n))[1]/(d*n))/(ee+ep**2)
                negative_controls['nonhermitian_detected'] |= abs(objective(nhz,eez)-wrong)>1e-4
            cases+=1

assert max(errors.values()) < 1e-9, errors
assert all(negative_controls.values()), negative_controls

# Illustrative scalar semicircular approximation. These finite samples need not be
# monotone or lie on one side of the limiting curve.
scalar=[]
for n in [16,32,64,128]:
    g=cn((n,n)); y=(g+g.conj().T)/np.sqrt(2*n)
    e=energy([y])
    vals=[]
    for ep in [0.1,0.03,0.01]:
        val=np.exp(np.linalg.slogdet(y.conj().T@y+ep**2*np.eye(n))[1]/n)/(e+ep**2)
        vals.append(dict(epsilon=ep,value=float(val)))
    scalar.append(dict(N=n,values=vals))

result=dict(seed=20261016, checked_at=datetime.now(timezone.utc).isoformat(),
    versions=dict(python=sys.version,numpy=np.__version__,sympy=sp.__version__),
    source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    exact=exact,numeric_cases=cases,max_errors={k:float(v) for k,v in errors.items()},negative_controls={k:bool(v) for k,v in negative_controls.items()},
    scalar_illustration=scalar,scalar_unregularized_limit=math.exp(-1),
    conclusion='All finite identities and normalization checks passed. These checks do not prove the asymptotic theorem or novelty.')
(OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
