from pathlib import Path
import sympy as s,json,traceback
P=Path(__file__).parent;rows=[]
try:
 for n in range(2,7):
  f=s.ones(n,1)/s.sqrt(n);F=f*f.T;PP=s.eye(n)-F
  for m in range(1,n):
   B=s.Matrix.hstack(*[s.sqrt(s.Rational(n,n-1))*(s.eye(n)[:,i]-s.ones(n,1)/n) for i in range(m)])
   G=s.simplify(B.T*B);one=s.ones(m,1);w=s.Matrix([s.Rational(1,j+2) for j in range(m)]);t=sum(w)
   T=s.simplify(B*s.diag(*w)*B.T);z=B*w;v=B*G.inv()*one;Q=s.simplify(B*G.inv()*B.T)
   assert s.simplify(T*v-z)==s.zeros(n,1)
   assert s.simplify((z.T*v)[0]-t)==0
   assert s.simplify((v.T*v)[0]-s.Rational(m*(n-1),n-m))==0
   k=n+3;b=s.Rational(1,4*n*k);d=s.Rational(1,2**k);e=b*d;a=s.Rational(1,n)-(n-2)*e-b;c2=a*b*(1-d)
   A=(a-e)*T+e*t*Q
   inv0=(A+s.eye(n)-Q).inv();Sch0=s.simplify(b*t-c2*(z.T*inv0*z)[0])
   invE=((a-e)*T+s.eye(n)-Q).inv()
   SchE=s.simplify(b*t-e*t-c2*(z.T*invE*z)[0])
   expected=-t*b*e*(1-d)/(a-e)
   assert Sch0>=b*t*d>0 and s.simplify(SchE-expected)==0 and SchE<0
   rows.append({'n':n,'support':m,'restricted_inverse_identity':True,'inverse_vector_norm2':str((v.T*v)[0].simplify()),'schur0':str(Sch0),'schur_at_epsilon_t':str(SchE),'exact_active_min_below_inactive':True})
  B=s.sqrt(s.Rational(n,n-1))*PP;w=s.Matrix([s.Rational(1,j+2) for j in range(n)]);t=sum(w);T=B*s.diag(*w)*B.T;z=B*w
  value=s.simplify((z.T*(T+F).inv()*z)[0]);deficit=s.simplify(t-value)
  assert deficit==n*n/sum(1/x for x in w)>0
  rows.append({'n':n,'fullsupport':True,'inverse_value':str(value),'deficit':str(deficit),'formula_n2_over_sum_reciprocals':True})
 # Denominator and support counterexamples that must not be promoted to equalities.
 K=s.Matrix([[0,s.Rational(1,3),s.Rational(2,5)],[s.Rational(3,4),0,s.Rational(3,5)],[s.Rational(1,4),s.Rational(2,3),0]])
 assert all(sum(K[:,i])==1 for i in range(3))
 tv=[sum(abs(K[j,i]-K[j,h]) for j in range(3))/2 for i in range(3) for h in range(i+1,3)]
 assert max(tv)==s.Rational(3,4)
 extra={'asymmetric3':{'pairwise_column_TV':list(map(str,tv)),'classical_KL_upper':str(max(tv)),'zero_Doeblin':True},'binary_09_02':{'d':'3/10','doeblin_upper':'7/10','exact_complete_from1115':'1/2','not_equal_to_Doeblin_upper':True},'n1':'excluded: equalR CQ hypotheses identical, no positive denominator','zero_output':'joint zero block, remove from support without postselection'}
 (P/'EXACT1136.json').write_text(json.dumps({'cases':rows,'extra':extra,'universal_derivation':'AUDIT1136 sections2-4'},indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'proper_support_exact_cases':15,'fullsupport_exact_cases':5,'all_passed':True}))
except Exception as e:
 (P/'EXACT_FAILURE1136.json').write_text(json.dumps({'exception':repr(e),'traceback':traceback.format_exc(),'completed':rows},indent=2)+'\n');raise
