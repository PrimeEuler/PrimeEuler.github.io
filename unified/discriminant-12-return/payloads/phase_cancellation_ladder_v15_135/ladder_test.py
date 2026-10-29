"""
Phase-cancellation / parabolic-ladder lattice test (sandbox, 2026-10-29).

Jeremy's idea under test: EM created the 1/4 lattice, gravity is the residue
of a phase cancellation between EM channels.

Three levels are kept separate throughout (hbar = 1):
  P  pair product     EM: P = eg in (1/2)Z.   TN: P = eps*l in (1/4)Z.
  S  HJ twist         s_EM = P (MIC coefficient of cos th);
                      s_TN = 2*P (TN coefficient is 2*eps*l). Both in (1/2)Z.
  R  parabolic seats  roots r_pm = (k -/+ s)/2, charges r_pm^2 (mic_sep.py).

Questions:
  Q1  Can centre/offset coordinates of two EM half-lattice variables reach
      the quarter lattice, and under what cancellation condition do the ODD
      quarters survive?
  Q2  Can any combination of two EM twists s1, s2 in (1/2)Z produce the TN
      twist/factorisation structure, or does the quarter live only in the
      Misner fiber factorisation s = 2*eps*l?
  Q3  Is the parabolic ladder (MIC separation) itself sensitive to how s is
      quantised? (If it separates for symbolic s, the ladder is s-blind and
      the lattice is imported from fiber single-valuedness, not created by
      the ladder.)
"""
from fractions import Fraction as F
import sympy as sp

print("=" * 72)
print("PART 0 -- the parabolic ladder is s-blind (symbolic separation)")
print("=" * 72)
# MIC separation with symbolic s (core of nut-pair-test/mic_sep.py).
xi, eta = sp.symbols('xi eta', positive=True)
k, s, E, kap = sp.symbols('k s E kap')
Up, Vp = sp.symbols('Up Vp')
r = (xi + eta) / 2
cth = (xi - eta) / (xi + eta)
sth2 = xi * eta / r**2
pr = (1 + cth) * Up + (1 - cth) * Vp
pth = sp.sqrt(xi * eta) * (Vp - Up)
HJ = pr**2 + (pth**2 + (k + s * cth) ** 2 / sth2) / r**2 + s**2 / r**2 - 2 * kap / r - 2 * E
mult = sp.expand(sp.simplify(sp.together(HJ)) * (xi + eta) / 4)
A = xi * Up**2 + ((k - s) / 2) ** 2 / xi - E * xi / 2
B = eta * Vp**2 + ((k + s) / 2) ** 2 / eta - E * eta / 2
resid = sp.simplify(mult - (A + B - kap))
print("MIC split residual (symbolic s):", resid, "-> separation holds for ANY s")

# TN vs MIC sector identity (core of nut-pair-test/tn_sector.py).
rr, th = sp.symbols('r th', positive=True)
l, m, eps = sp.symbols('l m eps')
prv, pthv = sp.symbols('pr pth')
Sig = rr**2 + l**2
f = (rr**2 - 2 * m * rr - l**2) / Sig
sTN = 2 * l * eps
TN = Sig * f * prv**2 + pthv**2 + (k + 2 * l * eps * sp.cos(th))**2 / sp.sin(th)**2
MIC = rr**2 * prv**2 + pthv**2 + (k + sTN * sp.cos(th))**2 / sp.sin(th)**2 + sTN**2
diff = sp.simplify(TN - MIC)
expect = -(2 * m * rr + l**2) * prv**2 - (2 * l * eps)**2
print("TN-MIC purely radial:", sp.simplify(diff - expect) == 0,
      "-> TN seats are MIC seats at s = 2*eps*l, centre k/2, root offset eps*l")

print()
print("=" * 72)
print("PART 1 -- dyadic pair theorem: centre/offset of two half variables")
print("=" * 72)
# A = p/2, B = q/2 (two EM half-lattice variables). C = (A+B)/2, X = (A-B)/2.
# Claim: 4C, 4X integers of the SAME parity (checkerboard quarter lattice).
bad = 0
classes = {}
for p in range(-16, 17):
    for q in range(-16, 17):
        A_, B_ = F(p, 2), F(q, 2)
        C, X = (A_ + B_) / 2, (A_ - B_) / 2
        if (4 * C).denominator != 1 or (4 * X).denominator != 1 or (4 * C - 4 * X) % 2 != 0:
            bad += 1
        key = ('same-parity' if (p - q) % 2 == 0 else 'opposite-parity',
               'C,X in (1/2)Z' if C.denominator <= 2 else 'C,X odd quarters')
        classes[key] = classes.get(key, 0) + 1
print("checkerboard violations:", bad)
for kk in sorted(classes):
    print("  ", kk, "->", classes[kk], "pairs")
print("odd-quarter example: A=1/2, B=0 -> C=1/4, X=1/4 (both raw vars are EM-legal)")

print()
print("=" * 72)
print("PART 2 -- cancellation conditions: which centre leaves odd-quarter X?")
print("=" * 72)
# Group by C mod 1; record the set of X mod 1 values that occur.
from collections import defaultdict
tab = defaultdict(set)
for p in range(-32, 33):
    for q in range(-32, 33):
        A_, B_ = F(p, 2), F(q, 2)
        C, X = (A_ + B_) / 2, (A_ - B_) / 2
        tab[C % 1].add(X % 1)
for cmod in sorted(tab):
    xs = sorted(tab[cmod])
    odd = any(x.denominator == 4 for x in xs)
    print(f"  centre C mod 1 = {str(cmod):>4}:  X mod 1 in {[str(x) for x in xs]}"
          f"   odd quarters survive: {odd}")
print("exact cancellation C = 0 forces X = A in (1/2)Z: odd quarters KILLED.")
print("odd-quarter offsets survive IFF the centre itself carries an odd-quarter")
print("holonomy (opposite-parity pair). Cancellation alone does not choose this.")

print()
print("=" * 72)
print("PART 3 -- twist combination rules vs the TN structure")
print("=" * 72)
halves = [F(i, 2) for i in range(-4, 5)]
def denoms(vals):
    return sorted({v.denominator for v in vals})
sums = [a + b for a in halves for b in halves]
diffs = [a - b for a in halves for b in halves]
halfdiffs = [(a - b) / 2 for a in halves for b in halves]
print("s1 + s2 denominators:", denoms(sums), " (stays in (1/2)Z: (1/2)Z is a group)")
print("s1 - s2 denominators:", denoms(diffs), " (stays in (1/2)Z)")
print("(s1 - s2)/2 denominators:", denoms(halfdiffs), " (reaches (1/4)Z -- offset coordinate)")
# Seat root offsets = s/2 for each candidate effective twist.
def root_offset_denoms(twists):
    return denoms([t / 2 for t in twists])
print("root offset s/2, EM/TN twists in (1/2)Z:", root_offset_denoms(halves))
print("root offset s/2, half-difference twists:", root_offset_denoms(halfdiffs),
      " -> EIGHTH lattice at seat level: rule overshoots, not in the record")
# Minimal-twist seat comparison: EM s = 1/2 vs TN eps*l = 1/4 (s = 2*eps*l = 1/2).
def seats(kk, ss):
    return sorted({((kk - ss) / 2) ** 2, ((kk + ss) / 2) ** 2})
em_seats = set()
tn_seats = set()
for kk in range(0, 5):
    em_seats.update(seats(F(kk), F(1, 2)))          # EM: s = eg = 1/2
    tn_seats.update(seats(F(kk), 2 * F(1, 4)))      # TN: s = 2*eps*l, eps*l = 1/4
print("minimal-twist seat charges EM (s=1/2) == TN (eps*l=1/4):", em_seats == tn_seats)
print("  -> the parabolic seats cannot see the quarter; it is in the FACTORISATION")
print("     s = 2*eps*l (state x coupling), not in the twist or the seats.")

print()
print("=" * 72)
print("PART 4 -- the fiber benchmark an EM-only mechanism would have to match")
print("=" * 72)
for n in range(0, 5):
    eps_n = F(n, 4)  # eps_n * l / hbar, from Misner period 8*pi*l: eps_n = n*hbar/(4l)
    print(f"  Misner rung n={n}: eps*l = {eps_n}  (quarter lattice, fiber momentum)")
print("EM has no time fiber and no eps: its quarter (Part 1) is a COORDINATE")
print("quarter (centre/offset of a pair). Identifying it with the fiber-product")
print("quarter above is exactly the weld's node=state premise (v14.904),")
print("not a consequence of EM phase algebra alone.")
print()
print("ALL CHECKS DONE")
