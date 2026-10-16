"""Finite checks supporting, but not replacing, the all-dimension proofs."""
from pathlib import Path
import json, itertools, hashlib, datetime
import numpy as np
import sympy as sp

ROOT=Path(__file__).parent
rng=np.random.default_rng(16102026)
A=[sp.Matrix(3,3,lambda a,b:sp.LeviCivita(i,a,b)) for i in range(3)]
K=[x/sp.sqrt(2) for x in A]
for i,j,k,l in itertools.product(range(3),repeat=4):
    expected=sp.Rational(int(i==j)*int(k==l)+int(i==l)*int(j==k),4)
    assert sp.simplify(sp.trace(K[i].H*K[j]*K[k].H*K[l])-expected)==0
H3=sum((sp.kronecker_product(x,x) for x in K),sp.zeros(9))
assert H3.det()==-sp.Rational(1,256)
assert (H3.H*H3).eigenvals()=={sp.Integer(1):1,sp.Rational(1,4):8}
pauli=[sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-sp.I],[sp.I,0]]),sp.diag(1,-1)]
H2=sum((sp.kronecker_product(K[i],pauli[i]/sp.sqrt(3)) for i in range(3)),sp.zeros(6))
assert (H2.H*H2).eigenvals()=={sp.Rational(2,3):2,sp.Rational(1,6):4}
x=sp.symbols('x',positive=True);u=sp.Rational(3,4)
q=sp.log(u)+(x-u)/u+(sp.log(4)-3)/(3-u)**2*(x-u)**2
assert sp.simplify(q.subs(x,u)-sp.log(u))==0
assert sp.simplify(sp.diff(q,x).subs(x,u)-1/u)==0
assert sp.simplify(q.subs(x,3)-sp.log(3))==0
poly=sp.Poly(q,x)
mean=poly.nth(0)+poly.nth(1)+sp.Rational(3,2)*poly.nth(2)
assert sp.simplify(mean-sp.log(u)-sp.log(4)/9)==0
grid=np.unique(np.r_[np.geomspace(1e-8,3,20000),.75,3])
gap=sp.lambdify(x,q-sp.log(x),'numpy')(grid)
assert gap.min()>-1e-12

def cmat(n,m): return rng.normal(size=(n,m))+1j*rng.normal(size=(n,m))
def amplified(ks,ys): return sum(np.kron(k,y) for k,y in zip(ks,ys))
def energy(ys): return sum(np.vdot(y,y).real for y in ys)/ys[0].shape[0]
def detvalue(h):
    sign,ld=np.linalg.slogdet(h)
    return float(np.exp(2*ld/h.shape[0])) if abs(sign)>0 else 0.
ks=[np.array(z,dtype=complex) for z in K]
B=2**(2/9)/4;b2=1/(3*2**(1/3))
random_cases=[]
for m in range(1,9):
    values=[]
    for _ in range(40):
        ys=[cmat(m,m) for _ in range(3)];en=energy(ys)
        ys=[y/np.sqrt(en) for y in ys]
        value=detvalue(amplified(ks,ys))
        assert value<=B+1e-12
        values.append(value)
    random_cases.append({'m':m,'cases':len(values),'largest_sample':max(values)})

ys2=[np.array(z,dtype=complex)/np.sqrt(3) for z in pauli]
ys3=ks
direct=[]
for m in range(2,21):
    residue={0:0,2:2,1:4}[m%3]
    blocks=[ys3]*((m-residue)//3)+[ys2]*(residue//2)
    ys=[]
    for i in range(3):
        yi=np.zeros((m,m),complex);off=0
        for block in blocks:
            size=block[i].shape[0];yi[off:off+size,off:off+size]=block[i];off+=size
        ys.append(yi)
    h=amplified(ks,ys);v=detvalue(h);expected=B*(b2/B)**(residue/m)
    assert abs(v-expected)<1e-12
    assert abs(energy(ys)-1)<1e-12
    direct.append({'m':m,'value':v,'expected':expected})

def noise_check(ks,ys,rank):
    d=ks[0].shape[0];m=ys[0].shape[0];n=d*m
    ys=[y/np.sqrt(energy(ys)) for y in ys]
    aa=amplified(ks,ys);uu,sv,vh=np.linalg.svd(aa)
    assert np.sum(sv>1e-9)==rank
    theta=1-rank/n;p=rank/n
    if theta>0:
        bb=uu[:,rank:]@vh[rank:,:]/(d*np.sqrt(theta))
        assert abs(d*np.linalg.norm(bb,'fro')**2/m-1)<1e-10
    result=[]
    for eps in [1e-8,1e-6,1e-4,.01,.1,.5]:
        if theta>0:
            hh=np.sqrt((1-eps)*p)*aa+np.sqrt(eps*theta)*bb
            expected=np.exp(p*np.log((1-eps)*p)+2*np.log(sv[:rank]).sum()/n+theta*np.log(eps/d**2))
            upper=(1/(1-theta))**(1-theta)*(eps/(d*d*theta))**theta
        else:
            hh=np.sqrt(1-eps)*aa;expected=(1-eps)*detvalue(aa);upper=1.
        actual=detvalue(hh)
        assert abs(actual-expected)<=max(1e-12,expected*1e-8)
        assert actual<=upper+1e-12
        result.append({'eps':eps,'value':actual,'witness_formula':expected,'upper':upper})
    return {'d':d,'m':m,'rank':rank,'theta':theta,'checks':result}

noise=[]
noise.append(noise_check(ks,[np.array([[1.]]),np.array([[0.]]),np.array([[0.]])],2))
noise.append(noise_check(ks,ys2,6))
noise.append(noise_check(ks,ys3,9))
replacer=[]
for d in range(2,7):
    kr=[]
    for j in range(d):
        kk=np.zeros((d,d));kk[0,j]=1;kr.append(kk)
    for m in [1,2,3]:
        yy=[np.eye(m)]+[np.zeros((m,m)) for _ in range(d-1)]
        noise.append(noise_check(kr,yy,m))
        for eps in [1e-8,1e-5,.01,.5]:
            rhos=np.r_[1-eps+eps/d,np.repeat(eps/d,d-1)]
            hh=np.kron(np.diag(np.sqrt(rhos)),np.eye(m))/np.sqrt(d)
            expected=np.exp(np.log(rhos).mean())/d
            assert abs(detvalue(hh)-expected)<1e-12
            replacer.append({'d':d,'m':m,'eps':eps,'value':expected})

out={'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'seed':16102026,'symbolic_fourth_order_identities':81,
 'exact_H3_determinant':'-1/256','exact_H3_squared_singular_values':{'1':1,'1/4':8},
 'exact_H2_squared_singular_values':{'2/3':2,'1/6':4},
 'symbolic_log_majorant_interpolation_and_moment':True,
 'majorant_grid_points':len(grid),'majorant_grid_minimum':float(gap.min()),
 'random_W3_cases':random_cases,'direct_sum_witnesses':direct,
 'noise_witnesses':noise,'pure_replacer_checks':replacer,'passed':True,
 'scope':'Finite checks and exact identities only; general bounds and priority require analytic arguments and literature review.'}
(ROOT/'verification-sharp-noise.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'trace_identities':81,'random_tuples':320,'direct_sum_witnesses':len(direct),'noise_tests':sum(len(z['checks']) for z in noise),'replacer_tests':len(replacer)}))
