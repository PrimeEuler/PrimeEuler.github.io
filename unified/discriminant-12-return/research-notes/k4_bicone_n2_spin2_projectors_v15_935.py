#!/usr/bin/env python3
"""Gravity v15.935: n=2 sqrt(n)/Casimir crossing does not select J=2
in a conditional glued spin-one x spin-one SO(3) representation.
Uses factor-pair n=2, which is hydrogen principal shell n_H=3,
NOT hydrogen n_H=2. All matrices exact SymPy.
"""
import sympy as s
P=s.Matrix([[0,s.sqrt(2),0],[0,0,s.sqrt(2)],[0,0,0]])
Z=s.diag(1,0,-1)
I3=s.eye(3);I=s.eye(9)
Jp=s.kronecker_product(P,I3);Kp=s.kronecker_product(I3,P)
Jm=Jp.T;Km=Kp.T
Jz=s.kronecker_product(Z,I3);Kz=s.kronecker_product(I3,Z)
X=(Jp*Km+Jm*Kp)/2+Jz*Kz
Lp=Jp+Kp;Lm=Jm+Km;Lz=Jz+Kz
L2=Lz**2+(Lp*Lm+Lm*Lp)/2
P0=(X+I)*(X-I)/3
P1=-(X+2*I)*(X-I)/2
P2=(X+2*I)*(X+I)/6
for label,Q,d,eigen in [(0,P0,1,-2),(1,P1,3,-1),(2,P2,5,1)]:
    assert Q*Q==Q and Q.T==Q
    assert s.trace(Q)==d and Q.rank()==d
    assert L2*Q==label*(label+1)*Q
    assert X*Q==eigen*Q
    assert Lp*Q==Q*Lp
    print('J',label,'rank',d,'L2',label*(label+1),'J dot K',eigen)
assert P0+P1+P2==I
Swap=s.zeros(9)
for a in range(3):
    for b in range(3):
        Swap[b*3+a,a*3+b]=1
assert Swap==P0-P1+P2
# Each component SU(2) Casimir is 2. They coincide with R_rest^2=2.
single=Z**2+(P*P.T+P.T*P)/2
assert single==2*I3
Cpair=(s.kronecker_product(single,I3)+s.kronecker_product(I3,single))/2
Rrest2=2*I
Rtrans2=s.Rational(9,4)*I
assert Cpair==Rrest2 and Rtrans2-Cpair==I/4
for Q in (P0,P1,P2):
    assert (Cpair-Rrest2)*Q==s.zeros(9)
# Adding an externally chosen g X separates the three sectors, but
# the common circle geometry cannot select the sign/value of g.
g=s.symbols('g',real=True)
for label,Q,eigen in [(0,P0,-2),(1,P1,-1),(2,P2,1)]:
    assert (g*X)*Q==g*eigen*Q
print('PASS projectors, exchange, all-sector crossing, conditional exchange splitting')
