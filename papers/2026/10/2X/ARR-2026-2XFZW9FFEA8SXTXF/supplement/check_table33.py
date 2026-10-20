"""Recompute the printed rational determinant and weight bounds, without search."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s

root = Path(__file__).resolve().parent
output = root / 'table-checks-33.json'
assert not output.exists()
data = json.loads((root / 'degree-obstruction-33.json').read_text())
nodes = [['-3/10','17/20','9/10'],
         ['-7/20','9/20','1/2','23/20','6/5'],
         ['-7/20','1/4','3/10','7/10','3/4','13/10','27/20']]
records = []
for M, row in enumerate(data['records'], 1):
    assert row['M'] == M
    assert [v['t'] for v in row['support']] == nodes[M-1]
    assert all(v['kind'] == 'd' for v in row['support'])
    cols = []
    for node in nodes[M-1]:
        t = s.Rational(node)
        z = s.cancel((1+s.I*t)/(1-s.I*t)).expand(complex=True)
        cs = s.re(z)
        basis = [s.Integer(1)]
        derivative = [s.Integer(0)]
        for k in range(1,M+1):
            power = s.expand_complex(z**k)
            basis += [2*s.re(power), -2*s.im(power)]
            derivative += [-2*k*s.im(power), -2*k*s.re(power)]
        F = -s.Rational(3,4)+s.Rational(51,20)*cs
        G = 1+s.Rational(3,5)*cs
        cols.append(s.Matrix([-M*F*v-G*u for v,u in zip(basis,derivative)]))
    B = s.Matrix.hstack(*cols)
    e0 = s.eye(2*M+1)[:,0]
    weights = -B.inv()*e0
    determinant = B.det()
    assert s.sign(determinant) == [1,-1,1][M-1]
    assert min(weights) > [1,2,6][M-1]
    assert B*weights == -e0
    assert list(weights) == [s.Rational(v['weight']) for v in row['support']]
    records.append({'M':M, 'nodes':nodes[M-1], 'determinant':str(determinant),
                    'determinant_sign':int(s.sign(determinant)),
                    'weights':[str(v) for v in weights],
                    'minimum_weight':str(min(weights)),
                    'strict_lower_bound':[1,2,6][M-1], 'identity':True})
result = {'at':datetime.now(timezone.utc).isoformat(), 'exact_rational':True,
          'optimizer_used':False, 'records':records}
output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'verified_rows':len(records), 'status':'PASS'}))
