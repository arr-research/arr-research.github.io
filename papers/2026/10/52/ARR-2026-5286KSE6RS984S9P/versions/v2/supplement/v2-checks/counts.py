fails=0
for l in range(1,25):
  for c in range(0,25):
    for s in range(0,6*l+c+1):
      q=min(l,s//2); r=s-2*q
      if not(0<=q<=l and 0<=r<=4*l+c and 2*q+r==s): fails+=1
print('counting fails',fails)
