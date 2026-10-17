# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from fractions import Fraction as F
import os,itertools,json,math,time
import sympy as sp
import networkx as nx
from ground_profiles import all_independent,bounded_compositions,kernel
from exact_inertia import inertia
R=Path(os.environ.get("AIRR_OUTPUT_DIR",str(Path(__file__).parent/"_run")))
R.mkdir(parents=True,exist_ok=True)

def full_restriction(G,s,ell,aa,occupations):
    H=[[F(0) for _ in range(4)] for _ in range(4)];mu=1-ell*ell
    for a,w,e in occupations:
        b=[s-x for x in a];rr=[a[v]+sum(a[u] for u in G[v]) for v in G]
        U=[[(1-ell*aa[i])**rr[v] for v in G] for i in range(4)]
        vv=[sum(b[v]*U[i][v] for v in G) for i in range(4)];weight=w*mu**e
        for i in range(4):
            for j in range(i,4):
                pair=vv[i]*vv[j]-sum(b[v]*U[i][v]*U[j][v] for v in G)
                edge=sum(b[v]*(b[v]-1)*U[i][v]*U[j][v] for v in G)
                edge+=sum(b[u]*b[v]*(U[i][u]*U[j][v]+U[i][v]*U[j][u]) for u,v in G.edges())
                H[i][j]+=weight*(pair-aa[i]*aa[j]*edge)
    for i in range(4):
        for j in range(i):H[i][j]=H[j][i]
    return sp.Matrix(H)

if __name__=='__main__':
    mixed=nx.Graph();mixed.add_nodes_from(range(5));mixed.add_edges_from([(3,0),(3,1),(4,0),(4,1),(4,2),(3,4)])
    examples=[('path3',nx.path_graph(3)),('cycle6',nx.cycle_graph(6)),('diamond',nx.complete_graph(4)),('mixed_unique',mixed)]
    examples[2][1].remove_edge(0,1)
    rows=[];start=time.time()
    for name,G in examples:
        s=2;alpha,iss=all_independent(G);h=alpha*s-1
        patterns=set(tuple((s-(u==v)) if u in I else 0 for u in G) for I in iss for v in I)
        L=sp.Matrix(kernel(G,s,patterns));occupations=[]
        for a in bounded_compositions(len(G),s,h):
            occupations.append((a,math.prod(math.comb(s,x) for x in a),sum(x*(x-1)//2 for x in a)+sum(a[u]*a[v] for u,v in G.edges())))
        for dpow in range(3,21):
            delta=F(1,2**dpow);aa=[-1+delta*z for z in [1,2,3,4]]
            U=sp.Matrix([[(delta*z)**r for r in range(L.rows)] for z in [1,2,3,4]])
            ii,_=inertia(U*L*U.T)
            if ii[0]>=2:break
        else:raise AssertionError('Ground search bound exhausted')
        for epow in range(dpow+2,81):
            ell=-1+F(1,2**epow);H=full_restriction(G,s,ell,aa,occupations);ii,blocks=inertia(H)
            if ii[0]>=2:break
        else:raise AssertionError('Positive target search bound exhausted')
        nodes=[ell,F(0)]+aa
        assert len(set(nodes))==6 and all(-1<x<1 for x in nodes)
        assert all(1-x*y>0 for x in nodes for y in nodes)
        row=dict(name=name,base_vertices=len(G),base_edges=list(map(list,G.edges())),s=s,h=h,delta=str(delta),ell=str(ell),nodes=list(map(str,nodes)),ground_inertia=inertia(U*L*U.T)[0],positive_hessian_inertia=ii,positive_hessian_matrix=[[str(v) for v in rr] for rr in H.tolist()],congruence=blocks,derivative_factor='h! * (n-h-2)!',occupations=len(occupations))
        rows.append(row);print(json.dumps({k:row[k] for k in ['name','delta','ell','positive_hessian_inertia','occupations']}),flush=True)
    (R/'six-spin-positive-examples.json').write_text(json.dumps(dict(status='PASS_EXACT_POSITIVE_SIX_SPIN_WITNESSES',rows=rows,seconds=time.time()-start,limitation='Four explicit examples, not a substitute for the general proof; search termination bounds in this script are only practical caps.'),indent=2)+'\n')
