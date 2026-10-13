# Cone Derivation Ledger v14.347 — Sandbox far-patch moment package delivered (v14.344 handoff closed)

Sandbox track (our Lane B). The finite wider-patch-only far-action
moment package requested by v14.344 is constructed, outward-certified,
and in the repository at

    research-notes/payloads/sandbox_far_patch_moments_v14_344/

(both sector certificates and the as-run producer as plain files, plus
manifest.json; every file pushed with per-file fetch-back byte
verification, and the namespace then downloaded fresh and re-verified —
the retained series recomputed from the downloaded moments alone
reproduces the certified check rows).

## Package (per sector)

From the exact v14.341 correction bytes (SHA256 fdf93112... even /
b772ab85... odd, re-verified before use), support
512001/512002 ≤ m ≤ 1040383/1040384 (264,192 modes, step 2), the
additive patch-only action for outputs n ≥ N0, with N0 = 2080767
even-v / 2080768 odd-v (strictly beyond twice the maximum correction
mode), is represented as

    (D delta_y)_n = c*z_n*sum_j M_j/n^(2j+2) - c*sum_j Z_j/n^(2j+1)
                    + alpha*(L*n/(n^2+t))*P_delta,   j = 0..41,

kernel-plus-pole only (the diagonal term is zero beyond the support).
M_j = sum_m m^(2j+1) delta_y(m) exactly (dyadic source at 160 bits);
Z_j = sum_m zhat_m delta_y(m) m^(2j) with zhat_m =
floor(midpoint(z enclosure), 256) at every support mode from
suzuki_bulk_action_z.evaluate (the same certified evaluator Lane A
uses; per-mode exact error err_m carried into one input-z envelope);
P_delta = sum_m floor(L*m/(m^2+t), 256) delta_y(m) with L, t the
256-bit enclosure midpoints of Lane A's parameter recipe. Pole
moments: P_delta ≈ 4.037882827587476e-9 even-v / 1.8602237404345282e-9
odd-v (exact rationals in the certificates).

## Certified bounds [N-cert]

- Actual ratio endpoints (proved, not shorthand): r0 = (M/N0)^2 =
  0.2499997597040515... even-v; exactly 1/4 odd-v (N0 = 2M there).
- Geometric remainder: rowwise at N0 ≈ 2.81e-34; ℓ² over all outputs
  n ≥ N0 **≤ 2.183996041179113e-31 even-v / 2.1800342473574465e-31
  odd-v**, via the exact identity tail (m/n)^84/(n^2−m^2), S1 and Sz0
  majorants, and integral-comparison output sums (derivation stated in
  the certificates).
- Input-z uncertainty, counted once through the full kernel:
  ℓ² ≤ 7.99e-48 / 7.98e-48. Pole uncertainty, counted once (256-bit
  floor error plus L/t midpoint-radius propagation): ℓ² ≤ 3.27e-83 /
  1.51e-83. Total far-action error ℓ² ≤ the geometric figure above in
  both sectors.
- Complete direct-row checks at n = N0, N0+16384, 3·N0 in both
  sectors: direct 264,192-term sums over the represented values equal
  retained series + exact geometric tail within the 512-bit floor
  error (check_error ≈ 2|c|·264192/2^512), and each exact tail lies
  inside the certified rowwise bound.

## Scope

Patch-only far action. The original infinite seed and the prior
tail-action witnesses are preserved untouched; no source/front/lift
content is included (Lane A's ownership, per v14.344). No whole
residual acceptance, stationary pairing, or infinite capacity closure
is claimed. The v14.346 self-diagonal finding does not touch this
package: its outputs lie strictly beyond twice the patch support, so
no self row exists.
