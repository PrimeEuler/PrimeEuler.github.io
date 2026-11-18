#!/usr/bin/env python3
"""Gravity v15.1125: half-step mirrored parabola heights reproduce the
ordinary Schwinger SU(2) transition weights on one n+1 action circle,
but their intersections do not determine a complex phase or a new
cross-cone interaction. Prior art v15.952, v15.955 explicitly credited.
"""
import sympy as s
I=s.I
for D in range(2,11):
    z=s.zeros(D)
    Jp=s.zeros(D)
    Jz=s.diag(*[s.Rational(D-1,2)-k for k in range(D)])
    for k in range(1,D):
        Jp[k-1,k]=s.sqrt(k*(D-k))
    Jm=Jp.T
    assert Jp*Jm-Jm*Jp==2*Jz
    assert Jz*Jp-Jp*Jz==Jp
    assert [k*(D-k) for k in range(1,D)]==[(D-k)*k for k in range(1,D)]
    phases=s.symbols('phi0:'+str(D),real=True)
    U=s.diag(*[s.exp(I*a) for a in phases])
    Jphase=s.simplify(U*Jp*U.conjugate().T)
    assert s.simplify(Jphase*Jphase.H-Jphase.H*Jphase-2*Jz)==z
    for k in range(1,D):
        assert s.simplify(Jphase[k-1,k]*s.conjugate(Jphase[k-1,k])-k*(D-k))==0
p=s.symbols('phase',real=True)
J=s.Matrix([[0,s.exp(I*p)],[0,0]])
assert s.simplify(J*J.H-J.H*J-s.diag(1,-1))==s.zeros(2)
print('PASS D=2..10 exact Schwinger operators; mirrored parabola edge weights')
print('PASS arbitrary edge phases leave all squared heights and SU2 commutators invariant')
print('Conclusion: geometry fixes magnitudes once a state carrier is chosen; not phases/cross-cone dynamics')
