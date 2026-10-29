from fractions import Fraction as Q
from pathlib import Path
import json
rows=[]
for d in range(2,9):
    for s in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]:
        P=[[Q(1-s,d)+s*Q(i!=y,d-1) for y in range(d)] for i in range(d)]
        assert all(sum(row)==1 and min(row)>=0 for row in P)
        eta=max(sum(abs(a-b) for a,b in zip(P[i],P[j]))/2 for i in range(d) for j in range(d))
        alpha=sum(min(P[i][y] for i in range(d)) for y in range(d))
        assert eta==s/(d-1) and alpha==1-s==1-(d-1)*eta
        rows.append({'d':d,'s':str(s),'ordinary_trace_factor_of_classical_channel':str(eta),'positive_CP_common_component_via_prior_measurement_formula':str(alpha)})
Path(__file__).with_name('CLASSICAL1207.json').write_bytes((json.dumps({'scope':'Separate unreviewed35-case classical calibration, not public1207 certificate or a new theorem','cases':rows},indent=2)+'\n').encode())
print('35 exact classical cases matched the claimed common-component envelope family')
