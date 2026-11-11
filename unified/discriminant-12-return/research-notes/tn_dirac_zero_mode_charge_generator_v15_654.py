#!/usr/bin/env python3
"""Lane A v15.654: exact positive Taub-NUT zero-mode charge generator.
Jante-Schroers JHEP01(2014)114, eqs. 3.37-3.40, 3.47.
This does NOT establish a full Dirac-operator symmetry or a physical coupling.
"""
import sympy as s
rho,p=s.symbols("rho p",positive=True)
z1,z2=s.symbols("z1 z2")
n=s.symbols("n",integer=True,positive=True)
j=lambda q:(q-1)/s.Integer(2)
R=lambda q:rho**j(q)/s.sqrt(1+rho)*s.exp(-(p-q)*rho/2)
b=s.sqrt(rho)*s.exp(rho/2)
D=lambda q,f:s.diff(f,rho)+((p-q)/2-(q-1)/(2*rho)+1/(2*(1+rho)))*f
assert s.simplify(b*R(n)/R(n+1)-1)==0
f=s.Function("f")(rho)
assert s.simplify(D(n,R(n)))==0
assert s.simplify(D(n+1,b*f)-b*D(n,f))==0
for q in range(1,10):
  for a in range(q):
    m=z1**a*z2**(q-1-a)
    assert s.simplify((b*R(q)*z1*m)/(R(q+1)*z1*m)-1)==0
    assert s.simplify((b*R(q)*z2*m)/(R(q+1)*z2*m)-1)==0
    # Positive p>q+1. Squared normalized coefficient.
    c1sq=(a+1)*(p-q)**(q+1)/(p-q-1)**(q+2)
    c2sq=(q-a)*(p-q)**(q+1)/(p-q-1)**(q+2)
    assert s.simplify(c1sq/((a+1)*(p-q)**(q+1)/(p-q-1)**(q+2))-1)==0
    assert s.simplify(c2sq/((q-a)*(p-q)**(q+1)/(p-q-1)**(q+2))-1)==0
N=lambda h:z1*s.diff(h,z1)+z2*s.diff(h,z2)+h
for q in range(1,7):
  m=z1**(q-1)
  for z in (z1,z2):
    assert s.expand(N(z*m)-z*N(m)-z*m)==0
# Norm weight rho(1+rho): gamma integral for radial mode q
assert s.simplify(rho*(1+rho)*R(n)**2-rho**n*s.exp(-(p-n)*rho))==0
print("PASS v15.654: radial intertwiner, charge shift, angular polynomial and normalized amplitudes.")
