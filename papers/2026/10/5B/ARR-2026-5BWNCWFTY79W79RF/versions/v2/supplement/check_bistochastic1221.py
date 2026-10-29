from pathlib import Path
import sympy as s,json,hashlib
C=Path(__file__).parent
P=[s.diag(1,0),s.diag(0,1)]
H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
Q=[H*p for p in P]
def vec(a):return s.Matrix([a[i,j] for j in range(2) for i in range(2)])
def words(seq):
 out=[s.eye(2)]
 for ks in seq:out=[b*a for b in ks for a in out]
 return out
def choi(seq):return sum((vec(a)*vec(a).H for a in words(seq)),s.zeros(4))
for ks in [P,Q]:
 assert sum((a.H*a for a in ks),s.zeros(2))==s.eye(2)
 assert sum((a*a.H for a in ks),s.zeros(2))==s.eye(2)
rows=[]
for phase in [0,1]:
 for n in range(1,9):
  seq=[[P,Q][(phase+j)%2] for j in range(n)]
  j=choi(seq);a=choi([[k.H for k in ks] for ks in seq])
  rank=int(j.rank());adjrank=int(a.rank())
  expected=(2 if n<(3 if phase==0 else 2) else 4)
  expected_adj=(2 if n<(2 if phase==0 else 3) else 4)
  assert rank==expected and adjrank==expected_adj
  if n>=3:assert j==a==s.eye(4)/2
  rows.append({'phase':phase,'steps':n,'choi_rank':rank,'pointwise_adjoint_choi_rank':adjrank})
x={'scope':'Additional exact candidate control for the same one running component audit; no new reviewer or grade','base':'Two-point uniform probability space with ergodic invertible swap','phase0':'Dephasing D_Z with Kraus P0,P1','phase1':'Hadamard after D_Z with Kraus H P0,H P1','both_channels':'CP,TP,unital; both channel and dual are faithful','source':'arXiv2607.01446v1 AppendixA definitions and LemmaA.1','chronological_convention':'Later Kraus matrix multiplies on the left','phase0_onsets':{'original_first_and_eventual':3,'pointwise_adjoint_first_and_eventual':2},'phase1_onsets':{'original_first_and_eventual':2,'pointwise_adjoint_first_and_eventual':3},'analytic_extension':'D_Z composed with H composed with D_Z is the complete depolarizer. After first depolarizing block, all later bistochastic steps preserve it.','finite_controls':rows,'all_assertions_pass':True,'no_independent_verdict_yet':True}
(C/'BISTOCHASTIC1221.json').write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'controls':len(rows),'status':'exact ranks and bistochasticity pass','onsets':'phase0 original3 adjoint2; phase1 original2 adjoint3'}))
