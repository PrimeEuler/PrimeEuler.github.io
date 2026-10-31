# BUILD LOG — K_full sharper-route return (v15.192 handoff), interval-inertia PRIMARY

Date: 2026-10-31. Route decision (Jeremy, 2026-10-31): interval inertia
on a declared contour PRIMARY; local-block/Schur fallback only.
Spec: kfull/SHARPER_ROUTE_SPEC_v15192.md (route-decision block + settled
addendum). Plan: kfull/INSTANTIATION_PLAN_v15155_158.md. Kernel:
kfull/DERIVATION.md §0. Ledger texts read in full into ./sources/:
v15.129, v15.155, v15.158, v15.179, v15.192 (probe entry), SEED_FORMULA.md.

## Sector naming — recorded to avoid the known trap

v15.192 names lattices by PHYSICAL parity of n. SEED_FORMULA.md and
ctgate/constants.json name sectors by start (start=1 is called "even"
there). Pairing used throughout this build (verified consistent across
SEED_FORMULA §Input, constants.json sigma/L/b/spike fields):

- Lattice ODD:  n = 512001 + 2j (odd n).  constants.json key "even-v",
  SEED_FORMULA start=1 sector: sigma = +1, L = 1.4357379705709206
  (L_rational in constants.json), spike m1 = 512001.
- Lattice EVEN: n = 512002 + 2j (even n). constants.json key "odd-v",
  SEED_FORMULA start=2 sector: sigma = -1, L = 0.6634791495304894,
  spike m1 = 512002.

Common: c = 2/pi (c_rational in constants.json), t = 1/pi^2
(t_rational, same both sectors). Kernel (DERIVATION §0):
K_{N,m} = c*(m*z_N - N*z_m)/(N^2-m^2) + 2*sigma*p_N*p_m (N != m);
K_{N,N} = d_N + 2*sigma*p_N^2; p_n = floor(L*n/(n^2+t)*2^256)/2^256
(exact rational from L_rational, t_rational).
d_n from suzuki_certified_remote_diagonal.evaluate(n) (certified
enclosure, radius ~7e-11, asserts n > R = 256000).
z_n from suzuki_certified_remote_z.evaluate(n, action_precision=True)
(certified enclosure, radius < 1e-39).

## Design decisions

D1. Replay set per sector: the 100 modes n = b + 2j, j = 0..99
    (v15.192 text, read directly — not from summaries).
D2. M verification from v15.129's displayed inequality ONLY:
    ||B0|| <= |c|*pi*Zbar + |c|*Zbar/(2*n_min), |c|*pi = 2 exactly,
    Zbar = 7.4232946911477145 (certified, coeff819/zbar_moments.py via
    project record; also Zbar < 7.4233 as stated in v15.192);
    pole 2||p||^2 < 4/(n_min-2) per v15.192's displayed bound
    (recomputed independently with exact L rationals in script).
D3. Finite section for inertia: J = 100 block K_J on the replay modes,
    interval entries as exact Fraction pairs (mpmath not needed;
    pure rational interval arithmetic, outward by construction).
    Interval LDL^T (no pivoting) at x-delta, x, x+delta; pivot
    intervals must exclude 0 for a certified count.
D4. x, delta chosen from the certified replay gap (x = midpoint of
    the certified first-gap interval of the replay diagonal,
    delta = certified gap / 4), NOT from float eigenvalue probes —
    the diagonal gap is what the handoff's contour language refers
    to; K_J inertia counts at that x are then whatever they are.
    (A float probe of K_J eigenvalues is run for context only and
    labeled as such; it selects nothing in the certificate path.)
D5. Tail transfer attempted via the sanctioned v15.155/v15.158
    machinery; the named suspects, in order: tau_S (tail diagonal
    approaching the strip), rho(D) membership at the crossing,
    A(Gamma) via the only certified full-K localization (min-max
    bracket with M = 15). Exhibits, if any, come from certified
    evaluator enclosures on an explicitly bounded tail scan window;
    scan extent and stop rule recorded in the script header.
D6. Uniform bound |d_n - log(n/4)|: derived from SEED_FORMULA §diag
    displayed formula with rigorous Fraction bounds on
    sum_q w_q*(2-log q) from the z-module's own constants()
    enclosures, plus cusp and arch-error terms — settles the
    v15.192 handoff sub-item "verify uniform < 3" if it comes out < 3.

## Step 1 result — evaluator check (2026-10-31)

- suzuki_certified_remote_diagonal.evaluate(n): works, asserts
  n > R = 256000 (R from suzuki_certified_remote_z). Enclosure radius
  at n = 512001: 1226328469/18446744073709551616 ~ 6.65e-11 (< 1e-9 as
  asserted in the module). ~0.002 s/eval after constants cache warm.
- suzuki_certified_remote_z.evaluate(n, action_precision=True):
  radius at 512001 = 20898107/2923003274661805836407369665432566039311865085952
  ~ 7.15e-42 — IDENTICAL rational to constants.json z_m1_radius for
  the 512001 sector; at 512002 = 10449053/1461501637330902918203684832716283019655932542976
  ~ 7.15e-42, also identical to constants.json. ~0.3-0.65 s/eval.
- Standard-precision z radius ~6.8e-12; matrix build uses
  action_precision (D3) for margin.

## FINDING F1 — the displayed d_approx formula is not the evaluator's diagonal at O(1/n)

Replay (replay.py, first run): all five lowest n match Lane A's order in
both sectors; p_n spike cross-check EXACT both sectors; M = 14.8466086
(odd lattice) / 14.8466055 (even lattice) < 15 verified from v15.129's
displayed inequality; BUT Lane A's five float values sit OUTSIDE the
certified enclosures by 2e-7..1.2e-6, and certified first gaps are
0.0041506260 odd / 0.0129580238 even vs stated 0.00414962 / 0.01295697
(differences +1.01e-6 / +1.05e-6). Too large for display rounding (5e-9)
or the arch remainder (6.6e-11).

Root cause (localized by exact Fraction component comparison against
60-digit mpmath): every factor in the evaluator (log, cusp, weights,
phases, sin, cos, invk) matches the displayed formula to <1e-52, EXCEPT
the term structure: suzuki_certified_remote_diagonal.evaluate computes
  prime_q = w_q * [ (2 - log q) * cos(theta_q n) + (2/(n pi)) * sin(theta_q n) ],
i.e. the (2/(n pi)) sin term is weighted by w_q ALONE, while the
SEED_FORMULA Sdiag displayed formula (and Lane A's probe) weights it by
w_q * (2 - log q):
  prime_q(display) = w_q * (2 - log q) * [ cos + (2/(n pi)) sin ].
Predicted per-n difference (certified - displayed)
  = sum_q w_q (1 - log q) (2/(n pi)) sin(theta_q n),  |.| <= ~1.9e-6,
sign-varying — matches all observed distances. The evaluator is the
producer of record (SEED_FORMULA Sdiag DEFINES d_n as its output;
DERIVATION S0 freezes d_N by it; v15.192's handoff names it "the exact
diagonal interval evaluator" and calls the displayed formula "leading",
"not an interval evaluation of the exact diagonal"). Verdict: the
probe's VALUES are approximations to the diagonal at the 1e-6 level,
not the diagonal; ordering and both gaps' qualitative size are
unaffected; the certified gaps supersede the stated ones.
Identity verified numerically in replay.py (section F1) to < 1e-9.

Consequence for D6: the uniform bound is recomputed with the module's
actual coefficients: |term_q| <= w_q(2-log q) + w_q * invk (not
w_q(2-log q)(1+invk); differs only at q=7 where 2-log 7 < 1).

## Inertia attempt 1 — natural-order interval LDL FAILS (width amplification)

Declared point per sector (design D4): x = midpoint of the certified
replay gap interval, delta = certified gap/4.
  odd lattice:  x = 10.442302397081809, delta = 0.0010376564980985107
  even lattice: x = 10.292076001905091, delta = 0.003239505915913396
Natural-order interval LDL^T of K_J - xI (and x +/- delta) failed in
both sectors: a pivot interval straddled 0 (odd x: pivot 24,
[-0.0801, +0.0173]; even x: pivot 33, similar width). Float diagnosis:
natural-order midpoint pivots get as small as 0.021 (odd) / 0.0098
(even); interval widths (~1.3e-10, from the diagonal enclosures)
amplify by ~(coupling/pivot)^2 per elimination step along coupled
paths, reaching ~1e-1 by pivot ~24-34. This is an algorithm failure,
not a spectral statement.
Remedy (design D7): symmetric pivoting — greedy order chosen from
FLOAT midpoints (largest |Schur diagonal| first), fixed in advance,
then the SAME permutation applied to the interval matrix; the
interval run remains the certificate. Float profiles with greedy
order: min pivot 0.077 (even), 0.00099 (odd).
Float context probe of K_J (midpoint matrix, eigvalsh): odd sector
has an eigenvalue at 10.442664, only 3.6e-4 from x and INSIDE the
strip [x-delta, x+delta] — so the odd strip test fails on the merits
for K_J regardless of arithmetic; its counts at x-delta and x+delta
will differ by 1. Even sector: no probe eigenvalue in the strip;
count below x = 10 (probe), nearest probe eigenvalues 10.253087 /
 10.341087. Probe counts below x_diag: odd 12, even 10 — the diagonal
gap does NOT separate 1 eigenvalue of K_J; B mixes the block strongly
(float ||B|| ~ 2), which is expected and not itself a finding.

## Inertia attempt 2 — pivoted interval LDL CERTIFIES the finite section

Greedy symmetric pivoting (order from float midpoints, fixed in
advance) cured the width amplification. All runs: every pivot
interval excludes 0; margins = min over pivots of dist(pivot, 0).

Odd lattice (x_diag = 10.442302397081809, delta = 0.0010376565):
  count(K_J < x-delta) = 12 (margin 0.00383)
  count(K_J < x)       = 12 (margin 0.000978)
  count(K_J < x+delta) = 13 (margin 0.00185)
  => K_J has EXACTLY ONE eigenvalue in (x, x+delta]: the strip test
     FAILS ON THE MERITS for K_J in this sector (certified).
  Secondary declared point x_alt = 10.423148427, delta_alt =
  0.009757644 (midpoint/quarter of the float spectral gap
  (10.403633140, 10.442663714) bracketing x_diag):
  counts 12 / 12 / 12 (margins >= 0.00935)
  => CERTIFIED for K_J: no eigenvalue in [x_alt-delta_alt,
     x_alt+delta_alt], exactly 12 eigenvalues below x_alt.

Even lattice (x_diag = 10.292076001905091, delta = 0.0032395059):
  counts 10 / 10 / 10 (margins >= 0.0718)
  => CERTIFIED for K_J: no eigenvalue in the strip, exactly 10
     eigenvalues below x.

## Tail transfer — FAILS STRUCTURALLY (the INCONCLUSIVE core)

Certified tail scan (tail_scan.py; first 20,000 tail modes per
sector, n in [b+202, b+40198], certified diagonal enclosures):
  odd:  462 enclosures entirely below x-delta; 464 below x;
        5 FULLY INSIDE the strip; closest |d_n - x| <= 1.5993e-4
        (n = 513623) => tau_S(x) >= 6252.6, M*tau_S >= 93,789.
  even: 192 below x-delta; 198 below x; 12 fully inside the strip;
        closest |d_n - x| <= 2.0133e-4 (n = 515042)
        => M*tau_S >= 74,505.
Consequences, all rigorous:
 (i) The diagonal-preserving cutoff K_R = D + P_R B P_R has the tail
     diagonal values as exact eigenvalues: >= 5 (odd) / >= 12 (even)
     of them lie IN the strip and >= 464 / >= 198 lie below x, so
     count_R(x) >= 476 (odd) / >= 208 (even) != count_J(x) = 12 / 10.
     The finite-section count does not transfer even to K_R.
 (ii) No contour through the strip lies in rho(K_R) (let alone the
     common resolvent of v15.158): the common-resolvent condition
     FAILS, not merely its bound.
 (iii) In the v15.155 bracket [h + M tau_S + M tau_R], the single
     term M*tau_S >= 7.45e4 already exceeds 1 by > 4 orders of
     magnitude; with prefactor eta^-1 (1 + M/eta) >= 1 the two-scale
     bound is vacuous for this window. FAILING ESTIMATE NAMED:
     M * tau_S, driven by tail diagonal density at spacing
     ~1e-4..1e-3 around the strip vs delta ~ 1e-3.
 (iv) The only other certified full-K localization, the v15.179
     min-max bracket with M = 15, has half-width 15 ~ 10^4 times the
     strip width; it cannot exclude spectrum from the strip either.
Scale note: modes with d_n < x can occur up to n < 4 e^{x + C}
~ 7.9e5 (odd) / 6.8e5 (even), i.e. ~1.4e5 lattice modes per sector;
a count transfer at this x by finite section would need a block of
that order, not J = 100. Verdict per sector for the FULL K:
INCONCLUSIVE (never "no gap"): finite-section certificates above
stand; the transfer is blocked at M*tau_S / rho(K_R), precisely.

## Assembly

DRAFT_LEDGER_ENTRY.md written in this run dir (parent ledgers it; this
build pushes nothing). MANIFEST.sha256 covers all scripts, outputs,
matrix caches, the draft entry, BUILD_LOG.md, and the hashed inputs.
Final state of the four task steps: (1) evaluator check DONE;
(2) replay DONE with finding F1; (3) inertia DONE at the finite-section
level (certified both sectors; odd primary strip fails on the merits,
odd secondary point certified, even primary certified) and transfer
INCONCLUSIVE with the failing estimate M*tau_S / rho(K_R) named
precisely; (4) return assembled.

## Numbers provenance rule

Every number in the return traces to: a certified evaluator enclosure
(file + sha256), an exact rational in constants.json, a displayed
inequality in a ledger text in ./sources/, or a script in this run
dir (sha256 recorded). Float values appear ONLY in the labeled
context probe (D4) and in comparisons against Lane A's published
float values (the replay's purpose).
