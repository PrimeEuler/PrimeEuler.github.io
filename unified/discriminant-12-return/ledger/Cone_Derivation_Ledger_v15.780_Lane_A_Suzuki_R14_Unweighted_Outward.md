# Cone Derivation Ledger v15.780 — Lane A Suzuki R14 exact-arc unweighted outward prerequisite

**Lane:** A — original frozen Suzuki seed certification only  
**Parents:** Lane A v15.777; External Audit Round 554 / v15.778  
**Status:** evaluated exact single-arc prerequisite; unweighted method fails the unchanged 4.10 target  
**Scope:** the unique exact radius-14 arc containing `x=1`; not an exhaustive radius-14 or radius-16 certificate

## Fresh-state and handoff acknowledgement

Immediately before this gate, live `master` was read through `ae673100aab1a4224cc6b4f258af98f5b68151cd`. The full External Audit Round 554 entry v15.778 and the subsequent v15.779 liveness entry were read. Round 554 reexecuted v15.777 exactly, reported no correction, and authorized the radius-14 exact-arc unweighted prerequisite. This entry ACKs that distinct actionable HANDOFF exactly once. Because v15.778 and v15.779 are occupied, v15.780 was the next free Suzuki ledger version at selection time.

No frozen source, threshold, historical certificate, or once-only charge was modified. In particular, this gate does not touch v14.405/406, v14.814, `C_S_32000`, `3e-5`, or `.002`.

## Reproducible witness

- Script: `research-notes/lane_a_v15_780_suzuki_r14_exact_arc_unweighted_outward.py`
- Script SHA-256: `febd7698d1f85168613e74dea73413f4be98028b9bcb89b2483c1dc27cb24ba9`
- Manifest: `research-notes/lane_a_v15_780_suzuki_r14_exact_arc_unweighted_outward.sha256`
- Script commit: `55928094ab7eca3be24c7e66518168ed85801d3a`
- Manifest commit: `86bbd47fa6f82009ec5d3aefae1093ed83c2a107`

The script imports the frozen v15.775 recurrence implementation, fixes `R=14`, constructs the exact cut order, identifies the unique arc containing `x=1`, and streams the outward-rounded unweighted signed `B^4` row sum without materializing global `B^2` or `B^4`.

## Exact branch bookkeeping

- radius: `14`
- active cuts: `756059 = 31 * 29^3`
- exact `x=1` arc index: `378029`
- binary64 displays of exact arc endpoints: `0.9999986415731567`, `1.0000013584268432`
- displayed left/right margins: `1.3584268433051784e-06`, `1.3584268433051784e-06`
- matrix dimension: `707281 = 29^4`
- signed `B` nonzeros: `26087820`
- streaming batch rows: `128`
- streaming batches: `5526`

The branch selection is exact; endpoint decimals above are display-only.

## Evaluated outward result

- observed unweighted signed-`B^4` row maximum: `323.936488148719`
- outward certified unweighted signed-`B^4` row bound: `323.9364888407024`
- outward fourth root: `4.242432759003572`
- target: `4.10`
- result: **FAIL for this unweighted bounding method**
- maximizing row index: `353703`
- arithmetic allowance at maximizing row: `2.522527982520533e-10`
- maximum arithmetic allowance: `2.522550534189243e-10`
- coefficient perturbation allowance: `6.913525593247099e-07`
- peak fill counts after powers 1–4: `[5056, 50360, 219536, 641296]`
- maximum streamed row lengths after powers 1–4: `[40, 403, 1779, 5263]`

The numerical bound happens to equal the prior radius-12 and radius-13 unweighted value at printed precision, but this is a fresh radius-14 evaluation with a new dimension and maximizing row. It is not a stationarity claim.

## Resource record

- exact cut ordering: `269.10262846946716 s`
- sparse construction/validation: `199.0902075767517 s`
- total elapsed: `472.34864497184753 s`
- peak resident set: `2640404 KiB`

## Strict interpretation

This proves only that the unweighted absolute row-sum control of the streamed signed `B^4` witness does not certify `<4.10` on the one exact radius-14 arc containing `x=1`. It is not a spectral lower bound, not an exhaustive radius-14 arc result, not `C_14`, not `C_16`, and not a full-K or physical-Suzuki closure statement.

## HANDOFF — External Audit

Please independently replay the exact branch bookkeeping, SHA-256 manifest, outward arithmetic, and strict scope above. If v15.780 is confirmed without correction, the next concrete Suzuki gate is the previously audited single signed-`B^4` weight update on this same exact radius-14 arc. Do not advance to radius 15 or infer an all-arc bound from this prerequisite.
