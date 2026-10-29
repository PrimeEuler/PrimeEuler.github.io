# Cone Derivation Ledger v15.095 — Lane A: source-faithful finite-Suzuki-to-K_full bridge gate

**Date:** 2026-10-29. **Lane:** A / Cone–Suzuki. **Parents:** v13.661–662 (finite-A boundary triple and domain correction), v13.785 (source-faithful T-side transfer), v14.972, v15.018–021 (audited K_full provenance obstruction), v15.092. **Status:** [D] exact necessary intertwining/Gram criteria; [O] existence, limiting closure, and physical certification. No claims about an actual operator realization newly proved.

**Collision check:** live HEAD immediately before this additive deposit was `50af3fae4cec7fe62d36407b2127834a4ec635cb` (v15.094); v15.095 was unoccupied. Gravity files untouched.

## 1. What the old Suzuki source actually supplies

The finite-interval construction has `A_a=Friedrichs(D^*G_aD)` and `T_a=A_a-lambda I`; Suzuki's Section-8 transfer `bar D: H(T_a) -> H(S_a)` is isometric/unitary in the source's energy-space framework. The boundary-triple `Gamma_0,Gamma_1` and `H_{a,pi}=ker Gamma_0` are fixed for the finite first-order symmetric operator (v13.661). They do **not** by themselves identify a coefficient-space Hilbert completion for the *different* frozen infinite matrix `K_full`.

The earlier v13.662 correction is controlling: a local Dirichlet Laplacian is **not** the same-domain Suzuki Friedrichs operator. Do not smuggle it in as a reference.

## 2. Exact finite/core bridge criterion

Let `H_a` be the source-fixed finite energy Hilbert space and `B_a` an explicitly selected source-faithful operator or bounded resolvent on it (the choice must be named). To relate the countable physical coefficient core `c_00` with basis `e_m` to `H_a`, a candidate synthesis `J_a:c_00 -> H_a` must supply actual vectors `f_{a,m}=J_a e_m`. The Gram matrix and action matrix must be calculated in the **same** finite-source inner product:

`G_a[m,k]=<f_{a,m},f_{a,k}>_{H_a}`,
`Q_a[m,k]=<f_{a,m},B_a f_{a,k}>_{H_a}` (when the vectors belong to the domain).

If the candidate claims to transport `K_full` by a unitary (or isometric, dense-range) coefficient identification `J`, then on its stated common core the necessary equalities are

`G[m,k]=delta_{mk}` for the asserted unweighted unitary, or `G[m,k]=w_m delta_{mk}` for an asserted weighted diagonal coefficient norm;

and `B J e_k=J K_full e_k`, *with both sides in the same Hilbert space and defined on the relevant domain*.

In the weighted diagonal case, the matrix-element identity becomes `Q[m,k]=w_m K_full[m,k]` (with the chosen inner-product convention). Any claim that `B` is self-adjoint then additionally forces `w_m K_full[m,k]=w_k conjugate(K_full[k,m])` on the core. These are **testable necessary conditions**; merely observing similar kernels or matching finite eigenvalues is not enough. If the Gram is non-diagonal, the induced coefficient norm has Gram G and cannot be replaced by a guessed diagonal weight without a separately proved transformation.

## 3. The missing infinite-volume bridge

The finite-a construction lives on changing Hilbert spaces as a grows, so a limit requires identified isometries into a common comparison Hilbert space (or another explicitly justified convergence framework). To claim a canonical limiting spectral operator, one needs a specified core, limit operator and domain, convergence of embedded resolvents (with precise strong/norm-resolvent scope), and the relevant boundary/sector normalization. The isolated exact spike in v15.018 distinguishes l2 from l2(N): it cannot determine the correct completion, but **it is a mandatory domain test for any proposed one**. The existing source transfer bar D is *internal to the finite-a energy spaces* and is not itself an intertwiner onto K_full.

## 4. Next constructive task (strictly scoped)

Search the existing **source-faithful** finite-A realizations for a canonical sequence family f_{a,m} whose Gram and operator matrix can be computed against the **frozen physical K_full columns**. Start with a single exact certified spike column m1 (v15.018), check domain membership, then a 2-by-2 off-diagonal pair for adjoint/weight consistency, **before** attempting a complete spectral-measure or infinite-volume convergence proof. A failed Gram or intertwining identity should be recorded as a negative gate, not repaired by fitted weights or adjusted zeros. If a family passes, demand a common-space embedding and domain/core limit theorem next.

This entry defines an exact *bridge test*, not a construction of the bridge. Current gate remains `K_full=CLOSED_SCOPED_OBSTRUCTION_CURRENT_FROZEN_DATA`; no production is reopened.

**HANDOFF**
target: sandbox / external-audit
type: suzuki-finite-energy-to-Kfull-bridge-witness
parent: v15.095
status: OPEN_RESEARCH_NOT_PRODUCTION
action: identify source-native finite-a coefficient synthesis and operator, compute exact Gram and spike/2x2 action identities and domain conditions, report positive certified witness or precise obstruction; do not fit weights or launch far rows.
deliverable: source path + reproducible finite computations and frozen hashes, followed by independent audit.

**Fence:** original C_S_32000, thresholds 3e-5 and .002 unchanged; no v14.354/v14.403 charges; no residual-consumer run, F1/F2 refresh, stationary or capacity conclusion.
