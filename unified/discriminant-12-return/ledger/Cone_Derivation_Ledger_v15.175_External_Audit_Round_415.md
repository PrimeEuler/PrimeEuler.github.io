# Cone Derivation Ledger v15.175 — External Audit Round 415: verified v15.174

**Date:** 2026-10-30
**Track:** External Audit
**Status:** [D] independently re-derived the covariance and variance transfer bounds from scratch, term by term; all constants confirmed exact.
**Parents:** v15.172 (Round 414), v15.173, v15.174.

---

## Fresh pre-write check

Live `origin/master` was `da63d65` (v15.174) both at the start of this round and immediately before this write; no further commits landed in between. `v15.175` is the next free ledger number; no collisions found.

## Verification

v15.174 builds a covariance/variance transfer bound on top of the already-verified word-moment gate (Round 414). Re-derived both pieces independently:

- **The symmetrized second-moment term.** `W=TU+UT` is self-adjoint since `T,U` are (`(TU+UT)^*=U^*T^*+T^*U^*=UT+TU`), with `\|W\|\le\|TU\|+\|UT\|\le2\nu_T\nu_U`. Applying the already-verified single-operator bound `|\langle x,Wx\rangle-\langle y,Wy\rangle|\le4\|W\|E_Γ` gives `\le8\nu_T\nu_UE_Γ`; halving reproduces the claimed `4\nu_T\nu_UE_Γ` bound on `\big|\tfrac12\langle x,(TU+UT)x\rangle-\tfrac12\langle y,(TU+UT)y\rangle\big|` exactly. (Equivalently, applying the bound separately to `TU` and `UT` and summing gives the identical `8\nu_T\nu_UE_Γ` before halving — both routes agree, as they must.)
- **The product-of-means term.** Using the standard two-term split `\mathrm{mean}_x(T)\mathrm{mean}_x(U)-\mathrm{mean}_y(T)\mathrm{mean}_y(U)=\mathrm{mean}_x(T)[\mathrm{mean}_x(U)-\mathrm{mean}_y(U)]+\mathrm{mean}_y(U)[\mathrm{mean}_x(T)-\mathrm{mean}_y(T)]$, and bounding each factor (`|\mathrm{mean}_z(T)|\le\nu_T$, and the already-verified first-moment transfer `|\mathrm{mean}_x(T)-\mathrm{mean}_y(T)|\le4\nu_TE_Γ`), get `\le\nu_T\cdot4\nu_UE_Γ+\nu_U\cdot4\nu_TE_Γ=8\nu_T\nu_UE_Γ` — confirmed exactly matching the claimed term.
- **Sum.** `4\nu_T\nu_UE_Γ+8\nu_T\nu_UE_Γ=12\nu_T\nu_UE_Γ`, matching the final covariance bound exactly.
- **Variance corollary.** Setting `U=T` gives `12\nu_T\cdot\nu_T\cdot E_Γ=12\nu_T^2E_Γ`, matching exactly.

No commutation of `T,U` is assumed anywhere in the derivation (the bound on `TU+UT` doesn't require `[T,U]=0`), consistent with the entry's own statement. Scope is correctly preserved — explicitly not a positivity, concentration, or far-moment certificate for the actual source.

## Summary

A correctly-derived, slightly involved but fully verified extension of the moment-transfer machinery to covariance and variance. No corrections needed. `K_full` remains closed; production fence unchanged; the gravity lane's v15.138/v15.142 coefficient correction (Round 406) remains the only outstanding item in the project.

HANDOFF
target: lane-a, sandbox, external-audit
type: external-audit-round-415
parent: v15.175
status: closed
action: none — bounds verified correct. Sandbox's numerical instantiation remains open and unowned by this audit.
deliverable: none.
