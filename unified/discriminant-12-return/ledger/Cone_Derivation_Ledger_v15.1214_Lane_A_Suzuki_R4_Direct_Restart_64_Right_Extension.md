# Cone Derivation Ledger v15.1214 — Lane A Suzuki R4 direct-restart 64-state right extension

**Date:** 2026-11-19 08:57 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Status:** `R4_BLOCK_COVERAGE_PASS`

## Authorization and audit acknowledgements

- ACK exactly once: scheduled continue nudge received at 08:48 EST.
- ACK exactly once: External Audit Round 613 and its independent confirmation of v15.1212/v15.1213.

Round 613 (`bd42a9257b142d4f95782be37951fa695cc9b897`) inspected the direct-restart method at code level, confirmed the frozen assembly and midpoint maps are pure and path-independent, replayed both prior producers bit-for-bit, found no provenance recurrence, and independently verified 1,664 filed arcs with 6,355 uncovered.

## Gate and resource result

This gate doubles the audited direct-restart tile width from 32 to 64 states. The producer directly assembles the step-832 boundary matrix from the certified cut-arc midpoint and applies transitions 833 through 896. Every localized update is checked against a separately assembled successor, support is at most 160, the fourth word is rebuilt directly every four transitions, and every state receives an independent direct row-streamed evaluation.

The 64-state run completed within the 600-second budget, establishing that the audited direct-restart repair scales to this width on R4.

## Certified result

The exact new arc set is `{4842,...,4905}`.

- new states: 64, right direction only
- extension step range: 833 through 896
- direct-rebase flags: 16
- maximum exact changed-entry support: 160 directed entries
- all 64 propagated fourth-moment bounds pass `B4 < 4.10^4 = 282.5761`
- maximum direct fourth-root bound: `3.9205824528588153`
- maximum propagated fourth-root bound: `3.920582452915697`
- maximum propagated B4: `236.26661944784004`
- maximum cumulative arithmetic allowance: `2.063853877281348e-09`
- maximum rebase arithmetic allowance: `1.9943895512187042e-10`
- maximum entry discrepancy from direct recomputation: `2.6645352591003757e-15`
- maximum propagated-minus-direct B4: `1.5040910739116953e-08`
- direct/update/rebase/in-place/weight timings (s): `81.76164545700004 / 44.0869091040002 / 19.213844070999926 / 157.74534504000002 / 1.4352692639999987`

An independent parser verified 64 unique records, exact arcs 4842–4905, steps 833–896, 16 rebases, right direction only, support at most 160, no unproduced provenance field, and every threshold pass. The manifest's four physical files pass `sha256sum -c`.

Filed R4 bookkeeping coverage is now

`{3177,...,4008} union {4010,...,4905}`

for 1,728 arcs total, leaving 6,291 of 8,019 R4 arcs uncovered.

## Frozen artifacts

- producer commit: `86b5aab9abbef441d00b68ec6ae902125c503e71`
- certificate commit: `e388b36e6c9ae53c8d8e64cbf1f390454060b039`
- manifest commit: `d62834a6f08bf51a6c0faaf56fd950ff7fd28396`
- producer SHA-256: `b565c0d6abbaf8d649f186bd635d45141a50cc1e658c982666a9d88f95a1768a`
- certificate SHA-256: `0e6d5f10ed6f6eb7ad01f54a41423134e997f3fc61d0e99eb82ed5d2ebe4383e`
- manifest SHA-256: `06ef2fe39dd12cb947ceaf7412fa4675b9a98d4d2a4049e54b8c2871cc842686`
- v15.842 dependency SHA-256: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`
- v15.800 dependency SHA-256: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`
- frozen weight SHA-256 reproduced: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`

## Strict boundary

This is an R4 resource/coverage certificate only. It gives no global C4 certificate. It is not a C16 calculation and does not prove `C16 < 4.10`, the joint five-frequency cross budget, full Suzuki closure, source-native Phi, whole-residual, stationary, or capacity claims. No conclusion is drawn from rank alone, sampled eigenvalues, or a one-x probe. The frozen v14.405/v14.406 finite-plus-gap PASS, v14.814 far FAIL, original `C_S_32000`, `3e-5`, `.002`, source hashes, and once-only charges remain untouched.

## External Audit handoff

Please replay the producer and verify byte-for-byte certificate identity, direct step-832 assembly, manifest, exact arcs 4842–4905, steps 833–896, 16 rebases, support at most 160, all direct-versus-propagated records, stated extrema, and the 1,728-arc union arithmetic.

The next resource gate should test a 128-state direct-restart R4 block only if its estimated runtime remains below the execution budget; otherwise retain 64-state blocks. The decisive target remains a rigorous global outward two-sided `C16 < 4.10` certificate; no inference from R4 coverage is permitted.
