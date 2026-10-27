from pathlib import Path
import sympy as s,json
P=Path(__file__).parent;rows=[]
# Independent full restricted-form test instead of testing individual random tangents.
for n in [2,3,4,9,16]:
 families={'uniform':[s.Rational(1,n)]*n,'dominant':[s.Rational(99,100)]+[s.Rational(1,100*(n-1))]*(n-1),'half':[s.Rational(1,2)]+[s.Rational(1,2*(n-1))]*(n-1)}
 if n>2:families['near_two_ray']=[s.Rational(49999,100000)]*2+[s.Rational(1,50000*(n-2))]*(n-2)
 Q=s.eye(n)[:,:n-1]
 for j in range(n-1):Q[n-1,j]=-1
 for label,r in families.items():
  F=Q.T*s.diag(*[1/x-1/(1-x) for x in r])*Q
  if n==2:assert F==s.zeros(1);piv=['0']
  else:
   L,V=F.LDLdecomposition();assert L*V*L.T==F;assert all(x>0 for x in V.diagonal());piv=[str(x) for x in V.diagonal()]
  rows.append({'name':'whole_tangent_space','n':n,'family':label,'LDL_pivots':piv,'positive_semidefinite':True})
for n in [4,9,16,25]:
 for a in [s.Rational(49,100),s.Rational(49999,100000)]:
  q=[a,a]+[(1-2*a)/(n-2)]*(n-2);t=s.Rational(1,1000000);p=q.copy();p[0]+=t;p[1]-=t
  o=lambda r:[(1-x)/(n-1) for x in r]
  tri=lambda p,q:sum((x-y)**2/(x+y) for x,y in zip(p,q))
  chi=lambda p,q:sum((x-y)**2/y for x,y in zip(p,q))
  rt=s.factor(tri(o(p),o(q))/tri(p,q));rc=s.factor(chi(o(p),o(q))/chi(p,q));target=a/((n-1)*(1-a))
  assert rc==target and rt<=s.Rational(1,n-1)
  rows.append({'name':'finite_two_ray','n':n,'a':str(a),'t':str(t),'chi_ratio':str(rc),'triangle_ratio':str(rt),'benchmark':str(s.Rational(1,n-1))})
# Exact Weyl-Bell embedding and marginal/channel checks, including complex basis d3.
for d in [2,3]:
 n=d*d;omega=-1 if d==2 else (-1+s.sqrt(3)*s.I)/2;vecs=[]
 for shift in range(d):
  for phase in range(d):
   v=s.zeros(n,1)
   for j in range(d):v[j*d+(j+shift)%d]=omega**(phase*j)/s.sqrt(d)
   vecs.append(v)
 V=s.simplify(s.Matrix.hstack(*vecs));assert s.simplify(V.H*V)==s.eye(n)
 pt=lambda X:s.Matrix(d,d,lambda j,k:sum(X[i*d+j,i*d+k] for i in range(d)))
 lam=-s.Rational(1,n-1)
 for v in vecs:
  pr=s.simplify(v*v.H);assert s.simplify(pt(pr))==s.eye(d)/d
  out=s.simplify(lam*pr+(1-lam)*s.eye(n)/n)
  assert s.simplify(out-(s.eye(n)-pr)/(n-1))==s.zeros(n)
 rows.append({'name':'quantum_Bell_embedding','d':d,'orthonormal_ME_basis':True,'all_projectors_uniform_marginal':True,'channel_complement_identity':True})
(P/'BELL1054.json').write_text(json.dumps({'records':rows,'all_passed':True,'universal_inequality':'Analytic reconstruction in AUDIT1054, not finite checks alone'},indent=2)+'\n',encoding='utf-8')
print('Whole tangent-space rational LDL, finite two-ray and complex Weyl-Bell checks passed.')
