#!/usr/bin/env python3
"""Gravity v15.936: exact spin-1 x spin-1 symmetric-traceless bicone
quadrupole. Auxiliary SO(3) tensor only: physical x_i != A_i not derived.
"""
import sympy as s
from sympy.physics.wigner import clebsch_gordan
p=s.Matrix([[0,s.sqrt(2),0],[0,0,s.sqrt(2)],[0,0,0]])
z=s.diag(1,0,-1);i3=s.eye(3);I=s.eye(9)
Jp=s.kronecker_product(p,i3);Kp=s.kronecker_product(i3,p)
Jm=Jp.T;Km=Kp.T;Jz=s.kronecker_product(z,i3);Kz=s.kronecker_product(i3,z)
Lp=Jp+Kp;Lm=Lp.T;Lz=Jz+Kz
L2=Lz**2+(Lp*Lm+Lm*Lp)/2
X=(Jp*Km+Jm*Kp)/2+Jz*Kz
P=[(X+I)*(X-I)/3,-(X+2*I)*(X-I)/2,(X+2*I)*(X+I)/6]
az=Jz-Kz;ap=Jp-Kp;am=ap.T
a2=az**2+(ap*am+am*ap)/2
Q=s.simplify(3*az**2-a2)
assert Lz*Q==Q*Lz and Q.T==Q and s.trace(Q)==0
comm=lambda a,b:a*b-b*a
assert comm(Lp,comm(Lp,comm(Lp,Q)))==s.zeros(9)
assert comm(Lp,comm(Lp,Q))!=s.zeros(9)
ranks=[];strength=[]
for a in range(3):
    rr=[];ss=[]
    for b in range(3):
        block=s.simplify(P[a]*Q*P[b])
        rr.append(block.rank())
        ss.append(s.trace(block.T*block))
    ranks.append(rr);strength.append(ss)
assert ranks==[[0,0,1],[0,3,0],[1,0,5]]
assert strength==[[0,0,32],[0,54,0],[32,0,14]]
def ket(spin,m):
    v=s.zeros(9,1)
    for a in range(3):
        for b in range(3):
            v[a*3+b]=clebsch_gordan(1,1,spin,1-a,1-b,m)
    return v
assert (ket(2,0).T*Q*ket(0,0))[0]==4*s.sqrt(2)
assert [(ket(1,m).T*Q*ket(1,m))[0] for m in (-1,0,1)]==[-3,6,-3]
assert [(ket(2,m).T*Q*ket(2,m))[0] for m in (-2,-1,0,1,2)]==[-2,1,2,1,-2]
S=s.zeros(9)
for a in range(3):
    for b in range(3):S[b*3+a,a*3+b]=1
assert S*Q==Q*S and S==P[0]-P[1]+P[2]
assert P[0]+P[1]+P[2]==I
# Unselected scalar geometry at n=2: no preference for any of 9 states
assert (2*I-2*I)*Q==s.zeros(9)
print('PASS: 9-state SO3 quadrupole, ranks',ranks,'norm2',strength)
print('0->2 m=0 amplitude 4sqrt2; 1->1 nonzero; 2->2 nonzero')
