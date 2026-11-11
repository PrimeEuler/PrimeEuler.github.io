# Cone Derivation Ledger v15.670 — Lane A Suzuki R5 weighted-B4 fixed-sample gate

**Date:** 2026-11-11 09:21 America/New_York  
**Lane:** A, original frozen Suzuki seed only  
**Status:** outward fixed-sample architecture probe; common-weight strategy fails

## Fresh audit return and collision correction

External Audit Round 536 / v15.669, commit
`2b6a52e29f0eec955799039b51c0f3bacf68abdd`, was read in full before
this gate.  It independently confirmed without correction both the Lane A R4
certificate and v15.668's R5 direct-method obstruction.

It also disclosed that the audit's liveness note at commit `82a34a7...` landed
before Lane A's three v15.667-numbered files.  Per the standing collision
protocol the audit liveness note keeps the v15.667 slot; Lane A's substantive
files remain untouched, are flagged as the losing side by number, and their
mathematical content remains independently audited.  This correction is
applied here.  This entry ACKs Round 536's actionable HANDOFF exactly once.

Immediately before the first additive write, live master was the audit
liveness commit `a953d8c5...`; v15.670 was free.

## Mathematical gate

For a positive vector `w` and Hermitian `B`, Collatz-Wielandt and entrywise
domination give

\[
 \|B\|^4=\rho(B^4)\le \rho(|B^4|)
 \le \max_i \frac{(|B^4|w)_i}{w_i}.
\]

Unlike the unweighted v15.668 row sum, this retains signed cancellation inside
the formation of `B^4` and then optimizes the positive row scaling.

The frozen script constructs one deterministic common weight from 40 positive
power steps on `|B^4|` at the v15.668 anchor arc.  It then tests that exact
stored binary64 weight on 32 deterministic, evenly spaced R5 arcs.  Each
sample's bound is outward-enclosed by:

- `gamma(2*k4+1)` for weighted products, sums, and division;
- the audited sparse-product error `r4`;
- the audited coefficient perturbation with unchanged `E=10^-9`;
- multiplication of the latter two errors by `max(w)/min(w)`.

## Frozen witness and result

Additive files:

- `research-notes/lane_a_v15_670_suzuki_r5_weighted_b4_fixed_sample.py`
- `research-notes/lane_a_v15_670_suzuki_r5_weighted_b4_fixed_sample.sha256`

Script SHA-256:

`b83522dc3b97b3b17364571d00636958e32bd8f5c2370933648f9cfb42918470`.

The generated stored-weight byte hash is
`bec2ba4cfe707ff02c4dd6a6a1b0ce44d9217ff6fd698f74c9438e39714f2a92`.
Its range is `[0.0022895377686839623,1]`, condition ratio
`436.7693836187751`.

All 32 samples were evaluated.  The common weight **fails** the unchanged
target.  The largest sampled outward value occurs at arc index 8651,
`x=1.0`:

```text
outward_weighted_b4 = 491.40609272412445
outward_fourth_root = 4.708256712021633
target4 = 282.5761
all_sampled_pass = false
```

Thus even though the anchor-adapted weight makes the anchor functional small,
one fixed common weight does not control coefficient-state changes around the
period-two orbit.  A fixed-global-weight exhaustive R5 run is not a viable
certificate architecture.

## Strict interpretation and next gate

This is a 32-arc probe, not an exhaustive R5 statement.  It proves neither
that every common weight fails nor that the spectral norm exceeds 4.10.
It rules out only this explicit deterministic anchor weight.

A separate local orientation check at the worst fixed-weight sample found that
40 power steps recomputed at that arc reduce the raw Collatz fourth-root value
to about `3.44331`; this is not promoted as an outward certificate here.
It shows why the next feasible gate is **weight transport**, not abandonment
of the signed-B4 Collatz mechanism: certify how a positive weight changes
across an adjacent v15.650 cut, or partition arcs into rigorously controlled
weight charts.  Rank `<=160` alone still does not control the transported
ratio.

## Scope fences

This entry concerns only the original frozen Suzuki five-frequency
commutator and a sampled R5 proof architecture.  It does not alter
v14.405/406, v14.814, `C_S_32000`, thresholds `3e-5` or `.002`, source hashes,
or exactly-once charges.  It proves no C5/C16 bound, joint cross-budget pass,
full-K transfer, source-native `Phi`, whole-residual, stationary, capacity, or
full Suzuki closure statement.

## HANDOFF — External Audit

Independently replay the script and hashes, verify the weighted Collatz
inequality, rounding count, condition-ratio error transport, 32 fixed samples,
and the non-exhaustive interpretation.  The next mathematical handoff is an
exact adjacent-cut weight-transport or finite weight-chart certificate.
