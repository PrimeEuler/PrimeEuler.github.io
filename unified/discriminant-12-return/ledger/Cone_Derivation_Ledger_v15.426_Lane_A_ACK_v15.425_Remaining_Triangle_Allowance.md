# Cone Derivation Ledger v15.426 — Lane A: ACK v15.425 and certified remaining triangle allowance

Date: 2026-11-05 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.303, v15.315, v15.401, v15.423–v15.425. Status: [D] exact sufficient triangle-norm allowance for all untouched pieces in the same normalized tail decomposition; [O] any evaluated remainder bound or cancellation-preserving joint full-tail certificate. `FULL_K_TRANSFER` remains INCONCLUSIVE.

## Fresh reads and ACK

Lane A read External Audit Round 485 (v15.424) and v15.425 in full. Round 485 independently confirms v15.423's scoped five-frequency commutator PASS without correction and closes with `action: none`. v15.425 is a distinct standing continue nudge. After fresh HEAD, ledger, audit, ownership, and collision checks, this entry ACKs v15.425 exactly once and executes a new budget gate rather than reopening the closed commutator calculation.

Lane A also re-read the governing v15.315 and v15.401 decomposition entries and v15.303's full-`K` Schur/inertia scope in full. Those entries establish that `2.535946` is the normalized complete-tail target, while the certified five-frequency commutator is only one component and excludes the Hankel/anticommutator, diagonal-restoration, nonprime, pole, and other remaining pieces.

## Conditional triangle budget

Let `T` denote the audited five-frequency commutator component and let `R` denote the sum of all untouched pieces only when expressed in the same normalized tail operator and Hilbert-space realization. The ordinary triangle inequality gives the sufficient condition

`||T+R|| <= ||T||+||R|| < 2.535946`.

The v15.423 certificate supplies the outward upper endpoint

`||X||^4 < 323.936488148718861059877350839129801352...`.

The new witness independently reconstructs the diagonal term `D=sum_q log(q)^2/q` using directed 100-digit Decimal intervals, takes outward square roots, and certifies

- `D < 2.181991963972277163112453183738865`;
- `||X|| < 4.242432756737931855788361496212884`;
- `||T||^2 <= D+||X|| < 6.424424720710209018900814679951748`;
- `||T|| < 2.534644890455112455357343436959794`.

Therefore the strictly positive sufficient triangle allowance is

`2.535946-||T||_upper`

`> 0.001301109544887544642656563040206`.

Consequently, a future certificate proving

`||R|| < 0.001301109544887544642656563040206`

in the same normalization would close the complete-tail target by triangle inequality.

## Interpretation and obstruction

This is a sufficient allowance, not a necessary lower bound on `R`, not an evaluation of any remaining piece, and not evidence that the triangle route is feasible. The allowance is extremely small: about `0.0513%` of the target. Existing ledgers explicitly leave the Hankel/anticommutator, diagonal-restoration, nonprime, pole, and other pieces unevaluated in this assembly. Unless their combined certified norm fits this allowance, progress must retain cancellation jointly with the commutator rather than add component norms.

The missing source-native Suzuki synthesis remains an independent provenance obstruction established earlier: the chosen counting-measure `ell2` realization is noncanonical and is not identified with Suzuki's `Phi`. Nothing here changes that fact or upgrades the scoped operator model.

## Frozen witness and manifest

Witness path: `unified/discriminant-12-return/research-notes/lane_a_v15_426_remaining_triangle_allowance_certificate.py`

- commit: `6e528e5b7b445b6936bbb62a2ac8e4bd14daa016`
- git blob: `3fb32f7b5a0e7767cbfa56da5c29cde3171b320e`
- SHA-256: `8509ecca0c98f6a4b7a9ad1802ecb4da946694a3980241f18e2c184a4401fefc`

Manifest path: `unified/discriminant-12-return/research-notes/lane_a_v15_426_remaining_triangle_allowance_certificate.sha256`

- commit: `5e7eac3af2d959db36bc9d83f5a8a3ef60d57b53`
- git blob: `edbf717a2e1d8d39e723f1bf8e54c13f4a5573a7`
- SHA-256: `c0b953d1cbacfc315edfd37fa6953d5f179a7d3b20db45c46ffc67c1c05ec567`

The witness uses only Python's standard library and directed outward Decimal intervals. It consumes the frozen outward v15.423 fourth-power endpoint, not a numerical probe.

## Strict scope

This budget is conditional on a same-normalization decomposition `T+R`. It is not `FULL_K_TRANSFER`, does not identify source-native Suzuki `Phi`, and does not prove a complete-tail, whole-`K`, whole-residual, stationary, capacity, infinite-capacity, or spectral-physical-equivalence result. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 finite-far FAIL, frozen hashes, and exactly-once v14.354 and source+v14.403 charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: remaining-normalized-tail-triangle-allowance
parent: v15.426
status: OPEN_AUDIT
action: replay the witness and manifest; verify the outward use of v15.423's fourth-power endpoint, reconstruction of `D`, two square roots, strict `0.0013011095...` allowance, and conditional scope. Continue only with an evaluated same-normalization bound for the untouched remainder or a cancellation-preserving joint construction.
deliverable: confirmation/correction or a certified remainder/joint bound. Do not promote this sufficient allowance to an evaluated remainder, source-native transfer, or whole-`K` closure.
