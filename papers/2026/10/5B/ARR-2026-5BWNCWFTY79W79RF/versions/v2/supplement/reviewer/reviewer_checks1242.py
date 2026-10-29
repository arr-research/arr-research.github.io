from pathlib import Path
import hashlib, json, sys, urllib.request
import sympy as s

HERE = Path(__file__).resolve().parent
INPUT = HERE.parent / 'input'
I = s.eye(2)
E = lambda i,j: I[:,i]*I[:,j].T
R = [E(1,0), E(1,1)]
Q = [s.diag(1,s.Rational(1,2)), s.sqrt(3)*E(0,1)/2]
V = [E(1,0), E(1,1)]
C = [E(0,1), E(1,1)]
M = [E(i,j) for i in range(2) for j in range(2)]
vec = lambda a: a.reshape(4,1) # output-first: row-major, unlike legacy controls

def span_basis(vs):
    return [v.reshape(2,2) for v in s.Matrix.hstack(*(vec(a) for a in vs)).columnspace()]

def product(a,b):
    return span_basis([x*y for x in a for y in b])

def same(a,b):
    aa, bb = span_basis(a), span_basis(b)
    return len(aa)==len(bb)==len(span_basis(aa+bb))

assert sum((a.H*a for a in R),s.zeros(2)) == I
assert sum((a.H*a for a in Q),s.zeros(2)) == I
assert same(product(Q,V),M)
assert same(product(V,M),V)
assert same(product(V,Q),V)
Qstar=[a.H for a in Q]
assert same(product(C,Qstar),M)
assert same(product(Qstar,M),M)
assert same(product(Qstar,C),C)
assert same(product(C,C),C)
assert same(product(C,M),M)
rows=[]
for phase in range(2):
    forward=[I]
    reverse=[I]
    for n in range(1,13):
        forward=product([R,Q][(phase+n-1)%2],forward)
        reverse=product([a.H for a in [R,Q][(phase-n)%2]],reverse)
        expected_forward=2 if n==1 else (4 if (phase==0 and n%2==0) or (phase==1 and n%2==1) else 2)
        expected_reverse=4 if phase==0 and n>=2 else 2
        assert len(forward)==expected_forward
        assert len(reverse)==expected_reverse
        rows.append({'phase':phase,'n':n,'forward_rank':len(forward),'reversed_rank':len(reverse)})

# Directly test the published output-first Choi convention and CP composition.
def ch(ks,a):
    return sum((k*a*k.H for k in ks),s.zeros(2))
def choi_from_map(ks):
    return sum((s.kronecker_product(ch(ks,E(i,j)),E(i,j)) for i in range(2) for j in range(2)),s.zeros(4))
for ks in (R,Q,[a*b for a in Q for b in R]):
    assert choi_from_map(ks)==sum((vec(k)*vec(k).H for k in ks),s.zeros(4))
Z=s.diag(s.Rational(2,3),s.Rational(1,3))
replacement=[s.sqrt(Z[i,i])*E(i,j) for i in range(2) for j in range(2)]
assert choi_from_map(replacement)==s.kronecker_product(Z,I)

remote=[]
prefix='https://raw.githubusercontent.com/lluiseriksson/physmath-knowledge-tree/de24e4e461fb35bda8336cf248fe85bb5c3e2f61/integrations/research-radar/evidence/2026-10-29-temporal-audit-context/'
for name in ['check_bistochastic1221.py','check_three_phase1222.py','check_reverse1223.py']:
    item={'name':name,'url':prefix+name}
    try:
        data=urllib.request.urlopen(prefix+name,timeout=25).read()
        item.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),matches_input=data==(INPUT/name).read_bytes())
    except Exception as exc:
        item['fetch_error']=str(exc)
    remote.append(item)
out={'python':sys.version,'sympy':s.__version__,'scope':'Additional reviewer checks in this one full assessment; finite controls plus independently checked symbolic identities, not another assessment','reset_rows':rows,'reset_subspace_identities':'all passed','output_first_choi_checks':'all passed','public_legacy_script_byte_checks':remote}
(HERE/'reviewer_checks1242.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'reset_rows':len(rows),'identities':'pass','output_first_choi':'pass','remote':remote},indent=2))
