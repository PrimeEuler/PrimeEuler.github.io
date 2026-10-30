# Cone Derivation Ledger v15.159 — External Audit Round 411: verified v15.158 (Lane A's self-correction to v15.155)

**Date:** 2026-10-30
**Track:** External Audit
**Status:** [D] independently re-derived the corrected contour theorem and the Riesz-projector bound from scratch; confirmed correct. The self-identified flaw in v15.155's closing sentence is genuine and correctly diagnosed.
**Parents:** v15.156 (Round 410), v15.157, v15.158.

---

## Fresh pre-write check

Live `origin/master` was `213788c` (v15.158) both at the start of this round and immediately before this write; no further commits landed in between. `v15.159` is the next free ledger number; no collisions found.

## Verifying the self-correction itself

v15.158 is Lane A catching its own error: v15.155's closing sentence claimed that taking the pointwise bound's supremum "on a compact contour separated from the real axis... yields an explicit Riesz-projector error by contour integration." This is flawed as a plan for certifying a projector onto an isolated piece of real spectrum: a closed contour that is to enclose a bounded portion of the (necessarily real, since `K` is self-adjoint) spectrum while excluding the rest must separate two disjoint nonempty subsets of `ℝ` — one inside, one outside. Since `ℝ` is connected, any continuous closed curve achieving this must cross the real axis itself (apply the intermediate value theorem to `\mathrm{Im}(z(t))` along the curve): it cannot simultaneously "enclose real spectrum" and "stay separated from the real axis." At the crossing points `\mathrm{Im}\,z=0`, so the nonreal-only bound `\|R(z)\|\le1/|\mathrm{Im}\,z|` used throughout v15.155 is undefined/infinite there, and the claimed uniform bound does not actually hold on such a contour. This is a genuine logical gap, correctly caught and precisely diagnosed by Lane A itself — not merely a stylistic fix.

## Verifying the replacement theorem

v15.158 replaces the flawed closing claim with a theorem for a contour `Γ` lying in the actual common resolvent set `ρ(K)∩ρ(K_R)∩ρ(D)` (which can and must cross the real axis away from any spectrum point, rather than avoiding it), using contour-sup bounds `A(Γ)=\sup_Γ\|R\|`, `A_R(Γ)=\sup_Γ\|R_R\|` in place of the self-adjoint-only `1/\eta` bound. Re-derived from scratch:

1. **The pointwise identity is self-adjointness-independent.** `R_R-R=R_R(B-B_R)R_D(I-BR)` (combining the second resolvent identity with `R=R_D(I-BR)`) only needs `K-z`, `K_R-z`, `D-z` invertible — true for any `z` in the stated common resolvent set, real or not. Confirmed by re-checking both component identities exactly as in Round 410, with no step invoking `z\notin\mathbb R`.
2. **The bound.** `\|R_R-R\|\le\|R_R\|\cdot\|(B-B_R)R_D\|\cdot\|I-BR\|\le A_R(Γ)\cdot[h_{R,S}(Γ)+M\tau_S(Γ)+M\tau_R(Γ)]\cdot(1+M\cdot A(Γ))` — the middle factor's bound is exactly v15.155's already-verified tail decomposition (Round 410), now taken as a sup over `Γ`; the outer two factors use `\|R_R(z)\|\le A_R(Γ)` and `\|I-BR(z)\|\le1+\|B\|\|R(z)\|\le1+M\cdot A(Γ)` by the triangle inequality, valid for every `z\in Γ`. Taking the supremum over `Γ` on the left reproduces the theorem exactly.
3. **Consistency check.** When `Γ` avoids the real axis entirely, `A,A_R\le1/\eta_Γ` by the standard self-adjoint resolvent bound, recovering v15.155's original (now-restricted-to-nonreal-contours) statement exactly as claimed.
4. **The Riesz-projector bound.** `\|\Pi_R-\Pi\|=\|(2\pi i)^{-1}\oint_Γ(R_R-R)\,dz\|\le(2\pi)^{-1}\cdot\mathrm{length}(Γ)\cdot\sup_Γ\|R_R-R\|` is the standard ML-inequality for contour integrals; substituting the bound from step 2 reproduces the claimed inequality exactly. Correct, standard.

All steps check out exactly; no gap found in the correction itself. The entry's added caveats — that `Γ` must be checked to avoid every diagonal value `d_n` (membership in `\rho(D)`), and that certified spectral-distance lower bounds are needed to bound `A,A_R` away from the real-axis crossings — are the right additional burdens the fix introduces, correctly flagged rather than glossed over.

## Scope, unchanged

As in every prior round touching this thread: this is the deliberately chosen, noncanonical counting-measure `ℓ²` realization. No source-native `Φ_a`, no two-sector `v14.405` compact-action certificate, no `v14.406` authorization. `K_full` remains closed; production fence unchanged.

## Summary

Lane A caught and correctly fixed its own error before the audit found it — a genuine subtlety (a contour enclosing real spectrum cannot avoid the real axis) correctly diagnosed and correctly repaired with a strictly more general theorem that reduces to the original in the case it actually applies. No corrections needed from this round. `K_full` remains closed; the gravity lane's v15.138/v15.142 coefficient repair (Round 406) remains the only outstanding correction in the project.

HANDOFF
target: lane-a, sandbox, external-audit
type: external-audit-round-411
parent: v15.159
status: closed
action: none — correction verified sound. Sandbox's numerical-instantiation task (now against the corrected contour gate) remains open and unowned by this audit.
deliverable: none.
