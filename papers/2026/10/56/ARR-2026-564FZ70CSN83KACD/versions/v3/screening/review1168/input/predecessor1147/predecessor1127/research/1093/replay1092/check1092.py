import json, pathlib, sympy as s
P=pathlib.Path(__file__).parent
Q=s.Rational; I=s.eye(2); a=Q(9,10);b=Q(1,5);delta=a-b;k=Q(1,2)
r=I/2
sigma0=s.Matrix([[Q(3,10),Q(1,50)],[Q(1,50),Q(1,10)]])
rho0=s.Matrix([[Q(1,10),s.I*Q(3,100)],[-s.I*Q(3,100),Q(1,5)]])
sigma=[sigma0,r-sigma0];rho=[rho0,r-rho0];z=rho0-sigma0
assert all(m==m.conjugate().T and m[0,0]>0 and m.det()>0 for m in sigma+rho)
assert rho0*sigma0!=sigma0*rho0
assert sum(rho,s.zeros(2))==sum(sigma,s.zeros(2))==r
x=s.symbols('x',real=True);q=b+delta*x
gap=s.factor(k-delta**2*x*(1-x)/(q*(1-q)))
assert s.simplify(gap-(7*x-4)**2/(2*(7*x+2)*(8-7*x)))==0
assert s.simplify((delta**2*x*(1-x)/(q*(1-q))).subs(x,Q(4,7)))==k
left=lambda m:s.kronecker_product(I,m)
right=lambda m:s.kronecker_product(m.T,I)
vec=s.Matrix([z[i,j] for j in range(2) for i in range(2)])
rows=[]
for label,t in [('resolvent0',Q(0)),('resolvent1third',Q(1,3)),('resolvent1',Q(1)),('resolvent5',Q(5)),('resolvent100',Q(100)),('quadratic',None),('SLD',None)]:
 if label=='quadratic':blocks=[right(m) for m in sigma]
 elif label=='SLD':blocks=[(left(m)+right(m))/2 for m in sigma]
 else:blocks=[left(p)+t*right(q) for p,q in zip(rho,sigma)]
 A,B=blocks
 inp=A.inv()+B.inv()
 out=delta**2*((a*A+b*B).inv()+((1-a)*A+(1-b)*B).inv())
 M=s.simplify(k*inp-out);assert M==M.conjugate().T
 minors=[s.factor(M[:j,:j].det()) for j in range(1,5)]
 assert all(v>0 for v in minors),(label,minors)
 ratio=s.factor((vec.conjugate().T*out*vec)[0]/(vec.conjugate().T*inp*vec)[0]);assert 0<ratio<k
 rows.append({'case':label,'ratio_exact':str(ratio),'gap_to_one_half':str(k-ratio),'all_four_leading_principal_minors_positive':True,'minors':[str(v) for v in minors]})
out={'status':'all exact fixed controls passed','binary_channel_columns':[['9/10','1/10'],['1/5','4/5']],'classical_coefficient':'1/2','maximizing_input_probability':'4/7','scalar_gap':str(gap),'reference_dimension':2,'rho_sigma_blocks_noncommuting':True,'joint_reference_marginal':'I_2/2','controls':rows,'scope':'Root-derived proof candidate and seven fixed exact operator controls, not external audit, formalization, exhaustive search or manuscript assessment; no publication priority claimed.'}
(P/'CONTROL1092.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'cases':len(rows),'full_operator_positive_checks':True,'classical_coefficient':'1/2'}))
