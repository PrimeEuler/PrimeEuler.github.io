# P1 and P2 — the weld's standing predictions, tested: both are premise corollaries

Sandbox note (little Euler), 2026-11-18. Producers:
`p1_kfactor.py`, `p2_w2_packages.py` (exact arithmetic;
all checks PASS). Tasked by Jeremy 2026-11-18 (gravity-
thread remaining topics, item 1). The predictions stand
since v14.910 (2026-10-26).

## P1 — k-factor member scale (h = 1/2 at every k)

**Counting form: exact.** On the half-grid (½ℤ_{>0})^k the
product-counting function satisfies
D_k^{1/2}(N) = D_k^{1}(2^k N) identically (enumerated,
k = 1..3; sieve-verified k ≤ 4) — the radial shift of the
k-factor family is −k·log 2 iff every factor carries the
sector spacing, and 0 on the EM (unit) grid. The anomaly
A_k(n) = D_k(2^k n) − 2^k D_k(n) has the weld's predicted
leading coefficient 2^k·k·log 2/(k−2)!: at k = 2 it is
4n·log 4 (fit 5.5375 vs 5.5452 at n = 2000 — v14.857's
Δ₄, the original weld's own anomaly); at k = 3, 4 the
fits decrease monotonically toward the predictions
(k = 3: 20.96 → 19.74, 1/log-extrapolated intercept
16.80 vs 16.64 predicted; k = 4: 43.98 → 36.83,
intercept 19.5 vs 22.2 — log-slow, as filed for this
family of limits).

**Geometry form: no shift exists.** The k-factor Hessian
curvature (v14.820) R_k = −k(k−2)/(4P) is a power law in
the product P; under x → λx it rescales by λ^{−k}. A
power law has no preferred product scale, so the geometry
defines no radial origin at any k (k = 2 is the flat
member). This is v14.856's k = 2 lesson at every k:
normalized geometry is grid-blind; the shift lives only
in where the discrete nodes sit.

**Verdict: P1 is a premise corollary.** Its counting
content is exactly equivalent to "every factor carries
the sector spacing h" — the weld premise itself
(node = state, member scale = sector property). It is
not falsified at any k, and no arena in the record can
confirm it independently: geometry returns no shift, and
every counting-side k-sector number is downstream of the
grid assumption. P1 retires as a test.

## P2 — W2 cutoff (4n, normalization 64, anomaly −12 n² ln n)

**Filed package: reproduced exactly.** shell(12) = 113
(v14.858); W2(4n)/W2(n) = 63.97 at n = 16000 (→ 64);
Δ₆₄/(n² ln n) = −9.88 (→ −12, the filed log-slow crawl;
v14.910 found −10.18 at n = 64000).

**The alternative is real and cleanly separated.** The
anomaly log-coefficient for a general cutoff multiplier
c is −c²(c−1)/4 (from the (1/4)N² ln N term of W2). If
the seat Casimir sum were built on the dyon product grid
(q = 1/4) instead of the state grid, the package would
be (16n, 4096, −960): computed Δ₄₀₉₆/(n² ln n) = −818.7
at n = 16000, heading to −960 — nowhere near the filed
package. So the cutoff question has two coherent answers,
and they are numerically distinguishable.

**What selects 4n is the premise.** The seat Casimir
counts *states*; states live on the h-grid, whose 2D
density is 1/h² = 4 at h = 1/2. That is the weld premise
again (h = 2q, node = state). Every gravity-side
seat-Casimir derivation in the record (v14.858's
Schwinger contacts, v14.989's q2 Casimir) uses the same
integer-contact node set, so none is independent in the
sense P2 demanded.

**Verdict: P2 is a premise corollary**, in the same
shape as P1: not falsified — the filed package is the
one the record's derivations produce — and not
independently confirmable from inside the record.

## Joint consequence

The second-fixed-point hunt (v14.910) is definitively
closed. The weld's two standing predictions are
corollaries of its premise, so no computation of their
form can score the weld an independent hit. The weld
remains what v14.910 found: a one-application dictionary
(the Suzuki /4, h = 2q) whose premise — node = state —
is untested by anything in the current record. Testing
it now requires a genuinely new independent spectrum or
counting derivation (a k-sector operator diagonal built
as Suzuki's was at k = 2, or the K4 action's own mode
spectrum), which is a construction project, not a check.
That is the same seam as item 2 of the 2026-11-18 tasking
(the pair-side ℏℤ / radial-flux identification), where
the premise does its quiet work.

Flags: P1 = PREMISE_COROLLARY (counting exact k ≤ 4;
geometry shift-free); P2 = PREMISE_COROLLARY (package
reproduced; alternative (16n, 4096, −960) separated);
second_fixed_point = NOT_FOUND, hunt CLOSED;
weld_applications = 1; G_derived = false; psi_selected
= false.
