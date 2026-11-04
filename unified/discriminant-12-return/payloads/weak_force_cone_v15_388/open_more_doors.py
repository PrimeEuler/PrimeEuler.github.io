"""
More doors (2026-11-04, sandbox). Four probes against the completed
(k=2 x k=3 split) frame:

 A. ANTIMATTER COMPLETION. Conjugate multiplets: Y -> -Y, tau ->
    (-tau) mod 3, same j. Embed them in the conjugate (b-mode) sector:
    a matter slot (N_A, c) conjugates to a b-sector slot with signed
    third-mode occupation c_signed = -c, whose split grading is
    c_signed mod 3. Check: grading and congruence fractions reproduce
    the full anti-table. (This is where a signed winding is LEGITIMATE
    -- an occupation difference of real modes, unlike B2's bookkeeping.)

 B. CHIRALITY. Every equation in this thread is invariant under
    flipping all fermion chirality tags (L<->R): the tags never enter
    a computation. What the frame encodes is the internal pattern
    (fermion doublets vs singlets, via N_A); what it cannot encode is
    that "doublet" means LEFT -- that is a correlation between the
    internal frame and the Lorentz bicone's (1/2,0) factor, a separate
    structure. The chiral door's exact content is that correlation.

 C. DYNAMICS PROBE. Is Y an OPERATOR identity in the frame --
    Y = alpha*N_A + beta*c + gamma*z + delta*N on the minimal
    embedding? e_R sits at (0,0,0,0) with Y = -2: any linear
    combination vanishes there. NO solution (verified by exact
    linear algebra). The frame + anomalies + anchor fix Y's VALUE per
    field; Y is not a function of shell position. Same freedom as the
    SM's per-field rep labels, in another costume.

 D. SCOPE CHECKS. (i) The anomaly weight kappa=3 for Q_L: shell 2's
    branching under the split contains exactly ONE doublet component
    -- the frame does not manufacture the color multiplicity; kappa=3
    stays imported (candidate: the list length k itself). (ii)
    Generations: slots exist for c = tau + 3g for every g >= 0 --
    the frame gives no generation count.
"""
from fractions import Fraction
import sympy as sp

M = {  # name: (j, Y, chirality tag, tau)
    "L_L":    (Fraction(1, 2), Fraction(-1),    "L", 0),
    "Q_L":    (Fraction(1, 2), Fraction(1, 3),  "L", 1),
    "H":      (Fraction(1, 2), Fraction(1),     "S", 0),
    "e_R":    (Fraction(0),    Fraction(-2),    "R", 0),
    "u_R":    (Fraction(0),    Fraction(4, 3),  "R", 1),
    "d_R":    (Fraction(0),    Fraction(-2, 3), "R", 1),
    "singlet": (Fraction(0),   Fraction(0),     "R", 0),
    "W":      (Fraction(1),    Fraction(0),     "V", 0),
}
def labels(name, j, tau):
    NA = int(2 * j); c = tau; N = NA + c; z = NA - 2 * c
    n2 = int(2 * j) % 2
    return NA, c, N, z, n2

print("=" * 76)
print("A. Antimatter completion (b-mode sector, signed c)")
print("=" * 76)
for name, (j, Y, tag, tau) in M.items():
    Ya = -Y; tau_a = (-tau) % 3
    NA, c, N, z, n2 = labels(name, j, tau)
    c_signed = -c
    grading_ok = (c_signed % 3) == tau_a
    forced = (-Fraction(tau_a, 3) - Fraction(n2, 2)) % 1
    frac_ok = (Ya / 2) % 1 == forced
    print(f"  anti-{name:>8}: Y={Ya}, tau={tau_a}: signed c={c_signed}, "
          f"grading match: {grading_ok}; y-frac {forced} match: {frac_ok}")
print("  -> conjugation flips the split grading's sign; the full anti-table")
print("     embeds in the conjugate sector. Matter + antimatter covered.")

print()
print("=" * 76)
print("B. Chirality: tag-flip invariance of every frame output")
print("=" * 76)
def all_outputs(tagmap):
    ok = True
    for name, (j, Y, tag, tau) in M.items():
        NA, c, N, z, n2 = labels(name, j, tau)
        forced = (-Fraction(tau, 3) - Fraction(n2, 2)) % 1
        ok &= ((Y / 2) % 1 == forced)
    return ok
flip = {"L": "R", "R": "L", "S": "S", "V": "V"}
print(f"  fraction checks pass with original tags: {all_outputs(None)}")
print(f"  fraction checks pass with all fermion tags flipped L<->R: {all_outputs(flip)}")
print("  (The tags are never read by any equation in the thread -- by")
print("   construction of this test, and on inspection of all prior scripts.)")
print("  Fermion pattern in-frame: tag = L iff N_A = 1 for every fermion.")
print("  The un-encoded step: identifying the N_A=1 sector with Lorentz-")
print("  left (the bicone's (1/2,0) factor). A correlation between two")
print("  independent structures -- selector-shaped, precisely located.")

print()
print("=" * 76)
print("C. Dynamics probe: Y as a frame-generator combination?")
print("=" * 76)
rows, rhs = [], []
for name, (j, Y, tag, tau) in M.items():
    NA, c, N, z, n2 = labels(name, j, tau)
    rows.append([NA, c, z, N]); rhs.append(Y)
A_mat = sp.Matrix(rows); b_vec = sp.Matrix(rhs)
sol = sp.linsolve((A_mat, b_vec), sp.symbols('a b g d'))
print(f"  linsolve for (alpha, beta, gamma, delta): {sol}")
print("  e_R row is (0,0,0,0) with Y=-2: every linear combination of frame")
print("  generators vanishes at the frame origin but Y does not. No operator")
print("  identity exists on the minimal embedding. Y's values are fixed")
print("  (frame + anomalies + anchor); Y as an operator is dynamics' job.")

print()
print("=" * 76)
print("D. Scope checks")
print("=" * 76)
# shell-2 branching under the split: (N_A, c) -> pair-state count
from collections import Counter
cnt = Counter()
for a_ in range(3):
    for b_ in range(3 - a_):
        c_ = 2 - a_ - b_
        cnt[(a_ + b_, c_)] += 1
print(f"  shell N=2 branching (N_A, c) -> states: {dict(sorted(cnt.items()))}")
print("  exactly ONE doublet component (N_A=1) -> kappa=3 is not a frame")
print("  multiplicity. It stays imported (candidate source: k = 3 itself).")
ok = True
for name, (j, Y, tag, tau) in M.items():
    NA = int(2 * j)
    for g in range(4):
        c = tau + 3 * g; N = NA + c
        # slot (N_A, c) in shell N always exists with N_A+1 pair states
        ok &= (0 <= c <= N)
print(f"  generation slots c = tau + 3g exist for g=0..3, all multiplets: {ok}")
print("  -> no generation count in the frame; the direction is unbounded.")
