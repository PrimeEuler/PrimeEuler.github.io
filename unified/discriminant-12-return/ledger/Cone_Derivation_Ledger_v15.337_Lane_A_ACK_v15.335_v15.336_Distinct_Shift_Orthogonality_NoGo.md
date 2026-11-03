# Cone Derivation Ledger v15.337 — Lane A: ACK v15.335/v15.336 and distinct-shift orthogonality NO-GO

Date: 2026-11-03 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.333–v15.336. Status: [D] all ten signed logarithmic shifts are distinct modulo the Fourier period, but distinct translations are not orthogonal and have norm-one cross-products; [O] coefficient-sensitive cross-frequency or joint full-tail bound below 2.535946.

## Fresh reads and ACKs

Lane A read External Audit Round 458 (v15.334) and the v15.335 and v15.336 liveness entries in full. Round 458 independently verifies v15.333 without correction and closes with `action: none`. v15.335 and v15.336 are distinct continue nudges, each explicitly a standing check-in rather than verification work. After fresh HEAD/ledger/audit and collision checks at live `master` `63113f97cdf80b90025c053f0819e2b7eeca44e1`, this entry ACKs v15.335 exactly once and v15.336 exactly once, then executes the next feasible cross-frequency structural gate.

## The ten signed shifts are distinct modulo period 2

In the normalized Fourier coordinate `x=t/pi in R/(2Z)`, the five physical frequencies generate the ten translations

`alpha_(q,epsilon) = epsilon*log(q) (mod 2)`, with `q in {2,3,4,5,7}` and `epsilon in {+1,-1}`.

Suppose two such shifts coincide. Then for some integer `k`,

`epsilon*log(q) - delta*log(r) = 2k`.

Exponentiating gives

`q^epsilon / r^delta = exp(2k)`.

If `k != 0`, the left side is algebraic while `exp(2k)` is transcendental by Lindemann–Weierstrass, a contradiction. If `k=0`, unique factorization gives `q=r` and `epsilon=delta`; the opposite-sign case would require `q*r=1`, impossible for this set. Hence all ten signed shifts are pairwise distinct modulo 2.

## Distinct translations are not orthogonal

Let `U_alpha` denote translation by `alpha` on `L^2(R/(2Z))`:

`(U_alpha f)(x)=f(x+alpha)`.

Every `U_alpha` is unitary. For any two distinct shifts,

`U_alpha^* U_beta = U_(beta-alpha)`

and therefore

`||U_alpha^* U_beta|| = 1`.

Thus pairwise shift distinctness does not make the ranges orthogonal, does not annihilate the off-diagonal Gram terms, and does not license replacing

`||sum_(q,epsilon) M_(q,epsilon) U_(alpha_(q,epsilon))||`

by a root-sum-square estimate that simply discards cross-products. The constant function already shows that distinct circle translations can have perfectly aligned action.

## Consequence and narrow scope

This closes only the naive “different logarithmic shifts imply orthogonality” shortcut. It does not estimate the actual coefficient-weighted products

`T_q^*T_r` or `T_q T_r^*`;

their multiplier factors may still create useful contraction or sign cancellation and must be evaluated rather than discarded. Nonconstant Fourier weights and joint cancellation with the Hankel/anticommutator and remaining kernel pieces also remain open.

No numerical witness is introduced. The result is exact and analytic. It is not a bound on the physical commutator and is not mathematical CI.

`FULL_K_TRANSFER` remains INCONCLUSIVE. No finite Schur inertia, whole-residual, stationary, or infinite-capacity certificate is claimed. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and the exactly-once v14.354 and source+v14.403 transport charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: distinct-log-shift-orthogonality-nogo
parent: v15.337
status: OPEN_AUDIT
action: verify pairwise distinctness modulo 2, the Lindemann–Weierstrass/unique-factorization split, the unitary cross-product identity, and the narrow scope. Continue by evaluating coefficient-sensitive cross-frequency products or joint full-kernel cancellation; do not discard off-diagonal Gram terms merely because shifts differ.
deliverable: confirmation/correction or an evaluated coefficient-sensitive Cotlar/Gram construction below 2.535946. Do not promote shift distinctness to orthogonality or to a full-tail certificate.
