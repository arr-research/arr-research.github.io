"""Exact structural controls + bounded BKM diagnostics; not a proof by samples.
Writes a JSON artifact only when --output is explicitly supplied.
No network or project-state writes; stdout-only by default.
"""
from pathlib import Path
import json,hashlib,argparse
import sympy as s
import numpy as np
import mpmath as mp
F=s.Rational;root=Path(__file__).resolve().parent

def adks(p):return [s.diag(1,s.sqrt(1-p)),s.Matrix([[0,s.sqrt(p)],[0,0]])]
def apply(x,ks):return s.simplify(sum((k*x*k.H for k in ks),s.zeros(ks[0].rows)))
J=s.Matrix([[0,1],[0,0]]);Q=lambda x:J*x*J.H
exact=[]
for p1,p2 in [(F(1,4),F(1,2)),(F(1,10),F(9,10))]:
    s1,s2=1-p1,1-p2;d=p2-p1;a=d/s1;c=s1/p1
    f=s.diag(1,s.sqrt(s2/s1));k0=adks(p1)[0]
    for i in range(2):
      for j in range(2):
        e=s.zeros(2);e[i,j]=1;y=apply(e,adks(p1))
        assert s.simplify(apply(e,adks(p2))-f*(y+a*Q(y))*f)==s.zeros(2)
        assert s.simplify(c*y-Q(y)-c*k0*e*k0.H)==s.zeros(2)
        assert Q(Q(e))==s.zeros(2)
    L=s.simplify((s2/s1)/((1+a*c)*(1+a*s.sqrt(c))**2))
    assert L>0
    if p1==F(1,4):assert s.simplify(L-(1-s.sqrt(3)/2))==0
    else:assert L==F(1,1089) and a*s.sqrt(c)>1
    exact.append({'p1':str(p1),'p2':str(p2),'L':str(L),'a_sqrt_c':str(s.simplify(a*s.sqrt(c)))})

# Qutrit finite-height example: all CP identities checked on matrix units.
J3=s.Matrix([[0,1,0],[0,0,1],[0,0,0]]);q=lambda z:J3*z*J3.H
b=F(1,100);a=F(1,2);c=1/b
D=s.diag(1,1/s.sqrt(1+b),1/s.sqrt(1+b+b*b))
ff=s.diag(1,s.sqrt(1-a),s.sqrt(1-a+a*a))
mks=[D,s.sqrt(b)*J3*D,b*(J3**2)*D]
kks=[ff,s.sqrt(a)*ff*J3]
assert s.simplify(sum((k.H*k for k in mks),s.zeros(3)))==s.eye(3)
assert s.simplify(sum((k.H*k for k in kks),s.zeros(3)))==s.eye(3)
for i in range(3):
  for j in range(3):
    e=s.zeros(3);e[i,j]=1;y=apply(e,mks)
    assert q(q(q(e)))==s.zeros(3)
    assert s.simplify(c*y-q(y)-c*D*e*D)==s.zeros(3)
    assert s.simplify(apply(y,kks)-ff*(y+a*q(y))*ff)==s.zeros(3)
P=1+a*s.sqrt(c)+a*a*c;L3=s.simplify((1-a)/((1+a*c)*P**2))
assert P==31 and a*s.sqrt(c)==5 and L3==F(1,98022)

# Explicit rational separable witness states. Positivity and nonclassical R.
sx=s.Matrix([[0,1],[1,0]]);XX=s.kronecker_product(sx,sx)
witnesses=[]
for n in [3,4,5,8]:
    x=F(1,n);r=F(1,2**(n*n));eps=r/n**2
    SA=s.diag(1-x,x);SR=s.diag(1-r,r);S=s.kronecker_product(SA,SR)
    rho=S+eps*XX
    assert s.trace(rho)==1 and eps==min(S.diagonal())/n
    _,ldl=rho.LDLdecomposition(hermitian=False)
    assert all(ldl[i,i]>0 for i in range(4))
    pt=s.Matrix(4,4,lambda i,j:rho[2*(i//2)+(j%2),2*(j//2)+(i%2)])
    assert pt==rho
    assert rho*s.kronecker_product(s.eye(2),SR)!=s.kronecker_product(s.eye(2),SR)*rho
    t2=s.factor(eps**2/(x*(1-x)*r*(1-r)));assert 0<t2<1
    witnesses.append({'n':n,'reference_dimension':2,'positive_LDL':True,'PPT_equals_rho':True,
                      'nonclassical_R_commutator_nonzero':True,'separable_filter_parameter_squared':str(t2)})

# Finite float diagnostics test whole Hermitian tangent spaces at selected
# correlated base states, including nontraceless directions used by the proof.
rng=np.random.default_rng(91520261027)
def nks(ks):return [np.array(k.evalf(),dtype=complex) for k in ks]
def localks(ks,dr):return [np.kron(k,np.eye(dr)) for k in ks]
def na(x,ks):return sum((k@x@k.conj().T for k in ks),np.zeros((ks[0].shape[0],ks[0].shape[0]),complex))
def basis(n):
    out=[]
    for i in range(n):
      e=np.zeros((n,n),complex);e[i,i]=1;out.append(e)
    for i in range(n):
      for j in range(i+1,n):
        e=np.zeros((n,n),complex);e[i,j]=e[j,i]=1/np.sqrt(2);out.append(e)
        e=np.zeros((n,n),complex);e[i,j]=1j/np.sqrt(2);e[j,i]=-1j/np.sqrt(2);out.append(e)
    return out
def gram(S,images):
    vals,U=np.linalg.eigh(S);assert vals.min()>1e-12
    kernel=np.empty((len(vals),len(vals)))
    for i,aa in enumerate(vals):
      for j,bb in enumerate(vals):
        kernel[i,j]=1/aa if abs(aa-bb)<1e-12*max(aa,bb) else (np.log(aa)-np.log(bb))/(aa-bb)
    mats=np.array([U.conj().T@z@U for z in images])
    return np.einsum('iab,jab,ab->ij',mats.conj(),mats,kernel).real
diagnostics=[]
for label,db,dr,ks1,ks2,L in [
 ('AD1/4_to1/2',2,2,nks(adks(F(1,4))),nks(adks(F(1,2))),float(1-s.sqrt(3)/2)),
 ('AD1/10_to9/10',2,3,nks(adks(F(1,10))),nks(adks(F(9,10))),1/1089),
 ('qutrit_nilpotent3',3,2,nks(mks),[k2@k1 for k2 in nks(kks) for k1 in nks(mks)],1/98022)]:
    n=db*dr;bs=basis(n);k1=localks(ks1,dr);k2=localks(ks2,dr)
    for case in range(3):
      W=rng.integers(-3,4,(n,n))+1j*rng.integers(-3,4,(n,n));W=W+(n+2)*np.eye(n)
      S=W@W.conj().T;S=S/np.trace(S)
      g1=gram(na(S,k1),[na(z,k1) for z in bs]);g2=gram(na(S,k2),[na(z,k2) for z in bs])
      mine=float(np.linalg.eigvalsh((g2-L*g1+(g2-L*g1).T)/2).min())
      assert mine>-1e-8
      diagnostics.append({'channel':label,'R_dimension':dr,'case':case,'Hermitian_tangent_dimension':n*n,'min_eigenvalue_gN_minus_L_gM':mine})

# BKM ratio on the exact rational sequence, evaluated at70 digits only as
# a diagnostic of the analytically established asymptotic, not a proof.
mp.mp.dps=70
def ell(a,b):return 1/a if a==b else (mp.log(a)-mp.log(b))/(a-b)
ratios=[]
for n in [3,5,10,30,100]:
    x=mp.mpf(1)/n;r=mp.mpf(2)**(-n*n);ss=mp.mpf(1)/2;u=1-ss*x;vv=ss*x
    gi=2*(ell((1-x)*(1-r),x*r)+ell((1-x)*r,x*(1-r)))
    go=2*ss*(ell(u*(1-r),vv*r)+ell(u*r,vv*(1-r)))
    ratio=go/gi;lower=(mp.mpf(n-1)/(n+1))*ratio
    ratios.append({'n':n,'p':'1/2','BKM_ratio':str(ratio),'finite_MI_ratio_lower_bound':str(lower)})
assert mp.mpf(ratios[-1]['finite_MI_ratio_lower_bound'])>mp.mpf('0.97')

out={'passed':True,'sympy':s.__version__,'numpy':np.__version__,'mpmath':mp.__version__,
 'exact_AD_structural_controls':exact,'qutrit':{'k':3,'a_sqrt_c':'5','P_k':'31','L':'1/98022'},
 'exact_rational_witness_controls':witnesses,'metric_diagnostics':diagnostics,'diagnostic_tolerance':1e-8,
 'witness_diagnostic_precision_digits':70,'witness_diagnostics':ratios,
 'scope':'Exact algebraic controls and9 selected full-tangent numerical metric checks; universal theorem relies on PROOF914, not these samples. No novelty or model score.',
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path)
args=parser.parse_args()
if args.output:args.output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'AD_controls':exact,'qutrit_L':'1/98022','metric_bases_checked':len(diagnostics),
                  'last_witness_bound':ratios[-1],'scope':out['scope']},indent=2))
