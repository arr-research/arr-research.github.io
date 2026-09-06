"""Independent bounded audit; does not import the constructor verifier."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, product
from collections import Counter
import hashlib, json

HERE=Path(__file__).resolve().parent
checks=[]
def check(name,b,detail=None):
    if not b: raise AssertionError(name)
    checks.append(dict(name=name,status='PASS',detail=detail))

# Geometry is reconstructed by collinear triples, not by normal-vector equations.
points=list(product(range(3),repeat=2))
def collinear(T):
    a,b,c=[points[i] for i in T]
    return ((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))%3==0
lines=[frozenset(T) for T in combinations(range(9),3) if collinear(T)]
check('twelve collinear triples',len(lines)==12)
counts=Counter(); spectra_count=0
for mask in range(1,1<<12):
    chosen=[i for i in range(12) if mask>>i&1]
    support=set().union(*(lines[i] for i in chosen))
    if len(support)>=7:continue
    kind={1:'vertex',2:('parallel' if len(support)==6 else 'crossing'),3:'triangle'}.get(len(chosen))
    check('family classified '+str(mask),kind is not None)
    counts[kind]+=1
    contained=[i for i,L in enumerate(lines) if L<=support]
    check('no hidden line '+str(mask),contained==chosen)
    private=[]
    for i in chosen:
        private.append(lines[i]-set().union(*(lines[j] for j in chosen if j!=i)))
    check('private cells '+str(mask),all(private))
    weights=[F(j+1,sum(range(1,len(chosen)+1))) for j in range(len(chosen))]
    values=[sum((weights[j] for j,i in enumerate(chosen) if p in lines[i]),F(0)) for p in range(9)]
    nonzero=sorted(v for v in values if v)
    if kind=='vertex': expected=[F(1)]*3
    elif kind=='parallel':expected=sorted(weights*3)
    elif kind=='crossing':expected=sorted([F(1),weights[0],weights[0],weights[1],weights[1]])
    else:expected=sorted(weights+[1-w for w in weights])
    check('spectrum '+str(mask),nonzero==expected)
    spectra_count+=1
check('150 strata',dict(counts)==dict(vertex=12,parallel=12,crossing=54,triangle=72),dict(counts))

# Exact field Q(omega), represented independently by two rational coefficients.
Z=(F(0),F(0));O=(F(1),F(0));W=(F(0),F(1))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[0],-a[1])
def sub(a,b):return add(a,neg(b))
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def conj(a):return(a[0]-a[1],-a[1])
def inv(a):
    norm=a[0]*a[0]-a[0]*a[1]+a[1]*a[1]
    if not norm:raise ZeroDivisionError()
    c=conj(a);return(c[0]/norm,c[1]/norm)
def scale(a,r):return(a[0]*r,a[1]*r)
def wp(n):return[O,W,neg(add(O,W))][n%3]
def mat(n):return[[Z for _ in range(n)] for _ in range(n)]
def eye(n):
    A=mat(n)
    for i in range(n):A[i][i]=O
    return A
def mm(A,B):
    R=mat(len(A))
    for i,row in enumerate(A):
        for k,a in enumerate(row):
            if a==Z:continue
            for j,b in enumerate(B[k]):
                if b!=Z:R[i][j]=add(R[i][j],mul(a,b))
    return R
def ms(A,B):return[[sub(a,b) for a,b in zip(ar,br)] for ar,br in zip(A,B)]
def adj(A):return[[conj(A[j][i]) for j in range(len(A))] for i in range(len(A))]
def rank(A):
    A=[list(row) for row in A];p=0
    for col in range(len(A[0])):
        found=next((i for i in range(p,len(A)) if A[i][col]!=Z),None)
        if found is None:continue
        A[p],A[found]=A[found],A[p];f=inv(A[p][col]);A[p]=[mul(f,a) for a in A[p]]
        for i in range(len(A)):
            if i==p or A[i][col]==Z:continue
            f=A[i][col];A[i]=[sub(a,mul(f,b)) for a,b in zip(A[i],A[p])]
        p+=1
    return p

for dimension in [9,27]:
    I=eye(dimension);U=mat(dimension);V=mat(dimension)
    for j in range(dimension):
        U[(j+dimension//3)%dimension][j]=O;V[j][j]=wp(j)
    check('commuting cyclic representation d='+str(dimension),mm(U,V)==mm(V,U))
    C=mm(ms(I,U),ms(I,V));CC=mm(C,adj(C))
    check('four-term exact rank d='+str(dimension),rank(C)==4*dimension//9)
    tr=Z
    for i in range(dimension):tr=add(tr,CC[i][i])
    check('four-term trace d='+str(dimension),tr==(F(4*dimension),F(0)))
    check('flat square spectrum d='+str(dimension),mm(CC,CC)==[[scale(a,9) for a in row] for row in CC])

# A genuine d=9, rank-three decoding fixture. A0 has columns e_0,e_3,e_6.
# Physical A=A0/sqrt(3), C=P/sqrt(3); B=A0. The square-root cancels
# from the POVM normalization, which is checked exactly below.
vectors=[]
for a,b in product(range(9),repeat=2):
    vec={3*((3*l+a)%9)+l:wp(b*l) for l in range(3)}
    vectors.append(((a,b),vec))
twirl=[[Z for _ in range(27)] for _ in range(27)]
for label,vec in vectors:
    for i,x in vec.items():
        for j,y in vec.items():twirl[i][j]=add(twirl[i][j],scale(mul(x,conj(y)),F(1,9)))
check('POVM 1/d twirl normalization',twirl==eye(27))
label_sizes=[]
for (a,b),vec in vectors:
    support=[]
    for (aa,bb),other in vectors:
        amp=Z
        for i,x in vec.items():amp=add(amp,mul(conj(x),other.get(i,Z)))
        if amp!=Z:support.append((aa,bb))
    expected=[(a,bb) for bb in range(9) if (bb-b)%3==0]
    check('outcome list '+str((a,b)),support==expected)
    label_sizes.append(len(support))
check('all exact three-label lists',set(label_sizes)=={3})

# Independent low-dimensional multiplicity arithmetic by direct subgroup closure.
def subgroup(gens,n):
    H={(0,0)};todo=[(0,0)]
    while todo:
        a=todo.pop()
        for g in gens:
            b=((a[0]+g[0])%n,(a[1]+g[1])%n)
            if b not in H:H.add(b);todo.append(b)
    return H
import math
noncommuting=0
labels=[a for a in product(range(9),repeat=2) if a!=(0,0)]
for u,v in product(labels,repeat=2):
    if u==v:continue
    delta=(u[0]*v[1]-u[1]*v[0])%9
    if not delta:continue
    q=9//math.gcd(9,delta);R=subgroup([tuple(q*x%9 for x in u),tuple(q*x%9 for x in v)],9)
    check('central dimension '+str((u,v)),len(R)==9//q)
    noncommuting+=1

report={'status':'PASS','checks':len(checks),'geometry_subsets':4095,'low_strata':dict(counts),'exact_matrix_dimensions':[9,27],'POVM_dimension':27,'POVM_outcomes':81,'central_noncommuting_pairs':noncommuting,
        'source_sha256':hashlib.sha256((HERE/'ternary_low_rank.md').read_bytes()).hexdigest(),
        'constructor_verifier_sha256':hashlib.sha256((HERE/'ternary_verify.py').read_bytes()).hexdigest(),
        'constructor_certificate_sha256':hashlib.sha256((HERE/'ternary_certificate.json').read_bytes()).hexdigest(),
        'review_verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Independent finite geometry, exact four-term matrices, an actual low-rank POVM normalization and central arithmetic. No formal or external-referee claim.',
        'checks_detail':checks}
(HERE/'independent_ternary_review.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='checks_detail'},indent=2))
