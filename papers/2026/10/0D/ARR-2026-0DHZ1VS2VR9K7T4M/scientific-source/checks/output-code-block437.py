from pathlib import Path
import runpy,json
import sympy as s
r=Path(__file__).resolve().parent;Q=s.Rational
# Deliberate author-code reuse, declared in README; no independence claim.
g=runpy.run_path(str(r/'complex-code-gram.py'))
C=s.Matrix.hstack(*g['code']);Pi=C*C.H/3;W=s.kronecker_product(s.eye(3),Pi)
v=s.Matrix.vstack(*g['code']);P=v*v.H/9;J=g['J'];a=Q(1,2);eta=Q(7,8)
assert W*W==W and W*P==P
assert J*W==a*W+(eta-a)*P and W*J==J*W
E=4*(J-a*s.eye(81)-(eta-a)*P)
assert E*E==E and E*W==s.zeros(81) and W*E==s.zeros(81)
assert s.conjugate(W)*g['G']==s.conjugate(J*W)
h=runpy.run_path(str(r/'werner429-ame6-controls.py'))
C=s.Matrix.hstack(*[s.Matrix(x) for x in h['code']]);Pi=C*C.T/32
W=s.kronecker_product(s.eye(2),Pi);P=h['P'];E=h['E1'];T=h['T']
assert W*W==W and W*P==P
assert E*W==s.zeros(64) and T*W==s.zeros(64)
J=sum(((-Q(1,2))**k*h['coeff'][k] for k in range(6)),s.zeros(64))
assert J*W==Q(3,8)*(W-P) and W*J==J*W
assert J.eigenvals()=={0:1,Q(3,16):15,Q(1,4):45,Q(3,8):3}
out={'status':'PASS_EXACT_OUTPUT_CODE_BLOCKS','cases':['nonreal_AME4_qutrit','real_wheel_AME6_qubit'],'entire_output_code_separation':True,'complex_Gram_projection':'conjugate(W)','producer_code_reused':True,'independent_review':False,'scope':'Finite transcription controls only; general proofs and analytic large-dimension witnesses are in the manuscript.'}
(r/'output-code-block437.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
