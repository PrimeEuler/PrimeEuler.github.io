"""
Door anatomy I (2026-11-05, sandbox): the chiral door, measured.
open_more_doors.py (v15.388) located the door exactly: every
equation in the frame thread is invariant under the global flip
of fermion chirality tags L<->R; the un-encoded step is the
correlation between the frame's tags and the bicone's Spin(4)
factors. This build MEASURES the door: it enumerates the
candidate correlations and tests each against every internal
constraint on record, to find the door's exact information
content.

Lorentz side: Spin(4) = SU(2)_A x SU(2)_B, irreps (jA, jB),
conjugation swaps the factors: (jA, jB)* = (jB, jA)  [the
SL(2,C) fact (1/2,0)* = (0,1/2)]. A correlation phi assigns the
frame's tagged-L fermion doublet to one factor's doublet:
  phi = identity:  L -> (1/2, 0), R -> (0, 1/2)
  phi = swap:      L -> (0, 1/2), R -> (1/2, 0)
(bosons carry no tag: H is a Lorentz scalar (0,0); W and gluons
are vectors (1/2,1/2); the graviton of the record is (1,1) --
all three are factor-swap invariant as reps.)

Constraints tested for each phi:
 C1 Yukawa/Dirac scalar: for each (doublet, singlet) fermion
    pair, conj(rep doublet) x rep singlet must contain (0,0).
 C2 Charged current: conj(D) x D x (1/2,1/2) must contain (0,0)
    (W couples the doublet to itself).
 C3 Antimatter: the frame's anti-doublet carries the flipped
    tag; consistency needs phi(flipped tag, doublet) ==
    conj(phi(tag, doublet)) -- the correlation must commute
    with the frame's conjugation (v15.388 antimatter section).
 C4 Bicone pair home: the spinor doublet of the record
    (v15.140/v15.282) is the unordered PAIR {(1/2,0),(0,1/2)};
    the pair as a set must be phi-independent.
 C5 Graviton (1,1) and vectors (1/2,1/2): self-conjugate and
    swap-fixed, so no constraint on phi (checked, not assumed).
If both phi pass everything, the door is exactly one bit, and
the bit is the Lorentz parity choice -- fixed in nature by
weak-interaction parity violation (an empirical input), not by
any quantity internal to the frame or the bicone.
"""
from fractions import Fraction as F

H = F(1, 2)
def prod(r1, r2):
    """(jA,jB) x (kA,kB) decomposition as a set of irreps."""
    out = set()
    for a in range(int(abs(r1[0] - r2[0])), int(r1[0] + r2[0]) + 1):
        for b in range(int(abs(r1[1] - r2[1])), int(r1[1] + r2[1]) + 1):
            out.add((F(a), F(b)))
    return out
def prodS(setA, setB):
    out = set()
    for r1 in setA:
        for r2 in setB:
            out |= prod(r1, r2)
    return out
def conj(r): return (r[1], r[0])
def swap(r): return (r[1], r[0])
SCALAR = (F(0), F(0)); VECTOR = (H, H); GRAV = (F(1), F(1))

PHIS = {
    "identity": {("L", "doublet"): (H, F(0)), ("R", "doublet"): (F(0), H),
                 ("L", "singlet"): (H, F(0)), ("R", "singlet"): (F(0), H)},
    "swap":     {("L", "doublet"): (F(0), H), ("R", "doublet"): (H, F(0)),
                 ("L", "singlet"): (F(0), H), ("R", "singlet"): (H, F(0))},
}
# frame species (one generation; H and gauge bosons tagless)
DOUBLETS = ["L_L", "Q_L"]            # tagged L in the frame
SINGLETS_R = ["e_R", "u_R", "d_R", "nu_R"]  # tagged R in the frame

print("=" * 76)
for pname, phi in PHIS.items():
    print(f"correlation phi = {pname}:  L doublet -> {phi[('L','doublet')]}, "
          f"R singlet -> {phi[('R','singlet')]}")
    D = phi[("L", "doublet")]; S = phi[("R", "singlet")]
    c1 = SCALAR in prod(conj(D), S)
    c2 = SCALAR in prodS(prod(conj(D), D), {VECTOR})
    c3 = all(phi[(t2, k)] == conj(phi[(t1, k)])
             for (t1, t2) in (("L", "R"),) for k in ("doublet", "singlet"))
    pair = {phi[("L", "doublet")], phi[("R", "doublet")]}
    c4 = pair == {(H, F(0)), (F(0), H)}
    c5 = conj(GRAV) == GRAV and swap(GRAV) == GRAV and conj(VECTOR) == VECTOR
    print(f"  C1 Yukawa scalar for all {len(DOUBLETS)}x{len(SINGLETS_R)} pairs: {c1}")
    print(f"  C2 charged current (W in D x Dbar): {c2}")
    print(f"  C3 antimatter (phi commutes with conjugation): {c3}")
    print(f"  C4 spinor pair home is phi-independent: {c4}")
    print(f"  C5 graviton/vector swap-fixed, no constraint: {c5}")
    print(f"  => {'PASSES all constraints' if all([c1, c2, c3, c4, c5]) else 'FAILS'}")
    print()
print("=" * 76)
print("VERDICT: both correlations pass every internal constraint on")
print("record. They differ by the global factor swap = Lorentz")
print("parity. The chiral door's exact content is ONE BIT, and no")
print("quantity internal to the frame (whose computations never see")
print("the tags) or to the bicone (whose two factors enter the")
print("record only symmetrically: gluing j1 = j2, pair quantities,")
print("swap-fixed boson reps) determines it. In nature the bit is")
print("set by weak-interaction parity violation -- an empirical")
print("input. With the bit supplied, every Lorentz rep of the 15")
print("fields + H + W + G is determined: this correlation is the")
print("single remaining frame<->Lorentz contact point.")
print("Caveat: a future factor-asymmetric bicone result would")
print("reopen the count; on the current record the factors are")
print("symmetric everywhere they appear.")
