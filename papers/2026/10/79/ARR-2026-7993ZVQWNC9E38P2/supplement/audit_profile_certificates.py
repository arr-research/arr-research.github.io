"""Independent characteristic-polynomial audit of stored finite certificates.
Same author context, not an external model or human review.
"""
from pathlib import Path
import json,hashlib,sys,time
import sympy as sp
import networkx as nx
R=Path(__file__).parent
src=R/'profile-hierarchy-exact.json';data=json.loads(src.read_text())
atlas=nx.graph_atlas_g();expected={i for i,G in enumerate(atlas) if len(G)>=3 and nx.is_connected(G) and G.number_of_edges()!=len(G)*(len(G)-1)//2}
assert {r['atlas_index'] for r in data['rows']}==expected and len(data['rows'])==len(expected)

def variation(seq):
    signs=[1 if x>0 else -1 for x in seq if x]
    return sum(a!=b for a,b in zip(signs,signs[1:]))
checks=[];start=time.time()
for row in data['rows']:
    G=atlas[row['atlas_index']]
    assert row['edges']==[list(e) for e in G.edges()]
    B=sp.Matrix([[sp.Integer(x) for x in r] for r in row['integer_kernel']]);q=B.rows
    assert B==B.T
    coeff=B.charpoly().all_coeffs()
    z=0
    for c in reversed(coeff):
        if c:break
        z+=1
    plus=variation(coeff);minus=variation([c*(-1)**(q-i) for i,c in enumerate(coeff)])
    assert plus+minus+z==q
    assert [plus,minus,z]==row['inertia'] and plus>=2
    aa=list(map(sp.Rational,row['target_parameters']))
    assert len(aa)==q and len(set(aa))==q and all(-1<x<1 for x in aa)
    assert aa[0]==sp.Rational(row['ell']) and aa[1]==0
    checks.append(dict(atlas_index=row['atlas_index'],characteristic_coefficients=list(map(str,coeff)),exact_positive_roots=plus,exact_negative_roots=minus,zero_roots=z))
out=dict(status='PASS_EXACT_CHARACTERISTIC_POLYNOMIAL_AUDIT',source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),cases=len(checks),method='The characteristic polynomial of each real symmetric integer kernel has only real roots. Descartes upper bounds for positive and negative roots sum, with the exact zero multiplicity, to its degree. Thus both counts are exact. These counts agree with the separately computed rational congruence certificates.',all_atlas_cases_present=True,checks=checks,environment=dict(python=sys.version,sympy=sp.__version__,networkx=nx.__version__),limits='Author-side audit, not an independent referee or proof-assistant verification.')
(R/'profile-characteristic-audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(status=out['status'],cases=len(checks),seconds=round(time.time()-start,1))))