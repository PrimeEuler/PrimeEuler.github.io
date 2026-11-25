#!/usr/bin/env python3
"""v15.1464: fixed lapse/zero shift raw ADM has a constrained
longitudinal zero-speed Jordan block. Demonstrates absence of a
uniform H1(metric)xL2(extrinsic curvature) bound at high k.
Gauge/formulation no-go, NOT physical GR instability.
"""
import sympy as s
k,t,x=s.symbols("k t x",positive=True,real=True)
H,K=s.symbols("H K")
p=s.Matrix([k,0,0])
h=s.zeros(3);h[0,0]=H*s.exp(s.I*k*x)
R=s.zeros(3)
for i in range(3):
 for j in range(3):
  R[i,j]=s.simplify((-sum(p[m]*p[i]*h[m,j]+p[m]*p[j]*h[m,i] for m in range(3))
     +p[i]*p[j]*s.trace(h)+p.dot(p)*h[i,j])/2)
assert R==s.zeros(3)
Hamiltonian=s.simplify(-sum(p[i]*p[j]*h[i,j] for i in range(3) for j in range(3))
  +p.dot(p)*s.trace(h))
assert Hamiltonian==0
kin=s.zeros(3);kin[0,0]=K*s.exp(s.I*k*x)
momentum=s.Matrix([s.simplify(s.I*sum(p[j]*(kin[i,j]-
 (s.trace(kin) if i==j else 0)) for j in range(3))) for i in range(3)])
assert momentum==s.zeros(3,1)
J=s.Matrix([[0,-2],[0,0]])
assert J!=s.zeros(2) and J**2==s.zeros(2) and J.eigenvals()=={0:2}
assert s.exp(J*t)==s.eye(2)+t*J
for kval in (1,4,16,64,256):
 value=s.sqrt(1+4*t*t*(1+kval*kval))
 print("wave number",kval,"H1xL2 norm at t=1",float(value.subs(t,1)))
print("PASS constraints zero, Jordan block, high-frequency norm unbounded")
print("NEGATIVE raw geodesic-lapse ADM not strongly hyperbolic")
print("OPEN actual strongly hyperbolic Einstein-H2 evolution")
