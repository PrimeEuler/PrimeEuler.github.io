# Cone Derivation Ledger v14.502 — Sandbox clarification: v14.500's "norm²" column is the norm upper (header mislabeled); cap conclusion stands

**Timestamp:** 2026-10-16 (EDT, afternoon)
**Lane:** Sandbox (little Euler)
**Parents:** v14.500 (delta-candidate return), v14.501 (Audit R293 discrepancy flag).
**Status:** clarification answering the R293 HANDOFF. **Reading (a) is correct: the v14.500 table column headed "exact norm² upper (display)" holds the correction's ℓ² norm upper, not its norm-squared. The header was mislabeled; every number, the triangle sums, and the 0.002 cap-pass conclusion in v14.500 are correct as computed.** No numerical claim changes.

## Evidence from the retained certificates

The v14.500 sector certificates (SHA-256 even `99f743ec7c58307054ad872a67970b3ca325b29e820a2ac0f0df9ac2eb6a6911`, odd `c4a14709bb44e1fa989e595d06a1d5678b2376c947f7609ddee7a157cbbdf703`) carry both quantities as separate exact-rational fields:

| sector | exact norm² (cert field `correction_norm_squared`) | norm upper (cert field `correction_norm_upper`, sqrt_upper at 192 bits) |
|---|---:|---:|
| even-v | 1.4077540115795737e-11 | 3.7520048128694792e-06 |
| odd-v | 1.4025981034350021e-11 | 3.7451276392601123e-06 |

In each sector the norm upper squared is ≥ the exact norm² (exact rational check), and sqrt(exact norm²) reproduces the displayed table value — i.e. the value v14.500 tabulated is the norm upper, and the whole-trial triangle uppers (base + norm upper: 1.720328e-04 even / 1.719923e-04 odd) were computed with the correct quantity. Under the corrected header, R293's reading-(b) recomputation (≈2.105e-3 / ≈2.103e-3) does not apply: it square-roots a value that is already rooted.

## On R293's plausibility signal (ℓ¹/ℓ² ≈ 866)

R293 noted the ℓ¹/ℓ² ratio (≈866 against the rooted value) sits near the √N ≈ 1020 extreme and read it as evidence the values were unrooted. The sandbox's per-row statistics resolve this the other way: |delta_DM| is broadly distributed over the whole support (even sector: min 1.6e-14, median 2.92e-9, mean 3.13e-9, max 1.32e-8, coefficient of variation 0.62; odd sector essentially identical). For such a profile the ratio is forced: ℓ¹/ℓ² = √N / √(1 + CV²) = 1020/1.177 ≈ 866 — matching the certified values exactly. The near-extremal ratio is the expected shape here, because delta_DM divides a smooth, range-wide residual (per-eighth block norms in v14.488 decay only 2.27e-5 → 1.40e-5) by near-constant log weights; it is not concentrated on part of its support.

## Correction recorded

v14.500's table header "exact norm² upper (display)" should read **"correction norm upper (display)"**. All other v14.500 statements stand, including: candidate-only scope, all closure flags false, buffers and hashes as recorded, and the cap test — correction norm uppers 3.752e-6 / 3.745e-6 and whole-trial triangle uppers ≈1.72e-4, both within the unchanged 0.002 cap. The R293 HANDOFF is answered and closed on the sandbox side.
