"""Extra finite checks by this referee. Not a formal proof or hardness experiment.

The compact compiler is reused from the supplied verifier; the direct quadratic
rounding check below is separate from its determinant-based reverse test.
"""
from pathlib import Path
from fractions import Fraction as F
import importlib.util
import json
import math
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('compiler', ROOT/'rerun/verify_weighted_gap.py')
cmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cmod)
rng = np.random.default_rng(6171043)

def hs2(x):
    return float(np.vdot(x,x).real/x.shape[0])

def polar(x):
    u,s,vh=np.linalg.svd(x)
    return u@vh

def unitary(m):
    q,r=np.linalg.qr(rng.normal(size=(m,m))+1j*rng.normal(size=(m,m)))
    return q@np.diag(np.diag(r)/np.abs(np.diag(r)))

def block(c,g,values):
    u,v,w,sgn=g
    return np.block([[.6*values[u],.8*sgn*values[w]],
                     [.8*values['z'],-.6*values[v]]])

records=[]
for trial in range(72):
    m=1+trial%4
    contexts=[([0,1,2],1),([0,1],1),([2],1)]
    if trial%2:
        contexts.append(([0,1,2],-1))
    c=cmod.compile_contexts(contexts)
    # Generic, nearly exact, and singular starting labels, including a singular reference.
    if trial%3==0:
        values={l:unitary(m)+.03*(rng.normal(size=(m,m))+1j*rng.normal(size=(m,m))) for l in c['labels']}
    elif trial%3==1:
        values={l:np.eye(m)+.001*(rng.normal(size=(m,m))+1j*rng.normal(size=(m,m))) for l in c['labels']}
    else:
        values={l:np.diag(rng.choice([0.,.4,1.2],m)).astype(complex) for l in c['labels']}
        values['z']=np.zeros((m,m),complex)
    energy=sum(c['w'][l]**2*hs2(z) for l,z in values.items())/c['D']
    assert energy>0
    values={l:z/math.sqrt(energy) for l,z in values.items()}
    v={l:polar(z) for l,z in values.items()}
    delta2=sum(n*hs2(values[l]-v[l]) for l,n in c['singles'].items())
    delta2+=50*sum(hs2(g-polar(g)) for g in (block(c,g,values) for g in c['gates']))
    delta2/=c['D']
    gauge=v['z'].conj().T
    decoded={l:z@gauge for l,z in v.items()}
    xi=cmod.word_error(c,decoded)
    bound=(9+6*math.sqrt(2))*delta2/c['rho']
    assert xi<=bound+1e-10,(trial,xi,bound)
    labelcost=sum(c['w'][l]**2*hs2(values[l]-v[l]) for l in values)/c['D']
    assert labelcost<=2*delta2+1e-11
    records.append(dict(trial=trial,m=m,singular_reference=trial%3==2,
                        delta_squared=delta2,relation_error=xi,upper_bound=bound))

gamma=F(1,36288000000)
alpha=sp.Rational(144,25)*(3+2*sp.sqrt(2))
assert sp.simplify(6*alpha/(50*sp.Rational(12,25)**2)-(9+6*sp.sqrt(2)))==0
assert F(17,50*2**40)<gamma/4
assert F(1750*8000)*gamma==F(1,2592)
assert F(1,2592)<F(1,1296)
assert gamma/4+gamma/8<5*gamma/8<gamma-gamma/8
result=dict(status='PASS',seed=6171043,cases=len(records),singular_reference_cases=24,
            maximum_relation_to_bound_ratio=max(r['relation_error']/r['upper_bound'] for r in records),
            symbolic_reverse_coefficient='9+6*sqrt(2)',exact_gap_checks='PASS',
            gamma=float(gamma),yes_upper_bound=float(F(17,50*2**40)),
            limitations=['Finite checks only.','Compiler reused from supplied code; not an independent compiler implementation.',
                         'No machine-to-game execution, global optimum certificate, or proof assistant.'],records=records)
(ROOT/'referee-checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
