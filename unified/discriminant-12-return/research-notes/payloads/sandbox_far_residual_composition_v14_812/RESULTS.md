# Far residual composition — analysis record (v14.585 actions 3–4)

*Sandbox workspace record, 2026-10-24. Companion to the six
`far-residual-*.json` certificates in this payload and the producer
`far_compose.py` (run by `run_far_compose.sh`).*

## Method

Per sector (even-v / odd-v) and class (F1 = modes [F, T2),
F2 = [T2, 2T2), step 2), the residual is composed row by row in the
audited v14.583 conventions (`dm490/residual554/compose_residual_v14554.py`):

  residual_i = S // (first + 2i − shift) − compact_i − seed_i,
  S = 2^256, shift = 0 (even) / 1 (odd),

with compact = the changed compact action evaluated off-support on
far rows (certs `far-compact-{sector}-{class}.json`, buffer widths
30 on F1 / 29 on F2) and seed = the noncompact seed assembly (certs
`far-seed-{sector}-{class}.json`, width 30). Input files are
hash-pinned against their certificates before composition. Physical
upper per class = point ℓ² norm (directed sqrt at the S grid) +
compact ℓ² error + seed ℓ² error + bare floor error upper(count)/S —
the v14.583 composition formula verbatim; transport charges are NOT
charged again (each was charged exactly once in v14.442).

## Verification

- Smoke runs (first 8,192 rows of F1, both sectors): every row
  cross-checked against an exact Fraction evaluation of
  1/(first + 2i − shift) − compact/S − seed/S; agreement within the
  2/S floor window.
- Spot checks in each production certificate: 23 rows per class
  (edges, thirds, and 16 fixed pseudo-random rows) re-read by
  independent seeks; residual + compact + seed = S // (first + 2i −
  shift) exactly, all classes.
- Independent re-decode of the written residual buffers (separate
  script): ℓ² norms reproduce the certificate point uppers to all
  printed digits; buffer SHA-256s (certificates):
  even F1 4682c363591f5f27…, even F2 11a331d1c8ebfe5f…,
  odd F1 5c709572c51c6bcd…, odd F2 dfbbece8d7d414a4….

## Results (physical uppers)

| sector | class | rows | point norm | physical upper |
|---|---|---|---|---|
| even | F1 | 2,080,765 | 4.1440519e-05 | 4.1440528e-05 |
| even | F2 | 4,161,532 | 3.2606786e-05 | 3.2606786e-05 |
| odd  | F1 | 2,080,765 | 4.1366381e-05 | 4.1366390e-05 |
| odd  | F2 | 4,161,532 | 3.2550819e-05 | 3.2550819e-05 |

Exact budget comparison (v14.444 q; v14.583 DM upper; exact
Fractions in `far-residual-{sector}-summary.json`):

| sector | q | DM upper | far headroom | F1²+F2² (finite far) | headroom² − (F1²+F2²) |
|---|---|---|---|---|---|
| even | 4.9513108e-10 | 4.8145856e-06 | 2.1724430e-05 | 5.8915 × headroom² | −2.3085690e-09 |
| odd  | 4.9673591e-10 | 4.8057856e-06 | 2.1763279e-05 | 5.8499 × headroom² | −2.2970936e-09 |

The evaluated finite far classes alone exceed the far headroom in
both sectors; the F3 tail [2T2, ∞) is nonnegative and can only
increase the far total. DM² + F1² + F2² ≤ q fails exactly.

## Mechanism (empirical)

Decomposition on the evaluated rows (even sector; odd is the same
to ~1%): ‖bare − seed‖ = 1.994e-05 (F1) / 1.413e-05 (F2) — the seed
cancels the bare source to ~8% relative; ‖compact‖ = 4.370e-05 /
3.137e-05. The full residual carries a clean persistent 1/n term:
block means (2^16-row blocks) of residual_n · n over the top octave
of each class —

| sector | F1 top octave | F2 top octave |
|---|---|---|
| even | +0.1596 ± 0.0008 | +0.1771 ± 0.0005 |
| odd  | +0.1593 ± 0.0008 | +0.1768 ± 0.0005 |

with per-block slope slightly positive (+0.0003…+0.0007): ρ(n) is
flat-to-rising across n = 4.16e6…1.66e7, not decaying. This is the
configuration DERIVATION.md §1 (2026-10-19) pre-registered as the
failure branch: the total 1/n coefficient of (source − compact −
seed) does not vanish, so no F3 envelope assembled on this
trial/seed pair can close the far bound. The exact attribution of
ρ(n) among the seed's affine-model defect (W₀ vs 1), the compact's
−(c·Z₀^trial − d^trial), and the seed channel coefficients remains
open; the verdict does not depend on it.

## Scope

The scoped v14.583 delivery (DM physical uppers inside allowance,
far headroom positive) is untouched and stands. Whole-residual
acceptance remains uncertified. Closing the far gate would require
an approximant whose total far 1/n coefficient vanishes; no such
trial/seed pair is frozen.
