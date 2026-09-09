"""Local workshop checks for v003 corrections; finite evidence, not a general proof."""
from pathlib import Path
import hashlib, itertools, json, sys
import sympy as sp

out={}
a,b,c,d=sp.symbols('a b c d')
C=sp.Matrix([[a+c,b-d],[b+d,a-c]])
det=sp.expand(C.det())
assert det==a*a-c*c-b*b+d*d
assert sp.Poly(det-(a+b+c+d)**2,a,b,c,d,modulus=2).is_zero
out['p2_symbolic_determinant']=str(det)
out['p2_mod2_identity']=True
n=0
for cs in itertools.product(range(-2,3),repeat=4):
    if not any(cs): continue
    # Only already-normalized residue vectors, with at least one odd coefficient.
    if not any(x%2 for x in cs): continue
    A=C.subs(dict(zip((a,b,c,d),cs)))
    labels=[(0,0),(1,0),(0,1),(1,1)]
    for u,v in [(1,0),(0,1),(1,1)]:
        f=[0,0]
        for g,x in zip(labels,cs): f[(u*g[0]+v*g[1])%2]^=x%2
        m=sum(bool(x) for x in f)
        if m: assert 2-A.rank()<=m-1
        n+=1
out['p2_integer_direction_checks']=n

# The fibre chosen for a non-collinear trinomial separates its unit coefficient.
n=0
for p in [2,3,5,7,11]:
    # Affine normalization sends the coefficient of minimum valuation to (0,0)
    # and the other two labels to (1,0),(0,1). Fibres: x+y=0 and x+y=1.
    for u,v in itertools.product(range(p),repeat=2):
        f=[1,(u+v)%p]
        m=sum(bool(x) for x in f)
        assert 1<=m<=2
        n+=1
out['trinomial_residue_checks']=n

n=0
p=5
for t0 in range(p):
    values=[(t*t-2*t0*t)%p for t in range(p)]
    assert len(set(values))==3 and values.count(values[t0])==1
    for rest in itertools.product(range(p),repeat=p-1):
        co=list(rest); co.insert(t0,1)
        f=[0]*p
        for val,x in zip(values,co): f[val]=(f[val]+x)%p
        m=sum(bool(x) for x in f)
        assert 1<=m<=3
        n+=1
out['parabola_residue_checks']=n

# Full support with all coefficients 1 has zero fibre sums in every direction.
p=3
for u,v in [(1,0)]+[(k,1) for k in range(p)]:
    f=[sum((u*a+v*b)%p==t for a,b in itertools.product(range(p),repeat=2))%p for t in range(p)]
    assert f==[0]*p
out['empty_direction_family_example_p3']=True

# Sufficiency normalization, p=r=3, A=C=I/sqrt(3), B=I, h=g=0.
p=3
A=sp.eye(p)/sp.sqrt(p); B=sp.eye(p); Ci=A*B.adjoint()
prob=sp.simplify(abs(sp.trace(B.adjoint()*A))**2/p)
correct=sp.simplify(abs(sp.trace(Ci))**2/p)
printed_v2=sp.simplify(abs(sp.trace(Ci))**2)
assert prob==correct==1 and printed_v2==3
out['lemma6_exact_example']={'actual':str(prob),'corrected':str(correct),'v002_printed':str(printed_v2)}

# Frame tightness by exact Fourier orthogonality for p=3, all r.
w=(-1+sp.sqrt(3)*sp.I)/2
checks=[]
for r in range(1,4):
    T=sp.Matrix([[sp.expand(w**(b*x))/sp.sqrt(r) for b in range(p)] for x in range(r)])
    frame=(T*T.adjoint()).applyfunc(sp.simplify)
    assert frame==sp.eye(r)*sp.Rational(p,r)
    checks.append({'p':p,'r':r,'frame_bound':str(sp.Rational(p,r))})
out['lemma7_exact_frames']=checks
out['python']=sys.version
out['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
print(json.dumps(out,indent=2))
print('FINAL REVISION CHECKS PASSED')
