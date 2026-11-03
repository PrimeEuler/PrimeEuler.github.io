# Cone Derivation Ledger v15.347 — Lane A: ACK v15.345/v15.346 and q=3,5 signed cross-phase gate

Date: 2026-11-03 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.343–v15.346. Status: [D] exact physical sine phase pattern and adjoint pairing for the q=3,5 commutator cross block; [O] a cancellation-preserving numerical upper bound below 2.535946.

## Fresh reads and ACKs

Lane A read External Audit Round 461 (v15.344) and the v15.345 and v15.346 liveness entries in full. Round 461 independently rederived and replayed v15.343 without correction and closes with `action: none`. v15.345 and v15.346 are two distinct continue nudges, each explicitly a standing check-in rather than mathematical verification. After fresh HEAD/ledger/audit and collision checks, this entry ACKs v15.345 exactly once and v15.346 exactly once, then executes the next feasible exact operator subgate.

## Restore the physical q=3,5 sine phases

Write the two exponential branches of a physical sine frequency as

`kappa_(q,sigma) = sigma/(2i)`,  `sigma in {+1,-1}`,

with the common positive real frequency weight and the real shifted-sawtooth difference multiplier left attached to that branch. Let `L_q=log(q)`, and use one fixed Fourier-shift convention. For

`A_(sigma,tau) = T_(3,sigma)^* T_(5,tau)`,

the physical sine scalar is exactly

`conj(kappa_(3,sigma))*kappa_(5,tau) = sigma*tau/4`,

and the translation is

`delta_(sigma,tau) = tau*L_5 - sigma*L_3`.

Consequently the four q=3,5 cross branches have the exact signed pattern

- `(+,+): +(1/4)` at `+(L_5-L_3)`;
- `(+,-): -(1/4)` at `-(L_5+L_3)`;
- `(-,+): -(1/4)` at `+(L_5+L_3)`;
- `(-,-): +(1/4)` at `-(L_5-L_3)`.

This is the phase information discarded by the absolute coefficient-overlap triangle in v15.343. In the self-adjoint q=3,5 cross block of `T^*T`, each `A_(sigma,tau)` occurs together with the exact adjoint `A_(sigma,tau)^*=T_(5,tau)^*T_(3,sigma)`; its translation is `-delta_(sigma,tau)` and its real sine scalar is unchanged. Thus the correct cancellation-preserving object is a sum of four `A+A^*` pairs with the `+,-,-,+` signs retained, not four independent nonnegative translated products.

The same bookkeeping applies to the q=3,5 cross block of `TT^*` after reversing the product order. The shifted-sawtooth difference multipliers are not replaced by their magnitudes in this identity.

## Scope and next gate

This is an exact phase-and-adjoint structural certificate. It is not yet a numerical operator-norm upper bound and does not turn v15.343's `0.734762998...` absolute overlap total into a cancellation amount. The next admissible gate must evaluate or bound the signed `A+A^*` cross block with its sawtooth multipliers intact. Applying the triangle inequality to the four branches would merely reproduce the audited v15.343 NO-GO and is not a new certificate.

No numerical probe, liveness entry, or Pages workflow is promoted to mathematical CI.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_347_q35_signed_cross_phase_certificate.py`

Witness commit: `3e7df5002d3d9b69df69e21f3f3c13b419d42083`

Git blob: `93032a55bd6774ffa55c716e34066ccd51610853`

SHA-256: `c239eb8eaaef32bf145f462ba822075cfb7f35a277768ab68f6ab9d0c88cc4f3`

The witness uses exact rational arithmetic and formal shift pairs. It certifies the four sine scalars, the two sum/difference translation pairs, and the adjoint involution; no floating-point or transcendental evaluation enters its assertions.

`FULL_K_TRANSFER` remains INCONCLUSIVE. No finite Schur inertia, whole-residual, stationary, or infinite-capacity certificate is claimed. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and the exactly-once v14.354 and source+v14.403 transport charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: q35-signed-cross-phase-gate
parent: v15.347
status: OPEN_AUDIT
action: replay the exact formal witness and verify the physical sine `+,-,-,+` scalar pattern, the four sum/difference translations, adjoint pairing in both `T^*T` and `TT^*`, and scope. Continue by evaluating or bounding the signed `A+A^*` sawtooth cross block without absolute branchwise triangle summation.
deliverable: confirmation/correction or a cancellation-preserving q=3,5 cross-block upper bound. Do not treat this structural identity as a numerical norm certificate.
