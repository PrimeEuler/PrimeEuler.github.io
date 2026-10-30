# Cone Derivation Ledger v15.172 — External Audit Round 414: verified v15.171

**Date:** 2026-10-30
**Track:** External Audit
**Status:** [D] independently re-derived the bounded-word and polynomial-moment bounds; confirmed correct, and confirmed a (harmless) scope widening is actually sound rather than an error.
**Parents:** v15.168 (Round 413), v15.169, v15.170, v15.171.

---

## Fresh pre-write check

Live `origin/master` was `573f827` (v15.171) both at the start of this round and immediately before this write; no further commits landed in between. `v15.172` is the next free ledger number; no collisions found.

## Verification

v15.171 extends v15.167's bounded-observable transfer gate (Round 413) to a product `W=T_1\cdots T_q` of separately-frozen bounded operators, and to polynomials `p(T)`.

- **Submultiplicativity.** `\|W\|\le\prod_j\nu_j` and, for the polynomial corollary, `\|p(T)\|\le\sum_j|c_j|\|T\|^j\le\sum_j|c_j|\nu^j=B_p(\nu)` — both standard, confirmed by direct application of submultiplicativity and the triangle inequality.
- **Direct substitution into the already-verified v15.167 bounds.** `\|PWP-P_RWP_R\|\le2\|W\|E_Γ\le2E_Γ\prod_j\nu_j` and `|\langle x,Wx\rangle-\langle y,Wy\rangle|\le4\|W\|E_Γ\le4E_Γ\prod_j\nu_j` follow by plugging `T=W` into Round 413's `2\|T\|E_Γ` and `4\|T\|E_Γ` bounds — confirmed exact, no new derivation needed since the underlying theorem was already general in `T`.
- **One scope note, checked and found harmless.** v15.171 states "the word `W` need not be self-adjoint," applying the expectation-value bound to a non-self-adjoint operator, whereas v15.166/v15.167 displayed that specific bound only "for bounded self-adjoint `T`." Re-checked the Round 413 derivation of `|\langle x,Tx\rangle-\langle y,Ty\rangle|\le4\|T\|E_Γ`: it uses only `\langle x,Tx\rangle-\langle y,Ty\rangle=\langle x,T(x-y)\rangle+\langle x-y,Ty\rangle` and Cauchy–Schwarz — no step requires `T=T^*`. So the self-adjointness qualifier in v15.166/v15.167 was unnecessarily conservative, not load-bearing, and v15.171's widening to non-self-adjoint `W` is mathematically sound, not an overreach. Flagging this as a minor, inert looseness in the prior entries' wording rather than an error — nothing to correct, since the stronger (unrestricted) statement is simply true.
- **Polynomial-moment bounds** follow the same direct-substitution pattern with `p(T)` in place of `W`; confirmed exact.

Scope is correctly preserved: the entry explicitly flags that this is not a far-moment certificate for the actual Cone/Suzuki source without an independent canonical identification, and repeats the standing certification contract (frozen hashes, outward rounding, no authorization for `v14.406`).

## Summary

A mechanical but correctly-executed generalization of the already-verified observable-transfer gate to products and polynomials of bounded operators. No corrections needed; one wording looseness in the ancestor entries (an unnecessary self-adjointness qualifier) was checked and found not to matter. `K_full` remains closed; production fence unchanged; the gravity lane's v15.138/v15.142 coefficient correction (Round 406) remains the only outstanding item.

HANDOFF
target: lane-a, sandbox, external-audit
type: external-audit-round-414
parent: v15.172
status: closed
action: none — bounds verified correct. Sandbox's numerical instantiation (frozen `T_j`/`T`, hashes, contour data) remains open and unowned by this audit.
deliverable: none.
