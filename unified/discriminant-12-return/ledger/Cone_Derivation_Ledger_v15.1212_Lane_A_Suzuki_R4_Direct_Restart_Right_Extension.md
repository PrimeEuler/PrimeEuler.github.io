# Cone Derivation Ledger v15.1212 — Lane A Suzuki R4 direct-restart right extension

**Date:** 2026-11-19 07:43 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Status:** `R4_BLOCK_COVERAGE_PASS`

## Authorization and audit acknowledgements

- ACK exactly once: scheduled continue nudge received at 07:38 EST.
- ACK exactly once: External Audit Round 612/v15.1209 and its independent confirmation of v15.1208.
- ACK exactly once: External Audit liveness v15.1210 and v15.1211, each instructing Lane A to continue.

Round 612 (`530b58b236dc4efafa7f7e829cfc228a14c14804`) independently reproduced the v15.1208 certificate bit-for-bit, confirmed no recurrence of the v15.1199 provenance discrepancy, and independently verified the 1,600-arc coverage arithmetic.

## Runtime obstruction and rigorous repair

A 64-state right extension and then a 32-state right extension both exhausted a 600-second execution bound without emitting a certificate. No partial artifact or pass was promoted. Profiling by controlled reduction identified the exact path reconstruction through the first 768 transitions as the dominant fixed cost.

The repaired producer does not use a serialized numerical checkpoint. It directly assembles the step-768 boundary matrix from the certified cut-arc midpoint, then applies only transitions 769 through 800. Every localized update is checked against a separately assembled successor matrix, every changed-entry support is bounded by 160, the current fourth word is directly rebuilt every four transitions, and every reached state is independently evaluated by the direct row-streamed certificate.

## Certified result

The exact new arc set is `{4778,...,4809}`.

- new states: 32, right direction only
- extension step range: 769 through 800
- direct-rebase flags: 8, at arcs 4778, 4782, 4786, 4790, 4794, 4798, 4802, 4806
- maximum exact changed-entry support: 160 directed entries
- all 32 propagated fourth-moment bounds pass `B4 < 4.10^4 = 282.5761`
- maximum direct fourth-root bound: `3.832042324204781`
- maximum propagated fourth-root bound: `3.8320423242243544`
- maximum propagated B4: `215.63596096734176`
- maximum cumulative arithmetic allowance: `1.9785281682229204e-09`
- maximum rebase arithmetic allowance: `1.96807125276763e-10`
- maximum entry discrepancy from direct recomputation: `3.1086244689504383e-15`
- maximum propagated-minus-direct B4: `1.2837460872106021e-08`
- weight condition number: `25.619807022162554`
- direct/update/rebase/in-place/weight timings (s): `36.634324106000065 / 19.952844455999895 / 8.099385539999986 / 71.841275817 / 1.270898105999997`

An independent post-run parser verified 32 unique records, exact arcs 4778–4809, right direction only, exact steps 769–800, eight rebase flags, support at most 160, no unproduced provenance field, and every threshold pass.

Together with audited v15.1208 and earlier filed certificates, R4 bookkeeping coverage is now

`{3177,...,4008} union {4010,...,4809}`

for 1,632 arcs total, leaving 6,387 of 8,019 R4 arcs uncovered.

## Frozen artifacts

- producer commit: `0487166e8d0fe4d89077f9df37cf435a8c20f0a1`
- certificate commit: `02ec10acc5f26ac11f032a578c5348ea73ffa7a1`
- manifest commit: `ae3f7a0e6d914ac4078ad352e8d9a50873e71e5f`
- producer SHA-256: `aff9580eb0efaa3a5f312b7baad997e92e6b5041ad6984a2cd2bd2b52ca87298`
- certificate SHA-256: `3a66d69404138ef5079e1b6128d545c2e0146c7a657925bfe6c5ccb350fa1586`
- manifest SHA-256: `3ec0b3e3dc75afba2829c43c9c64d5048544697830dcd034c163ba5c04b23b54`
- v15.842 dependency SHA-256: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`
- v15.800 dependency SHA-256: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`
- frozen weight SHA-256 reproduced: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`

## Strict boundary

This is an R4 resource/coverage certificate only. It gives no global C4 certificate. It is not a C16 calculation and does not prove `C16 < 4.10`, the joint five-frequency cross budget, full Suzuki closure, source-native Phi, whole-residual, stationary, or capacity claims. No conclusion is drawn from rank alone, sampled eigenvalues, or a one-x probe. The frozen v14.405/v14.406 finite-plus-gap PASS, v14.814 far FAIL, original `C_S_32000`, `3e-5`, `.002`, source hashes, and once-only charges remain untouched.

## External Audit handoff

Please replay the committed producer and verify byte-for-byte certificate identity, the direct step-768 boundary assembly, manifest, exact arcs 4778–4809, steps 769–800, eight rebases, support at most 160, all direct-versus-propagated records, stated extrema, and the 1,632-arc union arithmetic.

The next runtime-safe direct-restart right interval is `{4810,...,4841}` at steps 801–832. The decisive mathematical target remains a rigorous global outward two-sided `C16 < 4.10` certificate; no inference from these R4 tiles is permitted.
