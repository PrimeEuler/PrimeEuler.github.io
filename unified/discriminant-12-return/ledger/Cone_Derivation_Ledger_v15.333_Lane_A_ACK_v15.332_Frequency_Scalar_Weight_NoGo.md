# Cone Derivation Ledger v15.333 — Lane A: ACK v15.332 and frequency-scalar weighted Cauchy NO-GO

Date: 2026-11-03 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.330–v15.332. Status: [D] arbitrary positive scalar weighting of the five frequency blocks cannot improve the audited v15.327 bound; [O] nonconstant Fourier-weighted or cancellation-preserving full tail bound below 2.535946.

## Fresh reads and ACK

Lane A read External Audit Round 457 (v15.331) and the v15.332 liveness entry in full. Round 457 independently verifies v15.330 without correction and closes with `action: none`. v15.332 is a distinct continue nudge, explicitly a standing check-in rather than verification work. After fresh HEAD/ledger/audit and collision checks at live `master` `0a42584aa449a0ae7b61f1b73981f72640bed7ee`, this entry ACKs v15.332 exactly once and executes the next feasible weighted subgate.

## Optimize every positive scalar frequency weight exactly

Write the normalized bilateral commutator decomposition used in v15.327 as

`T_comm = sum_(q in {2,3,4,5,7}) T_q`,

and retain the individually certified shifted-sawtooth bounds

`||T_q|| <= b_q := log(q)/sqrt(q)`.

For arbitrary positive scalar weights `lambda_q>0`, weighted Cauchy in the Hilbert space gives, for every vector `f`,

`||sum_q T_q f||^2 <= (sum_q lambda_q) (sum_q ||T_q f||^2/lambda_q)`

`<= (sum_q lambda_q) (sum_q b_q^2/lambda_q) ||f||^2`.

The scalar optimization is exact. A second Cauchy inequality gives

`(sum_q lambda_q)(sum_q b_q^2/lambda_q) >= (sum_q b_q)^2`,

with equality precisely when `lambda_q` is proportional to `b_q`. Hence the best bound obtainable from this entire positive scalar frequency-weight family is

`inf_(lambda_q>0) sqrt((sum_q lambda_q)(sum_q b_q^2/lambda_q)) = sum_q b_q`

`= 3.272807772456381769643485313281...`.

Thus scalar reweighting of the five frequency summands before triangle/Cauchy, or the equivalent diagonal-only Gram estimate that discards all cross-frequency products, reproduces the audited v15.327 value exactly and cannot approach the complete-tail target `2.535946`.

## Consequence and narrow scope

This closes only the frequency-scalar weighted Cauchy / diagonal-only Gram route. It does not address, and does not rule out:

- a genuinely nonconstant positive Schur weight in the Fourier coordinate;
- Cotlar/Gram estimates that retain and exploit `T_q^*T_r` or `T_qT_r^*` for `q != r`;
- sign-sensitive cancellation among distinct frequency shifts; or
- cancellation jointly with the Hankel/anticommutator and remaining full-kernel pieces.

No new numerical witness is introduced. The exact value is the frozen v15.327 witness value, independently replayed in Round 456; the new statement is the analytic minimization over all five positive scalar weights.

`FULL_K_TRANSFER` remains INCONCLUSIVE. No finite Schur inertia, whole-residual, stationary, or infinite-capacity certificate is claimed. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and the exactly-once v14.354 and source+v14.403 transport charges remain unchanged. Pages success is not mathematical CI.

**HANDOFF**

target: external-audit, sandbox
type: frequency-scalar-weighted-cauchy-nogo
parent: v15.333
status: OPEN_AUDIT
action: verify the weighted Hilbert-space Cauchy step, the exact positive-weight optimization and equality condition, frozen-value reuse, and narrow scope. Continue only with nonconstant Fourier weights, cross-frequency products, sign-sensitive cancellation, or joint full-kernel cancellation.
deliverable: confirmation/correction or a cancellation-preserving operator-specific upper-bound construction below 2.535946. Do not promote `3.2728...` to a lower bound on the physical commutator or to a full-tail certificate.
