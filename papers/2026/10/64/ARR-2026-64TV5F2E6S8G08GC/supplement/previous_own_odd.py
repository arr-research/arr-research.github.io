"""Independent odd-cycle audit: positive occupations, explicit category formulas.
No author program is imported. Archived JSON is read only for comparison.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path
import hashlib, json, math, time
import sympy as sp

ROOT=Path(__file__).resolve().parent
IN=ROOT/'input-snapshot'
K=sp.symbols('k',integer=True,positive=True)

def save(name,obj):
    (ROOT/name).write_text(json.dumps(obj,ensure_ascii=True,indent=2)+'\n',encoding='utf-8')
def matjson(M): return [[str(x) for x in row] for row in M.tolist()]

def inertia(M,pivots=False):
    A=[[Fraction(x) for x in row] for row in M.tolist()]
    pos=neg=zero=0; cert=[]
    while A:
        n=len(A); pivot=next((i for i in range(n) if A[i][i]),None)
        if pivot is not None:
            order=[pivot]+[j for j in range(n) if j!=pivot]
            A=[[A[i][j] for j in order] for i in order]
            d=A[0][0]; pos+=d>0; neg+=d<0
            cert.append({'size':1,'permutation':order,'pivot':str(d)})
            A=[[A[i][j]-A[i][0]*A[0][j]/d for j in range(1,n)] for i in range(1,n)]
        else:
            pair=next(((i,j) for i in range(n) for j in range(i+1,n) if A[i][j]),None)
            if pair is None:
                zero+=n; break
            u,v=pair; order=[u,v]+[j for j in range(n) if j not in pair]
            A=[[A[i][j] for j in order] for i in order]; b=A[0][1]
            pos+=1; neg+=1; cert.append({'size':2,'permutation':order,'offdiag':str(b)})
            A=[[A[i][j]-(A[i][0]*A[1][j]+A[i][1]*A[0][j])/b for j in range(2,n)] for i in range(2,n)]
    answer=[int(pos),int(neg),int(zero)]
    return (answer,cert) if pivots else answer

def compositions(total,width,cap):
    if width==0:
        if total==0: yield ()
        return
    for x in range(max(0,total-cap*(width-1)),min(cap,total)+1):
        for rest in compositions(total-x,width-1,cap): yield (x,)+rest

def edges_inside(a):
    return sum(x*(x-1)//2 for x in a)+sum(a[i]*a[(i+1)%len(a)] for i in range(len(a)))

def actual_profiles(a,s):
    """Profiles and edges counted from remaining classes, with ordered endpoints."""
    m=len(a); nu=Counter(); C=Counter()
    remaining=[s-x for x in a]
    profiles=[a[(i-1)%m]+a[i]+a[(i+1)%m] for i in range(m)]
    for i,b in enumerate(remaining):
        r=profiles[i]; nu[r]+=b; C[r,r]+=b*(b-1)
        j=(i+1)%m
        C[r,profiles[j]]+=b*remaining[j]
        C[profiles[j],r]+=b*remaining[j]
    return {r:n for r,n in nu.items() if n},{rt:c for rt,c in C.items() if c}

def local_kernel(nu,C,s):
    out=defaultdict(lambda:0)
    for r,nr in nu.items():
        for t,nt in nu.items(): out[r,t]+=nr*nt
        out[r,r]-=nr
    for (r,t),c in C.items():
        out[r,t]-=c; out[r+1,t]+=c; out[r,t+1]+=c; out[r+1,t+1]-=c
    return out

def representatives(k,s):
    """Only genuine positive occupations: no endpoint duplication/subtraction."""
    m=2*k+1; out=[]
    for partial in range(k):
        a=[0]*m
        for j in range(k): a[2*j]=s-(j==partial)
        out.append((tuple(a),s,'unsplit'))
    for t in range(1,s-1):
        a=[0]*m; a[0]=t; a[1]=s-1-t
        for j in range(k-1): a[3+2*j]=s
        out.append((tuple(a),math.comb(s,t)*math.comb(s,t+1),'split_partial'))
    for t in range(1,s):
        for partial in range(k-1):
            a=[0]*m; a[0]=t; a[1]=s-t
            for j in range(k-1): a[3+2*j]=s-(j==partial)
            out.append((tuple(a),s*math.comb(s,t)**2,'split_full'))
    return out

def unique_patterns(k,s):
    out={}; m=2*k+1
    for a,w,kind in representatives(k,s):
        for j in range(m):
            b=a[j:]+a[:j]
            assert b not in out
            assert w==math.prod(math.comb(s,x) for x in b)
            out[b]=w
    assert len(out)==m*(k*s-1)
    return out

def ground_positive(k,s,return_stats=False):
    m=2*k+1; out=defaultdict(lambda:0); N=0; empty_counts=Counter()
    for a,w,kind in representatives(k,s):
        assert sum(a)==k*s-1 and edges_inside(a)==(s-1)*(k*s-2)//2
        nu,C=actual_profiles(a,s)
        for rt,c in local_kernel(nu,C,s).items(): out[rt]+=m*w*c
        N+=m*w
        for j in range(m):
            if a[j]==0:
                r=a[(j-1)%m]+a[(j+1)%m]
                empty_counts[r]+=m*w
    L=sp.zeros(2*s+2)
    for (r,t),c in out.items(): L[r,t]=c
    expected=m*(math.comb(2*s,s-1)+(k-1)*s*math.comb(2*s,s)-k*s)
    assert N==expected
    return (L,N,empty_counts) if return_stats else (L,N)

def brute_classification(k,s):
    m=2*k+1; h=k*s-1; best=math.inf; found=[]; examined=0
    for a in compositions(h,m,s):
        examined+=1; e=edges_inside(a)
        if e<best: best=e; found=[a]
        elif e==best: found.append(a)
    positive=unique_patterns(k,s)
    assert best==(s-1)*(k*s-2)//2 and set(found)==set(positive)
    return {'k':k,'s':s,'occupations_examined':examined,'ground_occupations':len(found),
            'ground_subsets':sum(positive.values()),'e0':best,'complete_pattern_equality':True}

def add(d,key,value): d[key]=d.get(key,0)+value
def diag(C,r,c): add(C,(r,r),c)
def cross(C,r,t,c): add(C,(r,t),c); add(C,(t,r),c)

def explicit_categories(s,k=K):
    """Derived from local configurations, not k=4 representatives or fitting.
    Returns name, multiplicity including binomial weight, nu, C.
    Near formulas are valid already at k=3; far-B is multiplied by k-3.
    """
    low=s-1; full=2*s; categories=[]
    # One component split into two nonempty classes, total s-1.
    for t in range(1,s-1):
        l=s+t; r=2*s-1-t
        nu={}; C={}
        for idx,val in [(low,s+1),(l,s),(r,s),(full,(k-2)*s)]: add(nu,idx,val)
        diag(C,low,s*(s+1))
        for idx,mult in [(l,1),(r,1),(full,k-2)]: diag(C,idx,mult*s*(s-1))
        cross(C,low,l,s*(s-t)); cross(C,low,r,s*(t+1))
        categories.append(('A',math.comb(s,t)*math.comb(s,t+1),nu,C))
    # Split total s; the unique partial single class is next to a boundary.
    for t in range(1,s):
        l=s+t; r=2*s-1-t
        nu={}; C={}
        for idx,val in [(s,s),(low,1),(l,s),(r,s),(2*s-1,s),(full,(k-3)*s)]: add(nu,idx,val)
        diag(C,s,s*(s-1))
        for idx,mult in [(l,1),(r,1),(2*s-1,1),(full,k-3)]: diag(C,idx,mult*s*(s-1))
        cross(C,s,l,s*(s-t)); cross(C,s,r,s*t)
        cross(C,low,r,s); cross(C,low,2*s-1,s)
        categories.append(('B_near',2*s*math.comb(s,t)**2,nu,C))
        # Far partial single class: two ordinary empty neighbors, k-4 full gaps.
        l=s+t; r=2*s-t
        nu={}; C={}
        for idx,val in [(s,s),(low,1),(l,s),(r,s),(2*s-1,2*s),(full,(k-4)*s)]: add(nu,idx,val)
        diag(C,s,s*(s-1))
        for idx,mult in [(l,1),(r,1),(2*s-1,2),(full,k-4)]: diag(C,idx,mult*s*(s-1))
        cross(C,s,l,s*(s-t)); cross(C,s,r,s*t); cross(C,low,2*s-1,2*s)
        categories.append(('B_far',(k-3)*s*math.comb(s,t)**2,nu,C))
    # Positive unsplit patterns, each weighted s; no subtraction.
    nu={}; C={}
    for idx,val in [(low,s+1),(s,s),(2*s-1,s),(full,(k-2)*s)]: add(nu,idx,val)
    diag(C,low,s*(s+1)); diag(C,s,s*(s-1)); diag(C,2*s-1,s*(s-1)); diag(C,full,(k-2)*s*(s-1))
    cross(C,low,s,s*s); cross(C,low,2*s-1,s)
    categories.append(('endpoint_near',2*s,nu,C))
    nu={}; C={}
    for idx,val in [(low,1),(s,2*s),(2*s-1,2*s),(full,(k-3)*s)]: add(nu,idx,val)
    diag(C,s,2*s*(2*s-1)); diag(C,2*s-1,2*s*(s-1)); diag(C,full,(k-3)*s*(s-1))
    cross(C,low,2*s-1,2*s)
    categories.append(('endpoint_far',(k-2)*s,nu,C))
    return categories

def symbolic_kernel(s):
    entries=defaultdict(lambda:0)
    for kind,w,nu,C in explicit_categories(s):
        for rt,c in local_kernel(nu,C,s).items(): entries[rt]+=w*c
    M=sp.zeros(2*s+2)
    for (r,t),v in entries.items(): M[r,t]=sp.expand(v)
    return M

def validate_categories(s,k):
    # Compare positive type totals to actual anchored occupations at this k.
    actual=defaultdict(lambda:sp.zeros(2*s+2))
    for a,w,kind in representatives(k,s):
        nu,C=actual_profiles(a,s); term=sp.zeros(2*s+2)
        for (r,t),v in local_kernel(nu,C,s).items(): term[r,t]=v*w
        actual[kind]+=term
    derived=defaultdict(lambda:sp.zeros(2*s+2))
    mapping={'A':'split_partial','B_near':'split_full','B_far':'split_full',
             'endpoint_near':'unsplit','endpoint_far':'unsplit'}
    for kind,w,nu,C in explicit_categories(s,k):
        if w==0: continue
        assert all(v>=0 for v in nu.values()) and all(v>=0 for v in C.values())
        term=sp.zeros(2*s+2)
        for (r,t),v in local_kernel(nu,C,s).items(): term[r,t]=v*w
        derived[mapping[kind]]+=term
    assert all(actual[name]==derived[name] for name in ('split_partial','split_full','unsplit'))

def vertex_subset_ground(k,s):
    m=2*k+1; n=m*s; h=k*s-1
    def edge(u,v):
        a,b=u//s,v//s
        return a==b or (a-b)%m in (1,m-1)
    edges=[(u,v) for u in range(n) for v in range(u+1,n) if edge(u,v)]
    adj=[{v for v in range(n) if v!=u and edge(u,v)} for u in range(n)]
    best=math.inf; N=0; L=sp.zeros(2*s+2)
    for ss in combinations(range(n),h):
        S=set(ss); e=sum(u in S and v in S for u,v in edges)
        if e>best: continue
        if e<best: best=e; N=0; L=sp.zeros(2*s+2)
        N+=1; rr={u:len(adj[u]&S) for u in range(n) if u not in S}
        for u,v in permutations(rr,2):
            r,t=rr[u],rr[v]; L[r,t]+=1
            if edge(u,v):
                L[r,t]-=1; L[r+1,t]+=1; L[r,t+1]+=1; L[r+1,t+1]-=1
    expected,count=ground_positive(k,s)
    assert L==expected and count==N
    return {'k':k,'s':s,'vertex_subsets':math.comb(n,h),'ground_subsets':N,'e0':best,'equality':True}

def check_archived_pivots(M,blocks):
    A=M.copy(); signs=[0,0,0]
    for block in blocks:
        size=block['size']
        if size==1:
            j=block['index']; order=[j]+[i for i in range(A.rows) if i!=j]
            A=A.extract(order,order); p=A[0,0]
            assert p==sp.Rational(block['pivot'])
            signs[0 if p>0 else 1]+=1
            A=A[1:,1:]-A[1:,0]*A[0,1:]/p
        else:
            raise AssertionError('Unexpected archived pivot format; inspect explicitly')
    assert A.rows==0
    return signs

def small_and_general_checks():
    started=time.time(); brute=[]
    for k,sizes in [(2,range(2,9)),(3,range(2,8)),(4,range(2,5)),(5,[2])]:
        for s in sizes: brute.append(brute_classification(k,s))
    save('classification-checks.json',{'status':'PASS','cases':brute,
         'total_occupations':sum(x['occupations_examined'] for x in brute)})
    print(json.dumps({'classification_cases':len(brute),'occupations':sum(x['occupations_examined'] for x in brute)}),flush=True)
    actual_vertices=[vertex_subset_ground(2,2),vertex_subset_ground(3,2),vertex_subset_ground(2,3)]
    stored=json.loads((IN/'odd-cycle-ground-kernels.json').read_text())
    c5={x['s']:x for x in json.loads((IN/'cycle-ground-classification-checks.json').read_text())['rows']}
    small={x['s']:x for x in json.loads((IN/'odd-cycle-small-four-inertia.json').read_text())['rows']}
    exception=json.loads((IN/'odd-cycle-size-six-exception.json').read_text())
    rows=[]; polynomial_rows=[]; s6data=None
    t=sp.symbols('t')
    for s in range(2,14):
        M=symbolic_kernel(s)
        active=[r for r in range(M.rows) if any(M.row(r))]
        archived=next(x for x in stored['symbolic_kernels'] if x['s']==s)
        archived_M=sp.Matrix([[sp.sympify(v,locals={'k':K}) for v in row] for row in archived['matrix_divided_by_cycle_length']])
        assert active==archived['active_profiles'] and M.extract(active,active)==archived_M
        for k in (3,4,5,7):
            validate_categories(s,k)
            L,N=ground_positive(k,s)
            assert M.subs(K,k)*(2*k+1)==L
            rows.append({'k':k,'s':s,'N':N,'positive_category_agreement':True})
        L,N=ground_positive(2,s)
        old=c5[s]; ids=old['active_profiles']
        assert L.extract(ids,ids)==sp.Matrix(old['active_kernel'])
        if s<=12: assert inertia(L.extract(ids,ids))[0]>=2
        rows.append({'k':2,'s':s,'N':N,'c5_archive_agreement':True})
        rec={'s':s,'active':active,'polynomial_kernel_divided_by_m':matjson(M.extract(active,active)),
             'maximum_entry_degree_k':int(max(sp.degree(v,K) for v in M if v!=0))}
        if s<=12:
            assert M[s-1,s-1]==0
            off=sp.expand(M[s-1,s]); offshift=sp.Poly(off.subs(K,t+3),t).all_coeffs()
            assert all(c>=0 for c in offshift) and offshift[-1]>0
            assert sp.expand(off-sp.sympify(small[s]['low_offdiagonal'],locals={'k':K}))==0
            ids=[s-1,s,2*s-1,2*s]
            det=sp.factor(M.extract(ids,ids).det(method='domain-ge'))
            shift=4 if s==6 else 3
            coefficients=sp.Poly(det.subs(K,t+shift),t).all_coeffs()
            assert all(c>=0 for c in coefficients) and coefficients[-1]>0
            reference=exception['certificate'] if s==6 else small[s]['certificate']
            assert ids==reference['profiles']
            assert sp.expand(det-sp.sympify(reference['determinant'],locals={'k':K}))==0
            key='shifted_coefficients' if s==6 else 'positive_det_shifted_coefficients'
            assert [str(c) for c in coefficients]==reference[key]
            rec.update({'four_profiles':ids,'determinant':str(det),'shift':shift,
                        'shifted_coefficients':[str(c) for c in coefficients],
                        'low_offdiagonal':str(off),'inertia_for_integer_k_at_least_shift':[2,2,0]})
            if s==6:
                # k=3 independently generated from real positive occupations.
                direct,N=ground_positive(3,6)
                B=direct.extract(active,active)/7
                assert B==M.extract(active,active).subs(K,3)
                signs,ownpivots=inertia(B,True)
                assert signs==[2,7,0]
                source=next(x for x in exception['rows'] if x['k']==3)
                assert check_archived_pivots(B,source['blocks'])==signs
                s6data={'k':3,'s':6,'actual_kernel_divided_by_7':matjson(B),'active':active,'inertia':signs,
                        'own_pivots':ownpivots,'archived_pivots_replayed':True,
                        'four_block_determinant_at_k3':str(det.subs(K,3)),
                        'four_block_inertia_at_k3':inertia(M.extract(ids,ids).subs(K,3)),
                        'N':N,'independent_positive_pattern_reconstruction':True}
        polynomial_rows.append(rec)
        print(json.dumps({'s':s,'symbolic_k3_and_higher_verified':True}),flush=True)
    save('symbolic-and-small-checks.json',{'status':'PASS','classified_pattern_checks':rows,
         'symbolic_kernels':polynomial_rows,'exception_s6_k3':s6data,'vertex_subset_checks':actual_vertices,
         'elapsed_seconds':round(time.time()-started,3)})
    return M

def shifted_integer_coefficients(poly,var,offset):
    """Plain integer binomial transform, independent of symbolic substitution."""
    P=sp.Poly(poly,var); n=P.degree(); coeff=[int(P.nth(i)) for i in range(n+1)]
    return [sum(coeff[j]*math.comb(j,i)*offset**(j-i) for j in range(i,n+1)) for i in range(n+1)]

def tail_checks():
    s,k,B,u,t=sp.symbols('s k B u t')
    choose=lambda j:sp.prod(s-i for i in range(j))/math.factorial(j)
    m=2*k+1; R=(k+1)*s+1
    A={j:2*m*(choose(j)*choose(j+1)+s*choose(j+1)**2+(k-2)*s*choose(j)**2) for j in (1,2,3)}
    N=m*(s*B/(s+1)+(k-1)*s*B-k*s)
    Gram=sp.Matrix([[R*(R-1)*N,(R-1)*s*(A[2]+A[3])],
                    [(R-1)*s*(A[2]+A[3]),s*(s-1)*(A[2]-A[1])]])
    F=sp.factor(R*N*(s-1)*(A[2]-A[1])-(k+1)*s*s*(A[2]+A[3])**2)
    assert sp.factor(Gram.det()-(k+1)*s*s*F)==0
    H=sp.factor(sp.cancel(F/(2*m*m)))
    num,den=sp.fraction(H)
    assert den==165888
    source=json.loads((IN/'odd-cycle-tail-induction.json').read_text())
    assert sp.expand(H-sp.sympify(source['F'],locals={'s':s,'k':k,'B':B}))==0
    coeffs=sp.Poly(sp.expand(num.subs(k,u+2)),u)
    assert coeffs.degree()==3
    cert=[]
    for j in range(4):
        c=sp.expand(coeffs.nth(j)); P=sp.expand(c).coeff(B); Q=-c.subs(B,0)
        assert sp.expand(c-P*B+Q)==0
        G=sp.expand((4*s+2)*P.subs(s,s+1)*Q-(s+1)*P*Q.subs(s,s+1))
        item={'power_k_minus_2':j,'polynomials':{},'base_margin':str((P*math.comb(26,13)-Q).subs(s,13))}
        assert int(item['base_margin'])>0
        for label,poly in [('P',P),('Q',Q),('G',G)]:
            exact=shifted_integer_coefficients(poly,s,13)
            symbolic=list(reversed(sp.Poly(poly.subs(s,t+13),t).all_coeffs()))
            assert exact==symbolic and all(v>0 for v in exact)
            archived=source['coefficients'][str(j)]['certificates'][label]
            assert sp.expand(poly-sp.sympify(archived['polynomial'],locals={'s':s}))==0
            assert [str(v) for v in reversed(exact)]==archived['coefficients_descending']
            item['polynomials'][label]={'expression':str(poly),'degree':len(exact)-1,
                                        'positive_shifted_coefficients_ascending':[str(v) for v in exact]}
        assert item['base_margin']==source['coefficients'][str(j)]['base_margin']
        cert.append(item)
    numerical=[]
    for kk in (2,3,4,5,7,12):
        for ss in (9,12,13,14,20):
            L,count,ec=ground_positive(kk,ss,True)
            actualA=[ec[ss+j] for j in (1,2,3)]
            predictedA=[int(A[j].subs({s:ss,k:kk})) for j in (1,2,3)]
            assert actualA==predictedA
            p=sp.ones(L.rows,1); x=sp.zeros(L.rows,1); x[ss+2]=x[ss+3]=1
            actual=sp.Matrix.hstack(p,x).T*L*sp.Matrix.hstack(p,x)
            expected=Gram.subs({s:ss,k:kk,B:math.comb(2*ss,ss)})
            assert actual==expected
            if ss>=13: assert actual[0,0]>0 and actual.det()>0
            numerical.append({'k':kk,'s':ss,'N':count,'A':actualA,'Gram':matjson(actual),
                              'determinant':str(actual.det()),'positive_if_s_at_least_13':bool(actual.det()>0)})
    save('tail-induction-checks.json',{'status':'PASS','normalization_denominator':str(den),
         'four_coefficients':cert,'independent_positive_pattern_compressions':numerical,
         'recurrence':'D_j(s+1)=((4s+2)/(s+1))*P_j(s+1)/P_j(s)*D_j(s)+G_j(s)/((s+1)*P_j(s))',
         'induction_valid_for':'all integer s>=13, all integer k>=2'})
    print(json.dumps({'tail_inductions':4,'tail_compressions':len(numerical),'status':'PASS'}),flush=True)

def main():
    start=time.time()
    for p in IN.iterdir():
        assert p.read_bytes()==(ROOT.parent/p.name).read_bytes()
    small_and_general_checks()
    tail_checks()
    save('audit-results.json',{'status':'PASS','input_hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(IN.iterdir())},
         'inputs_unchanged':all(p.read_bytes()==(ROOT.parent/p.name).read_bytes() for p in IN.iterdir()),
         'author_functions_imported':False,'arithmetic':'exact integers and rationals',
         'elapsed_seconds':round(time.time()-start,3),'new_score_assigned':False})
    print(json.dumps({'status':'PASS','elapsed_seconds':round(time.time()-start,3)}),flush=True)

if __name__=='__main__': main()
