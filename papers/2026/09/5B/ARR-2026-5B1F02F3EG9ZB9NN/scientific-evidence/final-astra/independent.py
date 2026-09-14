import json,gzip,itertools,math,time
from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
import cdd.gmp as cd
P=Path(__file__).parent/'repro/certs'; start=time.time()
def read(p):return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
def poly(rows,eq=()):return cd.polyhedron_from_matrix(cd.matrix_from_array(rows,rep_type=cd.RepType.INEQUALITY,lin_set=set(eq)))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def dist(a,b):
 e=lambda x:2*(1-x[0]);u=lambda x:sum(abs(v-F(1,len(x))) for v in x)
 return min(e(a)+u(b),u(a)+e(b))
def skew(a):return 2*(1-a[0])-sum(abs(v-F(1,len(a))) for v in a)
# Independently reconstruct the D_* polyhedral cells with exact GMP double description.
for N in range(3,13):
 vertices=set();edges=set()
 for r in range(1,N):
  rows=[[F(-1)]+[F(1)]*N]
  for j in range(N-1):
   row=[F(0)]*(N+1);row[j+1]=1;row[j+2]=-1;rows.append(row)
  rows.append([F(0)]*N+[F(1)])
  row=[F(-1,N)]+[F(0)]*N;row[r]=1;rows.append(row)
  row=[F(1,N)]+[F(0)]*N;row[r+1]=-1;rows.append(row)
  po=poly(rows,[0]);gs=cd.copy_generators(po);assert not gs.lin_set
  vs=[tuple(map(F,row[1:])) for row in gs.array];assert all(row[0]==1 for row in gs.array)
  vertices.update(vs)
  for i,adj in enumerate(cd.copy_adjacency(po)):
   for j in adj:edges.add(tuple(sorted((vs[i],vs[j]))))
 W=set(itertools.product(vertices,repeat=2))
 for a in vertices:
  qa=skew(a)
  for b,c in edges:
   qb,qc=skew(b),skew(c)
   if min(qb,qc)<qa<max(qb,qc):
    t=(qa-qb)/(qc-qb);x=tuple((1-t)*v+t*w for v,w in zip(b,c));W.add((a,x));W.add((x,a))
 cert=read(next(P.glob('gamma_N'+str(N)+'.json*')))
 supplied={(tuple(map(F,p['a'])),tuple(map(F,p['b']))) for p in cert['pairs']}
 assert supplied=={x for x in W if dist(*x)>0}
 for p in cert['pairs']:
  a,b=tuple(map(F,p['a'])),tuple(map(F,p['b']));assert dist(a,b)==F(p['Dstar'])
  assert (F(N+1,2)-sum(map(F,p['s'])))/dist(a,b)>=F(cert['gamma'])
 print('GMP independently regenerated W',N,len(W),'positive',len(supplied),flush=True)
# LR tableaux, not Horn recursion, generate all d=6 necessary inequalities.
def part(I):return tuple(i-j for j,i in reversed(list(enumerate(I,1))))
@lru_cache(None)
def lr(alpha,beta,nu):
 n=len(alpha)
 if any(alpha[i]>nu[i] for i in range(n)) or sum(alpha)+sum(beta)!=sum(nu):return False
 cells=[(r,c) for r in range(n) for c in range(nu[r],alpha[r],-1)]
 filling={}; used=[0]*n
 def go(t):
  if t==len(cells):return tuple(used)==beta
  r,c=cells[t]
  for v in range(n):
   if used[v]>=beta[v] or (v and used[v]+1>used[v-1]):continue
   if (r,c+1) in filling and v>filling[r,c+1]:continue
   if (r-1,c) in filling and v<=filling[r-1,c]:continue
   filling[r,c]=v;used[v]+=1
   if go(t+1):return True
   used[v]-=1;del filling[r,c]
  return False
 return go(0)
triples=[]
for r in range(1,6):
 for I,J,K in itertools.product(itertools.combinations(range(1,7),r),repeat=3):
  if sum(I)+sum(J)==sum(K)+r*(r+1)//2 and lr(part(I),part(J),part(K)):triples.append((I,J,K))
assert len(triples)==522;T=set(triples)
def coeff(I,J):
 v=[F(0)]*6
 for i in I:v[i-1]+=1
 for j in J:v[6-j]-=1
 return v
def primitive(v):
 den=math.lcm(*(x.denominator for x in v));z=[int(x*den) for x in v];g=math.gcd(*z)
 return tuple(x//g for x in z)
cert=read(P/'kappa6_certificate.json');forms=[tuple(map(F,ch['q'])) for ch in cert['chambers']];rays=0
for q,ch in zip(forms,cert['chambers']):
 rows=[[F(0)]+[F(i==j) for j in range(5)] for i in range(5)]
 rows += [[F(0)]+[x-y for x,y in zip(q,other)] for other in forms if other!=q]
 gs=cd.copy_generators(poly(rows));assert not gs.lin_set
 actual={primitive(tuple(map(F,row[1:]))) for row in gs.array if row[0]==0};assert actual==set(map(tuple,ch['rays']))
 c=[F(0)]*6;w=[F(0)]*6
 for I,J,K,y in ch['dual_y']:
  assert (tuple(I),tuple(J),tuple(K)) in T and F(y)>=0
  co=coeff(I,J);c=[x+F(y)*z for x,z in zip(c,co)]
  for k in K:w[k-1]+=F(y)
 for j,z in enumerate(map(F,ch['dual_z'])):assert z>=0;c[j]+=z;c[j+1]-=z
 assert all(x<=1 for x in c[:5]);assert tuple(sum(w[:j])-F(j,6)*sum(w) for j in range(1,6))==q
 for rho,s0 in zip(ch['rays'],ch['witness_s']):
  sv=list(map(F,s0))+[F(0)];lam=[sum(rho[i:]) for i in range(5)]+[0];avg=F(sum(lam),6);lam=[F(x)-avg for x in lam]
  assert all(sv[i]>=sv[i+1]>=0 for i in range(5)) and sum(sv)==dot(q,rho)
  assert all(sum(lam[k-1] for k in K)<=dot(coeff(I,J),sv) for I,J,K in triples)
 # Sum of spanning rays gives a point strictly inside every nonredundant dominance inequality.
 interior=[sum(r[i] for r in actual) for i in range(5)]
 assert all(x>0 for x in interior) and all(dot(q,interior)>dot(other,interior) for other in forms if other!=q)
 rays+=len(actual)
assert rays==112
print('PASS 522 LR triples, 22 exact GMP chambers, 112 witnesses and global duals',flush=True)
# Every long template here is a Lidskii identity partition times any partition.
# For r<=2 Horn recursion has only r=1 tests, so validate slopes directly.
for fn in P.glob('alld_lower_*.json'):
 z=read(fn);N=z['N'];M=z['M'];d0=z['d0'];assert d0>=2*M>=2*N
 a,b=list(map(F,z['a'])),list(map(F,z['b']));cs=[F(0)]*(2*M);val=F(0)
 for t in z['templates']:
  r=t['r'];y=F(t['y']);assert y>=0
  sym=lambda name:[(0,x) for x in sorted(t[name+'0'])]+[(1,1-x) for x in sorted(t[name+'1'],reverse=True)]
  I,J,K=map(sym,['I','J','K']);assert len(I)==len(J)==len(K)==r
  assert sum(x[0] for x in I+J)==sum(x[0] for x in K)
  assert sum(x[1] for x in I+J)-sum(x[1] for x in K)==r*(r+1)//2
  if r>=3:assert I==[(0,x) for x in range(1,r+1)] and J==K
  elif r==2:
   for f,g,h in [(1,1,1),(1,2,2),(2,1,2)]:
    sl=I[f-1][0]+J[g-1][0]-K[h-1][0];co=I[f-1][1]+J[g-1][1]-K[h-1][1]-1
    assert sl<=0 and sl*d0+co<=0
  for k in t['I0']:cs[k-1]+=y
  for k in t['I1']:cs[M+k-1]+=y
  for k in t['J0']:cs[M+k-1]-=y
  for k in t['J1']:cs[k-1]-=y
  aa,bb=(b,a) if t['refl'] else (a,b)
  val+=y*(sum(aa[k-1] if k<=N else 0 for k in t['K0'])-sum(bb[k-1] if k<=N else 0 for k in t['K1']))
 assert all(F(x)==0 for x in z['order_multipliers']) and max(cs)<=1 and val==F(z['bound'])
 print('PASS all-d exact structural certificate',fn.name,str(val),flush=True)
print('ALL INDEPENDENT CHECKS PASS, seconds',time.time()-start,flush=True)
