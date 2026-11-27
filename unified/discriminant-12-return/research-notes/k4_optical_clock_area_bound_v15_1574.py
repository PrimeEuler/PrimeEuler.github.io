import numpy as np
from scipy.integrate import quad
# Semicircle in H2 centered at distance R from the initial origin.
# Lorentz boost maps the initial point to origin, preserves length and area.
for R in (.1,.3,.7,1.,1.5,2.):
 c,s=np.cosh(R),np.sinh(R)
 def integrand(t):
  T=c*c-s*s*np.cos(t); X=c*s*(np.cos(t)-1); Y=s*np.sin(t)
  xp=-c*s*np.sin(t); yp=s*np.cos(t)
  return (X*yp-Y*xp)/(2*(T+1))
 psi=quad(integrand,0,np.pi,epsabs=1e-12)[0]
 L=np.pi*s
 bound=(np.hypot(np.pi,L)-np.pi)/2
 assert abs(abs(psi)-bound)<1e-11
 print(R,L,psi,bound)
# Clock bound on prescribed scalar speed histories: Xi'=v speed²/4.
for e in (.1,.3,.5):
 for A in (.25,1.,2.):
  for p in (1,2,3):
   b=1-e
   def xi(v):
    x=v-e
    return A*A*p*p/(4*b**(2*p))*(x**(2*p)/(2*p)+e*x**(2*p-1)/(2*p-1))
   D=quad(lambda v:np.expm1(xi(v)),e,1)[0]
   W=np.sqrt(b)*np.log1p(D/b)+2*np.sqrt(D)*np.arctan(np.sqrt(b/D))
   Lmax=2*np.sqrt(2*np.sqrt(b)*W/e)
   assert A<=Lmax
   assert A<=2*np.sqrt(xi(1)*np.log(1/e))
print('PASS 6 semicircles and 27 clock histories')
