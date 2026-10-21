from pathlib import Path
import ast, json, math
import numpy as np
R=Path(__file__).resolve().parent
tree=ast.parse((R/'check_reverse_channel.py').read_text())
# Reuse only pure mathematical helpers; do not repeat the earlier experiment.
helpers=ast.Module(body=[n for n in tree.body if isinstance(n,(ast.Import,ast.ImportFrom,ast.FunctionDef))],type_ignores=[])
scope={};exec(compile(helpers,'helpers','exec'),scope)
F=scope['formation_at_p'];h=scope['h'];reverse=scope['reverse']
rng=np.random.default_rng(20261017993)
threshold_error=0.;determinant_error=0.;roof_error=0.
for i in range(60):
    a,b=rng.dirichlet([2,2,2])[:2];k=1-a-b
    threshold=k+2*a*b-2*math.sqrt(a*b*(k+a*b))
    x=threshold+(k-threshold)*rng.random();p=.01+.98*rng.random()
    ap,bp,xp,t=reverse(a,b,x,p);kp=1-ap-bp;L=p*(1-p)/(t*(1-t))
    cp=kp+2*ap*bp-2*math.sqrt(ap*bp*(kp+ap*bp))
    threshold_error=max(threshold_error,abs(cp-L*threshold))
    det=(ap+kp*t)*(1-ap-kp*t)-xp*t*(1-t)
    determinant_error=max(determinant_error,abs(det-p*(1-p)*(1-x)))
    expected=h((1+math.sqrt(1-4*p*(1-p)*(1-x)))/2)
    roof_error=max(roof_error,abs(F(a,b,x,p,grid=24000)-expected))
assert threshold_error<1e-12 and determinant_error<1e-12 and roof_error<1e-7
examples=[]
for a,b,x,p in ((.1,.3,.6,.5),(.1,.3,.5,.5),(.1,.3,.1,.5169491077086091),(.02,.3,.514624,.5591616236738203)):
    threshold=k0=1-a-b
    threshold+=2*a*b-2*math.sqrt(a*b*(k0+a*b))
    bell=F(a,b,x,.5,grid=60000)/np.log(2)
    value=F(a,b,x,p,grid=60000)/np.log(2)
    examples.append(dict(a=a,b=b,lambda_squared=x,known_flat_threshold=threshold,p_tested=p,formation_at_tested_p_bits_approx=value,formation_at_bell_bits_approx=bell,difference_bits_approx=value-bell,closed_form_or_upper_bound_bits=float(h((1+math.sqrt(x))/2)/np.log(2))))
record=dict(status='Floating point diagnostics, not proofs or continuous optimization certificates',cases=60,threshold_identity_error=threshold_error,determinant_identity_error=determinant_error,sampled_roof_error_nats=roof_error,examples=examples)
(R/'closed-form-results.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record),flush=True)
