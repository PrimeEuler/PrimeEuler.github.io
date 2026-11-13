# Cone Derivation Ledger v15.930 — Round 574 audit repairs and exact boundary-Jacobi anomaly of weighted quarter-rung maps

**Date:** 2026-11-13 US Eastern. **Track:** Gravity/EM physical operator gates and Audit response. **Parents:** External Audit Round 574 v15.929; v15.140, v15.180, v15.572–574, v15.602/627 and Gravity v15.921–928. **Live HEAD immediately before this ledger write:** 9866f7d3d28f179fc417ecd9e015379467303995. Ledger target checked absent. Strictly additive; original historical scripts preserved; no modifications to audited objects, frozen Suzuki, Sandbox, or certified work.

**Status:** [D] exact boundary-defect Jacobi identity; [N] exact SymPy sweep L=2..25 and complete constant-mixing obstruction; [R] additive repairs to Auditor's identified two reproducibility issues; [O] physically justified boundary tensor, Hamiltonian and cross-principal-shell hydrogen E1 normalization.

## Audit Round 574 response — fully additive

External Audit v15.929 independently verified Gravity v15.918–928 and found **no errors in claimed mathematics**. It flagged two reproducibility issues.

1. Historical script `k4_quarter_staircase_product_transport_v15_926.py` uses upward-oriented factors for the lower/downward omitted transition. This causes assertion failure in the script, even though its ledger theorem specifies the correct downward orientation. A fresh additive corrected copy is `research-notes/k4_quarter_staircase_product_transport_v15_926_audit_repair_v15_930.py`, commit **5ec768d77f109bd12d9676f6ff43e553ff9bfd4f**. It sets lower source `m_l=-j+i_lower/2`, `a_l=j+m_l`, `b_l=j-m_l+1`, yielding `a_lb_l=j+1/4`. Original file remains untouched. Audit independently tested the exact correction in a scratch copy across all 80 shells; this copy reproduces that fix.
2. v15.921 had no standalone script. Additive `research-notes/k4_legacy_webgl_amgm_v15_921_audit_reproducer_v15_930_validated.py` was added in commit **9866f7d3d28f179fc417ecd9e015379467303995**, checking legacy `webgl/index.html` identities for X,Y²,T, the original t-scaling and hyperbola equality, the D=5 shell, and 420 finite sample points. Its first deposited draft `.../k4_legacy_webgl_amgm_v15_921_audit_reproducer_v15_930.py` (commit 87c3b9e53c7167baa02be189949680416e280f74) had a mistaken terminal print label saying “1680 sample points”; the validated add-only copy corrects the label to “420 sample points” and is the recommended execution target. No prior user webpage or ledger edited.

## Gate 671 — exact boundary-Jacobi identity

On the original **defective** q=2 quarter-refined shell `H_L`, define `J±, M` as in v15.602 and `D_L=[J+,J−]−2M`. Let `U:H_L→H_{L+1}` be any of the three nonzero weighted shifts from v15.928. Then

**J+_(L+1) U=U J+_L**, and **M_(L+1) U−U M_L=qU**, with q=−1/4 for A and q=+1/4 for B.

Define its lowering commutator **F_-=J−_(L+1)U−UJ−_L**. The exact Jacobi relation is

**J+_(L+1)F_−−F_−J+_L=2qU + (D_(L+1)U−UD_L)**.

This follows from `[J+,J−]=2M+D` and raising covariance; no model-specific approximation. The correction **B_U=D_(L+1)U−UD_L** is zero in an ideal undeformed SU(2) algebra but is nonzero here because the quarter-grid has missing/open endpoints. The magnetic charge of F_- is q−1, again an exact commutator statement, not a physical electromagnetic photon polarization.

## Gate 672 — the correction is boundary-localized and survives every constant mixture

Using the three basis weighted solutions `U_A,U_B0,U_B1` of v15.928, exact symbolic checks across **L=2..25** show that each **B_U** has rank 1 or 2 and is nonzero. Every nonzero matrix entry touches a source or target defect site of the previously audited `D_L` or `D_(L+1)`. The rank is a property of these **specified** weighted null maps; no universal rank-two claim for arbitrary operators is intended.

To test whether an arbitrary constant combination could cancel the anomaly, form `U=c_A U_A+c_0U_B0+c_1U_B1` and the linear map `(c_A,c_0,c_1)→B_U`. Across every tested L=2..25 the exact coefficient matrix has full rank **3**, so `B_U=0` only when all three coefficients vanish. Different magnetic-charge and parity-sector supports prevent a simple cancellation. This is a **strict no-go only inside the three-dimensional raising-compatible family** of v15.928. It does not preclude a more general multiplet with extra operator components, boundary counterterms or an independently supplied physical Hilbert-space representation.

For example L=3 (j=3/4), `D_L=diag(0,-1,+1,0)` and `D_(L+1)=diag(0,-5/4,0,+5/4,0)`. The three weighted maps have B_U ranks **2,2,1**, respectively. Their nonzero anomalies occur only at these missing-edge sites, directly linking the new calculation to the old v15.140 boundary mechanism instead of inventing a second anomalous structure.

## Gate 673 — physical selection rules / interpretation

The q=±1/4 charge belongs to the **formal geometric refined magnetic coordinate M**, which is not itself the genuine angular-momentum magnetic quantum number of a unitary irreducible spin-j representation on odd-quarter shells. Therefore the weighted maps cannot be called standard SO(3) rank-one dipoles just because their commutators have weight charges. Genuine hydrogen E1 transition operators change principal Coulomb shells, act on physically normalized `SO(4,2)` states, obey the actual angular momentum and spatial parity selection rules, and require properly normalized radial/KS factors. The existing hydrogen 2p/3p lifetime benchmark in v15.920 remains ordinary atomic physics and is not yet predicted by this q=2 algebra.

**Scientific verdict:** positive exact bulk raising covariance; negative boundary-localized Jacobi/covariance obstruction for all constant mixtures of the 3 weighted maps; v15.929 Audit repair actions addressed additively. No physical EM↔G coupling, radiative width, dimensional frequency, G value or universal clock selected.

**Gate reproducer:** `research-notes/k4_quarter_weighted_boundary_jacobi_v15_930.py`, commit **34b8df19e23113a48c9a19c4e61d703dc7d8cbba**. The same code was independently executed locally under SymPy before deposit and returned PASS for L=2..25, exact Jacobi identity, q−1 lower-residual charge, B rank/support and rank-3 no-cancellation map. **External Audit pending for new gate and the two repair copies.**

**Next nonredundant test:** Solve a *boundary-corrected* charged tensor algebra with explicit extra components and require Hermiticity/adjoints, formal Casimir-defect consistency, and q=2 sector selection. First compare its exact algebraic dimension and normalization freedoms to already-proved v15.602, v15.627; do not promote to physical hydrogen E1 without an independently derived SO(4,2)/KS dipole bridge and line-frequency/branching predictions.

**HANDOFF Audit/Muse:** rerun both corrected copies, check all 420 v15.921 WebGL sample points and all 80 v15.926 shells; verify Jacobi signs and rank-three cancellation obstruction, and independently test physical identification caveats. Do not modify previously certified ledgers or scripts.
