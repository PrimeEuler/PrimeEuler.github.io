#!/usr/bin/env python3
"""Gravity v15.1389: on-shell phase-matched Weyl-H2 -> transverse Maxwell.
Two distinct null sigma waves, conjugated TT gravitational wave, output
null photon current. Retarded resonance analytically / via ODE / quadrature.
Fixed-background leading EFT; no backreaction, quantum photon or free coupling.
"""
import numpy as np
from math import sqrt
from scipy.integrate import solve_ivp,quad
eta=np.diag([-1.,1.,1.,1.])
a=np.array([1.,0.,0.]);b=np.array([0.,1.,0.])
c=np.array([.5,.5,1/sqrt(2.)])
e1=np.array([1.,-1.,0.])/sqrt(2.);e2=np.cross(c,e1)
assert abs(c@e1)<1e-14 and abs(c@e2)<1e-14 and abs(e1@e2)<1e-14
h=np.zeros((4,4));h[1:,1:]=np.outer(e1,e1)-np.outer(e2,e2)
p=np.r_[-1.,a];q=np.r_[-1.,b];k=np.r_[-1.,c];S=p+q-k
for v in (p,q,k,S):assert abs(v@eta@v)<1e-14
B=-(np.outer(p,q)-np.outer(q,p))
R=np.empty((4,4,4,4))
for i in range(4):
 for j in range(4):
  for r in range(4):
   for s in range(4):
    R[i,j,r,s]=(-k[r]*k[j]*h[i,s]-k[s]*k[i]*h[j,r]+k[s]*k[j]*h[i,r]+k[r]*k[i]*h[j,s])/2
Ricci=np.einsum('rs,risj->ij',eta,R)
assert abs(Ricci).max()<1e-14
K=np.einsum('ijrs,rs->ij',R,eta@B@eta)
J=1j*(S@(eta@K@eta))
assert abs(S@J)<1e-14
trans=J[1:]-(J[1:]@S[1:])/(S[1:]@S[1:])*S[1:]
assert np.linalg.norm(trans-1j*np.array([.5,-.5,0]))<1e-13
frequency=-S[0];k2=S[1:]@S[1:];kabs=sqrt(k2)
assert abs(frequency-kabs)<1e-14
g_eff=.02;J0=g_eff*trans
def analytic(t):
 return (J0/(2j*kabs))*(t*np.exp(-1j*kabs*t)-np.sin(kabs*t)/kabs)
def green(t):
 out=[]
 for coeff in J0:
  def f(s):return -coeff*np.exp(-1j*kabs*s)*np.sin(kabs*(t-s))/kabs
  re=quad(lambda x:float(np.real(f(x))),0,t,epsabs=1e-13)[0]
  im=quad(lambda x:float(np.imag(f(x))),0,t,epsabs=1e-13)[0]
  out.append(re+1j*im)
 return np.array(out)
def numeric(t):
 def rhs(time,y):return np.r_[y[3:],-k2*y[:3]-J0*np.exp(-1j*frequency*time)]
 sol=solve_ivp(rhs,(0,t),np.zeros(6,complex),rtol=1e-12,atol=1e-14,method='DOP853')
 assert sol.success
 return sol.y[:3,-1]
if __name__=='__main__':
 print('INPUT_NULL',p,q,k)
 print('OUTPUT_NULL',S,'squared',S@eta@S)
 print('TT_RICCI_MAX',abs(Ricci).max(),'CURRENT_WARD',abs(S@J))
 print('TRANSVERSE_CURRENT',trans,'norm',np.linalg.norm(trans))
 for t in (.4,1.,2.,4.):
  A=analytic(t);G=green(t);O=numeric(t)
  err=max(np.max(abs(A-G)),np.max(abs(A-O)))
  assert err<1e-12
  print(dict(t=t,mode_amplitude=float(np.linalg.norm(A)),max_green_ode_error=float(err)))
 assert np.linalg.norm(analytic(4.))>np.linalg.norm(analytic(2.))
 print('PASS on-shell transverse photon channel with resonant retarded growth')
 print('NEGATIVE plane waves infinite extent; unbounded growth requires physical backreaction')
 print('OPEN finite wave packets, total coupled energy conservation, quarter coupling selector')
