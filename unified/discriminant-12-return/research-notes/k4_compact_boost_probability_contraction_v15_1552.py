import numpy as np
from scipy.stats import binom, nbinom, poisson
from scipy.special import gammaln
# Same mean occupation mu; compact binomial and noncompact negative binomial.
for n in (4,8,16,32,64,128,256,1024):
 for mu in (0.5,2.,3.):
  k=np.arange(0, max(n+1,200))
  a=binom.pmf(k,n,mu/n); b=nbinom.pmf(k,n,n/(n+mu)); p=poisson.pmf(k,mu)
  assert abs(a.sum()-1)<1e-12 and abs(b.sum()-1)<1e-12
  assert abs(k@a-mu)<1e-10 and abs(k@b-mu)<1e-10
  assert abs((k-mu)**2@a-mu*(1-mu/n))<1e-10
  assert abs((k-mu)**2@b-mu*(1+mu/n))<1e-10
  if mu==2: print(n, 'TV compact',.5*abs(a-p).sum(),'TV boost',.5*abs(b-p).sum())
# QGT from amplitude derivatives in occupation/phase coordinates
worst=0
for n in (4,8,16,32,64):
 for mu in (.5,1.,2.):
  for sign in (-1,1):
   k=np.arange(n+1 if sign==-1 else 512)
   p=binom.pmf(k,n,mu/n) if sign==-1 else nbinom.pmf(k,n,n/(n+mu))
   v=mu*(1+sign*mu/n)
   c=np.sqrt(p)*np.exp(1j*k*.7)
   d=np.stack([(k-mu)*c/(2*v),1j*k*c],axis=1)
   Q=d.conj().T@d-np.outer(d.conj().T@c,c.conj()@d)
   ref=np.array([[1/(4*v),.5j],[-.5j,v]])
   worst=max(worst,np.max(abs(Q-ref)))
assert worst<1e-10
print('PASS QGT cases 30; worst',worst)
