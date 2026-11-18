#!/usr/bin/env python3
"""Gravity v15.1132: simultaneous mechanical and paired-Jxy readouts.

The two-input model has g (tidal Hessian) and dG (magnetic gradient drift)
and two independent measurements y=(dtheta,dCxy).
The spin readout by itself cannot identify both; the two-channel matrix
is invertible when the tidal torque and gradient readout are nonzero.
The spin noise result is ideal shot/projection noise, not detector sensitivity.
"""
import sympy as s
theta,G,d,gamma,tau,DQ,kappa,In,drag,omega,phi,N=s.symbols(
    'theta G d gamma tau DQ kappa In drag omega phi N',
    real=True,positive=True)
chi=1/(kappa-In*omega**2-s.I*drag*omega)
A=chi*DQ*s.sin(2*theta)
W=(s.exp(s.I*omega*tau)-1)/(s.I*omega)
B=-2*s.sin(phi)*gamma*G*d*s.sin(theta)*W
Z=2*s.sin(phi)*gamma*d*s.cos(theta)*W
matrix=s.Matrix([[A,0],[B*A,Z]])
assert s.simplify(matrix.det()-A*Z)==0
assert matrix.rank()==2
yth,yspin=s.symbols('yth yspin')
sol=s.simplify(matrix.inv()*s.Matrix([yth,yspin]))
assert s.simplify(sol[0]-yth/A)==0
assert s.simplify(sol[1]-(yspin-B*yth)/Z)==0
mean=-2*s.cos(phi)
variance=4-mean**2
assert s.simplify(variance-4*s.sin(phi)**2)==0
assert s.simplify(s.diff(mean,phi).subs(phi,s.pi/2)-2)==0
assert s.simplify(variance.subs(phi,s.pi/2)-4)==0
f=s.sin(theta)*s.sin(2*theta)
noise=s.simplify(kappa/(gamma*G*d*tau*DQ*f*s.sqrt(N)))
optimal=s.asin(s.sqrt(s.Rational(2,3)))
expected=3*s.sqrt(3)*kappa/(4*gamma*G*d*tau*DQ*s.sqrt(N))
assert s.simplify(s.trigsimp(noise.subs(theta,optimal))-expected)==0
print('PASS dual channel identifiability and exact inverse for tidal g, magnetic dG')
print('PASS paired Jxy projection variance, ideal 1/sqrt(N) sensitivity')
print('determinant=',s.simplify(matrix.det()))
print('ideal DC tidal g shot-noise at optimal orientation=',expected)
print('LIMIT: measured spin readout alone is not identifiable; other noise omitted')
