from pathlib import Path
import json,hashlib
import sympy as s
C=Path(__file__).parent;I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
E=lambda i,j:s.eye(2)[:,i]*s.eye(2)[:,j].T
def choi(ks):
 return sum((k.reshape(4,1)*k.reshape(4,1).conjugate().T for k in ks),s.zeros(4))
def channel(ks,a):return sum((k*a*k.conjugate().T for k in ks),s.zeros(2))
def tp(ks):return s.simplify(sum((k.conjugate().T*k for k in ks),s.zeros(2)))==I
reset=[E(0,0),E(0,1)];assert tp(reset);pure=E(0,0);Jreset=choi(reset);assert Jreset.rank()==2
prefixes={'identity':[I],'dephasing':[E(0,0),E(1,1)],'complete_depolarizer':[E(i,j)/s.sqrt(2) for i in range(2) for j in range(2)],'Hadamard':[H]}
last_map=[]
for name,pre in prefixes.items():
 assert tp(pre);ks=[a*b for a in reset for b in pre];J=choi(ks);assert J.rank()==2 and J==Jreset
 last_map.append({'prefix':name,'rank_final_choi':J.rank(),'last_local_output_rank':channel(reset,I).rank(),'meaning':'Singular last-map output forces singular full-composition Choi; prefix need not have a common kernel'})
assert channel([I],I).rank()==2 and choi([I]).rank()==1
nonstationary=[]
for n in [1,2,4,8]:
 eps=s.Rational(1,2**(n+1));Z=s.diag(1-eps,eps);assert Z.det()>0;delta=[s.sqrt(Z[i,i])*E(i,j) for i in range(2) for j in range(2)]
 assert choi(delta)==s.kronecker_product(Z,I);err=2*eps
 nonstationary.append({'n':n,'faithful_target':str(Z),'exact_replacement_map_norm_error':str(err),'rank_actual_choi':2,'assumption_violated':'Target sequence is not stationary under a probability-preserving base; it tends to a pure state'})
amplitude=[]
for n in [1,2,4,8]:
 a=s.Rational(1,2)**n;ks=[s.diag(1,s.sqrt(a)),s.sqrt(1-a)*E(0,1)];assert tp(ks);J=choi(ks);assert J.rank()==2
 amplitude.append({'n':n,'survival_probability':str(a),'rank_choi':J.rank(),'local_output_positive':True,'assumption_violated':'Limit replacement state is pure, not faithful; entrywise Choi convergence therefore gives no full-rank onset'})
out={'status':'Exact finite controls, not general theorem audit or novelty certificate','local_last_map_obstruction':last_map,'converse_shortcut_refuted':'Phi(I)>0 does not imply full Choi rank: identity channel has ranks2 and1 respectively','nonstationary_faithful_targets_ablation':nonstationary,'nonfaithful_limit_ablation':amplitude,'all_length_formulas':'Reset is idempotent; AD survives with a_n=2^-n, rank2 for every finite n. Exact replacement error2epsilon_n follows from trace-functional norm1. Finite sample rows illustrate these algebraic formulas; no extrapolation-based proof.','new_paper':False,'new_score':False}
(C/'CONTROLS1236.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
