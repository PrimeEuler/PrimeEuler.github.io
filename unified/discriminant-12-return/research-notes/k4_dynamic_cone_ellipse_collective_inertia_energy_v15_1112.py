#!/usr/bin/env python3
"""Gravity v15.1112: exact collective shape electric inertia of the compact
cone-ellipse magnetic field, conditional electromechanical oscillator,
and finite tidal pulse energy bookkeeping. The varying current is prescribed
by a material constraint: this reduced ansatz is NOT source-free Maxwell.
"""
import sympy as s
import numpy as np
from scipy.integrate import solve_ivp
r,p,e,C,psi,eps0,mu0=s.symbols('r p e C psi eps0 mu0',positive=True,real=True)
D=1-e**2
A=C/D; B=C/s.sqrt(D); d=-C*e/D
qdot=-2*r*s.cos(p)*s.diff(d,e)/A-2*r*r*(s.cos(p)**2*s.diff(A,e)/A+s.sin(p)**2*s.diff(B,e)/B)
assert s.trigsimp(qdot-2*(r*(1+e**2)*s.cos(p)-e*r*r*(1+s.cos(p)**2))/D)==0
Fp=-4*(1-r*r)**3
assert s.integrate(r**3*Fp**2,(r,0,1))==s.Rational(1,7)
assert s.integrate(r**5*Fp**2,(r,0,1))==s.Rational(2,63)
ang=s.simplify(s.integrate(s.expand_trig(qdot**2).expand(),(p,0,2*s.pi)))
assert s.simplify(ang-s.pi*(4*r**2*(1+e**2)**2+19*e**2*r**4)/D**2)==0
M=s.simplify(eps0*psi**2*A*B*s.integrate(ang*Fp**2*r,(r,0,1)))
Mt=2*s.pi*eps0*psi**2*C**2*(18+55*e**2+18*e**4)/(63*D**s.Rational(7,2))
assert s.simplify(M-Mt)==0
K=4*s.pi*psi**2/(7*mu0)
U=K*(2-e**2)/(2*s.sqrt(D))
I=-K*e**2/s.sqrt(D)
assert s.simplify(s.diff(U,e)-K*e**3/(2*D**s.Rational(3,2)))==0
assert s.simplify(s.diff(U,e,2)-3*K*e**2/(2*D**s.Rational(5,2)))==0
assert s.simplify(s.series(U,e,0,6).removeO()-K-K*e**4/8)==0
assert s.simplify(s.series(I,e,0,4).removeO()+K*e**2)==0
assert s.simplify(s.diff(I,e).subs(e,0))==0
assert s.simplify(K/M.subs(e,0)-1/(eps0*mu0*C**2))==0
# Example passive support: Vwall = k*(e-e0)^2/2-U'(e0)*(e-e0).
# EOM derives from L=M(e)e_dot²/2-U(e)-Vwall(e)+h(t)I(e)/2;
# Rayleigh dissipation gamma*e_dot²/2. Energy accounting is exact
# within this constrained finite-dimensional model.
mfn=s.lambdify(e,M.subs({eps0:1,psi:1,C:1}),'numpy')
dmfn=s.lambdify(e,s.diff(M,e).subs({eps0:1,psi:1,C:1}),'numpy')
ufn=s.lambdify(e,U.subs({psi:1,mu0:1}),'numpy')
dufn=s.lambdify(e,s.diff(U,e).subs({psi:1,mu0:1}),'numpy')
ifn=s.lambdify(e,I.subs({psi:1,mu0:1}),'numpy')
difn=s.lambdify(e,s.diff(I,e).subs({psi:1,mu0:1}),'numpy')
e0=.3; kw=2.; gamma=.2; h0=.03
u0=float(dufn(e0))
V=lambda x:.5*kw*(x-e0)**2-u0*(x-e0)
dV=lambda x:kw*(x-e0)-u0
h=lambda t:h0*(1-t*t)**4 if abs(t)<1 else 0.
hd=lambda t:-8*h0*t*(1-t*t)**3 if abs(t)<1 else 0.
def ode(t,y):
    ev,v,w,loss=y
    accel=(-.5*dmfn(ev)*v*v-dufn(ev)-dV(ev)+.5*h(t)*difn(ev)-gamma*v)/mfn(ev)
    return [v,accel,-.5*hd(t)*ifn(ev),gamma*v*v]
sol=solve_ivp(ode,(-4,14),[e0,0,0,0],rtol=1e-11,atol=1e-13,max_step=.01)
assert sol.success
ee,vv,w,loss=sol.y[:,-1]
dEstored=.5*mfn(ee)*vv*vv+ufn(ee)+V(ee)-ufn(e0)-V(e0)
assert abs(dEstored+loss-w)<1e-8
assert w>0 and loss>0
print('PASS exact M(e), quartic U_B(e), zero linear tidal force at circle')
print('M(e)=',Mt)
print('K/M(0)=',s.simplify(K/M.subs(e,0)))
print('PASS passive finite-pulse energy identity')
print('gravity input:',w,'dissipation:',loss,'stored energy change:',dEstored,
      'closure residual:',dEstored+loss-w)
