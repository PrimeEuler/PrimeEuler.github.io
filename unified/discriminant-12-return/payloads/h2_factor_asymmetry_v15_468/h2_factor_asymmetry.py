"""
Hitting H2, and factor asymmetry from the machinery
(2026-11-06, sandbox; Jeremy: "lets hit H2, also, it seems
like we could get factor asymmetry out of this").

PART A -- H2 (the fold, v15.461, needs a sector that reads
the generation digit). Such a sector is exactly a CLASS
FUNCTION: values on slots factoring through the address
class mod 18 (equal on same-class slots -- in particular a
4th replica, g=3, would duplicate g=0's value), and not
through the mod-6 shadow alone. Tests run here:
 A2. the loop sector (v15.394 sec.4c) IS reader-shaped: its
     sums run over the tower with per-class weights; under
     the fold the completeness sum is over exactly 3 classes;
 A3. nature's one exact three-class relation: the Koide
     combination for charged leptons equals 2/3 -- the cone's
     native parabola constant (v14.592) -- to ~1e-5, inside
     the tau-mass uncertainty; the quark sectors FAIL it
     (running masses, indicative values): if this is a digit
     sector's fingerprint, it is lepton-shaped, not universal;
 A4. negative: the canonical operator side cannot currently
     be asked -- no dictionary maps frame addresses (Schwinger
     labels N_A, c) to canonical lattice modes; the two label
     systems share no symbols. The fold is frame-side only.

PART B -- factor asymmetry from the pair machinery. On the
doubled k=3, a composite carries signed classes (a, b) on the
(L, R) lists. Factor swap acts with conjugation,
S(a, b) = (-b, -a), and the pair coordinates split by parity:
sigma = a + b is swap-ODD, delta = a - b is swap-EVEN. The
mesons form swap doublets at fixed delta, exchanged by
sigma -> -sigma, with the seat sigma = 0 exactly the
flavor-diagonal pairs. So inside this machinery the factor
swap is a measurable involution on labeled composites -- the
pair sectors hold factor asymmetry as labeled structure
(verdict and limits in the printout; the door-I translation
is a reading, marked as such).
"""
from fractions import Fraction as F
import math

print("=" * 76)
print("A2. loop sums as class sums (reader shape, weights imported)")
print("=" * 76)
w = {0: F(3), 1: F(5), 2: F(7)}          # dummy per-class weights
slots = sum(w[g % 3] for g in range(4))  # tower slots g = 0..3
classes = sum(w[g] for g in range(3))
print(f"  with class-function weights, a sum over tower slots g=0..3")
print(f"  counts class 0 twice ({slots} vs class sum {classes}): under")
print("  the fold, loop completeness is over 3 classes; a 4th replica")
print("  would duplicate a term, not add one. (Shape only -- the")
print("  physical weights are CKM/masses, imported: v15.394 sec.4c.)")

print()
print("=" * 76)
print("A3. the Koide combination: nature's exact three-class relation?")
print("=" * 76)
def koide(m1, m2, m3):
    return (m1 + m2 + m3) / (math.sqrt(m1) + math.sqrt(m2) + math.sqrt(m3)) ** 2
lep = koide(0.51099895, 105.6583755, 1776.86)          # PDG pole masses, MeV
up = koide(2.16, 1270.0, 172690.0)                     # indicative
down = koide(4.67, 93.4, 4180.0)                       # indicative
print(f"  charged leptons: Q = {lep:.6f}   vs 2/3 = {2/3:.6f}   "
      f"(diff {abs(lep - 2/3):.1e})")
print(f"  up-type quarks:  Q = {up:.6f}   down-type quarks: Q = {down:.6f}")
print("  the lepton value hits the cone's own 2/3 (v14.592: the")
print("  parabola constant, already proven the wrong TYPE for a")
print("  charge -- here the type is right: a mass-sector relation")
print("  among exactly the three classes). Quark sectors fail it.")
print("  Filed as a located coincidence of the right type, at")
print("  coincidence grade -- not a derivation of any mass.")

print()
print("=" * 76)
print("B. factor asymmetry: swap parity of pair coordinates (fold digits)")
print("=" * 76)
# meson = (name, a, b): a = tau + 3g of the quark (tau = 1), b = -(tau + 3g')
MES = [("pi", 1, -1), ("K0", 1, -4), ("K0bar", 4, -1), ("B0", 1, -7),
       ("B0bar", 7, -1), ("Bs", 4, -7), ("Bsbar", 7, -4)]
def S(a, b): return (-b % 9, -a % 9)
inv_ok = True
table = {}
for name, a, b in MES:
    a9, b9 = a % 9, b % 9
    sig, dl = (a9 + b9) % 9, (a9 - b9) % 9
    table[name] = (sig, dl)
    sp = S(a9, b9)
    inv_ok &= (S(*sp) == (a9, b9))
    print(f"  {name:6s} (a, b) = ({a9}, {b9}):  sigma9 = {sig}, delta9 = {dl}"
          f"{'   <-- SEAT' if sig == 0 else ''}")
pairs = [("K0", "K0bar"), ("B0", "B0bar"), ("Bs", "Bsbar")]
pair_ok = all(table[x][1] == table[y][1] and (table[x][0] + table[y][0]) % 9 == 0
              for x, y in pairs)
print(f"  S is an involution: {inv_ok};  swap doublets share delta9 and")
print(f"  negate sigma9: {pair_ok};  the seat sigma9 = 0 is S-fixed")
print("  (flavor diagonal = balanced pair = condensate channel).")

print()
print("=" * 76)
print("VERDICTS")
print("=" * 76)
print("H2: NOT discharged, but its search space is now exact.")
print("A digit reader must be a class function on Z18 addresses;")
print("the canonical side cannot yet be asked (no frame<->mode")
print("dictionary); the loop sector has the reader's shape with")
print("imported weights; and nature's single exact relation")
print("among the three generation masses (Koide, leptons) lands")
print("on the frame's own constant 2/3 -- the right type of")
print("fingerprint, at coincidence grade, lepton sector only.")
print()
print("FACTOR ASYMMETRY: the machinery holds it as labeled")
print("structure. In the doubled k=3 the factor swap is a")
print("measurable involution on composites: off-seat pairs split")
print("into two distinct classes exchanged by the swap (K0 vs")
print("K0bar are different particles carrying opposite sigma9),")
print("and only the balanced seat is swap-blind. [I] Reading for")
print("door I: a Spin(4) fermion pair {(1/2,0),(0,1/2)} is the")
print("maximally off-seat object of its pair space (one factor")
print("carries the doublet, the other nothing) while every boson")
print("is a seat rep (j, j); the chiral bit is the SIGN of that")
print("displacement -- a coordinate this machinery elsewhere")
print("realizes as a physical label. The sign itself is still")
print("nature's datum: asymmetry has a home here, not a source.")
