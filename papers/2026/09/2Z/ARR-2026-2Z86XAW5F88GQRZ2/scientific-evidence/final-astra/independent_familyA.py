from datetime import datetime,timezone
print('UTC',datetime.now(timezone.utc).isoformat())
count=0
for m in range(3,31):
 for u2 in range(m):
  for u3 in range(u2,m):
   sched=[0,u2,u3];layers={};nexta=1;u=1
   while nexta<=m:
    c=sum(t<u for t in sched);take=min(c,m-nexta+1);layers[u]=list(range(nexta,nexta+take));nexta+=take;u+=1
   T=u-1
   if max(sched)>=T or any(len(a)+sum(t==j for t in sched)>3 for j,a in layers.items()):continue
   for z in range(6):
    d=m+3+z;coef=[0]*(d+1);rhs=[0]*(d+1)
    for u,aa in layers.items():
     t=min(aa);B={d-i for i,at in enumerate(sched) if at<u};c=len(B)
     if u<T or t+c-1<=m+z:
      K=set(range(t,d+1))-B;r=len(K);I=K;J=set(range(1,r+1));assert 1<=r<d
      for i in I:
       if i<d:coef[i]+=1
      for j in J:
       if j>1:coef[d+1-j]-=1
      for k in K:rhs[k]+=1
     else:
      for j in aa:coef[j]+=1;rhs[j]+=1
    # expected raw coefficients: each a has its layer, each -b its layer
    alevel={j:u for u,aa in layers.items() for j in aa};actual=[rhs[j]-rhs[d-2] for j in range(1,m+1)]+[-rhs[d]+rhs[d-2],-rhs[d-1]+rhs[d-2]]
    expected=[alevel[j]-sched[2] for j in range(1,m+1)]+[sched[2]-sched[0],sched[2]-sched[1]]
    assert actual==expected and max(coef[1:d])<=1
    count+=1
print('PASS newly coded family-A tile bookkeeping',count,'instances, m3..30 z0..5')
