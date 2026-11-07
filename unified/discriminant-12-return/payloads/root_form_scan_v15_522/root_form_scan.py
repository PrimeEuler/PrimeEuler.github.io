"""
Are Door III's reals roots of integers? A bounded scan
(2026-11-07, sandbox; Jeremy: "what if the reals are all
some root of another integer?" -- scan run at his go-ahead).

Idea under test: if a coupling value were a root -- sqrt(N),
or a root of a small integer polynomial -- it would be
discrete data in disguise (an integer + a prescription), the
one species-change that could bring Door III's three reals
inside the range of the consistency predicates (which output
discrete data only, v15.520/v15.521).

Section 0 is the record's own 137, stated before any
scanning: the frame ALREADY has an alpha contact -- the
bicone extraction (v14.106/v14.110; the pushed note
"Hydrogen Dipole Matrix Elements from Bicone Geometry").
The parabolic SO(4,2) matrix element is a pure number
(Y_geom = 768/(243 sqrt(6)) family); eliminating it against
the measured H(2p) lifetime tau = 1.592 +- 0.025 ns (Bukow
beam-foil) gives 1/alpha = 137.4 +- 2.2, and He+ gives 136.8
(range 136.4-137.1) -- both bracket 137.036. That is a
MEASUREMENT channel (the lifetime trick: G_F from the muon
lifetime is the same species), honest at +-1.6%. Its error
bars are ~1e8 times wider than the modern alpha precision,
so it cannot adjudicate root forms -- every candidate root
lives deep inside its interval. The scan therefore runs on
the precision values; the extraction enters as the reason
137 is this project's number at all, and as a filed scope
limit. (The 1966 n=3 extractions missed: 160.8 +- 16.7
excludes 137.036; 131.6 +- 4.9 sits just below -- the
channel is data-limited, as filed.)

TARGETS (imported standard values, flagged):
  alpha^-1(0)   = 137.035999177 +- 0.000000021  (CODATA 2022)
  alpha^-1(mZ)  = 127.951 +- 0.009              (PDG, MSbar)
  sin^2 thW(mZ) = 0.23122 +- 0.00004            (PDG, MSbar)
  alpha_s(mZ)   = 0.1179 +- 0.0009              (PDG)
The first is scale-free and is the harsh filter; the mZ
trio are Door III's values in measured form (their GUT-
normalized inverses are v15.429's (59.02, 29.58, 8.48)).

FAMILIES (frozen before looking; q = denominator of p/q in
lowest terms -- the standard simplicity measure here, since
|p| is forced by the target's size):
  F0 pure roots: x = N^(1/k), k = 2, 3, 4, N integer --
     the literal form of the question (x > 1 targets only;
     the family is empty inside (0, 1)).
  F1 rationals p/q.   F2 sqrt(p/q) (scan x^2).
  F3 cbrt(p/q) (scan x^3).
  F4 pi-forms: x/pi^k, x*pi^k rational, k = 1, 2 (pi is
     native to the cone's spectral data, e.g. the sqrt(8 pi)
     determinant of loop step 1, v15.394).
  NAMED historical candidates, evaluated directly:
     Eddington alpha^-1 = 137; Wyler's form
     (9/(16 pi^3)) (pi/120)^(1/4) for alpha; 3/13 for
     sin^2 thW.
GRADING (per family per target): (i) pull in sigma of the
best candidate with q <= 200; (ii) chance expectation
E = (6/pi^2) Q^2 d for that candidate, where d is its
distance on the scanned axis and Q = 200 -- the expected
number of family points at least that close to a RANDOM
target; E >> 1 means the closeness is unremarkable, and a
candidate excluded at many sigma needs no E. (iii) the
minimal denominator Q* reaching pull <= 1, against the
Dirichlet scale Q_D = 1/sqrt(sigma_axis): Q* << Q_D would
be atypically simple. PSLQ (mpmath, 40 digits) checks
alpha(0) for ANY integer polynomial relation of degree
<= 3 with coefficients <= 1e6 -- the bounded form of "root
of some integer polynomial." ~35 family-target trials are
run; the look-elsewhere effect is part of the grading.

VERDICT SHAPE: per-real grades, honestly split. A hit
would be a fingerprint (identification), not a selector:
no predicate forces the integer. A clean negative at
bounded height closes the small-integer version of the
hypothesis for the precise reals and leaves the imprecise
one (alpha_s) untestable rather than supported.
"""
from fractions import Fraction as F
import numpy as np
import mpmath as mp

mp.mp.dps = 40
QCAP = 200

TARGETS = [
    ("alpha^-1(0)",  F(137035999177, 10**9), 2.1e-8),
    ("alpha^-1(mZ)", F(127951, 1000),         9e-3),
    ("sin^2 thW",    F(23122, 100000),        4e-5),
    ("alpha_s(mZ)",  F(1179, 10000),          9e-4),
]

print("=" * 76)
print("0. the record's own 137 (context, not the scan)")
print("=" * 76)
print("""  bicone extraction (v14.106/v14.110): parabolic matrix
  element (pure number) x measured H(2p) lifetime
  1.592 +- 0.025 ns -> 1/alpha = 137.4 +- 2.2; He+ -> 136.8
  (136.4-137.1). A measurement channel at +-1.6%: its sigma
  is ~1e8 times the CODATA sigma below, so it brackets
  every root candidate and adjudicates none. Filed as the
  frame's alpha contact; the scan runs on precision data.""")

def chance_E(d, Q=QCAP):
    """Expected # of rationals with denom <= Q within distance d
    (one-sided) of a random point: density (3/pi^2) Q^2 per unit,
    interval 2d."""
    return (6 / np.pi**2) * Q * Q * d

def scan_axis(t, x, sig, sig_t, back, label):
    """Scan rational approximations to t (= transform of x);
    back(r) maps a rational on the t-axis back to x-units;
    sig_t is the target's sigma measured on the t-axis."""
    r = t.limit_denominator(QCAP)
    cand = back(r)
    d = abs(float(r) - float(t))
    p = abs(float(cand) - float(x)) / sig
    E = chance_E(d)
    qstar = None
    for cap in (200, 2000, 20000, 200000, 1000000):
        rr = t.limit_denominator(cap)
        if abs(float(back(rr)) - float(x)) / sig <= 1.0:
            qstar = cap
            break
    qd = 1 / np.sqrt(sig_t)
    print(f"  {label}: best q<={QCAP} p/q = {r} (q = {r.denominator}), "
          f"pull = {p:,.3g} sigma, chance E = {E:,.3g}; "
          f"minimal q for pull<=1: "
          + (f"~{qstar} (Dirichlet scale {qd:,.3g})"
             if qstar else "> 1e6 (dead at bound)"))

def scan_target(name, x, sig):
    xf = float(x)
    print()
    print("=" * 76)
    print(f"target {name} = {xf:.10g} +- {sig:.1g}")
    print("=" * 76)
    if xf > 1:
        for k in (2, 3, 4):
            tk = x ** k
            n0 = int(tk + F(1, 2))
            cand = float(n0) ** (1.0 / k)
            sig_tk = k * xf ** (k - 1) * sig
            print(f"  F0 x = N^(1/{k}): nearest N = {n0}, pull = "
                  f"{abs(cand - xf)/sig:,.2f} sigma "
                  f"(sigma on x^{k} axis = {sig_tk:.3g} -- "
                  f"{'integers are unavoidable neighbours' if sig_tk > 0.05 else 'a discriminating axis'})")
    else:
        print("  F0: family empty inside (0,1); see F2/F3.")
    scan_axis(x, x, sig, sig, lambda r: r, "F1 rational")
    scan_axis(x * x, x, sig, 2 * xf * sig,
              lambda r: mp.sqrt(mp.mpf(r.numerator) / r.denominator),
              "F2 sqrt(p/q)")
    scan_axis(x * x * x, x, sig, 3 * xf * xf * sig,
              lambda r: (mp.mpf(r.numerator) / r.denominator)
              ** (mp.mpf(1) / 3), "F3 cbrt(p/q)")
    for k in (1, 2):
        for sgn, lab in ((1, f"x/pi^{k}"), (-1, f"x*pi^{k}")):
            t = F(str(xf / (np.pi ** (k * sgn))))
            scan_axis(t, x, sig, sig / np.pi ** (k * sgn),
                      lambda r, k=k, sgn=sgn: float(r) * np.pi ** (k * sgn),
                      f"F4 {lab} = p/q")

for nm, xv, sg in TARGETS:
    scan_target(nm, xv, sg)

print()
print("=" * 76)
print("named historical candidates")
print("=" * 76)
xa, sa = 137.035999177, 2.1e-8
print(f"  Eddington 137: pull = {abs(137 - xa)/sa:,.0f} sigma -- dead")
wyler = 1 / ((9 / (16 * np.pi**3)) * (np.pi / 120) ** 0.25)
print(f"  Wyler form: alpha^-1 = {wyler:.7f}, pull = "
      f"{abs(wyler - xa)/sa:,.0f} sigma -- dead at modern precision")
s2, ss = 0.23122, 4e-5
print(f"  sin^2 thW = 3/13 = {3/13:.6f}: pull = "
      f"{abs(3/13 - s2)/ss:,.1f} sigma -- dead")

print()
print("=" * 76)
print("PSLQ: alpha^-1(0) against integer polynomials, degree <= 3")
print("=" * 76)
xamp = mp.mpf("137.035999177")
for deg in (1, 2, 3):
    vec = [xamp ** k for k in range(deg, -1, -1)]
    rel = mp.pslq(vec, maxcoeff=10**6)
    print(f"  degree {deg}: relation with coeffs <= 1e6: {rel}")

print()
print("=" * 76)
print("joint probe: one shared small denominator for the mZ trio?")
print("=" * 76)
trio = [(F(5902, 100), 0.010), (F(2958, 100), 0.006), (F(848, 100), 0.065)]
found = None
for q in range(1, 2001):
    if all(abs(round(float(v) * q) / q - float(v)) <= 2 * s
           for v, s in trio):
        found = q
        break
print(f"  smallest common denominator q <= 2000 putting all three")
print(f"  GUT-normalized inverses within 2 sigma: {found}")
print("  (alpha3^-1's sigma is 0.065 -- the test is weak by")
print("   construction; a pass here carries ~no information.)")

print()
print("=" * 76)
print("VERDICT")
print("=" * 76)
print("""  Read off per target from the tables above, under the
  header's grading (pull, chance E, minimal q vs the
  Dirichlet scale, ~35 trials of look-elsewhere included).
  Structural scope, independent of the numbers: even a
  small-q hit would be a FINGERPRINT (identification of the
  value with a discrete datum), not a selector -- no
  consistency predicate on record outputs 'this integer
  rather than its neighbour'. The hypothesis would
  relocate Door III from 'three reals' to 'three small
  integers + prescriptions', the species where mechanisms
  exist; whether nature has done so is what the pulls
  above measure.""")
