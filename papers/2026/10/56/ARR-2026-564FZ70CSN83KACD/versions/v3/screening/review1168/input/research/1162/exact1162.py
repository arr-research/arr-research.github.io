from pathlib import Path
import sympy as s,json,hashlib,datetime,shutil
P=Path(__file__).parent;src=Path(r'C:\Trabajo\airr\2026-10-28_cq1157-audit\SMALL_FALSIFIER1157.json');shutil.copyfile(src,P/'PRELIMINARY-FALSIFIER1157.json')
t,r=s.symbols('t r',positive=True);tau0=s.diag(1,0);v=s.Matrix([1,t]);tau1=v*v.T/(1+t*t);S=tau0+tau1;M=S.inv()*(tau0-tau1);C=(s.eye(2)+r*M.T*M).inv();cost=s.factor(s.trace(C*S));formula=2*t*t*(1+r)/(t*t*(1+r)**2+4*r)
assert s.factor(cost-formula)==0
rows=[]
for tv in [s.Rational(1,16),s.Rational(1,2),s.Rational(1),s.Rational(2)]:
 for k in [8,16,64]:
  beta=s.Rational(1,8*k);alpha=s.Rational(1,2)-beta;delta=s.Rational(1,2**k);rv=beta*(1-delta)/alpha;z=cost.subs({t:tv,r:rv});q=s.factor(beta*delta*z);p=s.factor(beta*(4-3*delta)*z)
  assert 0<q<p<1 and s.factor(p/q-(4-3*delta)/delta)==0
  rows.append({'t':str(tv),'k':k,'cost':str(z),'p':str(p),'q':str(q),'p_over_q':str(p/q),'direct_matrix_equals_formula':s.factor(z-formula.subs({t:tv,r:rv}))==0})
report={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'root exact arithmetic checks, not scientific audit or manuscript assessment','source_preliminary_falsifier_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'T0_identity_for_two_pure_states':True,'M':str(M.applyfunc(s.simplify)),'Tr_CS':str(cost),'cases':rows,'corrects_root1152_explanation':True,'no_change_to_frozen1152_or_audit_inputs':True,'no_score':True}
(P/'EXACT1162.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps({'cases':len(rows),'Tr_CS':str(cost),'source_sha256':report['source_preliminary_falsifier_sha256']}))
