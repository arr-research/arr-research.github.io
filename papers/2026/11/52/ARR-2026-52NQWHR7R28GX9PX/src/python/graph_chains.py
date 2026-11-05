"""Exact normalized chain complexes of finite labelled graph simplicial sets."""
from itertools import product
import json

def rank(columns):
    piv={}
    for c in columns:
        while c:
            p=c.bit_length()-1
            if p not in piv:piv[p]=c;break
            c^=piv[p]
    return len(piv)

def run(n, graph_edges):
    edges=list(graph_edges)
    def restrict(em,vm):return sum((1<<j) for j,(a,b) in enumerate(edges) if (em>>j)&1 and (vm>>a)&1 and (vm>>b)&1)
    bases=[[(0,0,())]]+[[] for _ in range(n)]
    hall=[0]*(n+1);hall[0]=1
    for vm in range(1,1<<n):
        verts=[i for i in range(n) if (vm>>i)&1]
        em_full=restrict((1<<len(edges))-1,vm)
        em=em_full
        while True:
            hall[len(verts)]+=1
            for k in range(1,len(verts)+1):
                for labels in product(range(k),repeat=len(verts)):
                    if set(labels)!=set(range(k)):continue
                    blocks=tuple(sum(1<<v for v,label in zip(verts,labels) if label==i) for i in range(k))
                    bases[k].append((vm,em,blocks))
            if em==0:break
            em=(em-1)&em_full
    indices=[{s:i for i,s in enumerate(b)} for b in bases]
    ds=[[] for _ in range(n+1)]
    for k in range(1,n+1):
        for vm,em,blocks in bases[k]:
            faces=[]
            if k==1:faces=[(0,0,()),(0,0,())]
            else:
                left=vm^blocks[0];right=vm^blocks[-1]
                faces=[(left,restrict(em,left),blocks[1:])]
                faces += [(vm,em,blocks[:i-1]+(blocks[i-1]|blocks[i],)+blocks[i+1:]) for i in range(1,k)]
                faces += [(right,restrict(em,right),blocks[:-1])]
            col=0
            for f in faces:col^=1<<indices[k-1][f]
            ds[k].append(col)
    for k in range(2,n+1):
        for col in ds[k]:
            val=0
            while col:
                low=col&-col;val^=ds[k-1][low.bit_length()-1];col^=low
            assert val==0
    ranks=[0]+[rank(ds[k]) for k in range(1,n+1)]+[0]
    betti=[len(bases[k])-ranks[k]-ranks[k+1] for k in range(n+1)]
    assert betti==hall
    summary = {'vertices':n,'normalized_chain_dimensions':[len(b) for b in bases],'boundary_ranks':ranks[1:-1],'mod2_betti':betti,'Hall_dimension_by_vertex_degree':hall,'boundary_squared_zero':True,'ring_isomorphism_checked':False}

    return bases, indices, ds, edges, restrict, summary
