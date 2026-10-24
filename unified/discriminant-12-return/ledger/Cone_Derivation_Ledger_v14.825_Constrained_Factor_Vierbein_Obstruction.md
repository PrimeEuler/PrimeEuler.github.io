# Cone Derivation Ledger v14.825 — Constrained factor vierbein and frozen-graviton obstruction

Date 2026-10-24. Gravity lane. Parents v14.818–824. Research note research-notes/Four_Factor_Constrained_Vierbein_Action_Degeneracy.md, commit 7e43f8c059a454fa6a1ed4fdf45a7b3e20c15c27. Live HEAD immediately before write 7e43f8c059a454fa6a1ed4fdf45a7b3e20c15c27. Additive only, protected Suzuki/far residual untouched.

## Covariant Cone vierbein [D]
For four positive scalar factor coordinates X^A, set r=Σ_A log X^A, s_A=log X^A-r/4, and z^i an orthonormal basis of the three-dimensional sum-zero shape hyperplane. The coframe \(e^0=(\sqrt3/2)e^{r/2}dr,\ e^i=e^{r/2}dz^i\) gives
\[
h_{\mu\nu}=\eta_{ab}e^a_\mu e^b_\nu=H_{AB}(X)\partial_\mu X^A\partial_\nu X^B,
\quad H_{AB}=\partial_A\partial_B\prod_C X^C.
\]
On nondegenerate factor maps this is a Lorentzian metric, locally diffeomorphic to the k=4 metric in v14.820.

## Explicit constrained on-shell action [D]
Let independent g, symmetric Λ^{μν}, and fluid labels φ^I have action
\[
S=\int\sqrt{-g}\left[\frac{R(g)}{2\kappa}-C b^{2/3}
+\frac12\Lambda^{\mu\nu}(g_{\mu\nu}-h_{\mu\nu}(X))\right]d^4x,\quad
b=\sqrt{\det(-g^{\mu\nu}\partial_\mu\phi^I\partial_\nu\phi^J)}.
\]
Variation in Λ gives g=h. The branch Λ=0, g=h, φ^I=z^I with κC=1 has the exact linearly expanding FLRW solution of v14.821–822, and satisfies X equations because all X dependence occurs in the multiplier term. This is an on-shell construction, **not** a selection theorem derived from AM–GM symmetry.

## Rigidity/stability obstruction [D/O]
For invertible X maps, the scalar factors are locally admissible spacetime coordinates. g=h then fixes the metric locally modulo diffeomorphisms: no independent local spin-2 gravitational perturbations remain. The model omits the naive indefinite Hessian sigma-model kinetic term (the immediate ghost of v14.823) but this does NOT establish a complete ghost-free Hamiltonian theory or viable GR limit. Constraint/multiplier modes remain untested.

Next gate: weaken the metric constraint to preserve a healthy dynamical spin-2 sector, establish an explicit constraint algebra and physical-sector energy positivity, while explaining why any proposed new action is selected rather than engineered. No G derived.

Flags: constrained_vierbein_exact=TRUE; on_shell_FLRW=EXACT_CONDITIONAL; local_spin2_frozen=TRUE; naive_sigma_ghost_avoided=TRUE; full_stability=OPEN; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.

HANDOFF
target: external-audit
type: gravity-vierbein-constraint-audit
parent: v14.825
status: open
action: Check coframe/pullback equivalence, all variational branches, Λ=0 on-shell solution, and the local frozen-graviton reasoning. Do not claim Hamiltonian ghost-freedom from omission of the naive sigma-model term.
deliverable: independent scoped verdict; leave Suzuki and far residual untouched.
