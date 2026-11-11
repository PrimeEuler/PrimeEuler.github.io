#!/usr/bin/env python3
"""Additive repair for v15.686 reproducibility error (External Audit Round 541).

This does not alter the historical script. It checks equivalent SymPy
rational expressions by simplification instead of bare structural ==.
"""
import sympy as s
L=s.symbols("L",positive=True)
C=lambda t:t*(t+4)/16
d1=s.simplify(C(L+1)-C(L))
d2=s.simplify(C(L+2)-C(L))
computed=s.simplify(d1/d2)
target=(2*L+5)/(4*(L+3))
assert s.simplify(computed-target)==0
assert computed.equals(target)
assert s.simplify(d1-(2*L+5)/16)==0
assert s.simplify(d2-(L+3)/4)==0
for n in range(1,64):
    assert s.simplify(computed.subs(L,n)-target.subs(L,n))==0
print("PASS: v15.686 Casimir gap-ratio identity independently reproduced")
