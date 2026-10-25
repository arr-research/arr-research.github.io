from pathlib import Path
import sympy as s,itertools,json
root=Path(__file__).resolve().parent;d=3;m=3;D=27
words=list(itertools.product(range(d),repeat=m));flat={x:i for i,x in enumerate(words)}
a=[(i,i,i) for i in range(3)];x=[(0,1,2),(1,2,0),(2,0,1)];z=[(0,2,1),(1,0,2),(2,1,0)]
entries={}
for rows,cols in [(a,a),(x,x+z)]:
 for r in rows:
  for c in cols:entries[(r,c)]=entries.get((r,c),0)+1
matrix=s.SparseMatrix(D,D,{(flat[r],flat[c]):v for (r,c),v in entries.items()})
assert matrix.rank()==2
norm=sum(v*v for v in entries.values());q=0;traces=[]
for mask in range(8):
 subset=[i for i in range(3) if mask>>i&1];keep=[i for i in range(3) if i not in subset];partial={}
 for (r,c),v in entries.items():
  if all(r[i]==c[i] for i in subset):
   key=(tuple(r[i] for i in keep),tuple(c[i] for i in keep));partial[key]=partial.get(key,0)+v
 value=sum(v*v for v in partial.values());q+=(-s.Rational(1,2))**len(subset)*value
 traces.append({'traced_slots':subset,'squared_Frobenius':int(value)})
ranks=[]
for slot in range(3):
 rem=[i for i in range(3) if i!=slot];re={}
 for (r,c),v in entries.items():
  row=3*r[slot]+c[slot];col=(3*r[rem[0]]+r[rem[1]])*9+3*c[rem[0]]+c[rem[1]];re[row,col]=v
 ranks.append(int(s.SparseMatrix(9,81,re).rank()))
assert ranks==[9,9,9]
assert matrix*matrix.T!=matrix.T*matrix
out={'status':'AUTHOR_EXACT_CONTROL_PASS','rank':2,'q3':str(q),'norm_squared':norm,'partial_trace_norms':traces,'operator_Schmidt_ranks_singleton_cuts':ranks,'nonnormal':True,'scope':'Explicit hypothesis separation, not a global Werner theorem or priority claim.'}
(root/'werner387-ghz-example.json').write_bytes((json.dumps(out,indent=2)+'\n').encode());print(json.dumps(out))
