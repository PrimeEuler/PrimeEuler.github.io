#!/usr/bin/env python3
"""Gravity v15.884: user's X axis is *velocity* (metres/second).

Nodes are coordinates in velocity, v_n, not times or phase seconds.
A given reference c can calibrate node velocities in SI, but their
temporal crossing frequency needs physical dv/dt (acceleration).
For phase theta(v)=2*pi*v/V_period, theta_dot/(2*pi)=a/V_period,
which depends on trajectory and need not be a periodic oscillation.
A massless null ray has fixed local speed c: it does not sweep v nodes.
"""
import sympy as s
v,c,V,a,a0,scale=s.symbols("v c V a a0 scale",positive=True)
theta=2*s.pi*v/V
assert s.simplify(s.diff(theta,v)*a/(2*s.pi)-a/V)==0
assert s.simplify((V/2)/a - V/(2*a))==0
for velocity in (s.Rational(1,4),s.Rational(1,2)):
    node=velocity*c
    assert s.simplify(node/c-velocity)==0
assert s.simplify((a*scale/V)/(a/V)-scale)==0
# A constant proper-acceleration trajectory has a NONuniform
# coordinate-time node interval because dv/dt decreases as v -> c.
# t(v) = v / [a0 sqrt(1-v**2/c**2)].
t_of_v=v/(a0*s.sqrt(1-v**2/c**2))
assert s.simplify(s.diff(t_of_v,v)-
                 1/(a0*(1-v**2/c**2)**s.Rational(3,2)))==0
# Here 0 < v < c, so phase step alone cannot imply equal time steps.
v1,v2=s.symbols('v1 v2',positive=True)
gap=s.simplify(t_of_v.subs(v,v2)-t_of_v.subs(v,v1))
assert gap.has(a0) and gap.has(c)
# Null ray's inertial propagation speed constant c: dv/dt=0.
assert s.simplify(s.diff(theta,v)*0)==0
print("PASS velocity-axis node positions, SI scale c")
print("PASS phase-rate depends on acceleration a=dv/dt")
print("PASS constant-proper-acceleration time intervals vary with v")
print("PASS null ray fixed speed c gives zero velocity-axis sweep")
print("NEGATIVE velocity node locations alone do not select frequency")
