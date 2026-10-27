from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext
import json
P=Path(__file__).parent;N=300
I=[[F(int(i==j)) for j in range(3)] for i in range(3)]
S=[[F(1,2),F(1,10),F(1,20)],[F(1,10),F(3,10),F(1,25)],[F(1,20),F(1,25),F(1,5)]]
H=[F(0),F(1,2),F(1)]
def add(A,B):return [[A[i][j]+B[i][j] for j in range(3)] for i in range(3)]
def scale(c,A):return [[c*x for x in row] for row in A]
def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def tr(A):return sum(A[i][i] for i in range(3))
K=[[(H[j]-H[i])*S[i][j] for j in range(3)] for i in range(3)] # Z=iK.
# For U_pi=diag(1,-i,-1), only Re(U S U*) enters Tr(rho log S), as log S is real.
Rreal=[[S[0][0],F(0),-S[0][2]],[F(0),S[1][1],F(0)],[-S[2][0],F(0),S[2][2]]]
delta=add(S,scale(-1,Rreal));O=add(scale(F(1,2),S),scale(F(1,6),I))
def evaluate(X,KK,dd,min_eigen):
 B=add(I,scale(-1,X));r=1-min_eigen
 # Gershgorin is an exact positive lower bound; trace1 also implies X<=I.
 assert min(X[i][i]-sum(abs(X[i][j]) for j in range(3) if j!=i) for i in range(3))>=min_eigen>0
 power=I;Y=scale(0,I);du=F(0);g=F(0)
 for k in range(1,N+1):
  Y=add(mul(B,Y),mul(KK,power));power=mul(B,power)
  du-=tr(mul(dd,power))/k;g-=tr(mul(KK,Y))/k
 # ||rho-X||_1<=2; log tail bounded in operator norm.
 ed=2*r**(N+1)/((N+1)*(1-r))
 # Frechet derivative tail: each k-term average <=||Z||_HS² r^(k-1).
 hs=sum(v*v for row in KK for v in row);eg=hs*r**N/(1-r)
 return (du-ed,du+ed),(g-eg,g+eg)
di,gi=evaluate(S,K,delta,F(11,100));do,go=evaluate(O,scale(F(1,2),K),scale(F(1,2),delta),F(133,600))
assert min(di+gi+do+go)>0
ratio=lambda a,b:(a[0]/b[1],a[1]/b[0])
rf=ratio(do,di);rg=ratio(go,gi);gap=(rf[0]-rg[1],rf[1]-rg[0]);assert gap[0]>0
def save(v):
 with localcontext() as c:
  c.prec=40;shown=[str(Decimal(x.numerator)/Decimal(x.denominator)) for x in v]
 return {'rational_endpoints':[str(x) for x in v],'display_only':shown}
out={'scope':'Certified falsifier of extending finite-phase Umegaki retention = local BKM retention to every unitary orbit. Does not refute special1051.',
 'sigma':'[[1/2,1/10,1/20],[1/10,3/10,1/25],[1/20,1/25,1/5]]','H':'diag(0,1/2,1)','U_pi':'diag(1,-i,-1)','lambda':'1/2','R':1,
 'method':'Exact rational matrix log/Frechet series in I-X with300terms; Gershgorin eigenvalue lower bounds11/100 and133/600; rigorous operator-norm tail bounds',
 'input_DU':save(di),'output_DU':save(do),'input_BKM':save(gi),'output_BKM':save(go),'finite_retention':save(rf),'BKM_retention':save(rg),'positive_difference':save(gap)}
(P/'FALSIFIER1054.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:out[k]['display_only'] for k in ['finite_retention','BKM_retention','positive_difference']}))
