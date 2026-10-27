"""Resume after a recorded structural-equality failure, without resampling.
All prior attempts remain intact. This does not rerun the expensive invariant forms.
"""
from pathlib import Path
p=Path(__file__).resolve().parent
src=(p/'own_controls1031-v3.py').read_text(encoding='utf-8')
prefix=src.split('try:\n',1)[0].replace('OWN1031-v3.json','OWN1031-resumed.json')
phase3=src.split('    # Two noncommuting complex finite states',1)[1]
diagnostic='''try:
    I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Yp=s.Matrix([[0,-s.I],[s.I,0]]);Zp=s.diag(1,-1)
    weights=[R(1,10),R(2,10),R(3,10),R(4,10)]
    pre=(3*I+4*s.I*Yp)/5;post=(5*I+12*s.I*X)/13
    bell=s.Matrix([1,0,0,1]);J=sum((w*s.kronecker_product(post*P*pre,I)*bell*bell.T*s.kronecker_product(post*P*pre,I).conjugate().T/2 for w,P in zip(weights,[I,X,Yp,Zp])),s.zeros(4))
    raw_trace_equality=(s.trace(J)==1)
    J=J.applyfunc(s.simplify)
    normalized=s.factor(1-16/s.trace(J.inv()))
    unnormalized=s.factor(1-8/s.trace((2*J).inv()))
    assert s.trace(J)==1 and normalized==unnormalized==R(29,125)
    emit('choi_failure_diagnosis',raw_structural_trace_equality=raw_trace_equality,simplified_trace=str(s.trace(J)),normalized_coefficient=str(normalized),unnormalized_coefficient=str(unnormalized),result='PASS after algebraic simplification of the exact same matrix; no counterexample')
    # Two noncommuting complex finite states'''
code=(prefix+diagnostic+phase3).replace('OWN1031-v3.json','OWN1031-resumed.json')
exec(compile(code,str(p/'resume_controls1031.py'), 'exec'))
