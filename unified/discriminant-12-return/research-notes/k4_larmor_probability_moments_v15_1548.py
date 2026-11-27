import numpy as np
import sympy as s
from scipy.special import comb
j,m=s.symbols('j m', real=True)
C=j*(j+1); R=C-m*m
# exact conditional fourth-moment defect via angular momentum algebra
# <Jx^4> = (3 R^2 - 2 R + 3 m^2)/8
for n in range(1,65):
 j=n/2; m=np.arange(n+1)-j; C=j*(j+1); r=C-m*m
 P=np.diag(np.sqrt((n-np.arange(n))*(np.arange(n)+1)),-1); X=(P+P.T)/2
 x,U=np.linalg.eigh(X); prob=abs(U)**2
 q2=prob@(x*x); q4=prob@(x**4)
 assert np.allclose(q2,r/2)
 assert np.allclose(q4,(3*r*r-2*r+3*m*m)/8)
 cl4=3*r*r/8
 assert np.allclose(np.mean(r),2*C/3)
 assert np.allclose(np.mean(cl4-q4),C/24)
 assert np.allclose(prob.mean(axis=0),1/(n+1))
 # CDF mixture versus uniform continuous limiting law, normalize by sqrt(C)
 grid=np.linspace(-1,1,2001); radii=np.sqrt(r/C)
 cdf=np.mean(.5+np.arcsin(np.clip(grid[:,None]/radii,-1,1))/np.pi,axis=1)
 if n in (1,2,4,8,16,32,64): print(n,j,np.mean(r)/C,np.mean(cl4-q4)/C**2,np.max(abs(cdf-(grid+1)/2)))
print('PASS 64 shells')
