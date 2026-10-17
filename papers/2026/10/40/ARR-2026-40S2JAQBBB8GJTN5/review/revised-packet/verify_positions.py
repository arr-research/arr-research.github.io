"""Finite diagnostics for positional normalization; no proof of source hardness.

Uses nonuniform rational distributions and Bob queries shared across answer
positions. Authored after the final referee requested these extra diagnostics.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
rng=np.random.default_rng(202610171202)
stats={'seed':202610171202,'tolerance':2e-12,'formal_proof':False}
def hs2(a): return float(np.vdot(a,a).real/a.shape[0])
def unitary(n):
    q,r=np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))
    return q@np.diag(np.diag(r)/np.abs(np.diag(r)))
def inv(n):
    q=unitary(n)
    return (q*rng.choice([-1.,1.],n))@q.conj().T
def parity(n,sigma):
    q=unitary(n)
    a,b=rng.choice([-1.,1.],size=(2,n))
    return [(q*v)@q.conj().T for v in (a,b,sigma*a*b)]

# An exhaustive scalar fixture: all three answer positions query the same y.
weights=[F(1,2),F(1,3),F(1,6)]
assert sum(weights)==1
count=0
for sigma in (-1,1):
    for pa,pb in product((-1,1),repeat=2):
        p=(pa,pb,sigma*pa*pb)
        for u in product((-1,1),repeat=3):
            for v in (-1,1):
                for eq in product((-1,1),repeat=3):
                    epar=sum(F((p[i]-u[i])**2,12) for i in range(3))
                    eeq=sum(weights[i]*F((eq[i]-u[i])**2+(eq[i]-v)**2,8) for i in range(3))
                    decoded=sum(weights[i]*F((p[i]-v)**2,4) for i in range(3))
                    enew=(epar+eeq)/2
                    assert decoded<=6*epar+8*eeq<=16*enew<=18*enew
                    old=sum(weights[i]*F((p[i]-v)**2,4) for i in range(3))
                    lifted=sum(weights[i]*F((p[i]-v)**2,16) for i in range(3))
                    assert lifted==old/4
                    count+=1
assert count==1024
stats['exhaustive_scalar_cases']=count
stats['scalar_probabilities']=[str(w) for w in weights]

# Two Alice questions, two Bob questions, all three checked positions.
triples=list(product(range(2),range(2),range(3)))
numerators=[1,3,2,4,5,1,2,1,4,1,2,6]
den=sum(numerators)
pi={t:F(w,den) for t,w in zip(triples,numerators)}
assert sum(pi.values())==1
pix={x:sum(w for (xx,y,i),w in pi.items() if xx==x) for x in range(2)}
# Exact integer duplication preserves all global variable identifiers.
rows=[]
for x in range(2):
    rows.append((tuple(('u',x,i) for i in range(3)),pix[x]/2))
for (x,y,i),w in pi.items():
    rows.append(((('u',x,i),('v',y)),w/2))
assert sum(w for _,w in rows)==1
expanded=[]
for variables,w in rows:
    assert len(set(variables))==len(variables)
    mult=w*(2*den)
    assert mult.denominator==1
    expanded.extend([variables]*mult.numerator)
assert len(expanded)==2*den
for variables,w in rows:
    assert F(expanded.count(variables),len(expanded))==w
assert sum(('v',0) in row for row in expanded)>1
stats['rational_row_duplication']={'rows':len(rows),'expanded_rows':len(expanded),'status':'PASS'}

max_sound_ratio=0.
for case in range(120):
    n=1+case%6
    p={x:parity(n,1 if x==0 else -1) for x in range(2)}
    u={(x,i):inv(n) for x in range(2) for i in range(3)}
    v={y:inv(n) for y in range(2)}
    eq={t:inv(n) for t in triples}
    epar=sum(float(pix[x])/12*sum(hs2(p[x][i]-u[x,i]) for i in range(3)) for x in range(2))
    eeq=sum(float(w)/8*(hs2(eq[x,y,i]-u[x,i])+hs2(eq[x,y,i]-v[y])) for (x,y,i),w in pi.items())
    decoded=sum(float(w)/4*hs2(p[x][i]-v[y]) for (x,y,i),w in pi.items())
    enew=(epar+eeq)/2
    assert decoded<=6*epar+8*eeq+2e-12
    assert 6*epar+8*eeq<=16*enew+2e-12
    assert decoded<=18*enew+2e-12
    old=decoded
    lifted=sum(float(w)/16*hs2(p[x][i]-v[y]) for (x,y,i),w in pi.items())
    assert abs(lifted-old/4)<2e-12
    if enew: max_sound_ratio=max(max_sound_ratio,decoded/(18*enew))
stats.update(matrix_cases=120,max_sound_ratio=max_sound_ratio,status='PASS')
(ROOT/'position-diagnostics.json').write_text(json.dumps(stats,indent=2)+'\n',encoding='utf-8')
print(json.dumps(stats,indent=2))
