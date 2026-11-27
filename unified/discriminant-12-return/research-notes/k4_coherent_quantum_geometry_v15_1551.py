import numpy as np
from scipy.special import gammaln
worst=0.; fisher=0.; overlap=0.; cases=0
for n in range(1,65):
 k=np.arange(n+1); logb=gammaln(n+1)-gammaln(k+1)-gammaln(n-k+1)
 def state(t,p):
  return np.exp((logb+k*np.log(t)+(n-k)*np.log1p(-t))/2+1j*k*p)
 for t in (.01,.1,.25,.5,.75,.9,.99):
  for p in (0.,.7,2.1):
   c=state(t,p); a=(k-n*t)/(2*t*(1-t)); d=np.stack([a*c,1j*k*c],axis=1)
   Q=d.conj().T@d-np.outer(d.conj().T@c,c.conj()@d)
   ref=n*np.array([[1/(4*t*(1-t)),.5j],[-.5j,t*(1-t)]])
   worst=max(worst,np.max(np.abs(Q-ref))/n)
   F=np.sum(abs(c)**2*(2*a)**2)
   fisher=max(fisher,abs(F-4*ref[0,0].real)/n)
   t2=.37;p2=p+.23
   exact=abs(np.sqrt((1-t)*(1-t2))+np.sqrt(t*t2)*np.exp(1j*(p2-p)))**(2*n)
   overlap=max(overlap,abs(abs(np.vdot(c,state(t2,p2)))**2-exact));cases+=1
assert worst<1e-9 and fisher<1e-9 and overlap<1e-11
print('cases',cases,'normalized QGT error',worst,'normalized Fisher error',fisher,'fidelity error',overlap)
