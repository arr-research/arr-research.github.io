from pathlib import Path
import sympy as s,itertools,json,time
root=Path(__file__).resolve().parent;started=time.time();d=3;m=3;D=d**m;N=D*D
def flat(xs):
 r=0
 for x in xs:r=d*r+x
 return r
labels=list(itertools.product(range(d),repeat=2*m));I=s.SparseMatrix(s.eye(N));W=I;Winv=I
for slot in range(m):
 entries={}
 for k,xs in enumerate(labels):
  ys=list(xs);ys[slot],ys[slot+m]=ys[slot+m],ys[slot];entries[flat(ys),k]=1
 F=s.SparseMatrix(N,N,entries);W=W*(I-F/2);Winv=Winv*(4*I/3+2*F/3)
assert W*Winv==I
a=s.SparseMatrix(D,1,{(flat([i]*m),0):1 for i in range(d)})
# Direct Phi(Eij) tensor power, rather than assuming the diagonal shortcut377.
H=s.zeros(D)
for i in range(d):
 for j in range(d):
  Q=s.eye(d)*int(i==j);Q[i,j]-=s.Rational(1,2)
  H+=s.kronecker_product(*([Q]*m))
Hinv=s.SparseMatrix(H.inv());md={}
for (rr,cc),v in W.todok().items():
 r,t=divmod(rr,D);source,j=divmod(cc,D)
 if a[source]:md[j*D+r,t]=md.get((j*D+r,t),0)+v
M=s.SparseMatrix(N,D,md);CP=M*Hinv*M.T;bd={}
for (rr,cc),v in CP.todok().items():
 j,r=divmod(rr,D);k,t=divmod(cc,D);bd[k*D+r,j*D+t]=v
B=s.SparseMatrix(N,N,bd);assert B==B.T;R=Winv*B
Hspec=H.eigenvals();assert min(Hspec)==s.Rational(3,2)
kernel=s.kronecker_product(s.eye(D),a)
assert (W-B)*kernel==s.zeros(N,D)
adj=[set() for _ in range(N)]
for (i,j),v in R.todok().items():
 if i!=j:adj[i].add(j);adj[j].add(i)
left=set(range(N));components=[]
while left:
 todo=[min(left)];seen=set(todo)
 while todo:
  i=todo.pop()
  for j in adj[i]-seen:seen.add(j);todo.append(j)
 left-=seen;components.append(sorted(seen))
print('components',len(components),'max',max(map(len,components)),'seconds',time.time()-started,flush=True)
factors={};checks=[];degree_sum=0
for inds in components:
 block=R.extract(inds,inds);poly=block.charpoly();x=poly.gen
 fs=s.factor_list(poly.as_expr(),x)[1]
 for f,power in fs:
  degree_sum+=int(s.degree(f,x))*int(power)
  key=str(f);factors[key]=factors.get(key,0)+int(power)
  if s.degree(f,x)==1 and f.subs(x,1)==0:continue
  p=s.Poly(f,x)
  assert p.count_roots(-s.oo,-s.Rational(7,8))==0,(len(inds),f,'lower')
  assert p.count_roots(s.Rational(3,4),s.oo)==0,(len(inds),f,'upper')
 checks.append({'dimension':len(inds),'minimum_index':min(inds),'factorization':str(s.factor(poly.as_expr()))})
 print('checked',len(inds),len(checks),'seconds',time.time()-started,flush=True)
assert factors.get('lambda - 1')==D
assert degree_sum==N
out={'status':'AUTHOR_EXACT_GHZ3_BLOCK_PASS','d':d,'slots':m,'Choi_dimension':N,'H_spectrum':{str(v):int(k) for v,k in Hspec.items()},'H_min_normalized':'1/2','W_positive_and_inverse_checked':True,'B_symmetric':True,'kernel_input_tensor_anchor_checked':True,'eigenvalue1_multiplicity':D,'other_eigenvalue_bounds':['-7/8','3/4'],'characteristic_factors':factors,'components':checks,'R_entries':len(R.todok()),'seconds':time.time()-started,'scope':'Exact finite block only, not independent audit, tensor theorem, worldwide priority or score.'}
(root/'werner378-ghz-exact.json').write_bytes((json.dumps(out,indent=2)+'\n').encode());print(json.dumps({k:v for k,v in out.items() if k!='components'}))
