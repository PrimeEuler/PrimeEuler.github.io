#!/usr/bin/env python3
"""Gravity v15.926: exact product transport in the audited q=2 quarter staircase.

Distinguishes transition-centered product P=(j-m)(j+m+1) from literal
state coordinates, upward/downward oriented edges, the established
L->L+2 boundary witness, and two CHOSEN L->L+1 null shifts.
No Hamiltonian or physical EM/gravity interaction inferred.
"""
import sympy as s

half=s.Rational(1,2)
quarter=s.Rational(1,4)
for L in range(1,81):
    j=s.Rational(L,4)
    c=j+quarter
    for i in range(L+1):
        m=-j+half*i
        a=j-m
        b=j+m+1
        P=a*b
        R=(a+b)/2
        X=(b-a)/2
        assert s.simplify(R*R-X*X-P)==0
        assert a==s.Rational(L-i,2)
        assert b==s.Rational(i+2,2)
        # Two canonical index injections into L'=L+1:
        # i'=i: m'=m-1/4, so a'=a+1/2,b'=b.
        # i'=i+1: m'=m+1/4, so a'=a,b'=b+1/2.
        for i_new, anew,bnew,deltaP,deltaX in [
            (i,a+half,b,b/2,-quarter),
            (i+1,a,b+half,a/2,quarter),
        ]:
            jnew=s.Rational(L+1,4)
            mnew=-jnew+half*i_new
            assert anew==jnew-mnew
            assert bnew==jnew+mnew+1
            assert s.simplify(anew*bnew-P-deltaP)==0
            assert s.simplify((anew+bnew)/2-R-quarter)==0
            assert s.simplify((bnew-anew)/2-X-deltaX)==0
            assert s.simplify((quarter)**2-deltaX**2)==0
            assert (L+1)%2!=L%2
            assert deltaP>=0 # a=0 at the top endpoint makes the b-increment's product change zero
        # deltaP can vanish when a=0 at the exact top endpoint:
        assert a>=0 and b>0
    # Both directed open-boundary sources exist for all L>=1:
    i_upper=L-1
    i_lower=1
    au=s.Rational(L-i_upper,2)
    bu=s.Rational(i_upper+2,2)
    al=s.Rational(L-i_lower,2)
    bl=s.Rational(i_lower+2,2)
    assert au*bu==c
    assert al*bl==c
    # Original chosen L->L+2 witness reaches j'=j+1/2 extrema:
    jtarget=j+half
    mt_up=jtarget
    mt_down=-jtarget
    # Orientation is vital: UPWARD transition at top and DOWNWARD at bottom.
    Ptarget_up=(jtarget-mt_up)*(jtarget+mt_up+1)
    Ptarget_down=(jtarget+mt_down)*(jtarget-mt_down+1)
    assert Ptarget_up==Ptarget_down==0
    assert Ptarget_up-au*bu==-c
    assert Ptarget_down-al*bl==-c
    assert (L+2)%2==L%2
    # At upward open end two L->L+1 injections: product changes c or 1/4.
    assert bu/2==c
    assert au/2==quarter
    if L in [1,2,3,4,7,11]:
        print(f'L={L:2}, j={j}, P_escape={c}, witness delta P={-c}, null shifts delta P={bu/2},{au/2}')
print('PASS: 80 quarter shells, every node, both null injections and boundary witness, grading')
