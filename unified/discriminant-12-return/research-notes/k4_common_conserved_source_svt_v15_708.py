#!/usr/bin/env python3
"""v15.708: a common conserved Fourier stress and SO(2) SVT source projectors.

Purely kinematic construction: not the coupled K4 source/metric transfer.
Spatial S_ij=n_i n_j with n a unit vector; the traceless part Q=S-I/3
is decomposed into orthogonal TT, vector and scalar stress projections
with the Fourier wavevector along z. e^(-i omega t+i k z) conservation
requires T^(0j)=(k/omega)T^(zj), T^(00)=(k/omega)^2 T^(zz).
"""
import sympy as s
x,y,z=s.symbols("x y z",real=True)
S=s.Matrix([[x*x,x*y,x*z],[x*y,y*y,y*z],[x*z,y*z,z*z]])
Q=S-s.eye(3)*(x*x+y*y+z*z)/3
D=(x*x-y*y)/2
TT=s.Matrix([[D,x*y,0],[x*y,-D,0],[0,0,0]])
V=s.Matrix([[0,0,x*z],[0,0,y*z],[x*z,y*z,0]])
Scalar=s.simplify(Q-TT-V)
assert Scalar==s.diag((x*x+y*y-2*z*z)/6,
                      (x*x+y*y-2*z*z)/6,
                      (2*z*z-x*x-y*y)/3)
assert (Q-TT-V-Scalar).applyfunc(s.simplify)==s.zeros(3)
inner=lambda X,Y:s.trace(X*Y)
for A,B in ((TT,V),(TT,Scalar),(V,Scalar)):
    assert s.simplify(inner(A,B))==0
nt=s.factor(inner(TT,TT))
nv=s.factor(inner(V,V))
ns=s.factor(inner(Scalar,Scalar))
assert s.simplify(nt-(x*x+y*y)**2/2)==0
assert s.simplify(nv-2*z*z*(x*x+y*y))==0
assert s.simplify(ns-(x*x+y*y-2*z*z)**2/6)==0
assert s.simplify((nt+nv+ns).subs(x*x+y*y,1-z*z)-s.Rational(2,3))==0
k,om=s.symbols("k omega",real=True,nonzero=True)
T=s.zeros(4)
for i in range(3):
    for j in range(3):
        T[i+1,j+1]=S[i,j]
for j in range(3):
    T[0,j+1]=T[j+1,0]=s.simplify(k/om*T[3,j+1])
T[0,0]=s.simplify((k/om)**2*T[3,3])
for nu in range(4):
    assert s.simplify(-om*T[0,nu]+k*T[3,nu])==0
cases=[
  ({x:1,y:0,z:0},"V"),
  ({x:0,y:0,z:1},"TV"),
  ({x:s.sqrt(s.Rational(2,3)),y:0,z:s.sqrt(s.Rational(1,3))},"S")]
for vals,zero in cases:
    a,b,c=[s.simplify(v.subs(vals)) for v in (nt,nv,ns)]
    if zero=="V":assert b==0 and a!=0 and c!=0
    if zero=="TV":assert a==b==0 and c!=0
    if zero=="S":assert c==0 and a!=0 and b!=0
print("PASS: orthogonal TT/V/S stress projectors, total 2/3, conserved Fourier source")
print("TT, V, S norms:",nt,nv,ns)
