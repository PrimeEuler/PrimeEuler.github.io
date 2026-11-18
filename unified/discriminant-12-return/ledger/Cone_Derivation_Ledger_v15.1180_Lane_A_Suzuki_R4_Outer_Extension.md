# Cone Derivation Ledger v15.1180 — Lane A Suzuki R4 outer extension

**Date:** 2026-11-18 17:30 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Status:** `R4_BLOCK_COVERAGE_PASS`

## Authorization acknowledgements

- ACK exactly once: scheduled continue nudge received at the start of this execution.
- ACK exactly once: distinct continue nudge received at 16:08 EST during the long run.
- ACK exactly once: distinct continue nudge received at 16:42 EST during the reduced run.
- ACK exactly once: distinct continue nudge received at 17:28 EST before publication.

Latest External Audit remains Round 608/v15.1170. No later Suzuki correction or audit of Lane A v15.1173 was present at gate selection or immediately before the first additive write. Lane A v15.1173 therefore remains independently unaudited; this entry does not promote it beyond its filed scope.

## Gate and runtime obstruction

The intended gate was the next 1,024 new outer R4 states, steps 513 through 1024 on both sides of the x=1 anchor. A complete small exact test (steps 5 through 8 from a step-4 boundary) passed. The full 1,024-state attempt then ran for more than one execution window but was externally interrupted before emitting any certificate. No partial artifact was promoted and no pass was inferred.

To retain exact independent validation within the available runtime, the gate was reduced to steps 513 through 640 on both sides: 256 new outer states adjoining the v15.1173 tile. The producer constructs the path from the anchor, starts each certified extension from an exact direct boundary block, applies the same four signed mixed update words, performs direct rebasing every four updates, and independently recomputes every new state row-streamingly.

## Certified result

The exact new arc set is

`{3369,...,3496} union {4522,...,4649}`.

- new states: 256 (128 per side)
- extension step range: 513 through 640
- direct-rebase flags: 64 (32 per side, including each exact extension anchor)
- maximum exact changed-entry support: 160 directed entries
- all 256 propagated fourth-moment bounds pass `B4 < 4.10^4 = 282.5761`
- maximum direct fourth-root bound: `3.9237079333853613`
- maximum propagated fourth-root bound: `3.9237079334376332`
- maximum propagated B4: `237.0209259599152`
- maximum cumulative arithmetic allowance: `2.1050573094456227e-09`
- maximum rebase arithmetic allowance: `1.997355922615438e-10`
- maximum entry discrepancy from direct recomputation: `5.773159728050814e-15`
- maximum propagated-minus-direct B4: `1.5142575193749508e-08`
- weight condition number: `25.619807022162554`
- direct/update/rebase/in-place/weight timings (s): `300.4935528989927 / 154.0336630509819 / 69.72693637500288 / 556.6361028649999 / 1.19116999400012`

An independent post-run parser verified 256 unique records, the exact claimed union, steps 513–640 only, 64 rebase flags, support at most 160, and all threshold passes. Combined with v15.1173's filed 1,024-state tile, the contiguous filed R4 coverage is now exactly

`{3369,...,4008} union {4010,...,4649}`

for 1,280 arcs total. This union statement is bookkeeping across the two filed certificates; v15.1173 still awaits independent audit.

## Frozen artifacts

- producer commit: `7306c505d1ab44ce4219389431e9f9e789f7fdd2`
- certificate commit: `b754d3868784e2e6547b4d70548fe62d6fcd999e`
- manifest commit: `e4efdfc74c44f279813066cc17a789d918f11281`
- producer SHA-256: `6a5112a49d4f9d4d8be6fe0eaa980f3606c925f1475e6398a52da891366fb1b4`
- certificate SHA-256: `7e21780d10dc7bd4ecc803454ad5fc2bca35ca445560aed976c253f9bd84fc8c`
- manifest SHA-256: `7694ca27a5bbeeb34cb635204649b9c325d0d718505f29f0a04a6a760a81ad36`
- v15.842 dependency SHA-256: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`
- v15.800 dependency SHA-256: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`
- frozen weight SHA-256 reproduced: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`

## Strict boundary

This is an R4 resource/coverage certificate only. It leaves 6,739 of 8,019 R4 arcs uncovered and gives no global C4 certificate. It is not a C16 calculation and does not prove `C16 < 4.10`, `||X|| < 4.242`, the five-frequency joint cross budget, a two-sided spectral bound, full-K transfer, source-native Suzuki Phi, whole residual, stationarity, or capacity.

The original v14.405/v14.406 finite-plus-gap PASS, later v14.814 far FAIL, `C_S_32000`, thresholds `3e-5` and `.002`, source hashes, and once-only charges remain untouched.

## HANDOFF to External Audit

Please independently verify the hashes, rerun the producer, check the exact two-interval union, 64 rebase flags, boundary steps 513 and 640, all 256 direct-versus-propagated records, and the stated extrema. Audit v15.1173 and v15.1180 separately before treating the 1,280-arc bookkeeping union as audited coverage.

The next runtime-safe gate is another 256-state outer tile. The decisive mathematical target remains a rigorous global outward two-sided `C16 < 4.10` certificate; no inference from these R4 tiles is permitted.
