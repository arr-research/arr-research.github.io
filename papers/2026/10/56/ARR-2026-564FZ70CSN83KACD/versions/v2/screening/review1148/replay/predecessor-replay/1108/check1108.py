from fractions import Fraction as F
import json,pathlib
p=pathlib.Path(__file__).with_name("CONTROL1108.json")
rows=json.loads(p.read_text())["rows"]
assert len(rows)==48
for row in rows:
 n=row["n"]; x=F(row["x"])
 a=[F(int(y!=0),n-1) for y in range(n)]
 b=[F(int(y!=1),n-1) for y in range(n)]
 v=x*(1-x)*sum((aa-bb)**2/(bb+(aa-bb)*x) for aa,bb in zip(a,b))
 assert v==F(row["F"])==F(1,n-1)
print("48 exact rational boundary controls passed")
