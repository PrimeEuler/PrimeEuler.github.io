#!/usr/bin/env python3
"""v15.938: q=2 odd-quarter position-quadrupole attempt.
Original step-one defective J, NOT closed refined SU2. Exact SymPy.
This is a necessary rank-two covariance test, NOT physical gravity.
"""
import sympy as s

def matrices(L):
    j=s.Rational(L,4)
    M=s.diag(*[-j+s.Rational(i,2) for i in range(L+1)])
    J=s.zeros(L+1)
    for i in range(L-1):
        J[i+2,i]=s.sqrt(s.Rational((L-i)*(i+2),4))
    B=J.T
    C=s.simplify(M*M+(J*B+B*J)/2)
    Cg=j*(j+1)*s.eye(L+1)
    E=s.simplify(Cg-C)
    Q=s.simplify(3*M*M-C)
    F=s.simplify(3*M*M-Cg)
    return M,J,B,C,Cg,E,Q,F

for L in range(1,32,2):
    M,J,B,C,Cg,E,Q,F=matrices(L)
    j=s.Rational(L,4)
    assert E==Q-F
    assert s.trace(E)==j+s.Rational(1,4)
    if L>=3:
        assert E.rank()==2
        assert (C*J-J*C).rank()==2
        assert sorted(C.eigenvals())==sorted([j*(j+1),j*(j+1)-(j+s.Rational(1,4))/2])
    else:
        assert E.rank()==2 and C*J==J*C
    triple=Q
    for _ in range(3):
        triple=s.simplify(J*triple-triple*J)
    # Necessary for a conventional rank-two spherical tensor q=0:
    # ad(J+)^3(Q20)=0; the quarter original-step candidate fails.
    assert (triple==s.zeros(L+1))==(L<=5)
    if L>=7:assert triple.rank()==2
    # n_H=3 physical Coulomb bicone has 9 states, never L+1 odd L.
    assert (L+1)%2==0 and L+1!=9
    if L in (1,3,5,7,15,31):
        print('L',L,'formal C',j*(j+1),'C_def spectrum',C.eigenvals(),
              'rank ad+^3(Q)',triple.rank(),'trace E',s.trace(E))
print('PASS: 16 odd quarter shells; C defect and rank-two covariance failure; dimension obstruction')
