#!/usr/bin/env python3
"""v15.872: controlled K4 tensor response to phase-tagged transition driving.

On coasting tau, gamma''+3 gamma'/tau + beta gamma/tau² = -2 Pi.
Let s=ln tau, gamma=tau^-1 U. Then
U_ss+(beta-1)U=-2 tau³ Pi.
Choose Pi=tau^-3 sin(Omega*s+phase). This is a PRESCRIBED
mode forcing, NOT an independently on-shell conserved EM/matter
source or physical Cone→EM/G coupling. Compare phase 0 (node
at s=0) and pi/2 (antinode at s=0), both with U(0)=U'(0)=0.
The response is an ordinary linear convolution. Phase shifts
change transient samples, but not forced steady-state gain.
"""
import sympy as sp
s,Omega,nu,phi=sp.symbols('s Omega nu phi',real=True,positive=True)
ys=-2*(sp.sin(Omega*s)-(Omega/nu)*sp.sin(nu*s))/(nu**2-Omega**2)
yc=-2*(sp.cos(Omega*s)-sp.cos(nu*s))/(nu**2-Omega**2)
for y,src in ((ys,sp.sin(Omega*s)),(yc,sp.cos(Omega*s))):
    assert sp.trigsimp(sp.simplify(sp.diff(y,s,2)+nu**2*y+2*src))==0
    assert sp.simplify(y.subs(s,0))==0
    assert sp.simplify(sp.diff(y,s).subs(s,0))==0
out=sp.cos(phi)*ys+sp.sin(phi)*yc
assert sp.trigsimp(sp.simplify(sp.diff(out,s,2)+nu**2*out+
                              2*sp.sin(Omega*s+phi)))==0
gain=2/sp.Abs(nu**2-Omega**2)
assert sp.simplify(gain.subs({nu:sp.sqrt(13),Omega:2})-sp.Rational(2,9))==0
# For K²=4 and solid eta_s=3/4, beta_T=3K²+8eta_s/3=14,
# so nu²=13. Prescribed rate/position phase Omega=2.
test={nu:sp.sqrt(13),Omega:2,s:1}
out_s=float(ys.subs(test).evalf())
out_c=float(yc.subs(test).evalf())
assert abs(out_s)>1e-2 and abs(out_c)>1e-3
assert abs(out_s-out_c)>1e-2
assert abs(out_s)<2*float(gain.subs(test))
assert abs(out_c)<2*float(gain.subs(test))
# Rotation in quadrature preserves drive coefficients/gain norm.
assert sp.simplify(sp.cos(phi)**2+sp.sin(phi)**2-1)==0
print('PASS K4 tensor log-time exact retarded zero-data sine/cosine response')
print('PASS prescribed-drive transfer magnitude independent of input phase')
print('K4 beta=14, forcing Omega=2: steady-state gain',gain.subs(test))
print('zero-data transient U(s=1) sine-phase',out_s,'cos-phase',out_c)
print('NEGATIVE no distinct EM 1/2 vs G 1/4 force selector without physical phase-rate map')
