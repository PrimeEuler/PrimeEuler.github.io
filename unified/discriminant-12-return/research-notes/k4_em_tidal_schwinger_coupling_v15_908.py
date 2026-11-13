#!/usr/bin/env python3
"""Gravity v15.908: conventional magnetic and tidal two-mode Schwinger controls.
Cone pair (n,k) maps to oscillator state |n-1,k>.
The coordinate q1,q2 for physical detector modes is NOT Cone X,Y.
Neither field magnitude nor a new Cone-specific gravitational response is derived.
"""
import sympy as s
n,k,M,hbar,omega,B,q,Txy=s.symbols("n k M hbar omega B q Txy",positive=True)
forward=s.sqrt(n*k)
back=s.sqrt((n-1)*(k+1))
assert s.simplify((forward/back)**2-n*k/((n-1)*(k+1)))==0
# Vcross = M*Txy*q1*q2; q_i=l*(a_i+a_i†), l²=hbar/(2*M*omega).
# RWA: Vcross-> hbar*Txy/(2*omega)*(J_++J_-)=hbar*(Txy/omega)*J_x.
hcross=hbar*Txy/(2*omega)
assert s.simplify(2*hcross/hbar-Txy/omega)==0
# Magnetism: Lz=2*hbar*J_y, H_B=-q*B*Lz/(2*M)=-hbar*(q*B/M)*J_y.
for D in range(2,11):
    jp=s.zeros(D)
    for a in range(D-1):
        b=D-1-a
        jp[a+1,a]=s.sqrt((a+1)*b)
    jm=jp.T
    jx=(jp+jm)/2
    jy=(jp-jm)/(2*s.I)
    jz=s.diag(*[s.Rational(2*a-(D-1),2) for a in range(D)])
    assert s.simplify(jx*jx+jy*jy+jz*jz-s.Rational(D*D-1,4)*s.eye(D))==s.zeros(D)
    assert s.simplify(jx*jy-jy*jx-s.I*jz)==s.zeros(D)
    for a in range(D-1):
        assert s.simplify(jx[a+1,a]*s.conjugate(jx[a+1,a])-jy[a+1,a]*s.conjugate(jy[a+1,a]))==0
    if D==5:
        a=3 # pair (4,1): Fock |3,1>.
        assert jx[a+1,a]==1
        assert jx[a-1,a]==s.sqrt(6)/2
        assert jy[a+1,a]==-s.I
        assert jy[a-1,a]==s.I*s.sqrt(6)/2
        assert s.simplify((jx[a+1,a]/jx[a-1,a])**2-s.Rational(2,3))==0
print("PASS: magnetic Jy and tidal Jx identical squared transition ratios, D=2..10")
print("PASS: (4,1) squared right/left ratio = 2/3")
print("Couplings external: g_B=q*B/M, g_tidal=Txy/omega; no Cone clock or novel G-free ratio selected")
