from pathlib import Path
import math,itertools,time,json
start=time.time()
def weight(r,p):
 z=1
 while r:z*=1+r%p;r//=p
 return z
def omega(d,p,m):return max(r for r in range(d) if weight(r,p)<=m)
# Exhaustive prime-field polynomials, different implementation from supplied rank tests.
for p,d in [(2,16),(3,9),(5,5)]:
 hasse=[[math.comb(e,j)%p if e>=j else 0 for e in range(d)] for j in range(d)]
 for encoded in range(1,p**d):
  coeff=[];n=encoded
  for _ in range(d):coeff.append(n%p);n//=p
  order=next(j for j in range(d) if sum(a*b for a,b in zip(coeff,hasse[j]))%p)
  assert weight(order,p)<=sum(bool(x) for x in coeff)
 print('PASS prime-field polynomials',p,d,p**d-1,flush=True)
# Closed scalar envelope and the actual rounded rank-bound gaps.
gaps={}
for p in [2,3,5,7]:
 d=p;k=1
 while d<=2401:
  vals=[weight(r,p) for r in range(d)]
  oms=[max(r for r,w in enumerate(vals) if w<=m) for m in range(1,d+1)]
  for m in range(1,d):
   power=1;a=0
   while p*power<=m:power*=p;a+=1
   c=m//power
   assert oms[m-1]==d-(p-c+1)*p**(k-a-1)
  if d in [4,8,9,16,25,27,32,49]:gaps[d]=[m for m in range(1,d+1) if m>2*p-1 and oms[m-1]<d-math.ceil(d/m)]
  d*=p;k+=1
print('PASS Omega formulas through 2401; actual open gaps',json.dumps(gaps),flush=True)
# Exact finite incidence counts and two-line obstruction words.
for p,k in [(2,2),(2,3),(2,4),(3,2),(3,3),(5,2)]:
 d=p**k;directions=[(s,1) for s in range(d)]+[(1,t) for t in range(0,d,p)]
 assert len(directions)==p**(k-1)*(p+1)
 for x,y in itertools.product(range(d),repeat=2):
  if x==y==0:continue
  z=min(next((v for v in range(k) if x%p**(v+1)),k),next((v for v in range(k) if y%p**(v+1)),k))
  assert sum((a*x+b*y)%d==0 for a,b in directions)==p**z
 step=p**(k-1);word={(step*t,0):1 for t in range(p)};word.update({(step*t,step):-1 for t in range(p)})
 for a,b in directions:
  sums=[0]*d
  for (x,y),v in word.items():sums[(a*x+b*y)%d]+=v
  assert all(v%p==0 for v in sums)
 # For p=2, any <=3 dependence containing zero has all coefficients one.
 if p==2:
  def col(x,y):return sum(1<<(j*d+(a*x+b*y)%d) for j,(a,b) in enumerate(directions))
  columns=[col(x,y) for x,y in itertools.product(range(d),repeat=2)];zero=columns[0]
  assert len(set(columns))==d*d and 0 not in columns
  rest=set(columns[1:]);assert all((zero^x) not in rest for x in rest)
 print('PASS incidence multiplicities and obstruction word',d,'directions',len(directions),'binary min-weight=4' if p==2 else '',flush=True)
# Direct Radon kernel enumeration for p=2,3, via row sums.
for p in [2,3]:
 pts=list(itertools.product(range(p),repeat=2));directions=[(s,1) for s in range(p)]+[(1,0)];minimum=p*p
 for n in range(1,p**(p*p)):
  coeff=[]
  for _ in pts:coeff.append(n%p);n//=p
  w=sum(bool(v) for v in coeff)
  if w>=minimum:continue
  if all(all(sum(c for (x,y),c in zip(pts,coeff) if (a*x+b*y)%p==t)%p==0 for t in range(p)) for a,b in directions):minimum=w
 assert minimum==2*p;print('PASS exhaustive Radon minimum',p,minimum,flush=True)
# Quadratic phases including cyclic wrap, no floating point.
for d,p in [(4,2),(8,2),(9,3),(16,2),(25,5),(27,3)]:
 modulus=2*d if p==2 else d
 quadratic=(lambda s,j:s*j*j) if p==2 else (lambda s,j:s*pow(2,-1,d)*j*j)
 mult=2 if p==2 else 1
 for s,a,j in itertools.product(range(d),repeat=3):
  assert (quadratic(s,(j+a)%d)-quadratic(s,j)-quadratic(s,a)-mult*s*a*j)%modulus==0
 print('PASS exact wrapped quadratic phases',d,d**3,flush=True)
print('ALL INDEPENDENT CHECKS PASS, seconds',time.time()-start,flush=True)
