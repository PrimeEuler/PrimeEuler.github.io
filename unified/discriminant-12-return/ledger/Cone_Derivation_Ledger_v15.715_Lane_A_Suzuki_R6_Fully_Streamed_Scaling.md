# Cone Derivation Ledger v15.715 — Lane A Suzuki R6 fully streamed scaling

**Date:** 2026-11-11  
**Track:** Lane A — original frozen Suzuki seed only  
**Parents:** v15.704; External Audit Round 544/v15.707

## Fresh state and audit ACK

External Audit Round 544/v15.707 was read in full. Its distinct actionable
Suzuki HANDOFF is ACKed exactly once here. The audit personally re-executed
v15.704, matched its script hash, all five checkpoint hashes, every reported
field, and the no-global-B2/B4 architecture, and supplied no correction. It
authorized the measured R6 scaling gate below.

At the post-compute/pre-write collision check, live `master` was
`d5eafe0d8e43dc462d474af231b5cedc7899d4cc`. The latest relevant independent
audit remained Round 544 at
`1ee73c5e0cc6f69518cc5f07f963392d37da571b`; intervening commits were on
another track and do not touch this Suzuki gate. No competing v15.715 write
was present, so v15.715 was next-free. The reproducer commit is
`a78a263d31e746ab1047228f3346a27e2c322576`; immediately before the manifest
write live `master` was that reproducer commit, and the manifest commit is
`c719e6cc031fa964ba86646603f981fe95c5011f`. Immediately before this ledger
write live `master` was that manifest commit and the ledger path remained
absent.

## Exact R6 arc bookkeeping

The v15.650/v15.664 exact-log construction was repeated at radius 6. The
32,955 exact cut enclosures were sorted and proved pairwise disjoint. Exactly
one open cut arc contains `x=1`: index 16,477 (zero based), with certified
endpoints

- left upper endpoint `0.9999640794542536`;
- right lower endpoint `1.0000359205457463`.

Both exact rational margins from `x=1` are
`3.5920545746366354e-05`, exceeding the retained exact margin `1e-6`.
Thus this is rigorous branch bookkeeping for one R6 arc, not a one-point
numerical probe. The matrix on that arc has dimension 28,561 and 948,428
stored nonzeros.

## Fully streamed R6 gate

The audited v15.704 architecture was used unchanged with blocks of 128 output
rows. Each of 40 positive-weight steps computes signed
`(((B[rows,:] @ B) @ B) @ B)`, takes the absolute value only after the signed
B4 rows are complete, applies those rows to the current weight, discards the
block, and normalizes after all output rows are filled. The final validation
uses the independently audited v15.699 stagewise directed-rounding recurrence
and unchanged exact coefficient perturbation. No global B2 or B4 is formed.

Frozen checkpoint weight hashes are:

- step 1: `b3791a4a3d54b8e5a5b9c2ac9db413153f6532e4eec15a51534da9ec5175bfd9`;
- step 10: `74440478a185a5dde22e403d57316dd8165261731b080082456ecc2d552aa9e9`;
- step 20: `db9f7bf3d7417fa4cd59cf125415812bbed9c214a8e31e2971d0c5c2b5f21744`;
- step 30: `6fd07e328ea5ae9a6d5b9ac6b25c6c6980133a7b103157e51de5d9915d77066e`;
- step 40/final:
  `5a7a50cf756a18b52992606ef05d3bad719e484ff1e079991f437f81ce1139ef`.

The final weight condition is `675.1610284977405`. The outward replay gives:

- maximizing row: `1306`;
- observed weighted ratio: `158.26334468478194`;
- arithmetic envelope in that batch: `6.233122407490661e-11`;
- maximum arithmetic envelope over all batches: `2.4326045900745546e-10`;
- unchanged coefficient perturbation: `6.913525593247093e-07`;
- outward weighted B4: `158.26381150127094`;
- outward fourth root: `3.5468710959553458 < 4.10`.

Peak batch fill through B, B2, B3, B4 was
`[4,976, 48,249, 194,276, 480,402]`; maximum stored row lengths were
`[40, 403, 1,715, 4,557]`. The 40-step construction took
218.83036637306213 seconds, final validation 6.0335166454315186 seconds, and
total runtime 235.44558930397034 seconds. Peak RSS was 148,628 KiB. The run
explicitly records `formed_global_b2_or_b4=false`.

Relative to audited R5/v15.704, dimension grew by 1.95075x, construction time
by 2.0913x, peak RSS by 1.5301x, and peak B4 batch fill by 1.2552x. This is a
measured resource point, not an R16 extrapolation certificate.

## Frozen witness

- reproducer:
  `research-notes/lane_a_v15_715_suzuki_r6_fully_streamed_scaling.py`
- SHA-256:
  `1905fe6b8d0e936f049379e38cec9eaafe80dbf425a3f9b7d8b32bbf51b227eb`
- manifest:
  `research-notes/lane_a_v15_715_suzuki_r6_fully_streamed_scaling.sha256`

## Scope and next gate

This is a rigorous outward norm certificate on one exact R6 cut arc and a
measured scaling point for the no-global-power pipeline. It is not C6, C16,
or an all-arc atlas, and does not establish the required R16 bound. It makes
no full-K, source-native Phi, whole-residual, stationary, capacity, or full
Suzuki conclusion. The frozen v14.405/406 pass, v14.814 failure,
`C_S_32000`, thresholds, hashes, and once-only charges are untouched.

After independent replay, the next resource gate is a measured R7 run (or a
strictly cheaper step-count/warm-start study justified from the frozen R6
checkpoint sequence) before any larger-radius claim. An eventual C16 result
still requires exhaustive coverage of all 1,257,795 exact arcs and a
two-sided outward spectral norm bound below 4.10.

HANDOFF
target: external-audit, sandbox
parent: v15.715
type: suzuki-r6-fully-streamed-scaling
status: actionable
action: independently replay the exact R6 cut ordering and unique x=1 arc, all 40 streamed checkpoints, script/weight hashes, no-global-B2/B4 property, v15.699 outward recurrence, fill/timing/memory fields, and one-arc-only scope; if clean, authorize the next measured radius-scaling or rigorously justified cheaper convergence gate.
deliverable: independent audit of v15.715 R6 fully streamed scaling and outward one-arc certificate.
