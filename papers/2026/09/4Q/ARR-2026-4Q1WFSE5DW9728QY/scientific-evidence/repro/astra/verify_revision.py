"""Bounded author-side revision replay. No pickle deserialization or network access.
The generator is copied from inspected submitted source, not claimed independently implemented.
All proof assertions below use integers/Fractions; LP is not used.
"""
from pathlib import Path
from fractions import Fraction as Q
import json
import numpy as np
from safe_horn import HornLP,lr_coeff,part

D=Path(__file__).resolve().parent
H8=HornLP(8);lam8=np.array([5,1,1,1,-2,-2,-2,-2]);s8=np.array([5,3,2,2,1,0,0])
assert np.min(H8.A@s8-H8.B@lam8)>=0 and sum(s8)==13
for cert in json.loads((D/'d8-exact-face-certificates.json').read_text()):
 lhs=[Q(0)]*7;rhs=Q(0)
 for row in cert['rows']:
  w=Q(row['weight']);assert w<=0
  inf=row['horn'];assert inf is not None
  I,J,K=map(tuple,(inf['I'],inf['J'],inf['K']))
  found=[i for i,x in enumerate(H8.info) if (x['I'],x['J'],x['K'])==(I,J,K)]
  assert len(found)==1;k=found[0]
  assert lr_coeff(part(I),part(J),part(K))>0
  assert row['A']==[-int(v) for v in H8.A[k]]
  assert row['b']==-int(H8.B[k]@lam8)
  lhs=[x+w*a for x,a in zip(lhs,row['A'])];rhs+=w*row['b']
 v=Q(cert['equality_weight']);z=list(map(Q,cert['lower_weights']))
 assert all(x>=0 for x in z)
 lhs=[x+v+zz for x,zz in zip(lhs,z)];rhs+=13*v
 assert lhs==list(map(Q,cert['objective'])) and rhs==Q(cert['bound'])
 print('PASS exact d8 face dual',cert['objective'],'>=',str(rhs))
print('PASS exact full-Horn integer rank-five witness; every optimizer has s5>=1 and s6=s7=0.')
H=HornLP(9);assert H.ntri==39716
pieri=np.array([x['box']==0 or len(x['lI'])==1 or all(y==1 for y in x['lI']) or len(x['lJ'])==1 or all(y==1 for y in x['lJ']) for x in H.info])
assert sum(pieri)==12798 and sum(H.box<=3)==13328
points=[
(['97/127','163/979','86/1945','29/1445','1/184'],['241/885','479/1954','209/1774'],['97/127','34142468748934736/84409551000378285','479/1954','209/1774','3891/265880','0','0','0'],['97/127','6197804698803613139/15531357384069604440','479/1954','209/1774','29/1445','1/184','0','0'],(3,1,1,2,2,-2,-1,0),'g',H.box<=3),
(['409/1715','179/878','283/1424','339/1784','203/1202'],['325/1224','495/1963','206/955'],['384815/1072184','325/1224','495/1963','206/955','203/1202','46058/3366545','0','0'],['384815/1072184','325/1224','495/1963','206/955','203/1202','14405079691/564562863410','0','0'],(1,1,2,3,4,-2,-1,0),'gprime',pieri)]
certs=[[
((1,),(1,),(1,)),(tuple(range(1,9)),(1,2,3,4,5,6,8,9),(1,2,3,4,5,6,8,9)),
(tuple(range(1,9)),(1,2,3,4,5,7,8,9),(1,2,3,4,5,7,8,9)),((1,2,5,6),(1,2,3,9),(1,4,5,9))],
[((5,),(1,),(5,)),((1,5),(1,5),(4,5)),((1,2,5,6),(1,2,5,9),(3,4,5,9)),
(tuple(range(1,9)),(1,2,3,4,5,6,8,9),(1,2,3,4,5,6,8,9)),(tuple(range(1,9)),(1,2,3,4,5,7,8,9),(1,2,3,4,5,7,8,9))]]
def verify_feasible(ss,lam,select):
 assert all(x>=y for x,y in zip(ss,ss[1:])) and ss[-1]>=0
 for k in np.flatnonzero(select):
  assert sum(int(v)*x for v,x in zip(H.A[k],ss))>=sum(int(v)*x for v,x in zip(H.B[k],lam))
for ii,(aa,bb,ss,ff,g,label,sel) in enumerate(points):
 a=list(map(Q,aa));b=list(map(Q,bb));b=[sum(a)-sum(b)]+b;lam=a+[-x for x in b[::-1]]
 assert min(a+b)>0 and all(x>=y for x,y in zip(a,a[1:])) and all(x>=y for x,y in zip(b,b[1:]))
 gval=sum(v*x for v,x in zip(g[:5],a))+sum(v*x for v,x in zip(g[5:],b))
 sq=list(map(Q,ss));verify_feasible(sq,lam,sel);assert sum(sq)<gval
 full=list(map(Q,ff));verify_feasible(full,lam,np.ones(H.ntri,bool));assert sum(full)==gval
 coef=np.zeros(8,dtype=int);rhs=np.zeros(9,dtype=int)
 for I,J,K in certs[ii]:
  assert lr_coeff(part(I),part(J),part(K))==1
  kk=[k for k,x in enumerate(H.info) if (x['I'],x['J'],x['K'])==(I,J,K)];assert len(kk)==1;k=kk[0]
  coef+=H.A[k].astype(int);rhs+=H.B[k].astype(int)
 # lambda=(a1..a5,-b4,-b3,-b2,-b1), eliminate b4 using trace.
 ab=list(rhs[:5])+list(-rhs[5:][::-1]);c4=ab[-1]
 canonical=tuple(x+c4 for x in ab[:5])+tuple(x-c4 for x in ab[5:8])
 assert canonical==g and max(coef)<=1 and all(x==1 for x in coef[:5])
 print('PASS exact',label,'restricted rows',int(sum(sel)),'gap',str(gval-sum(sq)),'full-Horn equality and LR tiling')
 if ii==1:
  box3=list(map(Q,['384815/1072184','142327501/513155880','495/1963','643050479/2955826510','203/1202','0','0','0']))
  verify_feasible(box3,lam,H.box<=3);assert sum(box3)<gval
  print('PASS exact gprime box<=3 obstruction')
print('ALL REVISION CHECKS PASSED. No complete catalogue/exposed-chamber claim is certified.')
