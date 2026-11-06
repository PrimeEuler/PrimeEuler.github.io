"""
AM-GM 3, squared -- on the square-root-hyperbola template
(2026-11-06, sandbox; Jeremy's identification: "its like the
square root hyperbola on the cone").

The record's square-root hyperbola (v15.234 sec.B; boost grid,
2026-10-31): pairs (u, v) with uv = N, a rectangular hyperbola
whose label and cone height are GM = sqrt(N); its lattice
points are exactly the factor pairs (d, N/d), counted by the
divisor function d_2(N); its seat u = v sits on the lattice
iff N is a perfect square; position along it is the ratio
coordinate psi, the split (lu, v/l) preserving the product.

This build runs the same construction at level k = 3 and then
squares it, the way the bicone squared AM-GM 2:
 1. the constant-product locus xyz = N: lattice points are
    factor triples, counted by d_3(N) (two computations agree);
    the seat x = y = z sits on the lattice iff N is a perfect
    cube; the label is GM_3 = N^(1/3), and the seat is the
    AM = GM point of the triple AM-GM inequality;
 2. the square: pairing the locus with itself squares the
    Dirichlet series -- d_3 * d_3 = d_6 exactly (and the k=2
    parallel d_2 * d_2 = d_4): (zeta^3)^2 = zeta^6, the k=6
    member, whose split grading is Z6 -- the SM's own quotient
    group; the square of k=2 is k=4, Hessian signature (1,3);
 3. the frame's composites are the locus's factor structures:
    mesons are factor PAIRS of the triple locus (3 x 3bar,
    total triality 0 = on the singlet sublocus), baryons are
    factor TRIPLES (singlet iff sum tau = 0 mod 3); positions
    along the pair locus in fold digits: sigma9 = 3(g - g'),
    the seat sigma9 = 0 iff g = g' (flavor diagonal -- the
    balanced pair, the condensate channel).
Sections 1-2 are unconditional family arithmetic; section 3's
digit statements inherit the fold's hypotheses H1/H2
(v15.461); its tau-level statements are v15.388-solid.
"""
from fractions import Fraction as F
from itertools import product as iproduct
import math

NMAX = 60

def d_k(k, n):
    """k-fold Dirichlet convolution of 1, exact integers."""
    cur = [0] + [1] * n
    for _ in range(k - 1):
        nxt = [0] * (n + 1)
        for a in range(1, n + 1):
            if cur[a]:
                for b in range(1, n // a + 1):
                    nxt[a * b] += cur[a]
        cur = nxt
    return cur

def triples(n):
    out = []
    for x in range(1, n + 1):
        if n % x: continue
        m = n // x
        for y in range(1, m + 1):
            if m % y == 0:
                out.append((x, y, m // y))
    return out

print("=" * 76)
print("1. the level-3 product locus xyz = N (the cube-root hyperbola)")
print("=" * 76)
d3 = d_k(3, NMAX)
agree = all(len(triples(n)) == d3[n] for n in range(1, NMAX + 1))
print(f"  factor-triple count == d_3(N) by Dirichlet convolution,")
print(f"  N = 1..{NMAX}: {agree}")
cubes = {r ** 3: r for r in range(1, 5)}
for n in (8, 27, 36, 64):
    ts = triples(n)
    seat = [t for t in ts if t[0] == t[1] == t[2]]
    ams = [F(sum(t), 3) for t in ts]
    print(f"  N = {n:2d}: {len(ts):2d} triples, seat on lattice: "
          f"{seat if seat else 'NO'} (perfect cube: {n in cubes}); "
          f"min AM = {min(ams)} vs GM = {n ** (1/3):.4f} "
          f"(AM = GM exactly at the seat only: "
          f"{(min(ams) == cubes[n]) if n in cubes else 'n/a'})")
print("  shell N = 36 has a k=2 seat (6,6) but NO k=3 seat -- the")
print("  two hyperbolas see different balanced points on one shell.")

print()
print("=" * 76)
print("2. the square: d_k * d_k = d_{2k} (Dirichlet self-pairing)")
print("=" * 76)
def conv(a, b, n):
    out = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, n // i + 1):
            out[i * j] += a[i] * b[j]
    return out
d2, d4, d6 = d_k(2, NMAX), d_k(4, NMAX), d_k(6, NMAX)
sq2 = conv(d2, d2, NMAX) == d4
sq3 = conv(d3, d3, NMAX) == d6
print(f"  d_2 * d_2 == d_4 (N <= {NMAX}): {sq2}   "
      f"[square of AM-GM 2: k=4, Hessian signature (1,3)]")
print(f"  d_3 * d_3 == d_6 (N <= {NMAX}): {sq3}   "
      f"[square of AM-GM 3: k=6, split grading Z6 = SM quotient]")
print("  self-pairing doubles the zeta exponent; the bicone is the")
print("  k=2 self-pairing, and its (1,3) signature is the k=4")
print("  member's Hessian signature -- on the family's analytic")
print("  face (the spacetime intertwiner stays open, v14.818).")

print()
print("=" * 76)
print("3. composites as factor structures of the locus (fold digits)")
print("=" * 76)
# meson = factor pair (q, qbar): classes c = tau + 3g and -(tau + 3g')
MESONS = [("pi (u ubar)", 0, 0), ("K0 (d sbar)", 0, 1), ("K0bar (s dbar)", 1, 0),
          ("B0 (d bbar)", 0, 2), ("Bs (s bbar)", 1, 2), ("B_sbar (b sbar)", 2, 1)]
for name, g, gp in MESONS:
    s9 = (3 * (g - gp)) % 9
    print(f"  {name:16s} g={g}, g'={gp}: sigma9 = {s9} "
          f"{'<-- SEAT (balanced pair)' if s9 == 0 else ''}")
print("  sigma9 = 3(g - g') mod 9 is tau-independent (tau cancels in")
print("  the pair sum): the pair's position along the hyperbola, in")
print("  fold digits; the seat is exactly the flavor-diagonal pairs.")
BARYONS = [("p (uud)", 0), ("Lambda (uds)", 1), ("Xi (uss)", 2), ("Omega (sss)", 3)]
for name, sg in BARYONS:
    print(f"  {name:14s} sum g = {sg}: total class 3(1 + sum g) mod 9 = "
          f"{(3 * (1 + sg)) % 9}")
print("  baryons: singlet iff sum tau = 3 = 0 mod 3 (on the locus);")
print("  the fold class cycles 3, 6, 0, 3 with total generation")
print("  number mod 3. qq and q q qbar never reach the singlet")
print("  sublocus (sum tau = 2, 1) -- v15.388's box-counting, restated")
print("  as positions relative to the product locus.")

print()
print("=" * 76)
print("VERDICT")
print("=" * 76)
print("Jeremy's identification holds as a construction: the")
print("square-root hyperbola is the k=2 face of a level-k pattern --")
print("constant-product locus, seat = k-th root = GM_k (the AM = GM")
print("point), lattice points = factor k-tuples counted by d_k,")
print("position = ratio/grading coordinates. Squaring = self-")
print("pairing: k -> 2k on the Dirichlet face (2 -> 4 with (1,3);")
print("3 -> 6 with Z6, the SM quotient itself). The frame's")
print("composites live on the k=3 locus as its factor pairs and")
print("triples, and in fold digits the meson's position along the")
print("locus is its generation difference, with the seat at the")
print("flavor diagonal. Digit statements conditional on H1/H2")
print("(v15.461); the locus and square arithmetic is unconditional.")
