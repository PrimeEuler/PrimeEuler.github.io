#!/usr/bin/env python3
"""v15.1469: same normalized 1/16 variance but different
Maxwell-accessible antisymmetric area. Toy covariance/orientation
test; not a physical derivation of quarter-grid EM coupling.
"""
import sympy as sp
V=sp.Rational(1,16)
a=sp.symbols('a',nonnegative=True,real=True)
Sigma=sp.diag(a,V-a)
area2=2*Sigma.det()
assert sp.simplify(area2-2*a*(V-a))==0
assert area2.subs(a,0)==0
assert area2.subs(a,V/2)==sp.Rational(1,512)
assert sp.simplify(sp.diff(area2,a)-(2*V-4*a))==0
assert sp.diff(area2,a,2)==-4
print('total_variance_trace',V,'rank_one_area2',area2.subs(a,0),
      'isotropic_area2',area2.subs(a,V/2))
theta=sp.symbols('theta',real=True)
p=sp.Matrix([sp.sqrt(V),0])
q=sp.Matrix([sp.sqrt(V)*sp.cos(theta),sp.sqrt(V)*sp.sin(theta)])
wedge=sp.factor((p[0]*q[1]-p[1]*q[0])**2)
assert sp.simplify(wedge-V**2*sp.sin(theta)**2)==0
print('fixed_norm_wedge2',wedge,'parallel',wedge.subs(theta,0),
      'orthogonal',wedge.subs(theta,sp.pi/2))
print('PASS fixed 1/16 trace/norm cannot uniquely fix area response')
print('OPEN selected covariance, normalization and EM coupling')
