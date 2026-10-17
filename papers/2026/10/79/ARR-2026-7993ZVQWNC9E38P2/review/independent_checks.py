"""Fresh referee implementation. No author helper or stored witness is imported.

Exact coefficient enumeration grows assignments one vertex at a time, multiplying
only newly completed edges. Kernel enumeration accumulates contributions from
explicit ordered pairs, independently of the degree-count implementation in the
supplement. The same mathematical formulas, SymPy and NetworkX are shared;
this is algorithmic checking, not statistical or human independence.
"""
from pathlib import Path
from collections import defaultdict, Counter
from functools import lru_cache
from itertools import combinations, product
from math import factorial, prod, comb, lcm
import json, time, sys
import networkx as nx
import sympy as sp

ROOT=Path(__file__).resolve().parent
RESULT={'provenance':'Fresh referee implementation; no author code imported. Exact integer/rational arithmetic.',
        'input_hashes':json.loads((ROOT/'input-verification.json').read_text())['file_hashes'],
        'environment':{'python':sys.version,'sympy':sp.__version__,'networkx':nx.__version__},'sections':{}}
START=time.time()

def checkpoint(name,data):
    RESULT['sections'][name]=data
    RESULT['seconds']=round(time.time()-START,3)
    (ROOT/'independent-check-results.json').write_text(json.dumps(RESULT,ensure_ascii=True,indent=2,default=str),encoding='utf-8')
    print(json.dumps({'section':name,'status':'PASS','seconds':RESULT['seconds']},ensure_ascii=True),flush=True)

def canon(G):return nx.convert_node_labels_to_integers(G)

def exact_inertia(M):
    """Characteristic-polynomial sign variations, with exact exhaustion check."""
    coeff=list(M.charpoly().all_coeffs())
    zeros=0
    while len(coeff)>1 and coeff[-1]==0:coeff.pop();zeros+=1
    def changes(seq):
        signs=[1 if x>0 else -1 for x in seq if x]
        return sum(a!=b for a,b in zip(signs,signs[1:]))
    pos=changes(coeff)
    neg=changes([x*(-1)**i for i,x in enumerate(coeff)])
    assert pos+neg+zeros==M.rows,('non-exhaustive Descartes bounds',M)
    return [pos,neg,zeros]

def parameters(q,ell):
    return [sp.Rational(ell),sp.Integer(0)]+[sp.Rational(i-1,q+1) for i in range(2,q)]

def target(aa):return sp.Matrix(len(aa),len(aa),lambda i,j:1-aa[i]*aa[j])

def hessian_from_coefficients(G,H,beta):
    """Differentiate coefficients obtained from definition (1), with no profiles."""
    G=canon(G);n=len(G);q=H.rows;assert sum(beta)==n-2
    den=lcm(*(int(x.q) for x in H))
    W=[[int(H[i,j]*den) for j in range(q)] for i in range(q)]
    back=[[v for v in G[u] if v<u] for u in range(n)]
    colors=[0]*n
    @lru_cache(None)
    def coefficient(counts):
        left=list(counts)
        def visit(v,weight):
            if v==n:return weight
            total=0
            for color in range(q):
                if not left[color]:continue
                edgeweight=prod(W[color][colors[w]] for w in back[v])
                if not edgeweight:continue
                left[color]-=1;colors[v]=color
                total+=visit(v+1,weight*edgeweight)
                left[color]+=1
            return total
        return visit(0,1)
    M=sp.zeros(q)
    for i in range(q):
        for j in range(i,q):
            counts=list(beta);counts[i]+=1;counts[j]+=1
            M[i,j]=M[j,i]=sp.Rational(coefficient(tuple(counts))*prod(factorial(x) for x in counts),den**G.number_of_edges())
    return M

def layers(G,h):
    """Pair-wise kernel layers, keyed by number of internal conditioned edges."""
    G=canon(G);n=len(G);size=h+2
    A={};B={};T=sp.zeros(h+1);set_counts=Counter()
    for cond_tuple in combinations(range(n),h):
        S=set(cond_tuple);outside=[v for v in range(n) if v not in S]
        e=sum(v in S and w in S for v,w in G.edges());set_counts[e]+=1
        if e not in A:A[e]=[[0]*size for _ in range(size)];B[e]=[[0]*size for _ in range(size)]
        profiles={v:len(S.intersection(G[v])) for v in outside}
        for u,v in combinations(outside,2):
            r,s=profiles[u],profiles[v]
            A[e][r][s]+=1;A[e][s][r]+=1
            if G.has_edge(u,v):
                T[r,s]+=1;T[s,r]+=1
                for i,di in ((r,1),(r+1,-1)):
                    for j,dj in ((s,1),(s+1,-1)):
                        B[e][i][j]+=di*dj;B[e][j][i]+=di*dj
    return {e:(sp.Matrix(A[e]),sp.Matrix(B[e])) for e in A},T,set_counts

def kernel(layer,theta):
    theta=sp.Rational(theta);size=next(iter(layer.values()))[0].rows
    return sum(((1-theta)**e*(theta*A-B) for e,(A,B) in layer.items()),sp.zeros(size))

def compare_profile(G,h,aa,label):
    n=len(G);q=len(aa);ell=aa[0];theta=ell**2
    layer,T,counts=layers(G,h);Q=kernel(layer,theta)
    U=sp.Matrix(q,h+2,lambda i,r:(1-ell*aa[i])**r)
    H=target(aa);beta=[h,n-h-2]+[0]*(q-2)
    direct=hessian_from_coefficients(G,H,beta)
    expected=factorial(h)*factorial(n-h-2)/theta*U*Q*U.T
    assert direct==expected,(label,n,h,q,ell)
    return {'label':label,'n':n,'h':h,'q':q,'ell':str(ell),'U_rank':U.rank(),'hessian_inertia':exact_inertia(direct),'kernel_inertia':exact_inertia(Q),'direct_identity':True}

def independence_number(G,vertices):
    vv=list(vertices)
    for k in range(len(vv),0,-1):
        if any(all(not G.has_edge(u,v) for u,v in combinations(S,2)) for S in combinations(vv,k)):return k
    return 0

def gap(G):
    b=c=0
    for u,v in G.edges():
        nu,nv=set(G[u]),set(G[v])
        b=max(b,independence_number(G,nu-{v}),independence_number(G,nv-{u}))
        c=max(c,independence_number(G,nu&nv))
    return b,c

def cluster(s,aa):
    G=nx.complete_graph(s);nextnode=s
    for a in aa:
        vv=list(range(nextnode,nextnode+a));G.add_nodes_from(vv);G.add_edges_from(combinations(vv,2))
        G.add_edges_from((u,v) for u in range(s) for v in vv);nextnode+=a
    return G

def run():
    # Polynomial identities without assigning graph data.
    N,E,W,U,l=sp.symbols('N E W U l')
    Bh=sp.Matrix([[N,-l*E,0],[-l*E,l*l*W-E,l*W],[0,l*W,-l*l*U]])
    assert sp.expand(Bh.det()-l*l*(N*(E*U-W*W)+l*l*U*(E*E-N*W)))==0
    n,d,tau=sp.symbols('n d tau')
    reg=Bh.subs({N:(n-1)*(n-2),E:d*(n-2),W:d*(d-1),U:tau})
    assert sp.expand(reg.det()-l*l*d*(n-2)*((n-1)*((n-2)*tau-d*(d-1)**2)+l*l*tau*(n-1-d)))==0
    A,B,s=sp.symbols('A B s');L=A+B;C=A*(A-1)+B*(B-1)
    two=sp.Matrix([[2*A*B,C,s*L],[C,2*s*L-C,s*(s-1-L)],[s*L,s*(s-1-L),-s*(s-1)]])
    assert sp.expand(two.det()+s*(L+s-1)*(L*L*(L+2*s-1)+2*A*B*(s-1)*(L+s)))==0
    L,C=sp.symbols('L C')
    M=sp.Matrix([[L*(L-1)-C,C,0,s*L],[C,-C,s*L,-s*L],[0,s*L,0,s*(s-1)],[s*L,-s*L,s*(s-1),-s*(s-1)]])
    assert sp.expand(M.det()-L*s*s*(L+s-1)*(s*L*L-(s-1)*C))==0
    M0=sp.Matrix([[0,0,0,s],[0,0,s,-s],[0,s,0,s*(s-1)],[s,-s,s*(s-1),-s*(s-1)]])
    assert sp.expand(M0.det()-s**4)==0
    aa,bb,cc=sp.symbols('aa bb cc')
    MP=sp.Matrix([[0,0,0,bb],[0,0,bb,-bb],[0,bb,aa,cc],[bb,-bb,cc,-cc]])
    MP1=sp.Matrix([[0,0,bb],[0,aa+2*bb,cc-bb],[bb,cc-bb,-cc]])
    assert sp.expand(MP.det()-bb**4)==0
    assert sp.expand(MP1.det()+bb**2*(aa+2*bb))==0
    VV=sp.Matrix([[x**j for j in [1,2,3,4]] for x in [1,sp.Rational(4,3),sp.Rational(5,3)]])
    restriction=VV*M.subs({L:1,C:0})*VV.T
    assert sp.factor(restriction.det())==sp.Rational(12800,4782969)*s**3*(185*s-473)
    checkpoint('symbolic_determinants',{'identities':8,'four_spin_trace':str(sp.factor(sp.trace(restriction))),'status':'all zero residuals'})

    # Fractional and endpoint profiles, rectangular and square, isolated vertices,
    # n=3, h=n-2, same free spins and coincidences with differentiated spin labels.
    testgraphs=[('empty3',nx.empty_graph(3)),('edge_isolate',nx.Graph([(0,1)])),('P3',nx.path_graph(3)),('K3',nx.complete_graph(3)),('C4',nx.cycle_graph(4)),('star4',nx.star_graph(3)),('diamond',cluster(2,[1,1])),('bowtie',cluster(1,[2,2])),('K5',nx.complete_graph(5)),('P5',nx.path_graph(5))]
    testgraphs[1][1].add_node(2)
    comparisons=[]
    for label,G in testgraphs:
        for h in sorted(set([1,len(G)-2])):
            for q in sorted(set([2,3,h+2,h+3])):
                for ell in [sp.Rational(-2,5),sp.Integer(-1)]:
                    comparisons.append(compare_profile(G,h,parameters(q,ell),label))
    checkpoint('rectangular_profile',{'comparisons':len(comparisons),'rows':comparisons})

    # General degree identity: disconnected and irregular cases are included.
    degree_rows=[]
    for label,G in testgraphs:
        if max(dict(G.degree()).values(),default=0)<2:continue
        G=canon(G);n=len(G);D=max(dict(G.degree()).values());q=D+1
        counts=[sum(G.degree(v)==r for v in G) for r in range(q)]
        nu=sp.Matrix(counts);B0=nu*nu.T-sp.diag(*counts)
        for u,v in G.edges():
            x=sp.zeros(q,1);y=sp.zeros(q,1)
            x[G.degree(u)]=1;x[G.degree(u)-1]=-1
            y[G.degree(v)]=1;y[G.degree(v)-1]=-1
            B0-=x*y.T+y*x.T
        H=sp.Matrix(q,q,lambda i,j:i+j+2)
        ev=sp.Matrix(q,q,lambda i,r:sp.Rational(i+2,2)**r)
        direct=hessian_from_coefficients(G,H,[n-2]+[0]*D)
        assert direct==factorial(n-2)*2**G.number_of_edges()*ev*B0*ev.T
        degree_rows.append({'label':label,'inertia':exact_inertia(B0)})
    checkpoint('degree_kernel',{'comparisons':len(degree_rows),'rows':degree_rows})

    # Independent structural census; no stored labels or certificate choices.
    atlas=[(i,G) for i,G in enumerate(nx.graph_atlas_g()) if 3<=len(G)<=7 and nx.is_connected(G)]
    noncliques=[(i,G) for i,G in atlas if G.number_of_edges()<len(G)*(len(G)-1)//2]
    counts=Counter();max_rows=[];gap_rows=[];diamond_rows=[]
    for ix,G in noncliques:
        D=max(dict(G.degree()).values());vertices=[v for v in G if G.degree(v)==D]
        eligible=all(set(G[u])|{u}!=set(G[v])|{v} for u,v in combinations(vertices,2))
        minimum=min(dict(G.degree()).values());mv=[v for v in G if G.degree(v)==minimum]
        if all(not G.has_edge(u,v) for u,v in combinations(mv,2)):counts['independent_minimum_degree']+=1
        if eligible:
            h=D-1;layer,T,_=layers(G,h)
            assert T[h,h]==0
            j=next(j for j in range(h) if T[h,j]>0)
            f=sp.zeros(h+1,1);f[j]=1;f[h]=-(T[j,j]+1)/(2*T[h,j])
            assert (f.T*T*f)[0]==-1
            y=sp.Matrix([sum(f[k] for k in range(r,h+1)) for r in range(h+1)]+[0]);p=sp.ones(h+2,1)
            columns=sp.Matrix.hstack(p,y)
            found=None
            for k in range(1,32):
                theta=sp.Rational(1,4**k);Q=kernel(layer,theta);compressed=columns.T*Q*columns
                if compressed[0,0]>0 and compressed.det()>0:found=k;break
            assert found is not None
            max_rows.append({'atlas_index':ix,'h':h,'k':found,'compression_det':str(compressed.det())})
        b,c=gap(G)
        if b>c:
            h=c+1;layer,T,sc=layers(G,h);Q=kernel(layer,1)
            p=sp.ones(h+2,1);u=sp.zeros(h+2,1);u[-1]=1;w=Q*u
            V=sp.Matrix.hstack(p,u,w);comp=V.T*Q*V
            assert (u.T*Q*u)[0]==0 and (p.T*Q*u)[0]==0 and any(w)
            assert comp.det()==-comp[0,0]*((w.T*w)[0])**2 and comp[0,0]>0
            gap_rows.append(ix)
        diamondfree=all(G.subgraph(S).number_of_edges()!=5 for S in combinations(G,4))
        if diamondfree:
            assert b>c
            diamond_rows.append(ix)
            counts['diamond_trianglefree' if sum(nx.triangles(G).values())==0 else 'diamond_triangles']+=1
    assert len(atlas)==994 and len(noncliques)==989
    assert len(max_rows)==817 and len(gap_rows)==634 and len(diamond_rows)==255
    assert counts['independent_minimum_degree']==806
    checkpoint('atlas_structural_census',{'connected':len(atlas),'noncliques':len(noncliques),'max_degree_certificates':len(max_rows),'gap_graphs':len(gap_rows),'diamondfree':len(diamond_rows),'counts':dict(counts),'maximum_degree_rows':max_rows,'gap_indices':gap_rows,'diamond_indices':diamond_rows})

    # Distinct universal-family branches, with large h relative to q and h=1.
    family_rows=[]
    diamondpars=[sp.Integer(-1),0,sp.Rational(1,3),sp.Rational(2,3)]
    fivepars=[sp.Integer(-1),0,sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4)]
    for s,parts in [(1,[1,1]),(4,[1,1]),(1,[2,1]),(2,[3,2]),(1,[1,1,1]),(3,[1,1,1]),(2,[2,1,1]),(1,[2,1,1,1,1,1]),(1,[1]*7)]:
        G=cluster(s,parts);r=len(parts);L=sum(a-1 for a in parts)
        h=(2 if L else 1) if r==2 else (r if L else r-1)
        pars=diamondpars if r==2 else fivepars
        row=compare_profile(G,h,pars,f'cluster({s},{parts})');assert row['hessian_inertia'][0]>=2
        family_rows.append(row)
    for parts in [[2,1],[2,2],[2,1,1],[3,1],[3,2,1],[4,1,1],[4,3],[5,1],[6,1,1],[3,3,3]]:
        G=nx.complete_multipartite_graph(*parts);h=max(parts)-1
        row=compare_profile(G,h,diamondpars,f'multipartite({parts})');assert row['hessian_inertia'][0]>=2
        family_rows.append(row)
    for s in [1,2,3,5]:
        row=compare_profile(cluster(s,[2,1,1]),3,diamondpars,f'four_spin_restriction(s={s})')
        assert row['hessian_inertia']==([2,1,1] if s<3 else [1,2,1])
        family_rows.append(row)
    checkpoint('fixed_targets',{'direct_comparisons':len(family_rows),'rows':family_rows})

    # C5[K2]: explicit subsets, not the manuscript's binomial local formula.
    blow=nx.lexicographic_product(nx.cycle_graph(5),nx.complete_graph(2));blow=canon(blow)
    rows=[];stored={}
    for h in range(1,9):
        layer,T,sc=layers(blow,h);ins=exact_inertia(T);assert ins[1]==0
        stored[h]=T
        row={'h':h,'T':[[str(x) for x in rr] for rr in T.tolist()],'T_inertia':ins}
        if h<=4:
            minors=[T[:j,:j].det() for j in range(1,h+2)]
            row['leading_principal_minors']=list(map(str,minors));assert all(x>0 for x in minors)
        if h in [3,4,5]:
            emin=min(sc);leading=layer[emin][0]-layer[emin][1]
            row['minimum_internal_edges']=emin;row['leading_endpoint_inertia']=exact_inertia(leading)
            aa=[sp.Rational(-99,100),0]+[sp.Rational(i-1,h+2) for i in range(2,h+2)]
            directrow=compare_profile(blow,h,aa,f'C5[K2],h={h}')
            expected={3:[2,3,0],4:[2,4,0],5:[2,3,2]}
            assert directrow['hessian_inertia']==expected[h]
            assert row['leading_endpoint_inertia'][0]==(1 if h==5 else 2)
            row['full_hierarchy']=directrow
        rows.append(row)
    for h in [1,2,3]:
        for r in range(h+1):
            for t in range(h+1):assert stored[h][r,t]==stored[8-h][4-r,4-t]
    checkpoint('C5_K2_limitation',{'rows':rows,'direct_comparisons':3,'all_eight_T_PSD':True})

    # Genuine Lorentzian controls for three fixed subtargets: enumerate all
    # assignments and all derivatives, plus symmetric M-convex exchanges.
    g7=nx.Graph([(0,1),(0,4),(1,2),(1,4),(2,3),(4,5),(5,6)])
    g6=nx.Graph([(0,1),(0,4),(0,5),(1,2),(1,5),(2,3),(2,5),(3,4)])
    controls=[]
    for G,aa in [(g7,[-1,0,sp.Rational(1,3)]),(g6,[-1,0,sp.Rational(2,3)]),(g6,[-1,sp.Rational(1,3),sp.Rational(2,3)])]:
        G=canon(G);n=len(G);H=target(aa);coef=defaultdict(lambda:sp.Integer(0))
        for colors in product(range(3),repeat=n):
            wt=prod(H[colors[u],colors[v]] for u,v in G.edges())
            if wt:coef[tuple(colors.count(i) for i in range(3))]+=wt
        support=set(coef);exchange_tests=0
        for a in support:
            for b in support:
                for i in range(3):
                    if a[i]<=b[i]:continue
                    found=False
                    for j in range(3):
                        if a[j]>=b[j]:continue
                        ca=list(a);cb=list(b);ca[i]-=1;ca[j]+=1;cb[i]+=1;cb[j]-=1
                        if tuple(ca) in support and tuple(cb) in support:found=True;break
                    assert found;exchange_tests+=1
        inertias=[]
        for b0 in range(n-1):
            for b1 in range(n-1-b0):
                beta=[b0,b1,n-2-b0-b1];M=sp.zeros(3)
                for i in range(3):
                    for j in range(3):
                        alpha=beta.copy();alpha[i]+=1;alpha[j]+=1
                        M[i,j]=coef.get(tuple(alpha),0)*prod(factorial(x) for x in alpha)
                ins=exact_inertia(M);assert ins[0]<=1;inertias.append(ins)
        controls.append({'n':n,'parameters':list(map(str,aa)),'support_size':len(support),'exchange_tests':exchange_tests,'derivatives':len(inertias),'inertias':inertias})
    checkpoint('three_subtarget_Lorentzian_controls',{'rows':controls,'all_derivatives':sum(r['derivatives'] for r in controls)})
    RESULT['status']='PASS_ALL_INDEPENDENT_CHECKS'
    checkpoint('complete',{'status':RESULT['status']})

if __name__=='__main__':run()
