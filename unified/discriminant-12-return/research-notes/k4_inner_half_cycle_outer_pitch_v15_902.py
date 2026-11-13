#!/usr/bin/env python3
"""Gravity v15.902 — inner half-circuit vs outer (n+1) phase-station pitch.
These are geometric arc lengths in shared grid units. No physical clock assumed.
"""
import sympy as s
n,u,k=s.symbols("n u k",positive=True)
Ri=u*s.sqrt(n)
Ro=u*(n+1)/2
N=n+1
inner_half=s.pi*Ri
outer_pitch=2*s.pi*Ro/N
ratio=s.simplify(inner_half/outer_pitch)
assert s.simplify(outer_pitch-s.pi*u)==0
assert s.simplify(ratio-s.sqrt(n))==0
assert s.simplify(ratio.subs(n,k**2)-k)==0
# One full inner circuit = 2 pi radians, half = pi. Wave with one circuit/cycle has first sign change there.
theta=s.symbols("theta",real=True)
assert s.sin(s.pi)==0 and s.cos(s.pi)==-1
# Independent wave-node versus phase-station counting:
# If m is integer, sin(m theta) has 2m zeros around full 2pi; N station marks need not be zeros.
for v in [1,2,3,4,5,9,16]:
 print(f"n={v}, half-arc/u={float((inner_half/u).subs(n,v)):.12f}, "
       f"outer-pitch/u={float((outer_pitch/u).subs(n,v)):.12f}, ratio={float(ratio.subs(n,v)):.8f}")
print("PASS exact sqrt(n) arc-pitch ratio, square-index integer condition, radian-vs-arc distinction")
