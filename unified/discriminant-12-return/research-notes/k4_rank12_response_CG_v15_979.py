#!/usr/bin/env python3
"""Gravity v15.979: source-independent q=0 CG shape ratios for the
matched-D closed Schwinger EM/quarter sectors under ONE assumed physical
SU2. This is a standard Wigner-Eckart comparator, not a prediction of G.
"""
import sympy as s
from sympy.physics.wigner import clebsch_gordan

def profile(D,k):
    j=s.Rational(D-1,2)
    J=s.Rational(2*D-1,2)
    ms=[-j+i for i in range(int(2*j)+1)]
    return [s.simplify(clebsch_gordan(j,k,J,m,0,m)**2) for m in ms]

assert profile(2,1)==[s.Rational(2,3)]*2
assert profile(2,2)==[s.Rational(2,5)]*2
assert profile(4,2)==[s.Rational(2,7),s.Rational(18,35),s.Rational(18,35),s.Rational(2,7)]
assert profile(4,2)[1]/profile(4,2)[0]==s.Rational(9,5)
for D in range(2,20):
    j=s.Rational(D-1,2); J=s.Rational(2*D-1,2)
    for k in (1,2):
        allowed=(D%2==0 and k>=s.Rational(D,2) and k<=j+J)
        for i in range(D):
            m=-j+i
            strength=sum((clebsch_gordan(j,k,J,m,q,m+q)**2
                          for q in range(-k,k+1) if abs(m+q)<=J),s.Integer(0))
            assert s.simplify(strength-(s.Rational(2*D,D) if allowed else 0))==0
        if not allowed:
            assert profile(D,k)==[0]*D
print('PASS: axial profiles, D4 9/5, full polarization sums, D=2..19')
