# The divisor-split sign test: the T/D/A coloring's fluctuation, its crossings, and its seats

*Sandbox note (little Euler), 2026-11-07. Jeremy's sketch
and go-ahead the same evening, with the mod-12 units comb
and the binary D(n) function added mid-run at his
direction. The apparatus is Jeremy's (2016-era; sessions
2026-10-01/02/08/13): the cone base at level n is the
triangular array T(n) = n(n+1)/2 positions; D(n) =
Σ_{k≤n} d(k) marks the divisor-hit positions; A(n) =
T(n) − D(n) the misses; row recursion A(n+1) = A(n) +
(n+1) − d(n+1). His framing, stated during the run: a
divisor and a non-divisor are parabolic action/reaction
pairs — each row's inflow (n+1) splits into the hit
channel d(n+1) and the miss channel (n+1) − d(n+1), two
complementary channels of one total, and the fluctuation
below is the pair's imbalance (Δ_A = −Δ exactly, by
A = T − D). His question: the divisor count rides above
and below its average across boundaries — could that
split embed a selection? Producers:
`divisor_split_sign.py`, `divisor_split_sign2.py`
(sieve to N = 2×10⁶).*

## Setup and partition checks [D]

Δ(n) = D(n) − M(n) against the standard smooth trend
M(n) = n log n + (2γ−1)n. Checks against the record:
A(300) = 43383 exactly as recorded (2026-10-13); d(n) odd
iff n is a perfect square, verified here to all
n ≤ 2×10⁶. Known backdrop, stated in advance: Δ is
provably two-sided (Ω± results, swings ≥ ~x^{1/4} both
ways), so the bare split cannot select; the test is about
addresses, bias, and extremality.

## Q1 — the crossing census [D]

295,268 sign changes of Δ for n ≤ 2×10⁶ — at integer
resolution the split is crossing-dense (median gap 3
shells, mean 6.8). Crossing rate per shell by decade:
11%, 23%, 26%, 22%, 16%, 13% — peaking mid-range and
declining as Δ's x^{1/4} scale outgrows the increments.
Δ > 0 on 59.65% of shells: the fluctuation already spends
more time above its trend than below at this range.

## Q2 — crossing addresses [D]

Mean distance from a crossing shell to the nearest square
shell: 444.3, against a permutation null of 471.3 ± 0.6
(2000 draws, same count) — crossings are ~6% closer to
seats than chance. Real but modest, and §5 gives its
mechanism: the seat boost (a local bump of size
~2.2·n^{1/4} in Δ) manufactures crossings on both flanks.
The crossings are seat-*influenced*, not seat-locked;
they are everywhere.

## Q3/Q4 — the seat bias (the headline) [D]

At square shells the fluctuation is one-sided:

- Δ(m²)/n^{1/4}: mean **+2.1911**, positive at **99.9%**
  of the 1413 squares ≤ 2×10⁶. Neighbouring offsets are
  also positive-biased but less (means +0.66 to +1.93 at
  offsets ±1…±3): the boost is centred on the seat and
  decays over a few shells.
- Δ(m²) is a local **maximum** in its seat window
  [m²−m, m²+m] at 3.3% of squares and a local minimum at
  **0.0%** — against a random-shell control at 0.04% /
  0.02% (5000 shells). Seats are local maxima at ~80× the
  chance rate, and never minima.
- Row level: the seat rows are divisor-rich — row excess
  e(k) = d(k) − (log k + 2γ) averages **+10.73** on square
  rows (d on squares has a higher mean order) against
  −0.0075 on non-square rows; prime rows average
  **−12.57** (the hollow rows ride below trend).

In Jeremy's action/reaction reading: at seat shells the
pair's imbalance locks to the action (divisor) side.

## The mechanism: the Voronoi phase-lock [D]

Δ(x) is a sum of modes (Voronoi): terms
d(k)·k^{−3/4}·cos(4π√(kx) − π/4), the circle-side modes of
the divisor problem. At a square argument x = m², every
square mode k = j² has phase 4πmj − π/4 ≡ −π/4 (mod 2π)
— **all square modes phase-lock and pull the same way**;
at generic x their phases spread and cancel. Measured:
the truncated series (K = 20000 modes) tracks Δ/x^{1/4}
with correlation 0.81 at squares, 0.92 at non-squares;
the square modes' coherent contribution at a square is
S/(2π) with S = Σ_j d(j²)j^{−3/2} = 13.893 (j ≤ 20000),
i.e. **+2.211** in normalized units — against the
measured seat mean **+2.1911**. The square modes alone
account for the seat bias, to ~1%. Their contribution at
non-squares: mean +0.028 (mean |·| 0.224) — the lock
dissolves off the seats. The mechanism is classical
(Voronoi-era), and it is exactly Jeremy's picture in
analytic dress: the circles align at the parabola
vertices.

## The comb and the binary channel (Part 2) [D]

- **Klein-4 units comb.** The row excess stratifies by
  gcd(k,12), monotonically (range-averages at N = 2×10⁶;
  the class means drift logarithmically, since the
  classes carry different log-coefficients in mean d):
  gcd 12: +27.82; gcd 6: +9.47; gcd 4 (classes 4, 8):
  +4.97; gcd 3 (3, 9): −2.02; gcd 2 (2, 10): −3.69;
  gcd 1 — the units {1,5,7,11}, all four classes at
  −8.947 to three decimals: the comb's teeth are the
  divisor-*poorest* rows of the base, exact duals of the
  hollow prime rows. But the seat bias is **comb-blind**:
  Δ(m²) at unit seats (m ∈ {1,5,7,11} mod 12, m² ≡ 1)
  averages +2.162, positive 99.8% (470 seats), against
  non-unit seats +2.206, 99.9% (943). The unit-restricted
  fluctuation Δ_U (main term (1/9)·[n log n +
  (2γ−1+2 log 2+log 3)n] from the restricted Dirichlet
  series) is again two-sided and crossing-dense (172,193
  crossings; 53.3% positive) and shows **no** seat bias
  at squares (+0.089 normalized, 60.2% positive).
- **Binary D(n).** The binary readout b(k) = d(k) mod 2
  is the square indicator, so its summatory is the seat
  counter **exactly**: B(n) = ⌊√n⌋ (verified at sample
  points to 2×10⁶; B(2×10⁶) = 1414 seats). The binary
  channel of the coloring has no fluctuation at all
  beyond the sawtooth — it counts the seats.

## Verdict

Jeremy's asymmetry is real, and it is located more
precisely than the sketch put it: not in the crossings'
addresses (seat-influenced at 6%, explained by the boost)
but in the fluctuation's **values at seat shells** —
one-sided (99.9% positive, local maxima at ~80× chance,
never minima), quantitatively accounted for by the
Voronoi phase-lock of the square modes (2.211 predicted,
2.191 measured). In the action/reaction reading, the
pair's imbalance locks action-side exactly at the seats.

As a selector for the doors, it does not reach — stated
plainly: the asymmetry lives on a measure-zero
subsequence (the squares), the global split remains
two-sided (59.65/40.35), the effect is a bias in a
real-valued fluctuation rather than a discrete choice
among framework alternatives, and its mechanism is
classical analytic number theory, not cone dynamics. It
is a fingerprint-grade structure — an exact, cone-native
asymmetry of Jeremy's coloring, with a known mechanism
and a measured size. A door could use it only if two of
its alternatives differed in their square-mode content;
no door on the table poses that question. The comb
result stands separately: the mod-12 base is
gcd-stratified, the Klein-4 teeth are its hollows, and
the binary channel counts the seats exactly.
