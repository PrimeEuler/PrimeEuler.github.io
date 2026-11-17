#!/usr/bin/env python3
"""Gravity v15.1121 — 3D cone/plane and displaced-null-cone intersections.

General AM-GM cone: T²=X²+Y² (upper sheet T>=0), T+aX+bY=C.
Its cut is ellipse/parabola/hyperbola by s=sqrt(a²+b²) versus 1.
Two congruent null cones: (T,X,Y)=(0,0,0) and (t0,l,0).
Their difference is a plane. For timelike apex separation, the
intersection of first future with second past cone is a Lorentz-boosted
rest-frame action-CIRCLE-shaped spatial circle. There is no physical
action quantization or Compton radius here: R=tau/2 is geometric.
"""
import sympy as s
T,X,Y,t0,l,tau,v,chi=s.symbols("T X Y t0 l tau v chi",real=True)
F0=T*T-X*X-Y*Y
F1=(T-t0)**2-(X-l)**2-Y*Y
assert s.expand(F1-F0)==-2*t0*T+2*l*X+t0*t0-l*l
g=1/s.sqrt(1-v*v)
Tb=g*tau*(1+v*s.cos(chi))/2
Xb=g*tau*(v+s.cos(chi))/2
Yb=tau*s.sin(chi)/2
assert s.trigsimp(F0.subs({T:Tb,X:Xb,Y:Yb}))==0
assert s.trigsimp(F1.subs({T:Tb,X:Xb,Y:Yb,t0:g*tau,l:g*v*tau}))==0
assert s.simplify(Tb-v*Xb-tau/(2*g))==0
center_x=g*v*tau/2
major=g*tau/2
minor=tau/2
assert s.simplify(major**2-minor**2-center_x**2)==0
# The interval tau²=t0²-l², the projection axes are
# major=t0/2, minor=tau/2 and projected eccentricity=abs(l/t0).
# Center of ellipse is spacetime midpoint (t0/2,l/2).
u=s.symbols('u',real=True)
tanu,segu=s.tanh(u),s.sech(u)
assert s.simplify(tanu*tanu+segu*segu-1)==0
Tu=g*tau*(1+v*tanu)/2
Xu=g*tau*(v+tanu)/2
Yu=tau*segu/2
assert s.simplify(F0.subs({T:Tu,X:Xu,Y:Yu}))==0
assert s.simplify(Tu-v*Xu-tau/(2*g))==0
# Boost v is a constant relating two apex rest frames; u is an
# angular coordinate of each point ON the rest-frame circle,
# not automatically its physical time or an additional common boost.
a,b,C,ang=s.symbols('a b C ang',real=True)
r=C/(1+a*s.cos(ang)+b*s.sin(ang))
assert s.trigsimp(r*(1+a*s.cos(ang)+b*s.sin(ang))-C)==0
# Example of 3 null cones with intersection exactly two points.
FB=(T-4)**2-X*X-Y*Y
FC=(T-4)**2-(X-1)**2-Y*Y
for sign in (-1,1):
    point={T:s.Integer(2),X:s.Rational(1,2),Y:sign*s.sqrt(15)/2}
    assert s.simplify(F0.subs(point))==0
    assert s.simplify(FB.subs(point))==0
    assert s.simplify(FC.subs(point))==0
assert s.simplify((FB-F0).subs(T,2))==0
assert s.simplify((FC-F0).subs({T:2,X:s.Rational(1,2)}))==0
# Spacelike apex displacement (t0=0): X=l/2 and remaining
# curve T²-Y²=l²/4, which is a hyperbola in the vertical plane.
assert s.simplify(F0.subs(X,l/2)-(T*T-Y*Y-l*l/4))==0
# Null-separated apices t0=l: the plane is T=X; on the
# cone this forces Y=0: a shared generator, NOT a parabola.
FN=(T-l)**2-(X-l)**2-Y*Y
assert s.simplify((FN-F0)/(2*l)-(X-T))==0
assert s.simplify(F0.subs({T:X,Y:0}))==0
print("PASS: boosted future/past-null-cone ellipse, rapidity/sech and focal offset")
print("PASS: two-plane classification and explicit three-null-cone two-point cut")
print("PASS: spacelike hyperbola and null-generator degeneracy")
print("R_rest = tau/2; A_lab = gamma*tau/2; B_lab = tau/2; projected e = abs(v)")
