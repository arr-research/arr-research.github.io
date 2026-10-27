"""Exact finite consistency checks; not a universal proof or research-campaign certificate."""
import sympy as s,json
from pathlib import Path
R=s.Rational;rows=[]
for d in [2,3,4]:
 for L in [R(1,4),R(2,5),R(3,4)]:
  w=(1-L)/d;ls=[(L+j*w)/(L+(j+1)*w) for j in range(d)];S=s.zeros(d);prod=s.Integer(1)
  for j,l in enumerate(ls):
   v=s.eye(d)[:,j];S=l*S+(1-l)*v*v.H;prod*=l
  assert s.simplify(prod-L)==0 and S==w*s.eye(d)
  assert s.simplify(L**2/(L+w)-d*L**2/(1+(d-1)*L))==0
  for i in range(d):
   for j in range(d):
    E=s.zeros(d);E[i,j]=1;out=E
    for a,l in enumerate(ls):
     v=s.eye(d)[:,a];out=l*out+(1-l)*s.trace(out)*v*v.H
    assert s.simplify(out-L*E-s.trace(E)*S)==s.zeros(d)
  rows.append({'d':d,'L':str(L),'lambda_schedule':[str(x) for x in ls],'replacement_min':str(w),'coefficient':str(s.simplify(L**2/(L+w))),'matrix_units':d*d})
unitary=[]
for d in [2,3,4]:
 m=d-1;S=s.zeros(d);V=s.eye(d);L=s.Integer(1);stages=[]
 for j in range(m):
  U=s.zeros(d)
  for i in range(d):U[(i+1)%d,i]=s.I**((i+j)%4)
  assert U.H*U==s.eye(d)
  v=s.eye(d)[:,j];l=R(j+1,j+3);tau=v*v.H;stages.append((l,U,tau));S=l*U*S*U.H+(1-l)*tau;V=U*V;L*=l
 assert S.rank()<=m<d and S.det()==0 and s.trace(S)==1-L
 for i in range(d):
  for j in range(d):
   E=s.zeros(d);E[i,j]=1;out=E
   for l,U,tau in stages:out=l*U*out*U.H+(1-l)*s.trace(out)*tau
   assert s.simplify(out-L*V*E*V.H-s.trace(E)*S)==s.zeros(d)
 unitary.append({'d':d,'stages':m,'rank':S.rank(),'L':str(L),'matrix_units':d*d})
q=R(3,5);v=s.Matrix([q,R(4,5)]);S=R(1,4)*s.diag(1,0)+R(1,2)*v*v.H;a=(3-s.sqrt(1+8*q*q))/8;assert s.simplify((S-a*s.eye(2)).det())==0
out={'scope':'Nine exact orthogonal schedules plus three unitary sequences, matrix-unit composition; finite consistency only','orthogonal':rows,'unitary_depth_obstruction':unitary,'overlap_3_5_min':str(a),'L_1_4_equal_stage_coefficient':str(s.simplify(R(1,16)/(R(1,4)+a))),'symbolic_failures':0}
Path(__file__).with_name('CHECK950.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'exact_schedules':len(rows),'unitary_sequences':len(unitary),'failures':0}))
