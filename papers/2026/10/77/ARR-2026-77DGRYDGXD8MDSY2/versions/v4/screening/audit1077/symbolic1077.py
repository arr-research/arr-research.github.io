from pathlib import Path
import sympy as s,json,traceback
P=Path(__file__).parent;rows=[]
try:
 A,C,b=s.symbols('A C b',real=True);W=s.Matrix([[A,b],[b,C]]);V=s.diag(1,-1);g=s.sqrt((A-C)**2+4*b*b);h=(A+C+g)/2;l=(A+C-g)/2;Pi=(h*s.eye(2)-W)/g
 assert all(s.simplify(v)==0 for v in Pi*Pi-Pi);assert s.simplify(s.trace(Pi)-1)==0
 assert s.simplify(s.trace(Pi*W)-l)==0;assert s.simplify(s.trace(Pi*V*W*V)-l-4*b*b/g)==0
 comm=W*(V*W*V)-(V*W*V)*W;assert s.simplify(comm[0,1]-2*b*(C-A))==0
 rows.append({'name':'general_exact_projector','projector_idempotent_trace1':True,'base_probability':'l','phase_probability':'l+4*b^2/(h-l)','commutator_offdiagonal':'2*b*(C-A)','scope':'Embedded as zero outside plane; ambient complement is I-Pi.'})
 a,x,delta=s.symbols('a x delta',positive=True);d=a+1;q=a+x;th=1-delta;lam=-1/(d*d-1);p=lam*th
 block=lambda pp:s.Matrix([[1+(d*a-1)*pp,d*pp*s.sqrt(a*x)],[d*pp*s.sqrt(a*x),(1+a*pp)*x]])/(d*q)
 K=s.Matrix([[a*x,s.sqrt(a*x)],[s.sqrt(a*x),1]])/(1+a*x)
 assert all(s.simplify(v)==0 for v in K*K-K);assert all(s.simplify(v)==0 for v in block(lam)*K)
 qb=s.factor(s.trace(K*block(p)));pb=s.factor(s.trace(K*V*block(p)*V))
 assert s.simplify(qb-delta*x/(q*(1+a*x)))==0
 assert s.simplify(pb-qb-4*th*a*x/((d*d-1)*q*(1+a*x)))==0
 rows.append({'name':'dimension_dependent_endpoint_kernel_control','projector':'[[a*x,sqrt(a*x)],[sqrt(a*x),1]]/(1+a*x)','q_exact':str(qb),'p_minus_q_exact':str(s.factor(pb-qb)),'conclusion':'Same leading constants for fixedt,beta>1, with no beta-dependent eigenvector. Exact1070 finiteformula still specifically needs its chosen projector.'})
 u,t=s.symbols('u t',positive=True);dc=1/u;qc=dc-1+t/dc
 leak=t*(1-s.sqrt(1-u))**2/((1+t)*(dc*dc-1)*qc)
 leakconstant=s.limit(leak/u**5,u,0,dir='+');assert s.simplify(leakconstant-t/(4*(1+t)))==0
 rows.append({'name':'limiting_vector_falsifier','vector_coefficients':'(sqrt(t),1)/sqrt(1+t) in dimension-dependent active basis','q_leak_at_delta0':str(leak),'d5_q_leak_limit':str(leakconstant),'fixed_beta_fraction_of_quantum_output':'min(beta-1,2)/(beta-1)','beta4_fraction':'2/3','beta6_fraction':'2/5','endpoint_kernel_fraction':'1 for all fixedbeta>1'})
 dd=s.symbols('dd',positive=True);xx=dd**-2;de=dd**-2;qq=dd-1+xx;thh=1-de;ll=-1/(dd*dd-1);pp=ll*thh
 tr=(1+(dd*(dd-1)-1)*pp+(1+(dd-1)*pp)*xx)/(dd*qq);det=xx*(1-pp)*(1+(dd*dd-1)*pp)/(dd*dd*qq*qq);ci=thh**2*xx*(dd-1)/qq**2
 vals=[s.limit(z,dd,s.oo) for z in [dd**3*tr,dd**8*det,dd**7*ll**2*ci,dd**3*ci]];assert vals==[1,1,1,1]
 rows.append({'name':'moving_t_exact_rational_scalings','parameters':'t_d=1/d,beta2','scalings':['d3 outputtrace','d8 outputdet','d7 b_squared','d3 inputcoherence_squared'],'values':list(map(str,vals)),'deduced':'h~d^-3,l~d^-5,p~4d^-4,q~d^-5; measured fraction1/2 and dmeasured/input1/6.'})
 rows.append({'name':'other_scope_falsifiers','reverse_orientation':'D(Ber(q)||Ber(p))~p while quantumoutput~p*(beta-1)*logd; ratio tends0','moving_t':'t_d=1/d,beta2: h~d^-3,l~d^-5,b^2~d^-7,p0~4d^-4,q0~d^-5; binary/quantumoutput->1/2 and d*binary/quantuminput->1/6, not1 and1/5.','block_normalization':'Conditional Bernoulli divergence must be multiplied by active mass; no free postselection.','wrong_full_identity':'(h*I_ambient-QWQ)/(h-l) has eigenvalueh/(h-l)>1 outside plane; not a POVM effect.','input_denominator':'Same output measurement on input yields different divergence; affine binary map need not be stochastic on all input probabilities.','Stein_epsilon0':'For a faithful null state, typeIerror0 forces testI, typeIIerror1; cannot includeepsilon0 in nonzero Stein exponent.'})
 (P/'SYMBOLIC1077.json').write_text(json.dumps({'records':rows,'passed':True},indent=2)+'\n',encoding='utf-8');print('Projector identities and endpoint-kernel simplification passed; scope falsifiers recorded.')
except Exception as ex:
 (P/'SYMBOLIC_FAILURE1077.json').write_text(json.dumps({'error':repr(ex),'traceback':traceback.format_exc(),'completed':rows},indent=2)+'\n',encoding='utf-8');raise
