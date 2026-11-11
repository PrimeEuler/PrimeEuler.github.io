#!/usr/bin/env python3
"""v15.702: invariant Kaluza-Klein fiber minimal wave operator is k-diagonal.

A 2D base/fiber sub-block of conventional KK metric:
  ds^2 = dx^2 + R^2 (dpsi + A(x) dx)^2.
This is NOT a full Taub-NUT Dirac computation. It verifies the local
natural-operator charge selection independent of speculative Cone labels.
"""
import sympy as s
x,ps=s.symbols("x psi",real=True)
R=s.symbols("R",positive=True,real=True)
k=s.symbols("k",integer=True)
A=s.Function("A")(x);f=s.Function("f")(x)
metric=s.Matrix([[1+R**2*A**2,R**2*A],[R**2*A,R**2]])
assert s.simplify(metric.det()-R**2)==0
inv=s.simplify(metric.inv())
assert (inv-s.Matrix([[1,-A],[-A,A**2+R**(-2)]])).applyfunc(s.simplify)==s.zeros(2)
phi=f*s.exp(s.I*k*ps)
coords=[x,ps]
lap=sum(s.diff(sum(inv[i,j]*s.diff(phi,coords[j]) for j in range(2)),coords[i]) for i in range(2))
result=s.simplify(s.expand(lap/s.exp(s.I*k*ps)))
expected=(s.diff(f,x,2)-2*s.I*k*A*s.diff(f,x)
          -s.I*k*s.diff(A,x)*f-k*k*A**2*f-k*k*f/R**2)
assert s.simplify(result-expected)==0

# All coefficients are independent of psi, so [P,Delta]=0 and every
# Fourier sector sees only its own U(1) minimal coupling with charge k.
for kk in range(-6,7):
    for mm in range(-6,7):
        overlap=s.integrate(s.exp(s.I*(kk-mm)*ps),(ps,0,2*s.pi))
        assert s.simplify(overlap-(2*s.pi if kk==mm else 0))==0
print("PASS: KK inverse, Fourier-diagonal Laplacian and charge-k minimal coupling")
