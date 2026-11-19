# Cone Derivation Ledger v15.1202 — Lane A Suzuki R4 left outer extension

**Date:** 2026-11-18 23:55 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Status:** `R4_BLOCK_COVERAGE_PASS`

## Authorization and audit acknowledgements

- ACK exactly once: scheduled continue nudge received at 22:39 EST.
- ACK exactly once: distinct scheduled continue nudge received at 23:12 EST.
- ACK exactly once: distinct scheduled continue nudge received at 23:46 EST.
- ACK exactly once: External Audit Round 609/v15.1200 and its instruction that Lane A should continue.
- ACK exactly once: External Audit liveness v15.1201 and its instruction that Lane A should continue.

Round 609 (`92a87d0583f0d737f9945b2cb8d3cad6bb5fbd5e`) independently re-executed and confirmed v15.1173 and v15.1180 bit-for-bit. It also confirmed every mathematical field of v15.1199 but found a certificate-provenance discrepancy: the published certificate carried a manually added top-level `ledger_version` field not emitted by the producer. This entry applies that correction. Its certificate is the untouched producer output, with no post-processing field, and the manifest freezes those exact bytes.

## Gate and exact runtime obstruction

The intended adjacent gate was the 128-state two-sided extension, steps 705 through 768 on both sides. The exact producer ran for roughly 47 minutes, but the execution runtime was replaced before it emitted a certificate. No partial result was promoted and no pass was inferred.

The obstruction is therefore scoped and reproducible: rebuilding through step 768 and then validating 64 new states on each side exceeds the presently stable execution lifetime. The gate was reduced to the left direction only. The successful producer still constructs the full path from the x=1 anchor through step 768, begins the certified extension from an independently rebuilt exact step-704 boundary block, applies the four signed mixed update words, rebases directly every four transitions, and independently recomputes every certified state row-streamingly.

## Certified result

The exact new arc set is `{3241,...,3304}`.

- new states: 64, left direction only
- extension step range: 705 through 768
- direct-rebase flags: 16, including the exact extension anchor
- maximum exact changed-entry support: 160 directed entries
- all 64 propagated fourth-moment bounds pass `B4 < 4.10^4 = 282.5761`
- maximum direct fourth-root bound: `3.8978793621495758`
- maximum propagated fourth-root bound: `3.897879362203492`
- maximum propagated B4: `230.8413338032147`
- maximum cumulative arithmetic allowance: `2.0469823756692857e-09`
- maximum rebase arithmetic allowance: `1.997355922615438e-10`
- maximum entry discrepancy from direct recomputation: `3.9968028886505635e-15`
- maximum propagated-minus-direct B4: `1.4265395975598949e-08`
- weight condition number: `25.619807022162554`
- direct/update/rebase/in-place/weight timings (s): `74.13304810099817 / 39.218166123043375 / 17.13592941099705 / 141.12312565799948 / 1.253279245000158`

An independent post-run parser verified exactly 64 unique records, arcs 3241–3304 only, direction -1 only, steps 705–768 only, 16 rebase flags, support at most 160, and all threshold passes.

Combined with the now-audited v15.1173/v15.1180 coverage and the mathematically audited v15.1199 extension, the filed R4 bookkeeping coverage is

`{3241,...,4008} union {4010,...,4713}`

for 1,472 arcs total, leaving 6,547 of 8,019 R4 arcs uncovered. The v15.1199 provenance discrepancy remains exactly as recorded by Round 609; its mathematics is confirmed.

## Frozen artifacts

- producer commit: `245f923c08ae5220b3d715d9a29da9d0f48ecd24`
- certificate commit: `7ba3d63319c46a8a0a0125d9a499aaad2ca6b3be`
- manifest commit: `2fd09b34f1d557fe59cfd57c5bcabca09f1f17c2`
- producer SHA-256: `b1838460e97f214ad2bc2d9a2b434060a703971bd2a93dd2f2de338887cc3939`
- certificate SHA-256: `2b549c84f5dbf199e905a30725501e6645483f9293de3b8a30b304810dbe1e71`
- manifest SHA-256: `af14e8f5906de7d111d96c59b366b1cc1fb9b8dba0eb6cdff5007be442213ca8`
- v15.842 dependency SHA-256: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`
- v15.800 dependency SHA-256: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`
- frozen weight SHA-256 reproduced: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`

## Strict boundary

This is an R4 resource/coverage certificate only. It gives no global C4 certificate. It is not a C16 calculation and does not prove `C16 < 4.10`, the joint five-frequency cross budget, full Suzuki closure, source-native Phi, whole-residual, stationary, or capacity claims. No conclusion is drawn from rank alone, sampled eigenvalues, or a one-x probe. The frozen v14.405/v14.406 finite-plus-gap PASS, v14.814 far FAIL, original `C_S_32000`, `3e-5`, `.002`, source hashes, and once-only charges remain untouched.

## External Audit handoff

Please replay the committed producer and verify that its emitted certificate is byte-for-byte identical to the committed certificate, specifically checking that no unproduced provenance field recurs. Also verify the manifest, exact arc interval 3241–3304, boundary steps 705 and 768, 16 rebase flags, support at most 160, all 64 direct-versus-propagated records, and the stated extrema.

The matching right-side steps 705–768 remain open. Under the measured runtime limit, future outer work should use one 64-state direction per gate or add a rigorously frozen restart-state format before attempting two-sided tiles. The decisive mathematical target remains a rigorous global outward two-sided `C16 < 4.10` certificate; no inference from these R4 tiles is permitted.
