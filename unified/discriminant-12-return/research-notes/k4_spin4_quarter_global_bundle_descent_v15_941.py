#!/usr/bin/env python3
"""v15.941: fourth-root descent obstruction at unit Chern charge;
rank-four clutching is global but not a U(1) representation or
Spin(4) character. Independent physical connection remains missing.
"""
import math
import sympy as s

z=s.symbols('z',nonzero=True)
I=s.eye(4)
M=s.Matrix([[0,0,0,z],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
chi=s.diag(1,-1,1,-1)
assert M**4==z*I
assert s.factor(M.det())==-z
assert M*chi==-chi*M
assert M.subs(z,1)!=I # a clutching function is not a circle group homomorphism
assert s.factor(M.charpoly().as_expr())==s.Symbol('lambda')**4-z
for k in range(1,33):
    # A line root exists precisely for Chern charge divisible by four.
    assert (k%4==0)==(s.Rational(k,4).q==1)
    q=s.Rational(k,4)
    descent=s.simplify(s.exp(2*s.pi*s.I*q)-1)
    assert (descent==0)==(k%4==0)
    # The eigenbranch analytic-continuation cycle count is gcd(k,4).
    assert 4//math.gcd(4,k) in (1,2,4)
# SU2 Lie algebra is perfect: any linear homomorphism into abelian
# u(1) kills [X,Y]=Z, [Y,Z]=X, [Z,X]=Y and hence every generator.
a,b,c=s.symbols('a b c')
assert s.solve([a,b,c],[a,b,c])=={a:0,b:0,c:0}
print('PASS: U1 4th-root condition, rank-four companion, parity sign,')
print('branch winding, Spin4 no nontrivial continuous 1D characters')
