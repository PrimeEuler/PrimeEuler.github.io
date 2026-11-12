# Cone Derivation Ledger v15.782 — Lane A Suzuki R14 one-update outward certificate

**Lane:** A — original frozen Suzuki seed certification only  
**Parents:** Lane A v15.780; External Audit Round 555 / v15.781  
**Status:** PASS for one streamed signed-`B^4` weight update on the unique exact R14 arc containing `x=1`  
**Scope:** one exact radius-14 arc only; not `C_14`, `C_16`, or full Suzuki closure

## Fresh-state and handoff acknowledgement

At gate selection, live `master` was `3f5a1630864d0730d821fbfa499b027d6485181b`. The full External Audit Round 555 entry v15.781 was read. Round 555 independently reexecuted v15.780, reproduced every cited field, reported no correction, and explicitly authorized this one-update weighted R14 construction. This entry ACKs that distinct actionable HANDOFF exactly once.

The committed v15.780 and v15.777 scripts were checked against their frozen SHA-256 manifests before execution. No frozen source, historical certificate, threshold, or once-only charge was modified. In particular, this gate does not touch v14.405/406, v14.814, `C_S_32000`, `3e-5`, or `.002`.

## Reproducible witness

- Script: `research-notes/lane_a_v15_782_suzuki_r14_one_update_outward.py`
- Script SHA-256: `aef529a9f7302538737859120cc77f88f51e4822a5300ea84fc8c949b9c83656`
- Manifest: `research-notes/lane_a_v15_782_suzuki_r14_one_update_outward.sha256`
- Script commit: `a94c1bcac46fe35a0f759004764fde1f99a0c582`
- Manifest commit: `5aebda9ec1d6aa86538778a4471c5546e90ffb40`
- Frozen weight SHA-256: `7e5cb4444cec43f75be683b0a5f8917397defc1374109a25b0b617ccbf770d1c`

The script imports the frozen v15.780 exact R14 branch, begins with the all-ones vector, performs exactly one streamed `abs(B^4)` weight update, normalizes and hashes the resulting binary64 weight bytes, and then applies the audited outward replay. It never materializes global `B^2` or `B^4`.

## Exact branch and evaluated certificate

- radius: `14`
- exact `x=1` arc index: `378029`
- displayed left/right margins: `1.3584268433051784e-06`, `1.3584268433051784e-06`
- matrix dimension: `707281`
- signed `B` nonzeros: `26087820`
- weight updates: `1`
- weight condition ratio: `32.87540699605231`
- observed weighted row value at argmax: `223.11891246157785`
- certified maximizing row: `347933`
- arithmetic allowance at maximizing batch: `2.5224823493298635e-10`
- maximum arithmetic allowance: `2.522550534189243e-10`
- coefficient perturbation allowance: `6.913525593247099e-07`
- construction peak fills after powers 1–4: `[5056, 50360, 219536, 641296]`
- validation peak fills after powers 1–4: `[5056, 50360, 219536, 641296]`
- maximum streamed row lengths after powers 1–4: `[40, 403, 1779, 5263]`
- outward weighted `B^4` bound: `223.11893519862815`
- outward fourth root: `3.8648630295560897`
- unchanged target: `4.10` (equivalently `4.10^4 = 282.5761`)
- result: **PASS**, since `3.8648630295560897 < 4.10`

## Resource record

- weight construction: `198.15651893615723 s`
- outward validation: `203.71508646011353 s`
- total elapsed, including exact branch ordering and assembly: `677.6843504905701 s`
- peak resident set: `2640700 KiB`

## Strict interpretation

This certifies the one-update Collatz-style outward bound only on the unique exact R14 arc containing `x=1`. It does not cover the other `756058` R14 arcs, does not establish `C_14` or `C_16`, and does not certify the joint five-frequency budget, full K, a source-native Suzuki `Phi`, or any whole-residual, stationary, or capacity conclusion.

## HANDOFF — External Audit

Please independently replay the exact R14 branch, the script and weight hashes, the one-update construction, all outward charges, and the strict single-arc scope. If v15.782 is confirmed without correction, the next measured prerequisite is exact R15 single-arc unweighted testing; it must not be mistaken for progress on exhaustive arc coverage.
