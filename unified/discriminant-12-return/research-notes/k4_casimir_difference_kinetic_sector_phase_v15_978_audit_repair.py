#!/usr/bin/env python3
"""Cone Gravity v15.969: what a Casimir *difference* can mean as kinetic
energy. At matched physical D, formal quarter q2 and ordinary SU2 C
labels differ. Only a specified kinetic Hamiltonian makes this an
energy splitting. A sector-only splitting induces relative phase but
not population transport; a transverse quadratic produces known
Jz^2 state-dependent phases, not a novel gravity interaction.
"""
import sympy as s
D=s.symbols('D',integer=True,positive=True)
j=s.Rational(1,2)*(D-1)
jq=s.Rational(1,4)*(2*D-1)
Ce=s.factor(j*(j+1))
Cq=s.factor(jq*(jq+1))
assert s.simplify(s.factor(Cq-Ce)-(4*D+1)/16)==0
assert s.simplify(Cq-
       (j*(j+1)+(j+s.Rational(1,2))*(j+s.Rational(3,2)))/2
       +s.Rational(1,16))==0
hbar,Ie,Ig=s.symbols('hbar I_e I_g',positive=True)
de=s.factor(hbar**2*(Cq/Ig-Ce/Ie)/2)
assert s.simplify(de.subs(Ig,Ie)-
                  hbar**2*(4*D+1)/(32*Ie))==0
# DO NOT claim diagonal q2 formal states are equivalent: doubled space
# below is expressly an arbitrary same-dimensional auxiliary copy.
for d in range(2,11):
    jj=s.Rational(d-1,2)
    Jp=s.zeros(d)
    for k in range(1,d):
        Jp[k-1,k]=s.sqrt(k*(d-k))
    Jm=Jp.T
    Jz=s.diag(*[jj-k for k in range(d)])
    Jx=(Jp+Jm)/2
    Jy=(Jp-Jm)/(2*s.I)
    Q=s.simplify(Jx*Jx+Jy*Jy)
    assert s.simplify(Q-(jj*(jj+1)*s.eye(d)-Jz*Jz))==s.zeros(d)
    assert s.simplify(Q*Jp-Jp*Q+Jp*(2*Jz+s.eye(d)))==s.zeros(d)
    Cem=s.Rational(d*d-1,4)
    Cqm=s.Rational((2*d-1)*(2*d+3),16)
    assert Cqm-Cem==s.Rational(4*d+1,16)
    H=s.diag(*([Cem]*d+[Cqm]*d))
    Z=s.diag(*([1]*d+[-1]*d))
    X=s.BlockMatrix([[s.zeros(d),s.eye(d)],
                     [s.eye(d),s.zeros(d)]]).as_explicit()
    assert H*Z-Z*H==s.zeros(2*d)
    assert s.simplify(H*X-X*H-(Cem-Cqm)*Z*X)==s.zeros(2*d)
    assert H[:d,:d]==Cem*s.eye(d)
    assert H[d:,d:]==Cqm*s.eye(d)
    if d in (2,3,5):
        print('D',d,'C_EM',Cem,'C_quarter_formal',Cqm,
              'DeltaC',Cqm-Cem,
              'Q diagonal',list(Q.diagonal()))
print('PASS: shared-D formal Casimir gap, conditional kinetic factor,')
print('sector-only relative phase without population flow,')
print('ordinary transverse Jz^2 anisotropy D=2..10')
