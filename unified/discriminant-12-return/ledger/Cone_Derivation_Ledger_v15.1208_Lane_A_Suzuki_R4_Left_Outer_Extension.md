# Cone Derivation Ledger v15.1208 — Lane A Suzuki R4 left outer extension

**Date:** 2026-11-19 04:01 EST  
**Track:** Lane A — original frozen Suzuki seed certification only  
**Status:** `R4_BLOCK_COVERAGE_PASS`

## Authorization and audit acknowledgements

- ACK exactly once: scheduled continue nudge received at 03:30 EST.
- ACK exactly once: External Audit Round 611/v15.1206 and its independent confirmation of v15.1205.
- ACK exactly once: External Audit liveness v15.1207 and its instruction that Lane A should continue.

Round 611 (`94249bf8821329e7725cbe8cf6244350a76c065c`) independently re-executed v15.1205 and reproduced its certificate bit-for-bit. It confirmed the stated union arithmetic and no recurrence of the v15.1199 provenance discrepancy. This certificate is likewise untouched producer output and contains no manually added provenance field.

## Gate

The producer constructs the exact path from the x=1 anchor through step 832, begins the certified left extension from an independently rebuilt exact step-768 boundary block, applies the four signed mixed update words, rebases directly every four transitions, and independently recomputes every certified state row-streamingly.

## Certified result

The exact new arc set is `{3177,...,3240}`.

- new states: 64, left direction only
- extension step range: 769 through 832
- direct-rebase flags: 16, including the exact extension anchor
- maximum exact changed-entry support: 160 directed entries
- all 64 propagated fourth-moment bounds pass `B4 < 4.10^4 = 282.5761`
- maximum direct fourth-root bound: `3.9214348783882627`
- maximum propagated fourth-root bound: `3.9214348784363566`
- maximum propagated B4: `236.47216583436088`
- maximum cumulative arithmetic allowance: `1.9881963724764853e-09`
- maximum rebase arithmetic allowance: `1.997355922615438e-10`
- maximum entry discrepancy from direct recomputation: `3.1086244689504383e-15`
- maximum propagated-minus-direct B4: `1.4155659755488159e-08`
- weight condition number: `25.619807022162554`
- direct/update/rebase/in-place/weight timings (s): `77.06063599700065 / 39.88290694597936 / 17.540437801986855 / 144.335814498 / 1.4523538750000853`

An independent post-run parser verified 64 unique records, exact arcs 3177–3240, left direction only, steps 769–832, 16 rebase flags, support at most 160, no unproduced provenance field, and all threshold passes.

Together with the audited right companion v15.1205 and earlier filed certificates, the R4 bookkeeping coverage is now

`{3177,...,4008} union {4010,...,4777}`

for 1,600 arcs total, leaving 6,419 of 8,019 R4 arcs uncovered.

## Frozen artifacts

- producer commit: `b54ae74ae8e7df4c471b42364aa66be8d753a0f9`
- certificate commit: `9a7643025eb7aa48652f6ee64ca8a1acf479c634`
- manifest commit: `918fdea321af5573f17afdf6967add5d44ad50c9`
- producer SHA-256: `064b113743111011a497eaa4b4923527afb7996ad65c3dc149d468d554f0970c`
- certificate SHA-256: `78a2d4bfdbc6496eb25750aaa72d742744b180a8207c087321ea30f7b238760c`
- manifest SHA-256: `8eff9c4f77ddf677db51690bc2b9dbf9c8c1ee895d6d3d2712d92cae3e3e0d34`
- v15.842 dependency SHA-256: `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`
- v15.800 dependency SHA-256: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`
- frozen weight SHA-256 reproduced: `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`

## Strict boundary

This is an R4 resource/coverage certificate only. It gives no global C4 certificate. It is not a C16 calculation and does not prove `C16 < 4.10`, the joint five-frequency cross budget, full Suzuki closure, source-native Phi, whole-residual, stationary, or capacity claims. No conclusion is drawn from rank alone, sampled eigenvalues, or a one-x probe. The frozen v14.405/v14.406 finite-plus-gap PASS, v14.814 far FAIL, original `C_S_32000`, `3e-5`, `.002`, source hashes, and once-only charges remain untouched.

## External Audit handoff

Please replay the committed producer and verify that its emitted certificate is byte-for-byte identical to the committed certificate. Also verify the manifest, exact arc interval 3177–3240, boundary steps 769 and 832, 16 rebase flags, support at most 160, all 64 direct-versus-propagated records, the stated extrema, and the 1,600-arc bookkeeping union with v15.1205 and earlier filed tiles.

The matching next right-side interval would be `{4778,...,4841}` at steps 769–832. Any next runtime-safe outer gate should remain one direction and at most 64 new states unless a rigorously frozen restart-state format is first established. The decisive mathematical target remains a rigorous global outward two-sided `C16 < 4.10` certificate; no inference from these R4 tiles is permitted.
