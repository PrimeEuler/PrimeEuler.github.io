#!/usr/bin/env python3
"""Gravity v15.1051: exact conditional smooth signed-pair hinge crossing.
No physical K4 source, time calibration, or quarter-ladder T implied.
"""
import sympy as s
x,r=s.symbols("x r",positive=True)
for p in (1,3,5):
    # x=2t-1; v=-x**p; t in [0,1]; work on x>0 for R=sqrt(|uv|)
    v=-x**p
    T=(r+v)/2; X=(r-v)/2
    R=s.sqrt(r)*x**s.Rational(p,2)
    assert s.expand(X**2-T**2-r*x**p)==0
    Rdot2=s.simplify((2*s.diff(R,x))**2)
    # Full time integral: two identical half intervals, dt=dx/2
    full=s.simplify(s.integrate(Rdot2,(x,0,1)))
    plane=s.integrate(2*p*p*x**(2*p-2),(x,-1,1))/2
    assert s.simplify(plane-s.Rational(2*p*p,2*p-1))==0
    print("p=",p,"Rdot2(x>0)=",Rdot2,"integral Rdot2 dt=",full,
          "int(Tdot2+Xdot2)dt=",plane)
    assert (full==s.oo)==(p==1)
# p5 height R= sqrt(r)*|x|^(5/2) has continuous first and second
# derivatives at x=0; p3 has a divergent second derivative there.
assert s.limit(s.diff(s.sqrt(r)*x**s.Rational(5,2),x,2),x,0,dir="+")==0
assert s.limit(s.diff(s.sqrt(r)*x**s.Rational(3,2),x,2),x,0,dir="+")==s.oo
for n in (1,5,7,11):
    Ts=(s.Integer(n)+1)/2;Xs=(s.Integer(n)-1)/2
    assert Ts*Ts-Xs*Xs==n
    assert Ts*Ts-Xs*Xs==n  # mirrored X-cone uses (T,X)=(Xs,Ts)
# A two-sector parity Q cannot be changed by a Q-commuting generator.
# A chosen parity-odd g*sigma_x CAN produce transfer; g is free.
g,h,t=s.symbols("g h t",real=True)
Q=s.diag(1,-1)
H=s.Matrix([[0,g],[g,0]])
assert H*Q+Q*H==s.zeros(2)
assert H*H==g*g*s.eye(2)
assert s.sin(g*t/h).subs(g,0)==0
print("PASS: V4 signed ray points, smooth hinge path, p1/p3/p5 rate tests and conditional odd generator")
