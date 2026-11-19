#!/usr/bin/env python3
"""Gravity v15.1198 — additive correction of v15.1197 trace-basis error.

Correct conversion of v15.787 E=A_raw I + R nn into
E=A_iso I + R Q, Q=nn-I/3, A_iso=A_raw+R/3.
Uses the eternal traveling Maxwell harmonic particular solution of
v15.1194/1195, not the compact Maxwell packet v15.1085.
The finite arm average is a simultaneous-time spatial proxy only.
"""
import sympy as s
I=s.I
k,eta=s.symbols("k eta",positive=True,real=True)
w=s.sqrt(3)*k
nu2=(8*eta-3)*(1+k*k)/3
D=(-1-I*w)**2+nu2
x=-2-I*w
p=-3*s.sqrt(3)/(k*k*D)
phi=((x*x+x)*p/3+s.sqrt(3)-3*I*k*(-1-I*w)/(2*k*k))/(1+k*k)
psi=((k*k-x)*p/3+s.sqrt(3)/2+3*I*k/(2*k*k))/(1+k*k)
R=-3*k*k*phi
W=3*k*k*(phi+psi)/2
Araw=(x*x+x)*psi+x*phi
Aiso=Araw+R/3
assert s.simplify(Aiso+s.sqrt(3))==0, "universal isotropic contact"
assert s.simplify(R-W+3*k*k*(3*phi+psi)/2)==0
# Complete spatial curvature: Ez=Araw+R, Ex=Araw.
# Its two-arm proxy must equal the A_iso/Q-basis expression exactly.
kr=s.symbols("kr",real=True)
F=(s.exp(I*kr)-1)/(I*kr)
geom=(2*F+1)*R/3+(F-1)*Aiso
direct=(Araw+R)*F-Araw
assert s.simplify(geom-direct)==0
subs={eta:s.Rational(3,4),k:s.sqrt(s.Rational(1,2)),kr:1}
num=lambda z:complex(s.N(z.subs(subs),16))
expected=[
    (Araw,complex(-3.5878195299641042,.30304576336566313)),
    (Aiso,complex(-s.sqrt(3).evalf(),0)),
    (R,complex(5.567306167185677,-.9091372900969894)),
    ((2*F+1)*R/3,complex(5.2575386684856795,.8931310078062333)),
    ((F-1)*Aiso,complex(.2745803087865817,-.7962197623586393)),
    (geom,complex(5.532118977272262,.0969112454475938))
]
for expression,correct in expected:
    assert abs(num(expression)-correct)<1e-10
assert s.limit(geom,kr,0)==R
print("PASS corrected finite-arm trace basis, general A_iso=-sqrt(3),")
print("     two independently derived arm formulas and local limit")
for title,exp in [("R",R),("W",W),("A_iso",Aiso),
                  ("STF part",(2*F+1)*R/3),("trace leakage",(F-1)*Aiso),
                  ("FULL fixed-time proxy",geom)]:
    print(title,num(exp))
print("OPEN causal photon/mirror/clock, compact 3D Maxwell packet, q2 action")
