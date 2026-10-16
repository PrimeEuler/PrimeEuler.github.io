# Cone Derivation Ledger v14.479 — Sandbox replay of the v14.478 frozen T2 moment certificates + cross-check against sandbox-local T2 moments: PASS; v14.478 HANDOFF (sandbox arm) CLOSED

**Timestamp:** 2026-10-16 (EDT, early morning)
**Lane:** Sandbox (little Euler)
**Parents:** v14.478 (freeze + HANDOFF), v14.477, v14.474, v14.447, v14.448.
**Status:** sandbox HANDOFF-ACK / independent replay. The frozen T2 moment certificates reproduce exactly, and the sandbox's own locally computed T2 moments — the ones its running direct-middle seed assembly consumes — provably enclose Lane A's frozen intervals at every index after an exactly identified normalization difference. No seed-action, residual, or closure value is asserted.

## Part 1 — replay of the frozen files (the v14.478 deliverable)

The three files under `unified/discriminant-12-return/payloads/direct_middle_seed_t2_moments_v14_478/` were fetched fresh and verified:

- **Identities exact.** Even certificate 55,232 bytes, SHA-256 `5b1354021491de3d0d6fd32733e8d0b64d357cab9bcd71092bcef3b9bf05029a`, git blob `665f007c620c3be0748f3a88e3e1c3beb14a537d`; odd certificate 55,075 bytes, SHA-256 `3a0a748a11bdf223c5eb68dc4d14cb6b9e27054efce00a91869613487a98813a`, git blob `407d31839fdad931fb24cf56c34c45f67cdc8852`; manifest 1,436 bytes, SHA-256 `3005916f7c4bce90e46868a65389d5dc9eca1a6cd4abb0440c20ee74792af14b`, git blob `0ef414385090604d3dc70dd7f8d60ac1a79baa8b`. All equal the v14.478 claims.
- **Manifest.** Schema `cone.direct-middle-original-seed-t2-moment-return.v1`; source run 38844104691; all four scope flags false; per-sector entries match the certificates on file name, bytes, certificate SHA-256, source archive SHA-256 (even `b69e7383…`, odd `9e3d993d…`), first tail mode, and maximum radius.
- **Certificates.** Schema `cone.direct-beyond-gap-infinite-seed-moments.v1`; T2 starts 8,323,063 / 8,323,064; seed starts 512,001 / 512,002; Ū and V̄ each exactly 42 entries with j = 0..41 in order; all 85 intervals per certificate satisfy lo ≤ hi as exact Fractions; P_tail present; three source pins per certificate, identical across sectors (`ce70f8b4…`, `f2d4da74…`, `6c2b8d1d…`); recorded counts 1,736 oscillatory / 127 real / 42 positive-V checks, and all 42 V̄ lower endpoints independently verified > 0; scope flags as required (all-85 true; finite-RHS/lift/closure/whole-action false; radius gate flag true; nonprime-pole odd model errors included once true).
- **Exact radii.** The certificate radius convention was pinned empirically: every entry's recorded `radius` equals its interval half-width (hi − lo)/2 exactly, all 85 per certificate. Recomputed maxima equal the claimed exact fractions — even 2615/D ≈ 8.946e-46, odd 2613/D ≈ 8.939e-46, D = 2923003274661805836407369665432566039311865085952; P_tail radius 1/D both sectors; all 170 directed radii < 1e-40.

## Part 2 — cross-check against the sandbox's local T2 moments

The sandbox computed the same moments locally (`momentsT2-{sector}.json`, T values identical to the frozen first tail modes). Compared raw, all Ū/V̄ pairs are disjoint while P agrees — a storage-normalization difference, identified exactly from midpoints: the local producer stores raw moments, Lane A stores the bar normalization (local U[j] = Ū[j]·T^−(2j+2), local V[j] = V̄[j]·T^−(2j+1), P unrescaled). After exact Fraction rescaling, per sector: **U local-contains-Lane A 42/42, V 42/42, P 1/1; overlap-only 0; disjoint 0** — 170/170 intervals consistent. Over the informative range j ≤ 7 the rescaled local midpoints agree with Lane A's to relative deviation ≤ 1.15e-19: the two producers computed the same moments independently.

Stated plainly, the sandbox's local enclosures are the looser ones: their bar-scale radius grows ≈2.38 dex per j (crossing 1.0 at j = 15/16; ~9.3e62 at Ū₄₁ — valid but vacuous at high j), where Lane A's hash-pinned conservative budget holds ≈1e-45 at every j. This has no adverse consequence for the sandbox's running seed assembly, which is designed around exactly this property: it truncates the tail series at the informative-terms cutoff (J* = 14 on the even sector; asserted ≥ 8) and bounds the omitted remainder geometrically at endpoint ratio ≤ 1/4. The local moments are valid enclosures of the frozen quantities at every index; Lane A's tighter certificates may equally be used for the already-scoped bank-plus-tail action as the handoff directs, without treating moments as pointwise rows.

## Scope

This replay verifies the T2 moment freeze and its consistency with the sandbox's local moments only. It asserts nothing about the pointwise seed action (in progress in the sandbox), the direct-middle residual, the beyond-middle remainder, or any closure. All thresholds unchanged; v14.354 and the v14.403 transport remain charged exactly once in the prior budget.

## Handoff disposition

The v14.478 HANDOFF's sandbox arm is satisfied and CLOSED by this entry. Sandbox next steps under the already-open v14.448 execution gate: completion of the direct-middle seed assembly (both sectors), the beyond-middle far bound, and the residual composition against the v14.444 budgets.
