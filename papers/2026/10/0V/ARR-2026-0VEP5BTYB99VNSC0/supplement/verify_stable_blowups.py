# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
import os,json,math,time
import networkx as nx
from ground_profiles import all_independent,bounded_compositions,kernel
R=Path(os.environ.get("AIRR_OUTPUT_DIR",str(Path(__file__).parent/"_run")))
R.mkdir(parents=True,exist_ok=True)

start=time.time();rows=[];tested=0
for atlas_id,G in enumerate(nx.graph_atlas_g()):
    if len(G)<3 or not nx.is_connected(G):continue
    alpha,indsets=all_independent(G)
    stable=all(sum(v in I for v in G[u])>=2 for I in indsets for u in G if u not in I)
    # Independent edge-deletion characterization check.
    deleted_stable=True
    for e in list(G.edges()):
        H=G.copy();H.remove_edge(*e)
        if all_independent(H)[0]!=alpha:deleted_stable=False;break
    assert stable==deleted_stable
    tested+=1
    if not stable:continue
    nd={}
    for I in indsets:
        for u in G:
            if u not in I:
                d=sum(v in I for v in G[u]);nd[d]=nd.get(d,0)+1
    d0=min(nd);assert d0>=2
    for s in [2,3]:
        h=alpha*s-1;emin=(alpha-1)*s*(s-1)//2+(s-1)*(s-2)//2
        expected=set()
        for I in indsets:
            for v in I:expected.add(tuple((s-(u==v)) if u in I else 0 for u in G))
        found=set();actual_min=10**9
        for a in bounded_compositions(len(G),s,h):
            e=sum(x*(x-1)//2 for x in a)+sum(a[u]*a[v] for u,v in G.edges())
            if e<actual_min:actual_min=e;found=set()
            if e==actual_min:found.add(a)
        assert actual_min==emin and found==expected,(atlas_id,s)
        M=kernel(G,s,found);A=[s-1,s,d0*s-1,d0*s]
        active=[i for i in range(len(M)) if any(M[i])]
        assert active[:4]==A
        assert all(M[i][j]==0 for i in A[:2] for j in A[:2])
        factor=s*s*nd[d0]
        assert [[M[i][j] for j in A[2:]] for i in A[:2]]==[[0,factor*alpha],[factor*d0,-factor*d0]]
        rows.append(dict(atlas_id=atlas_id,base_vertices=len(G),base_edges=list(map(list,G.edges())),alpha=alpha,maximum_independent_sets=len(indsets),s=s,h=h,minimum_edges=emin,minimum_patterns=len(found),first_four_profiles=A,N_d0=nd[d0],offdiagonal_block_determinant=str(-s**4*alpha*d0*nd[d0]**2)))
    if len(rows)%50==0:print(json.dumps(dict(cases=len(rows),last_atlas=atlas_id,seconds=time.time()-start)),flush=True)
out=dict(status='PASS_EXACT_CLASSIFICATION_AND_INITIAL_BLOCK',base_graphs_characterization_tested=tested,stable_bases=len(rows)//2,blowup_cases=len(rows),rows=rows,seconds=time.time()-start,limitation='Finite checks support but do not replace the general proof. No numerical score or priority claim.')
(R/'stable-blowup-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','base_graphs_characterization_tested','stable_bases','blowup_cases','seconds']}),flush=True)
