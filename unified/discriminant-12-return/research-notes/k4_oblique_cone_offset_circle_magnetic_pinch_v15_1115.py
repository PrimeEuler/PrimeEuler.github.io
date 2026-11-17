#!/usr/bin/env python3
"""Gravity v15.1115: an oblique cone view sends a genuine tilted section
ellipse to an offset circle, while a fixed-T circle stays a circle.
Second test: static force-balanced infinite cylindrical magnetic pinch.
The map is VIEW-DEPENDENT; no cone physical dynamics follows.
"""
import sympy as s
X,Y,T,C,e,R=s.symbols("X Y T C e R",real=True,positive=True)
t=s.sqrt(1-e**2)
q=(1-t)/e
d=-C*e/(1-e**2)
A=C/(1-e**2)
B=C/t
# The actual cone section T+eX=C is an XY ellipse. A viewing
# projection (U,V)=(X+qT,Y) is circular on the tilted section.
U=s.simplify(X+q*(C-e*X))
U0=s.simplify(t*d+q*C)
ellipse=s.expand((C-e*X)**2-X**2-Y**2)
circle=s.expand((U-U0)**2+Y**2-B**2)
assert s.simplify(circle+ellipse)==0
assert s.simplify(U0-C*(1-1/t)/e)==0
# Meanwhile each fixed-height section T=R becomes a circle
# (U-qR)^2+V^2=R^2. Check a real inner-circle inclusion.
sample={C:1,e:s.Rational(2,5),R:3}
assert float((B+s.Abs(U0-q*R)-R).subs(sample).evalf())<0
# An off-center circle in the *orthographic* XY view, by contrast,
# is generally NOT a plane-section ellipse: lifting it gives
# T²-2dX+d²=constant, which is quadratic in T, not a plane equation.
r,L,b,P=s.symbols("r L b P",positive=True)
Bphi=b*r*(1-(r/L)**2)**2
Jx=s.simplify(s.diff(r*Bphi,r)/r)  # mu0=1
Fr=s.simplify(-s.diff(Bphi**2,r)/2-Bphi**2/r)
assert s.simplify(Fr+Jx*Bphi)==0
# Equilibrium 0=-dp/dr+Fr, with external p(L)=P.
pressure=P+b**2*L**2/10*(1-r**2/L**2)**5-Bphi**2/2
assert s.simplify(s.diff(pressure,r)-Fr)==0
assert s.simplify(pressure.subs(r,L)-P)==0
assert s.simplify(pressure.subs(r,0)-P-b**2*L**2/10)==0
assert s.simplify(pressure.subs(r,L/s.sqrt(3))-P+8*b**2*L**2/405)==0
print("PASS cone oblique apparent offset circle, and infinite cylindrical radial equilibrium")
print("sample n=5: outer R=3, inner r=",float(B.subs(sample)),
      "centers separation=",float(abs((U0-q*R).subs(sample))))
print("pressure boundary positivity sufficient/necessary: P >= 8*b^2*L^2/405")
