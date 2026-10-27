from pathlib import Path
import mpmath as mp,json
P=Path(__file__).parent;iv=mp.iv;iv.dps=260
Z=iv.mpf(0);one=iv.mpf(1)
add=lambda A,B:[[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]
scale=lambda c,A:[[c*A[i][j] for j in range(2)] for i in range(2)]
mul=lambda A,B:[[sum((A[i][k]*B[k][j] for k in range(2)),Z) for j in range(2)] for i in range(2)]
I=[[one,Z],[Z,one]]
def logmatrix(A):
 delta=iv.sqrt((A[0][0]-A[1][1])**2+4*A[0][1]**2);hi=(A[0][0]+A[1][1]+delta)/2
 lo=(A[0][0]*A[1][1]-A[0][1]*A[1][0])/hi
 assert lo.a>0 and (hi-lo).a>0
 return add(scale(iv.log(lo),I),scale((iv.log(hi)-iv.log(lo))/(hi-lo),add(A,scale(-lo,I))))
def pair(W,T,t):
 L=logmatrix(W);out=Z
 for sign in [-1,1]:
  A=add(W,scale(sign*t,T));B=mul(A,add(logmatrix(A),scale(-one,L)));out+=B[0][0]+B[1][1]
 return out
def endpoints(x):return dict(enclosure=str(x),binary_endpoints=[list(t) for t in x._mpi_])
rows=[]
for d in [3,4]:
 a=d-1;e=iv.mpf('1e-30');t=iv.mpf('1e-90');theta=iv.mpf(99)/100;q=a+e*e
 W=lambda p:scale(one/(2*d*q),[[1+(d*a-1)*p,d*p*e*iv.sqrt(a)],[d*p*e*iv.sqrt(a),(2+(d-2)*p)*e*e]])
 T=[[Z,iv.sqrt(a)],[iv.sqrt(a),2*e]]
 for lam,label in [(-one/(d*d-1),'negative_CP_endpoint'),(one/2,'one_half')]:
  before=pair(W(theta),T,t);after=pair(W(lam*theta),T,lam*t);assert before.a>0 and after.a>0
  ratio=after/before;bell=lam*lam*(one*d*d/2)/(1+lam*(one*d*d/2-1));gap=ratio-bell
  assert gap.a>0
  rows.append(dict(d=d,lambda_case=label,input_divergence=endpoints(before),output_divergence=endpoints(after),ratio=endpoints(ratio),Bell_endpoint=endpoints(bell),positive_gap=endpoints(gap),input_and_output_divergence_strictly_positive=True))
out=dict(scope='Four bounded outward-interval logarithmic comparisons for1035, exact binary endpoints retained; not a universal proof, novelty or manuscript score',mpmath_version=mp.__version__,interval_decimal_precision=iv.dps,parameters=dict(e='1/10^30',t='1/10^90',theta='99/100',actual_order_budget='M=d(2d-1)/2; exact positive plane/slack certificates inCHECK1035'),cases=rows,all_passed=True)
(P/'INTERVAL1035.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(dict(cases=len(rows),positive_interval_gaps=True)))
