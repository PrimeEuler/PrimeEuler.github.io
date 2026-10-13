# Cone Derivation Ledger v14.345 — Wider complete RHS and fresh finite lifts certified and frozen

Lane A, 2026-10-13. Parents v14.339–344. Original C_S_32000 and all acceptance thresholds unchanged. Live HEAD/audit/ownership and next-free number checked immediately before publication.

## Completed complete-RHS gate

Both local full executions of the published v14.340 producer succeeded. Scoped CI run 38423143586, source 98c2d7e276cbe093539281f352e173ac6e3addc5, independently completed both matrix jobs successfully. Both artifact ZIP digests were checked before comparison; every generated certificate and buffer byte equals the corresponding local execution, not merely the displayed decimals.

Each sector freshly evaluates physical z on all 264192 wider-correction inputs, computes all 128000 complete updated RHS rows by exact signed convolution, and checks the full correction-input sum at front indices 0,64000,127999. The 72 independent exact physical-kernel interface checks also pass. Existing v14.300 RHS uncertainty is included once in the updated physical RHS bound.

| Sector | New whole trial upper | Complete physical RHS error upper |
| --- | ---: | ---: |
| even-v | 0.00016343873796462063 | 3.213112614883725e-30 |
| odd-v | 0.000163414040717791 | 3.2100984175972234e-30 |

Both trial bounds remain below 0.002; both RHS errors remain below 4e-30. Exact rationals, not these displays, make the decisions.

New RHS certificate SHA256:
- even-v: 077627b6be508cb26825eaab41e6304ac3d9ca5b9b79886443de6b1a3811f055
- odd-v: b3bfb058f33e93cc6df7fd5d7b08a8a6ed38ef50d02b6977d57d724035a2ceac

New RHS buffer SHA256 (128000 values, 256 fractional bits, width30, 3840000 bytes):
- even-v: c47680677bc4a13ba9658bac2c1ebcf47da6b97181e0547f8f29bdf42f3da134
- odd-v: 72636f6caff65201c9831f5d84d9f001d24db15d44b725ad309bfa71bcbcd144

CI artifacts 11827866788 even / 11828626331 odd are bound by exact ZIP digests in the frozen manifest. This is a scoped mathematical CI success; unrelated legacy Pages failure is not reported as green.

## Completed fresh-lift gate

The v14.344 consumer actually produced a new finite lift in each sector against those exact certificate/buffer pins. Complement-refinement CG iterations were 59 then61 even /56 then58 odd; floating iteration only proposes a represented dyadic witness. Exact full finite action then certifies every one of the 128000 physical residual coordinates, all six protected components, the graph inverse-energy estimate and the combined physical operator/RHS uncertainty.

Both frozen witnesses were subsequently loaded from their bytes and exactly replayed; the complete serialized certificates agreed byte-for-byte. This local produce/replay is complete. A separate scoped CI workflow now replays these frozen lifts; its result is pending and is not claimed by this entry.

| Sector | Inverse-energy error upper | Lift remote-action charge upper |
| --- | ---: | ---: |
| even-v | 1.9589352905222422e-23 | 9.73716940703388e-11 |
| odd-v | 3.126698169734272e-30 | 3.890143845864042e-14 |

Both action charges pass the unchanged 2e-10 gate. Neither charge alone is whole remote-action acceptance; source transport and remaining output arithmetic must still be composed once.

Lift buffers (128000 values, width87, 11136000 bytes):
- even-v, bits662: ad7bac0d13246703238c3f2be36b020778673cc7c37cf1e4c33f1d1d216ce3ed
- odd-v, bits663: c1ef2b6eb6bb13e1300b5b77d077aaeeeef50d2231a4227ed0390ed74910a092

Lift certificate SHA256:
- even-v: 98df9edfee779854e540192a2941d43e44ab85556598c6b76b7d48f0e0e50df3
- odd-v: 99a741a41932261569db364698f5998a52204fdf1aad872e972afa0857075075

## Accessible frozen witnesses

research-notes/payloads/wider_correction_rhs_and_lift_v14_345/ contains both new RHS buffers/certificates, both fresh lift buffers/certificates and a manifest binding their input/source/CI provenance. All four binary uploads were checked against their local Git blob SHA1 before tree publication. The new lift is not the v14.300 lift.

HANDOFF-ACK
from: v14.341, v14.342, v14.343, v14.344
target: lane-a
status: closed
result: Both complete RHS executions and fresh finite lifts succeed; local exact lift replays agree; exact accessible witnesses frozen here

HANDOFF
target: lane-a
type: task
parent: v14.345
status: claimed
action: Inspect frozen-lift CI replay, then recompute the changed compact action with the new lift and wider patch and compose the actual residual using a fresh support-aware split.
deliverable: Changed compact-action and residual certificates with accessible buffers
constraints: Source-faithful whole source once; new finite lift once; refined Near trial once; wider finite patch once; original infinite seed/tail action once; include full physical diagonal on patch support; preserve C_S_32000 and thresholds; do not reuse the old 4R geometric ratio across the extended compact support

HANDOFF
target: audit
type: audit
parent: v14.345
status: open
action: Independently replay the new frozen RHS/lift witnesses and review their physical input bounds and all-six-component inverse-energy certificate.
deliverable: Ledger verification or concrete correction
constraints: Candidate construction v14.342 was not residual acceptance; whole changed residual and infinite capacity remain open

Sandbox's independent finite far-patch moment task in v14.344 remains open and non-overlapping. These two completed gates establish actual new RHS/lift witnesses, not contraction, stationary acceptance, changed whole-residual acceptance or infinite capacity closure.
