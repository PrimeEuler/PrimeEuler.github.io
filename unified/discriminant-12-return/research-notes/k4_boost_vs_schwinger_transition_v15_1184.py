#!/usr/bin/env python3
"""Gravity v15.1184 — rapidity dictionary versus discrete Schwinger jumps.
Standard fixed-pair Cone T=(n+k)/2 X=(n-k)/2 Y=sqrt(nk).
A Lorentz O(1,1) boost rescales n,k reciprocally, preserving product
Y²=nk, but not generally the oscillator shell D=n+k.
The physical Schwinger J+ instead maps (n,k)->(n+1,k-1), preserving
D but changing product, with zero Bohr gap in the isotropic H0.
The dictionary beta=tanh(psi)=X/T does not determine physical v/c.
"""
import sympy as s
n,k,z=s.symbols("n k z",positive=True)
T=(n+k)/2;X=(n-k)/2;Y=s.sqrt(n*k)
assert s.simplify(T*T-X*X-Y*Y)==0
nb=z*n;kb=k/z
assert s.simplify(nb*kb-n*k)==0
assert s.simplify(nb+kb-(n+k))!=0
ns=n+1;ks=k-1
assert s.expand(ns+ks-n-k)==0
assert s.expand(ns*ks-n*k)==k-n-1
assert s.simplify((n-k)/(n+k)-(n/k-1)/(n/k+1))==0
assert s.simplify((n-k)/(n+k)-s.tanh(s.log(n/k)/2).rewrite(s.exp))==0
print("PASS boost preserves product/changes D; J+ preserves D/changes product")
print("PASS tanh(1/2 log(n/k)) = X/T")
print("EXAMPLE boost n,k=(2,1), z=2 -> (4,1/2): D changes 3 to 9/2")
print("NEGATIVE no physical v/c or radiative frequency selected")
