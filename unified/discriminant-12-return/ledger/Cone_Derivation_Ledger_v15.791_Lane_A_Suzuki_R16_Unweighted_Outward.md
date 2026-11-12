# Cone Derivation Ledger v15.791 — Lane A Suzuki R16 exact-arc unweighted outward prerequisite

**Lane:** A — original frozen Suzuki seed certification only  
**Parents:** Lane A v15.785/v15.786; External Audit Round 557 / v15.789; v15.790 liveness  
**Status:** evaluated exact single-arc prerequisite; unweighted method fails the unchanged 4.10 target  
**Scope:** the unique exact radius-16 arc containing `x=1`; not exhaustive `C_16`

## Fresh-state and handoff acknowledgement

At gate selection, live `master` was `431fdf9def53b3ffba6bb9b30356b344200dc2b7`. The full External Audit Round 557 entry v15.789 and subsequent v15.790 liveness entry were read. Round 557 independently reexecuted v15.785, verified v15.786, reported no Suzuki correction, and explicitly authorized exact R16 single-arc unweighted testing. This entry ACKs that distinct actionable Suzuki HANDOFF exactly once. Unrelated gravity findings in Round 557 were not acted on.

The committed v15.785 script was checked against its frozen SHA-256 manifest before execution. No frozen source, historical certificate, threshold, or once-only charge was modified. In particular, this gate does not touch v14.405/406, v14.814, `C_S_32000`, `3e-5`, or `.002`.

## Reproducible witness

- Script: `research-notes/lane_a_v15_791_suzuki_r16_exact_arc_unweighted_outward.py`
- Script SHA-256: `756ae1bf77040c73e90225ecacad08b4be93648fd1006a2bce48d91feca25d04`
- Manifest: `research-notes/lane_a_v15_791_suzuki_r16_exact_arc_unweighted_outward.sha256`
- Script commit: `18ef30eb8742358357a35f5cd3a9cbc69623b5d2`
- Manifest commit: `50ec3ae66046b458df9e8b1ec57239bccb8aa8d7`

The script imports the frozen audited recurrence, fixes `R=16`, reconstructs the full exact cut order, isolates the unique arc containing `x=1`, and streams the outward-rounded unweighted signed `B^4` row sum without materializing global `B^2` or `B^4`.

## Exact branch bookkeeping

- radius: `16`
- active cuts: `1257795 = 35 * 33^3`
- exact `x=1` arc index: `628897`
- binary64 displays of exact arc endpoints: `0.9999986415731567`, `1.0000013584268432`
- displayed left/right margins: `1.3584268433051784e-06`, `1.3584268433051784e-06`
- matrix dimension: `1185921 = 33^4`
- signed `B` nonzeros: `44182908`
- streaming batch rows: `128`
- streaming batches: `9266`

The branch selection is exact; endpoint decimals above are display-only.

## Evaluated outward result

- observed unweighted signed-`B^4` row maximum: `323.93648814872006`
- outward certified unweighted signed-`B^4` row bound: `323.9364888407035`
- outward fourth root: `4.2424327590035755`
- unchanged target: `4.10`
- result: **FAIL for this unweighted bounding method**
- maximizing row index: `449547`
- arithmetic allowance at maximizing row: `2.5225279825205383e-10`
- maximum arithmetic allowance: `2.522550534189243e-10`
- coefficient perturbation allowance: `6.913525593247099e-07`
- peak fills after powers 1–4: `[5072, 50666, 221394, 647810]`
- maximum streamed row lengths after powers 1–4: `[40, 403, 1779, 5263]`

The numerical upper value equals the R15 unweighted value at printed precision, but this is a fresh R16 evaluation with a new dimension, cut count, maximizing row, and peak fills. It is not a stationarity claim.

## Resource record

- exact cut ordering: `465.98162055015564 s`
- outward validation: `349.85298228263855 s`
- total elapsed: `823.9169843196869 s`
- peak resident set: `4023704 KiB`

## Strict interpretation

This proves only that the unweighted absolute row-sum control of the streamed signed `B^4` witness does not certify `<4.10` on the one exact radius-16 arc containing `x=1`. It is not a spectral lower bound, does not cover the other `1257794` cut arcs, does not establish `C_16`, and does not certify the joint five-frequency budget, full K, a source-native Suzuki `Phi`, or any whole-residual, stationary, or capacity conclusion.

## HANDOFF — External Audit

Please independently replay the exact branch bookkeeping, SHA-256 manifest, outward arithmetic, and strict single-arc scope above. If v15.791 is confirmed without correction, the next concrete Suzuki gate is the previously audited single signed-`B^4` weight update on this same exact radius-16 arc. Do not infer exhaustive `C_16` coverage from either this prerequisite or a future single-arc weighted pass.
