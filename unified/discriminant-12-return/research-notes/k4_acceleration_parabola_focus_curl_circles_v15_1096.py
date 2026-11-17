#!/usr/bin/env python3
"""Gravity v15.1096: focus of the near-seat acceleration parabola and
independent azimuthal Maxwell circulation radius.

The match with an idealized Zitterbewegung radius is CONDITIONAL on
Rindler length c^2/a = reduced Compton length. No Maxwell field or
action has selected that condition. The acceleration diagram uses
coordinates (x,ct), unlike spatial magnetic azimuthal planes.
"""
import sympy as s
t,c,acc,m,hbar,rho,rb,zoff=s.symbols(
    't c acc m hbar rho rb zoff',positive=True,real=True)
R=c*c/acc
worldline=R*(s.sqrt(1+(c*t/R)**2)-1)
assert s.simplify(s.diff(worldline,t).subs(t,0))==0
assert s.simplify(s.diff(worldline,t,2).subs(t,0)-acc)==0
# In length coordinate y=ct, x(y)=(a/2c²)y² +O(y⁴).
y=s.symbols('y',real=True)
x_y=R*(s.sqrt(1+(y/R)**2)-1)
parabolic=s.expand(s.series(x_y,y,0,6).removeO())
assert s.simplify(parabolic.coeff(y,2)-1/(2*R))==0
assert s.simplify(parabolic.coeff(y,4)+1/(8*R**3))==0
focus=1/(2*s.diff(x_y,y,2).subs(y,0))
osculating=1/s.diff(x_y,y,2).subs(y,0)
assert s.simplify(focus-R/2)==0
assert s.simplify(osculating-R)==0
lambdaC=hbar/(m*c)
azb=hbar/(2*m*c)
accStar=m*c**3/hbar
assert s.simplify(focus.subs(acc,accStar)-azb)==0
# Unfixed positive scale rho from preexisting v15.886.
acc_rho=m*c**3/(rho*hbar)
assert s.simplify(focus.subs(acc,acc_rho)-rho*azb)==0
assert s.simplify(osculating.subs(acc,acc_rho)-rho*lambdaC)==0
# Purely azimuthal B around charge's motion axis has field-line
# circles at arbitrary cylindrical radius rb; no Maxwell selection.
Bphi=rb/(rb**2+zoff**2)**s.Rational(3,2)
assert s.simplify(s.diff(Bphi,rb).subs(rb,zoff/s.sqrt(2)))==0
# Any extremum of this representative transverse profile depends
# on the arbitrary axial observer separation zoff.
assert s.simplify((zoff/s.sqrt(2))/focus.subs(acc,accStar)-
                  s.sqrt(2)*m*c*zoff/hbar)==0
print('PASS: osculating parabola focus c²/(2a), curvature circle c²/a')
print('PASS: at imposed Compton acceleration focus equals hbar/(2mc)')
print('PASS: free scale rho remains, and B azimuthal circles have no selected radius')
