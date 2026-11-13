# Cone Derivation Ledger v15.938 — Odd-quarter position-like quadrupole and the boundary tensor obstruction

**Date:** 2026-11-13 US Eastern. **Lane:** Gravity. **Parents:** audited odd-quarter Casimir distinction v15.625, no ordinary SU2 odd-quarter j v15.630, original-step defect theorem v15.602/v15.572, prior bicone quadrupole and physical hydrogen comparators Gravity v15.935–937. **Live HEAD immediately prewrite:** 3c56f672b176ff0963c319f8b4d81bf0702bb14b. New target path checked absent. Add-only; no changes to Suzuki, audit, sandbox or older objects.

**Question:** Can one derive the physical, rank-two tidal/position quadrupole directly on the odd-quarter q=2 mesh, without identifying its distinct formal Casimir with the EM one or fitting hydrogen's reduced radial amplitudes?

**Status:** [D] precise obstruction for the minimal intrinsic quadratic candidate; [N] explicit finite exact checks L=1,3,...,31; [O] independent gravity angular generators, physical position operator, normalization and new G-free observable.

## Gate 699 — identify the three different “Casimirs” before building a tensor

On odd `L`, the original q=2 shell has `j=L/4`, states `m_i=−j+i/2` for i=0..L, and *original step-one* raising `J_+|i>=sqrt[(L−i)(i+2)/4]|i+2>` where i+2≤L. The Hermitian adjoint defines J−; M is diagonal m_i. **This is not the co-scaled closed refined-step SU2**.

Define `C_geom=j(j+1)I`, and the actual quadratic of the retained operators `C_def=M²+(J+J−+J−J+)/2`. The exact old boundary identity is **C_geom−C_def=E_L**. For odd L≥3, the two edge-source eigenvalues of E are `c/2=(j+1/4)/2`, with all other values zero, trace `c=j+1/4`, rank 2. L=1 is degenerate, `E=(1/4)I_2`, rank 2.

At L=3, `C_geom=(21/16)I_4`, whereas **C_def=diag(21/16,13/16,13/16,21/16)** in site order. `[C_def,J+]` has rank 2 for L≥3 and does not vanish: **C_def is not central** in the defective original-step ladder. This is the already established boundary problem, not a new gravitational Casimir.

## Gate 700 — explicit minimal quadratic candidate and necessary rank-two covariance test

The natural analogy of the bicone axial tensor is **Q_trial=3M²−C_def**. It is a well-defined Hermitian geometric matrix. The formal-shell alternative **Q_formal=3M²−C_geom** differs exactly by the boundary defect: **Q_trial−Q_formal=E_L**. Thus even this seemingly innocuous replacement introduces localized boundary-sensitive matrix elements.

For any genuine SU2 spherical rank-two operator `T_(2,0)`, a necessary tensor covariance condition is **ad_(J+)³(T_(2,0))=0** (successive adjoint raising beyond q=2 must vanish). Under the proposed identification of the *original defective* quarter J+ with physical SU2 raising, evaluate the condition on Q_trial. It vanishes accidentally for L=1,3,5 where chains are too short, but for **every tested odd L≥7 through 31**, **ad_(J+)³(Q_trial)** is nonzero of rank **2**, localized in the finite boundary ladders. Hence the minimal quadratic Q_trial is **not** a conventional rank-two tensor with respect to this original quarter-grid ladder for L≥7.

This is a negative result for the **specified trial operator and specified defective ladder**, not an impossibility theorem for all modified tensors, different gravitational Lie algebras, higher-rank extensions, or physically justified boundary repairs. In particular one cannot demand an SU2 rank-two identity from an algebra that is known not to be SU2 and then conclude no gravity representation exists.

## Gate 701 — dimensional / physical position obstruction

For odd L, dimension of the native quarter shell is **L+1**, which is even. The previously matched physical hydrogen n_H=3 SO4 bicone has dimension **9** and spin sectors 1+3+5. Therefore **no individual odd-quarter q=2 shell is unitarily equivalent to that complete nine-state hydrogen bicone**. A physical mapping would require a nontrivial subspace/projection, direct sum, added carrier or different Hilbert space, with its action and normalization independently specified. Moreover nothing in the parabola factors identifies the abstract M coordinate with the actual spatial position z or `x_i x_j` in Fermi-normal tidal Hamiltonian. The three Coulomb reduced amplitude scale factors in v15.937, 45/2, 24, 36, do not emerge from this quarter-grid construction.

**Scientific result:** The distinct geometric quarter Casimir is preserved and the natural local quadratic candidate is explicit, but it fails the necessary conventional rank-two covariance test on all sufficiently large tested odd-quarter shells, and the direct hydrogen carrier identification is dimensionally impossible. No physical gravity tidal tensor, massless helicity-two mode, novel frequency, coupling, or experimentally distinguishing dimensionless number was derived.

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_oddquarter_position_tensor_boundary_v15_938.py`, additive commit **3c56f672b176ff0963c319f8b4d81bf0702bb14b**. Local independently run SymPy construction checked 16 odd L shells 1..31, E/C spectra and rank, noncentrality, triple adjoint-commutator rank (short-shell exceptions) and even-dimension obstruction. **Independent Audit pending.**

**NEXT:** If advancing, derive a non-SU2 gravitational generator set and action from independent physical input (e.g. source-derived Lorentzian tidal/connection field), then specify a position or quadrupole operator that is Hermitian with the correct gravitational symmetry and measure. Compare a field-normalized response with the same operator embedded in ordinary Maxwell/GR or Coulomb physics; do not fit three reduced dipoles or assume the quarter formal spectrum itself supplies spacetime dynamics. Preserve the old audited q=2 open-boundary theorem and the parked Suzuki physical integration.

**HANDOFF Audit:** Check the exact L=3 C_def spectrum, L≥7 triple-adjoint failure, L≤5 accidental vanishing, distinction between geometric C and actual noncentral quadratic, and the scope of the nine-dimensional physical comparison.
