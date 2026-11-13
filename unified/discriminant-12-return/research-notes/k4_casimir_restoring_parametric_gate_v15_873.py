#!/usr/bin/env python3
"""v15.873: Casimir squared-half-step versus restoring-force/parametric energy gate.

Algebraic paired-level identity is independent of oscillator dynamics.
Actual oscillator with stiffness k(t) exchanges energy through kdot*x²/2,
not by a force maximum alone. For a weak 2 omega modulation of k,
leading-order net work in one unperturbed cycle is pi*A²*delta_k*cos(phi)/2.
The phase, stiffness modulation and an energy source must be specified;
the sector offset h/2 itself fixes none of those quantities.
"""
import sympy as s
j,h=s.symbols('j h', real=True)
A,m,omega,delta_k=s.symbols('A m omega delta_k',positive=True)
t,phi=s.symbols('t phi',real=True)
AM=h*(j+s.Rational(1,2));GM2=h*h*j*(j+1)
assert s.expand(AM**2-(h/2)**2-GM2)==0
for step,offset in [(s.Integer(1),s.Rational(1,4)),(s.Rational(1,2),s.Rational(1,16))]:
    assert s.simplify((h*h/4).subs(h,step)-offset)==0
# x=A cos(wt); k(t)=m w²+delta_k*sin(2wt+phi).
# Mechanical energy E=mv²/2+k(t)x²/2, so dE/dt=kdot*x²/2
# for trajectories satisfying m xddot + k(t)x=0.
x=A*s.cos(omega*t)
xprime=s.diff(x,t)
k=m*omega**2+delta_k*s.sin(2*omega*t+phi)
E=m*xprime**2/2+k*x**2/2
# Off-shell derivative identity plus m*xddot+k*x=0:
res=s.simplify(s.diff(E,t)-s.diff(k,t)*x*x/2-
                 xprime*(m*s.diff(x,t,2)+k*x))
assert res==0
work_rate=s.diff(k,t)*x*x/2
one_cycle=s.simplify(s.integrate(work_rate,(t,0,2*s.pi/omega)))
assert s.simplify(one_cycle-s.pi*A*A*delta_k*s.cos(phi)/2)==0
for phase,val in [(0,1),(s.pi/2,0),(s.pi,-1)]:
    assert s.simplify(one_cycle.subs(phi,phase)-
       val*s.pi*A*A*delta_k/2)==0
# At turning points x=+/-A, speed=0; stiffness changes can
# still exchange energy with its external actuator via kdot*x²/2.
assert s.simplify(xprime.subs(t,0))==0
assert s.simplify(work_rate.subs({t:0,phi:0})-
                  delta_k*omega*A*A)==0
# If stiffness itself is maximum at t=0 then kdot=0 and no
# instantaneous energy transfer despite maximum restoring force.
assert s.simplify(work_rate.subs({t:0,phi:s.pi/2}))==0
# Bare restoring-force maximum and squared half-step are separate.
assert not one_cycle.has(h)
assert s.simplify(one_cycle.subs(delta_k,0))==0
print('PASS exact paired-level Casimir offsets: EM=1/4, G-mesh=1/16')
print('PASS dE/dt=kdot*x^2/2 for parametric stiffness')
print('PASS weak-modulation work over one unperturbed period:',one_cycle)
print('PASS phases 0/gain, pi/2/zero, pi/loss')
print('NEGATIVE no gain or physical modulation supplied by Casimir offset alone')
