import numpy as np
from scipy.linalg import expm
from scipy.integrate import solve_ivp
import sympy as s
l,h,x,p=s.symbols('l h x p',real=True)
A=s.Matrix([[0,1],[l,0]])
B=s.Matrix([[0,1,0],[l,0,h],[0,0,0]])
assert A*A==l*s.eye(2)
assert B.subs(l,0)**3==s.zeros(3)
assert B.subs(l,0)**2!=s.zeros(3)
J=np.array([[0.,1.],[-1.,0.]])
worst=np.zeros(4); count=0
for lam in (-1.,-.25,-.000001,0.,.000001,.25,1.):
 for H in (.25,.5,2/3,1.):
  b=np.array([[0,1,0],[lam,0,H],[0,0,0.]])
  for t in (.1,1.,2.):
   e=expm(t*b); S=e[:2,:2]; x,p=e[:2,2]
   y=solve_ivp(lambda t,y:[y[1],H+lam*y[0]],(0,t),[0,0],rtol=1e-12,atol=1e-14).y[:,-1]
   cov=S@S.T/2
   errs=[abs(p*p-2*H*x-lam*x*x),np.max(abs(S@J@S.T-J)),abs(np.linalg.det(cov)-.25),np.max(abs(y-[x,p]))]
   worst=np.maximum(worst,errs);count+=1
assert max(worst)<1e-10
print(count,worst)
# oscillator coherent-state manifold not invariant under shear: vacuum becomes squeezed
for t in (0.,.5,1.,2.):
 S=np.array([[1.,t],[0.,1.]])
 cov=S@S.T/2
 occupation=(np.trace(cov)-1)/2
 assert abs(occupation-t*t/4)<1e-14
 print('shear',t,'cov',cov.tolist(),'centered occupation',occupation)
