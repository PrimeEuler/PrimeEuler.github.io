#!/usr/bin/env python3
"""Gravity v15.1100: exact accelerated worldline through confocal
parabola, moving secant, Lorentz hyperbola and projective sech circle.
Every geometric identity follows from existing Cone chart formulae;
no new force, frequency or physical scale is selected.
"""
import sympy as s
R,u,k,h,c,a,tau=s.symbols('R u k h c a tau',positive=True,real=True)
K=R*s.exp(u)
X=(K*K-R*R)/(2*K)
T=(K*K+R*R)/(2*K)
assert s.simplify((X-R*s.sinh(u)).rewrite(s.exp))==0
assert s.simplify((T-R*s.cosh(u)).rewrite(s.exp))==0
assert s.simplify(T*T-X*X-R*R)==0
assert s.simplify(K*K-2*K*X-R*R)==0
assert s.simplify((T-R)-(R*(s.cosh(u)-1)).rewrite(s.exp))==0
assert s.simplify((X-c*(c/a)*s.sinh(u)).rewrite(s.exp).subs(R,c*c/a))==0
circle_cos=s.sech(u)
circle_sin=s.tanh(u)
assert s.simplify(circle_cos**2+circle_sin**2-1)==0
theta=s.atan(s.sinh(u))
assert s.simplify(s.diff(theta,u)-s.sech(u))==0
assert s.simplify(s.diff(theta.subs(u,a*tau/c),tau)-a/c*s.sech(a*tau/c))==0
# The non-arbitrary scale R enters as the secant height. Mesh k is
# dimensionful, and half-step lattice means specifying a length unit.
Xk=(k*k-R*R)/(2*k)
Tk=(k*k+R*R)/(2*k)
assert s.simplify(Tk*Tk-Xk*Xk-R*R)==0
assert s.simplify(k*k-2*k*Xk-R*R)==0
assert s.simplify((Xk/Tk)**2+(R/Tk)**2-1)==0
theta_k=2*s.atan(k/R)-s.pi/2
assert s.simplify(s.diff(theta_k,k)-2*R/(k*k+R*R))==0
delta_tau=(c/a)*s.log((k+h)/k)
delta_theta=2*(s.atan((k+h)/R)-s.atan(k/R))
assert s.simplify(s.diff(delta_tau,k)+c*h/(a*k*(k+h)))==0
assert s.simplify(s.diff(delta_theta,k))!=0
# Inversion mirrors X but not T, and may not preserve a discrete mesh.
mirror=R*R/k
assert s.simplify(Xk.subs(k,mirror)+Xk)==0
assert s.simplify(Tk.subs(k,mirror)-Tk)==0
print('PASS: parabola/secant -> hyperbola -> sech circle, proper-time derivative and half-step nonuniformity')
print('theta(k+h)-theta(k)=',delta_theta)
print('tau(k+h)-tau(k)=',delta_tau)
