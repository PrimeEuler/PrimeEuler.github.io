#!/usr/bin/env python3
"""v15.694: Taub-NUT fixed-l Misner-time Fourier scale/phase audit.

Here the formal Lorentzian time circle has T=8*pi*l/c and
E_k=2*pi*hbar*k/T. Fractional translations are ordinary
circle characters, not automatically gauge-invariant angular holonomies.
"""
import sympy as s
k=s.symbols("k",integer=True)
l,c,hbar=s.symbols("l c hbar",positive=True)
pi=s.pi
T=8*pi*l/c
E=lambda n:s.simplify(2*pi*hbar*n/T)
assert s.simplify(E(k)-hbar*c*k/(4*l))==0
assert s.simplify(E(k+1)-E(k)-hbar*c/(4*l))==0
assert s.simplify(E(k)*l/(hbar*c)-k/4)==0
assert s.simplify(E(k+1)/E(k)-(k+1)/k)==0
for r in (2,3,4,5,8):
    for n in range(-20,21):
        z=s.exp(-2*s.I*pi*n/r)
        assert s.simplify(z**r-1)==0
lam=s.symbols("lam",positive=True)
assert s.simplify(E(k).subs(l,lam*l)*lam-E(k))==0
for n in range(-20,21):
    assert s.simplify(s.exp(-2*s.I*pi*n)-1)==0
print("PASS: p_G=k/4; full-circle phase=1; fractional phase=exp(-2pi i k/r)")
print("PASS: scale-free ratios depend only on winding k; absolute 1/l scale is free")
