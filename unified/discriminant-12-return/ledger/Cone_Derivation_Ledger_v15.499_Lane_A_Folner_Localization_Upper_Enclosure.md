# Cone Derivation Ledger v15.499 — Lane A: exact Følner-localization upper enclosure

**Date:** 2026-11-06 (America/New_York)  
**Track:** Lane A Cone/Suzuki  
**Status:** [A] Exact upper-enclosure architecture proved for the noncanonical chosen-counting-measure five-frequency commutator. The remaining finite Hermitian matrix-field supremum is unevaluated.
**Parents:** v15.420, v15.495, v15.497, v15.498 (External Audit Round 509).

## Fresh audit, correction, and ACK

External Audit Round 509/v15.498 was read in full at live head `ffeaef1d64781635227ab1a65c48e9cdd25beb86`. It confirms v15.497's faithful regular representation, support census, and Følner ratios without a substantive correction.

One illustrative label in Round 509 is mistyped: `g=(3,0,0,0)` is attained by the `q=2,r=4` pair (using `log 4=2 log 2`), not by `q=2,r=5`. The audited maximum radii, ratios, and conclusions are unchanged. This additive entry applies that correction downstream.

The current scheduled continue instruction is ACKed once here. Round 509's HANDOFF is closed with `action: none`, so it is not treated as a new actionable handoff.

Immediately before each additive write, live `master`, v15.499, and the target payload path were rechecked. No collision or competing ownership was present.

## Localization identity

Use the faithful regular representation from v15.497 and write the self-adjoint v15.420 operator as

`T = sum_(g in S) A_g lambda_g`, with `A_g=pi_tilde(a_g)` and `|S|=40`.

Let `phi` be any nonnegative, finitely supported unit vector on `ell2(Z^4)`, and let `phi_k(h)=phi(h-k)`. Then `sum_k phi_k(h)^2=1`. Since the scalar group-coordinate multipliers `phi_k` commute with every diagonal coefficient `A_g`, exact summation gives

`sum_k phi_k T phi_k = sum_(g in S) c_phi(g) A_g lambda_g`,

where `c_phi(g)=sum_h phi(h)phi(h-g)`.

Let `F` contain the support of `phi`, and set

`C_F = sup_k ||P_(k+F) T P_(k+F)||`.

The map `V xi=(phi_k xi)_k` is an isometry, and the localized sum is `V* (direct-sum_k P_(k+F) T P_(k+F)) V`. Therefore

`||sum_k phi_k T phi_k|| <= C_F`.

The remainder is exact and finite:

`T-sum_k phi_k T phi_k = sum_g (1-c_phi(g)) A_g lambda_g`.

Consequently,

`||T|| <= C_F + sum_g (1-c_phi(g)) ||a_g||`.

This is a genuine upper enclosure, not a lower finite-section probe. Translation of the cube center conjugates the coefficient field by the `Z^4` action; in the concrete multiplication representation this is translation of the period-two variable and preserves essential suprema. Thus every centered compression has the same norm and `C_F` is the norm of the central finite compression.

That compression is a direct integral over the period-two variable of a finite sparse Hermitian matrix field, so

`C_F = ess sup_x ||B_F(x)||`.

The signed cancellations remain inside `B_F(x)`; they are not replaced by a common-row absolute Schur sum.

## Box and tent windows

For the normalized box window on `F_R=[-R,R]^4`,

`c_R(g)=product_i max(0,2R+1-|g_i|)/(2R+1)^4`.

The witness independently evaluates 360 exact translate-sum identities and records every pairwise four-sign boundary sum for `R=2,4,8,16,32`.

A stronger exact choice is the tensor tent window generated in one dimension by

`w_R(n)=max(0,R+1-|n|)`.

After exact `ell2` normalization, its correlation is rational:

`c_R^tent(g)=product_i [sum_n w_R(n)w_R(n-g_i) / sum_n w_R(n)^2]`.

For every physical support label the tent penalties decrease strictly with `R`; from `R>=8` they improve on the box penalties. This gives quadratic rather than linear boundary decay for the fixed radius-three support.

## Coefficient penalty

The period-two sawtooth has essential range in `[-1,1]`. Each difference factor in v15.420 has norm at most `2`; each transported coefficient `G_(sigma,tau)` is a sum of two products, hence

`||G_(sigma,tau)||_infinity <= 8`.

Since `alpha_q=log(q)/(2 sqrt(q))`, the fully explicit tent error is bounded by

`E_R^tent = sum_(q<r) [2 log(q)log(r)/sqrt(qr)] Delta_R^tent(q,r)`,

where `Delta_R^tent(q,r)` is the exact rational sum of `1-c_R^tent(g)` over the four sign branches. All ten rational values at each tested radius are frozen in the witness. Decimal orientation values (not promoted to interval certificates) are approximately `1.92014`, `0.558612`, and `0.150773` at radii `8`, `16`, and `32`, respectively. Thus radius 32 reduces the certified-boundary term to a scale compatible with the earlier noncertifying joint probe, but no pass follows until `ess sup_x ||B_F(x)||` is itself enclosed rigorously.

At `R=32`, the finite field has `(2R+1)^4=17,850,625` group sites but only 40-neighbor propagation. The next concrete gate is therefore a verified sparse matrix-field supremum, using exact sawtooth breakpoints plus outward interval/Lanczos or positive-polynomial bounds. A sampled eigenvalue is not sufficient.

## Frozen replay

Witness: `research-notes/lane_a_v15_499_folner_localization_upper_enclosure.py`  
Commit: `4d830b178154ab21a897afbd6b28c9d19fe55853`  
Blob: `176fe33c8b520785edb73bf50fd6a9d73bba786a`  
SHA-256: `14bd5f124c6da78deca28a0a7e19422ff0767c38c83a48763106ac762b623236`

Manifest: `research-notes/lane_a_v15_499_folner_localization_upper_enclosure.sha256`  
Commit: `3c94cf28e24ace6319ab5d525730b809fb340935`  
Blob: `693812ce7ce31cdd9f7b30183b18b0057a0d49e3`  
SHA-256: `2042c9d0fdfcd7428eba359c646ed1dde9b297576a8a641ced75327ba44bac7c`

Replay: `python3 -I lane_a_v15_499_folner_localization_upper_enclosure.py`. It reports `PASS_EXACT_FOLNER_LOCALIZATION_UPPER_ENCLOSURE`, 360 exact localization checks, all box and tent rational penalties, and leaves the finite matrix-field supremum and signed 45-diagonal norm explicitly unevaluated.

## Scope

The audited normalized frontier remains `2.892017147262984` against target `2.535946`; the required signed joint cross budget remains `<4.249030150943723`. This gate supplies the previously missing finite-section upper-error formula, not the matrix-field norm needed to test that budget.

This concerns only the noncanonical chosen-counting-measure `ell2` five-frequency commutator. It is not the whole `K`, not source-native Suzuki `Phi`, and not a physical spectral equivalence. `FULL_K_TRANSFER` remains `INCONCLUSIVE`. No whole-residual, stationary, capacity, or full-`K` conclusion is drawn.

HANDOFF
target: external-audit, sandbox
parent: v15.499
type: folner-localization-upper-enclosure-audit
status: open
action: independently verify the localization/isometry inequality, the box and tensor-tent correlations, the coefficient penalty, and the Round 509 q=2/r=4 illustrative-label correction; do not promote the decimal penalty orientation or any sampled finite-matrix eigenvalue to a certificate.
deliverable: correction or confirmation, then a rigorous outward enclosure of the radius-32 sparse Hermitian matrix-field essential supremum if runtime permits.
