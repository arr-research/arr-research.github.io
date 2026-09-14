"""Replay exact rational exposedness witnesses; no optimizer or pickle required."""
from pathlib import Path
from fractions import Fraction as Q
import json
W=Path(__file__).parent
records=json.loads((W/'fresh-20260914/exposedness-exact-witnesses.json').read_text())
seen={}
for record in records:
 m,z=record['m'],record['z'];f=tuple(record['form']);x=list(map(Q,record['point']))
 S=set(map(tuple,json.loads((W/f'author/closed_m{m}_z{z}.json').read_text())))
 assert f in S and sum(x[:m])==sum(x[m:])==1
 gaps=[x[j]-x[j+1] for j in range(m-1)]+[x[m-1],x[m]-x[m+1],x[m+1]-x[m+2],x[m+2]]
 gaps += [sum((f[i]-h[i])*x[i] for i in range(m+2)) for h in S if h!=f]
 assert min(gaps)>0 and min(gaps)==Q(record['minimum_strict_gap'])
 seen.setdefault((m,z),set()).add(f)
for m in range(3,10):
 for z in (0,1):
  assert seen[m,z]==set(map(tuple,json.loads((W/f'author/closed_m{m}_z{z}.json').read_text())))
print('PASS',len(records),'exact strict exposedness witnesses, complete for m=3..9,z=0,1')
