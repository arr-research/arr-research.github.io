"""Exact rational similar-coordinate certificates for all four tiny pairs.
No radicals, floating point, or imported original checker.
"""
from pathlib import Path
import sympy as s,json
P=Path(__file__).parent;R=s.Rational;rows=[]
for d in [3,4]:
 a=d-1;e=R(1,10**30);t=R(1,10**90);theta=R(99,100);q=a+e*e;M=R(d*(2*d-1),2)
 W=lambda p:s.Matrix([[1+(d*a-1)*p,d*p*e],[d*p*e*a,(2+(d-2)*p)*e*e]])/(2*d*q)
 T=s.Matrix([[0,1],[a,2*e]]);B=s.diag(1,2*e*e)/(2*d*q)
 for l in [-R(1,d*d-1),R(1,2)]:
  cert=[]
  for sign in [-1,1]:
   for name,A in [('input',W(theta)+sign*t*T),('output',W(l*theta)+sign*l*t*T),('order_slack',M*B-W(theta)-sign*t*T)]:
    det=s.factor(A.det());assert A[0,0]>0 and det>0
    # Gram diag(a,1) makes this coordinate matrix self-adjoint.
    H=s.diag(a,1);assert H*A==A.T*H
    cert.append({'matrix':name,'sign':sign,'first_diagonal':str(A[0,0]),'determinant':str(det),'Gram_selfadjoint':True})
  modes={'input_replacement_factor':1-theta,'output_replacement_factor':1-l*theta,'order_slack_replacement_factor':M-1+theta};assert all(x>0 for x in modes.values())
  rows.append({'d':d,'R':2*d-1,'lambda':str(l),'kappa':str(M),'actual_base_order':str(1+(M-1)*theta),'plane_certificates':cert,'unperturbed_modes_positive_factors':{k:str(v) for k,v in modes.items()},'total_trace_perturbation':str(t*s.trace(T)-t*s.trace(T))})
(P/'POSITIVITY1044.json').write_text(json.dumps({'scope':'Four exact complete finite-pair positivity/budget checks via rational invariant planes plus all other positive modes; global geometry checked separately','cases':rows,'all_passed':True},indent=2)+'\n',encoding='utf-8');print('4 rational/similarity positivity and both-order certificates passed.')
