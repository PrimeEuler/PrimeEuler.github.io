# Cone Derivation Ledger v14.478 — Lane A freeze of exact T2 original-seed moment returns

**Timestamp:** 2026-10-16 00:41:22 EDT
**Lane:** A (Cone/Suzuki)
**Parent:** v14.477 / verifier run `38851758219`
**Status:** exact two-sector T2 moment certificates verified and frozen; pointwise seed action remains open

## Verifier return and exact replay

The v14.477 verifier completed successfully. It downloaded the two original run-`38844104691` ZIPs inside GitHub Actions and replayed every declared gate before emitting the exact certificate bytes. The verifier required both transport hashes, exactly one JSON per archive, correct schema/sector/T2 starts and all three source pins, complete U/V index sets `0..41`, the pole moment, recomputed exact maximum radius, the `<1e-40` radius gate, scalar/envelope counts, all-85 and once-only error flags, and every false scope flag.

Verifier run: `38851758219`
Verifier freeze-bundle artifact: `12025756785`
Verifier freeze-bundle archive SHA-256: `6e60af4a4f1356427b364faf532415f122b713fbee1aafe02da75e019e4a4439`

## Frozen exact witnesses

Frozen under `payloads/direct_middle_seed_t2_moments_v14_478/`:

| item | bytes | SHA-256 | Git blob SHA-1 |
|---|---:|---|---|
| even-v certificate | 55,232 | `5b1354021491de3d0d6fd32733e8d0b64d357cab9bcd71092bcef3b9bf05029a` | `665f007c620c3be0748f3a88e3e1c3beb14a537d` |
| odd-v certificate | 55,075 | `3a0a748a11bdf223c5eb68dc4d14cb6b9e27054efce00a91869613487a98813a` | `407d31839fdad931fb24cf56c34c45f67cdc8852` |
| return manifest | 1,436 | `3005916f7c4bce90e46868a65389d5dc9eca1a6cd4abb0440c20ee74792af14b` | `0ef414385090604d3dc70dd7f8d60ac1a79baa8b` |

The source archive hashes remain even-v `b69e7383a740c06f377d236fb33636189192f7597d8e67c2abfe2111237012d0` and odd-v `9e3d993df05481f76bd90bbafe87636ea55336b07697b5beaf033b378482b63c`.

The exact maximum radii are unchanged conservative values:

- even-v: `2615/2923003274661805836407369665432566039311865085952`;
- odd-v: `2613/2923003274661805836407369665432566039311865085952`.

Both certificates evaluate all 85 inverse moments at T2 `8,323,063/8,323,064`, with 1,736 oscillatory scalars, 127 real scalars, 42 positive-V checks, and every directed radius below `1e-40`.

## Scope fence and next gate

This closes only the T2 inverse-moment return. Moments are not pointwise original-seed action rows. No direct-middle seed action, residual, whole action, stationary acceptance, or infinite-capacity closure is claimed.

The next physical gate remains the explicit original-seed bank action from modes `512001/512002` through T2-2, followed by the frozen T2 tail expansion on all 1,040,383 direct-middle outputs and composition with v14.471's compact buffers. `C_S_32000`, all thresholds, v14.354, and the once-only v14.403 transport accounting remain unchanged.

---

HANDOFF
target: external-audit, sandbox
type: exact-freeze-review
parent: v14.478
status: open
action: replay the three frozen files, their SHA-256 and Git blob identities, T2 starts, complete moment indices, exact radii, source pins, and false scope flags; use these witnesses for the already-scoped bank-plus-tail action without treating moments as pointwise rows
constraints: no residual or closure claim; no duplicate transport; all thresholds unchanged
