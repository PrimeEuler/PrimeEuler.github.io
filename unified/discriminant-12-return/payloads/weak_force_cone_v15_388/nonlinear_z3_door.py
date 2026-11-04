"""
The nonlinear door vs the SU(3)/thirds door -- are they the same door?
(2026-11-04, sandbox, exact arithmetic.)

Claim under test: getting hypercharge thirds out of a U(1) requires the
SAME move whether you call it "nonlinear coupling" or "SU(3)": enlarging
the global structure by a Z3 so fractional charges are correlated with a
triality label. Three checks:

 1. Charge lattice is representation theory, not dynamics. A U(1)
    character chi_q(theta) = e^{i q theta} is single-valued on the
    circle (period 2pi) iff q is an integer. NO Lagrangian -- linear or
    nonlinear -- changes this: the allowed charges of a compact U(1)
    are Z. A "1/3 charge" is single-valued only on the TRIPLE COVER
    (period 6pi). Fractional charge relative to a fixed circle <=>
    Z3 holonomy. That is a change of global group structure, not of
    field equations.

 2. The SM itself does exactly this move. Its gauge group is
    (SU(3) x SU(2) x U(1)_Y) / Z6, and the quotient is the congruence
        y + tau/3 + n2/2  in  Z,
    with y = Y/2, tau = color triality (0 singlet, 1 triplet),
    n2 = 2j mod 2 (doublet parity). Verified on all eight multiplets.
    Inverting: the fractional part of y is FORCED by (tau, n2):
        y mod 1 = (-tau/3 - n2/2) mod 1.
    Thirds appear in y if and only if tau != 0. Fractional hypercharge
    IS color triality, read through the quotient.

 3. B2 was already smuggling this. In the bicone fit family
    (beta = -2/(3s), alpha = -1 - beta*m_L), the canonical member
    (s=1, m_L=0) has winding residues m mod 3 exactly equal to the
    required triality of every multiplet. But the equality is
    gauge-dependent bookkeeping: shifting m_L breaks it outright, and
    rescaling s changes the extraction rule (tau = s^{-1} m mod 3).
    The fit did not avoid the Z3 -- it hid it in the residue of m.
"""
from fractions import Fraction

print("=" * 76)
print("1. Single-valuedness: U(1) charges are integers, dynamics or not")
print("=" * 76)
for q in [Fraction(1), Fraction(1, 2), Fraction(1, 3), Fraction(2, 3),
          Fraction(4, 3), Fraction(-2, 3), Fraction(3, 2)]:
    # chi_q(theta + 2pi) / chi_q(theta) = e^{2 pi i q}; single-valued iff q in Z
    sv_circle = (q.denominator == 1)
    # on the triple cover (period 6pi): single-valued iff 3q in Z
    sv_cover3 = (3 * q).denominator == 1
    print(f"  q={str(q):>5}: single-valued on U(1) circle? {sv_circle}; "
          f"on triple cover? {sv_cover3}")
print("  => every third needs the cover. The cover IS the Z3 move.")

print()
print("=" * 76)
print("2. SM Z6-quotient congruence: y + tau/3 + n2/2 in Z")
print("   y = Y/2, tau = triality (quarks 1, else 0), n2 = 2j mod 2")
print("=" * 76)
# name: (j, Y, tau)
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
for name, (j, Y, tau) in TABLE.items():
    y = Y / 2
    n2 = int(2 * j) % 2
    S = y + Fraction(tau, 3) + Fraction(n2, 2)
    frac_forced = (-Fraction(tau, 3) - Fraction(n2, 2)) % 1
    frac_actual = y % 1
    print(f"  {name:>8}: y={str(y):>5}, tau={tau}, n2={n2}: "
          f"S={S} (integer: {S.denominator == 1}); "
          f"y mod 1 = {frac_actual}, forced by (tau,n2): {frac_forced}, "
          f"match: {frac_actual == frac_forced}")
print("  Fractional classes (tau, n2) -> y mod 1:")
for tau in range(3):
    for n2 in range(2):
        f = (-Fraction(tau, 3) - Fraction(n2, 2)) % 1
        has_third = f.denominator == 3 or f.denominator == 6
        print(f"    tau={tau}, n2={n2}: y mod 1 = {f}   (thirds: {has_third})")
print("  => thirds in y occur exactly when tau != 0. No exceptions.")

print()
print("=" * 76)
print("3. B2's winding residue IS the triality -- in a non-canonical gauge")
print("=" * 76)
def windings(s, mL):
    beta = Fraction(-2, 3 * s)
    alpha = Fraction(-1) - beta * mL
    out = {}
    for name, (j, Y, tau) in TABLE.items():
        NA = int(2 * j)
        m = (Y - alpha * NA) / beta
        assert m.denominator == 1, (name, m)
        out[name] = int(m)
    return out

def check(member, rule, label):
    ok = all(rule(member[name]) % 3 == TABLE[name][2] for name in TABLE)
    print(f"  {label}: {ok}")
    return ok

w = windings(1, 0)
print(f"  canonical member s=1, m_L=0 windings: {w}")
print(f"  residues m mod 3: {{ {', '.join(f'{n}: {w[n] % 3}' for n in w)} }}")
print(f"  required triality:{{ {', '.join(f'{n}: {TABLE[n][2]}' for n in w)} }}")
check(w, lambda m: m, "tau == m mod 3 for the canonical member")
w_shift = windings(1, 1)
check(w_shift, lambda m: m, "tau == m mod 3 after shifting m_L to 1 (alpha gauge change)")
w_s2 = windings(2, 0)
check(w_s2, lambda m: m, "tau == m mod 3 for s=2")
check(w_s2, lambda m: 2 * m, "tau == s^{-1} m mod 3 for s=2 (s^{-1}=2 mod 3): the rule itself moves")
print("  => the triality sits in m's residue, but WHERE depends on the")
print("     arbitrary family parameters. Non-canonical = bookkeeping,")
print("     and the Z3 grading it encodes is precisely the imported piece.")
