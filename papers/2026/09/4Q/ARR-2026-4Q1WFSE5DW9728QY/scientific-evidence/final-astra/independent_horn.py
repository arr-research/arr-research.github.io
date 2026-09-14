from functools import lru_cache
from itertools import combinations
from fractions import Fraction as F
from datetime import datetime,timezone
import time
print('UTC',datetime.now(timezone.utc).isoformat(),flush=True)
@lru_cache(None)
def horn(r,d):
 subsets=list(combinations(range(1,d+1),r));by={}
 for K in subsets:by.setdefault(sum(K),[]).append(K)
 inner=[(p,t) for p in range(1,r) for t in horn(p,r)];out=[]
 for I in subsets:
  for J in subsets:
   for K in by.get(sum(I)+sum(J)-r*(r+1)//2,[]):
    if all(sum(I[i-1] for i in X)+sum(J[j-1] for j in Y)<=sum(K[k-1] for k in Z)+p*(p+1)//2 for p,(X,Y,Z) in inner):out.append((I,J,K))
 return tuple(out)
def part(I):return tuple(i-j for i,j in zip(I[::-1],range(len(I),0,-1)))
def lhs(t,s):
 I,J,K=t;d=len(s)+1;return sum(s[i-1] for i in I if i<d)-sum(s[d-j] for j in J if j>1)
def rhs(t,l):return sum(l[k-1] for k in t[2])
def boxes(t):return min(sum(part(t[0])),sum(part(t[1])))
def pieri(t):
 shapes=[tuple(x for x in part(I) if x) for I in t[:2]]
 return boxes(t)==0 or any(len(s)==1 or all(x==1 for x in s) for s in shapes)
t0=time.time();T8=[t for r in range(1,8) for t in horn(r,8)];T9=[t for r in range(1,9) for t in horn(r,9)];assert len(T8)==8752 and len(T9)==39716
print('new scalar Horn recursion counts',len(T8),len(T9),'seconds',round(time.time()-t0,2),flush=True)
T3=[t for t in T9 if boxes(t)<=3];TP=[t for t in T9 if pieri(t)];assert len(T3)==13328 and len(TP)==12798
cases=[(['97/127','163/979','86/1945','29/1445','1/184'],['241/885','479/1954','209/1774'],['97/127','34142468748934736/84409551000378285','479/1954','209/1774','3891/265880','0','0','0'],[3,1,1,2,2,-2,-1,0],T3),(['409/1715','179/878','283/1424','339/1784','203/1202'],['325/1224','495/1963','206/955'],['384815/1072184','325/1224','495/1963','206/955','203/1202','46058/3366545','0','0'],[1,1,2,3,4,-2,-1,0],TP)]
for a,b,s,g,Ts in cases:
 a=list(map(F,a));b=list(map(F,b));b=[sum(a)-sum(b)]+b;s=list(map(F,s));l=a+[-x for x in b[::-1]]
 assert all(x>=y for x,y in zip(s,s[1:])) and s[-1]>=0
 assert all(lhs(t,s)>=rhs(t,l) for t in Ts)
 value=sum(x*y for x,y in zip(g,a+b[:-1]));assert value>sum(s)
 print('independent obstruction',len(Ts),'rows exact gap',value-sum(s),flush=True)
s=[5,3,2,2,1,0,0];l=[5,1,1,1,-2,-2,-2,-2];assert sum(s)==13 and all(lhs(t,s)>=rhs(t,l) for t in T8)
print('independent full-Horn rank5 spectrum witness PASS')
# Verify the four printed additional face inequalities, including their coefficient vectors.
triples=[((1,2),(1,8),(1,8)),((1,2,3,5,6,7),(1,2,3,5,7,8),(1,3,4,6,7,8)),((1,2,5),(1,2,8),(1,4,8)),((1,2,3,5,6),(1,2,3,7,8),(1,3,4,7,8))]
expected=[([0,1,0,0,0,0,0],3),([0,0,1,-1,1,0,0],1),([0,1,0,0,1,0,-1],4),([0,0,1,0,1,0,-1],3)]
for t,(co,rr) in zip(triples,expected):
 assert t in T8 and rhs(t,l)==rr
 for j in range(7):e=[0]*7;e[j]=1;assert lhs(t,e)==co[j]
print('PASS independent face-row coefficients; summed rows force s6=s7=0 and s5>=1 on sum(s)=13')
