#!/usr/bin/env python3
"""Gravity v15.1060: circle/Milne/Penrose coordinate bridge and causal hinge test."""
import sympy as s
rho,eta,theta,ell,U,V,r,t=s.symbols('rho eta theta ell U V r t',positive=True,real=True)
u=rho*s.exp(eta)
v=rho*s.exp(-eta)
T=(u+v)/2; X=(u-v)/2
assert s.simplify(T*T-X*X-rho**2)==0
assert s.simplify(s.diff(u,rho)*s.diff(v,rho)-1)==0
assert s.simplify(s.diff(u,rho)*s.diff(v,eta)+s.diff(u,eta)*s.diff(v,rho))==0
assert s.simplify(s.diff(u,eta)*s.diff(v,eta)+rho**2)==0
uc=rho/s.tan(theta/2)
vc=rho*s.tan(theta/2)
assert s.simplify(s.trigsimp(s.diff(uc,rho)*s.diff(vc,rho)-1))==0
assert s.simplify(s.trigsimp(s.diff(uc,rho)*s.diff(vc,theta)+s.diff(uc,theta)*s.diff(vc,rho)))==0
assert s.simplify(s.trigsimp(s.diff(uc,theta)*s.diff(vc,theta)+rho**2/s.sin(theta)**2))==0
om=s.cos(U)*s.cos(V)/ell
assert s.simplify(om**2*s.diff(ell*s.tan(U),U)*s.diff(ell*s.tan(V),V)-1)==0
A=s.symbols('A',positive=True)
x=A*(u-v)/(u+v)
assert s.simplify(s.diff(x,rho))==0
for p in (1,3,5,7):
    vp=-(2*t-1)**p
    Tp=(r+vp)/2; Xp=(r-vp)/2
    assert s.simplify(s.diff(Tp,t)**2-s.diff(Xp,t)**2)==0
    assert s.simplify(s.diff(Tp,t)-s.diff(vp,t)/2)==0
    assert vp.subs(t,0)==1 and vp.subs(t,s.Rational(1,2))==0 and vp.subs(t,1)==-1
    assert s.diff(Tp,t).subs(t,s.Rational(1,4))<0
    assert s.diff(Tp,t).subs(t,s.Rational(3,4))<0
print('PASS: Milne/angular metric, Penrose conformal factor, radial information loss, past-null hinge p=1,3,5,7')
