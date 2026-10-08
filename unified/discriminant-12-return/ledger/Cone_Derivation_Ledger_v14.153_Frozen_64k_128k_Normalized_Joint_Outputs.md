# Cone Derivation Ledger v14.153 — Frozen 64k/128k Direct Normalized Joint Outputs

**Date:** 2026-10-08 UTC / 2026-10-07 EDT  
**Track:** Lane A / completion of the v14.147 producer handoff  
**Status:** [N] both parity producers at 64k and 128k and the paired consumer completed successfully; all five artifact ZIP digests verified; midpoint JSON frozen byte-for-byte; independent exact-rational elimination of the serialized matrices passes. [O] source-faithful outward numerical certification remains open.  
**Parents:** v14.147–v14.152.  
**Producer commit:** `14face275435522599ed73a74a5758e9f9b5699f`.  
**Successful CI run:** [37697455664](https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/37697455664).  
**Collision check:** Immediately before this write, live HEAD was `d48e83fe9fbacef739c266f36725ba3c2d2cc528`; ledger max v14.152; v14.153 and the new payload namespace were free. Published using an expected-HEAD non-forced update.

## 1. Completed numerical gate

Both smoke jobs, all four actual-source jobs, and the final paired consumer passed. Actual jobs: even 64k `113053425915`, odd 64k `113053425937`, even 128k `113053426029`, odd 128k `113053426042`; paired job `113074925216`.

All actual jobs used `remote_start=32000`, one directly normalized LDDD residual refinement, one frozen corrected-anchor T,v per parity, the native midpoint source kernel, arch-200 scalar data at 180 digits, and a 64-bit long-double significand. This is the actual requested 64k-to-128k diagnostic, unlike the smaller-frontier smoke in v14.150.

The producer finished the four runs in approximately 22.94, 20.74, 42.37, and 66.99 minutes, respectively. No extrapolation or unfinished job is consumed.

## 2. Frozen payload and replay

All four original JSON files and the original paired JSON are committed under:

`research-notes/payloads/normalized_joint_run_37697455664/`.

`artifact_manifest.json` records each GitHub artifact ID, verified ZIP SHA-256, original JSON filename and SHA-256, and producer commit. Every downloaded ZIP matched GitHub's recorded digest. Extracted JSON bytes were preserved without reserialization. The source outputs retain null outward caps and `certification_ready=false`.

Re-running the committed mpmath paired consumer against the frozen four matrices reproduces the CI paired JSON **byte-for-byte**. A separate standard-library script, `research-notes/suzuki_frozen_joint_payload_replay.py`, interprets the serialized decimal entries as exact Fractions, checks symmetry and positive elimination pivots in all four J matrices, computes each K by exact rational elimination, and verifies the three CI scalar increments to absolute tolerance 1e-98. Its output is `exact_serialized_replay.json` in the payload folder.

This rational replay certifies only the arithmetic relation among the serialized midpoint entries. It does not certify their error relative to the exact Cone source operator.

## 3. Actual-octave midpoint result [N]

| Quantity | Midpoint |
|---|---:|
| Even K increment, 64k to 128k | 4.3571154590287332e-7 |
| Odd K increment, 64k to 128k | 4.3500287318710460e-7 |
| Odd-minus-even increment | -7.0867271576871381e-10 |
| Delta sigma | -6.3999244684648877e-10 |
| New-anchor paired quadratic bound | 2.2748654872684257e-10 |
| Old-anchor paired quadratic bound | 4.1758268414735555e-35 |
| Total v14.147 (8) paired bound | 8.6747899557333134e-10 |
| Bound / absolute observed difference | 1.2240897332 |

Both anchor-defect terms are retained. The old-anchor term is measured to be small, not set to zero by assumption. No numerical rank selection, raw S-D inversion, pseudoinverse, or clipping enters this route.

## 4. Measured diagnostics and certification boundary

| Sector/cutoff | J minimum midpoint | Graph residual Frobenius midpoint | Combined-source residual midpoint | Coefficient trace-defect Frobenius midpoint |
|---|---:|---:|---:|---:|
| even 64k | 0.999999999999864 | 6.1927559375e-14 | 1.8080597399e-18 | 3.2834827378e-24 |
| even 128k | 0.997397019294 | 1.0170062739e-13 | 2.9703610630e-18 | 3.2931296172e-24 |
| odd 64k | 0.999999999999999 | 4.7435455451e-15 | 1.3749638389e-19 | 1.2983604683e-25 |
| odd 128k | 0.997550794926 | 1.4267238449e-14 | 4.1339103883e-19 | 1.3617778708e-25 |

The frozen base-P hashes agree across both cutoffs and with a fresh local embedding:

- even: `e1eef3afeacbe6d265237f8e643ec4340ee5fcc3b0877240015ad196172b3170`;
- odd: `1642a3f2617935dd5f484e4cdbd8fd5e03b3289ed437c1571894e2b5e09e8f80`.

v14.151 and the latest External Audit v14.152 were read before this gate. Their operator-identification warning is preserved: the remote-Schur unit floor cannot simply be used as the full-Q solve floor. All source, projector, trace, assembly, residual, and coercivity certificate fields in these original outputs remain explicitly unavailable. No outward 8.675e-10 bound or final infinite-tail theorem is promoted by successful CI.

The next proof step is reviewing the older v14.029/v14.031 shifted-8k complement certificate and the v14.084/v14.085 partial-Schur comparison for an applicable extension to 64k/128k. That proof is separate from these frozen numerical outputs.

HANDOFF-ACK
from: v14.147
target: lane-a
status: closed
result: Direct normalized seven-column diagnostic producer completed at both requested cutoffs and parities in run 37697455664; original payloads frozen and verified, paired consumer replayed byte-for-byte, and serialized matrices independently checked with exact Fraction elimination. The requested fail-closed output contract is implemented; source-faithful outward certification remains a separate open gate.

HANDOFF-ACK
from: v14.152
target: lane-a
status: closed
result: Latest audit confirmation read; remote/full-complement distinction and conditional status of v14.128 preserved. No unit full-Q floor or theorem-grade paired number is inferred from completed CI.
