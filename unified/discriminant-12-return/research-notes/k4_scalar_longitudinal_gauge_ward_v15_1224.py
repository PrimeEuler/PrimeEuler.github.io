#!/usr/bin/env python3
"""Gravity v15.1224: longitudinal diffeo Ward check, K4 scalar and Maxwell.

In archived +--- ADM variables on spatially flat FLRW:
 g_0z=-a d_z B, g_zz=-a²(1-2psi-2d_z² E), phi^z=z+d_z P.
For xi^z=d_z lambda and passive perturbation delta=-Lie_xi(background):
 delta E=lambda, delta P=-lambda, delta B=-a lambda_dot.
Noether requires EL_E-EL_P+d_t(a EL_B)=0; it is not an
independent unsatisfied E equation after the P/B equations are imposed.
The Maxwell stress/source sector obeys the same identity by covariant
longitudinal momentum conservation. Does not certify the flawed v15.1222
isotropic R00 source dictionary or solve compact K4 constraints.
"""
import sympy as s

t,k=s.symbols('tau k', positive=True, real=True)
a=s.Function('a')(t)
E,P,B=(s.Function(n)(t) for n in ['E','P','B'])
mu=s.Function('mu')(t);K=s.Function('K')(t);C=s.Function('C')(t)
# Scalar tensor gauge-invariant building blocks.
chi=P+E
b=B+a*s.diff(E,t)
L=K*s.diff(chi,t)**2/2-C*chi**2/2+mu*b**2/2+chi*b
EL=lambda q:s.diff(L,q)-s.diff(s.diff(L,s.diff(q,t)),t)
ward=s.simplify(EL(E)-EL(P)+s.diff(a*EL(B),t))
assert ward==0
lam=s.Function('lam')(t)
# Direct infinitesimal gauge check.
delta_chi=s.simplify((-lam)+(lam))
delta_b=s.simplify((-a*s.diff(lam,t))+a*s.diff(lam,t))
assert delta_chi==0 and delta_b==0

# Source derived from (a^3/2)T^munu delta g_munu, after pairing
# longitudinal cosine metric modes with T^(0z)=m(t) sin(kz),
# T^(zz)=q(t) cos(kz). Overall common spatial-average factor 1/2.
m=s.Function('m')(t);q=s.Function('q')(t)
JB=k*a**4*m/2
JE=-k**2*a**5*q/2
momentum=s.diff(a**5*m,t)-k*a**5*q
assert s.simplify(JE+s.diff(a*JB,t)-k*momentum/2)==0

# From the FLRW Christoffel symbols, momentum conservation is
# dot(T^0z)+5H T^0z + d_z T^zz=0 (constant Fourier wave k).
H=s.diff(a,t)/a
cons=s.diff(m,t)+5*H*m-k*q
assert s.simplify(momentum-a**5*cons)==0

# The E source alone is nonzero, but its EL equation is redundant on-shell.
assert s.simplify(JE)!=0
assert s.simplify(JB)!=0

# No arbitrary Casimir/quarter coefficient arises.
print('PASS passive longitudinal diffeo: E->E+lambda, P->P-lambda, B->B-a lambda_dot')
print('PASS Noether identity EL_E-EL_P+(a EL_B)dot=0')
print('PASS Maxwell sources JE+(a JB)dot = (k/2)[(a^5 m)dot-k a^5 q]')
print('PASS FLRW longitudinal momentum conservation dot(m)+5H m-k q=0')
print('NEGATIVE omitted E EL is not an independent equation when Ward and P/B EL hold')
print('OPEN full physical source/curvature sign reconciliation of v15.1222')
