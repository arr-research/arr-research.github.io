from pathlib import Path
import sympy as s,json
C=Path(__file__).parent
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
P=[s.diag(1,0),s.diag(0,1)]
ops=[P,[H*p for p in P],[(I+X)/2,(I-X)/2]]
def v(a):return s.Matrix([a[i,j] for j in range(2) for i in range(2)])
def rank(seq):
 words=[I]
 for ks in seq:words=[b*a for b in ks for a in words]
 J=sum((v(a)*v(a).H for a in words),s.zeros(4))
 return int(J.rank()),J
for ks in ops:
 assert sum((a.H*a for a in ks),s.zeros(2))==I
 assert sum((a*a.H for a in ks),s.zeros(2))==I
rows=[]
for phase in range(3):
 for n in range(1,8):
  seq=[ops[(phase+j)%3] for j in range(n)]
  r,J=rank(seq);a,A=rank([[k.H for k in ks] for ks in seq])
  assert r==(2 if n<4-phase else 4)
  assert a==(2 if n<2 else 4)
  if n>=4:assert J==A==s.eye(4)/2
  rows.append({'phase':phase,'length':n,'original_rank':r,'pointwise_adjoint_rank':a})
x={'scope':'Exact supplemental candidate; single active audit; no novelty claim or manuscript grade','base':'Uniform three-cycle; invertible ergodic stationary process','channels':['D_Z','Hadamard after D_Z','D_X'],'normalization':'All CP,TP,unital; both channel and dual faithful','first_and_eventual_original_onsets':[4,3,2],'first_and_eventual_pointwise_adjoint_onsets':[2,2,2],'original_CDF_at2':'1/3','pointwise_adjoint_CDF_at2':'1','analytic_extension':'Bloch maps measure/prepare along Z->Z,Z->X,X->X. An orthogonal adjacent measurement kills the surviving component, producing the complete depolarizer, preserved thereafter by all bistochastic maps.','finite_controls':rows,'all_assertions_pass':True,'review_status':'Unreviewed supplemental candidate'}
(C/'THREE-PHASE1222.json').write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8',newline='\n')
print('21 exact rank controls pass; original onset CDF at2=1/3, pointwise-adjoint CDF=1')
