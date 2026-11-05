from pathlib import Path
from itertools import permutations
import json
from graph_chains import run

def pivot_basis(vectors):
    piv={}
    for x in vectors:
        while x:
            i=x.bit_length()-1
            if i in piv:x^=piv[i]
            else:piv[i]=x;break
    return piv

def reduce(x,piv):
    for i in sorted(piv,reverse=True):
        if (x>>i)&1:x^=piv[i]
    return x

def check(n, graph_edges):
    bases,idx,ds,edges,restrict,summary=run(n, graph_edges)
    cob=[{}]
    for k in range(1,n+1):
        rows=[0]*len(bases[k-1])
        for j,col in enumerate(ds[k]):
            while col:
                low=col&-col;rows[low.bit_length()-1]^=1<<j;col^=low
        cob.append(pivot_basis(rows))
    def alpha(vm,em):
        order=[1<<v for v in range(n) if (vm>>v)&1];k=len(order);out=0
        for j,(bigV,bigE,blocks) in enumerate(bases[k]):
            if bigV&vm==vm and restrict(bigE,vm)==em and [b&vm for b in blocks]==order:out|=1<<j
        return out
    graphs=[(v,e,alpha(v,e)) for v,e,b in bases[1]]
    for vm,em,c in graphs:
        k=vm.bit_count()
        if k<n:assert all((col&c).bit_count()%2==0 for col in ds[k+1])
        # Pairing with the full permutation cycle is one for its own graph.
        z=sum(1<<idx[k][(vm,em,tuple(1<<v for v in order))] for order in permutations(v for v in range(n) if (vm>>v)&1))
        assert (z&c).bit_count()%2==1
    products_checked=0
    for va,ea,a in graphs:
        p=va.bit_count()
        for vb,eb,b in graphs:
            q=vb.bit_count();k=p+q
            if k>n:continue
            actual=0
            for j,(vm,em,blocks) in enumerate(bases[k]):
                leftV=0;rightV=0
                for block in blocks[:p]:leftV|=block
                for block in blocks[p:]:rightV|=block
                front=(leftV,restrict(em,leftV),blocks[:p])
                back=(rightV,restrict(em,rightV),blocks[p:])
                if ((a>>idx[p][front])&1) and ((b>>idx[q][back])&1):actual|=1<<j
            expected=0
            if not va&vb:
                for vc,ec,c in graphs:
                    if vc==va|vb and restrict(ec,va)==ea and restrict(ec,vb)==eb:expected^=c
            assert reduce(actual^expected,cob[k])==0
            products_checked+=1
    return {'vertices':n,'explicit_subgraph_cocycles_checked':len(graphs),'cup_products_equal_Hall_products_mod_coboundaries':products_checked,'additive_checks':summary,'all_cocycles_closed':True,'self_cycle_pairings_one':True}
examples=[(f'path{n}',n,[(i,i+1) for i in range(n-1)]) for n in range(1,5)]+[('triangle',3,[(0,1),(1,2),(0,2)]),('star4',4,[(0,1),(0,2),(0,3)]),('cycle4',4,[(0,1),(1,2),(2,3),(0,3)]),('complete4',4,[(i,j) for i in range(4) for j in range(i+1,4)]),('edgeless4',4,[])]
results=[]
for name,n,edges in examples:
    result=check(n,edges);result['graph']=name;result['edges']=edges;results.append(result)
print(json.dumps({'field':'F2','results':results,'scope':'Non-path exact validation of cocycles and Hall/cup multiplication, not an independent referee report'},indent=2))
