"""Model a LIST that fits psi = 45.310004305 (2 psi = 90.620008610).
Forced lists only; rules fixed before looking at totals."""
import numpy as np
from math import log, factorial
T2 = 2*45.310004305

print('=== L1: balanced-state loop rapidities up the multiplet ladder ===')
print('at balance: p=(j+1)/(2j+1), h=j/(2j+1) -> rapidity (1/2)ln((j+1)/j)')
print('sum telescopes EXACTLY: total(J) = (1/2) ln(J+1)')
for J in (11, 12, 29, 42):
    print(f'  J={J:3d}: total = {0.5*log(J+1):.4f}')
print(f'  to fit psi the list needs J+1 = e^(2 psi) = D links -- the count IS D.')

print()
print('=== L2: closure-count accumulation, links ln(2j+1) (balanced N per shell) ===')
acc, vals = 0.0, {}
for j in range(0, 61):
    acc += log(2*j+1) if j > 0 else 0.0
    vals[j] = acc
for J in (12, 42):
    print(f'  at forced terminus J={J}: total ln prod(2j+1) = {vals[J]:.4f} vs 2psi = {T2:.4f}')

print()
print('=== L3: the 12-node helix list, Y^2 = k(12-k), k=1..11 ===')
tot = sum(0.5*log(k*(12-k)) for k in range(1, 12))
print(f'  sum (1/2)ln Y^2 = ln(11!) = {tot:.4f}   (target 45.3100 for psi, 90.6200 for 2psi)')

print()
print('=== L4: conductor channel list (v14.612), links from measured s(chi) ===')
s = [0.7525491014, 0.4115927347, 0.2406063975, 0.2159410817, 0.1108409991,
     0.0914220662, 0.377326159, 0.2110741011, 0.04066865951, 0.01889365299]
print(f'  sum ln(1/s) over 10 diving channels = {sum(log(1/x) for x in s):.4f}')
print(f'  sum |C1| = {sum(x*q for x, q in zip(s, [5,8,12,13,21,24,3,4,7,8])):.4f}  (s=-C1/q)')
