import sympy as s
import numpy as np
from scipy.integrate import solve_ivp
x,v,l,w,h,M,k,l0,g=s.symbols('x v l w h M k l0 g',real=True)
V=k*(l-l0)**2/2+g*x**4/4-h*x-l*x*x/2
E=v*v/2+M*w*w/2+V
f=[v,-s.diff(V,x),w,-s.diff(V,l)/M]
assert s.simplify(sum(s.diff(E,q)*p for q,p in zip([x,v,l,w],f)))==0
I=v*v-2*h*x-l*x*x
assert s.simplify(sum(s.diff(I,q)*p for q,p in zip([x,v,l,w],f))+w*x*x+2*g*x**3*v)==0
print('effective potential:',s.expand(V.subs(l,l0+x*x/(2*k))))
# autonomous bounded model; choose dimensionless parameters, not fitted
for h0 in [.25,.5,1.,2/3]:
 def rhs(t,z):
  x,v,l,w=z;return [v,h0+l*x-x**3,w,-(l+.5)+x*x/2]
 def energy(z):
  x,v,l,w=z;return (v*v+w*w)/2+(l+.5)**2/2+x**4/4-h0*x-l*x*x/2
 sol=solve_ivp(rhs,(0,20),[0,0,-.5,0],rtol=1e-11,atol=1e-13,dense_output=True,max_step=.03)
 z=sol.sol(np.linspace(0,20,4001)); err=np.max(abs(energy(z)-energy(z[:,0])))
 assert err<1e-8
 print(h0,'lambda range',z[2].min(),z[2].max(),'energy error',err,'crossings',np.count_nonzero(z[2,1:]*z[2,:-1]<0))
