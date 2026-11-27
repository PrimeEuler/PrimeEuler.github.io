import numpy as np
from scipy.linalg import expm
from scipy.special import gammaln
from scipy.special import roots_legendre
worst=0.; closure=0.; moment=0.
for n in range(1,65):
 k=np.arange(n+1); j=n/2
 A=np.sqrt((k[:-1]+1)*(n-k[:-1])); P=np.diag(A,-1); Y=(P-P.T)/(2j) # imaginary literal
 logbin=gammaln(n+1)-gammaln(k+1)-gammaln(n-k+1)
 for theta in (.2,1.1,2.4):
  t=np.sin(theta/2)**2
  c=np.exp((logbin+k*np.log(t)+(n-k)*np.log1p(-t))/2)
  # Rotation from lowest state: exp(+i theta Jy)
  u=expm(1j*theta*Y)[:,0]
  worst=max(worst,np.max(abs(u-c)))
  moment=max(moment,abs(np.dot(c*c,k-j)-j*(2*t-1)))
 x,w=roots_legendre(n+1); t=(x+1)/2
 diag=(n+1)*np.exp(logbin[None,:]+np.log(t[:,None])*k+np.log1p(-t[:,None])*(n-k)).T@(w/2)
 closure=max(closure,np.max(abs(diag-1)))
assert worst<1e-11 and closure<1e-11 and moment<1e-10
print('PASS 64 shells, 192 rotations; max amplitude error',worst,'resolution error',closure,'moment error',moment)
