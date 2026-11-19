#!/usr/bin/env python3
"""v15.1197: complete scalar-Riemann fixed-time finite-arm spatial proxy.
Combine the existing v15.1195 analytic traveling-null-Maxwell scalar
Bardeen transfer and the v15.793 spatial line-sampling formula.
This is NOT the v15.1196 compact source, and NOT a causal photon-mirror
clock simulation; the trace A is known here only for an eternal Fourier
particular solution on the original K4 Einstein+solid background.
"""
import sympy as s
I=s.I
eta=s.Rational(3,4)
k=s.sqrt(s.Rational(1,2))
w=s.sqrt(3)*k
nu2=(8*eta-3)*(1+k*k)/3
D=(-1-I*w)**2+nu2
x=-2-I*w
p=-3*s.sqrt(3)/(k*k*D)
phi=((x*x+x)*p/3+s.sqrt(3)-3*I*k*(-1-I*w)/(2*k*k))/(1+k*k)
psi=((k*k-x)*p/3+s.sqrt(3)/2+3*I*k/(2*k*k))/(1+k*k)
R=-3*k*k*phi
W=3*k*k*(phi+psi)/2
A=(x*x+x)*psi+x*phi
# Ricci decomposition: R_STF=Weyl-0.5 spatial Ricci STF.
assert s.simplify(R-W+3*k*k*(3*phi+psi)/2)==0
# kL=1. Along z an arm samples e^(ikz), but along x at z=0 it does not.
F=(s.exp(I)-1)/I
STF=(2*F+1)*R/3
leak=(F-1)*A
response=STF+leak
value=lambda z:complex(s.N(z,15))
expected=[
    (R,complex(5.567306167185677,-.9091372900969894)),
    (W,complex(-3.7115374447904514,2.727411870290968)),
    (A,complex(-3.5878195299641042,.30304576336566313)),
    (STF,complex(5.2575386684856795,.8931310078062333)),
    (leak,complex(.4294640581365803,-1.69735391131025)),
    (response,complex(5.687002726622261,-.8042229035040176))
]
for term,target in expected:
    assert abs(value(term)-target)<1e-10
# The arm identity holds for arbitrary (complex) scalar-curvature amplitudes.
S,A0,G=s.symbols('S A0 G')
assert s.expand((A0+2*S/3)*G-(A0-S/3)-
                ((2*G+1)*S/3+(G-1)*A0))==0
print('PASS v15.1197 full scalar fixed-time arm response and Ricci leakage')
for label,e in [('R_STF',R),('Weyl',W),('isotropic A',A),
                ('sampled STF',STF),('isotropic leakage',leak),
                ('complete arm proxy',response)]:
    print(label,value(e))
print('OPEN compact Maxwell initial isotropic A(z), K4 source evolution,')
print('     gauge-complete causal photon/mirror/clock response and q2 physics')
