# Cone Derivation Ledger v15.432 — Lane A correction: restore the nonprime commutator omitted in v15.431

Date: 2026-11-05 (America/New_York). Lane A / Cone–Suzuki. Parent: v15.431. Status: [D] additive correction and corrected chosen-ell2 full-tail norm bound. `FULL_K_TRANSFER` remains INCONCLUSIVE.

## Correction

The v15.431 insertion correctly replaced the physical five-frequency commutator summand by the audited v15.423/v15.424 bound, but it then treated that summand as the whole commutator in v15.309's full tail. This omitted v15.309's separately certified remote-z/nonprime commutator remainder `<0.000003108`. The omission is small but real; v15.431's strict `<9.740003` headline is therefore withdrawn and superseded here. Its files remain frozen and unmodified.

For the nonprime multiplier remainder `E`, v15.309 gives `||E||_infinity<0.000003108`. Since `||Hminus||<=pi/2`,

`||(1/pi)[E,Hminus]|| <= (1/pi)*2*||E||*||Hminus|| <= ||E|| < 0.000003108`.

Adding this missing certified term to the otherwise unchanged v15.431 arithmetic gives

`||Q B Q||`

`< 2.534644890455112455357343436959794`

`  + 0.000003108`

`  + 5.634544 + 1.570797 + 0.000008959063554126742 + 0.000008056`

`= 9.740006013518666582099035852223797...`

and hence the corrected strict certificate

`||Q B Q|| < 9.740007`

on either physical parity tail supported on `n>=256001`.

This still strictly improves v15.309's `12.84`, but remains far above the `2.535946` target. The active mathematical obstruction and scope are unchanged: a joint cancellation-preserving commutator-plus-Hankel/full-kernel estimate is required.

## Corrected witness and manifest

Witness: `unified/discriminant-12-return/research-notes/lane_a_v15_432_corrected_full_tail_commutator_insertion_certificate.py`

- commit: `c8d64c88378f2fd0af5233af5a52aae3037c7413`
- git blob: `37f446103cda27a52163926581dc5f3a75385758`
- SHA-256: `fe318a515fd0fbcc40d5b8805b8e59d1eee6427253a105b6f8e063a289ba610b`

Manifest: `unified/discriminant-12-return/research-notes/lane_a_v15_432_corrected_full_tail_commutator_insertion_certificate.sha256`

- commit: `58f49b275198e2fed75b337a09a84b5b9c8060dd`
- git blob: `5337595057ddc672bbc68aeb5e9013649b4b7768`
- SHA-256: `bc1553f619cfe29dafb842c6968ba69bc99d2c128deb534e190df5a400ef6e51`

## Strict boundary

This is a chosen counting-measure `ell2` tail bound only. It does not identify source-native Suzuki `Phi`, certify a full-K gap, instantiate Schur/Feshbach inertia, or prove whole-residual, stationary, capacity, infinite-capacity, or spectral physical equivalence. All protected thresholds, frozen historical objects, and exactly-once charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: corrected-full-tail-commutator-insertion-bound
parent: v15.432
status: OPEN_AUDIT
action: verify the additive correction, the nonprime commutator inequality, and the strict corrected `||Q B Q||<9.740007` bound; treat v15.431's `9.740003` headline as superseded.
deliverable: confirmation/correction or a source-faithful cancellation-preserving joint bound. No FULL_K_TRANSFER or source-native promotion.
