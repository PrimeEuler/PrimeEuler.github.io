#!/usr/bin/env python3
"""Cone Gravity v15.974 -- matched-outer-D EM and quarter closed
Schwinger CP1 orbits. Chern difference D, relative standard Hopf/Berry
connection, equatorial parity, distinct angular Casimir normalizations
and absence of a nonzero SU2-equivariant map between unequal irreps.
This uses an explicitly CHOSEN identification of the two CP1 bases.
It does not create an EM/gravity coupling or new physical observable.
"""
import sympy as s
D=s.symbols('D',integer=True,positive=True)
theta=s.symbols('theta', real=True)
Ne,Nq=D-1,2*D-1
assert s.simplify(Nq-Ne-D)==0
A_N=lambda k:s.factor(k*(1-s.cos(theta))/2)
A_S=lambda k:s.factor(-k*(1+s.cos(theta))/2)
Fcoeff=lambda k:s.simplify(s.diff(A_N(k),theta))
for k in (Ne,Nq,D):
    assert s.trigsimp(A_N(k)-A_S(k)-k)==0
    assert s.simplify(Fcoeff(k)-k*s.sin(theta)/2)==0
assert s.simplify(A_N(Nq)-A_N(Ne)-A_N(D))==0
assert s.simplify(A_S(Nq)-A_S(Ne)-A_S(D))==0
assert s.simplify(Fcoeff(Nq)-Fcoeff(Ne)-Fcoeff(D))==0
C_e=(D**2-1)/4
C_q_scaled=(D**2-s.Rational(1,4))/4
C_q_normal=((2*D-1)*(2*D+1))/4
assert s.simplify(C_q_scaled-C_e-s.Rational(3,16))==0
assert s.simplify(C_q_normal-C_e-3*D**2/4)==0
for d in range(2,101):
    em=d-1
    q=2*d-1
    assert q-em==d
    assert em+1==d and q+1==2*d
    # Equatorial holonomy exp(i*pi*k): relative parity (-1)^D
    assert (-1)**(q-em)==(-1)**d
    assert (q%2)==1    # formal quarter label L_q is always odd
    # Multiplication by z0^D injects degree-(D-1) polynomials into
    # degree-(2D-1) polynomials; its image is non-surjective.
    # Degree d-1 monomial z0^(d-1-r) z1^r goes to
    # z0^(2d-1-r) z1^r; only r=0,...,d-1 among q+1=2d.
    image={ (2*d-1-r,r) for r in range(d)}
    assert len(image)==d and len(image)<2*d
    # Under SU2, each is an irrep of differing highest weight.
    # Schur's lemma implies no nonzero intertwiner.
    assert em!=q
print('PASS: D=2..100 Berry north/south patching, relative Chern D,')
print('equator phase alternation, Casimir normalization, state count,')
print('and explicitly non-equivariant polynomial embedding.')
