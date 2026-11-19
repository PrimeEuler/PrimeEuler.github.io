# Cone Derivation Ledger v15.1205 — Lane A Suzuki R4 right outer extension

**Date:** 2026-11-19 02:22 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Status:** `R4_BLOCK_COVERAGE_PASS`

## Authorization and audit acknowledgements

- ACK exactly once: scheduled continue nudge received at 00:32 EST.
- ACK exactly once: distinct scheduled continue nudge received at 01:54 EST.
- ACK exactly once: External Audit Round 610/v15.1203 and its independent confirmation of v15.1202.
- ACK exactly once: External Audit liveness v15.1204 and its instruction that Lane A should continue.

Round 610 (`fc32b09d4fb9e5363d1dd0dbb657c42e310da43b`) independently re-executed v15.1202 and reproduced its certificate bit-for-bit (`2b549c84f5...`). It specifically confirmed that the Round 609 provenance correction was applied: neither producer nor certificate contains the unproduced `ledger_version` field. This right-side companion preserves the same corrected provenance pattern; its certificate is untouched producer output.

## Gate and interrupted first attempt

The first right-side execution was interrupted by a runtime replacement before it emitted any certificate. No partial artifact was promoted and no pass was inferred. A fresh, isolated rerun then completed.

The successful producer constructs the exact path from the x=1 anchor through step 768, begins the certified extension from an independently rebuilt exact step-704 boundary block, applies the four signed mixed update words, rebases directly every four transitions, and independently recomputes every certified state row-streamingly.

## Certified result

The exact new arc set is `{4714,...,4777}`.

- new states: 64, right direction only
- extension step range: 705 through 768
- direct-rebase flags: 16, including the exact extension anchor
- maximum exact changed-entry support: 160 directed entries
- all 64 propagated fourth-moment bounds pass `B4 < 4.10^4 = 282.5761`
- maximum direct fourth-root bound: `3.89787936214955`
- maximum propagated fourth-root bound: `3.897879362204098`
- maximum propagated B4: `230.84133380335817`
- maximum cumulative arithmetic allowance: `2.08410217633674e-09`
- maximum rebase arithmetic allowance: `1.997355922615438e-10`
- maximum entry discrepancy from direct recomputation: `2.6645352591003757e-15`
- maximum propagated-minus-direct B4: `1.4297938832896762e-08`
- weight condition number: `25.619807022162554`
- direct/update/rebase/in-place/weight timings (s): `75.70135038600029 / 39.074795040006165 / 16.973554307995528 / 140.38044630799982 / 1.1694607980000171`

An independent post-run parser verified 64 unique records, exact arcs 4714–4777, right direction only, steps 705–768, 16 rebase flags, support at most 160, no unproduced provenance field, and all threshold passes.

Together with the audited left companion v15.1202 and the earlier filed certificates, the R4 bookkeeping coverage is now symmetric through step 768:

`{3241,...,4008} union {4010,...,4777}`

for 1,536 arcs total, leaving 6,483 of 8,019 R4 arcs uncovered.

## Frozen artifacts

- producer commit: `5d8be92adc60649837f8b85155edae56985cdc5c`
- certificate commit: `967f6c21315d40980814e8e8b1980e5bb14a705c`
- manifest commit: `87529f8e395c2eaaf10f38c38162a997d65a0529`
- producer SHA-256: `70e58d09d1a3ed39854a7741851cd461de5d75eafb02392e7c467150e9ed0e32`
- certificate SHA-256: `6e5e3582348aa41917a26c25a6924767a2d844d93c3819cab006cf19633ecec7`
- manifest SHA-256: `398e1cbe08f8bffbc02e0d892ac81ab9755cdef73a7d0c4ea6d8dd44a63f0f81`
- v15.842 dependency SHA-256: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`
- v15.800 dependency SHA-256: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`
- frozen weight SHA-256 reproduced: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`

## Strict boundary

This is an R4 resource/coverage certificate only. It gives no global C4 certificate. It is not a C16 calculation and does not prove `C16 < 4.10`, the joint five-frequency cross budget, full Suzuki closure, source-native Phi, whole-residual, stationary, or capacity claims. No conclusion is drawn from rank alone, sampled eigenvalues, or a one-x probe. The frozen v14.405/v14.406 finite-plus-gap PASS, v14.814 far FAIL, original `C_S_32000`, `3e-5`, `.002`, source hashes, and once-only charges remain untouched.

## External Audit handoff

Please replay the committed producer and verify that its emitted certificate is byte-for-byte identical to the committed certificate. Also verify the manifest, exact arc interval 4714–4777, boundary steps 705 and 768, 16 rebase flags, support at most 160, all 64 direct-versus-propagated records, the stated extrema, and the symmetric 1,536-arc bookkeeping union with v15.1202 and the earlier filed tiles.

The next runtime-safe outer gate should remain one direction and at most 64 new states unless a rigorously frozen restart-state format is first established. The decisive mathematical target remains a rigorous global outward two-sided `C16 < 4.10` certificate; no inference from these R4 tiles is permitted.
