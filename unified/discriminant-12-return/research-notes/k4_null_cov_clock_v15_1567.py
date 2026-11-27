import sympy as S
import numpy as np
from scipy.integrate import quad
s=S.symbols('s', real=True)
M=S.Matrix([[1+s*s,s],[s,1]])
assert M.det()==1
assert S.simplify(S.trace((M.inv()*M.diff(s))**2)/2)==1
for e in (.01,.1,.3):
 for A in (.25,.5,1.,2.):
  for p in (1,2,3):
   def speed(v):return A*p*(v-e)**(p-1)/(1-e)**p
   def xi(v):return quad(lambda u:u*speed(u)**2/4,e,v)[0]
   def exact(v):
    x=v-e
    return A*A*p*p/(4*(1-e)**(2*p))*(x**(2*p)/(2*p)+e*x**(2*p-1)/(2*p-1))
   assert abs(xi(1)-exact(1))<1e-12
   clock=quad(lambda v:np.exp(xi(v)),e,1)[0]/(1-e)
   assert abs(clock-quad(lambda v:np.exp(exact(v)),e,1)[0]/(1-e))<1e-12
   if e==.1 and A==1:print(p,xi(1),clock)
print('PASS 36 histories; exact shear metric')
