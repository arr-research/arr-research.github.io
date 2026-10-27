from pathlib import Path
import sympy as s,mpmath as mp,json
p=Path(__file__).parent;e=s.symbols('e',positive=True);l=s.symbols('l',positive=True)
a=s.Matrix([1,0,0,0,e,0]);b=s.Matrix([0,e,0,0,0,1]);sigma=(a*a.T+b*b.T)/(2*(1+e*e));P=2*sigma;Q=s.eye(6)-P
Z=s.Matrix([[0,-1],[-1,-2*e]]);J=s.Matrix([[0,1],[1,0]]);D=s.zeros(6)
for ids,z in [([0,4],Z),([1,5],-J*Z*J)]:
    for i in range(2):
        for j in range(2):D[ids[i],ids[j]]=z[i,j]
pt=lambda x:s.Matrix(3,3,lambda i,j:sum(x[k*3+i,k*3+j] for k in range(2)))
assert s.simplify(P*P-P)==s.zeros(6)
assert pt(D)==s.zeros(3) and s.simplify(Q*D*Q)==s.zeros(6)
assert s.simplify(s.trace(D*D)-(4+8*e*e))==0
assert s.simplify(s.trace((P*D*P)**2)-8*e*e)==0
assert s.simplify(pt(sigma)-s.diag(1,2*e*e,1)/(2*(1+e*e)))==s.zeros(3)
N=lambda x:l*x+(1-l)*s.kronecker_product(s.eye(2)/2,pt(x))
W=s.Matrix([[1+l,2*l*e],[2*l*e,2*e*e]])/(4*(1+e*e))
assert s.simplify(N(sigma).extract([0,4],[0,4])-W)==s.zeros(2)
assert s.simplify(N(D)-l*D)==s.zeros(6)
w0=(1+3*l)/4;w=(1-l)/4
assert s.simplify(1-16/(1/w0+3/w)-3*l*l/(1+2*l))==0
mp.mp.dps=75
def form(a,b,z):
    # Row-major vectorization; aY+Yb=z on two-by-two real matrices.
    mat=mp.matrix(4);v=mp.matrix(4,1)
    for i in range(2):
        for j in range(2):
            row=2*i+j;v[row]=z[i,j]
            for k in range(2):mat[row,2*k+j]+=a[i,k];mat[row,2*i+k]+=b[k,j]
    y=mp.lu_solve(mat,v)
    return sum(z[i,j]*y[2*i+j] for i in range(2) for j in range(2))
rows=[]
for ev in ['.5','.1','.03']:
    ep=mp.mpf(ev);delta=ep**6/10;t=delta/100;z=mp.matrix([[0,-1],[-1,-2*ep]])
    S=(mp.matrix([[1,ep],[ep,ep**2]])/(2*(1+ep**2)))*(1-delta)+delta*mp.eye(2)/6
    for lv in ['.2','.5','.8']:
        lam=mp.mpf(lv);W=(mp.matrix([[1+lam,2*lam*ep],[2*lam*ep,2*ep**2]])/(4*(1+ep**2)))*(1-delta)+delta*mp.eye(2)/6
        din=form(S+t*z,S,z)+form(S-t*z,S,z)
        dout=lam**2*(form(W+lam*t*z,W,z)+form(W-lam*t*z,W,z))
        ratio=dout/din;limit=3*lam**2/(1+2*lam)
        tangent=lam**2*(4*ep**2*lam+2*ep**2+3*lam+3)/((2*lam+1)*(2*ep**2+lam+1))
        # Positivity of full rho follows deltaI/6 and t||D|| <=t||D||F<delta/6.
        assert t*mp.sqrt(4+8*ep**2)<delta/6
        assert 0<ratio<limit and abs(ratio-tangent)<delta*100
        rows.append(dict(epsilon=ev,lambda_value=lv,regularization=mp.nstr(delta,30),pair_step=mp.nstr(t,30),finite_pair_ratio=mp.nstr(ratio,65),boundary_tangent_formula=mp.nstr(tangent,65),supremum_candidate=mp.nstr(limit,65)))
result=dict(exact_symbolic_identities=9,high_precision_finite_pairs=len(rows),decimal_digits=75,failures=0,scope='Symbolic projector/tangent/channel identities plus bounded2x2 finite-pair controls; not independent review, Lean formalization or worldwide novelty certificate.',rows=rows)
(p/'VERIFY993.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
