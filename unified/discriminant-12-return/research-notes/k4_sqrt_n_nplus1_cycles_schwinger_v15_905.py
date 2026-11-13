#!/usr/bin/env python3
"""Gravity v15.905: exact (n,1) Cone -> Schwinger shell, n+1 phase windings.
Equal-frequency two-mode Hamiltonian is an explicit conditional input;
global quantum phase is not an observable inner-circle mechanical rotation.
"""
import sympy as s
n=s.symbols("n",integer=True,positive=True)
j=s.Rational(1,2)*n
outer=(n+1)/2
inner=s.sqrt(n)
cas=s.factor(j*(j+1))
assert s.simplify(2*j+1-(n+1))==0
assert s.simplify(outer**2-cas-s.Rational(1,4))==0
assert s.simplify(outer**2-((n-1)/2)**2-inner**2)==0
assert s.simplify(cas-n*(n+2)/4)==0
# The (x,y)=(n,1) point under Paper C x=n1+1,y=n2 yields:
n1,n2=n-1,s.Integer(1)
assert s.simplify(n1+n2-n)==0
assert s.simplify((n1-n2+1)/2-(n-1)/2)==0
# H0=hbar*omega*(N+1), fixed-shell eigenvalue, and adjacent-shell gap
assert s.simplify(((n+1)+1)-(n+1)-1)==0
phase_one_base_period=s.exp(-s.I*2*s.pi*(n+1))
assert s.simplify(phase_one_base_period-1)==0
# Along the whole SU(2) multiplet n_a+n_b=n, isotropic H identical.
for N in range(1,9):
    energies={a+(N-a)+1 for a in range(N+1)}
    assert energies=={N+1}
    dimension=len(energies) # different from multiplicity!
    assert len(list(range(N+1)))==N+1
    assert s.simplify(cas.subs(n,N)-N*(N+2)/4)==0
    print("n",N,"spin",s.Rational(N,2),"states",N+1,
          "inner",float(s.sqrt(N)),"outer",float(s.Rational(N+1,2)),
          "casimir",float(cas.subs(n,N)),"H0/(hbar omega)",N+1,
          "intra-shell energy gap",0)
print("PASS: Paper C Schwinger (n,1) mapping, Casimir offset, and conditional n+1 phase winding")
