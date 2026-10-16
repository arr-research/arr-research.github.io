"""Independent mathematical audit; no author code imported. Outputs beside this file."""
from pathlib import Path
import sys, json, hashlib, itertools as it, math, time
sys.path.insert(0,'C:/Users/lluis/AppData/Roaming/Python/Python312/site-packages')
import numpy as np
import sympy as sp
ROOT=Path(__file__).resolve().parent
SOURCE=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'source-reviewed-snapshot.tex'
rng=np.random.default_rng(1602026)
start=time.time()
report={'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'seed':1602026,'scope':'Independent finite checks supplement analytic review; not general proof certification.'}
# Independent permutation construction of the accepting block; no Gaussian identity used.
characters={1:{(1,):{(1,):1}},2:{(2,):{(1,1):1,(2,):1},(1,1):{(1,1):1,(2,):-1}},3:{(3,):{(1,1,1):1,(2,1):1,(3,):1},(2,1):{(1,1,1):2,(2,1):0,(3,):-1},(1,1,1):{(1,1,1):1,(2,1):-1,(3,):1}},4:{(4,):{(1,1,1,1):1,(2,1,1):1,(2,2):1,(3,1):1,(4,):1},(3,1):{(1,1,1,1):3,(2,1,1):1,(2,2):-1,(3,1):0,(4,):-1},(2,2):{(1,1,1,1):2,(2,1,1):0,(2,2):2,(3,1):-1,(4,):0}}}
def ctype(p):
    seen=set(); lengths=[]
    for i in range(len(p)):
        if i not in seen:
            j=i; count=0
            while j not in seen: seen.add(j); count+=1; j=p[j]
            lengths.append(count)
    return tuple(sorted(lengths,reverse=True))
def make_blocks(d,n):
    words=list(it.product(range(d),repeat=n)); lookup={w:i for i,w in enumerate(words)}
    permutations=list(it.permutations(range(n)))
    maps=[np.array([lookup[tuple(w[p[i]] for i in range(n))] for w in words]) for p in permutations]
    blocks={}
    for lam,ch in characters[n].items():
        if len(lam)>d: continue
        m=ch[(1,)*n]; P=sum(ch[ctype(p)]*np.eye(d**n)[idx] for p,idx in zip(permutations,maps))*m/math.factorial(n)
        q=round(np.trace(P).real/m)
        assert np.linalg.norm(P@P-P)<1e-10
        blocks[lam]=(P,q,m)
    assert np.linalg.norm(sum(v[0] for v in blocks.values())-np.eye(d**n))<1e-10
    return maps,blocks
def direct(K,n):
    d=K[0].shape[0]; maps,blocks=make_blocks(d,n); ans={lam:0. for lam in blocks}
    for inds in it.product(range(len(K)),repeat=n):
        A=np.array([[1.]])
        for j in inds: A=np.kron(A,K[j])
        avg=sum(A[np.ix_(idx,idx)] for idx in maps)/len(maps)
        for lam,(P,q,m) in blocks.items(): ans[lam]+=float(np.linalg.norm(P@avg@P)**2/(q*m))
    return ans
# Homogeneous complex-Gaussian moments computed from coefficient dictionaries of minors.
def pmul(a,b):
    c={}
    for i,x in a.items():
        for j,y in b.items():
            t=tuple(v+w for v,w in zip(i,j)); c[t]=c.get(t,0)+x*y
    return c
def padd(a,b,scale=1):
    c=a.copy()
    for i,x in b.items(): c[i]=c.get(i,0)+scale*x
    return c
def detpoly(K,rows,cols):
    k=len(K); z=(0,)*k; out={}
    for p in it.permutations(range(len(rows))):
        sign=(-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
        term={z:complex(sign)}
        for i,j in enumerate(p):
            entry={tuple(int(v==a) for v in range(k)):K[a][rows[i],cols[j]] for a in range(k)}
            term=pmul(term,entry)
        out=padd(out,term)
    return out
def moment(p): return sum(abs(v)**2*math.prod(math.factorial(x) for x in key) for key,v in p.items())
def balanced_moment(K,n):
    d=K[0].shape[0]; a,r=divmod(n,d); dp=detpoly(K,tuple(range(d)),tuple(range(d))); power={(0,)*len(K):1.}
    for _ in range(a): power=pmul(power,dp)
    total=0.
    for rows in it.combinations(range(d),r):
        for cols in it.combinations(range(d),r): total+=moment(pmul(power,detpoly(K,rows,cols)))
    return float(total/math.factorial(n)/math.comb(d,r))
def random_channel(d,k):
    Z=rng.normal(size=(k*d,d))+1j*rng.normal(size=(k*d,d)); Q=np.linalg.qr(Z)[0]
    return [Q[j*d:(j+1)*d] for j in range(k)]
def depol(d): return [np.eye(d)[:,i:i+1]@np.eye(d)[j:j+1,:]/np.sqrt(d) for i in range(d) for j in range(d)]
def replacer(d): return [np.eye(d)[:,0:1]@np.eye(d)[j:j+1,:] for j in range(d)]
def wh(d):
    ans=[]
    for i in range(d):
        for j in range(i+1,d):
            A=np.zeros((d,d)); A[i,j]=1; A[j,i]=-1; ans.append(A/np.sqrt(d-1))
    return ans
cases=[]
for d,maxn in [(2,4),(3,3)]:
    channels=[('unitary',random_channel(d,1)),('depolarizing',depol(d)),('pure_replacer',replacer(d)),('werner_holevo',wh(d))]
    for k in [2,3]:
        for rep in range(3): channels.append((f'random_rank{k}_{rep}',random_channel(d,k)))
    for name,K in channels:
        assert np.linalg.norm(sum(A.conj().T@A for A in K)-np.eye(d))<1e-10
        for n in range(1,maxn+1):
            vals=direct(K,n); a,r=divmod(n,d); lam=tuple([a+1]*r+[a]*(d-r)); lam=tuple(x for x in lam if x)
            gauss=balanced_moment(K,n); actual=vals[lam]
            assert abs(actual-gauss)<1e-10,(name,d,n,actual,gauss)
            assert actual<=min(vals.values())+1e-10
            if name=='unitary': assert abs(actual-1)<1e-10
            if name=='pure_replacer' and n>=2: assert abs(actual)<1e-10
            if name=='werner_holevo' and d==3 and n==3: assert abs(actual)<1e-10
            if name=='depolarizing':
                _,bl=make_blocks(d,n); P,q,m=bl[lam]; assert abs(actual-q/(d**n*m))<1e-10
            cases.append({'channel':name,'d':d,'n':n,'balanced':actual,'moment':gauss,'all_blocks':{str(l):v for l,v in vals.items()}})
report['block_checks']={'count':len(cases),'max_gaussian_residual':max(abs(c['balanced']-c['moment']) for c in cases),'cases':cases}
print('BLOCK CHECKS PASS',len(cases),flush=True)
# Qubit spectrum and finite bounds; spin flip evaluated by Hermitian positive square roots.
Y=np.array([[0,-1j],[1j,0]]); YY=np.kron(Y,Y); spectrum_checks=[]
for k in [1,2,3,4]:
    for rep in range(5):
        K=random_channel(2,k); C=np.empty((k,k),complex)
        for i in range(k):
            for j in range(k): C[i,j]=np.linalg.det(K[i]) if i==j else (np.linalg.det(K[i]+K[j])-np.linalg.det(K[i])-np.linalg.det(K[j]))/2
        sigma=np.sort(np.linalg.svd(C,compute_uv=False))[::-1]; delta=float(sigma[0])
        V=np.column_stack([A.reshape(-1)/np.sqrt(2) for A in K]); omega=V@V.conj().T
        ev,U=np.linalg.eigh(omega); root=(U*np.sqrt(np.maximum(ev,0)))@U.conj().T
        M=root@YY@omega.conj()@YY@root; roots=np.sqrt(np.maximum(np.linalg.eigvalsh((M+M.conj().T)/2),0))[::-1]
        resid=float(np.max(abs(np.pad(sigma,(0,4-k))-roots)))
        assert resid<3e-8,resid
        for n in range(1,9):
            b=balanced_moment(K,n); r=n%2; upper=math.comb(n+k-1,k-1)*delta**(n-r)
            assert b>=delta**n-1e-10 and b<=upper+1e-10,(k,n,b,delta,upper)
            if n%2==0:
                a=n//2; coef=[1.]+[0.]*a
                for s in sigma:
                    piece=[math.comb(2*j,j)*s**(2*j) for j in range(a+1)]
                    coef=[sum(coef[i]*piece[j-i] for i in range(j+1)) for j in range(a+1)]
                formula=math.factorial(a)**2/math.factorial(n)*coef[a]
                assert abs(formula-b)<1e-10
        spectrum_checks.append({'rank':k,'spectrum_residual':resid,'delta':delta})
report['qubit_checks']={'channels':len(spectrum_checks),'query_numbers_per_channel':8,'max_spin_flip_residual':max(x['spectrum_residual'] for x in spectrum_checks),'cases':spectrum_checks}
print('QUBIT CHECKS PASS',flush=True)
# Exact full twelve-variable signed-minor identity and tensor-square diagonal identity.
x=sp.symbols('x0:12'); X=[sp.Matrix(2,2,x[4*i:4*i+4]) for i in range(3)]; zero=sp.zeros(2)
H=sp.BlockMatrix([[zero,X[0],X[1]],[-X[0],zero,X[2]],[-X[1],-X[2],zero]]).as_explicit()
W=sp.Matrix(3,4,x); minors={c:W[:,list(c)].det() for c in it.combinations(range(4),3)}
identity=minors[(0,1,3)]*minors[(0,2,3)]-minors[(0,1,2)]*minors[(1,2,3)]
exact=sp.expand(H.det(method='domain-ge')-identity); assert exact==0
A=[]
for i,j in [(0,1),(0,2),(1,2)]:
    M=sp.zeros(3); M[i,j]=1; M[j,i]=-1; A.append(M)
s=sp.symbols('s0:3'); T=sum((s[i]*sp.kronecker_product(A[i],A[i])/2 for i in range(3)),sp.zeros(9))
diagdet=sp.factor(T.det()); assert diagdet==-sp.prod(s)**3/256
I=sp.eye(2); XX=sp.Matrix([[0,1],[1,0]]); ZZ=sp.diag(1,-1)
Hsat=sum((sp.kronecker_product(A[i],B) for i,B in enumerate([I,XX,ZZ])),sp.zeros(6))
assert Hsat.det()==4
assert sorted(Hsat.singular_values())==[1,1,1,1,2,2]
report['symbolic']={'full_12_variable_minor_identity':True,'diagonal_tensor_square_determinant':str(diagdet),'saturator_unscaled_determinant':str(Hsat.det()),'saturator_singular_values':[1,1,1,1,2,2],'max_abs_det_six_dimensional':'1/3456','delta_six_dimensional':'2^(2/3)/24','delta_nine_dimensional':'2^(2/9)/12'}
print('SYMBOLIC CHECKS PASS',flush=True)
# Random complex checks test orientation/cross terms not visible at diagonal coefficients.
Afloat=[np.array(a).astype(complex) for a in A]; tensor_res=0.; minor_res=0.; maxdet=0.
for _ in range(150):
    Z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)); Z/=np.linalg.norm(Z)
    G=sum(Z[i,j]*np.kron(Afloat[i],Afloat[j])/2 for i in range(3) for j in range(3))
    tensor_res=max(tensor_res,abs(abs(np.linalg.det(G))-abs(np.linalg.det(Z))**3/256))
    Wn=rng.normal(size=(3,4))+1j*rng.normal(size=(3,4)); Wn/=np.linalg.norm(Wn)
    Hn=sum(np.kron(Afloat[i],Wn[i].reshape(2,2)) for i in range(3))
    pm={c:np.linalg.det(Wn[:,c]) for c in it.combinations(range(4),3)}
    det=np.linalg.det(Hn); rhs=pm[(0,1,3)]*pm[(0,2,3)]-pm[(0,1,2)]*pm[(1,2,3)]
    minor_res=max(minor_res,abs(det-rhs)); maxdet=max(maxdet,abs(det)); assert abs(det)<=1/54+1e-12
assert tensor_res<1e-12 and minor_res<1e-12
report['complex_tensor_checks']={'count_each':150,'tensor_square_max_residual':tensor_res,'minor_identity_max_residual':minor_res,'largest_random_abs_det_H':maxdet,'analytic_bound_H':1/54}
report['status']='PASS'; report['elapsed_seconds']=time.time()-start
(ROOT/'independent-checks.json').write_text(json.dumps(report,indent=2)+chr(10),encoding='utf-8')
print(json.dumps({'status':report['status'],'elapsed_seconds':report['elapsed_seconds'],'max_gaussian_residual':report['block_checks']['max_gaussian_residual'],'max_spin_flip_residual':report['qubit_checks']['max_spin_flip_residual'],'complex_tensor_checks':report['complex_tensor_checks']},indent=2))
