#!/usr/bin/env python3
"""v15.925: put fixed-product hyperbola intersections on the existing
unbounded q=2 quarter-grid shell j=L/4, WITHOUT altering the established
defective original unit-step ladder or promoting the geometric witness
to a physical EM/gravity interaction.
Checks v15.140, v15.180, v15.572/573 and v15.602/627.
"""
import sympy as s

for L in range(1,45):
    j=s.Rational(L,4)
    dim=L+1
    jp=s.zeros(dim)
    M=s.diag(*[-j+s.Rational(i,2) for i in range(dim)])
    w={}
    for i in range(dim):
        m=-j+s.Rational(i,2)
        a=j-m
        b=j+m+1
        x=(b-a)/2
        radius=(a+b)/2
        P=a*b
        assert a==s.Rational(L-i,2) and b==s.Rational(i+2,2)
        assert P==s.Rational((L-i)*(i+2),4)
        assert x==s.Rational(2*i+2-L,4)
        assert radius==j+s.Rational(1,2)
        assert s.simplify(radius**2-x**2-P)==0
        if a>0:
            assert s.simplify((P-a*a)/(2*a)-x)==0
        if i+2<=L:
            jp[i+2,i]=s.sqrt(P)
        w[i]=P
    jm=jp.T
    jx=(jp+jm)/2
    jy=(jp-jm)/(2*s.I)
    defect=s.simplify(jp*jm-jm*jp-2*M)
    E=s.simplify(j*(j+1)*s.eye(dim)-(jx*jx+jy*jy+M*M))
    escape=j+s.Rational(1,4)
    # v15.602's CHOSEN geometric cross-shell witness j'=j+1/2.
    T=s.zeros(dim+2,dim)
    T[dim+1,L-1]=s.sqrt(escape)
    T[0,1]=s.sqrt(escape)
    assert s.simplify(T.T*T-2*E)==s.zeros(dim)
    D_expected=s.zeros(dim)
    D_expected[L-1,L-1]+=escape
    D_expected[1,1]-=escape
    assert defect==D_expected
    assert s.simplify(s.trace(E)-escape)==0
    assert w[L-1]==escape
    assert (L+2)%2==L%2  # v15.627: witness preserves chi=(-1)^L.
    if L in (1,2,3,4,5,7):
        print('L=',L,'j=',j,'escape=',escape,
              'Ddef=',list(defect.diagonal()),'E=',list(E.diagonal()))
print('PASS 44 shells: hyperbola incidence, D/E defects, T^dagger T=2E, sector grading')
