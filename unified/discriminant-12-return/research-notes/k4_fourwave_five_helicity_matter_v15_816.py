#!/usr/bin/env python3
"""v15.816: positive-energy on-shell canonical scalar with five
nonzero stress helicities at a common spatial Fourier wavevector.
Not a complete metric/detector response; plane-wave witness.
"""
import sympy as s
p=s.Matrix([2,0,0]);q=s.Matrix([0,0,1])
r=s.Matrix([1,1,0]);v=s.Matrix([1,-1,1])
K=s.Matrix([2,0,1])
assert p+q==K and r+v==K
n=K/s.sqrt(5);e=s.Matrix([1,0,-2])/s.sqrt(5);b=s.Matrix([0,1,0])
assert all(s.simplify(z)==0 for z in [n.dot(e),n.dot(b),e.dot(b)])
cross=lambda x,y:x*y.T+y*x.T
# χ=cos(p.x)+cos(q.x)+sqrt2 cos(r.x)+sqrt2 cos(v.x)
# each positive exp plane-wave coefficient is 1/2; sqrt2 products give 2.
S=cross(p,q)+2*cross(r,v)
assert S==s.Matrix([[4,0,4],[0,-4,2],[4,2,0]])
pol=[s.simplify((n.T*S*n)[0]-s.trace(S)/3),
     s.simplify((n.T*S*e)[0]),s.simplify((n.T*S*b)[0]),
     s.simplify(((e.T*S*e)[0]-(b.T*S*b)[0])/2),
     s.simplify((e.T*S*b)[0])]
assert pol==[s.Rational(32,5),-s.Rational(4,5),
             2/s.sqrt(5),s.Rational(4,5),-4/s.sqrt(5)]
assert all(z!=0 for z in pol)
# Fourier stress T_ij orth in coasting a^2=1/3 is -3/4 S at τ=1.
assert [s.simplify(-3*z/4) for z in pol]==[
    -s.Rational(24,5),s.Rational(3,5),-3*s.sqrt(5)/10,
    -s.Rational(3,5),3*s.sqrt(5)/5]
t=s.symbols("tau",positive=True,real=True)
for vec in (p,q,r,v):
    q2=(vec.T*vec)[0]
    a=s.cos(s.sqrt(3*q2-1)*s.log(t))/t
    assert s.simplify(s.diff(a,t,2)+3*s.diff(a,t)/t+3*q2*a/t**2)==0
    assert a.subs(t,1)==1 and s.diff(a,t).subs(t,1)==-1
x0,x1,x2,x3=s.symbols("x0 x1 x2 x3",real=True)
rho=(x0*x0+3*(x1*x1+x2*x2+x3*x3)/t**2)/2
assert s.simplify(rho.subs({x0:1,x1:0,x2:0,x3:0})-s.Rational(1,2))==0
print("PASS: real on-shell canonical scalar waves; nonnegative local energy")
print("PASS: 5 nonzero same-K stress helicities",pol)
print("CAUTION: plane-wave witness, not localized matter or detector observable")
