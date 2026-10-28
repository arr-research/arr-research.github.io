from pathlib import Path
import sympy as s,json,itertools,traceback
P=Path(__file__).parent;R=s.Rational;rows=[]
try:
 n,k,d=s.symbols('n k d',positive=True);b=1/(4*n*k);eps=b*d;a=1/n-(n-2)*eps-b;c2=a*b*(1-d);m=n-1;ap=(a+n*(n-2)*eps)/m**2;ep=(n*a+(n*n-3*n+1)*eps)/m**2
 identities={'input_det':s.simplify(a*b-c2-a*b*d)==0,'output_det':s.simplify(ap*b-c2/m**2-b*d*(a+n*(n-2)*b)/m**2)==0,'output_eval_at_epsilon':s.simplify((ap-eps)*(b-eps)-c2/m**2+eps*b*(1-d)/m**2)==0,'output_global_max':s.simplify(ep-ap-b-((a-eps)/m-b))==0,'reference_condition':s.simplify(n*(a+(n-2)*eps)/m/(n*b)-(4*k-1)/m)==0};assert all(identities.values())
 # Actual81x81 HS map, independent of candidate spectra; column-vector convention.
 N=9;Id=s.eye(N)
 def channel(X):
  bs=[X[i*3:(i+1)*3,i*3:(i+1)*3] for i in range(3)];r=sum(bs,s.zeros(3));return s.diag(*[(r-B)/2 for B in bs])
 def pinch(X):return s.diag(*[X[i*3:(i+1)*3,i*3:(i+1)*3] for i in range(3)])
 def expect(X):return s.diag(*([sum([X[i*3:(i+1)*3,i*3:(i+1)*3] for i in range(3)],s.zeros(3))/3]*3))
 vec=lambda X:s.Matrix([X[i,j] for j in range(N) for i in range(N)])
 basis=[]
 for j in range(N):
  for i in range(N):X=s.zeros(N);X[i,j]=1;basis.append(X)
 T=s.Matrix.hstack(*[vec(channel(X)) for X in basis]);E=s.Matrix.hstack(*[vec(expect(X)) for X in basis]);Pin=s.Matrix.hstack(*[vec(pinch(X)) for X in basis]);Q=Pin-E;O=s.eye(81)-Pin
 assert T==T.T and T*vec(Id)==vec(Id) and E*E==E and Q*Q==Q and O*O==O and E*Q==s.zeros(81) and T==E-Q/2 and T*T==E+Q/4
 ranks=[int(s.trace(x)) for x in [E,Q,O]];assert ranks==[9,18,54]
 J=s.zeros(81)
 for x in range(3):
  for y in range(3):
   if x!=y:
    M=s.zeros(3);M[y,x]=1;v=vec(s.kronecker_product(M,s.eye(3)));J+=v*v.T/2
 assert J==J.T and J*J==R(3,2)*J and s.trace(J)==9
 # Classical primitive symmetric channel with disjoint columns: broad-prior falsifier.
 C=s.Matrix(5,5,lambda i,j:R(1,2) if (i-j)%5 in [1,4] else 0)
 assert C==C.T and all(sum(C[:,j])==1 for j in range(5)) and all(x>0 for x in C**4)
 pp=s.Matrix([R(3,4),R(1,4),0,0,0]);qq=s.Matrix([R(1,4),R(3,4),0,0,0]);assert all(C[i,0]*C[i,1]==0 for i in range(5))
 # Relative entropy exactly retained on support, then common uniformregularization.
 assert list(C*pp)==[R(1,8),R(3,8),R(1,8),0,R(3,8)]
 sigma0=s.Matrix([[R(3,10),s.I/20],[-s.I/20,R(1,5)]]);sigma1=s.diag(R(3,5),R(2,5))-sigma0
 D=s.Matrix([[R(1,50),R(1,60)+s.I/100],[R(1,60)-s.I/100,-R(1,50)]]);rho0=sigma0+D;rho1=sigma1-D
 assert rho0+rho1==sigma0+sigma1
 for B in [sigma0,sigma1,rho0,rho1]:assert B[0,0]>0 and s.simplify(B.det())>0
 chans=[('constant',[0,1],[0,1],R(0)),('perfect_with_zero_row',[0,1,0],[0,0,1],R(1)),('Z075',[R(3,4),R(1,4),0],[0,1,0],R(3,4)),('reverse_Z075',[1,0],[R(1,4),R(3,4)],R(3,4)),('erasure04',[R(2,5),0,R(3,5),0],[0,R(2,5),R(3,5),0],R(2,5)),('nonunital09_02',[R(9,10),R(1,10),0],[R(1,5),R(4,5),0],R(1,2))]
 L=lambda X:s.kronecker_product(s.eye(2),X);RR=lambda X:s.kronecker_product(X.T,s.eye(2))
 for name,aa,bb,cap in chans:
  active=[(x,y) for x,y in zip(aa,bb) if x or y]
  for u in [0,R(1,7),1,5,'quadratic','SLD']:
   if u=='quadratic':A,B=RR(sigma0),RR(sigma1)
   elif u=='SLD':A,B=(L(sigma0)+RR(sigma0))/2,(L(sigma1)+RR(sigma1))/2
   else:A,B=L(rho0)+u*RR(sigma0),L(rho1)+u*RR(sigma1)
   G=s.simplify(cap*(A.inv()+B.inv())-sum([(x-y)**2*(x*A+y*B).inv() for x,y in active],s.zeros(4)))
   assert s.simplify(G-G.conjugate().T)==s.zeros(4)
   minors=[s.simplify(G.extract(ix,ix).det()) for sz in range(1,5) for ix in itertools.combinations(range(4),sz)]
   assert all(v>=0 for v in minors)
   rows.append(dict(channel=name,kernel=str(u),cap=str(cap),active_rows=len(active),full_complex_HS_PSD_all_principal_minors=True,zero_gap_matrix=(G==s.zeros(4))))
 out=dict(symbolic_identities=identities,Phi9=dict(HS_dimension=81,unital=True,trace_preserving=True,selfadjoint=True,CP_choi_nonzero_eigenvalue='3/2',CP_choi_multiplicity=6,spectrum={'1':9,'-1/2':18,'0':54},projection='I_A/3 tensorTr_A',two_step_exact='E+Q/4',not_primitive=True),classical_prior_counterexample=dict(cycle5=[[str(x) for x in row] for row in C.tolist()],fourth_power_strictlypositive=True,disjoint_columns=[0,1],input_p=[str(x) for x in pp],input_q=[str(x) for x in qq],exact_D='(log3)/2',retention_on_support='1',faithful_limit='Mix both with samepositiveuniform epsilon, then epsilon->0',scope='Own explicit reversible primitive classical example; broad no-uniform-one-step phenomenon already classical,not1110referenceactivation'),binary_operator_cases=rows,passed=True)
 (P/'EXACT1115.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'symbolic':len(identities),'binary_full_HS':len(rows),'Phi81_and_classical_cycle':True}))
except Exception as e:
 (P/'EXACT_FAILURE1115.json').write_text(json.dumps(dict(error=repr(e),traceback=traceback.format_exc(),completed=rows),indent=2)+'\n');raise
