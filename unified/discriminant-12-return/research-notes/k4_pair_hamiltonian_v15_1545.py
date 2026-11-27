import sympy as s
import numpy as np
from scipy.integrate import solve_ivp
q,p,r,t=s.symbols('q p r t',real=True)
a=(q*q+p*p)/2;b=(r*r+t*t)/2;N=a+b
Jx=(q*r+p*t)/2;Jy=(q*t-p*r)/2;Jz=(a-b)/2
Q=4*Jy**2
pb=lambda f,g:s.expand(s.diff(f,q)*s.diff(g,p)-s.diff(f,p)*s.diff(g,q)+s.diff(f,r)*s.diff(g,t)-s.diff(f,t)*s.diff(g,r))
assert s.expand(Jx**2+Jy**2+Jz**2-N**2/4)==0
for f,g,h in [(Jx,Jy,Jz),(Jy,Jz,Jx),(Jz,Jx,Jy)]: assert s.expand(pb(f,g)-h)==0
for f in (Jx,Jy,Jz):assert pb(N,f)==0
assert s.expand(pb(Q,Jz)-8*Jy*Jx)==0
assert pb(Q,Jy)==0
for h in [.25,.5,2/3,1.]:
 z0=[np.sqrt(h),0,np.sqrt(h),0]
 def rhs(time,z):q,p,r,t=z;return [p/2,-q/2,-t/2,r/2]
 ts=np.linspace(0,2*np.pi,1001);z=solve_ivp(rhs,(0,ts[-1]),z0,t_eval=ts,rtol=1e-12,atol=1e-14).y
 n=np.sum(z*z,axis=0)/2;Qn=(z[0]*z[3]-z[1]*z[2])**2
 err=np.max(abs(Qn-h*h*np.sin(ts)**2)); drift=np.max(abs(n-h))
 assert err<1e-10 and drift<1e-10
 print(h,'Q error',err,'N drift',drift,'max Q',max(Qn),'cycle mean',np.trapz(Qn,ts)/(2*np.pi))
print('PASS')
