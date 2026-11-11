#!/usr/bin/env python3
"""v15.705: local-WKB TT electric tidal curvature with arbitrary dispersion.

This is a pure linear TT perturbation on a locally Minkowski background,
not the exact full cosmological K4 Fermi metric. K4 tensor mass only enters
through the conditional dispersion K²=Omega²-m_T². The normalized
polarization/eigenvalue structure is independent of K in this approximation.
"""
import sympy as s
t,z=s.symbols("t z",real=True)
Om,K=s.symbols("Omega K",positive=True,real=True)
A,B=s.symbols("A B",real=True)
phase=s.exp(s.I*(Om*t-K*z))
coords=[t,s.Symbol("x"),s.Symbol("y"),z]
h=s.zeros(4)
h[1,1]=A*phase
h[2,2]=-A*phase
h[1,2]=h[2,1]=B*phase
def R0i0j(i,j):
    return s.simplify((
        s.diff(h[0,j],coords[0],coords[i])
        +s.diff(h[i,0],coords[j],coords[0])
        -s.diff(h[i,j],coords[0],2)
        -s.diff(h[0,0],coords[i],coords[j]))/2)
E=s.Matrix(3,3,lambda i,j:R0i0j(i+1,j+1))
Eexpected=s.Matrix([[A,B,0],[B,-A,0],[0,0,0]])*Om**2*phase/2
assert (E-Eexpected).applyfunc(s.simplify)==s.zeros(3)
assert s.simplify(E.trace())==0
lam=s.Symbol("lambda")
assert s.simplify(Eexpected.charpoly(lam).as_expr()
       -lam*(lam**2-(Om**4*phase**2/4)*(A*A+B*B)))==0
mass2=s.symbols("m_T_squared",real=True)
assert (E-Eexpected).subs(K**2,Om**2-mass2).applyfunc(s.simplify)==s.zeros(3)
print("PASS: TT electric tidal polarization independent of local timelike dispersion")
