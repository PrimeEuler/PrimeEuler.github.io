# Cone Derivation Ledger v15.992 — Open quarter two-circle bridge versus sourced Maxwell/K4 selection

**Date:** 2026-11-14 US Eastern. **Lane:** Gravity. **Question:** Does the established Maxwell/K4 action activate the *original-unit-step* q2 open-boundary bridge T from v15.602/v15.991, with its specific boundary matrix elements? **Status:** [D] exact selection rule and coefficient comparison in a specified canonical two-mode Schwinger embedding; [N] leading quadratic Maxwell/Fermi tidal operators cannot realize T there; [C] quartic oscillator interaction could have the appropriate charge change, but its amplitudes are not those of T and the needed coefficient is unselected; [O] a physically derived non-Schwinger carrier or higher-order covariant field action.

**Redundancy/audit:** v15.602 (independently audited v15.603) constructed the original-unit-step q2 boundary defect E and T with T†T=2E; v15.628 (Audit v15.629) proved T preserves L parity and distinguishes it from an odd-rung bridge. v15.695 (its earlier script repaired additively at v15.701) derives the conventional curved Maxwell source and unselected odd-rung normalization; v15.696/702 prove invariant KK/Taub–NUT source/fiber-charge preservation. v15.908/914 give physical leading magnetic J_y and Fermi tidal J_x and full quadratic a_i a_j/a_i†a_j† terms. v15.918 velocity parity no-go. v15.991 already corrects v15.989's too-narrow closed q2 Casimir interpretation. Latest independent Audit Round 583/v15.990, commit 1f4a0031dbe63c9779f1e8d317b17072b8e24ab5, verified v15.988–989; v15.991 is pending. **Immediately prewrite live HEAD** 5e074ce8b6a7c035e43ab372f18959496cd3f39b (exact executable). Target checked absent. Strictly additive; certified/Audit/Suzuki/Muse/Sandbox files untouched.

## Gate 814 — canonical q2 embedding makes T a highly specific operator

In the original q=2 refined shell, geometric magnetic m_q=−L/4+i/2 for i=0,...,L and original-unit-step J+ moves i→i+2. The previous v15.602 cross-shell T has L′=L+2 and connects the upper boundary source i=L−1 to upper target i′=L+2, with mirrored lower boundary link i=1 to i′=0. Each has amplitude sqrt(w_L), where **w_L=(L+1)/4**.

The *canonical alternative physical Schwinger embedding* of the refined nodes into two native oscillator occupations is **n1=i, n2=L−i**, with physical spin L/2 and **m_phys=(n1−n2)/2=2m_q**. This is the *closed refined-step representation* at the level of states, but we retain T's ORIGINAL unit-step boundary pattern and test its matrix elements on those same node labels. This is a deliberate comparator, not proof that this embedding is the physical Cone gravity sector.

The upper boundary T maps

**(n1,n2)=(L−1,1) -> (L+2,0)**,

and the lower mirror maps **(1,L−1)->(0,L+2)**. Thus the source requires respectively

**(Delta n1, Delta n2)=(+3,−1)** or **(−1,+3)**,
**Delta N=+2, Delta m_phys=+2 or −2**, and **Delta m_q=±1**.

The boundary raising map shifts **L→L+2**, conserving refined χ=(-1)^L. It is not automatically the missing odd-quarter EM↔gravity source (v15.628).

## Gate 815 — physically sourced leading magnetic/tidal quadratic terms cannot connect these boundaries

In this canonical two-mode oscillator embedding:

- The weak-field magnetic J_x/J_y number-conserving mode transfer has **Delta N=0**, so cannot implement T's Delta N=+2.
- The full physical leading Fermi tidal Hamiltonian in v15.914 is quadratic in q1,q2 and hence quadratic in a_i,a_i†. Its **Delta N=+2** component contains only bilinear creation operators a1†², a1†a2†, a2†², which have **Delta m_phys=+1,0,−1**, respectively.
- The open boundary T needs **Delta m_phys=±2** at the same Delta N=+2. Therefore **every leading quadratic Fermi tidal matrix element between T's source and destination states vanishes exactly** in this embedding. This is a degree/occupation selection rule, not numerical smallness.
- The standard curved Maxwell bilinear source of v15.695 excites gauge-field modes but supplies no canonical identification of its field photon transfer with T's two-mode occupation labels. It does not circumvent the detector selection rule merely because its amplitude is sourced.

The result does not prohibit distinct higher-order gravitational waves, nonminimal detector matter interactions, multi-mode or enlarged physical carriers. It explicitly rules out the **specified original T** within the **specified ordinary quadratic two-mode detector**. The invariant KK fiber result v15.702 is a separate charge-selection theorem; do not conflate fiber charge k with q2 shell L without a derived map.

## Gate 816 — lowest-degree oscillator monomial allowance and coefficient mismatch

A normal-ordered oscillator monomial meeting upper boundary changes (+3,−1) is **(a1†)^3 a2**, with lower mirror **(a2†)^3 a1**. This is **quartic**, not quadratic. Its exact source-to-target amplitude on (L−1,1) is

**A4(L)=sqrt[L(L+1)(L+2)]**.

By contrast the geometric original-unit-step boundary T has **A_T(L)=sqrt[(L+1)/4]**. To match the two using one monomial with a coefficient, its required value is

**c_L=A_T/A4=1/[2 sqrt(L(L+2))]**.

This explicitly **depends on L**. A single constant multiple of the simple quartic monomial cannot reproduce all boundary shell weights. Nonpolynomial number-dependent dressings or alternative matter field couplings can be designed to fit, but their normalization and physical selection must be derived from a covariant action, not reverse-engineered from T.

For L=3: A_T=1, A4=sqrt60, c_3=1/sqrt60. The exact q2 boundary construction is neither a spontaneous universal coefficient nor automatically a seeded ordinary Maxwell/Gertsenshtein frequency law.

## Gate 817 — exact reproducibility and physical verdict

**Script:** `research-notes/k4_open_boundary_physical_source_selection_v15_992.py`, additive commit **5e074ce8b6a7c035e43ab372f18959496cd3f39b**. Executed locally: PASS across L=3..21 on both occupation shifts, quadratic creation-pair selection, quartic exact Fock amplitudes, needed shell-dependent normalization, radius difference 1/2, parity preservation. The test requires no chosen G, force or detector frequency. Independent Audit pending.

**Positive:** The user-corrected open quarter ladder is a genuine nonzero cross-shell boundary map in the refined lattice. Its exact occupation changes and minimal oscillator operator degree are now explicit in a standard physical comparator. It is a stronger, useful source-search target than a central Casimir.

**Negative:** The *already sourced leading* magnetic and Fermi tidal terms do not activate those links in the canonical two-mode embedding. The allowed quartic comparator has a different shell amplitude profile, and a universal physical coefficient cannot be read from the null circle. There is currently no demonstrated experimental Cone-specific EM/G cross-sector observable.

**Next/Audit/Muse:** independently check T's i↔i′ endpoint convention and exact (+3,−1) changes in both branches. Test whether a real physically justified K4 or Maxwell higher-order interaction contains the quartic monomial with the necessary geometric projection and shell coefficient, or if all existing locally covariant action terms force a mismatch. A source term with genuinely new degrees of freedom must supply its own field content, charge and normalization; do not quietly substitute the closed q2 ladder.
