# Cone Derivation Ledger v15.527 — Sandbox: the divisor-split sign test (Jeremy's T/D/A asymmetry lives at the seat shells; Voronoi phase-lock measured)

**Deposit type:** Sandbox exploration, independently checkable. Jeremy's
sketch and go-ahead 2026-11-07 (evening): the divisor count of his T/D/A
coloring (T(n) = n(n+1)/2 the cone base; D(n) = sum d(k) the hits; A(n) =
T − D the misses) rides above and below its average across boundaries —
could that split embed a selection? His framing: a divisor and a
non-divisor are parabolic action/reaction pairs (each row's inflow splits
into the hit and miss channels of one total; the fluctuation is the pair's
imbalance, Δ_A = −Δ exactly). Mid-run he added the Klein-4 mod-12 units
comb and the binary D(n) function. Producers re-executed at staging;
payload snapshot's title block records the staging state of the note.

## (a) The crossing census — the split is dense and two-sided

Δ(n) = D(n) − (n log n + (2γ−1)n), sieve to 2×10⁶. Partition checks pass:
A(300) = 43383 (record, 2026-10-13); d(n) odd iff n is a square, to 2×10⁶.
Δ changes sign 295,268 times (median gap 3 shells; rate per shell by
decade 11%, 23%, 26%, 22%, 16%, 13% — declining as the x^{1/4} scale
outgrows the increments); Δ > 0 on 59.65% of shells. Crossing addresses
are seat-INFLUENCED, not seat-locked: mean crossing→nearest-square
distance 444.3 vs a permutation null of 471.3 ± 0.6 (~6% closer), the
mechanical product of the seat boost below manufacturing flank
crossings.

## (b) The seat bias — one-sided, and fully accounted for

At the 1413 square shells ≤ 2×10⁶: Δ(m²)/n^{1/4} has mean **+2.1911** and
is positive at **99.9%** of squares; Δ(m²) is a local maximum in its seat
window [m²−m, m²+m] at 3.3% of squares and a local minimum at 0.0%
(random-shell control 0.04% / 0.02% — maxima at ~80× chance, minima
never). Row level: square rows' divisor excess averages +10.73 (d on
squares has a higher mean order), prime rows −12.57 (the hollow rows ride
below trend). Mechanism, measured: in the Voronoi expansion of Δ, at
x = m² every square mode k = j² has phase ≡ −π/4 (mod 2π) — the square
modes **phase-lock**. Their coherent contribution at a square is
S/(2π), S = Σ_j d(j²) j^{−3/2} = 13.893, i.e. **+2.211** against the
measured +2.1911 — the lock accounts for the whole bias to ~1%; at
non-squares the square modes contribute mean +0.028 (dissolved). The
truncated series (K = 20000) tracks Δ/x^{1/4} at correlation 0.81
(squares) / 0.92 (non-squares).

## (c) The comb is blind to the bias; the binary channel counts seats

Row excess stratifies by gcd(k,12) monotonically (range-averages;
log-coefficients differ by class): gcd 12: +27.82; gcd 6: +9.47; gcd 4:
+4.97; gcd 3: −2.02; gcd 2: −3.69; gcd 1 — the Klein-4 units
{1,5,7,11}, all four at −8.947 — the divisor-POOREST rows, duals of the
hollow prime rows. But the seat bias does not see the comb: unit seats
(m² ≡ 1 mod 12) average +2.162, 99.8% positive (470) vs non-unit seats
+2.206, 99.9% (943); the unit-restricted fluctuation Δ_U (restricted
series' own main term) is two-sided, crossing-dense (172,193 crossings,
53.3% positive), with NO seat bias (+0.089, 60.2%). The binary readout
b(k) = d(k) mod 2 is the square indicator; its summatory is the seat
counter exactly: B(n) = floor(sqrt(n)) (B(2×10⁶) = 1414) — no
fluctuation in the binary channel beyond the sawtooth.

## Verdict and scope

The asymmetry Jeremy pointed at is real and sits one level deeper than
the crossings: in the fluctuation's VALUES at seat shells — one-sided,
seat-locked, classically mechanised (Voronoi), and measured to 1%
against its own explanation. As a door selector it does not reach: it
lives on the measure-zero square subsequence, the global split stays
two-sided, and it biases a real-valued fluctuation rather than choosing
among framework alternatives. Filed as a fingerprint-grade structure of
the T/D/A coloring — in Jeremy's action/reaction reading, the pair's
imbalance locks action-side exactly at the seats — usable by a door only
if two of its alternatives differed in square-mode content; no door on
the table poses that question.

**Payload:** `payloads/divisor_split_sign_v15_527/` — Divisor_Split_Sign_Test.md `a6bd562c5f8a440ceaa723f3d91f3253393be51b79d2a1352de450505a79f612`, divisor_split_sign.py `c024bec1bf490543ff0bed1a4692612454ad664f74ae86320af089ece05e63f9`, divisor_split_sign2.py `90e470b3693d841774f25203ed85ad925480bf0025e57b94ffcc2790e95d2ec4`.
