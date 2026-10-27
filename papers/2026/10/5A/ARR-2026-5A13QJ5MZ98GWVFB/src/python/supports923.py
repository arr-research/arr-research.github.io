import json,pathlib,math
import numpy as np
import scipy.linalg as la
out=pathlib.Path(__file__).resolve().parent
rng=np.random.default_rng(92317)
def g(s,y):
    w,u=la.eigh(s);yy=u.conj().T@y@u;ans=0.
    for i,a in enumerate(w):
        for j,b in enumerate(w):
            if min(a,b)<1e-13:
                assert abs(yy[i,j])<1e-10
                continue
            ell=1/a if abs(a-b)<1e-12*a else math.log(a/b)/(a-b)
            ans+=abs(yy[i,j])**2*ell
    return ans
def rel(r,s):
    w,u=la.eigh(r);v,z=la.eigh(s);ds=(z.conj().T@r@z).diagonal().real
    assert sum(abs(ds[i]) for i,x in enumerate(v) if x<1e-13)<1e-10
    return sum(x*math.log(x) for x in w if x>1e-13)-sum(ds[i]*math.log(x) for i,x in enumerate(v) if x>1e-13)
def ch(k,x):return sum(a@x@a.conj().T for a in k)
def ad(p):return [np.kron(np.diag([1,math.sqrt(1-p)]),np.eye(2)),np.kron(np.array([[0,math.sqrt(p)],[0,0]]),np.eye(2))]
checks=[]
j=np.kron(np.array([[0,1],[0,0]]),np.eye(2));M=ad(.25)
for case in range(20):
    z=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4));s=z@z.conj().T+np.eye(4);s=s/np.trace(s);S=ch(M,s)
    z=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4));Z=z+z.conj().T;QZ=j@Z@j.conj().T;QS=j@S@j.conj().T
    v=[g(S,QZ),3*g(QS,QZ),3*g(S,Z)]
    checks.append({'case':case,'values_gS_QZ_c_gQS_QZ_c_gS_Z':v,'passed':bool(v[0]<=v[1]+1e-9 and v[1]<=v[2]+1e-9)})
# Singular S and exactly zero failure flag. Phi=Ad_P, on a two-dimensional support.
P=np.diag([1,1,0,0]);S=np.diag([.6,.4,0,0]);Y=np.array([[.3,.2j,0,0],[-.2j,-.1,0,0],[0,0,0,0],[0,0,0,0]])
flag={'Tr_ES':float(np.trace((np.eye(4)-P)@S)),'Tr_EY':float(np.trace((np.eye(4)-P)@Y).real),'g_before':g(S,Y),'g_after':g(P@S@P,P@Y@P)}
# Supported rank-two pair, singular outputs of rank three; convergence under common regularization.
sig=np.diag([.4,0,0,.6]);rho=np.diag([.3,0,0,.7]).astype(complex);rho[0,3]=rho[3,0]=.1
M=ad(.25);N=ad(.5);lam=1-math.sqrt(3)/2
rr=[]
for delta in [0,.01,.0001,.000001]:
    r=(1-delta)*rho+delta*np.eye(4)/4;s=(1-delta)*sig+delta*np.eye(4)/4
    dm=rel(ch(M,r),ch(M,s));dn=rel(ch(N,r),ch(N,s))
    rr.append({'delta':delta,'D_M':dm,'D_N':dn,'ratio':dn/dm,'passed':bool(dn>=lam*dm)})
report={'Qnorm_singular_image':checks,'zero_failure_block':flag,'singular_supported_pair':rr,'status':'PASS' if all(x['passed'] for x in checks+rr) and flag['Tr_ES']==flag['Tr_EY']==0 and abs(flag['g_before']-flag['g_after'])<1e-12 else 'FAIL'}
(out/'SUPPORTS923.json').write_text(json.dumps(report,indent=2),encoding='utf-8');print(json.dumps({'status':report['status'],'Qnorm_checks':len(checks),'flag':flag,'supported_pairs':rr},indent=2))
