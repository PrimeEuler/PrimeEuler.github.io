#!/usr/bin/env python3
"""v15.834: false elastic gradient energy when K4 solid phonon is frozen.
Using original J=tr(B²)/(tr B)²-1/3 and the v14.935 K4 action.
"""
import sympy as s
eps,a,uq,k,x,etas,C=s.symbols("eps a u k x eta_s C",positive=True,real=True)
U=s.Matrix([0,uq*s.cos(k*x),0])
D=s.Matrix([[s.diff(U[j],x) if i==0 else 0 for j in range(3)]
            for i in range(3)])
h=-D-D.T
# Pure coordinate spatial shear h=-partial U-partial U
Ewrong=-h           # freezes solid pi^I=0 INCORRECTLY
Eright=-h-D-D.T     # correct gauge pi^I=-U^I
assert Eright==s.zeros(3)
Bwrong=(s.eye(3)+eps*Ewrong)/a**2
Jwrong=s.factor(s.trace(Bwrong*Bwrong)/s.trace(Bwrong)**2-s.Rational(1,3))
J2=s.simplify(s.diff(Jwrong,eps,2).subs(eps,0)/2)
assert s.simplify(J2-2*uq**2*k**2*s.sin(k*x)**2/9)==0
assert s.simplify(J2.subs({uq:s.Rational(1,10),k:2,x:s.pi/4})
                 -s.Rational(2,225))==0
# L_matter background in conformal coordinates is -C a².
false_L=-C*a*a*etas*J2
assert s.simplify(false_L.subs({uq:s.Rational(1,10),k:2,x:s.pi/4})
                 +C*a*a*etas*s.Rational(2,225))==0
assert s.simplify(J2/(uq**2*k**2)-2*s.sin(k*x)**2/9)==0
print("PASS full solid displacement pi=-U gives J2=0")
print("FAIL if frozen phonon: spurious J2=",J2)
print("At u=0.1,k=2,x=pi/4: false J2=",s.Rational(2,225))
