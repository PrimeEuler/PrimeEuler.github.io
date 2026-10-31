# Cone Derivation Ledger v15.227 — Sandbox K_full interval-inertia return on the v15.192 handoff: certified diagonal replay (finding F1), M and uniform bound verified, finite-section inertia certified, full-K transfer INCONCLUSIVE at M·tau_S

Date 2026-10-31. Track: Sandbox (Lane B). Parents: v15.192 (handoff), v15.179, v15.158, v15.155, v15.129. Route decision (Jeremy, 2026-10-31): interval inertia on a declared contour PRIMARY; local-block/Schur fallback only. Live HEAD checked immediately before write. Nothing in the certificate path uses float point values; floats appear only as labeled context probes and in pivot-order selection. Payload: payloads/kfull_inertia_return_v15_227/ (scripts, outputs, build log, manifest; the two matrix-cache JSONs remain in the sandbox run dir with their hashes in the manifest — they are derived artifacts, regenerable by re-running inertia2.py).

Sector pairing (naming trap, stated once): v15.192 names lattices by
physical parity. The odd-n lattice (base b = 512001) pairs with
constants.json key "even-v", sigma = +1, L = 1.4357379705709206; the
even-n lattice (b = 512002) pairs with key "odd-v", sigma = -1,
L = 0.6634791495304894. The pairing is not asserted: it is proved by
§1.3 below. Common: c = 2/pi, t = 1/pi^2.

## 1. Certified diagonal replay [D]

The 100 lowest modes per lattice were evaluated with the certified
producer `suzuki_certified_remote_diagonal.evaluate(n)` (enclosure
radius ~6.65e-11 at these n; the evaluator asserts n > 256000).

1.1 Order and gaps. The five lowest modes coincide EXACTLY with Lane
A's sample order in both sectors (odd: 512035, 512151, 512191, 512053,
512013; even: 512082, 512122, 512174, 512024, 512064). Certified first
sorted gaps (outward, from enclosures): odd 0.004150625992394043
(exact 38282767713689819/9223372036854775808), even
0.012958023663653584 (exact 59758336556122475/4611686018427387904).
Lane A's stated float gaps were 0.00414962 / 0.01295697. The certified
values supersede them; the qualitative verdict (gap << 2M = 30, screen
fails) is unchanged.

1.2 FINDING F1 — Lane A's five float values per sector lie OUTSIDE the
certified enclosures, by 9.4e-9 to 1.22e-6 (odd distances by rank:
2.16e-7, 8.00e-7, 9.4e-9, 1.22e-6, 2.19e-7; even: 7.00e-7, 3.54e-7,
9.59e-7, 2.21e-7, 1.23e-6). Too large for display rounding (5e-9) or
the evaluator's arch remainder (~6.6e-11). Cause, isolated by exact
Fraction component comparison against 60-digit mpmath: every factor of
the certified evaluator matches the displayed d_approx formula
(SEED_FORMULA §diag display, as probed at v15.192) to <1e-52 EXCEPT
the sine-term weighting — the evaluator computes
prime_q = w_q·[(2 − log q)·cos(theta_q n) + (2/(n pi))·sin(theta_q n)],
while the displayed formula weights the sine term by w_q·(2 − log q).
The identity
  (certified) − (displayed) = sum_q w_q (1 − log q) (2/(n pi)) sin(theta_q n)
reproduces the observed discrepancies with max residual 4.7e-9 (odd) /
2.7e-9 (even). The evaluator is the producer of record: SEED_FORMULA
§diag DEFINES d_n as its output and DERIVATION §0 freezes the diagonal
by it; v15.192 itself labels the displayed formula "leading" and not an
interval evaluation. So: Lane A faithfully computed the displayed
formula (mpmath at 50 digits reproduces its targets to ~2-3e-9); the
formula display is what differs from the producer. The probe values
are 1e-6-level approximations to the diagonal, not the diagonal.

1.3 Pairing proof. p_n = floor(L·n/(n^2 + t)·2^256)/2^256 computed
from the exact rationals of constants.json equals constants.json's
p_m1_rational EXACTLY at both spike modes (512001 with L of "even-v";
512002 with L of "odd-v"). The z evaluator at action precision returns
enclosure radii identical to constants.json's z_m1_radius values in
both sectors.

## 2. The two certified bounds Lane A asked to verify [D]

2.1 M <= 15, both sectors. From v15.129's displayed inequality
||B0|| <= |c|·pi·Zbar + |c|·Zbar/(2 n_min) with |c|·pi = 2 exactly and
Zbar < 7.4233 as displayed at v15.192, plus the pole term: totals
14.846608641118573 (odd lattice) / 14.846605474814707 (even lattice),
consistent with Lane A's ||B0|| < 14.84661 and pole < 7.813e-6.
M = 15 is certified per sector.

2.2 Uniform bound. |d_n − log(n/4)| <= C = 1.745855454249828 for all
lattice n >= 512001, with module-faithful coefficients — C < 3 (and
< 1.76). This discharges the "verify uniform < 3" sub-item and makes
v15.192's conditional kill unconditional: with M = 15 the min-max
pre-screen cannot pass at any j <= 99 in either sector.

## 3. Interval inertia on the finite section K_J (J = 100) [D]

Declared primary point per sector: x = midpoint of the certified
replay gap interval [hi_(1), lo_(2)], delta = certified gap/4. Interval
LDL^T (Sylvester) of K_J − xI with all entries interval (diagonal and z
from the certified evaluators, p_n and c exact), outward rounding on a
2^-512 grid after every operation; symmetric greedy pivoting with the
order fixed in advance from float midpoints (natural order failed by
width amplification through ~0.01 pivots — recorded in the build log;
the pivoted interval run is the certificate). A count is certified
only when every pivot interval excludes 0; margins are the minimum
pivot distance to 0.

Odd lattice: x = 10.442302397081809, delta = 0.0010376564980985107.
  count(K_J < x − delta) = 12 (margin 0.00383)
  count(K_J < x)         = 12 (margin 0.000978)
  count(K_J < x + delta) = 13 (margin 0.00185)
=> K_J has EXACTLY ONE eigenvalue in (x, x + delta]: the strip test
   FAILS ON THE MERITS for the finite section in this sector.
Secondary declared point (midpoint/quarter of the finite section's
probe spectral gap (10.403633140, 10.442663714) bracketing x):
x_alt = 10.423148427, delta_alt = 0.009757644; counts 12 / 12 / 12,
margins >= 0.00935 => CERTIFIED: no K_J eigenvalue in
[x_alt − delta_alt, x_alt + delta_alt], exactly 12 below x_alt.

Even lattice: x = 10.292076001905091, delta = 0.003239505915913396.
  counts 10 / 10 / 10, margins >= 0.0718
=> CERTIFIED: no K_J eigenvalue in [x − delta, x + delta], exactly 10
   eigenvalues of K_J below x.

## 4. Transfer to the full K — INCONCLUSIVE, obstruction named [D]

Certified tail scan (first 20,000 tail modes per sector,
n in [b+202, b+40198], certified diagonal enclosures; all counts are
rigorous lower bounds for the full tail):

  odd:  462 enclosures entirely below x − delta; 464 below x;
        5 enclosures FULLY INSIDE the strip; closest approach
        |d_n − x| <= 1.5993e-4 at n = 513623, hence tau_S(x) >= 6252.6
        and M·tau_S >= 93,789.
  even: 192 below x − delta; 198 below x; 12 fully inside the strip;
        closest |d_n − x| <= 2.0133e-4 at n = 515042, hence
        M·tau_S >= 74,505.

Consequences:
(i) The diagonal-preserving cutoff K_R = D + P_R B P_R carries the
    tail diagonal values as exact eigenvalues, so >= 5 (odd) / >= 12
    (even) eigenvalues of K_R lie IN the strip and
    count_R(x) >= 12 + 464 = 476 (odd) / >= 10 + 198 = 208 (even)
    != count_J(x). The finite-section count does not transfer even
    to K_R.
(ii) No contour through the strip lies in rho(K_R); the v15.158
    common-resolvent condition FAILS outright, not merely its bound.
(iii) In the v15.155 bracket [h_{R,S} + M·tau_S + M·tau_R], the single
    term M·tau_S >= 7.45e4 already exceeds the rank-stability
    threshold E_Gamma < 1 by more than four orders of magnitude.
    FAILING ESTIMATE: M·tau_S, driven by tail diagonal density
    (enclosures at spacing ~1e-4..1e-3 around the strip, vs
    delta ~ 1e-3).
(iv) The v15.179 min-max bracket (half-width M = 15) is the only other
    certified full-K localization and cannot exclude spectrum from a
    strip of width ~1e-3 either.

VERDICT, both sectors, for the full K: INCONCLUSIVE. This is NOT a
"no gap" claim for K: nothing here excludes or establishes spectrum of
K in the strip. The finite-section certificates of §3 stand as stated.

Scale of a repair: tail modes with d_n < x occur up to
n < 4·e^(x + C) ~ 7.9e5 (odd) / 6.8e5 (even) — ~1.4e5 lattice modes per
sector. A count transfer at this x by finite section would need a
block of that order (with the residual tail then separated), or a
transfer method not routed through the diagonal-preserving cutoff.
The local-block/Schur fallback named in the route decision faces the
same tail-diagonal obstruction at its boundary terms unless its block
absorbs the sub-strip modes; it was not attempted, per the decision
that interval inertia is primary and this attempt's failure mode is
now precisely located.

## 5. Handoff state

Discharged: exact-diagonal replay (with finding F1 on the probe's
formula display); M <= 15 per sector; uniform bound < 3 (C = 1.7459),
making the v15.192 conditional kill unconditional; certified
finite-section inertia at declared points (§3). Still open, precisely:
a certified eigenvalue count / spectral gap for the FULL K at a
declared remote point — blocked at M·tau_S and rho(K_R) as above, not
at the finite-section step. Gate status unchanged:
CLOSED_SCOPED_OBSTRUCTION_CURRENT_FROZEN_DATA; production fence
untouched (C_S_32000, thresholds 3e-5 / 0.002, exactly-once charges
unspent).

## Payload and provenance

Repo payload: payloads/kfull_inertia_return_v15_227/ ; sandbox run dir: lane_b/sandbox/runs/20261031-kfull-inertia/
Scripts: replay.py, inertia.py (natural-order attempt, kept for the
record), inertia2.py (pivoted, certifying), tail_scan.py.
Outputs: replay_output.json, inertia_output.json, inertia2_output.json,
tail_scan_output.json, matrix_cache_{odd,even}_lattice_*.json (the
exact interval block matrices K_J as built). BUILD_LOG.md records every
design decision. SHA-256 manifest in MANIFEST.sha256 alongside.
Inputs: suzuki_certified_remote_diagonal.py 08226538..., 
suzuki_certified_remote_z.py 8a24c589..., constants.json 369a5fa5...,
ledger texts v15.129 1dc2eea0..., v15.155 924ffadf..., v15.158
c9260633..., v15.179 bf562463..., v15.192 a00bae96..., SEED_FORMULA.md
ac579974... (full hashes in the manifest).
