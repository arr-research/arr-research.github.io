"""Review1031 controls. Fixed exact inputs; no optimization or score selection.
The accompanying prose supplies the general proof analysis, not these samples.
"""
from pathlib import Path
import sympy as s, json, traceback, time
ROOT=Path(__file__).resolve().parent
R=s.Rational; out={'scope':'Own fixed exact controls for manuscript1030','checks':[]}
def emit(name, **row):
    out['checks'].append(dict(name=name,**row))
    (ROOT/'OWN1031-v2.json').write_text(json.dumps(out,indent=2,default=str),encoding='utf-8')
    print(name,flush=True)
def zero(M): return all(s.simplify(x)==0 for x in M)
def hs(A,B): return s.simplify(s.trace(A.conjugate().T*B))
def syl(A,B,Z):
    n=A.rows
    K=s.kronecker_product(s.eye(n),A)+s.kronecker_product(B.T,s.eye(n))
    zv=s.Matrix([Z[i,j] for j in range(n) for i in range(n)])
    y=K.inv(method='DM')*zv
    Y=s.Matrix(n,n,lambda i,j:y[i+n*j])
    assert zero(A*Y+Y*B-Z)
    return hs(Z,Y)
def metric(A,Z): return 2*syl(A,A,Z)
def ptr(A,d,r): return s.Matrix(r,r,lambda i,j:sum(A[h*r+i,h*r+j] for h in range(d)))
def E(A,d,r): return s.kronecker_product(s.eye(d)/d,ptr(A,d,r))
def positive(A):
    L,D=A.LDLdecomposition(hermitian=True)
    assert zero(L*D*L.conjugate().T-A)
    piv=[s.simplify(D[i,i]) for i in range(A.rows)]
    assert all(x>0 for x in piv)
    return list(map(str,piv))
try:
    # Derive the rank-two aligned-plane limit by a 2x2 inverse identity,
    # without the supplied three-variable Sylvester solve.
    d,e,p=s.symbols('d e p',positive=True);m=d-1;q=1+m*e**2;cap=d*(d+1)/2
    W=s.Matrix([[1+m*p,d*p*e*s.sqrt(m)],[d*p*e*s.sqrt(m),(2+(d*m-2)*p)*e**2]])/(2*d*q)
    T=s.Matrix([[0,s.sqrt(m)],[s.sqrt(m),2*e*m]])
    Y=(T+W.det()*W.inv()*T*W.inv())/s.trace(W)
    assert zero(W*Y+Y*W-2*T)
    G=s.factor(s.trace(T*Y));lim=s.factor(s.limit(G,e,0)/(8*m))
    assert s.factor(lim-cap/(1+(cap-1)*p))==0
    A=1+m*p;B=d*p*s.sqrt(m);C=2+(d*m-2)*p
    assert s.factor(A*C-B**2-2*(1-p)*(1+(cap-1)*p))==0
    assert s.factor(C-2*d*m*p+A*m-(m+2)*(1-p))==0
    emit('general_ranktwo_symbolic_limit',G=str(G),normalized_limit=str(lim),sylvester_residual_zero=True,limiting_system_determinant=str(s.factor(A*C-B**2)),domain='d integer >=2; -1/(L_d-1)<p<1. Physical p=lambda*theta lies strictly in this interval.')

    # Exact signed-normal-form invariance with genuinely complex unitaries.
    I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Yp=s.Matrix([[0,-s.I],[s.I,0]]);Zp=s.diag(1,-1)
    Us=[s.kronecker_product(P,s.eye(3)) for P in [I,X,Yp,Zp]]
    weights=[R(1,10),R(2,10),R(3,10),R(4,10)]
    N=lambda A:sum((w*U*A*U.conjugate().T for w,U in zip(weights,Us)),s.zeros(6))
    ee=R(1,20);xi=R(1,10**7);tt=R(1,10**9)
    a=s.Matrix([1,0,0,0,ee,0]);b=s.Matrix([0,ee,0,0,0,1])
    sig=(1-xi)*(a*a.T+b*b.T)/(2*(1+ee**2))+xi*s.eye(6)/6
    D=s.zeros(6)
    for i,j,v in [(0,4,1),(4,0,1),(4,4,2*ee),(1,1,-2*ee),(1,5,-1),(5,1,-1)]:D[i,j]=v
    pre=(3*I+4*s.I*Yp)/5;post=(5*I+12*s.I*X)/13
    VR=s.Matrix([[R(3,5),R(4,5)*s.I,0],[R(4,5)*s.I,R(3,5),0],[0,0,1]])
    Pin=s.kronecker_product(pre.conjugate().T,VR);Pout=s.kronecker_product(post,VR)
    assert zero(Pin.conjugate().T*Pin-s.eye(6)) and zero(Pout.conjugate().T*Pout-s.eye(6))
    rsig=Pin*sig*Pin.conjugate().T;rd=Pin*D*Pin.conjugate().T
    os=Pout*N(sig)*Pout.conjugate().T;od=Pout*N(D)*Pout.conjugate().T
    assert zero(ptr(rd,2,3))
    g0=metric(sig,D);g1=metric(N(sig),N(D));rg0=metric(rsig,rd);rg1=metric(os,od)
    assert g0==rg0 and g1==rg1
    h=1-16/sum(1/w for w in weights);ratio=s.factor(g1/g0)
    assert h==R(29,125) and 0<ratio<h
    rho=rsig+tt*rd;orr=os+tt*od
    pivots={n:positive(M) for n,M in [('sigma',rsig),('rho',rho),('out_sigma',os),('out_rho',orr)]}
    tri=s.factor(syl(orr,os,tt*od)/syl(rho,rsig,tt*rd));assert 0<tri<h
    bell=s.Matrix([1,0,0,1]);J=sum((w*s.kronecker_product(post*P*pre,I)*bell*bell.T*s.kronecker_product(post*P*pre,I).conjugate().T/2 for w,P in zip(weights,[I,X,Yp,Zp])),s.zeros(4))
    assert s.trace(J)==1 and s.factor(1-16/s.trace(J.inv()))==h
    assert s.factor(1-8/s.trace((2*J).inv()))==h
    emit('complex_pre_post_and_reference_invariance',weights=list(map(str,weights)),epsilon=str(ee),xi=str(xi),t=str(tt),full_sylvester_size=36,input_form=str(g0),output_form=str(g1),ratio=str(ratio),triangular_ratio=str(tri),sharp_bound=str(h),invariance_exact=True,normalized_and_unnormalized_choi_exact=True,LDL_pivots=pivots)

    # Two noncommuting complex finite states with an exact common marginal.
    H=s.kronecker_product(X,s.diag(1,-1,0))+s.kronecker_product(Zp,s.Matrix([[0,s.I,0],[-s.I,0,0],[0,0,0]]))
    F=s.kronecker_product(Yp,s.diag(1,0,-1))+s.kronecker_product(X,s.Matrix([[0,0,1],[0,0,0],[1,0,0]]))
    sig=s.eye(6)/6+H/100;rho=sig+F/200;D=rho-sig;budget=R(3,2);lam=-R(1,3)
    assert ptr(sig,2,3)==ptr(rho,2,3)==s.eye(3)/3 and not zero(sig*rho-rho*sig)
    dep=lambda A:lam*A+(1-lam)*E(A,2,3)
    ns=dep(sig);nr=dep(rho);nd=nr-ns;bound=lam**2*budget/(1+lam*(budget-1))
    pivots={n:positive(M) for n,M in [('sigma',sig),('rho',rho),('out_sigma',ns),('out_rho',nr),('slack_sigma',budget*s.eye(6)/6-sig),('slack_rho',budget*s.eye(6)/6-rho)]}
    rows=[]
    for ss in [0,R(1,7),1,7]:
        tin=syl(rho,ss*sig,D);tout=syl(nr,ss*ns,nd);rr=s.factor(tout/tin)
        assert 0<rr<bound;rows.append({'resolvent_t':str(ss),'ratio':str(rr),'upper':str(bound)})
    quadratic=s.factor(hs(nd,nd*ns.inv())/hs(D,D*sig.inv()));assert quadratic<bound
    assert s.factor(s.trace(rho*rho*sig.inv())-1-hs(D,D*sig.inv()))==0
    emit('complex_noncommuting_order_upper_negative_noise',lambda_=str(lam),kappa=str(budget),rows=rows,quadratic_endpoint_ratio=str(quadratic),LDL_pivots=pivots)

    # Exact adverse controls for shortcuts, all retained.
    sig=s.diag(9,1,1,9)/20;D=s.zeros(4);D[0,3]=D[3,0]=1
    lam=-R(1,3);dep=lambda A:lam*A+(1-lam)*E(A,2,2)
    classical_base_ratio=s.factor(metric(dep(sig),dep(D))/metric(sig,D))
    assert classical_base_ratio==R(3,11)>R(1,9)
    assert R(3,8)<R(2,5)
    assert R(1,4)<R(3,10)
    emit('adverse_quantifier_controls',classical_base_only=str(classical_base_ratio),fixed_reference_R1_d3_upper='3/8 < 2/5',pinching_index_only='1/4 < 3/10',nonpositive_raw_c='lambda=-1/3,kappa=5 gives c=-1/15; cannot invert as positive bound',scope='These refute stronger readings, not the stated manuscript theorems.')
    out['all_passed']=True
except Exception:
    out['all_passed']=False;out['exception']=traceback.format_exc();print(out['exception'],flush=True)
    raise
finally:
    out['sympy']=s.__version__
    (ROOT/'OWN1031-v2.json').write_text(json.dumps(out,indent=2,default=str),encoding='utf-8')
