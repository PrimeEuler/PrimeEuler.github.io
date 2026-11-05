# Cone Derivation Ledger v15.412 — Lane A separate-row-max information barrier

**Date:** 2026-11-05  
**Track:** Lane A (Cone/Suzuki)  
**Status:** evaluated information-model certificate; frontier unchanged

## Nudge ACKs

- ACK exactly once: v15.410 (`3ff3c4ecc01ca39493c835ecace444e50178bbbb`), External Audit liveness/continue nudge.
- ACK exactly once: v15.411 (`185c9a92af190beea2817fcd76132c0d25b938dd`), External Audit liveness/continue nudge.

Both entries were read in full. Neither is a verification round or a mathematical certificate, and neither introduced a correction. External Audit Round 481 remains the latest completed audit round and confirmed v15.408 without correction.

## Fresh pre-gate state

Immediately before opening this gate, live `master` was `185c9a92af190beea2817fcd76132c0d25b938dd`; the v15.412 ledger and witness paths were absent, and that HEAD had no combined-status entries or associated workflow runs.

## Evaluated gate

Let the ten audited pair constants be `B_qr`, with only the separate row-function facts

`sup_X f_qr <= B_qr`

retained on a common row domain `X`. Then

`sup_X sum_qr f_qr <= sum_qr B_qr`

is sharp even in a simultaneous commutative model: take the singleton `X={*}` and set every `f_qr(*)=B_qr`. The frozen exact-interval witness evaluates

- sharp separate-maxima joint bound: `6.181771216090852`;
- required joint-cross budget from v15.405: `4.249030150943723`;
- certified excess: `1.9327410651471295`.

Therefore no theorem retaining only the ten separate row maxima can certify the required joint-cross budget. A successful next gate must retain the signed pair row functions on one shared translation/torus domain, including common extremum locations, before taking absolute values or maxima.

## Frozen witness

- Path: `unified/discriminant-12-return/witnesses/lane_a_v15_412_separate_row_max_information_barrier.py`
- Commit: `d20afd75ea28de672fba9e1a1bb6afb5e4219a1a`
- Git blob: `7affaf7fddf46a1f28bbc8d5a380b57bd6813abe`
- SHA-256: `b6396536d848ca7d16fa56ea1603da776d1411d6051ecd704d0150dbbdd8c9f2`

The witness imports the audited v15.405 exact-interval constants and replays successfully. No `C_S_32000` value or existing threshold was changed; no additional v14.354 charge or source/v14.403 transport charge was made.

## Scope discipline

This is an information-model no-go only. It is not a physical lower bound, a cancellation certificate, a whole-residual result, a complete-tail certificate, or stationary/infinite-capacity closure. The audited Lane A frontier remains `2.892017147262984`, above the unchanged target `2.535946`.
