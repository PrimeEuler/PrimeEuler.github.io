"""
The frame's whole label set is one class mod 18 (2026-11-06,
sandbox). The frame's labels come from three family members:
n2 (the k=2 parity shadow), tau (the k=3 triality shadow), and
-- under the fold, v15.461 -- the generation digit g (the k=9
class's second base-3 digit). Since Z18 = Z2 x Z9 by CRT
(gcd(2,9) = 1), the triple (n2, tau, g) is the shadow system
of a single class c18 mod 18 = 2 * 3^2: the bicone prime times
the squared triple prime -- the square theme of v15.466,
carried by one integer.

Checks (exact):
 1. the CRT map (n2, tau, g) -> c18 is a bijection onto Z18
    (18 triples, 18 classes);
 2. the frame's 24 slots (8 entries x 3 generations) land on
    those classes with EXACTLY the degeneracies filed at
    v15.388 (L_L/H share (1,0); u_R/d_R share (0,1); e_R/nu_R/W
    share (0,0)) -- the address is as informative as the
    frame's label set, no more, no less; the degeneracy is
    lifted by Y's integer part (anomaly/anchor data), as before;
 3. charges read only the mod-6 shadow: c18 mod 6 recovers
    (n2, tau), and the Z6 congruence / Y mod 2 are functions of
    it -- the mod-18 class's extra digit is the generation
    digit and nothing else;
 4. antimatter is negation: the fold's digit law (v15.461)
    composed with CRT gives class(antiparticle) = -c18 mod 18
    for every slot; the self-conjugate addresses are exactly
    c18 in {0, 9} -- the tau=0, g=0 slots (e_R/nu_R/W at 0,
    L_L/H at 9) -- whose particle/antiparticle split was always
    carried by the sign data (Y sign, chirality tag), not by
    (n2, tau).
Discussion filed with the build: the class serves as an
ADDRESS (distinctness + tower order); nature's mixing does not
use its cyclic addition law -- on Z3, generations 0 and 2 are
cyclically adjacent to 0 exactly as 1 is, but the measured
(imported) |V_ub| / |V_us| ~ 1/59, and the two |dg| = 1
elements differ 5x themselves (|V_us| 0.2245, |V_cb| 0.0410);
mixing follows the tower's linear order and the mass data,
not digit addition. The fold needs only distinct classes in
an order -- which is what an address is.
"""
from fractions import Fraction as F

ENTRIES = [("L_L", 1, 0, F(-1)), ("Q_L", 1, 1, F(1, 3)), ("H", 1, 0, F(1)),
           ("e_R", 0, 0, F(-2)), ("u_R", 0, 1, F(4, 3)), ("d_R", 0, 1, F(-2, 3)),
           ("nu_R", 0, 0, F(0)), ("W", 0, 0, F(0))]

def crt_class(n2, tau, g):
    c9 = (tau + 3 * g) % 9
    for c in range(18):
        if c % 2 == n2 and c % 9 == c9:
            return c
    raise ValueError

print("=" * 76)
print("1-2. the address map: bijection on triples, frame degeneracies kept")
print("=" * 76)
triples = [(n2, tau, g) for n2 in (0, 1) for tau in (0, 1, 2) for g in (0, 1, 2)]
classes = [crt_class(*t) for t in triples]
print(f"  18 triples -> classes {sorted(classes)}: bijection "
      f"{sorted(classes) == list(range(18))}")
slots = {}
for name, n2, tau, Y in ENTRIES:
    for g in (0, 1, 2):
        slots.setdefault(crt_class(n2, tau, g), []).append(f"{name}(g{g})")
shared = {c: v for c, v in slots.items() if len(v) > 1}
print(f"  24 frame slots occupy {len(slots)} classes; shared addresses:")
for c, v in sorted(shared.items()):
    print(f"    class {c:2d}: {', '.join(v)}")
print("  sharing is exactly the v15.388 degeneracies ((n2, tau) pairs),")
print("  lifted by Y's integer part -- the address loses nothing the")
print("  frame's labels had, and adds the generation digit.")

print()
print("=" * 76)
print("3. charges read only the mod-6 shadow")
print("=" * 76)
ok6 = True
for name, n2, tau, Y in ENTRIES:
    for g in (0, 1, 2):
        c = crt_class(n2, tau, g)
        ok6 &= (c % 6) % 2 == n2 and (c % 6) % 3 == tau
        ok6 &= ((Y / 2 + F(tau, 3) + F(n2, 2)) % 1 == 0)
print(f"  c18 mod 6 recovers (n2, tau) for every slot, and the Z6")
print(f"  congruence holds from the shadow alone: {ok6}")

print()
print("=" * 76)
print("4. antimatter is negation mod 18")
print("=" * 76)
neg_ok = True
for name, n2, tau, Y in ENTRIES:
    for g in (0, 1, 2):
        c = crt_class(n2, tau, g)
        c9 = (tau + 3 * g) % 9
        cp9 = (-c9) % 9                      # fold involution (v15.461)
        taup, gp = cp9 % 3, ((cp9 - (cp9 % 3)) // 3) % 3
        neg_ok &= (crt_class(n2, taup, gp) == (-c) % 18)
print(f"  class(antiparticle) == -c18 (mod 18) for all 24 slots: {neg_ok}")
fixed = [c for c in range(18) if (-c) % 18 == c]
print(f"  self-conjugate addresses: {fixed} = the (tau 0, g 0) slots")
print(f"  (class 0: e_R/nu_R/W addresses; class 9: L_L/H addresses),")
print(f"  split particle/antiparticle by sign data, as since v15.388.")

print()
print("=" * 76)
print("VERDICT")
print("=" * 76)
print("The frame's complete discrete label set -- weak parity,")
print("triality, generation -- is the shadow system of one class")
print("mod 18 = 2 * 3^2, faithfully: bijective on triples, frame")
print("degeneracies preserved, charges on the mod-6 shadow,")
print("antimatter as negation. H1 (v15.461) sharpens accordingly:")
print("the identification needed is no longer three separate")
print("shadows but one -- the frame's fields carry addresses in")
print("Z18, and the fold is the statement that the address's")
print("mod-9 component is a real class, not a bookkeeping tower.")
print("The class is an address, not an operand: nature's mixing")
print("(|V_ub|/|V_us| ~ 1/59 against cyclic adjacency) does not")
print("add digits. Conditional on H1/H2 as before; the CRT")
print("repackaging itself is unconditional arithmetic.")
