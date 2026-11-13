#!/usr/bin/env python3
"""v15.937: exact H n=3 position quadrupole vs glued spin1xspin1
Runge-Lenz quadrupole. Units of physical Q: a0^2."""
import sympy as s
from sympy.physics.wigner import wigner_3j,clebsch_gordan
r=s.symbols('r',positive=True)
def R(l):
 n=3;rho=s.Rational(2,3)*r
 c=s.sqrt((s.Rational(2,3))**3*s.factorial(2-l)/(6*s.factorial(3+l)))
 return c*s.exp(-rho/2)*rho**l*s.assoc_laguerre(2-l,2*l+1,rho)
rad={}
for l,k in [(0,2),(1,1),(2,2)]:
 rad[l,k]=s.simplify(s.integrate(
 s.expand(R(l)*R(k)*s.exp(s.Rational(2,3)*r))*s.exp(-s.Rational(2,3)*r)*r**4,
 (r,0,s.oo)))
assert rad=={(0,2):45*s.sqrt(10),(1,1):180,(2,2):126}
states=[(l,m) for l in (0,1,2) for m in range(-l,l+1)]
phys=s.zeros(9)
for a,(l,m) in enumerate(states):
 for b,(k,mp) in enumerate(states):
  if m!=mp or (min(l,k),max(l,k)) not in rad:continue
  angle=2*s.Integer(-1)**m*s.sqrt((2*l+1)*(2*k+1))*wigner_3j(l,2,k,0,0,0)*wigner_3j(l,2,k,-m,0,m)
  phys[a,b]=s.simplify(angle*rad[min(l,k),max(l,k)])
p=s.Matrix([[0,s.sqrt(2),0],[0,0,s.sqrt(2)],[0,0,0]])
z=s.diag(1,0,-1);u=s.eye(3)
Ap=s.kronecker_product(p,u)-s.kronecker_product(u,p)
Az=s.kronecker_product(z,u)-s.kronecker_product(u,z)
aux=3*Az**2-(Az**2+(Ap*Ap.T+Ap.T*Ap)/2)
cg=s.zeros(9)
for b,(l,m) in enumerate(states):
 for a in range(3):
  for c in range(3):cg[3*a+c,b]=clebsch_gordan(1,1,l,1-a,1-c,m)
assert cg.T*cg==s.eye(9)
aux=s.simplify(cg.T*aux*cg)
P={l:s.diag(*[int(ll==l) for ll,_ in states]) for l in (0,1,2)}
ratios={(0,2):s.Rational(45,2),(1,1):s.Integer(24),(2,2):s.Integer(36)}
for l in (0,1,2):
 for k in (0,1,2):
  x=P[l]*phys*P[k];y=P[l]*aux*P[k]
  if (min(l,k),max(l,k)) in ratios:
   assert s.simplify(x-ratios[min(l,k),max(l,k)]*y)==s.zeros(9)
  else:assert x==y==s.zeros(9)
  print(l,k,'physical HS²',s.trace(x.T*x),'aux HS²',s.trace(y.T*y))
assert phys[states.index((2,0)),states.index((0,0))]==90*s.sqrt(2)
assert aux[states.index((2,0)),states.index((0,0))]==4*s.sqrt(2)
print('PASS exact 9x9; three independently different reduced radial factors')
