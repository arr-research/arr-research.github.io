from pathlib import Path
import sympy as s,json,traceback
P=Path(__file__).parent;records=[]
try:
 d,x,delta,t,y,u=s.symbols('d x delta t y u',positive=True);q=d-1+x;theta=1-delta;lam=-1/(d*d-1);A=d*(d-1)-1+(d-1)*x
 def td(p):return s.factor((1+(d*(d-1)-1)*p+(1+(d-1)*p)*x)/(d*q)),s.factor(x*(1-p)*(1+(d*d-1)*p)/(d*d*q*q))
 ti,di=td(theta);to,do=td(lam*theta);ci=theta**2*x*(d-1)/q**2;emin=delta*x/(d*q)
 assert s.factor(ti-(1-delta*A/(d*q)))==0
 assert s.factor(to-(d*(1+(d-1)*x)+delta*A)/((d*d-1)*d*q))==0
 assert s.factor(di-x*delta*(d*d-(d*d-1)*delta)/(d*d*q*q))==0
 assert s.factor(do-x*delta*(d*d-delta)/((d*d-1)*d*d*q*q))==0
 records.append({'name':'general_exact_forms','input_trace':str(ti),'input_det':str(di),'output_trace':str(to),'output_det':str(do),'coherence_squared':str(s.factor(ci))})
 exprs=[ti,d**5*di,d**3*to,d**7*do,d**3*ci,d**5*emin,d**4*lam**2]
 pp=[s.factor(v.subs({x:1/d**2,delta:1/d}).subs(d,1/u)) for v in exprs];vals=[s.simplify(v.subs(u,0)) for v in pp];assert vals==[1,1,2,1,1,1,1]
 records.append({'name':'1063_rational_limits','expressions_in_u':list(map(str,pp)),'u_to_zero_values':list(map(str,vals))})
 # beta>1 implies y=d*delta=d^(1-beta)->0 jointly with u=1/d.
 exprs=[ti,d**3*di/delta,d**3*to,d**5*do/delta,d**2*ci,d**3*emin/delta,d**4*lam**2]
 pp=[s.factor(v.subs({x:t/d,delta:y/d}).subs(d,1/u)) for v in exprs]
 vals=[]
 for v in pp:
  num,den=s.fraction(v);assert s.simplify(den.subs({u:0,y:0}))!=0;vals.append(s.simplify(v.subs({u:0,y:0})))
 assert vals==[1,t,1+t,t,t,t,1]
 records.append({'name':'1066_joint_rational_limits_all_fixed_t_beta','substitution':'u=1/d,y=d^(1-beta); t>0 fixed,beta>1. Rational denominators nonzero at(u,y)=(0,0); no exchange of dimension and epsilon limits.','expressions':list(map(str,pp)),'values':list(map(str,vals))})
 # Boundary and moving-parameter counterexamples to overly broad quantifiers.
 critical=s.limit((d**3*to).subs({x:t/d,delta:1/d}),d,s.oo);assert s.simplify(critical-(2+t))==0
 moving=[s.limit(v.subs({x:1/d**2,delta:1/d**2}),d,s.oo) for v in [ti,d**6*di,d**3*to,d**8*do,d**3*ci]];assert moving==[1,1,1,1,1]
 records.append({'name':'scope_falsifiers','beta_equals_one':{'scaled_output_trace':str(critical),'fixed_beta_gt1_formula_would_be':'1+t','dR_limit':'0; output roots have the same d^-3 order, so the stated separated-root exponent proof does not apply.'},'moving_t_1_over_d_beta2':{'scaled_rational_limits':list(map(str,moving)),'actual_dR_limit':'1/3','incorrect_substitution_in_fixed_t_alpha_limit':'1/5','actual_scaled_input_constant':'24 with d^3/log(d)','incorrect_fixed_t_constant':'20 with d^3/log(d)'},'minimum_x_gt1':'Exact input minimum is delta*min(1,x)/(d*q); formula delta*x/(d*q) fails when x>1.'})
 alpha0=s.Rational(9,10);tt=s.Rational(1,100);nu=s.Integer(45);alpha=(nu-4)/((1+tt)*nu);assert alpha>alpha0
 records.append({'name':'cost_of_large_fraction','target':str(alpha0),'t':str(tt),'beta':'42','nu':str(nu),'alpha':str(alpha),'condition_asymptotic':'100*d^45','interpretation':'Existence at fixed parameters; not a uniform bound as target approaches1.'})
 (P/'SYMBOLIC1068.json').write_text(json.dumps({'records':records,'passed':True},indent=2)+'\n',encoding='utf-8');print('General identities, joint rational limits and quantifier falsifiers passed.')
except Exception as ex:
 (P/'SYMBOLIC_FAILURE1068.json').write_text(json.dumps({'error':repr(ex),'traceback':traceback.format_exc(),'completed':records},indent=2)+'\n',encoding='utf-8');raise
