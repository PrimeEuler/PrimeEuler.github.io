# Cone Derivation Ledger v15.665 — Lane A Suzuki R4 degree-four resource benchmark

**Date:** 2026-11-11 05:25 America/New_York  
**Lane:** A, original frozen Suzuki seed only  
**Status:** evaluated fixed-sample binary64 resource benchmark; **not** an exhaustive or outward norm certificate

## Fresh-state and correction check

Immediately before this gate, live `master` was
`aee45b3adfe30a255ea312f02bc6aa21ab56ccc4` (Lane A v15.664).
The latest full independent audit remained External Audit Round 534 / v15.662,
commit `284f43fde2f5ee009833ec77ef0818516003e6c6`.  Its correction is retained:
Round 530's claimed missing `sigma*tau` in the v15.650 four-corner identity was
the audit's transcription error; the original v15.650 identity is correct.
No independent audit of the outward R3 certificate v15.664 had landed.

This entry ACKs the current distinct PRIMARY MISSION continuation exactly once.
It does not ACK or modify any independent-audit ownership.

## Frozen producer and benchmark

The benchmark imports the already frozen v15.657 producer and makes no change
to its matrix definition.  New additive files:

- `research-notes/lane_a_v15_665_suzuki_r4_degree4_resource_benchmark.py`
- `research-notes/lane_a_v15_665_suzuki_r4_degree4_resource_benchmark.sha256`

The new script SHA-256 is

`f9ca27df20deac53e4faecb546d11c40e4464d586fdba0f603dca843c238fb1a`.

It evaluates 32 deterministic, evenly spaced indices
`floor(j*8019/32)`, `0 <= j < 32`, among all 8,019 v15.650 R=4 arcs.
For every sampled midpoint it constructs the physical signed sparse matrix
`B`, checks binary64 symmetry, constructs `B2=B@B` and `B4=B2@B2`, and records
`max_i sum_j |B4_ij|` and its fourth root.

## Replayed output

- R=4 sites: 6,561.
- Candidate arcs: 8,019; sampled arcs: 32.
- Every sampled `B`: 199,260 nonzeros.
- Every sampled `B2`: 1,576,425 nonzeros.
- Every sampled `B4`: 11,388,533 nonzeros.
- Largest sampled binary64 fourth-root value:
  `4.030255741742137`, at sampled arc index 0,
  midpoint `x=0.00020828994260790878`.
- Median timed sparse construction through `B4`: `0.831578387499988 s/arc`.
- Maximum timed sparse construction through `B4`: `0.8936372699999993 s/arc`.
- Whole 32-arc process wall time, including absolute row sums, output and
  allocation cleanup: `39.63233495399999 s`.
- Observed process high-water RSS: `335196 KiB` (about 327.34 MiB).

The script's median sparse-construction-only extrapolation is
`6668.427089362404 s` for 8,019 arcs.  The more conservative observed whole-run
wall extrapolation is about `9930 s` (2.76 h) serial.  Parallel execution would
multiply the roughly 327 MiB observed process footprint and therefore requires
an explicit memory budget; no unmeasured parallel speed or memory claim is made.

## Scoped conclusion and obstruction

This gate establishes that an exhaustive R=4 degree-four calculation is
computationally plausible but is not a short gate in the current execution.
It also identifies the dominant concrete object: an 11.39-million-nonzero
`B4` per arc with about 327 MiB observed process high-water memory.

The value `4.030255741742137` is from only 32 arcs and binary64 arithmetic.
It is **not** an upper bound for all R=4 arcs, is **not** outward rounded, and
cannot be used as a certificate.  In particular it says nothing by itself
about the decisive R=16 quantity `C16`.

The next certificate promotion remains gated on independent review of v15.664's
exact interval construction, `E=1e-9` reserve and IEEE `gamma_k` bookkeeping.
If that audit passes, the next resource-supported promotion is an exhaustive
R=4 run with the same outward machinery, under an explicit time/memory budget.
If it is corrected, the correction must be applied before R=4 promotion.

## Scope fences

This entry concerns only the original frozen Suzuki five-frequency commutator.
It does not alter v14.405/406, v14.814, `C_S_32000`, thresholds `3e-5` or
`.002`, source hashes, or exactly-once charges.  It proves no full-K transfer,
source-native `Phi`, whole-residual, stationary, capacity, or full Suzuki
closure statement.

## HANDOFF — External Audit

Independently replay the frozen 32-index benchmark, its SHA-256, sparse nonzero
counts, timing/RSS reporting, and the non-certifying interpretation.  This
handoff does not ask Audit to infer an exhaustive R=4 bound from the sample.
