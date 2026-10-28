from pathlib import Path
import sympy as s,json
P=Path(__file__).parent;Q=s.Rational
# Own prior directed arithmetic is executed without writing bytecode.
ns={'__file__':str(P/'integer_arithmetic1093.py')};exec((P/'integer_arithmetic1093.py').read_text(),ns);iv=ns['iv'];log=ns['log'];saved=ns['saved']
U=s.Matrix([[Q(3,5),4*s.I/5,0],[4*s.I/5,Q(3,5),0],[0,0,1]]);assert U.conjugate().T*U==s.eye(3)
F=U*s.diag(Q(9,10),Q(1,2),Q(1,5))*U.conjugate().T;E=(F-Q(1,5)*s.eye(3))/Q(7,10)
assert sorted(E.eigenvals().keys())==[0,Q(3,7),1]
assert F==Q(9,10)*E+Q(1,5)*(s.eye(3)-E)
x=Q(4,7);h=Q(1,100);rows=[]
for eps in (Q(1,10),Q(1,100),Q(1,10000)):
 q=[(1-eps)*x+eps/3,eps/3,(1-eps)*(1-x)+eps/3];p=[q[0]+(1-eps)*h,q[1],q[2]-(1-eps)*h]
 sigma=U*s.diag(*q)*U.conjugate().T;rho=U*s.diag(*p)*U.conjugate().T
 qout=s.trace(F*sigma);pout=s.trace(F*rho)
 chiin=sum((aa-bb)**2/bb for aa,bb in zip(p,q));chiout=(pout-qout)**2/(qout*(1-qout));ratio=s.factor(chiout/chiin);assert 0<ratio<Q(1,2)
 rows.append({'epsilon':str(eps),'rho_eigenvalues':list(map(str,p)),'sigma_eigenvalues':list(map(str,q)),'pout':str(pout),'qout':str(qout),'minchi_and_localSLD_ratio_exact':str(ratio)})
eps=s.symbols('eps',positive=True);q0=(1-eps)*x+eps/3;q2=(1-eps)*(1-x)+eps/3;qo=Q(9,10)*q0+eps/6+Q(1,5)*q2;rr=Q(49,100)/(qo*(1-qo)*(1/q0+1/q2));assert s.limit(rr,eps,0)==Q(1,2)
# Exact outward finite Umegaki counterexample to49/99; faithful scalar pair.
p=x+h;q=x
kl=lambda a,b:iv(str(a))*log(iv(str(a/b)))+iv(str(1-a))*log(iv(str((1-a)/(1-b))))
din=kl(p,q);dout=kl(Q(1,5)+Q(7,10)*p,Q(1,5)+Q(7,10)*q);ret=dout/din;gap=ret-iv('49/99');assert gap.l>0
result={'POVM_F_exact':str(F),'POVM_E_exact':str(E),'factorization_exact':True,'faithful_regularization_cases':rows,'regularization_limit':'1/2','finite_Umegaki_old_guess_falsifier':{'p':str(p),'q':str(q),'ratio':saved(ret),'gap_over49_99':saved(gap),'gap_certified_positive':True},'arithmetic_lineage':'Own1077/1068/1054 primitives;1024bit dyadic,600term atanh, explicit tail; not independent arithmetic library','passed':True}
(P/'POVM_FINITE1093.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print('POVM exact factorization and faithful limit passed; Umegaki finite ratio',saved(ret)['decimal_display_only'][0])
