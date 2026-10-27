"""Own finite adverse controls for exact PDF995; analytical review is separate.
No optimizer and no restarts to select successful samples. Exact Gaussian
rational arithmetic for resolvents, independent spectral evaluation for one
faithful 6x6 triangular-divergence pair.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,traceback
import sympy as s
from sympy.polys.matrices import DomainMatrix
import mpmath as mp

ROOT=Path(__file__).resolve().parent
R=s.Rational
records=[]
def canon(M): return M.applyfunc(s.expand)
def equal(A,B): return all(s.expand(x)==0 for x in A-B)
def real(x):
    x=s.expand(x)
    assert s.im(x)==0
    return s.re(x)
def pt(M,r): return s.Matrix(r,r,lambda i,j:M[i,j]+M[r+i,r+j])
def unitary_apply(U,M): return canon(U*M*U.H)
def channel(M,us,ws):
    return canon(sum((w*unitary_apply(u,M) for u,w in zip(us,ws)),s.zeros(M.rows)))
def sylvester_form(a,b,z):
    n=a.rows;Q=s.zeros(n*n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                Q[n*i+j,n*k+j]+=a[i,k]
                Q[n*i+j,n*i+k]+=b[k,j]
    vec=s.Matrix(list(z))
    dm=DomainMatrix.from_Matrix(canon(Q)).convert_to(s.QQ_I)
    y=dm.inv().to_Matrix()*vec
    return real((vec.H*y)[0])
def save():
    (ROOT/'CONTROLS998.json').write_text(json.dumps({'tests':records},indent=2)+'\n',encoding='utf-8')
def test(name,fn):
    try:
        ans=fn();records.append({'test':name,'status':'pass','result':ans})
    except Exception as exc:
        records.append({'test':name,'status':'FAIL','exception':repr(exc),'traceback':traceback.format_exc()})
    save();print(name+': '+records[-1]['status'],flush=True)

def exact_upper_controls():
    I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1)
    G=s.Matrix([[1,s.I,0,1],[0,1,1,0],[1,0,s.I,0],[0,1,0,1]])
    H=canon(5*s.eye(4)+G*G.H);sigma=H/s.trace(H)
    C=s.Matrix([[1,s.I],[1-s.I,2]])
    D=C.row_join(s.zeros(2))
    delta=s.zeros(4)
    for i in range(2):
        for j in range(2):delta[i,2+j]=C[i,j];delta[2+j,i]=s.conjugate(C[i,j])
    assert pt(delta,2)==s.zeros(2) and delta==delta.H
    step=R(1,1000);rho=sigma+step*delta
    floor=R(5,1)/s.trace(H)
    frob2=real(s.trace(delta*delta))
    assert floor**2>4*step**2*frob2 # rho >= floor/2 I.
    sets=[('pauli_depolarizing_half',[I,X,Y,Z],[R(5,8),R(1,8),R(1,8),R(1,8)]),
          ('pauli_nonuniform',[I,X,Y,Z],[R(1,2),R(1,3),R(1,10),R(1,15)]),
          ('involution_twirl',[I,Z],[R(2,7),R(5,7)])]
    out=[]
    for name,us0,ws in sets:
        us=[s.kronecker_product(u,I) for u in us0]
        assert sum(ws)==1
        twirl_delta=sum((unitary_apply(u,delta) for u in us),s.zeros(4))
        assert equal(twirl_delta,s.zeros(4))
        r_out,s_out,z_out=[channel(v,us,ws) for v in [rho,sigma,delta]]
        h=1-R(len(ws)**2,1)/sum(1/w for w in ws)
        for t in [R(0),R(1,5),R(1),R(5)]:
            fin=sylvester_form(rho,t*sigma,delta)
            fout=sylvester_form(r_out,t*s_out,z_out)
            assert fin>0 and fout>=0 and h*fin-fout>=0
            out.append({'channel':name,'generator':'(x-1)^2/(x+'+str(t)+')','h':str(h),
                        'ratio':str(fout/fin),'margin_positive':bool(h*fin-fout>0)})
        # Positive quadratic endpoint, Q=R_sigma.
        invs=DomainMatrix.from_Matrix(canon(sigma)).convert_to(s.QQ_I).inv().to_Matrix()
        invo=DomainMatrix.from_Matrix(canon(s_out)).convert_to(s.QQ_I).inv().to_Matrix()
        fin=real(s.trace(delta*delta*invs));fout=real(s.trace(z_out*z_out*invo))
        assert h*fin-fout>=0
        out.append({'channel':name,'generator':'(x-1)^2 endpoint','h':str(h),'ratio':str(fout/fin),
                    'margin_positive':bool(h*fin-fout>0)})
        print('  '+name+' five exact generators checked',flush=True)
    return {'cases':out,'complex_noncommuting':not equal(rho*sigma,sigma*rho),
            'faithfulness_certificate':'sigma >=5/Tr(H) I; step*||delta||F<floor/2',
            'scope':'15 finite rational controls, not a proof for all f or references'}

def faithful_boundary_algebra():
    e,xi=s.symbols('e xi',positive=True)
    a=s.Matrix([1,0,0,0,e,0]);b=s.Matrix([0,e,0,0,0,1]);sigma=(a*a.T+b*b.T)/(2*(1+e*e))
    P=2*sigma;K=s.eye(6)-P
    delta=s.zeros(6)
    z=s.Matrix([[0,-1],[-1,-2*e]]);J=s.Matrix([[0,1],[1,0]])
    for ids,block in [([0,4],z),([1,5],-J*z*J)]:
        for i in range(2):
            for j in range(2):delta[ids[i],ids[j]]=block[i,j]
    assert (K*delta*K).applyfunc(s.factor)==s.zeros(6)
    assert pt(delta,3)==s.zeros(3)
    ss=s.factor(s.trace((P*delta*P)**2));cross=s.factor(s.trace(delta**2)-ss)
    assert ss==8*e*e and cross==4
    pos=R(1,2)-xi/3;ker=xi/6
    form=ss/pos+2*cross/(pos+ker)
    assert s.simplify(s.limit(form,xi,0)-16*(1+e*e))==0
    # Scope check: xi>0 alone is not a sufficient global state condition.
    assert pos.subs(xi,R(8,5))<0
    return {'exact_regularized_input_form':str(s.factor(form)),
            'support_eigenvalue':str(pos),'kernel_eigenvalue':str(ker),
            'limit':str(s.factor(s.limit(form,xi,0))),
            'minor_text_precision':'Use 0<xi<1 (or sufficiently small xi); xi>0 alone includes nonstates, but the xi-down-to-zero proof is unaffected'}

def spectral_finite_pair():
    mp.mp.dps=90
    e=mp.mpf(1)/10;xi=mp.mpf(1)/10**7;step=xi/100;lam=mp.mpf(1)/2
    aa=mp.matrix([1,0,0,0,e,0]);bb=mp.matrix([0,e,0,0,0,1])
    S=(1-xi)*(aa*aa.T+bb*bb.T)/(2*(1+e*e))+xi*mp.eye(6)/6
    D=mp.matrix(6);z=mp.matrix([[0,-1],[-1,-2*e]]);j=mp.matrix([[0,1],[1,0]])
    for ids,block in [([0,4],z),([1,5],-j*z*j)]:
        for ii in range(2):
            for jj in range(2):D[ids[ii],ids[jj]]=block[ii,jj]
    def dep(M):
        ref=mp.matrix(3,3)
        for i in range(3):
            for k in range(3):ref[i,k]=M[i,k]+M[3+i,3+k]
        ans=lam*M
        for a in range(2):
            for i in range(3):
                for k in range(3):ans[3*a+i,3*a+k]+=(1-lam)*ref[i,k]/2
        return ans
    rho=S+step*D
    def form(A,B,T):
        va,ua=mp.eigsy(A);vb,ub=mp.eigsy(B)
        assert min(va)>0 and min(vb)>0
        C=ua.T*T*ub
        return sum(C[i,j]**2/(va[i]+vb[j]) for i in range(6) for j in range(6))
    fin=form(rho,S,D);fout=form(dep(rho),dep(S),lam*D)
    ratio=fout/fin;upper=3*lam**2/(1+2*lam)
    assert 0<ratio<upper
    saved=json.loads((ROOT/'reproduction'/'VERIFY993.json').read_text())
    refrow=next(row for row in saved['rows'] if row['epsilon']=='.1' and row['lambda_value']=='.5')
    discrepancy=abs(ratio-mp.mpf(refrow['finite_pair_ratio']))
    assert discrepancy<mp.mpf('1e-63')
    return {'method':'Independent full 6x6 spectral resolvent evaluation; 90 decimal digits',
            'ratio':mp.nstr(ratio,75),'target':'3/8','difference_from_supplied_block_calculation':mp.nstr(discrepancy,10),
            'finite_pair_divergence_input':mp.nstr(step**2*fin,30),
            'scope':'High precision diagnostic; exact finite certificate replay is separate'}

def scope_and_barrier():
    l,r=s.symbols('l r',positive=True)
    S=r*r/(l+(1-l)*r)+(1-r)/(1-l)
    h=s.factor(1-1/S)
    assert s.factor(h-l*l*(1-r)/(l+(1-2*l)*r))==0
    derivative=s.factor(s.diff(h,r))
    assert s.factor(derivative+l*l*(1-l)/(l+(1-2*l)*r)**2)==0
    for d in [2,3,5]:
        assert s.factor(h.subs(r,R(1,d*d))-(d*d-1)*l*l/(1+(d*d-2)*l))==0
    # Equal reference condition cannot be removed: both states are fixed.
    sigma=s.kronecker_product(s.eye(2)/2,s.diag(R(3,5),R(2,5)))
    rho=s.kronecker_product(s.eye(2)/2,s.diag(R(2,5),R(3,5)))
    dep=lambda M:M/2+s.kronecker_product(s.eye(2)/2,pt(M,2))/2
    assert dep(sigma)==sigma and dep(rho)==rho and pt(sigma,2)!=pt(rho,2)
    return {'scalar_method_h':str(h),'derivative':str(derivative),
            'dimensions_checked':[2,3,5],
            'outside_equal_reference_counterexample':'Faithful fixed product states with differing R marginals have ratio 1, so no <1 unrestricted extension'}

test('complex_exact_Petz_resolvents_and_endpoint',exact_upper_controls)
test('ordered_faithful_regularization',faithful_boundary_algebra)
test('full_matrix_spectral_finite_pair',spectral_finite_pair)
test('scalar_method_and_scope',scope_and_barrier)
output={'utc':datetime.now(timezone.utc).isoformat(),'tests':records,
        'failures':sum(x['status']!='pass' for x in records),'sympy':s.__version__,'mpmath':mp.__version__,
        'scope':'Own controls only for frozen995; no universal proof inferred from finite tests'}
(ROOT/'CONTROLS998.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'groups':len(records),'failures':output['failures']}))
raise SystemExit(bool(output['failures']))
