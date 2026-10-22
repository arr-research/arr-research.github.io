# SPDX-License-Identifier: Apache-2.0
"""Preserve the smaller-block failures explicitly mentioned in the manuscript."""
from pathlib import Path
import json
from odd_cycle_ground_kernels import ground
from exact_inertia import inertia
R=Path(__file__).parent;rows=[]
for s,k,failed,working in [(4,k,5,6) for k in (3,4,5)]+[(7,k,7,8) for k in range(6,25)]:
 L,N=ground(k,s);active=[i for i in range(L.rows) if any(L.row(i))]
 bad,pb=inertia(L.extract(active[:failed],active[:failed]));good,pg=inertia(L.extract(active[:working],active[:working]))
 assert bad[0]==1 and good[0]>=2 and good[2]==0
 rows.append(dict(s=s,k=k,failed_profiles=active[:failed],failed_inertia=bad,failed_pivots=pb,working_profiles=active[:working],working_inertia=good,working_pivots=pg))
L,N=ground(3,6);bad,pb=inertia(L.extract([5,6,11,12],[5,6,11,12]));active=[i for i in range(L.rows) if any(L.row(i))];good,pg=inertia(L.extract(active[:7],active[:7]))
assert bad==[1,3,0] and good==[2,5,0]
rows.append(dict(s=6,k=3,failed_profiles=[5,6,11,12],failed_inertia=bad,failed_pivots=pb,working_profiles=active[:7],working_inertia=good,working_pivots=pg))
(R/'smaller-block-failures.json').write_text(json.dumps(dict(status='PASS',cases=rows,limitation='Failures of these specific restrictions, not lower bounds on target states.'),indent=2)+'\n',encoding='utf-8')
print('PASS: 23 preserved smaller-block failures and their successful alternatives.')
