#!/usr/bin/env python3
"""Gravity v15.885: can velocity-axis nodes, action circle and tangency select a clock?

The constant-proper-acceleration worldline is x(t)=(c^2/a)(sqrt(1+(at/c)^2)-1)
with beta=v/c=(at/c)/sqrt(1+(at/c)^2), t(beta)=(c/a)*beta/sqrt(1-beta^2).
The m/s axis nodes beta=1/4,1/2 have times proportional to 1/a.
Tangency at the shared vertex is exact for every a>0; unit-normalized
parabola and hyperbola shapes are invariant under acceleration rescaling.

The constant-force bouncer J(E)=4sqrt(2) E^(3/2)/(3 a sqrt(m))
can be set equal to 2pi*hbar*(n+alpha) but this fixes E as a
function of supplied acceleration and mass, not acceleration.
This is a no-selector result, not a claim of a new force or quantum clock.
"""
import sympy as s

c,a,t,beta,E,m,hbar,N=s.symbols('c a t beta E m hbar N',positive=True)
u=a*t/c
xrel=c*c/a*(s.sqrt(1+u*u)-1)
xpar=s.Rational(1,2)*a*t*t
speed=s.simplify(s.diff(xrel,t))
assert s.simplify(speed/c-u/s.sqrt(1+u*u))==0
acc=s.simplify(s.diff(speed,t))
assert s.simplify(acc-a/(1+u*u)**s.Rational(3,2))==0
# The shared vertex has equal x, speed, acceleration; difference first at t^4.
assert s.simplify(xrel.subs(t,0))==0
assert s.simplify(s.diff(xrel,t).subs(t,0))==0
assert s.simplify(s.diff(xrel,t,2).subs(t,0)-a)==0
assert s.simplify(s.diff(xpar,t,2).subs(t,0)-a)==0
scaled_diff=s.simplify((a/c**2)*(xpar-xrel))
assert s.simplify(s.series(scaled_diff,t,0,8).removeO()-u**4/8+u**6/16)==0
# Convert velocity-axis nodes to coordinate time, not phase-time.
node_t=c*beta/(a*s.sqrt(1-beta*beta))
assert s.simplify(speed.subs(t,node_t)**2-(c*beta)**2)==0
# Branch is positive for 0<beta<1; check concrete conditional nodes.
for b in (s.Rational(1,4),s.Rational(1,2)):
    assert s.simplify(speed.subs(t,node_t.subs(beta,b))-c*b)==0
v1=s.Rational(1,4);v2=s.Rational(1,2)
gap=s.simplify(node_t.subs(beta,v2)-node_t.subs(beta,v1))
expected=c/a*(1/s.sqrt(3)-1/s.sqrt(15))
assert s.simplify(gap-expected)==0
assert s.simplify(gap.subs(a,7*a)/gap-s.Rational(1,7))==0
# A monotone trajectory crossing nodes alone is NOT a full oscillation.
# Constant proper-acceleration rapidity beta=tanh(a*tau/c).
rapidity=s.atanh(beta)
proper_t=c*rapidity/a
assert s.simplify(s.diff(proper_t,beta)-c/(a*(1-beta*beta)))==0
assert s.simplify((proper_t.subs(beta,v2)-proper_t.subs(beta,v1)).subs(a,7*a)/
                  (proper_t.subs(beta,v2)-proper_t.subs(beta,v1))-s.Rational(1,7))==0
# Both hyperbola and Galilean parabola have fixed dimensionless shape.
xi_h=s.sqrt(1+u*u)-1
xi_p=u*u/2
assert s.simplify((a/c**2)*xrel-xi_h)==0
assert s.simplify((a/c**2)*xpar-xi_p)==0
# Constant-force bouncer action: full back/forth momentum integral.
J=4*s.sqrt(2)*E**s.Rational(3,2)/(3*a*s.sqrt(m))
T=s.simplify(s.diff(J,E))
assert s.simplify(T-2*s.sqrt(2*E/m)/a)==0
energy=s.solve(s.Eq(J,2*s.pi*hbar*N),E)[0]
assert s.simplify(energy**3-(3*s.pi*hbar*N*a*s.sqrt(m)/(2*s.sqrt(2)))**2)==0
assert s.simplify(energy.subs(a,8*a)/energy-4)==0
period=s.simplify(T.subs(E,energy))
assert s.simplify(period.subs(a,8*a)/period-s.Rational(1,4))==0
assert s.simplify(J.subs(E,energy)-2*s.pi*hbar*N)==0
assert s.simplify(s.diff(energy,a))!=0
print('PASS shared parabola/hyperbola tangency, every a>0')
print('PASS conditional beta=1/4 to 1/2 lab node interval:',gap)
print('PASS node times vary as 1/a; no repeated cycle implied')
print('PASS same shape under acceleration rescaling')
print('PASS J=2*pi*hbar*N imposes E(a,m,N), not a itself')
print('PASS with a->8a: E->4E, bouncer T->T/4 at SAME action')
print('NEGATIVE no physical acceleration or frequency selector from geometry alone')
