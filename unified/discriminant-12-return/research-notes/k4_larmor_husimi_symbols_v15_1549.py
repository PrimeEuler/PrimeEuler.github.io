import numpy as np
from scipy.special import roots_jacobi
from scipy.special import comb
from math import factorial
# t=(1+n_z)/2, beta(k+1,n-k+1); Gauss-Jacobi integrates exactly
worst=0.; fourth=0.; normalized=0.
for n in range(1,65):
 j=n/2; m=np.arange(n+1)-j; C=j*(j+1)
 P=np.diag(np.sqrt((n-np.arange(n))*(np.arange(n)+1)),-1); X=(P+P.T)/2
 q2=np.diag(X@X); q4=np.diag(np.linalg.matrix_power(X,4))
 moments=[]
 for k in range(n+1):
  z,w=roots_jacobi(8,n-k,k); w=w/w.sum()
  moments.append([np.dot(w,z**r) for r in range(5)])
 moments=np.array(moments)
 b=(j+1)*(2*j+3)/2
 hx2=(1-moments[:,2])/2
 err=np.max(abs(b*hx2-(j+1)/2-q2)); worst=max(worst,err)
 normalized=max(normalized,abs(np.mean(hx2)-1/3))
 assert np.allclose(b*hx2-(j+1)/2,q2,atol=1e-10)
 degrees=list(range(0,min(n,4)+1,2)); coeff=np.linalg.lstsq(moments[:,degrees],m**4,rcond=None)[0]
 hx4=3*(1-2*moments[:,2]+moments[:,4])/8
 xmom={0:np.ones(n+1),2:hx2,4:hx4}
 estimate=sum(c*xmom[d] for c,d in zip(coeff,degrees)); fourth=max(fourth,np.max(abs(estimate-q4)))
 assert np.allclose(estimate,q4,atol=1e-8,rtol=1e-10)
 if n in (1,2,4,8,16,32,64):
  print(n, 'pole <nx²>',hx2[-1], 'quantum <Jx²>',q2[-1], 'quadratic symbol error',err,'fourth symbol coeff',coeff)
print('worst absolute second/fourth errors',worst,fourth,'uniform sphere error',normalized)
print('PASS 64 shells')
