from itertools import product
from datetime import datetime,timezone
print('UTC',datetime.now(timezone.utc).isoformat())
count=late=0
for m in range(1,8):
 for n in range(1,5):
  for sched in product(range(m+1),repeat=n):
   if min(sched)!=0:continue
   layers={};j=1;u=1
   while j<=m:
    cap=sum(t<u for t in sched);take=min(cap,m-j+1);layers[u]=list(range(j,j+take));j+=take;u+=1
   T=u-1
   if max(sched)>T:continue
   for z in [0,2]:
    d=m+n+z;sc=[0]*(d+1);rc=[0]*(d+1)
    for u,aa in layers.items():
     if u==T:
      for i in aa:sc[i]+=1;rc[i]+=1
     else:
      B={d-i for i,t in enumerate(sched) if t<u};K=set(range(min(aa),d+1))-B;r=len(K);assert 1<=r<d
      for i in K:
       rc[i]+=1
       if i<d:sc[i]+=1
      for j in range(2,r+1):sc[d+1-j]-=1
    assert sc[1:m+1]==[1]*m and max(sc[1:d])<=1
    for u,aa in layers.items():
     assert all(rc[j]==u for j in aa)
    assert all(rc[d-i]==t-int(t==T) for i,t in enumerate(sched))
    count+=1;late+=int(max(sched)==T)
print('PASS independent ordered full-capacity certificate bookkeeping',count,'cases; late-final-negative cases',late)
print('Codimension clarification: m=n=2, fixed admissible schedule (1,0), L={-b2}{a1,-b1}{a2}.')
print('Every balanced path system forces b2=a1 and b1=a2. Ordering a1>=a2, b1>=b2 then forces all four equal.')
print('On the trace hyperplane of dimension3 the aligned set is dimension1 (codimension2), not n-1=1. Additivity theorem remains true.')
