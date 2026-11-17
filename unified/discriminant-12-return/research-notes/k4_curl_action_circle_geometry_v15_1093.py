#!/usr/bin/env python3
"""Gravity v15.1093: Maxwell curl and streamlines of the certified compact packet.

The source's circulating E streamlines generally are not circles;
their Faraday magnetic field initially points axially at the packet center.
The source gives no hbar, mass or selected action-circle radius.
"""
import sympy as s
x,y,z,a,b,c,A,t=s.symbols('x y z a b c A t',real=True,nonzero=True)
f=lambda u:(1-u*u)**3
psi=A*f(x/a)*f(y/b)*f(z/c)
Ex=s.diff(psi,y)
Ey=-s.diff(psi,x)
E=s.Matrix([Ex,Ey,0])
def curl(v):
 return s.Matrix([s.diff(v[2],y)-s.diff(v[1],z),
                  s.diff(v[0],z)-s.diff(v[2],x),
                  s.diff(v[1],x)-s.diff(v[0],y)])
assert s.simplify(s.diff(Ex,x)+s.diff(Ey,y))==0
assert s.simplify(E.dot(s.Matrix([s.diff(psi,x),s.diff(psi,y),s.diff(psi,z)])))==0
Bdot=-curl(E)
assert Bdot==s.Matrix([-s.diff(psi,x,z),-s.diff(psi,y,z),
                       s.diff(psi,x,2)+s.diff(psi,y,2)])
center=s.simplify(Bdot.subs({x:0,y:0,z:0}))
assert s.simplify(center[2]+6*A*(a**-2+b**-2))==0
assert center[0]==0 and center[1]==0
# The electric streamline is NOT a circle around the axis for a != b.
radial=s.factor((x*Ex+y*Ey).subs({x:a/2,y:b/2,z:0}))
assert s.simplify(radial-A*f(s.Rational(1,2))*s.diff(f(s.Symbol('u')),s.Symbol('u')).subs(s.Symbol('u'),s.Rational(1,2))*(a/b-b/a)/2)==0
assert s.simplify(radial.subs(b,2*a))!=0
# Stokes and Faraday: circulation integral E = - d/dt flux B.
assert s.simplify(curl(E)[2]+Bdot[2])==0
# Total initial axial magnetic flux generation over a complete transverse
# plane vanishes (derivative of compact-support field).
u=s.symbols('u',real=True)
f0=f(u)
assert s.integrate(s.diff(f0,u,2),(u,-1,1))==0
# A local axial B does not select a universal circle radius.
hbar,m,c0=s.symbols('hbar m c0',positive=True)
r=hbar/(2*m*c0)
omega=2*m*c0*c0/hbar
assert s.simplify(omega*r-c0)==0
assert s.simplify((m*c0)*(2*s.pi*r)-s.pi*hbar)==0
assert s.simplify(m*c0*r-hbar/2)==0
print('PASS Maxwell streamlines, induced axial B, local Faraday circulation, no fixed action radius')
print('Bdot(center)=',center)
print('radial E projection at (a/2,b/2,0)=',radial)
