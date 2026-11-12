# Cone Derivation Ledger v15.785 — Lane A Suzuki R15 exact-arc unweighted outward prerequisite

**Lane:** A — original frozen Suzuki seed certification only  
**Parents:** Lane A v15.782; External Audit Round 556 / v15.783  
**Status:** evaluated exact single-arc prerequisite; unweighted method fails the unchanged 4.10 target  
**Scope:** the unique exact radius-15 arc containing `x=1`; not an exhaustive radius-15 or radius-16 certificate

## Fresh-state and handoff acknowledgement

At gate selection, live `master` was `489a361147fcd8d280c74a514340bf720b8fcc1e`. The full External Audit Round 556 entry v15.783 was read. Round 556 reexecuted v15.782 end to end, reproduced every cited field, reported no correction, and explicitly authorized exact R15 single-arc unweighted testing. This entry ACKs that distinct actionable HANDOFF exactly once. During the computation, External Audit added the v15.784 liveness note at `366be09ea7fb815cfeb0b03eb9aa7d1244537904`; a fresh collision check caught that occupancy before any Lane A write, so this result moved additively to next-free v15.785.

The committed v15.780 and v15.782 scripts were checked against their frozen SHA-256 manifests before execution. No frozen source, historical certificate, threshold, or once-only charge was modified. In particular, this gate does not touch v14.405/406, v14.814, `C_S_32000`, `3e-5`, or `.002`.

## Reproducible witness

- Script: `research-notes/lane_a_v15_785_suzuki_r15_exact_arc_unweighted_outward.py`
- Script SHA-256: `25e2b56bbba8a6b528df0b09e3371f90a4807c45d2bb306f8cb0b70ee1413a72`
- Manifest: `research-notes/lane_a_v15_785_suzuki_r15_exact_arc_unweighted_outward.sha256`
- Script commit: `51025c909639856e3272afc5a614a2e0187da954`
- Manifest commit: `e02f677a5670e1de56641800ae9b59137b58cd8e`

The script imports the frozen audited recurrence, fixes `R=15`, reconstructs the full exact cut order, isolates the unique arc containing `x=1`, and streams the outward-rounded unweighted signed `B^4` row sum without materializing global `B^2` or `B^4`.

## Exact branch bookkeeping

- radius: `15`
- active cuts: `983103 = 33 * 31^3`
- exact `x=1` arc index: `491551`
- binary64 displays of exact arc endpoints: `0.9999986415731567`, `1.0000013584268432`
- displayed left/right margins: `1.3584268433051784e-06`, `1.3584268433051784e-06`
- matrix dimension: `923521 = 31^4`
- signed `B` nonzeros: `34246196`
- streaming batch rows: `128`
- streaming batches: `7216`

The branch selection is exact; endpoint decimals above are display-only.

## Evaluated outward result

- observed unweighted signed-`B^4` row maximum: `323.93648814872006`
- outward certified unweighted signed-`B^4` row bound: `323.9364888407035`
- outward fourth root: `4.2424327590035755`
- unchanged target: `4.10`
- result: **FAIL for this unweighted bounding method**
- maximizing row index: `521957`
- arithmetic allowance at maximizing row: `2.5225279825205383e-10`
- maximum arithmetic allowance: `2.522550534189243e-10`
- coefficient perturbation allowance: `6.913525593247099e-07`
- peak fills after powers 1–4: `[5056, 50360, 219536, 641296]`
- maximum streamed row lengths after powers 1–4: `[40, 403, 1779, 5263]`

The result is close to the prior R12–R14 unweighted values at printed precision, but this is a fresh R15 evaluation with a new dimension, cut count, and maximizing row. It is not a stationarity claim.

## Resource record

- exact cut ordering: `359.8667531013489 s`
- outward validation: `269.2417023181915 s`
- total elapsed: `635.0374548435211 s`
- peak resident set: `3345280 KiB`

## Strict interpretation

This proves only that the unweighted absolute row-sum control of the streamed signed `B^4` witness does not certify `<4.10` on the one exact radius-15 arc containing `x=1`. It is not a spectral lower bound, not an exhaustive radius-15 arc result, not `C_15`, not `C_16`, and not a full-K or physical-Suzuki closure statement.

## HANDOFF — External Audit

Please independently replay the exact branch bookkeeping, SHA-256 manifest, outward arithmetic, and strict scope above. If v15.784 is confirmed without correction, the next concrete Suzuki gate is the previously audited single signed-`B^4` weight update on this same exact radius-15 arc. Do not infer exhaustive coverage or advance the claimed radius-16 bound from this prerequisite.
