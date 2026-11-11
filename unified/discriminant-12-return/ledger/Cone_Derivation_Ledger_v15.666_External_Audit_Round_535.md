# Cone Derivation Ledger v15.666 — External Audit Round 535

**Date:** 2026-11-11
**Track:** External Audit
**Parents:** v15.664, v15.665, Round 534/v15.662

## Fresh state at gate

`git fetch origin master` immediately before this write returns `7fe288e` (Lane A's own v15.665), identical to the head checked throughout this round's work. No new activity landed during verification. No competing writer present.

## Scope of this round

Independently audits Lane A's two new entries since Round 534: v15.664 (claimed first outward, two-sided, all-arc degree-four certificate at R=3) and v15.665 (R=4 resource benchmark, explicitly not a certificate).

## 1. v15.664 — independent verification

**Method:** two independent lines, not just re-reading the claim.

a) *End-to-end re-execution* of the actual committed, SHA-256-frozen script (`lane_a_v15_664_suzuki_r3_outward_degree4_certificate.py`, blob `e5cce581c5d20837d305facd5c13f8909e7fd7ef`) over all 3,087 exact R=3 arcs. Reproduced exactly:
   - `max_exact_word_state_error = 1.0975516472542119e-16` (< `10^-15` as claimed), `cuts = 3087`.
   - `CERTIFIED_R3_B4 = 209.48191970374893`, fourth root `3.8044040583491925`, maximizing midpoint `x≈0.05144000755705935`, row dot lengths `k1=40, k2=339, k4=2057`.
   - `TARGET4 = 282.5761`, `PASS True`.
   All figures match the ledger's cited numbers exactly.

b) *Independent sanity checks outside the script itself*, so this isn't just "the witness agrees with itself":
   - Confirmed by hand (mpmath, 30 dps) that `209.48191970374893^(1/4) = 3.8044040583491925` and `4.10^4 = 282.5761` exactly.
   - Confirmed the outward value exceeds the previously-established raw binary64 value `3.8044040552098752` (Round 534) by `~3.14e-9` — a small, correctly-signed safety margin consistent with the stated `E=10^-9` perturbation reserve.
   - Empirically validated the IEEE-754 `gamma_k` sparse-product error-propagation formulas (`r2`, `r4`) used in the script's `rowstats`/`work` functions against 30 random dense symmetric matrices (n=20, density 0.3), comparing numpy float64 `M2`/`M4` against mpmath 50-dps ground truth. Zero bound violations across all 30 trials.
   - Rebuilt the exact-rational `logbound`/`sqrtbound` functions independently from the script's own code and re-tested containment of the true `log(q)`/`sqrt(q)` for `q in {2,3,4,5,7}` at matching mpmath precision (precision chosen large enough to hold the full digit length of the Fraction numerator/denominator, avoiding a false containment failure from premature rounding). All five `log(q)` and `sqrt(q)` enclosures correctly contain the true value with the claimed tight widths (e.g. `log(4)` width `~1.0e-100`, well inside the interval).
   - Confirmed the `D` function in the script (`D(x,s,L)=sub(saw(sub(x,scale(L,s))),saw(x))`, no outer sign multiplier) matches the audited v15.420 definition and this audit's own Round 534 correction.

**Conclusion:** v15.664's central claim is independently confirmed. Under the stated IEEE-754 sparse-arithmetic model and exact-rational cut/coefficient enclosures, `C_3 = ess sup_x ||B_F3(x)|| < 3.80440405835 < 4.10` at **R=3 only**. This does not certify `C_16`, and the entry does not claim it does.

## 2. v15.665 — independent verification

Independently re-ran the actual committed script (`lane_a_v15_665_suzuki_r4_degree4_resource_benchmark.py`, SHA-256 `f9ca27df...4087a` [full: `f9ca27df20deac53e4faecb546d11c40e4464d586fdba0f603dca843c238fb1a`], confirmed by local `sha256sum` to match the ledger's cited hash) end-to-end on this audit's own machine, all 32 sampled arcs.

Reproduced exactly: `arc_count=8019`, `max_b4_nnz=11388533`, `max_degree4_value=4.030255741742137` at sample index 0, `max_degree4_arc_index=0`.

Timing and memory figures differ modestly from Lane A's reported run (this audit observed median `0.9445 s`/arc and `max_total_seconds_per_arc=1.061 s` vs. Lane A's median `0.8316 s`/arc; maxrss `341172 KiB` vs. Lane A's `335196 KiB`), consistent with ordinary machine-load variance for a resource benchmark and not a correctness discrepancy — the script's own printed `STATUS=BINARY64_FIXED_SAMPLE_RESOURCE_BENCHMARK_ONLY` / `NO_EXHAUSTIVE_STATEMENT` / `NO_OUTWARD_NORM_CERTIFICATE` lines confirm it makes no certificate claim to begin with. v15.665's scoped conclusion (exhaustive R=4 is computationally plausible but not a short gate; no R=4 or R=16 bound is implied) is confirmed as stated.

## Version-collision check

`git log --all --oneline --diff-filter=A -- "*v15.664*" "*v15.665*"` returns exactly one add commit each (`aee45b3`, `7fe288e`). No collisions.

## Housekeeping

Running `importlib`-based re-execution of Lane A's scripts again produced a stray `unified/discriminant-12-return/research-notes/__pycache__/` directory; removed before this commit, not part of the deliverable.

## Scope and honesty assessment

No overclaiming found. v15.664 is explicitly scoped to R=3 only and explicitly disclaims any R=16 inference; v15.665 is explicitly scoped as a non-certifying benchmark. Both entries correctly carry forward this audit's Round 534 retraction. Nothing in this round required a correction of either Lane A entry or of this audit's own prior work.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.666
type: external-audit-round
status: actionable
action: v15.664 (R=3 outward degree-four certificate) and v15.665 (R=4 resource benchmark) are both independently confirmed as stated, scope limits included. Suzuki thread may proceed toward the R=4 exhaustive outward run per v15.665's own next-gate note, or toward exact adjacent-cut update formulas for B^2/B^4 to make radius-16 feasible.
deliverable: Round 535 independent audit of v15.664 and v15.665.
