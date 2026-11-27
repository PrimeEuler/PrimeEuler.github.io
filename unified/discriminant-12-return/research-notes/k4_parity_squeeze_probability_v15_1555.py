import numpy as np
from scipy.special import gammaln
from scipy.linalg import expm
# On the interior of a truncated oscillator basis, test exact algebra.
N=100
a=np.diag(np.sqrt(np.arange(1,N)),1); ap=a.T
P=ap@ap/2; M=a@a/2; Z=np.diag(np.arange(N)/2+.25)
cut=np.s_[:N-4,:N-4]
assert np.max(abs((M@P-P@M-2*Z)[cut]))<1e-11
assert np.max(abs((Z@Z-(P@M+M@P)/2+3*np.eye(N)/16)[cut]))<1e-11
worst=0.; means=0.; norm=0.
for r in (.1,.3,.5,.7):
 for phi in (0.,.7,1.5):
  U=expm(r*(np.exp(1j*phi)*P-np.exp(-1j*phi)*M))
  for parity in (0,1):
   b=.25+parity/2; k=np.arange(N//2); t=np.tanh(r)**2
   prob=np.exp(gammaln(2*b+k)-gammaln(2*b)-gammaln(k+1)+2*b*np.log1p(-t)+k*np.log(t))
   num=abs(U[parity::2,parity])**2
   worst=max(worst,np.max(abs(prob-num)))
   norm=max(norm,abs(prob.sum()-1))
   means=max(means,abs((2*k+parity)@prob-(parity+(2*parity+1)*np.sinh(r)**2)))
assert worst<1e-10 and means<1e-10 and norm<1e-10
print('24 cases; max probability error',worst,'normalization defect',norm,'mean error',means)
for parity in (0,1):
 b=.25+parity/2
 print('Bargmann',b,'Gaussian curvature',-2/b,'Casimir',b*(b-1))
