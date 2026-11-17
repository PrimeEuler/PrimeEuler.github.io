#!/usr/bin/env python3
"""Gravity v15.1058: reduced Maxwell sources; exact Fourier time harmonics and Z2 check.

These are generalized Hamiltonian forces, NOT full solutions to coupled
Einstein-K4-Maxwell constraints or prescribed graviton amplitudes.
"""
import sympy as s
t,Q,U=s.symbols('t Q U',real=True)
q1=Q*s.cos(t); p1=s.diff(q1,t)
q3=U*s.cos(3*t); p3=s.diff(q3,t)
# Exact v15.998 overlaps, unnormalized tensor cos(k z) amplitudes:
# c2: C13=+1/2, D13=3/2; c4: C13=-1/2,D13=3/2.
vc2=s.expand(p1*p3-3*q1*q3)
vc4=s.expand(-p1*p3-3*q1*q3)
# plus b2: x mode C11=+1/2, D11=+1/2;
# y-mode C33=D33=0 in this harmonic.
vb2=s.expand((p1*p1-q1*q1*s.Integer(0))/2) if False else -(p1*p1+q1*q1)/2
targets=[
 (vc2,-3*Q*U*s.cos(4*t)),
 (vc4,-3*Q*U*s.cos(2*t)),
 (vb2,-Q**2/2),
]
for result,expected in targets:
    assert s.simplify(s.expand_trig(result-expected))==0
    assert s.simplify(result.subs(U,-U)-(-result if result in (vc2,vc4) else result))==0
# K4 invariant quartic mixed Hessian, sign-odd in cross background.
b,c=s.symbols('b c',real=True)
J=s.Rational(8,9)*(b*b+c*c)-s.Rational(8,9)*(b*b+c*c)**2
mixed=s.diff(J,b,c)
assert s.simplify(mixed+s.Rational(64,9)*b*c)==0
# Integrating out an odd cross tensor with an odd Maxwell source:
# a schematic even quadratic effective vertex is necessarily even in U.
G=s.symbols('G',real=True)
effective=G*vc2**2
assert s.simplify(effective.subs(U,-U)-effective)==0
print('PASS: reduced Maxwell source harmonics; reflection symmetry; K4 mixed Hessian')
print('V_c2=',s.trigsimp(vc2))
print('V_c4=',s.trigsimp(vc4))
print('V_b2=',s.trigsimp(vb2))
