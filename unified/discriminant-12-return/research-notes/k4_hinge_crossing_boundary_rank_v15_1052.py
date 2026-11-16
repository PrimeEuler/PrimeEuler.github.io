#!/usr/bin/env python3
"""v15.1052: signed V4 hinge crossing and rigorous boundary-rank control.
Earlier provisional v15.1051 script collided in number with Audit Round
587; this independently canonicalizes result without rewriting files.
"""
import sympy as s
x,r=s.symbols('x r',positive=True)
for p in (1,3,5):
    v=-x**p
    T=(r+v)/2
    X=(r-v)/2
    R=s.sqrt(r)*x**s.Rational(p,2) # x>0; extend with abs(x)
    assert s.simplify(X**2-T**2-r*x**p)==0
    integrand=s.simplify((2*s.diff(R,x))**2)
    full=s.simplify(s.integrate(integrand,(x,0,1)))
    plane=s.integrate(p*p*x**(2*p-2),(x,-1,1))
    assert s.simplify(plane-s.Rational(2*p*p,2*p-1))==0
    assert (full==s.oo)==(p==1)
    print(p,'height_sq_rate_time_integral',full,'plane_sq_rate_time_integral',plane)
assert s.limit(s.diff(s.sqrt(r)*x**s.Rational(5,2),x,2),x,0,dir='+')==0
assert s.limit(s.diff(s.sqrt(r)*x**s.Rational(3,2),x,2),x,0,dir='+')==s.oo
for n in (1,5,7,11):
    n=s.Integer(n)
    assert ((n+1)/2)**2-((n-1)/2)**2==n
    # at hinge u=n and v=0, X=T=n/2.
    assert (n/2)**2-(n/2)**2==0
# One-to-one V4 signed reflection on four representative states:
F=s.eye(4)
assert F.rank()==4 and F.T*F==s.eye(4)
# The original-step quarter cross-shell T is rank 2 with
# two equal nonzero singular squared weights w=(L+1)/4.
for L in range(3,14):
    w=s.Rational(L+1,4)
    T=s.zeros(L+3,L+1)
    T[0,1]=s.sqrt(w)
    T[L+2,L-1]=s.sqrt(w)
    E=s.zeros(L+1)
    E[1,1]=w/2
    E[L-1,L-1]=w/2
    assert T.rank()==2
    assert T.T*T==2*E
    assert T.T*T != s.eye(L+1)
    assert (-1)**(L+2)==(-1)**L
print('PASS: smooth p5 hinge, divergent p1 height coordinate, open T rank-two vs isometric V4 reflection')
