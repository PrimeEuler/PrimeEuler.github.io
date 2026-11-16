#!/usr/bin/env python3
"""Gravity v15.1053: exact confocal parabola / secant-to-circle
radial compactification, transported from T-cone to signed X-cone.
Separate half-step parabola labels from equally spaced circle abscissae.
No physical time/force source or open-quarter T coupling is posited.
"""
import sympy as s
k,n,A,l=s.symbols("k n A l",positive=True)
T=(k+n/k)/2
X=(k-n/k)/2
Y=s.sqrt(n)
xc=s.factor(A*X/T)
yc=s.factor(A*Y/T)
assert s.simplify(T*T-X*X-n)==0
assert s.simplify(xc*xc+yc*yc-A*A)==0
assert s.simplify(xc-A*(k*k-n)/(k*k+n))==0
assert s.simplify(yc-2*A*k*s.sqrt(n)/(k*k+n))==0
assert s.simplify((n-k*k)/(2*k)+X)==0
# A signed second factor creates the X-cone:
# (k,n/k) -> (k,-n/k) has (T_X,X_X,R_X)=(X,T,Y).
TX=X;XX=T;RR=Y
assert s.simplify(XX*XX-TX*TX-RR*RR)==0
assert s.simplify(A*TX/XX-xc)==0
assert s.simplify(A*RR/XX-yc)==0
# The real circle is the rational stereographic compactification
# of positive q=k/sqrt(n), not a uniformly angular map of k-grid.
assert s.simplify(s.diff(xc,k)-4*A*n*k/(k*k+n)**2)==0
assert s.simplify(s.diff(yc,k)-2*A*s.sqrt(n)*(n-k*k)/(k*k+n)**2)==0
q=s.symbols("q",real=True)
qp=s.factor((l*l*(1+q)-(1-q))/(l*l*(1+q)+(1-q)))
assert s.simplify(qp.subs(q,(k*k-n)/(k*k+n)) -
    (l*l*k*k-n)/(l*l*k*k+n))==0
# n=11, outer n+1 diameter 12 has A=6.
# k=1 and 11 are exact circle ladder endpoints; k=2 is NOT
# the j=2 circle ladder abscissa, which is -4.
assert xc.subs({n:11,A:6,k:1})==-5
assert yc.subs({n:11,A:6,k:1})==s.sqrt(11)
assert xc.subs({n:11,A:6,k:2})==-s.Rational(14,5)
assert xc.subs({n:11,A:6,k:2})!=-4
for j in range(1,12):
    xx=s.Integer(j)-6
    yy=s.sqrt(j*(12-j))
    assert s.simplify(xx*xx+yy*yy-36)==0
# The hinge R=0 for n>0 does not occur at positive finite k;
# the circle reaches boundary only as k -> 0 or +infinity.
assert s.limit(yc,k,0,dir="+")==0
assert s.limit(yc,k,s.oo)==0
print("PASS: exact secant-to-circle mapping, signed X-cone mirror,")
print("Pell Mobius action, nonuniform half-step sampling, n+1 circle test.")
print("x_A=",xc," y_A=",yc,"Pell q transform=",qp)
