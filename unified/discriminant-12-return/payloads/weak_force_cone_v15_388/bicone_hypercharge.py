"""
Bicone hypercharge test -- exact verification (2026-11-04, sandbox).

Setup: weak SU(2) shell from cone A (N_A = 2j), hypercharge candidate
Y = alpha * N_A + beta * m, with m the second U(1)'s label.
SM requirements (j, Y): L (1/2,-1), Q (1/2,+1/3), H (1/2,+1),
e_R (0,-2), u_R (0,+4/3), d_R (0,-2/3), singlet (0,0), W (1,0).
All arithmetic exact (Fractions).

Checks:
 A. Singlet difference lattice: the pairwise differences of the singlet
    hypercharges {-2, 4/3, -2/3, 0} generate (2/3)Z. Hence any beta with
    all singlet windings integral obeys beta = (2/3)/t form (up to the
    m-offset freedom); in particular NO nonzero integer beta works, and
    beta = 0 fails.
 B. B2 family: for beta = -2/(3t) (t = +/-1,+/-2,+/-3) and alpha set by
    the lepton offset choice m_L in {-1,0,1} via alpha = -1 - beta*m_L,
    every multiplet's winding m is an integer and every Q spectrum
    reproduces the SM table exactly.
 C. Reading B1 closure (spot-check of the proof): with m restricted to
    nonnegative integers and alpha,beta scanned over a rational grid,
    no (alpha,beta) places all four singlets -- as the sign argument
    requires (at N_A=0, Y = beta*m is one-signed or zero, but the
    singlet set has both signs nonzero).
"""
from fractions import Fraction
from itertools import combinations

MULTIPLETS = {
    "L_L":   (Fraction(1, 2), Fraction(-1)),
    "Q_L":   (Fraction(1, 2), Fraction(1, 3)),
    "H":     (Fraction(1, 2), Fraction(1)),
    "e_R":   (Fraction(0),    Fraction(-2)),
    "u_R":   (Fraction(0),    Fraction(4, 3)),
    "d_R":   (Fraction(0),    Fraction(-2, 3)),
    "singlet": (Fraction(0),  Fraction(0)),
    "W":     (Fraction(1),    Fraction(0)),
}

def q_spectrum(j, Y):
    steps = int(2 * j)
    return sorted(Fraction(steps - 2 * i, 2) + Y / 2 for i in range(steps + 1))

SM_Q = {name: q_spectrum(j, Y) for name, (j, Y) in MULTIPLETS.items()}

print("=" * 76)
print("A. Singlet difference lattice")
print("=" * 76)
sing_Y = sorted({Y for name, (j, Y) in MULTIPLETS.items() if j == 0})
diffs = sorted({b - a for a, b in combinations(sing_Y, 2)})
print(f"  singlet hypercharges: {[str(y) for y in sing_Y]}")
print(f"  pairwise differences: {[str(d) for d in diffs]}")
# gcd of a set of rationals: gcd of numerators over lcm of denominators
from math import gcd
from functools import reduce
def rat_gcd(vals):
    dens = [v.denominator for v in vals]
    L = reduce(lambda a, b: a * b // gcd(a, b), dens, 1)
    nums = [abs(int(v * L)) for v in vals]
    return Fraction(reduce(gcd, nums), L)
g = rat_gcd(diffs)
print(f"  gcd of differences = {g}  -> the difference lattice is ({g})Z.")
print(f"  => beta must satisfy: singlet Y-differences are beta * (integers),")
print(f"     so beta divides {g} rationally: beta = {g}/t, t a nonzero integer")
print(f"     (or beta=0, impossible). Integer beta check:")
for b in range(-3, 4):
    if b == 0: continue
    ok = all((Y / b).denominator == 1 for Y in sing_Y)
    print(f"     beta={b:+d}: all singlet windings integral? {ok}")

print()
print("=" * 76)
print("B. B2 family verification: beta = -2/(3t), alpha = -1 - beta*m_L")
print("=" * 76)
all_ok = True
for t in [1, -1, 2, -2, 3, -3]:
    beta = Fraction(-2, 3 * t)
    for mL in [-1, 0, 1]:
        alpha = Fraction(-1) - beta * mL
        row = {}
        for name, (j, Y) in MULTIPLETS.items():
            NA = int(2 * j)
            m = (Y - alpha * NA) / beta
            if m.denominator != 1:
                all_ok = False; row[name] = f"m={m} NON-INTEGER"; continue
            m = int(m)
            # reproduce Y and the Q spectrum from (alpha, beta, m)
            Y_back = alpha * NA + beta * m
            ok = (Y_back == Y) and (q_spectrum(j, Y_back) == SM_Q[name])
            all_ok &= ok
            row[name] = m
        print(f"  t={t:+d}, beta={beta}, m_L={mL:+d}, alpha={alpha}: windings {row}")
print(f"  ALL family members reproduce the full SM table exactly: {all_ok}")

print()
print("=" * 76)
print("C. Reading B1 spot-check (m >= 0): rational grid scan for the singlets")
print("=" * 76)
found = 0
grid = [Fraction(p, q) for q in (1, 2, 3, 4, 6) for p in range(-12, 13)]
for alpha in grid:
    for beta in grid:
        good = True
        for name, (j, Y) in MULTIPLETS.items():
            if j != 0: continue
            if beta == 0:
                if Y != 0: good = False; break
                continue
            m = Y / beta  # alpha * N_A = 0 on singlets
            if m.denominator != 1 or m < 0: good = False; break
        if good: found += 1
print(f"  (alpha,beta) grid pairs placing all four singlets with m>=0: {found}")
print("  (Matches the proof: beta*m at N_A=0 is one-signed, singlet Y is not.)")
