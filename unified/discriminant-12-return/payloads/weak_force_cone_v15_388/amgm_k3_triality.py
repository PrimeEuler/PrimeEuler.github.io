"""
The 2D+1 AM-GM extension as the triality door (2026-11-04, sandbox).

Jeremy's generalized AM-GM family (ledger v14.818): for a k-list,
nabla^2 P_k = P_k D^{-1}(J-I)D^{-1}, log-coordinate metric of signature
(1, k-1) -- the "1" is the list-sum (radial) direction, the k-1 shape
directions are the SU(k) side. Our cone is k=2: signature (1,1), U(2).
The k=3 member -- signature (1,2), "2D+1" -- is the candidate door.

Why it might succeed where the parabola 2/3 failed: the tests that
killed the earlier candidates were (i) ADDITIVITY (a charge/grading
must be a homomorphism) and (ii) SELECTION (the coefficient must not be
a free family). Triality on the k=3 object is a representation label
of U(3) = (SU(3) x U(1))/Z3, and the AM of a 3-list is S/3 with the
1/3 fixed by the list length. Checks:

 A. 3-mode Schwinger shells: states (n1,n2,n3), N = sum; shell N is
    the symmetric SU(3) irrep (N,0), dimension (N+1)(N+2)/2; the SU(3)
    center Z3 acts on shell N as omega^N, omega = e^{2 pi i /3}:
    triality tau = N mod 3 is an intrinsic label of every state.
 B. Additivity: tau(M (x) N) = (tau_M + tau_N) mod 3 -- a homomorphism
    to Z3. (Contrast: the parabola's (N-1/4)^{2/3} failed additivity
    outright.) Also AM = S/3 is LINEAR in the additive sum S, with
    coefficient 1/k = 1/3 fixed by the list length -- no s-family.
    Fractional part of the AM is forced by tau: A mod 1 = tau/3.
 C. Correlation: the SM congruence y + tau/3 + n2/2 in Z splits as
    (k=3 triality) x (k=2 doublet parity -- the cone's existing Z2
    grading). With tau = 1 for quarks, 0 for non-quarks, the forced
    fractional parts reproduce every SM multiplet's y mod 1, and the
    unused tau=2 classes are exactly the anti-multiplets' fractions.
"""
from fractions import Fraction
from itertools import product as cart

print("=" * 76)
print("A. k=3 shells: triality is intrinsic (center of SU(3) in U(3))")
print("=" * 76)
for N in range(0, 9):
    states = [(a, b, N - a - b) for a in range(N + 1) for b in range(N + 1 - a)]
    dim = (N + 1) * (N + 2) // 2
    assert len(states) == dim
    print(f"  shell N={N}: dim={dim} = (N,0) symmetric, center phase omega^{N}, "
          f"triality tau = N mod 3 = {N % 3}")

print()
print("=" * 76)
print("B. Gates: additivity of tau; AM thirds fixed by tau; 1/3 = 1/k selected")
print("=" * 76)
ok = all((M + N) % 3 == ((M % 3) + (N % 3)) % 3 for M in range(12) for N in range(12))
print(f"  tau additive under composition (homomorphism to Z3): {ok}")
for N in range(0, 9):
    A = Fraction(N, 3)  # AM of the shell's list sum S=N, list length k=3
    print(f"  N={N}: AM = S/3 = {A}, AM mod 1 = {A % 1}, tau/3 = {Fraction(N % 3, 3)}"
          f"  -> fractional part forced by tau: {(A % 1) == Fraction(N % 3, 3)}")
print("  The coefficient is 1/k with k=3 the list length of THIS family member.")
print("  No free parameter: contrast B2's beta = -2/(3s), s arbitrary.")

print()
print("=" * 76)
print("C. Correlation: SM y-fractions = (k=2 parity) x (k=3 triality)")
print("=" * 76)
# name: (j, Y, tau from k=3 shell: quarks 1, non-quarks 0)
TABLE = {
    "L_L":    (Fraction(1, 2), Fraction(-1),    0),
    "Q_L":    (Fraction(1, 2), Fraction(1, 3),  1),
    "H":      (Fraction(1, 2), Fraction(1),     0),
    "e_R":    (Fraction(0),    Fraction(-2),    0),
    "u_R":    (Fraction(0),    Fraction(4, 3),  1),
    "d_R":    (Fraction(0),    Fraction(-2, 3), 1),
    "singlet": (Fraction(0),   Fraction(0),     0),
    "W":      (Fraction(1),    Fraction(0),     0),
}
allmatch = True
for name, (j, Y, tau) in TABLE.items():
    y = Y / 2
    n2 = int(2 * j) % 2
    forced = (-Fraction(tau, 3) - Fraction(n2, 2)) % 1
    match = (y % 1) == forced
    allmatch &= match
    print(f"  {name:>8}: y mod 1 = {y % 1}, forced by (tau={tau}, n2={n2}): {forced}, match: {match}")
print(f"  ALL SM fractional parts reproduced by (parity, triality): {allmatch}")
print("  Unused tau=2 classes: (2,0) -> 1/3, (2,1) -> 5/6. Anti-multiplet check:")
for name, (j, Y, tau) in [("anti-Q_L", TABLE["Q_L"]), ("anti-u_R", TABLE["u_R"])]:
    ybar = -Y / 2
    n2 = int(2 * j) % 2
    forced = (-Fraction(2, 3) - Fraction(n2, 2)) % 1
    print(f"  {name}: y mod 1 = {ybar % 1}, forced by (tau=2, n2={n2}): {forced}, "
          f"match: {(ybar % 1) == forced}")
print()
print("REMAINING INPUT, stated exactly: one k=3 shell residue per multiplet --")
print("tau = N_3 mod 3, with quarks at N_3 = 1 mod 3 and non-quarks at 0. The")
print("grading, its additivity, and the 1/3 normalization are the k=3 object's")
print("own; the assignment of multiplets to shells (the embedding of the k=2")
print("weak structure into/against the k=3 object) is NOT built here.")
