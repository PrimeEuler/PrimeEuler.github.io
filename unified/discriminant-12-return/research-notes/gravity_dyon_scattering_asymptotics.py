#!/usr/bin/env python3
"""SymPy derivation of radial asymptotics in Taub-NUT versus MIC-Kepler."""
import sympy as s
x,m,l,eps,J=s.symbols('x m l eps J',real=True)
r=1/x
Sigma=r*r+l*l
f=(r*r-2*m*r-l*l)/Sigma
smon=2*eps*l
ptn=eps**2/f**2-1/f-(J**2-smon**2)/(Sigma*f)
expansion=s.series(ptn,x,0,3).remove().expand().collect(x)
expected=eps**2-1+2*m*(2*eps**2-1)*x+((8*eps**2-2)*l*l+(12*eps**2-4)*m*m-J*J)*x*x
assert s.simplify(expansion-expected)==0
print('TN radial momentum squared:', expansion)
print('MIC radial: 2E+2kappa/r-J^2/r^2')
print('Matching E=(eps^2-1)/2, kappa=m(2eps^2-1)')
print('Residual at 1/r^2:',s.factor(expected.coeff(x,2)+J*J))
print('PASS')
