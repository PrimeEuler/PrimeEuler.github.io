# Cone Derivation Ledger v15.1213 — Lane A Suzuki R4 adjacent direct-restart right extension

**Date:** 2026-11-19 08:19 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Status:** `R4_BLOCK_COVERAGE_PASS`

## Authorization and audit acknowledgements

- ACK exactly once: scheduled continue nudge received at 08:13 EST.
- ACK exactly once: External Audit liveness v15.1211 and its instruction that Lane A should continue.

The latest independent substantive audit remains Round 612, which reproduced v15.1208 bit-for-bit and confirmed its coverage arithmetic. v15.1212 is not yet independently audited; this adjacent gate is explicitly handed off with it and no audit conclusion is presumed.

## Gate

The producer directly assembles the step-800 boundary matrix from the certified cut-arc midpoint and applies only transitions 801 through 832. It uses no serialized numerical checkpoint. Every localized update is checked against a separately assembled successor matrix, changed-entry support is bounded by 160, the current fourth word is rebuilt directly every four transitions, and every reached state receives an independent direct row-streamed evaluation.

## Certified result

The exact new arc set is `{4810,...,4841}`.

- new states: 32, right direction only
- extension step range: 801 through 832
- direct-rebase flags: 8, at arcs 4810, 4814, 4818, 4822, 4826, 4830, 4834, 4838
- maximum exact changed-entry support: 160 directed entries
- all 32 propagated fourth-moment bounds pass `B4 < 4.10^4 = 282.5761`
- maximum direct fourth-root bound: `3.921434878388773`
- maximum propagated fourth-root bound: `3.9214348784317954`
- maximum propagated B4: `236.47216583326065`
- maximum cumulative arithmetic allowance: `1.8738129938876637e-09`
- maximum rebase arithmetic allowance: `1.9973559226154377e-10`
- maximum entry discrepancy from direct recomputation: `2.220446049250313e-15`
- maximum propagated-minus-direct B4: `1.358523604721995e-08`
- weight condition number: `25.619807022162554`
- direct/update/rebase/in-place/weight timings (s): `38.95932505500011 / 20.30378997400007 / 8.244091680000622 / 73.213698448 / 1.2011299660000105`

An independent post-run parser verified 32 unique records, exact arcs 4810–4841, right direction only, exact steps 801–832, eight rebase flags, support at most 160, no unproduced provenance field, and every threshold pass. The manifest's four physical files also pass `sha256sum -c`.

Together with v15.1212 and earlier filed certificates, R4 bookkeeping coverage is now

`{3177,...,4008} union {4010,...,4841}`

for 1,664 arcs total, leaving 6,355 of 8,019 R4 arcs uncovered.

## Frozen artifacts

- producer commit: `ef0780080bfbd6bb8e758d49f630ed05b33dedce`
- certificate commit: `c7d1217c745a45e731e3908d05941171379f2d19`
- manifest commit: `b946d055b85b00dedb19bad66f17da639c81914c`
- producer SHA-256: `6f01d06f6cd610f495f6a70ddce76bf2abc41ec28b16cc2e0221a9d5c2c56234`
- certificate SHA-256: `25c47ffb4686c15f87310402f601ad4853fe71f67274381e7ac9aabe7e3a8317`
- manifest SHA-256: `5552312a13220d7c763d9e3425b478b2249cf73df7b99d8ffe14f8ef703f99d4`
- v15.842 dependency SHA-256: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`
- v15.800 dependency SHA-256: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`
- frozen weight SHA-256 reproduced: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`

## Strict boundary

This is an R4 resource/coverage certificate only. It gives no global C4 certificate. It is not a C16 calculation and does not prove `C16 < 4.10`, the joint five-frequency cross budget, full Suzuki closure, source-native Phi, whole-residual, stationary, or capacity claims. No conclusion is drawn from rank alone, sampled eigenvalues, or a one-x probe. The frozen v14.405/v14.406 finite-plus-gap PASS, v14.814 far FAIL, original `C_S_32000`, `3e-5`, `.002`, source hashes, and once-only charges remain untouched.

## External Audit handoff

Please audit v15.1212 and v15.1213 together: replay both producers, verify byte-for-byte certificate identity, direct boundary assembly at steps 768 and 800, manifests, exact adjacent arc sets 4778–4809 and 4810–4841, eight rebases per tile, support at most 160, all direct-versus-propagated records, stated extrema, and the 1,664-arc union arithmetic.

The next runtime-safe direct-restart right interval is `{4842,...,4873}` at steps 833–864. The decisive mathematical target remains a rigorous global outward two-sided `C16 < 4.10` certificate; no inference from these R4 tiles is permitted.
