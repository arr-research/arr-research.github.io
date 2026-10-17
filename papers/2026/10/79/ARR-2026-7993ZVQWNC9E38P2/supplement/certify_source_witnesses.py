"""Exact author-side certificates for a bounded graph census, not a general proof."""
from pathlib import Path
from collections import defaultdict
import itertools,json,math,hashlib
import sympy as sp
R=Path(__file__).parent
data=json.loads((R/'source-lorentzian-rank2-probe.json').read_text())
certs=[]
for row in data['results']:
    w=row['witness']
    if w is None:
        assert row['complete']
        continue
    H=[[int(v) for v in r] for r in w['target']]
    assert all(float(H[i][j])==w['target'][i][j] for i in range(3) for j in range(3))
    t=[H[i][i]//2 for i in range(3)]
    assert all(H[i][j]==t[i]+t[j] for i in range(3) for j in range(3))
    assert len(set(t))>1 and min(t)>=0
    # H=1*t^T+t*1^T has rank 2 and exactly one positive eigenvalue:
    # its quadratic form vanishes on 1^perp, and it has a negative
    # 2x2 principal determinant -(t_i-t_j)^2 and positive trace.
    beta=w['derivative'];wanted={}
    for i in range(3):
        for j in range(i,3):
            a=list(beta);a[i]+=1;a[j]+=1;wanted[tuple(a)]=math.prod(math.factorial(k) for k in a)
    coeff=defaultdict(int)
    for a in itertools.product(range(3),repeat=row['n']):
        expo=tuple(a.count(i) for i in range(3))
        if expo not in wanted:continue
        weight=math.prod(H[a[u]][a[v]] for u,v in row['edges'])
        coeff[expo]+=weight
    M=[]
    for i in range(3):
        vals=[]
        for j in range(3):
            a=list(beta);a[i]+=1;a[j]+=1;a=tuple(a)
            vals.append(coeff[a]*wanted[a])
        M.append(vals)
    mat=sp.Matrix(M);det=int(mat.det());trace=int(sp.trace(mat))
    assert det<0 and trace>0,(row['atlas_index'],det,trace)
    certs.append(dict(n=row['n'],edges=row['edges'],target=H,rank_two_parameters=t,derivative=beta,hessian=M,determinant=str(det),trace=str(trace),inertia=[2,1,0]))
out=dict(status='PASS_EXACT_BOUNDED_CENSUS',source_conjecture='Lee-Oh-Seo 2506.13659v2, Conjecture 7.1',source_scope='Connected finite simple graphs on 3 through 6 vertices in NetworkX graph_atlas_g',graphs=141,complete_graph_controls=4,noncomplete_graphs=137,certified_obstructions=len(certs),certificates=certs,proof_of_certificate='Each target equals 1*t^T+t*1^T for distinct nonnegative integer t, hence has exactly one positive eigenvalue. Exact derivative Hessians have negative determinant and positive trace, hence two positive eigenvalues. This violates the necessary Lorentzian Hessian condition.',limits=['Bounded census only; the conjecture for arbitrary order remains unproved.','This is an author-side check, not an Astra assessment or a formal proof assistant certificate.','No claim of novelty or publication readiness.'])
(R/'source-witness-certificates.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','graphs','complete_graph_controls','noncomplete_graphs','certified_obstructions']}))
