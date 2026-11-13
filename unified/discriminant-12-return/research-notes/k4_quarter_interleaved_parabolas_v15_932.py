#!/usr/bin/env python3
"""Gravity v15.932: quarter-factor rows interleave the half-vertex EM
parabolas, but quarter nodes are not ordinary EM SU(2) states.
Exact midpoint surplus 1/4 in squared GM heights, distinct from
the separately existing quarter Casimir 1/4 depth; parity-odd
observable needs inter-sector coherence.
"""
import sympy as s
D,k,t=s.symbols('D k t',positive=True)
f=lambda b: s.expand(b*(D-b))
half=s.Rational(1,2)
assert s.simplify(f(k+half)-(f(k)+f(k+1))/2)==s.Rational(1,4)
assert s.simplify((-(k+half)/2)-(((-k/2)+(-(k+1)/2))/2))==0
assert s.simplify(((D/2)-(k+half))-(((D/2-k)+(D/2-k-1))/2))==0
assert s.simplify((f(k+half)-(f(k)+f(k+1))/2)/t**2)==s.Rational(1,4)/t**2
for L in range(1,65):
    j=s.Rational(L,4); diameter=2*j+1
    assert diameter==s.Rational(L+2,2)
    assert s.simplify((j+half)**2-j*(j+1))==s.Rational(1,4)
    for i in range(L+1):
        a=s.Rational(L-i,2);b=s.Rational(i+2,2)
        P=a*b; X=(b-a)/2
        assert s.simplify(X**2+P-(diameter/2)**2)==0
        if L%2==0:
            if i%2==0:assert (a.q,b.q)==(1,1)
            else:assert (a.q,b.q)==(2,2)
        else:
            assert (a.q,b.q) in [(1,2),(2,1)]
# Abstract sector parity and off-diagonal probe: intersector coherence required.
chi=s.diag(1,-1)
U=s.Matrix([[0,1],[1,0]])
assert chi*U+U*chi==s.zeros(2)
assert (s.Matrix([1,0]).T*U*s.Matrix([1,0]))[0]==0
assert (s.Matrix([0,1]).T*U*s.Matrix([0,1]))[0]==0
phi=s.symbols('phi',real=True)
psi=s.Matrix([1,s.exp(s.I*phi)])/s.sqrt(2)
assert s.simplify((s.conjugate(psi).T*U*psi)[0]-s.cos(phi))==0
print('PASS: 64 quarter-grid shells, vertex/circle midpoints, +1/4 squared height,')
print('even/odd shell parity of factor cosets, separate Casimir depth, coherence witness')
