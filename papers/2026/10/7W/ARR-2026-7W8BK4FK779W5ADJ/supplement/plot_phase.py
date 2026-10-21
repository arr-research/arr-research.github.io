from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parent/'figure'
root.mkdir(parents=True,exist_ok=False)
a=np.linspace(0.001,4,1200)
boundary=(1+a**(2/3))**1.5
prior=2*(a+1)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42})
fig,ax=plt.subplots(figsize=(7.4,4.0),layout='constrained')
ax.fill_between(a,0,boundary,color='#dceee7')
ax.fill_between(a,boundary,12,color='#f7e5d6')
ax.plot(a,boundary,color='#994219',lw=2,label=r'Exact threshold $(1+a^{2/3})^{3/2}$')
ax.plot(a,prior,color='#555555',lw=1.5,ls='--',label=r'Earlier obstruction $2(a+1)$')
ax.text(2.65,1.5,'Strict polynomial\ncertificates',ha='center',va='center',color='#154d3a')
ax.text(2.6,8.6,'No polynomial or local\nanalytic certificate',ha='center',va='center',color='#713210')
ax.set(xlim=(0,4),ylim=(0,12),xlabel=r'Damping $a>0$',ylabel=r'Forcing amplitude $|b|$')
ax.set_xticks(np.arange(0,4.1,1));ax.set_yticks(np.arange(0,12.1,2))
ax.grid(alpha=.2,lw=.5)
ax.legend(loc='upper left',frameon=True,facecolor='white',framealpha=.94,fontsize=9)
fig.savefig(root/'phase-boundary.pdf')
fig.savefig(root/'phase-boundary.png',dpi=180)
print(root)
