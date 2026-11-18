#!/usr/bin/env python3
"""Gravity v15.1152: source-first 5-helicity local bicone tidal tomography.

Wave-adapted orthonormal n,e,b; STF tidal tensor decomposes as
S*(nn-I/3) + Ve*(ne+en) + Vb*(nb+bn)
 + Tplus*(ee-bb)+Tcross*(eb+be).
A bicone rotating in plane (u,v) at angle theta=0 has normalized
torsion torque -u.T*E*v, with E the physical full Riemann tidal tensor.

K4 canonical scalar source benchmark v15.730/787 has K=(2,0,1),
Phi_N=191/1800, Psi_N=-1/72, a²=1/3 at tau=1. NOT a calibrated SI
strain or a new Cone source coupling. Match conventional GR+same solid.
"""
import sympy as s
S,Ve,Vb,Tp,Tx,eiso,DQ,theta=s.symbols("S Ve Vb Tp Tx eiso DQ theta",real=True)
rt=s.sqrt
n=s.Matrix([2/rt(5),0,1/rt(5)])
e=s.Matrix([1/rt(5),0,-2/rt(5)])
b=s.Matrix([0,1,0])
Q=s.Matrix.hstack(n,e,b)
assert s.simplify(Q.T*Q-s.eye(3))==s.zeros(3)
E=eiso*s.eye(3)+S*(n*n.T-s.eye(3)/3)+Ve*(n*e.T+e*n.T)+Vb*(n*b.T+b*n.T)+Tp*(e*e.T-b*b.T)+Tx*(e*b.T+b*e.T)
E_want=s.Matrix([[eiso+2*S/3,Ve,Vb],[Ve,eiso-S/3+Tp,Tx],[Vb,Tx,eiso-S/3-Tp]])
assert s.simplify(Q.T*E*Q-E_want)==s.zeros(3)
planes=[(n,e),(n,b),(e,b),((e+b)/rt(2),(e-b)/rt(2)),((n+e)/rt(2),(n-e)/rt(2))]
helicities=s.Matrix([S,Ve,Vb,Tp,Tx]);read=[]
for u,v in planes:
    assert s.simplify(u.dot(u)-1)==0 and s.simplify(v.dot(v)-1)==0 and s.simplify(u.dot(v))==0
    p=s.cos(theta)*u+s.sin(theta)*v
    U=s.trigsimp(DQ*(p.T*E*p)[0]/2)
    force=s.trigsimp(-s.diff(U,theta)/DQ)
    assert s.simplify(force.subs(theta,0)+(u.T*E*v)[0])==0
    assert s.simplify(s.diff(force,eiso))==0
    read.append(s.simplify(force.subs(theta,0)))
M=s.Matrix([[s.simplify(s.diff(expr,h)) for h in helicities] for expr in read])
expected=s.Matrix([[0,-1,0,0,0],[0,0,-1,0,0],[0,0,0,0,-1],[0,0,0,-1,0],[-s.Rational(1,2),0,0,s.Rational(1,2),0]])
assert s.simplify(M-expected)==s.zeros(5)
assert M.det()==s.Rational(1,2) and M.rank()==5
assert s.simplify(s.Matrix(read)-M*helicities)==s.zeros(5,1)
y1,y2,y3,y4,y5=s.symbols("y1 y2 y3 y4 y5")
assert s.simplify(M.inv()*s.Matrix([y1,y2,y3,y4,y5])-s.Matrix([-y4-2*y5,-y1,-y2,-y4,-y3]))==s.zeros(5,1)
Phi=s.Rational(191,1800);Psi=-s.Rational(1,72);a2=s.Rational(1,3);k2=5
S_full=-k2*Phi/a2
S_weyl=k2*(Phi+Psi)/(2*a2)
assert S_full==-s.Rational(191,120) and S_weyl==s.Rational(83,120)
actual=M*s.Matrix([S_full,0,0,0,0])
wrong=M*s.Matrix([S_weyl,0,0,0,0])
assert actual==s.Matrix([0,0,0,0,s.Rational(191,240)])
assert wrong==s.Matrix([0,0,0,0,-s.Rational(83,240)])
assert actual[4]-wrong[4]==s.Rational(137,120)
for angle in (s.Integer(0),s.pi/9,s.pi/4):
    u=s.cos(angle)*e+s.sin(angle)*b
    v=-s.sin(angle)*e+s.cos(angle)*b
    trans=s.simplify((u.T*E*v)[0])
    for h in (S,Ve,Vb): assert s.simplify(s.diff(trans,h))==0
print("PASS exact five-helicity bicone torque matrix",M,"det",M.det())
print("PASS full versus Weyl-only scalar source",actual.T,wrong.T)
print("SCOPE local Fourier tidal coefficients; no new gravity source, no spin readout assumption")
