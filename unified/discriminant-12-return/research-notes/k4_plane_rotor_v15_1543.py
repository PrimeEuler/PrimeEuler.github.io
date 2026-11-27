import numpy as np
from scipy.integrate import solve_ivp
import sympy as s
h,u,t=s.symbols('h u t', real=True)
c,si=s.cos(t),s.sin(t)
u0=h*(si-c)/(si+c)
f=(h*c+u*si)**2-(-h*si+u*c)**2
assert s.trigsimp(f.subs(u,u0))==0
assert s.trigsimp(s.diff(f,u).subs(u,u0)-2*h)==0
assert s.trigsimp(s.diff(f,u,2)+2*s.cos(2*t))==0
# dimensionless rotor witness, optional quartic stabilization
for w0 in [0.,.1,.5,1.]:
 for H in [.25,.5,2/3,1.]:
  def rhs(t,z):
   x,v,a,w=z;return [v,H-np.cos(2*a)*x-x**3,w,x*x*np.sin(2*a)]
  def energy(z):
   x,v,a,w=z;return (v*v+w*w)/2-H*x+np.cos(2*a)*x*x/2+x**4/4
  def crossing(t,z):return -np.cos(2*z[2])
  sol=solve_ivp(rhs,(0,20),[0,0,0,w0],rtol=1e-11,atol=1e-13,max_step=.03,events=crossing,dense_output=True)
  z=sol.sol(np.linspace(0,20,4001));err=max(abs(energy(z)-energy(z[:,0])));assert err<1e-8
  print(w0,H,len(sol.t_events[0]),round(float(np.max(-np.cos(2*z[2]))),8),f'{err:.3g}')
