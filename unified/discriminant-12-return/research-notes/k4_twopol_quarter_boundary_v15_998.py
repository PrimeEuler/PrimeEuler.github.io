#!/usr/bin/env python3
"""v15.998: exact two-polarization Maxwell vertex and K4 parity control.
x-polarized sin(z) at omega=1; y-polarized sin(3z) at omega=3.
TT transverse metric exp(2S), S=[[b,c],[c,-b]].
No on-shell b0 or physical two-circle identification assumed.
"""
import sympy as s
z=s.symbols('z',real=True)
a,ad,d,dd=s.symbols('a ad d dd',commutative=True)
b,c=s.symbols('b c',real=True)
e1=s.sqrt(2/s.pi)*s.sin(z)
e3=s.sqrt(2/s.pi)*s.sin(3*z)
q1=(a+ad)/s.sqrt(2)
p1=-s.I*(a-ad)/s.sqrt(2)
q3=(d+dd)/s.sqrt(6)
p3=-s.I*s.sqrt(s.Rational(3,2))*(d-dd)
def overlap(k):
    h=s.cos(k*z)
    return (s.simplify(s.integrate(h*e1*e3,(z,0,s.pi))),
            s.simplify(s.integrate(h*s.diff(e1,z)*s.diff(e3,z),(z,0,s.pi))))
assert overlap(0)==(0,0)
assert overlap(2)==(s.Rational(1,2),s.Rational(3,2))
assert overlap(4)==(-s.Rational(1,2),s.Rational(3,2))
assert overlap(6)==(0,0)
# Canonical H=1/2 int p^T exp(2S)p + 1/2 int A'^T exp(-2S) A'.
Vplus0=s.expand(p1*p1-q1*q1)
Vcross2=s.expand(2*(overlap(2)[0]*p1*p3-overlap(2)[1]*q1*q3))
Vcross4=s.expand(2*(overlap(4)[0]*p1*p3-overlap(4)[1]*q1*q3))
assert s.simplify(Vplus0+a*a+ad*ad)==0
assert s.simplify(Vcross2+s.sqrt(3)*(a*d+ad*dd))==0
assert s.simplify(Vcross4+s.sqrt(3)*(a*dd+ad*d))==0
# Top-degree normal-ordered symbols: quantum contractions do not create degree 4.
p=s.Poly(s.expand(2*Vplus0*Vcross4),ad,dd,a,d)
assert s.simplify(p.coeff_monomial(ad**3*d)-2*s.sqrt(3))==0
assert s.simplify(Vcross4.subs({d:-d,dd:-dd})+Vcross4)==0
assert s.simplify(Vplus0.subs({d:-d,dd:-dd})-Vplus0)==0
assert s.simplify((Vcross2*Vcross4).subs({d:-d,dd:-dd})-Vcross2*Vcross4)==0
assert s.Poly(s.expand(Vcross2*Vcross4),ad,dd,a,d).coeff_monomial(ad**3*d)==0
r=s.symbols('r',real=True)
Jrad=(1+2*s.cosh(4*r))/(1+2*s.cosh(2*r))**2-s.Rational(1,3)
assert s.simplify(s.series(Jrad,r,0,5).removeO()-(s.Rational(8,9)*r*r-s.Rational(8,9)*r**4))==0
J4=s.Rational(8,9)*(b*b+c*c)-s.Rational(8,9)*(b*b+c*c)**2
assert s.simplify(s.diff(J4,b,c).subs(c,0))==0
assert s.simplify(s.diff(J4,c,2).subs(c,0)-(s.Rational(16,9)-s.Rational(32,9)*b*b))==0
e0=1/s.sqrt(s.pi)
e4=s.sqrt(2/s.pi)*s.cos(4*z)
I04=s.simplify(s.integrate(e0*e4*s.cos(2*z)**2,(z,0,s.pi)))
assert I04==s.sqrt(2)/4
print('PASS exact two-pol Maxwell modes, plus/cross selection and K4 reflection')
print('Vplus_0=',Vplus0, 'Vcross_2=',Vcross2, 'Vcross_4=',Vcross4)
print('conditional plus0-cross4 O4 coefficient=',2*s.sqrt(3))
print('K4 b-c kernel at c=0: zero; cross-cross overlap=',I04)
