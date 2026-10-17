"""Exploratory finite tests of Lee--Oh--Seo Conjecture 7.1.

No general theorem or novelty claim. The known P3 witness is a control.
"""
from pathlib import Path
import itertools,math,json
import numpy as np
import networkx as nx
R=Path(__file__).parent
rng=np.random.default_rng(10717)

def compositions(n,q):
    if q==1:yield (n,);return
    for a in range(n+1):
        for z in compositions(n-a,q-1):yield (a,)+z

def setup(n,q):
    assignments=np.array(list(itertools.product(range(q),repeat=n)),dtype=int)
    exps=list(compositions(n,q));index={a:i for i,a in enumerate(exps)}
    bins=np.array([index[tuple(np.bincount(a,minlength=q))] for a in assignments])
    mats=[]
    for b in compositions(n-2,q):
        ids=np.zeros((q,q),dtype=int);fac=np.zeros((q,q))
        for i in range(q):
            for j in range(q):
                a=list(b);a[i]+=1;a[j]+=1;ids[i,j]=index[tuple(a)]
                fac[i,j]=math.prod(math.factorial(v) for v in a)
        mats.append((b,ids,fac))
    return assignments,bins,exps,mats

sources=[]
for g in nx.graph_atlas_g():
    n=len(g)
    if 3<=n<=6 and nx.is_connected(g):sources.append(g)
targets=[np.array([[0,0,1],[0,0,2],[1,2,0]],float)]
for k in range(0):
    v=rng.normal(size=(3,2));v/=np.linalg.norm(v,axis=1)[:,None]
    v*=rng.uniform(.4,1,size=(3,1))
    h=np.ones((3,3))-v@v.T
    if k%2==0:
        d=np.exp(rng.uniform(-1.5,1.5,size=3));h*=d[:,None]*d[None,:]
    targets.append(h)
targets=[np.add.outer(t,t) for t in [[0.,1.,2.],[1.,2.,3.],[1.,2.,10.],[0.,1.,10.]]]
cache={n:setup(n,3) for n in range(3,7)}
out=[];tests=0
for idx,g in enumerate(sources):
    n=len(g);a,bins,exps,mats=cache[n];found=None
    for hi,h in enumerate(targets):
        weights=np.ones(len(a))
        for u,v in g.edges():weights*=h[a[:,u],a[:,v]]
        coeff=np.bincount(bins,weights,minlength=len(exps))
        for beta,ids,fac in mats:
            M=coeff[ids]*fac;scale=max(np.linalg.norm(M,ord=2),1e-300);ev=np.linalg.eigvalsh(M/scale)
            tests+=1
            if ev[-2]>1e-8:
                found=dict(target_index=hi,target=h.tolist(),derivative=list(beta),normalized_eigenvalues=ev.tolist(),hessian=M.tolist());break
        if found:break
    out.append(dict(atlas_index=idx,n=n,edges=list(g.edges()),complete=g.number_of_edges()==n*(n-1)//2,regular=len(set(dict(g.degree()).values()))==1,witness=found))
    if idx%30==0:print(json.dumps(dict(processed=idx+1,found=sum(x['witness'] is not None for x in out))),flush=True)
result=dict(status='exploratory_not_proof',source='https://arxiv.org/html/2506.13659v2',models=len(targets),q=3,graphs=len(out),hessian_tests=tests,results=out,limitations=['Floating point witnesses need exact rational certification.','No witness does not establish the Lorentzian property.','Finite graph and model search does not settle the conjecture.','Author-context computation, not Astra review.'])
(R/'source-lorentzian-rank2-probe.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(graphs=len(out),witnesses=sum(x['witness'] is not None for x in out),unresolved_noncliques=sum(not x['complete'] and x['witness'] is None for x in out))),flush=True)
