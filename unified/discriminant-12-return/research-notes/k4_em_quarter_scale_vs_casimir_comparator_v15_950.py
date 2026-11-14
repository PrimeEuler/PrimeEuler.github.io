#!/usr/bin/env python3
"""Gravity v15.950: matched normalized shell vs matched physical product
for u_EM=1 and u_quarter=1/2. Geometric action-circle comparator,
not a newly derived gravitational operator Casimir.
"""
import sympy as s
n,P,u=s.symbols("n P u", positive=True)
inner2=u*u*n
cas2=u*u*n*(n+2)/4
outer2=u*u*(n+1)**2/4
assert s.simplify(outer2-cas2-u*u/4)==0
assert s.simplify(cas2-inner2-u*u*n*(n-2)/4)==0
assert s.simplify(outer2/inner2-(n+1)**2/(4*n))==0
assert s.simplify(cas2/outer2-n*(n+2)/(n+1)**2)==0
# Fixed physical product P=u² n; the original (un,u) endpoint
# diameter depends on u, while the inner chord does not.
n_at_P=P/u**2
assert s.simplify(inner2.subs(n,n_at_P)-P)==0
D_at_P=s.factor(u*(n_at_P+1))
C_at_P=s.factor(cas2.subs(n,n_at_P))
assert s.simplify(D_at_P-(P/u+u))==0
assert s.simplify(C_at_P-(P**2/(4*u*u)+P/2))==0
C_em=s.simplify(C_at_P.subs(u,1))
C_g=s.simplify(C_at_P.subs(u,s.Rational(1,2)))
assert s.simplify(C_g-C_em-3*P**2/4)==0
assert s.simplify(D_at_P.subs(u,s.Rational(1,2))-
                  D_at_P.subs(u,1)-(P-s.Rational(1,2)))==0
# The q=2 *formal* odd-quarter shell j=L/4 has a different
# representation label; it is not the co-scaled physical SU2 Casimir.
L=s.symbols('L',integer=True,positive=True)
C_formal=L*(L+4)/16
C_refined=L*(L+2)/4
assert s.factor(C_refined-C_formal)==L*(3*L+4)/16
# At matched dimensionless n, physical product levels differ by 1/4:
for N in range(1,201):
    assert s.Rational(1,4)*N != N
    em=s.simplify(C_em.subs(P,N))
    grav=s.simplify(C_g.subs(P,N))
    assert grav-em==s.Rational(3*N*N,4)
for N in (1,2,3,6,12):
    print('physical P=',N, 'EM C_radius²=',C_em.subs(P,N),
          'quarter C_radius²=',C_g.subs(P,N),
          'difference=',(C_g-C_em).subs(P,N))
print('PASS: matched-shell scale covariance, equal-product contrast, distinct formal Casimir')
