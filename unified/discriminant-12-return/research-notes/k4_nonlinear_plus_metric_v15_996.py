#!/usr/bin/env python3
"""v15.996: even pure-plus K4 solid and canonical second-order
metric-Maxwell vertex in the same 1D PEC photon mode pair (1,3).
Fixed homogeneous isotropic K4 background; NOT general tensor helicities.
"""
import sympy as s
b,z=s.symbols("b z",real=True)
J=(s.exp(4*b)+s.exp(-4*b)+1)/(s.exp(2*b)+s.exp(-2*b)+1)**2-s.Rational(1,3)
assert s.simplify(J.subs(b,-b)-J)==0
assert s.simplify(s.series(J,b,0,8).removeO()-
                  (s.Rational(8,9)*b*b-s.Rational(8,9)*b**4+
                   s.Rational(112,135)*b**6))==0
assert s.diff(J,b,3).subs(b,0)==0
# In x/y-symmetric Einstein+K4 solid action x<->y sends b->-b;
# hence all odd pure-plus vertices vanish in this restricted ansatz.
f=[s.sqrt(2/s.pi)*s.sin(n*z) for n in (1,3)]
def mat(h,grad):
    return s.Matrix(2,2,lambda i,j:s.simplify(
       s.integrate(h*s.diff(f[i],z,grad)*s.diff(f[j],z,grad),(z,0,s.pi))))
C2,D2=mat(s.cos(2*z),0),mat(s.cos(2*z),1)
C22,D22=mat(s.cos(2*z)**2,0),mat(s.cos(2*z)**2,1)
C0,D0=mat(1,0),mat(1,1)
C4,D4=mat(s.cos(4*z),0),mat(s.cos(4*z),1)
assert C22==(C0+C4)/2 and D22==(D0+D4)/2
# Photon L kinetic matrix G=I+2b C2+2b² C22+..., so
# H at order b² contains p^T(2 C2²-C22)p + q^T D22 q.
Q2=s.simplify(2*C2*C2-C22)
assert Q2==s.Matrix([[s.Rational(1,2),-s.Rational(1,4)],
                     [-s.Rational(1,4),0]])
assert D22==s.Matrix([[s.Rational(1,2),s.Rational(3,4)],
                       [s.Rational(3,4),s.Rational(9,2)]])
a,c,ad,cd=s.symbols("a c ad cd")
ann=[a,c];dag=[ad,cd];omega=[1,3]
q=s.Matrix([(ann[i]+dag[i])/s.sqrt(2*omega[i]) for i in range(2)])
p=s.Matrix([-s.I*s.sqrt(s.Rational(omega[i],2))*(ann[i]-dag[i]) for i in range(2)])
V2=s.expand((p.T*Q2*p+q.T*D22*q)[0])
poly=s.Poly(V2,ad,cd,a,c)
assert poly.coeff_monomial(ad**2)==0
assert poly.coeff_monomial(ad*c)==0
assert poly.coeff_monomial(ad*cd)==s.sqrt(3)/2
assert poly.coeff_monomial(ad**3*c)==0
assert poly.total_degree()==2
print("PASS pure-plus K4 odd cubic zero; nonlinear Maxwell b² Hamiltonian has pairs but no lower-mode squeeze, photon conversion or bare O4")
print("J(b)=",s.series(J,b,0,8))
print("C22=",C22,"D22=",D22,"canonical Q2=",Q2)
print("V2=",s.factor(V2))
