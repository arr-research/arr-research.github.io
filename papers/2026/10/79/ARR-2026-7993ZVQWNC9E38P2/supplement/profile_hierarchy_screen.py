from pathlib import Path
import itertools,json,math,time
import networkx as nx
import numpy as np
R=Path(__file__).parent

def profile_blocks(G,h):
    q=h+2
    NN=np.zeros((h*(h-1)//2+1,q,q),dtype=np.int64)
    CC=np.zeros_like(NN)
    for S0 in itertools.combinations(list(G),h):
        S=set(S0);rem=[v for v in G if v not in S]
        profiles={v:sum(G.has_edge(u,v) for u in S) for v in rem}
        nu=np.bincount(list(profiles.values()),minlength=q)
        e=G.subgraph(S).number_of_edges()
        NN[e]+=np.outer(nu,nu)-np.diag(nu)
        for u,v in G.edges():
            if u in profiles and v in profiles:
                a,b=profiles[u],profiles[v]
                for x,y,sg in [(a,b,1),(a+1,b,-1),(a,b+1,-1),(a+1,b+1,1)]:
                    CC[e,x,y]+=sg;CC[e,y,x]+=sg
    return NN,CC

rows=[];started=time.time()
for atlas_index,G in enumerate(nx.graph_atlas_g()):
    n=len(G)
    if n<3 or not nx.is_connected(G):continue
    complete=G.number_of_edges()==n*(n-1)//2
    found=None;min_second=0
    for h in range(1,n-1):
        NN,CC=profile_blocks(G,h)
        for t in [1.,.98,.75,.5,.25,.05,.005]:
            w=(1-t)**np.arange(len(NN))
            B=t*np.einsum('e,eij->ij',w,NN)-np.einsum('e,eij->ij',w,CC)
            ev=np.linalg.eigvalsh(B);scale=max(np.max(np.abs(ev)),1)
            ratio=float(ev[-2]/scale);min_second=max(min_second,ratio)
            if ratio>1e-9:
                found=dict(h=h,t=t,second_positive_ratio=ratio)
                break
        if found:break
    assert not(complete and found),(n,found)
    rows.append(dict(atlas_index=atlas_index,n=n,edges=list(G.edges()),complete=complete,detected=found,best_second_ratio=min_second))
    if len(rows)%100==0:print(json.dumps(dict(progress=len(rows),seconds=round(time.time()-started,1))),flush=True)
out=dict(status='EXPLORATORY_NUMERIC_ONLY',graphs=len(rows),detected=sum(bool(r['detected']) for r in rows),misses=[r for r in rows if not r['complete'] and not r['detected']],rows=rows,parameter='t=ell^2; kernel t*N-D*C*D^T in profile basis',limits='Numeric screening, not a proof of completeness or Lorentzianity; no independent review.')
(R/'profile-hierarchy-screen.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(status=out['status'],graphs=out['graphs'],detected=out['detected'],misses=len(out['misses']),seconds=round(time.time()-started,1))),flush=True)