from pathlib import Path
from fractions import Fraction
import ast,itertools,json,math,time,collections
import networkx as nx
import sympy as sp
R=Path(__file__).parent
for name in ['certify_profile_hierarchy.py','probe_zero_parameter_kernels.py']:
    tree=ast.parse((R/name).read_text())
    exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef)],type_ignores=[]),'helpers','exec'))
G=blowup_cliques(nx.cycle_graph(5),2);rows=[];zero_rows=[]
for h in range(1,len(G)-1):
    C=local_kernel(G,h);D=sp.zeros(h+2,h+1)
    for r in range(h+1):D[r,r]=1;D[r+1,r]=-1
    Q0,_=integer_kernel(G,h,Fraction(0));assert Q0==-D*C*D.T
    ins,blocks=inertia(C);assert ins[1]==0
    zero_rows.append(dict(h=h,matrix=[[str(x) for x in row] for row in C.tolist()],inertia=ins,congruence=blocks,direct_subset_comparison=True))
for h in [3,4,5]:
    emin=min(G.subgraph(S).number_of_edges() for S in itertools.combinations(list(G),h));L=sp.zeros(h+2);cnt=0
    for ss in itertools.combinations(list(G),h):
        S=set(ss)
        if G.subgraph(S).number_of_edges()!=emin:continue
        cnt+=1;outside=[v for v in G if v not in S];p={v:len(set(G[v])&S) for v in outside}
        nu=sp.Matrix([sum(p[v]==r for v in outside) for r in range(h+2)])
        L+=nu*nu.T-sp.diag(*nu)
        for u,v in G.edges():
            if u in p and v in p:
                a=sp.zeros(h+2,1);b=sp.zeros(h+2,1)
                a[p[u]]=1;a[p[u]+1]=-1;b[p[v]]=1;b[p[v]+1]=-1
                L-=a*b.T+b*a.T
    ii,blocks=inertia(L)
    ell=Fraction(-99,100);Q,den=integer_kernel(G,h,ell)
    H,U,aa,target=direct_hessian(G,h,ell)
    factor=sp.Rational(math.factorial(h)*math.factorial(len(G)-h-2),den)/(sp.Rational(ell.numerator,ell.denominator)**2)
    assert H==factor*U*Q*U.T and min(target)>0
    jj,_=inertia(Q);assert jj[0]>=2
    rows.append(dict(h=h,minimum_induced_edges=emin,minimizing_sets=cnt,
        leading_kernel=[[str(x) for x in row] for row in L.tolist()],leading_inertia=ii,leading_congruence=blocks,
        ell=str(ell),positive_inertia=jj,direct_partition_identity=True))

# Independent checks of the coefficient certificate printed in the paper.
x,z,y=sp.symbols('x z y')
poly=sp.Poly(sp.expand(10*(1+x*y*z)**4*(1+z)**4+40*(1+x*y*z)**2*(1+x*z)**2*(1+y*z)**2*(1+z)**2),x,y,z)
expected_pivots={1:['120','200/3'],2:['100','224','300/7'],3:['40','480','360','200/9'],4:['10','320','600','592/3','250/37']}
embedded={};J=sp.zeros(5)
for i in range(5):J[i,4-i]=1
for h in range(9):
    Ch=local_kernel(G,h)
    for r in range(h+1):
        for t in range(h+1):assert Ch[r,t]==poly.coeff_monomial(x**r*y**t*z**h)
    embedded[h]=sp.Matrix(5,5,lambda r,t:Ch[r,t] if max(r,t)<Ch.rows else 0)
    if h in expected_pivots:
        _,bb=inertia(Ch)
        assert [b['pivot'] for b in bb]==expected_pivots[h]
for h in range(9):assert embedded[h]==J*embedded[8-h]*J

# Symbolic first non-independent layer for the full C5[K_s] family.
s=sp.symbols('s',integer=True,positive=True);F=nx.cycle_graph(5)
Z=sp.zeros(5);patterns=[]
for t in itertools.product(range(4),repeat=5):
    if sum(t)!=3:continue
    e=sum(x*(x-1)//2 for x in t)+sum(t[u]*t[v] for u,v in F.edges())
    if e!=1:continue
    w=sp.prod(sp.Rational(1,math.factorial(x))*sp.prod(s-j for j in range(x)) for x in t)
    nu=sp.zeros(5,1);profile={i:t[i]+sum(t[j] for j in F[i]) for i in F}
    rem={i:s-t[i] for i in F}
    for i in F:nu[profile[i]]+=rem[i]
    Q=nu*nu.T-sp.diag(*nu)
    for i in F:
        v=sp.zeros(5,1);v[profile[i]]=1;v[profile[i]+1]=-1
        Q-=rem[i]*(rem[i]-1)*v*v.T
    for i,j in F.edges():
        a=sp.zeros(5,1);b=sp.zeros(5,1)
        a[profile[i]]=1;a[profile[i]+1]=-1;b[profile[j]]=1;b[profile[j]+1]=-1
        Q-=rem[i]*rem[j]*(a*b.T+b*a.T)
    Z+=w*Q;patterns.append(t)
Z=Z.applyfunc(sp.factor)
assert all(Z[0,j]==0 for j in range(5))
M=(Z[1:,1:]/(5*s*s)).applyfunc(sp.factor)
assert not M.atoms(sp.Float)
assert Z.subs(s,2)==sp.Matrix(rows[0]['leading_kernel'])
det=sp.factor(M.det())
out=dict(status='PASS_EXACT_BLOWUP_LAYER_DIAGNOSTIC',source='C5[K2]',edges=list(G.edges()),zero_parameter_psd_all_eight_levels=True,zero_parameter_certificates=zero_rows,
    direct_positive_checks=3,rows=rows,coefficient_polynomial_checked=True,profile_reversal_checked=True,pivot_table_checked=True,symbolic_family='C5[K_s], h=3, minimum induced-edge layer 1',
    symbolic_patterns=len(patterns),symbolic_normalized_matrix=[[str(x) for x in row] for row in M.tolist()],
    symbolic_determinant=str(det),symbolic_integer_samples=[dict(s=k,inertia=inertia(M.subs(s,k))[0]) for k in range(2,11)],symbolic_principal_minors={','.join(map(str,ix)):str(sp.factor(M.extract(ix,ix).det())) for ix in itertools.combinations(range(4),2)},
    limit='The C5[K2] checks are exact. The symbolic family requires a written sign proof and further direct checks before integration. Not an external review.')
(R/'blowup-layer-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['rows','zero_parameter_certificates','edges']}))
print(json.dumps([dict(h=x['h'],leading_inertia=x['leading_inertia'],positive_inertia=x['positive_inertia']) for x in rows]))
