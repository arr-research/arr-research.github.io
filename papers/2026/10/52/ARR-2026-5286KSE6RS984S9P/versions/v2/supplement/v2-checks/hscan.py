import numpy as np
H=lambda a,c,s:(1-2*s/(1-a))**30*(1-2*s/(1-c))**4
s=np.linspace(0,1,200001)
print('H*(1/16)',H(-2/3,3/4,1/16),'H*(5/24)',H(-2/3,3/4,5/24),'H*(1)',H(-2/3,3/4,1),'(3/4)^30(2/3)^4',0.75**30*(2/3)**4,'7^4/5^30',7**4/5**30)
m=H(-2/3,3/4,s[s>=1/16]).max(); print('sup on [1/16,1]',m, 'at', s[s>=1/16][H(-2/3,3/4,s[s>=1/16]).argmax()])
# box scan
eta=0.02;worst=0;worstlog=-1e9
for a in np.linspace(-2/3-eta,-2/3+eta,9):
  for c in np.linspace(0.75-eta,0.75+eta,9):
    hh=H(a,c,s[s>=1/16]); worst=max(worst,hh.max())
    ss=s[(s>0)&(s<=1/16)]
    worstlog=max(worstlog,(np.log(H(a,c,ss))/ss).max())
print('box sup on [1/16,1]',worst,' box max of logH/s on (0,1/16]',worstlog)
