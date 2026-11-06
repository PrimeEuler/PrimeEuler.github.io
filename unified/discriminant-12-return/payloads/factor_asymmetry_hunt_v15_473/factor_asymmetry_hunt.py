"""
The factor-asymmetry hunt (2026-11-06, sandbox; door I,
Jeremy's v15.429 bet: "we can find a factor-asymmetric
bicone result when we are ready"; target language from
v15.468: a quantity ODD under the factor exchange would
reopen the one-bit count).

What would count: a swap-odd OUTPUT of the cone's own
structures (mesh, operator, dynamics) -- not a label
(v15.468 already has those), not an imported datum.

Census, each item checked against the record:
 A. THE GRID. Node map (X, Y, T) = ((n-k)/2, sqrt(nk),
    (n+k)/2): swap n<->k sends X -> -X, fixes Y, T; the two
    mesh families exchange; the seat n = k (X = 0) is fixed;
    the node SET is invariant. The grid is an exact mirror
    pair carrying no asymmetry (symbolic check below).
 B. THE OPERATOR. The frozen formula (dm490/far585/kfull/
    DERIVATION.md sec.0-1) gives K_{N,m} = c(m z_N - N z_m)/
    (N^2-m^2) + 2 sigma p_N p_m, d_N real (ln(N/4) + bounded
    cos oscillations), all data real; the file's own sec.1:
    "K_full is a formally symmetric (real) operator."
    A real operator has no handedness in its elements:
    conjugation is trivial, and no phase/screw sense
    propagates into K. (The screw overlay of v13.258 is not
    present in inspectable formula form in the local record;
    whatever its sense, it does not reach K's matrix
    elements. Located gap, stated.)
 C. SECTOR CONTENT. The two parity sectors carry genuinely
    different certified spectral data (v15.227 first gaps:
    odd 0.00415063, even 0.01295802) -- a real asymmetry of
    CONTENT. But the grading is shell parity; per v15.282
    the doublet's home is the odd sector and the factor swap
    acts WITHIN the doublet. Distinguishing sectors is not
    a swap-odd observable: no bearing on the bit.
 D. NATURE'S SIDE-PICKS. Every dynamical asymmetry in the
    record is an occupancy or an arrow, i.e. a datum:
    (i) retardation -- the two-body arc's dynamics uses the
    past cone only (imported with the force laws);
    (ii) NUT charge l = 0 -- the gravitational dyon's
    magnetic side is unoccupied (weld thread, v14.910 memo);
    (iii) the cosmic seat -- Sciama's B = 0.4996 sits at +1/2
    opposite the cone's seat at -1/2 (occupancy);
    (iv) the chiral bit itself (v15.429).
Verdict in the printout: the bet cashes in form but not in
effect -- factor-asymmetric results exist throughout the
record, and every one is the bit's own species (nature
picks a side of a mirror pair the cone supplies). None is
a swap-odd output of the cone's dynamics, so the count
stands; what the hunt adds is the census: the bit is one
of at least four same-shaped side-picks.
"""
import sympy as sp

print("=" * 76)
print("A. the grid under the swap (symbolic)")
print("=" * 76)
n, k = sp.symbols('n k', positive=True)
X, Y, T = (n - k) / 2, sp.sqrt(n * k), (n + k) / 2
Xs, Ys, Ts = (sp.simplify(q.subs({n: k, k: n}, simultaneous=True))
              for q in (X, Y, T))
print(f"  node (X, Y, T) = ((n-k)/2, sqrt(nk), (n+k)/2)")
print(f"  under n<->k: X -> {Xs} (sign flip), Y -> {Ys}, T -> {Ts}")
print(f"  seat n = k: X = {X.subs(k, n)} (fixed). The two mesh families")
print("  (rows x = u, columns y = u) exchange under X -> -X; the node")
print("  set and every seat quantity are invariant: mirror pair,")
print("  no asymmetry carried by the grid.")

print()
print("=" * 76)
print("B-D. the census (record-grounded; see header for sources)")
print("=" * 76)
rows = [
    ("canonical operator K_full", "real symmetric elements (frozen formula)",
     "no handedness in elements; conjugation trivial"),
    ("parity sector gaps (v15.227)", "odd 0.00415063 vs even 0.01295802",
     "content asymmetry; swap acts within the doublet -- no bearing"),
    ("retardation (two-body arc)", "dynamics uses the past cone only",
     "ARROW: imported with the force laws (Sommerfeld)"),
    ("NUT charge (weld thread)", "l = 0 in all bounds",
     "OCCUPANCY: magnetic side of the dyon unoccupied"),
    ("cosmic seat (Sciama B)", "+0.4996 measured; cone seat at -1/2",
     "OCCUPANCY: nature sits on the + side of the pair"),
    ("meson sigma9 doublets (v15.468)", "K0<->K0bar etc. exchanged by sigma -> -sigma",
     "LABELS: swap structure exact, seat swap-blind (filed)"),
    ("the chiral bit (v15.429)", "one bit, set by parity violation",
     "THE DATUM ITSELF"),
]
for a, b, c in rows:
    print(f"  {a:34s} {b:44s} {c}")
print()
print("  screw overlay (v13.258/v13.285): not inspectable in local")
print("  formula form; per (B) its sense cannot reach K's elements.")

print()
print("=" * 76)
print("VERDICT")
print("=" * 76)
print("Jeremy's bet cashes in form: factor-asymmetric bicone")
print("results are all over the record. It does not cash in")
print("effect: every one is an occupancy or an arrow -- nature")
print("picking a side of a mirror pair the cone supplies --")
print("which is the bit's own species, not a cone output that")
print("is odd under the swap. The cone's own structures (grid,")
print("operator, sectors) are mirror-exact or content-graded,")
print("never swap-odd. Door I therefore stands at one bit,")
print("with a sharpened picture: the bit is one of at least")
print("four same-shaped side-picks in the record (retardation,")
print("NUT, cosmic seat, chirality) -- the machinery's recurring")
print("transaction with nature is: it supplies the pair, she")
print("picks the side. A genuinely reopening result would need")
print("a swap-odd DYNAMICAL output; the two places one could")
print("still hide are the screw overlay's sense (not locally")
print("inspectable, and screened from K by reality) and the")
print("absent factor<->mode dictionary (v15.468 sec.4).")
