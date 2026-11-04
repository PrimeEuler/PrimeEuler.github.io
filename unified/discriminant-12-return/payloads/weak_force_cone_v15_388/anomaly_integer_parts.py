"""
Opening the next doors (2026-11-04, sandbox).

0. TIGHTENING (a correction to the k=3 section's wording): the k=3
   object carries TWO additive Z3 gradings, and the embedding uses
   the second one:
     (i)  irrep triality of the (N,0) shell: N mod 3 (equivalently
          z mod 3 -- every branching component of a shell shares it);
     (ii) the SPLIT grading: with the modes split (pair | third), the
          third mode's own Z3 phase diag(1,1,omega) grades states by
          c mod 3. It commutes with the pair SU(2), with N and with z,
          and c = (N - z)/3 exactly.
   The SM tau slot is filled by (ii), not (i): tabulated below. The
   closure is unaffected (the congruence checks always used tau as
   the split grading via c = tau), but "triality of the shell irrep"
   was the wrong name for what the embedding uses.

1. INTEGER PARTS VIA THE ANOMALY SYSTEM. Frame output so far:
   Y_i = r_i + 2 n_i, with r_i the forced residue mod 2 and n_i in Z
   unknown. Impose the SM's per-generation anomaly conditions on the
   five fermion multiplets (weights are the standard ones; the 3s are
   the color multiplicity -- imported, with the k=3 list length as
   its candidate native source):
     (a) [SU3]^2 U1:  2 Y_Q - Y_u - Y_d = 0
     (b) [SU2]^2 U1:  3 Y_Q + Y_L = 0
     (c) [grav]^2 U1: 6 Y_Q + 2 Y_L - 3 Y_u - 3 Y_d - Y_e = 0
     (d) [U1]^3:      6 Y_Q^3 + 2 Y_L^3 - 3 Y_u^3 - 3 Y_d^3 - Y_e^3 = 0
   Solve exactly. Then anchor and mirror-resolution, then Yukawa
   ties for H and the singlet.

2. GENERATIONS PROBE: the frame's outputs (n2, tau, Y mod 2) under
   c -> c + 3 -- a generation-blind direction, matching the SM's
   generation-universal hypercharges. Count and masses untouched.
"""
from fractions import Fraction
import sympy as sp

M = {  # name: (j, Y_SM, tau_SM)
    "L_L":    (Fraction(1, 2), Fraction(-1),    0),
    "Q_L":    (Fraction(1, 2), Fraction(1, 3),  1),
    "H":      (Fraction(1, 2), Fraction(1),     0),
    "e_R":    (Fraction(0),    Fraction(-2),    0),
    "u_R":    (Fraction(0),    Fraction(4, 3),  1),
    "d_R":    (Fraction(0),    Fraction(-2, 3), 1),
    "singlet": (Fraction(0),   Fraction(0),     0),
    "W":      (Fraction(1),    Fraction(0),     0),
}

print("=" * 76)
print("0. Two Z3 gradings on the embedded multiplets: which one is tau?")
print("=" * 76)
for name, (j, Y, tau) in M.items():
    NA = int(2 * j); c = tau; N = NA + c; z = NA - 2 * c
    irrep_tau = N % 3
    split_tau = c % 3
    c_check = Fraction(N - z, 3)
    print(f"  {name:>8}: shell N={N}, z={z}: irrep triality N mod 3 = {irrep_tau}; "
          f"split grading c mod 3 = {split_tau}; SM tau = {tau}; "
          f"c = (N-z)/3 = {c_check} (exact: {c_check == c})")
print("  -> the operative grading is the SPLIT grading c mod 3 (the third")
print("     mode's Z3 phase in the 2+1 split). Correction filed with this run.")

print()
print("=" * 76)
print("1. Anomaly system in frame variables")
print("=" * 76)
a = sp.symbols('a', integer=True)   # n_Q: Y_Q = 1/3 + 2a
# Linear equations (a),(b),(c) solved by hand-checkable algebra:
#   (b): 3 Y_Q + Y_L = 0 and Y_L = 1 + 2b  ->  b = -1 - 3a
#   (a): u + d = 2a - 1   (writing Y_u = 4/3 + 2u, Y_d = 4/3 + 2d)
#   (c): e = -1 - 6a      (writing Y_e = 2e)
b_ = -1 - 3 * a
e_ = -1 - 6 * a
t = 2 * a + sp.Rational(1, 3)       # = Y_Q
YQ, YL, Ye = t, -3 * t, -6 * t
# cubic (d) reduces to w^2 = 9 t^2 for w = u - d:
w = sp.symbols('w')
m = t  # common part of Y_u, Y_d: Y_u = m + w, Y_d = m - w
cubic = 6 * YQ**3 + 2 * YL**3 - 3 * ((m + w)**3 + (m - w)**3) - Ye**3
cubic_simpl = sp.expand(cubic)
print(f"  cubic (d) with linear solutions substituted: {cubic_simpl} = 0")
sol_w = sp.solve(sp.Eq(cubic_simpl, 0), w)
print(f"  -> w = u - d solves to: {sol_w}   (so w = +/- 3t, t = Y_Q = 2a + 1/3)")
print("  Full anomaly-free family (exact, all four equations):")
print("    Y = t * (Q: 1, L: -3, u: 4, d: -2, e: -6),  t = 2a + 1/3, a in Z,")
print("    plus the u<->d mirror (w -> -w). Ratios are FORCED; the scale t")
print("    is not -- anomalies are homogeneous. Verified numerically:")
for a_val in range(-2, 3):
    tt = Fraction(2 * a_val) + Fraction(1, 3)
    for mirror in (1, -1):
        Y = {"Q_L": tt, "L_L": -3 * tt,
             "u_R": (4 if mirror == 1 else -2) * tt,
             "d_R": (-2 if mirror == 1 else 4) * tt,
             "e_R": -6 * tt}
        eqs = [2 * Y["Q_L"] - Y["u_R"] - Y["d_R"],
               3 * Y["Q_L"] + Y["L_L"],
               6 * Y["Q_L"] + 2 * Y["L_L"] - 3 * Y["u_R"] - 3 * Y["d_R"] - Y["e_R"],
               6 * Y["Q_L"]**3 + 2 * Y["L_L"]**3 - 3 * Y["u_R"]**3
               - 3 * Y["d_R"]**3 - Y["e_R"]**3]
        assert all(v == 0 for v in eqs), (a_val, mirror, eqs)
    print(f"    a={a_val:+d}: t={tt}, all four anomaly equations vanish (both mirrors)")

print()
print("  ANCHOR: the cone's own native lepton shell (pass 1) has Y_L = -1")
print("  exactly -- its spectrum is {0,-1}, it contains a neutral member:")
for a_val in range(-2, 3):
    tt = Fraction(2 * a_val) + Fraction(1, 3)
    print(f"    a={a_val:+d}: Y_L = {-3 * tt}, neutral component in L? {-3 * tt == -1}")
print("  -> a = 0 uniquely. Mirror: Q_L's T3=+1/2 component has charge")
print("     1/2 + t/2 = 2/3; the singlet carrying charge 2/3 (Y = 4/3) is u_R,")
print("     so w = +3t (unmirrored). Full fermion table = SM, uniquely.")
print("  YUKAWA TIES (gauge invariance of the Yukawa terms):")
YL, YQ, Ye, Yu, Yd = Fraction(-1), Fraction(1, 3), Fraction(-2), Fraction(4, 3), Fraction(-2, 3)
YH_from_e = YL - Ye; YH_from_d = YQ - Yd; YH_from_u = Yu - YQ
print(f"    Y_H from L-e: {YH_from_e}; from Q-d: {YH_from_d}; from Q-u: {YH_from_u}"
      f"  -> all equal: {YH_from_e == YH_from_d == YH_from_u} (Y_H = 1, the SM value)")
print(f"    Y_singlet (nu_R) from L + H: {YL + YH_from_e} (= 0, the SM value)")
print("    W: Y = 0 by the gauge-multiplet definition (adjoint of SU(2)_L).")

print()
print("=" * 76)
print("2. Generations probe: c -> c + 3 leaves every frame output invariant")
print("=" * 76)
for name, (j, Y, tau) in M.items():
    NA = int(2 * j); n2 = int(2 * j) % 2
    outs = set()
    for g in range(3):
        c = tau + 3 * g
        frac = (-Fraction(c % 3, 3) - Fraction(n2, 2)) % 1
        outs.add((n2, c % 3, frac == (Y / 2) % 1))
    print(f"  {name:>8}: (n2, tau, Y-frac match) identical for g=0,1,2: {len(outs) == 1}")
print("  -> the frame has an exact generation direction: shells repeat every")
print("     3 in c with identical (parity, grading, Y mod 2) -- matching the")
print("     SM's generation-universal hypercharges. WHY 3 generations, and")
print("     their masses/mixing: untouched.")
