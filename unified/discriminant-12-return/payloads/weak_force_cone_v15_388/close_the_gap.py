"""
Closing the gap (2026-11-04, sandbox).

The gap as filed: each SM multiplet needs a k=3 shell residue
tau = N_3 mod 3 (quarks 1, non-quarks 0), and the embedding of the
weak multiplets into the k=3 AM-GM object was not built. Three steps:

 1. BOUNDARY (negative, exact): tau is NOT a function of the k=2
    labels. The multiplets (L_L, Q_L, H) share (j, N_A, chirality,
    dim) = (1/2, 1, L, 2) but carry tau = (0, 1, 0); (e_R, u_R, d_R)
    share (0, 0, R, 1) but carry tau = (0, 1, 1). Any derivation of
    tau from weak-side data alone is refuted by these collisions.
    Tau is the second sector's own datum -- the gap's content was
    precisely the sector's existence, and the sector is the k=3
    AM-GM member.

 2. MINIMAL EMBEDDING (positive): read a k=3 shell state by its
    mode split (pair modes a,b | third mode c). A state with pair
    occupation N_A = a+b and third-mode occupation c sits in shell
    N = N_A + c, has pair spin j = N_A/2, U(1)_3 charge
    z = N_A - 2c, and triality contribution c mod 3. Embedding rule:
    c = tau (smallest shell with the required residue). Verified:
    every multiplet's (j, c) slot actually occurs in shell
    N = N_A + tau, with pair-state count exactly 2j+1.

 3. WHAT THE COMBINED FRAME FORCES: with (n2, tau) the congruence
    forces y mod 1, i.e. Y mod 2, completely -- checked on all eight
    multiplets. The residual freedom is exactly integer shifts
    Y -> Y + 2Z per field, and it is NOT removable inside the frame:
    (L_L, H) share (j, N_A, c, N, z) = (1/2, 1, 0, 1, 1) with
    Y = -1 vs +1; (u_R, d_R) share (0, 0, 1, 1, -2) with
    Y = 4/3 vs -2/3. In the SM that integer part is what anomaly
    cancellation fixes; the cone's symmetries are global, so no
    anomaly machinery exists here yet. The thirds gap closes;
    the integer gap is a different, older gap, now isolated exactly.
"""
from fractions import Fraction
from collections import defaultdict

# name: (j, Y, chirality, tau)
M = {
    "L_L":    (Fraction(1, 2), Fraction(-1),    "L", 0),
    "Q_L":    (Fraction(1, 2), Fraction(1, 3),  "L", 1),
    "H":      (Fraction(1, 2), Fraction(1),     "S", 0),
    "e_R":    (Fraction(0),    Fraction(-2),    "R", 0),
    "u_R":    (Fraction(0),    Fraction(4, 3),  "R", 1),
    "d_R":    (Fraction(0),    Fraction(-2, 3), "R", 1),
    "singlet": (Fraction(0),   Fraction(0),     "R", 0),
    "W":      (Fraction(1),    Fraction(0),     "V", 0),
}

print("=" * 76)
print("1. Boundary: tau is not a function of the k=2 labels")
print("=" * 76)
by_label = defaultdict(set)
for name, (j, Y, chir, tau) in M.items():
    NA = int(2 * j)
    by_label[(j, NA, chir, NA + 1)].add((name, tau))
for lab, members in sorted(by_label.items()):
    taus = {t for _, t in members}
    if len(members) > 1:
        print(f"  labels (j, N_A, chir, dim) = {lab}: {sorted(members)}"
              f"  -> tau unique? {len(taus) == 1}")
print("  (H is a scalar, chirality tag 'S': even dropping chirality, L_L and")
print("   Q_L share (1/2, 1, 2) with tau 0 vs 1. The singlet trio shares")
print("   everything. No weak-side function gives tau.)")

print()
print("=" * 76)
print("2. Minimal embedding into (N,0) shells: slot (j, c=tau) in shell N = N_A + tau")
print("=" * 76)
def shell_slots(N):
    """(N_A, c) -> (pair state count, z) for k=3 shell N, modes (a,b|c)."""
    slots = {}
    for a in range(N + 1):
        for b in range(N + 1 - a):
            c = N - a - b
            NA = a + b
            cnt, _ = slots.get((NA, c), (0, NA - 2 * c))
            slots[(NA, c)] = (cnt + 1, NA - 2 * c)
    return slots
shells = {N: shell_slots(N) for N in range(5)}
for name, (j, Y, chir, tau) in M.items():
    NA = int(2 * j)
    c = tau
    N = NA + c
    cnt, z = shells[N][(NA, c)]
    print(f"  {name:>8}: j={j}, N_A={NA}, c={c} -> shell N={N}: pair states={cnt} "
          f"(need 2j+1={NA + 1}: {cnt == NA + 1}), z = N_A - 2c = {z}, "
          f"c mod 3 = {c % 3} = tau: {c % 3 == tau}")

print()
print("=" * 76)
print("3. The combined frame forces Y mod 2; the integer part is the boundary")
print("=" * 76)
for name, (j, Y, chir, tau) in M.items():
    n2 = int(2 * j) % 2
    forced_y_frac = (-Fraction(tau, 3) - Fraction(n2, 2)) % 1
    ok = (Y / 2) % 1 == forced_y_frac
    print(f"  {name:>8}: Y mod 2 = {Y % 2}, from (n2={n2}, tau={tau}): "
          f"2*forced = {2 * forced_y_frac}, match: {ok}")
print("  Residual collisions inside the combined frame (same j, N_A, c, N, z):")
pairs = [("L_L", "H"), ("u_R", "d_R")]
for a_name, b_name in pairs:
    ja, Ya, _, ta = M[a_name]; jb, Yb, _, tb = M[b_name]
    NAa, NAb = int(2 * ja), int(2 * jb)
    za, zb = NAa - 2 * ta, NAb - 2 * tb
    same = (ja, NAa, ta, NAa + ta, za) == (jb, NAb, tb, NAb + tb, zb)
    print(f"  {a_name} vs {b_name}: frame labels equal? {same}; "
          f"Y = {Ya} vs {Yb} (differ by {Ya - Yb}, an integer shift of y by {(Ya - Yb) / 2})")
print()
print("VERDICT: the thirds gap is CLOSED by the minimal embedding -- every")
print("multiplet occupies a real k=3 shell slot, and (parity, triality) then")
print("forces Y mod 2 with zero free parameters. What remains is exactly the")
print("integer part of Y per field: in the SM, anomaly cancellation's job;")
print("here, untouched territory (global symmetries have no anomalies).")
