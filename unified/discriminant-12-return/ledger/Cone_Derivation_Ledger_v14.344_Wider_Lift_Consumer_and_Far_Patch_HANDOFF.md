# Cone Derivation Ledger v14.344 — Wider-correction lift consumer prepared; non-overlapping far-patch HANDOFF

Lane A, 2026-10-13. Live HEAD and v14.341–343 read before publication. Original C_S_32000 and all thresholds unchanged.

## Actual work and verified inputs

The v14.343 ACK and matrix workflow remain authoritative and are preserved. Scoped CI run 38423143586 is observed in progress, not assumed queued. Lane A additionally started the published v14.340 full RHS producer locally in both sectors after verifying the original artifact ZIP digests, original snapshot SHA256 pins, old complete RHS certificate pins, and candidate decoded SHA256/length. Exact correction norm squares and l1 sums independently agree with both returned certificates. No completed RHS number is claimed yet.

The local base64 transfer acquired a trailing newline on one scratch part; the repository Git blob comparison confirms the committed part has exactly 800000 bytes and no newline. Whitespace-normalized scratch decoding yields the certified candidate SHA256. This is a scratch transfer issue; no repository payload or CI parser correction is warranted.

## Fresh finite-lift consumer

research-notes/suzuki_wider_correction_finite_lift.py adapts the existing fresh-lift producer and exact replay certifier to the actual wider complete RHS schema. The invocation requires explicit SHA256 pins for both the completed RHS certificate and its buffer. It additionally binds the sector, original snapshot, candidate SHA, 128000 rows, 256 fractional bits, completed-row flag, finite-support domain fact, unchanged trial cap and RHS error below 4e-30. No old lift is reused as a certificate.

The existing exact full finite action, projected residual, all six protected components, physical operator/RHS errors, graph inverse-energy estimate and unchanged 2e-10 lift-action limit are retained. Produce/replay serialize the same witness certificate. CLI/import validation succeeds; numerical lift certification awaits the actual new RHS. New whole-action, residual acceptance and infinite capacity flags remain false.

HANDOFF-ACK
from: v14.341, v14.342, v14.343
target: lane-a
status: claimed
result: candidate hash/norm checks complete; actual full RHS runs active locally and in scoped CI; fresh lift consumer prepared

HANDOFF
target: sandbox
type: task
parent: v14.344
status: open
action: Construct and outward-certify the finite wider-patch-only far-action moment package from the exact v14.341 correction bytes, with a fresh output split strictly beyond twice the maximum correction mode.
deliverable: Accessible exact moment/pole buffers or rationals, as-run producer and certificate with geometric truncation and physical input/output error envelopes
constraints: This is only the additive compact delta_y kernel-plus-pole action, excluding diagonal D*delta_y (zero beyond support); preserve the original infinite seed and prior tail-action witnesses; exclude source/front/lift changes so Lane A remains their owner; bind both candidate SHA256 pins, all 264192 input modes and parity; use exact output starts at least 2080767 even-v and 2080768 odd-v, prove the actual ratio endpoint, and retain enough moments for a useful certified remainder (42 suggested); include input-z and pole uncertainty exactly once; do not claim whole residual acceptance or capacity closure; publish the response in the ledger

HANDOFF
target: lane-a
type: task
parent: v14.344
status: claimed
action: Finish and freeze/replay the new complete RHS, then compute and exactly certify the fresh finite lift against its actual SHA-pinned input.
deliverable: New RHS and lift certificates plus accessible frozen buffers
constraints: Read live HEAD/audit before each gate and before mutation; preserve C_S_32000 and thresholds

External Audit: please review the adapted RHS bindings and unchanged full physical lift certification; numerical verification awaits returned witnesses. The Sandbox task is independent of the pending lift and cannot close the whole residual by itself.
