#!/usr/bin/env python3
"""Gravity v15.1155 — a source-free magnetostatic 3D Ramsey readout for all
five bicone mechanical tidal planes from Gravity v15.1152–1154.

For ANY orthonormal oriented triad (u,v,w=u×v), magnetic field
B(r)=B0*w+G*((w.r)*v+(v.r)*w) is divergence/curl free in sensor volume.
Spins at +/-d*p(theta)/2 in plane (u,v), with p=cos(theta)u+
sin(theta)v, see DeltaOmega=gamma*G*d*sin(theta). At theta=0,
dDeltaOmega/dtheta=gamma*G*d and tidal torque/DeltaQ=-u.T E v.
A separately applied Ramsey phase bias is needed for first-order Jxy
readout and neither coil nor frequency is predicted by Cone geometry.
"""
import sympy as s
from itertools import product
x,y,z,B0,G,d,gamma,th,DQ=s.symbols("x y z B0 G d gamma theta DeltaQ",real=True)
position=s.Matrix([x,y,z])
# Use arbitrary 3D oriented u,v,w triad, with spin quantization field w.
n=s.Matrix([2/s.sqrt(5),0,1/s.sqrt(5)])
e=s.Matrix([1/s.sqrt(5),0,-2/s.sqrt(5)])
b=s.Matrix([0,1,0])
planes=[(n,e),(n,b),(e,b),((e+b)/s.sqrt(2),(e-b)/s.sqrt(2)),((n+e)/s.sqrt(2),(n-e)/s.sqrt(2))]
S,Ve,Vb,Tp,Tx=s.symbols("S Ve Vb Tp Tx",real=True)
E=S*(n*n.T-s.eye(3)/3)+Ve*(n*e.T+e*n.T)+Vb*(n*b.T+b*n.T)+Tp*(e*e.T-b*b.T)+Tx*(e*b.T+b*e.T)
read=[]
for u,v in planes:
    w=s.simplify(u.cross(v))
    assert s.simplify(u.dot(u)-1)==0 and s.simplify(v.dot(v)-1)==0 and s.simplify(u.dot(v))==0
    assert s.simplify(w.dot(w)-1)==0
    Bfield=s.simplify(B0*w+G*(w.dot(position)*v+v.dot(position)*w))
    assert s.simplify(sum(s.diff(Bfield[i],position[i]) for i in range(3)))==0
    curl=s.Matrix([s.diff(Bfield[2],y)-s.diff(Bfield[1],z),
                   s.diff(Bfield[0],z)-s.diff(Bfield[2],x),
                   s.diff(Bfield[1],x)-s.diff(Bfield[0],y)])
    assert s.simplify(curl)==s.zeros(3,1)
    p=s.cos(th)*u+s.sin(th)*v
    def b_at(sign):
        coords={position[j]:sign*d*p[j]/2 for j in range(3)}
        return s.simplify(Bfield.subs(coords,simultaneous=True))
    DeltaOmega=s.trigsimp(gamma*w.dot(b_at(1)-b_at(-1)))
    assert s.trigsimp(DeltaOmega-gamma*G*d*s.sin(th))==0
    assert s.simplify(s.diff(DeltaOmega,th).subs(th,0)-gamma*G*d)==0
    U=s.trigsimp(DQ*(p.T*E*p)[0]/2)
    torque=s.trigsimp(-s.diff(U,th)/DQ).subs(th,0)
    assert s.simplify(torque+(u.T*E*v)[0])==0
    read.append(s.simplify(torque))
h=s.Matrix([S,Ve,Vb,Tp,Tx])
M=s.Matrix([[s.simplify(s.diff(q,k)) for k in h] for q in read])
expected=s.Matrix([[0,-1,0,0,0],[0,0,-1,0,0],[0,0,0,0,-1],[0,0,0,-1,0],[-s.Rational(1,2),0,0,s.Rational(1,2),0]])
assert s.simplify(M-expected)==s.zeros(5)
assert M.det()==s.Rational(1,2)
print("PASS 5 independent 3D source-free Maxwell gradients, all gain gamma*G*d")
print("PASS 5 oriented tidal torque channels, det",M.det())
print("Spin channel: delta Cxy=2*sin(phi_bias)*gamma*G*d*W_R*chi_theta*DeltaQ*s_i")
print("LIMIT: independent 3D calibrated coil mounts, common support and noise controls")
