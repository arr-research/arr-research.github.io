"""Version-2 author-supplied generic verification from the ORIGINAL basis matrices.
Adapted with attribution from the exact-algebra portion of GPT-6 Astra's v1 review.
This published adaptation is reproducibility material, not an independent v2 review.
No import or execution of the author's verify.py. Exact generic identities use a
multiquadratic algebra over Q(u), and numerical checks form a 36x36 channel.
"""
from pathlib import Path
import json, hashlib, platform, time
from datetime import datetime, timezone
import sympy as sp

ROOT=Path(__file__).resolve().parent
u=sp.Symbol('u')
K=sp.QQ.frac_field(u)
ku=K.from_sympy(u)
rad=[1-ku,ku,4*ku-1,K(3),K(-1)]
checks=[]
t0=time.perf_counter()
def check(ok,name):
    if not ok: raise AssertionError(name)
    checks.append(name); print('PASS:',name,flush=True)

class E:
    def __init__(self,value=0):
        if isinstance(value,E): self.d=value.d.copy()
        elif isinstance(value,dict): self.d={m:c for m,c in value.items() if c}
        else:
            c=K(value); self.d={0:c} if c else {}
    def __add__(self,other):
        other=E(other); d=self.d.copy()
        for m,c in other.d.items(): d[m]=d.get(m,K.zero)+c
        return E(d)
    __radd__=__add__
    def __neg__(self): return E({m:-c for m,c in self.d.items()})
    def __sub__(self,other): return self+-E(other)
    def __rsub__(self,other): return E(other)+-self
    def __mul__(self,other):
        other=E(other); d={}
        for m,c in self.d.items():
            for n,v in other.d.items():
                v=c*v
                common=m&n
                for bit,r in enumerate(rad):
                    if common&(1<<bit): v*=r
                key=m^n; d[key]=d.get(key,K.zero)+v
        return E(d)
    __rmul__=__mul__
    def __truediv__(self,other): return self*E(K.one/K(other))
    def __pow__(self,n):
        out=E(1)
        for _ in range(n): out=out*self
        return out
    def conj(self): return E({m:(-c if m&16 else c) for m,c in self.d.items()})
    def __eq__(self,other): return not (self-E(other)).d
    def rational(self):
        assert not any(m for m in self.d),self.d
        return sp.factor(K.to_sympy(self.d.get(0,K.zero)))

a,b,c,r,ii=[E({1<<i:K.one}) for i in range(5)]
x=a+ii*b
t=(1-ii*r)*(1-2*E(ku)+ii*a*c)*b/(2*ku)
w=(-1+ii*r)/2
F=[[E(1),E(1)],[E(1),E(-1)]]
H=[[E(1),w*t*t],[E(1),-w*t*t]]

def scale(s,M): return [[s*v for v in row] for row in M]
def block(parts):
    out=[]
    for rowparts in parts:
        for k in range(len(rowparts[0])):
            out.append([v for part in rowparts for v in part[k]])
    return out

def leftdiag(d,M): return [[d[j]*v for v in row] for j,row in enumerate(M)]
def overlap(M,N):
    return [[sum(M[k][j].conj()*N[k][l] for k in range(6)) for l in range(6)] for j in range(6)]

M1=block([[F,F,F],[F,scale(w,F),scale(w.conj(),F)],[H,scale(w.conj(),H),scale(w,H)]])
M2=block([[F,F,F],[H,scale(w,H),scale(w.conj(),H)],[H,scale(w.conj(),H),scale(w,H)]])
M3=block([[F,F,F],[H,scale(w,H),scale(w.conj(),H)],[F,scale(w.conj(),F),scale(w,F)]])
M1=leftdiag([x.conj(),x,ii*w.conj()*t*x*x,-ii*w.conj()*t*x.conj()*x.conj(),x.conj(),x],M1)
M3=leftdiag([x,x.conj(),w.conj()*x,w.conj()*x.conj(),-ii*t*x.conj()*x.conj(),ii*t*x*x],M3)
Ms=[M1,M2,M3]
check(x*x.conj()==1 and t*t.conj()==1 and w*w.conj()==1,'generic phase normalization from original parameter branch')
for j,M in enumerate(Ms,1):
    O=overlap(M,M)
    check(all(O[k][l]==(6 if k==l else 0) for k in range(6) for l in range(6)),f'generic original U{j} unitarity: all 36 entries')
    check(all(v*v.conj()==1 for row in M for v in row),f'generic original U{j} canonical unbiasedness: all 36 entries')

A=E(4)*(1-E(ku))**2/3
B=(1-2*E(ku))**2
C=(1-E(ku))*(4*E(ku)-1)/3
D=[[A,B],[B,A]]; Dt=[[B,A],[A,B]]; O=[[C,C],[C,C]]
expected=[block([[D,O,O],[O,D,O],[O,O,D]]),block([[O,D,O],[O,O,D],[D,O,O]]),block([[O,O,Dt],[Dt,O,O],[O,Dt,O]])]
generic_blocks={}
for (j,k),want in zip([(0,1),(1,2),(2,0)],expected):
    ov=overlap(Ms[j],Ms[k])
    p=[[v*v.conj()/36 for v in row] for row in ov]
    check(all(p[a][b]==want[a][b] for a in range(6) for b in range(6)),f'generic original P{j+1}{k+1} matches claimed block identity: all 36 entries')
    generic_blocks[f'P{j+1}{k+1}']=[[str(v.rational()) for v in row] for row in p]


report = {"status":"PASS", "generated_utc":datetime.now(timezone.utc).isoformat(),
    "python_version":platform.python_version(), "sympy_version":sp.__version__,
    "method":"Exact multiquadratic algebra over Q(u); identities from original basis matrices",
    "scope":"Fixed branch, 1/4 <= u <= 1; rational denominators are powers of nonzero u",
    "attribution":"Adapted from the exact generic-check portion of GPT-6 Astra's advisory v1 review",
    "checks":checks, "generic_probability_blocks":generic_blocks,
    "files_sha256":{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                    for name in ("verify_generic.py","paper.tex")},
    "seconds":round(time.perf_counter()-t0,3)}
(ROOT/'generic-verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(f'Completed {len(checks)} exact generic check groups.')
