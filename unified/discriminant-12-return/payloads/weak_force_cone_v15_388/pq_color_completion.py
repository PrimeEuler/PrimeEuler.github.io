"""
The (p,q) color completion (2026-11-04, sandbox).

Extend the k=3 side with conjugate modes: a-modes in the fundamental
3, b-modes in the antifundamental 3bar (two-oscillator Schwinger
construction). Irreps (p,q): dimension (p+1)(q+1)(p+q+2)/2, Young
diagram (p+q, q) with p + 2q boxes, irrep triality (p - q) mod 3 =
boxes mod 3. Conjugation: (p,q) <-> (q,p), triality flips sign.

Assemble the FULL SM internal table in one frame:
    field = ( color (p,q) )  x  ( weak slot: j, shell N, N_A, c, z )  x  Y
with the weak slot and Y from the completed weak-side work, and check
the cross-consistency of the two factors. The headline identity:
on every field -- matter, antimatter, gluons included --
    c  =  p - q        (exactly, signed),
so the weak slot's third-mode occupation and the color factor's
(p - q) are one integer seen from two sides, and the split grading
c mod 3 IS the color irrep triality (p - q) mod 3. (Consistency of
the completed assignments, stated as such in the report: both were
built from tau_SM; the completion shows the two presentations mesh
on the whole table with no exceptions, and the earlier presentational
tension -- Q_L sitting in a frame shell (2,0) -- dissolves: the frame
shell is a weak-side slot label, the color (1,0) is its own factor.)

Composites: triality is uniform across any tensor product's
components (box count mod 3 is additive; removing a height-3 column
changes boxes by 3). A product can contain the singlet (0,0) only if
its total triality is 0 mod 3. Verify the standard decompositions by
dimension + triality, and the exclusions by box counting.
"""
from fractions import Fraction

def dim(pq):
    p, q = pq
    return (p + 1) * (q + 1) * (p + q + 2) // 2
def tau_irrep(pq):
    p, q = pq
    return (p - q) % 3
def boxes(pq):
    p, q = pq
    return p + 2 * q
def conj(pq):
    p, q = pq
    return (q, p)

print("=" * 76)
print("1. (p,q) machinery: dimensions, triality, boxes mod 3 = triality")
print("=" * 76)
for pq in [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (3, 0), (0, 3), (2, 2)]:
    print(f"  {pq}: dim={dim(pq)}, triality={tau_irrep(pq)}, boxes={boxes(pq)}, "
          f"boxes mod 3 = {boxes(pq) % 3} (equal: {boxes(pq) % 3 == tau_irrep(pq)}); "
          f"conjugate {conj(pq)} triality {tau_irrep(conj(pq))}")

print()
print("=" * 76)
print("2. The full SM internal table in one frame:  c = p - q on every field")
print("   (weak slot: shell N, pair N_A, third-mode c, z;  Y from completed work)")
print("=" * 76)
# name: (color (p,q), j, Y, c_signed)
FIELDS = {
    "Q_L":    ((1, 0), Fraction(1, 2), Fraction(1, 3),   1),
    "u_R":    ((1, 0), Fraction(0),    Fraction(4, 3),   1),
    "d_R":    ((1, 0), Fraction(0),    Fraction(-2, 3),  1),
    "L_L":    ((0, 0), Fraction(1, 2), Fraction(-1),     0),
    "e_R":    ((0, 0), Fraction(0),    Fraction(-2),     0),
    "nu_R":   ((0, 0), Fraction(0),    Fraction(0),      0),
    "H":      ((0, 0), Fraction(1, 2), Fraction(1),      0),
    "W":      ((0, 0), Fraction(1),    Fraction(0),      0),
    "gluon":  ((1, 1), Fraction(0),    Fraction(0),      0),
    "anti-Q": ((0, 1), Fraction(1, 2), Fraction(-1, 3), -1),
    "anti-u": ((0, 1), Fraction(0),    Fraction(-4, 3), -1),
    "anti-d": ((0, 1), Fraction(0),    Fraction(2, 3),  -1),
    "anti-L": ((0, 0), Fraction(1, 2), Fraction(1),      0),
    "anti-e": ((0, 0), Fraction(0),    Fraction(2),      0),
    "anti-H": ((0, 0), Fraction(1, 2), Fraction(-1),     0),
}
allok = True
for name, (pq, j, Y, c) in FIELDS.items():
    NA = int(2 * j)
    N = NA + abs(c) if c >= 0 else NA + abs(c)  # shell by |c| in its sector
    z = NA - 2 * c
    ident = (c == pq[0] - pq[1])
    grading = (c % 3) == tau_irrep(pq)
    n2 = int(2 * j) % 2
    frac_ok = (Y / 2) % 1 == (-Fraction(c % 3, 3) - Fraction(n2, 2)) % 1
    allok &= ident and grading and frac_ok
    print(f"  {name:>8}: color {pq} (tau={tau_irrep(pq)}), j={j}, c={c:+d}: "
          f"c = p-q: {ident}; c mod 3 = irrep triality: {grading}; "
          f"Y-frac via (n2, c mod 3): {frac_ok}")
print(f"  ALL fields consistent (identity, grading, fractions): {allok}")
# electric charge spectra spot-check from Q = T3 + Y/2
def spectrum(j, Y):
    steps = int(2 * j)
    return sorted(Fraction(steps - 2 * i, 2) + Y / 2 for i in range(steps + 1))
print(f"  Q_L spectrum: {[str(x) for x in spectrum(Fraction(1,2), Fraction(1,3))]} (SM: 2/3, -1/3)")
print(f"  W spectrum:   {[str(x) for x in spectrum(Fraction(1), Fraction(0))]} (SM: 1, 0, -1)")

print()
print("=" * 76)
print("3. Composites: singlet containment and exclusion")
print("=" * 76)
DECOMP = {  # asserted standard decompositions, checked by dim + triality
    "(1,0)x(0,1) [q qbar]": ([(1, 0), (0, 1)], [(0, 0), (1, 1)]),
    "(1,0)x(1,0) [q q]":    ([(1, 0), (1, 0)], [(2, 0), (0, 1)]),
    "(1,0)^3 [qqq]":        ([(1, 0)] * 3,     [(3, 0), (1, 1), (1, 1), (0, 0)]),
    "(1,1)x(1,1) [g g]":    ([(1, 1), (1, 1)], [(0, 0), (1, 1), (1, 1), (3, 0), (0, 3), (2, 2)]),
}
for label, (factors, comps) in DECOMP.items():
    dim_in = 1
    for f in factors: dim_in *= dim(f)
    dim_out = sum(dim(c) for c in comps)
    total_tau = sum(tau_irrep(f) for f in factors) % 3
    uniform = all(tau_irrep(c) == total_tau for c in comps)
    has_singlet = (0, 0) in comps
    print(f"  {label}: dim {dim_in} = {dim_out}: {dim_in == dim_out}; "
          f"triality uniform ({total_tau}): {uniform}; contains singlet: {has_singlet}")
print("  Exclusions by box counting (total boxes mod 3 != 0 => no singlet possible):")
for label, factors in [("q q", [(1, 0), (1, 0)]),
                       ("q q qbar", [(1, 0), (1, 0), (0, 1)]),
                       ("q", [(1, 0)])]:
    tb = sum(boxes(f) for f in factors) % 3
    print(f"  {label}: total boxes mod 3 = {tb} -> singlet (0 boxes, 0 mod 3) excluded: {tb != 0}")
print("  qqq total boxes mod 3 =", sum(boxes(f) for f in [(1, 0)] * 3) % 3,
      "-> singlet allowed by triality, and present in the decomposition above (baryons).")
print()
print("SCOPE: the color factor is a global Schwinger (p,q) structure --")
print("container and labels, singlet-composition rules. No gauge fields,")
print("no confinement dynamics, no running coupling. The identity c = p - q")
print("is a consistency of the completed assignments across the whole")
print("table, not a derivation of one factor from the other.")
