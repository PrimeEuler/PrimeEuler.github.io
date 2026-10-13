# Cone Derivation Ledger v14.356 — Lane A compact-gap CI receipt and artifact-access blocker

- Date: 2026-10-13
- Lane: A (Cone/Suzuki)
- Parent inspected HEAD: `bf233375409e4c4f32ca51f35c417a1e59575f47` (v14.355)
- CI run: [38436590050](https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/38436590050)
- Status: both scoped compact-gap jobs succeeded; exact witness freeze/replay is not yet complete.

## Scope actually evaluated

The v14.353 compact-gap workflow checked out `a89827f879fdf982a1625199733cec0266b7e159`, replayed the hash-bound v14.353 finite residual and its three buffers byte-for-byte, reassembled the hash-bound wider candidate, passed the 54-row exact physical-kernel self-check, and evaluated all 520191 changed compact-gap rows in each sector.

The successful returned bounds are:

| sector | complete compact-gap error upper |
|---|---:|
| even-v | `6.909845268071272e-16` |
| odd-v | `1.3660609076703798e-17` |

These agree with the v14.352 geometric remainder scale. They are evaluated CI outputs, but they are not yet repository-frozen certificates.

## Returned artifacts

| sector | artifact ID | archive bytes | archive SHA-256 |
|---|---:|---:|---|
| even-v | `11833778843` | `27267117` | `52b81debffa89ad2d2482aa48f8e811ec0c5af21161558954d56870257eac9f2` |
| odd-v | `11834810109` | `27265858` | `9fd1a5142d4b0a34cb4ce470fccf256c88332532287915c5a513ba145de33123` |

The current GitHub connector exposes artifact metadata and decoded job logs, but rejects binary archive downloads. Therefore this lane cannot honestly freeze or replay the six-file sector artifacts in this run. Log values and archive digests are recorded here only as a CI receipt; they must not be substituted for the exact witness bytes.

## Correction carried from v14.354/v14.355

The compact-gap calculation contains only the changed compact contribution, so the v14.354 artificial Hankel self-diagonal defect in the old v14.327 original-seed tail buffers does not alter the two compact-gap bounds above. In the eventual whole residual, Lane A must subtract the exact rowwise term
[
s_n=-\frac{c}{2}g_{k_n}y_n(z_{\mathrm{out},n}+z_{\mathrm{in},n})
]
or carry the rigorous Region2/Region3 combined correction envelope once, as recorded in v14.355. No double charge is permitted.

## Gate status

This entry does **not** claim an infinite-tail closure or full residual acceptance. The next whole-composition gate remains blocked on both:

1. repository-freezing and independent replay of the exact compact-gap artifact bytes; and
2. the v14.351 Sandbox return for the original infinite-seed-only action on the same gap, with self rows excluded.

The original `C_S_32000` and all existing acceptance thresholds remain unchanged.

## HANDOFF ledger

- **HANDOFF (target: lane-a; status: BLOCKED):** acquire the two exact CI archives through an authorized binary-artifact path, verify the archive SHA-256 values above, freeze all contained witnesses additively, replay them, and only then compose.
- **HANDOFF (target: sandbox; source: v14.351; status: OPEN):** return the original infinite-seed-only gap action for both sectors with self rows excluded and the requested rigorous error accounting.
- **HANDOFF (target: external-audit; status: OPEN):** independently review v14.352–v14.356, including the v14.354 correction and this CI receipt. No acceptance is inferred from silence.

No ownership is claimed beyond these already scoped Lane A obligations.
