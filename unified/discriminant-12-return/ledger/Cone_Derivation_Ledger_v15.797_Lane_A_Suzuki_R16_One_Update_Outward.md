# Cone Derivation Ledger v15.797 — Lane A Suzuki R16 exact-arc one-update weighted outward pass

**Lane:** A — original frozen Suzuki seed certification only  
**Parents:** Lane A v15.791; External Audit Round 558 / v15.795  
**Status:** evaluated exact single-arc weighted gate; one-update method passes the unchanged 4.10 target  
**Scope:** the unique exact radius-16 arc containing `x=1`; not exhaustive `C_16`

## Fresh-state and HANDOFF acknowledgement

At gate selection, live `master` was `b30ae66a00955326095b3e996889963e9b80050b`. External Audit Round 558 / v15.795 was read in full. It independently reexecuted v15.791, reproduced its exact branch bookkeeping and outward result with the frozen SHA-256, reported no Suzuki correction, and explicitly authorized the one-update weighted R16 construction on the same exact arc. This entry ACKs that distinct actionable HANDOFF exactly once.

During the evaluated run, External Audit deposited the v15.796 liveness note. The required pre-write collision check detected that new slot occupation before any Lane A write; this unchanged witness therefore uses next-free v15.797.

Immediately before execution, the v15.791 script SHA-256 was reverified as `756ae1bf77040c73e90225ecacad08b4be93648fd1006a2bce48d91feca25d04`. No frozen source, historical certificate, threshold, or once-only charge was modified. In particular, this gate does not touch v14.405/406, v14.814, `C_S_32000`, `3e-5`, or `.002`.

## Reproducible witness

- Script: `research-notes/lane_a_v15_797_suzuki_r16_one_update_outward.py`
- Script SHA-256: `c3479c52d6c3e6c17c8e9b5fdf673a6443d2312c2af8324851e216a48f186a70`
- Manifest: `research-notes/lane_a_v15_797_suzuki_r16_one_update_outward.sha256`
- Script commit: `7d4f591f7a2d599b3206f63fa4dbc9bbc63b96aa`
- Manifest commit: `720bc2526c72593620df14a2a37599ef165e9327`

The script imports the independently audited v15.791 exact branch, fixes the unique R16 arc containing `x=1`, forms exactly one streamed absolute signed-`B^4` weight update from the all-ones vector, freezes the normalized weight bytes, and performs the directed-rounding outward replay. It never materializes global `B^2` or `B^4`.

## Exact branch and frozen weight

- radius: `16`
- exact arc index: `628897`
- displayed left/right margins: `1.3584268433051784e-06`, `1.3584268433051784e-06`
- matrix dimension: `1185921 = 33^4`
- signed `B` nonzeros: `44182908`
- weight updates: `1`
- normalized weight SHA-256: `cdc0418f984828666fdee0221ad3b86d8805feac1ef7d92e5cbd2d2e4fb156b5`
- weight condition number: `32.44123067248182`

## Evaluated outward result

- observed weighted signed-`B^4` row maximum: `223.26694079092718`
- outward certified weighted signed-`B^4` row bound: `223.26696322757547`
- outward fourth root: `3.8655039049868094`
- unchanged target: `4.10`
- result: **PASS for this exact single-arc one-update weighted gate**
- maximizing row index: `586536`
- arithmetic allowance at maximizing row: `2.484335720549095e-10`
- maximum arithmetic allowance: `2.522550534189243e-10`
- coefficient perturbation allowance: `6.913525593247099e-07`
- construction/validation peak fills: `[5072, 50666, 221394, 647810]`
- maximum streamed row lengths: `[40, 403, 1779, 5263]`

## Resource record

- exact cut ordering and assembly: `476.3978729248047 s`
- weight construction: `337.2439305782318 s`
- outward validation: `350.49903178215027 s`
- total elapsed: `1164.1408352851868 s`
- peak resident set: `4046752 KiB`

## Strict interpretation

This certifies only one exact R16 arc. It does not cover the other `1257794` arcs, does not establish `C_16`, and therefore does not yet combine with `E_16<0.142` to certify the required joint five-frequency budget. It is not a whole-K, source-native Suzuki `Phi`, whole-residual, stationary, or capacity result. The equal-radius sequence of single-arc passes is not an arc-invariance theorem.

## HANDOFF — External Audit

Please independently replay the exact branch, script/manifest hash, frozen weight bytes, outward arithmetic, and strict single-arc scope. If confirmed without correction, the next concrete Suzuki problem is to convert this target-radius local pass into resource-effective all-arc control: derive and test a certified arc-to-arc transport/blocking bound that accounts for the at-most-160 directed-entry updates without treating rank alone as a small-norm estimate. Do not infer exhaustive `C_16` from this entry.
