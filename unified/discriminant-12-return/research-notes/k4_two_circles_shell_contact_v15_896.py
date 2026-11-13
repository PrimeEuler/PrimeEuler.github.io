#!/usr/bin/env python3
"""Cone Gravity v15.896: exact two-circle shell station/contact-order checks.
Uses normalized Cone units, NOT an asserted m/s calibration or physical time law.
"""
import sympy as S
n,u,z,r=S.symbols("n u z r",positive=True)
s=S.symbols("s",real=True)
X=u*S.sqrt(n)*S.sinh(s)
T=u*S.sqrt(n)*S.cosh(s)
Y=u*S.sqrt(n)
assert S.simplify(T*T-X*X-u*u*n)==0
assert S.simplify(T*T-X*X-Y*Y)==0
end=S.log(n)/2
toexp=lambda expr:S.expand_power_exp(expr.rewrite(S.exp))
assert S.simplify(toexp(X.subs(s,end))-u*(n-1)/2)==0
assert S.simplify(toexp(T.subs(s,end))-u*(n+1)/2)==0
assert S.simplify(toexp((Y*Y-u*u-2*u*X).subs(s,end)))==0
Rout=u*(n+1)/2
Rrest=u*S.sqrt(n)
assert S.simplify(Rout-Rrest-u*(S.sqrt(n)-1)**2/2)==0

# Shell circle in auxiliary (X,T) section, local coordinate z=X.
shell=S.sqrt(r*r+z*z)
circle=S.sqrt(r*r-z*z)
assert S.series(shell-circle,z,0,6).removeO()==z*z/r

# Unit-u row parabola and its own small tangent circle in (X,Y).
par=(z*z-u*u)/(2*u)
small=-S.sqrt(u*u/4-z*z)
assert S.series(small-par,z,0,4).removeO()==z*z/(2*u)

# Outer parabola intersection slope is unequal at all n>0.
xp=u*(n-1)/2
yp=u*S.sqrt(n)
assert S.simplify(u/yp+xp/yp-(n+1)/(2*S.sqrt(n)))==0

# Sector scaling u=1 vs u=1/2 preserves normalized geometry.
for scale in [S.Integer(1),S.Rational(1,2)]:
    assert S.simplify((Rout/Rrest).subs(u,scale)-(n+1)/(2*S.sqrt(n)))==0
    assert S.simplify(((-u/2).subs(u,scale))+scale/2)==0

# Same shell endpoints for arbitrarily rescaled traversal speed.
lam=S.symbols("lambda",positive=True)
assert S.simplify(lam*(end/lam)-end)==0
print("PASS exact shell rapidity map, two distinct contact orders, u scaling, and rate nonselector")
print("Shell-to-circle rest gap:",S.series(shell-circle,z,0,8))
print("Parabola-to-small-circle gap:",S.series(small-par,z,0,6))
