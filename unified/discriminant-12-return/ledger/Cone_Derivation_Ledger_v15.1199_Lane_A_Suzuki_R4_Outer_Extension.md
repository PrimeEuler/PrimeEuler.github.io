# Cone Derivation Ledger v15.1199 — Lane A Suzuki R4 outer extension

**Date:** 2026-11-18 21:20 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Status:** `R4_BLOCK_COVERAGE_PASS`

## Authorization acknowledgements

- ACK exactly once: scheduled continue nudge received at the start of this execution.
- ACK exactly once: distinct scheduled continue nudge received at 20:29 EST.
- ACK exactly once: distinct scheduled continue nudge received at 21:02 EST.
- ACK exactly once: distinct scheduled continue nudge received at 21:16 EST.

Latest External Audit remains Round 608/v15.1170 (`1f40b89d40c21682391f2d5123491ffc8d4d5480`). Its full correction text was read before gate selection; it contains no Suzuki correction and ends with the actionable authorization that Lane A should continue. No later audit of Lane A v15.1173 or v15.1180 was present at gate selection or immediately before publication. Those entries therefore remain independently unaudited, and this entry does not promote them beyond their filed scopes.

## Gate and runtime obstruction

The first intended gate was the next 256 outer R4 states, steps 641 through 768 on both sides of the x=1 anchor. That execution was interrupted across an execution boundary before emitting any certificate. No partial artifact was promoted and no pass was inferred.

To remain inside the observed runtime budget, the gate was reduced to steps 641 through 704 on both sides: 128 new outer states adjoining v15.1180. The producer constructs the path from the anchor, starts each certified extension from an exact direct step-640 boundary block, applies the same four signed mixed update words, performs direct rebasing every four updates, and independently recomputes every new state row-streamingly.

## Certified result

The exact new arc set is

`{3305,...,3368} union {4650,...,4713}`.

- new states: 128 (64 per side)
- extension step range: 641 through 704
- direct-rebase flags: 32 (16 per side, including each exact extension anchor)
- maximum exact changed-entry support: 160 directed entries
- all 128 propagated fourth-moment bounds pass `B4 < 4.10^4 = 282.5761`
- maximum direct fourth-root bound: `3.9123615466882566`
- maximum propagated fourth-root bound: `3.9123615467282233`
- maximum propagated B4: `234.29117309557083`
- maximum cumulative arithmetic allowance: `2.0021637762776946e-09`
- maximum rebase arithmetic allowance: `1.9875246450545048e-10`
- maximum entry discrepancy from direct recomputation: `3.1086244689504383e-15`
- maximum propagated-minus-direct B4: `1.433156171515293e-08`
- weight condition number: `25.619807022162554`
- direct/update/rebase/in-place/weight timings (s): `153.2030594709995 / 80.1274332310154 / 35.01113071401778 / 288.2249472939998 / 1.165735189000003`

An independent post-run parser verified 128 unique records, the exact claimed union, steps 641–704 only, 32 rebase flags, support at most 160, and all threshold passes. Combined with the filed v15.1173 and v15.1180 certificates, the contiguous filed R4 coverage is now exactly

`{3305,...,4008} union {4010,...,4713}`

for 1,408 arcs total, leaving 6,611 of 8,019 R4 arcs uncovered. This union statement is bookkeeping across three filed certificates; v15.1173 and v15.1180 still await independent audit.

## Frozen artifacts

- producer commit: `859a2e92812d41161779055cc950646441272183`
- certificate commit: `77053ada5138f28c4050c44f2352e78cebc345e8`
- manifest commit: `804f733a769a6af57559fd00da3673eb0a7aaa50`
- producer SHA-256: `dad1f2baaa09a6a866521823ccfeb4ea261943df735ad97846506c6bd4a960a0`
- certificate SHA-256: `2ab0abd2b66d908cdb6864b65a11f78361babe646cd04b573b47394aba0ec9c5`
- manifest SHA-256: `65ca336438d6146ee7c08688da8e16ebca0f2499d8d9c7c389038679f50b3e89`
- v15.842 dependency SHA-256: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`
- v15.800 dependency SHA-256: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`
- frozen weight SHA-256 reproduced: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`

## Strict boundary

This is an R4 resource/coverage certificate only. It gives no global C4 certificate. It is not a C16 calculation and does not prove `C16 < 4.10`, the joint five-frequency cross budget, full Suzuki closure, source-native Phi, whole-residual, stationary, or capacity claims. No conclusion is drawn from rank alone, sampled eigenvalues, or a one-x probe. The frozen v14.405/v14.406 finite-plus-gap PASS, v14.814 far FAIL, original `C_S_32000`, `3e-5`, `.002`, source hashes, and once-only charges remain untouched.

## External Audit handoff

Please independently replay the producer and verify the manifest, exact arc union, boundary steps 641 and 704, 32 rebase flags, support at most 160, all 128 direct-versus-propagated records, and the stated extrema. Audit v15.1173, v15.1180, and v15.1199 separately before treating the 1,408-arc bookkeeping union as audited coverage.

The next runtime-safe gate should not exceed 128 new outer states under the present execution budget. The decisive mathematical target remains a rigorous global outward two-sided `C16 < 4.10` certificate; no inference from these R4 tiles is permitted.
