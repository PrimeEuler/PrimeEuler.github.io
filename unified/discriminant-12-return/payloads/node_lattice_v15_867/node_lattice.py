"""
The node-lattice reading of the 1/2 (2026-11-13,
sandbox; Jeremy: could the 1/2 of the transition
parabola be related to the sin/cos wave transition
from positive to negative, like defining its nodes?).

Verified content:

1. The wave's sign flip is exactly the half turn:
   psi(theta + pi) = -psi(theta) for psi = e^{i theta},
   an action advance of h/2. Between consecutive nodes
   the sign is constant, so a sign transition has
   half-turn granularity -- the finest possible.
2. Node lattices in turn units (theta / 2 pi): sin's
   nodes at (1/2) Z; cos's nodes at the odd quarters
   (2k+1)/4; the pair (sin, cos) taken together
   transitions at every point of (1/4) Z. Standing
   waves inherit it: nodes at half-wavelength spacing,
   L = n lambda/2.
3. The mesh image: consecutive lattice nodes straddle
   their centre at half the sector step (offset h/2 --
   EM 1/2, G 1/4, q = h/2 of v15.866): the transition
   split sits at the half because the wave's own sign
   lattice has half-period granularity. The antinodes
   (extrema) sit at the odd quarters -- the components'
   transition points of item 2.
4. The record's bookkeeping echo, exact: the
   bouncer's comb (n - 1/4) is its transitions' phase
   losses -- hard wall pi (a forced node) + soft
   turning point pi/2 -- summed over the round trip:
   (2 pi (n-1) + 3 pi/2) / (2 pi) = n - 1/4. The comb
   offset is node bookkeeping, not a fitted shift.

Scope: this explains why the transition step is the
half (a sign cannot change at finer granularity than
half a period); it does not set the sector step h,
which remains the weld dictionary's datum (v15.866).
The component/quarter correspondence (cos nodes at
quarter turns against the G sector's quarter vertex)
is filed as a rhyme [I], not a derivation.
"""
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

th = sp.symbols("theta", real=True)
flip = sp.simplify(sp.exp(sp.I * (th + sp.pi)) / sp.exp(sp.I * th))
print(f"1. psi(theta+pi)/psi(theta) = {flip} -- sign flip at exactly the half turn (h/2 of action)")
zeros_at = [z for z in (0, sp.pi, 2 * sp.pi)]
pattern = []
for k in range(4):
    xs = np.linspace(k * np.pi + 1e-9, (k + 1) * np.pi - 1e-9, 2000)
    sg = np.sign(np.sin(xs))
    assert np.all(sg == sg[0])
    pattern.append("+" if sg[0] > 0 else "-")
print(f"   sin nodes in [0, 2 pi]: {[str(z) for z in zeros_at]} -> in turns: "
      f"{[sp.nsimplify(z / (2 * sp.pi)) for z in zeros_at]} -- the (1/2) Z lattice; "
      f"sign constant on each interval between nodes (pattern over 4 intervals: {pattern})")

print("\n2. node lattices in turns:")
print("   sin: k/2 (k in Z). cos: (2k+1)/4 -- odd quarters. Union: (1/4) Z:")
union = sorted({Fr(k, 2) for k in range(5)} | {Fr(2 * k + 1, 4) for k in range(4)})
print(f"   {union} -- the (sin, cos) pair transitions at every quarter turn")
print("   standing wave sin(n pi x / L): nodes at x = L k / n -- spacing lambda/2 with lambda = 2L/n")

print("\n3. straddle: mesh nodes j, j+1 straddle centre j + 1/2 at offset h/2 per sector")
print("   (EM 1/2, G 1/4 = q of v15.866); wave antinodes at odd quarter turns (2k+1)/4,")
print("   the components' nodes of item 2 [I rhyme with the quarter sector].")

print("\n4. bouncer comb bookkeeping (exact fractions):")
for n in range(1, 5):
    lhs = (2 * Fr(1) * (n - 1) + Fr(3, 2)) / 2  # (2 pi (n-1) + 3 pi/2) / (2 pi), in units of pi -> /pi
    print(f"   n = {n}: (2(n-1) + 3/2)/2 = {lhs} = n - 1/4 = {n - Fr(1, 4)}: {lhs == n - Fr(1, 4)}")
print("   phase losses: hard wall pi (forced node) + soft turn pi/2; total 3 pi/2 per round trip.")
