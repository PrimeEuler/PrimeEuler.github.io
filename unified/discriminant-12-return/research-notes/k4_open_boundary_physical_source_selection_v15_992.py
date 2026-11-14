#!/usr/bin/env python3
"""v15.992 source selection for original-unit-step q2 open boundary map.
Scope: canonical auxiliary two-mode occupation embedding only.
"""
import sympy as s
for L in range(3,22):
    j=s.Rational(L,4); jp=j+s.Rational(1,2)
    w=s.Rational(L+1,4)
    # Source upper (i=L-1) -> destination upper (i'=L+2) in shell L'=L+2.
    # Physical Schwinger embedding: n1=i,n2=L-i, m_phys=(n1-n2)/2.
    i=L-1; ip=L+2
    src=(i,L-i); dst=(ip,L+2-ip)
    dN=sum(dst)-sum(src)
    dm=s.Rational((dst[0]-dst[1])-(src[0]-src[1]),2)
    assert src==(L-1,1) and dst==(L+2,0)
    assert (dN,dm)==(2,2)
    # A net +2 quadratic operator must be a pair of creators.
    possible=set(s.Rational(a-(2-a),2) for a in range(3))
    assert possible=={-1,0,1} and dm not in possible
    # Quartic (a1^dagger)^3 a2 is permitted, but weights mismatch.
    quartic=s.sqrt(L*(L+1)*(L+2))
    target=s.sqrt(w)
    needed=s.simplify(target/quartic)
    assert s.simplify(needed-1/(2*s.sqrt(L*(L+2))))==0
    assert s.simplify(jp-j-s.Rational(1,2))==0
    assert (L+2)%2==L%2
    if L in (3,4,6,10):
        print("L=",L,"boundary=",target,"quartic=",quartic,"required coefficient=",needed)
print("PASS L=3..21: quadratic no-go; quartic allowance with L-dependent coefficient; parity preservation")
