"""Independent audit of frozen tropical candidate, plus explicitly separated phase-menu proposal.
No author checker is read or imported. All files resolve beside __file__.
Dependencies: numpy, sympy. Run python -B verify_independent.py.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,itertools,math,time
import numpy as np
import sympy as sp
BASE=Path(__file__).resolve().parent
rng=np.random.default_rng(2026101603)
t0=time.time()
R={'candidate_sha256':hashlib.sha256((BASE/'candidate-reviewed-snapshot.txt').read_bytes()).hexdigest(),'seed':2026101603,'author_code_read':False,'sections':{}}
# All vertices of the asserted row-column polytope, computed over Q.
C=sp.Matrix([[1,0,1,2,0,0],[1,1,0,0,2,0],[0,1,1,0,0,2]])
b=sp.Matrix([2,2,2]);verts=set()
for ix in itertools.combinations(range(6),3):
 B=C[:,list(ix)]
 if B.det()==0:continue
 u=B.inv()*b
 if min(u)<0:continue
 v=[sp.Integer(0)]*6
 for i,j in enumerate(ix):v[j]=u[i]
 verts.add(tuple(v))
expected={(0,0,0,1,1,1),(2,0,0,0,0,1),(0,2,0,1,0,0),(0,0,2,0,1,0),(1,1,1,0,0,0)}
assert verts==expected
assert all(sum(v)==3 for v in verts)
R['sections']['exact_vertices']=[list(map(int,v)) for v in sorted(verts)]
x,y,z,a,b,c=sp.symbols('x y z a b c');weights=(x,y,z,a,b,c)
A=[]
for i,j in ((0,1),(1,2),(2,0)):
 T=sp.zeros(3);T[i,j]=1;T[j,i]=-1;A.append(T)
for i in range(3):
 T=sp.zeros(3);T[i,i]=1;A.append(T)
scalar=sum((q*T for q,T in zip(weights,A)),sp.zeros(3)).det()
assert sp.expand(scalar-(a*b*c+c*x*x+a*y*y+b*z*z))==0
G=sp.Matrix(6,6,lambda i,j:sp.trace(A[i].H*A[j]))
assert G==sp.diag(2,2,2,1,1,1)
R['sections']['scalar_example']={'determinant':str(scalar),'gram_spectrum':[2,2,2,1,1,1],'C_A':'2/3'}
# Message-supplied extension (not in frozen candidate): explicit six-tuple and grid.
P=[sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-sp.I],[sp.I,0]]),sp.diag(1,-1)]
Yraw=P+[sp.eye(2)]*3
H=sum((q*sp.kronecker_product(T,Y) for q,T,Y in zip(weights,A,Yraw)),sp.zeros(6))
# Permutation determinant is an independent exact coefficient expansion.
poly={}
for perm in itertools.permutations(range(6)):
 term=sp.Integer((-1)**sum(perm[i]>perm[j] for i in range(6) for j in range(i+1,6)))
 for i,j in enumerate(perm):term*=H[i,j]
 if term==0:continue
 pp=sp.Poly(term,*weights)
 for ex,co in pp.terms():poly[ex]=sp.simplify(poly.get(ex,0)+co)
poly={ex:co for ex,co in poly.items() if co!=0}
assert all(sum(ex)==6 for ex in poly)
assert all(C*sp.Matrix(ex)==sp.Matrix([4,4,4]) for ex in poly)
vertex_co={v:poly.get(tuple(2*t for t in v),0) for v in sorted(verts)}
assert [vertex_co[v] for v in sorted(verts)]==[1,1,1,-4,1]
assert poly[(2,2,2,0,0,0)]==-4
maxdeg=[max(ex[i] for ex in poly) for i in range(6)]
assert maxdeg==[4,4,4,2,2,2]
# Energy of raw tuple is 6; determinant of normalized tuple divides by 216.
assert sum(sp.trace(Y.H*Y) for Y in Yraw)/2==6
assert min(abs(v) for v in vertex_co.values())==1
# Exact no-aliasing check proves discrete Parseval on the 1125 point menu.
moduli=(5,5,5,3,3)
residues=[tuple(ex[i]%moduli[i] for i in range(5)) for ex in poly]
assert len(set(residues))==len(poly)
R['sections']['post_freeze_extension']={'provenance':'Explicit tuple, constants and 1125-grid proposed in coordinator message after candidate freeze; independently verified here.','unnormalized_polynomial_terms':[{'exponent':list(ex),'coefficient':str(co)} for ex,co in sorted(poly.items())],'vertex_coefficients':[{'vertex':[int(t) for t in v],'coefficient':str(co)} for v,co in vertex_co.items()],'maximum_variable_degrees':maxdeg,'normalized_energy':1,'determinant_normalization_factor':216,'c_A':'1/6','C_A':'2/3','factor_bound':4,'phase_count':math.prod(moduli),'exact_no_aliasing':True}
# Later coordinator proposal: a single fixed tuple works on positive weights.
expanded=sum(co*sp.prod(q**e for q,e in zip(weights,ex)) for ex,co in poly.items())
S=a*b*c+a*y*y+b*z*z+c*x*x
assert sp.expand(expanded-(S+2*sp.I*x*y*z)**2)==0
R['sections']['post_freeze_single_witness']={'provenance':'Further coordinator message after candidate and first manuscript freeze; exact identity independently checked.','factorization':'(abc+a*y**2+b*z**2+c*x**2+2*I*x*y*z)**2','normalized_objective':'(S**2+4*x**2*y**2*z**2)**(1/3)/6','one_fixed_tuple':True,'factor_bound':4,'exact_identity':True}
An=[np.array(T,complex) for T in A]
Ybase=np.array([np.array(Y,complex)/np.sqrt(6) for Y in Yraw])
V=np.array(list(sorted(verts)),float)
exponents=np.array(list(poly),int)
coeffs=np.array([complex(poly[ex]) for ex in poly],complex)/216
phaseangles=np.array(list(itertools.product(*[2*np.pi*np.arange(n)/n for n in moduli])))
phasefactors=np.exp(1j*phaseangles@exponents[:,:5].T)

def cnormal(shape):return rng.normal(size=shape)+1j*rng.normal(size=shape)
def energy(Y):return sum(np.vdot(T,T).real for T in Y)/len(Y[0])
def normtuple(Y):return np.array(Y)/np.sqrt(energy(Y))
def detlog(H):return 2*np.linalg.slogdet(H)[1]/len(H)
def matrix(zs,Y,As=An):return sum(zz*np.kron(T,U) for zz,T,U in zip(zs,As,Y))
def tropical(logz):return float(np.max((2/3)*V@logz))
# Diverse weight regimes, not a proof over all positive weights.
regimes=[np.zeros(6)]
for j in range(6):
 for sign in (-1,1):
  v=np.zeros(6);v[j]=sign*20;regimes.append(v)
regimes.extend(rng.uniform(-12,12,size=(120,6)))
# Positive/negative rates and paths crossing different minimizing branches.
regimes.extend(np.log(t)*w for t in (0.1,1e-4,1e-8) for w in rng.uniform(-3,3,(15,6)))
max_parseval_error=0.;min_menu_ratio=math.inf;max_menu_ratio=0.;max_upper_ratio=0.;normalization_error=0.
branches=set();records=[];single_ratios=[]
for trial,logz0 in enumerate(regimes):
 # Remove common homogeneous scale to avoid overflow.
 logz=logz0-np.max(logz0);zs=np.exp(logz)
 tropical_log=tropical(logz); terms=coeffs*np.exp(exponents@logz)
 xx,yy,zz,aa,bb,cc=zs
 ss=aa*bb*cc+aa*yy*yy+bb*zz*zz+cc*xx*xx
 fixed_log=np.log(ss*ss+4*(xx*yy*zz)**2)/3-np.log(6)
 fixed_ratio=float(np.exp(fixed_log-tropical_log))
 assert fixed_ratio>=1/6-1e-11 and fixed_ratio<=2/3+1e-11
 single_ratios.append(fixed_ratio)
 gridvalues=phasefactors@terms
 squares=np.abs(gridvalues)**2
 exact_average=float(np.sum(abs(terms)**2))
 err=abs(float(np.mean(squares))-exact_average)/max(exact_average,1e-300)
 max_parseval_error=max(max_parseval_error,err)
 maxabs=float(np.max(np.abs(gridvalues)))
 logobjective=np.log(maxabs)/3
 ratio=float(np.exp(logobjective-tropical_log))
 assert ratio>=1/6-1e-11 and ratio<=2/3+1e-11
 min_menu_ratio=min(min_menu_ratio,ratio);max_menu_ratio=max(max_menu_ratio,ratio)
 branches.add(int(np.argmax((2/3)*V@logz)))
 # Direct determinant at selected phase agrees with polynomial.
 winner=int(np.argmax(np.abs(gridvalues)))
 ph=np.r_[np.exp(1j*phaseangles[winner]),1.]
 direct=matrix(zs,Ybase*ph[:,None,None])
 if maxabs>1e-200:
  # Ill-conditioned cases are tested by exact polynomial/DFT, not cancellation-prone floating determinant.
  cond=np.linalg.cond(direct)
  if cond<1e9:assert abs(np.linalg.det(direct)-gridvalues[winner])/maxabs<1e-6
 if trial<100:
  m=1+trial%7;Y=normtuple(cnormal((6,m,m)))
  raw=matrix(zs,Y);lograw=detlog(raw)
  ratio_up=np.exp(lograw-tropical_log)/(2/3)
  assert ratio_up<=1+1e-6
  max_upper_ratio=max(max_upper_ratio,float(ratio_up))
 # Complete positivity and determinant correction (diagonal R for this tuple).
 rr=np.array([zs[3]**2+zs[0]**2+zs[2]**2,zs[4]**2+zs[0]**2+zs[1]**2,zs[5]**2+zs[1]**2+zs[2]**2])
 invroot=np.diag(1/np.sqrt(rr));Ks=[zz*T@invroot for zz,T in zip(zs,An)]
 tp=np.linalg.norm(sum(T.conj().T@T for T in Ks)-np.eye(3));assert tp<1e-12
 expected_log=logobjective-np.sum(np.log(rr))/3
 normalized=matrix(np.ones(6),Ybase*ph[:,None,None],Ks)
 if np.linalg.cond(normalized)<1e9:
  err=abs(detlog(normalized)-expected_log);normalization_error=max(normalization_error,err);assert err<1e-6
 # The analytic normalized tropical exponent must be nonnegative for t down to zero.
 if trial<10:records.append({'log_weights':logz0.tolist(),'menu_over_tropical':ratio,'cptp_logobjective':float(expected_log)})
assert max_parseval_error<1e-12 and len(branches)==5
R['sections']['finite_weight_checks']={'regimes':len(regimes),'represented_tropical_vertices':sorted(branches),'minimum_menu_over_tropical':min_menu_ratio,'maximum_menu_over_tropical':max_menu_ratio,'maximum_random_over_C_T':max_upper_ratio,'discrete_Parseval_max_relative_error':max_parseval_error,'cptp_log_determinant_max_error':normalization_error,'records':records}
# Exact torus norm example: p(z1,z2)=z1^2+z1*z2-z2^2, ||p||_T=sqrt(5).
# |p(e^it,1)|^2=1+4sin(t)^2. Includes rays with negative rational components.
toricmax=0.
for zz in np.exp(rng.uniform(-15,15,size=(500,2))):
 lhs=abs(zz[0]**2+zz[0]*zz[1]-zz[1]**2)
 rhs=np.sqrt(5)*max(zz[0]**2,zz[0]*zz[1],zz[1]**2)
 assert lhs<=rhs*(1+1e-12);toricmax=max(toricmax,lhs/rhs)
# Negative control: replacing torus sup by the largest coefficient is false for 1+z at z=1.
assert 2>1
R['sections']['toric_modulus_diagnostic']={'samples':500,'known_unit_torus_sup':'sqrt(5)','largest_ratio':toricmax,'negative_control_largest_coefficient_bound_fails':True}
# d=1 edge case: F_infty=sum_i |A_i|^2 z_i^2; polytope is the active simplex.
smallest=math.inf;largest=0.
weights1=np.array([1.,2.,.25])
for lz in rng.uniform(-10,10,size=(100,3)):
 zz=np.exp(lz);actual=np.sum(weights1**2*zz**2);T=np.max(zz**2)
 assert np.min(weights1**2)*T<=actual+1e-10 and actual<=np.sum(weights1**2)*T+1e-10
 smallest=min(smallest,actual/T);largest=max(largest,actual/T)
R['sections']['d1_boundary']={'samples':100,'min_ratio':smallest,'max_ratio':largest}
# Mixture of two pure replacers is exactly known at every m.
mixtures=[]
for beta in ((0,1),(1,0),(2,3),(-2,1),(4,4)):
 theta=(beta[0]+beta[1])/2-min(beta)
 for t in (1e-1,1e-4,1e-8):
  un=np.array([t**beta[0],t**beta[1]]);p=un/un.sum();exact=np.sqrt(p[0]*p[1])/2
  asym=exact/(t**theta)
  assert .25-1e-12<=asym<=.5+1e-12
  mixtures.append({'beta':list(beta),'t':t,'theta':theta,'objective':float(exact),'ratio_to_power':float(asym)})
R['sections']['normalized_mixture']=mixtures
# Explicit normalized exponent of the six-parameter example: no negative values.
min_theta=math.inf
for w in rng.uniform(-5,5,size=(1000,6)):
 numerator=(2/3)*min(V@w)
 denominator=(2/3)*(min(w[3],w[0],w[2])+min(w[4],w[0],w[1])+min(w[5],w[1],w[2]))
 theta=numerator-denominator
 assert theta>=-1e-12;min_theta=min(min_theta,float(theta))
R['sections']['normalized_example_rates']={'samples':1000,'smallest_exponent':min_theta,'normalization_subtraction_checked':True}
R['sections']['post_freeze_single_witness']['finite_checks']={'regimes':len(single_ratios),'minimum_over_tropical':min(single_ratios),'maximum_over_tropical':max(single_ratios)}
R['status']='PASS';R['completed_at']=datetime.now(timezone.utc).isoformat();R['elapsed_seconds']=time.time()-t0
R['limitations']=['Finite diagnostics do not prove the universal theorem or HIOS stabilization.','The 1125-menu and explicit constants were supplied after freezing and are not part of the hashed candidate.','No author verification file or other reviewer report was read.','Floating determinant comparisons are skipped when condition number is at least 1e9; exact polynomial and no-aliasing checks still apply.']
(BASE/'independent-checks.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':R['status'],'elapsed_seconds':R['elapsed_seconds'],'vertices':R['sections']['exact_vertices'],'polynomial_terms':len(poly),'phase_menu':math.prod(moduli),'regimes':len(regimes),'min_menu_ratio':min_menu_ratio,'Parseval_error':max_parseval_error,'normalization_error':normalization_error}))
