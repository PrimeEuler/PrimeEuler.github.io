"""
The supply method applied to Door II (2026-11-07, sandbox;
Jeremy: "can we apply this same method to door 2?")

The method of v15.520: supply one door's empirical datum,
complete the framework on top of it, and scan downstream for
a selection. Supplying Door I's bit selected a floor at Door
II. This build supplies Door II instead -- the generation
integer itself, N_g = 3 as measured -- and scans the only
downstream the integer touches: Door III's running couplings
(the beta vector is a function of N_g, v15.429), plus two
retro-checks (does the supplied count select the bit back?
does it fix any value in the mixing sector it completes?).

Machinery: the Door III anatomy's own (couplings_door_
anatomy.py, v15.429), reused exactly -- the per-generation
fermion index sums from the closed label table (f1 = f2 =
f3 = 2 in the equal-index normalization), the Higgs-doublet
terms, the same imported mZ inputs, the same one-loop
running. New here: N_g kept symbolic / scanned.

HEADLINE (exact, one loop): every generation contributes
(4/3) N_g to ALL THREE beta coefficients, because the
per-generation trace indices are EQUAL (S = 2, 2, 2 -- the
frame's 5/3 fact of v15.429). The pairwise differences
b_i - b_j are therefore pure gauge+Higgs numbers with ZERO
N_g coefficient -- computed symbolically below -- and the
pairwise crossing scales are exactly independent of N_g.
Consequences, both directions of the method:
 (i) supplying N_g cannot move the crossings: the v15.429
     falsification of exact one-loop unification (three
     distinct scales) holds identically for every count;
 (ii) unification cannot select N_g either: no integer --
     and no real number -- of generations makes the three
     couplings meet at one loop.
The running sector's only count statement is asymptotic
freedom's loose ceiling: b3(N_g) < 0 iff N_g <= 8, far above
the v15.520 squeeze (3 <= N_g <= 3 under its premises).

RETRO-CHECKS: at the supplied N_g = 3, the vectorlike
completion carries N(N-1) = 6 CP phases (v15.520) -- CP
violation at three generations is consistent with BOTH
completions, so the supplied count does not retro-select
Door I's bit. In the lepton sector the supplied count gives
PMNS the mirror counting (one Dirac phase at N_g = 3):
existence of a slot, not a value -- and leptonic CP is not
yet observed in any case.

VERDICT SHAPE: the method reaches exactly as far as the
integer/reals border. It worked at I -> II because a
rigidity predicate (phase existence) speaks about an
INTEGER. At II -> III the target residue is three REALS,
and the one candidate meeting-condition on them provably
does not even see the supplied integer (its N_g coefficient
is exactly zero). Supplying Door II completes real structure
-- the beta vector becomes definite, the loop generation
sums close over the three fold classes -- but a completion
is not a selection: no downstream quantity is fixed that
was not already an input. One-loop scope throughout,
matching the door anatomy's grade; two-loop running shifts
the crossings but is outside the anatomy's machinery.
"""
from fractions import Fraction as F
import numpy as np
import sympy as sp

# per-generation fermion index sums (LH Weyl), from the closed
# label table -- couplings_door_anatomy.py's f1, f2, f3.
F3 = F(2)   # SU(3): Q_L components x T(fund)
F2 = F(2)   # SU(2): color multiplicity x T(doublet)
F1 = F(2)   # U(1)_yhat: S_(Y/2) * (3/5) = (10/3)(3/5)

def betas(Ng):
    b3 = F(-11) + F(2, 3) * Ng * F3
    b2 = F(-22, 3) + F(2, 3) * Ng * F2 + F(1, 3) * F(1, 2)
    b1 = F(2, 3) * Ng * F1 + F(1, 3) * (2 * F(3, 5) * F(1, 2) ** 2)
    return b1, b2, b3

print("=" * 76)
print("1. the beta vector as a function of the supplied integer (exact)")
print("=" * 76)
for Ng in (0, 1, 2, 3, 4, 8, 9):
    b1, b2, b3 = betas(Ng)
    print(f"  N_g={Ng}: (b1, b2, b3) = ({b1}, {b2}, {b3})")
b1, b2, b3 = betas(3)
assert (b1, b2, b3) == (F(41, 10), F(-19, 6), F(-7))
print("  N_g=3 reproduces the v15.429 vector (41/10, -19/6, -7).")
print("  asymptotic freedom: b3 < 0 iff N_g <= 8 "
      f"(b3(8) = {betas(8)[2]}, b3(9) = {betas(9)[2]}) -- the running")
print("  sector's only count statement, a loose ceiling far above "
      "the squeeze.")

print()
print("=" * 76)
print("2. pairwise differences: the N_g coefficient is EXACTLY ZERO")
print("=" * 76)
n = sp.symbols("n")
b1s = sp.Rational(4, 3) * n + sp.Rational(1, 10)
b2s = sp.Rational(4, 3) * n - sp.Rational(43, 6)
b3s = sp.Rational(4, 3) * n - 11
for nm, d in (("b1-b2", b1s - b2s), ("b1-b3", b1s - b3s), ("b2-b3", b2s - b3s)):
    assert sp.expand(d).coeff(n) == 0
    print(f"  {nm} = {d}   (coefficient of N_g: 0, exactly)")
print("""  reason, from the table: each generation adds (2/3)*f_i to b_i
  with f = (2, 2, 2) in the equal-index normalization -- the
  frame's trace indices are equal per generation (v15.429), so
  the generation contribution is a common shift and cancels in
  every difference. What survives is gauge + Higgs only.""")

print()
print("=" * 76)
print("3. crossing scales vs N_g: invariant (v15.429 inputs, one loop)")
print("=" * 76)
MZ = 91.1876
ainv, s2w, als = 127.951, 0.23122, 0.1179      # imported, as v15.429
ai = [(3 / 5) * ainv * (1 - s2w), ainv * s2w, 1 / als]
print(f"  alpha_i^-1(mZ) = ({ai[0]:.2f}, {ai[1]:.2f}, {ai[2]:.2f}) [imported]")
ref = None
for Ng in (1, 2, 3, 4, 5, 6):
    bb = [float(x) for x in betas(Ng)]
    scales = []
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        t = 2 * np.pi * (ai[i] - ai[j]) / (bb[i] - bb[j])
        scales.append(MZ * np.exp(t))
    if ref is None:
        ref = scales
    assert all(abs(s / r - 1) < 1e-12 for s, r in zip(scales, ref))
    print(f"  N_g={Ng}: crossings at "
          + ", ".join(f"{s:.2e}" for s in scales) + " GeV")
print(f"  identical for every N_g (asserted to 1e-12); the extreme")
print(f"  crossings differ by a factor {ref[2]/ref[0]:.2e} at EVERY count:")
print("  no generation count -- integer or real -- unifies the")
print("  couplings at one loop, and supplying the count moves")
print("  nothing downstream. The v15.429 falsification is promoted")
print("  from 'at N_g=3' to 'at all N_g, exactly'.")

print()
print("=" * 76)
print("4. retro-checks: the supplied count selects nothing back")
print("=" * 76)
Ng = 3
ph_chiral = (Ng - 1) * (Ng - 2) // 2
ph_vector = Ng * (Ng - 1)
print(f"  CP phases at N_g=3 (v15.520 exact counts): chiral {ph_chiral}, "
      f"vectorlike {ph_vector}.")
print("  Both completions violate CP at three generations, so CP +")
print("  the supplied count does not retro-select Door I's bit.")
assert ph_chiral == 1 and ph_vector == 6
print("  PMNS mirror counting at N_g=3: one Dirac phase slot exists")
print("  (existence, not a value; leptonic CP unobserved to date).")
print("  What the supply DOES complete -- not select: the beta vector")
print("  is definite (sec.1); loop generation sums close over the")
print("  three fold classes with weights still imported (v15.394);")
print("  the Koide/m_tau fingerprint becomes a statement inside a")
print("  fully supplied sector (H2's test, unchanged).")

print()
print("=" * 76)
print("VERDICT -- the method's reach ends at the integer/reals border")
print("=" * 76)
print("""  Applied faithfully to Door II, the supply method finds NO
  new selection -- and locates exactly why. The I -> II step
  worked because a rigidity predicate (CP-phase existence)
  connects the supplied bit to an INTEGER, the species such
  predicates can output. Downstream of Door II the residue is
  Door III's three REALS; the sole candidate condition on
  them -- a common meeting under the running -- is exactly
  N_g-invariant (sec.2), so it neither selects the count nor
  is moved by supplying it. Supplying Door II completes the
  framework's running and its loop sums, and completes is
  all it does: no value downstream is fixed that was not
  already an input. The doors' species table (one bit, one
  integer, three reals) is also the supply method's range
  table: it transmits selections between the discrete doors
  and stops at the continuous one.""")
