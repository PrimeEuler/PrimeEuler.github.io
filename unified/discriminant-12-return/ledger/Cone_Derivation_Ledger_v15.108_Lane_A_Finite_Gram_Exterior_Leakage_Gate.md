# Cone Derivation Ledger v15.108 — Lane A: finite Gram block requires exterior leakage; source-native synthesis gate

**Date:** 2026-10-29. **Lane:** A / Suzuki. **Parents:** v13.661–662, v13.785, v15.018–021, v15.095, v15.097, Sandbox v15.106 (original v15.102-S, renumbered), Audit R401 v15.103. **Status:** [D] exact finite-block Gram/intertwining identity with exterior terms; [O] actual source-native Gram witness and operator closure.

**Pre-write collision check:** live HEAD `61746195dd08e437b69445917622aeaf61de99b3` (gravity v15.107); v15.108 next free. Additive only.

## 1. Audited return received

Sandbox v15.106 independently confirms full physical kernel `K[N,m]=c(m z_N-N z_m)/(N²-m²)+2 sigma p_N p_m` for distinct rows and real diagonal, so `K[N,m]=K[m,N]`. It proves, using the exact floor crossover and certified spike z, that the spike-star nonzero rows force diagonal weights constant on the certified tail for any diagonal-weight symmetric unchanged realization. Audit R401 replayed this return before collision renumbering. This is formal matrix symmetry, **not** operator self-adjointness.

## 2. A critical finite-block leakage identity

Suppose a source-native synthesis `J e_m=f_m` into a Hilbert space `H` and a densely defined self-adjoint source operator `B` genuinely satisfy the intertwining equation `BJ e_k=J K e_k` on a common domain with justified convergence. Set `G_{ij}=<f_i,f_j>`, and take the convention in which the corresponding Gram intertwining identity is `GK=K^*G`. For a finite index set `I`, and its complement `O`, the exact `I x I` block of this relation is

`G_II K_II + G_IO K_OI = K_II^* G_II + K_OI^* G_OI`,

hence

`G_II K_II-K_II^*G_II = K_OI^*G_OI-G_IO K_OI`.

Therefore **a 2-by-2 Gram block does not by itself satisfy or refute** `G_II K_II=K_II^*G_II`, unless the exterior leakage terms vanish or are rigorously bounded. This matters especially here: the frozen spike has nonzero couplings to arbitrarily remote rows, so cutting the matrix to two indices is not an invariant compression. An apparent 2x2 commutator defect might be entirely canceled by omitted exterior channels. The new gate refines v15.095's suggested 2x2 witness to include certified exterior terms.

For a real symmetric K, `K^*=K` on the algebraic core, but that does not justify asserting `GK=KG` as an unbounded operator identity: matrix product convergence and domains remain prerequisites. The finite-block identity is conditional on that already-justified equality.

## 3. Focused source-native test

Choose a *named* finite-a Suzuki energy space from v13.662 and a source-native synthesis rule. For example, a possible test family (not a proven bridge) uses source test functions `phi_m` and the bounded positive finite-a resolvent `T_a^{-1}`, setting `f_{a,m}=T_a^{-1}phi_m`. Then its Gram is exactly `G_a[m,k]=<phi_m,T_a^{-2}phi_k>_{L2}` **only if** this is actually the chosen L2 inner product and T_a is positive self-adjoint on that same L2 space. If instead using H(T_a), recompute the Gram in its *energy inner product* (no substitution of L2 is allowed). The source-native choice and normalizations must be justified first. Check the spike and partner; for each finite block compute/bound the exterior interaction rather than discarding it.

The initial target is a **genuine Gram/intertwining witness**, or a source-domain mismatch that excludes a candidate. Neither formal symmetry nor a finite numerical diagonalization supplies self-adjointness, a spectral measure, or a coupling to the actual K_full domain.

**HANDOFF**
target: sandbox / external-audit
type: source-native-Gram-with-exterior-leakage
parent: v15.108
status: OPEN_RESEARCH
action: complete the v15.106 part-(b) source-native Gram calculation with exact finite-a Suzuki inner product, compare a spike and partner against K_full using an explicit exterior leakage estimate or justified invariant core, and report a positive source-faithful witness or a negative obstruction. Verify v15.108 block identity independently.
deliverable: exact definitions, Gram and action pairings with tail remainder, replayable code/hashes. No full spectral/far production.

**Production fence:** v15.018 audited provenance obstruction remains scoped and in force; C_S_32000, 3e-5, 0.002 unchanged; no residual consumer, far rerun, stationarity, or infinite capacity; no charges repeated.
