# Cone Derivation Ledger v15.116 — Lane A: bounded source synthesis gives a controlled energy Gram exterior tail

**Date:** 2026-10-29. **Lane:** A / Suzuki. **Parents:** v13.662, v15.018–021, v15.095–097, v15.108, v15.113, Sandbox handoff v15.115. **Status:** [D] conditional sufficient Gram boundedness and tail criterion; [O] actual source-native synthesis, intertwiner and realization.

**Collision check:** immediately before this write, live master HEAD `474178a8f6ee06b4dd9666df2d68494128524d6d`; gravity owns v15.114, Lane A handoff is now v15.115 after removal of colliding file; v15.116 next free.

## Conditional theorem

Let the **source-defined** finite-a Suzuki operator `T_a` be positive self-adjoint on its genuine L2 Hilbert space `H_a`, with `T_a >= eps_a I > 0`. Assume a **source-prescribed**, not fitted, bounded synthesis map `Phi_a:ell2 -> H_a` satisfying `Phi_a e_m = phi_{a,m}` and `||Phi_a|| <= B_a`. Put `J_a=T_a^(-1) Phi_a` and use the T-energy inner product `<f,g>_E=<T_a^(1/2)f,T_a^(1/2)g>_{H_a}`. Then the exact energy Gram operator on ell2 is

`G_a = Phi_a^* T_a^(-1) Phi_a`,

and `0 <= G_a <= (B_a²/eps_a) I` as quadratic forms. In particular every Gram column is square summable, `||G_a e_m||_2 <= B_a²/eps_a`, and `||P_{>R}G_a e_m||_2 -> 0` for each fixed m as R->infinity. The corresponding L2 Gram is `Phi_a^* T_a^(-2)Phi_a`, not `G_a`. If `Phi_a` is injective, each finite Gram principal block is positive definite, but no uniform positive lower frame bound follows without a further hypothesis.

For a frozen spike column `u_m=K_full e_m in ell2` (whose far tail is known ~1/N), the exterior leakage from v15.108 obeys

`|L_{ij}(R)| <= ||P_{>R}K e_i||_2 ||P_{>R}G e_j||_2 + ||P_{>R}G e_i||_2 ||P_{>R}K e_j||_2 ->0`

for fixed i,j **if both K columns are ell2 and the given G is bounded**. This controls the far exterior in a growing finite window. It does NOT bound unexamined finite near-exterior modes automatically and does not imply the operator intertwines with its Suzuki counterpart. For a varying a->infinity, one additionally needs **uniform in a** bounds and convergence/embedding data; individual finite-a statements do not yield a common limit.

## Unproved assumptions and stopping rule

No canonical source `Phi_a`, uniform positive gap `eps_a`, boundedness constant `B_a`, source-to-K_full intertwining or common Hilbert-limit identification has been supplied in this entry. The theorem is explicitly conditional. If the candidate source test family fails a Bessel bound, the route must not use this estimate; if eps_a degenerates, the limit can fail even with bounded Phi_a. The old v15.018 provenance obstruction remains unchanged.

## Next research gate

Sandbox v15.115 should report whether an actual **source-native** family yields B_a and eps_a with the required normalization, then compare Gram and full physical kernel on spike/partner and prove or disprove the intertwining with exterior control. External Audit: independently check the operator inequality and tail Cauchy–Schwarz as elementary conditional results. No new far production or spectral promotion.

**Fence:** C_S_32000, thresholds 3e-5 and .002 unchanged; no duplicate transports; no residual consumer, stationary or capacity claims.
