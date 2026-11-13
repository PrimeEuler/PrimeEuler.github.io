# Cone Derivation Ledger v15.937 — Actual hydrogen n_H=3 position quadrupole versus glued bicone Runge–Lenz quadrupole

**Date:** 2026-11-13 US Eastern. **Track:** Gravity, physical operator bridge. **Parents:** v15.905, v15.931–936, staged `arxiv/note-bicone-dipole-alpha/Note_BiconeDipole_FineStructure_v1.0.tex`, physical Coulomb / tidal comparator v15.912–914. **Live HEAD immediately before write:** 5d07d116d8f9d22d6df1d162ca4ed744ebbb297b; target path checked absent. Strictly additive; Suzuki frozen work, existing audit results and historical ledgers unchanged.

**Question:** Does the auxiliary bicone rank-two tensor `Q_A=3(J_z−K_z)²−(J−K)²` actually agree, up to a single scale, with the physical position tidal quadrupole `Q_x=3z²−r²` on the correctly matched hydrogen principal shell `n_H=3`? Require exact physical normalized hydrogen radial integrals and all angular blocks without fitting amplitudes.

**Status:** [D] exact hydrogen Coulomb-integral matrix and exact coupled-spin transformation; [N] no single scale can identify physical position quadrupole with auxiliary Runge–Lenz quadrupole; [D] they have identical angular support and are proportional *separately on each of three irreducible channel blocks*; [O] source-derived graviton/quarter-grid coupling, dynamical selector, experiment.

## Gate 696 — fix the n labels and actual position operator

The older geometric pair (n,1) with **factor n=2** has single-cone spin j=1 and nine states after gluing. In the standard SO(4) hydrogen bicone, the same pair is **principal n_H=2j+1=3**, so compare only the hydrogen `3s,3p,3d` states (l=0,1,2, m=−l..l). Actual weak-field Fermi-normal tidal coupling uses **x_i x_j** in physical length units, not the Runge–Lenz operator A=J−K. For axial traceless field choose `Q_x=3z²−r²=2r²P_2(cosθ)` in units a0². Neither physical G nor an observed rate is entered.

Independent normalized Coulomb radial integrals at n_H=3 are exactly

**∫R_30 R_32 r⁴ dr =45 sqrt(10) a0²**,

**∫R_31² r⁴ dr =180 a0²**,

**∫R_32² r⁴ dr =126 a0²**.

The angular matrix factor is `2(−1)^m sqrt((2l+1)(2l'+1)) (l,2,l';0,0,0)(l,2,l';−m,0,m)` in terms of two standard Wigner 3j symbols.

## Gate 697 — exact nine-state comparison

Transform auxiliary `Q_A` on spin1⊗spin1 to the same `|l,m>` basis with ordinary real Clebsch–Gordan coefficients. Its exact projected blocks have the same selection rules as physical `Q_x`: only **0↔2**, **1→1**, **2→2** are nonzero (for q=0); all other blocks vanish. Every nonzero channel block is **proportional**, but with a *different exact factor*:

**P_2 Q_x P_0 = (45/2) a0² P_2 Q_A P_0**, and reverse,

**P_1 Q_x P_1 = 24 a0² P_1 Q_A P_1**,

**P_2 Q_x P_2 = 36 a0² P_2 Q_A P_2**.

These are exact identities of nine-by-nine matrices; the single-scale identification `Q_x=c a0² Q_A` is **false**. Specific reference matrix elements:

**<3d,m=0|Q_x|3s,m=0>=90 sqrt2 a0²**, versus auxiliary **<2,0|Q_A|0,0>=4 sqrt2**;

**<3p,0|Q_x|3p,0>=144 a0²**, versus auxiliary **6**;

**<3d,0|Q_x|3d,0>=72 a0²**, versus auxiliary **2**.

The full diagonal triplet `3p` is `(−72,144,−72) a0²`; `3d` diagonal quintet is `(−72,36,72,36,−72) a0²`; these reproduce the auxiliary patterns from v15.936 with scale factors 24 and 36, respectively.

## Gate 698 — exact projected Frobenius strengths, physical interpretation

The Hilbert–Schmidt squared block strengths, rows l=0,1,2 and columns l'=0,1,2, are:

Auxiliary `Q_A`: **[[0,0,32],[0,54,0],[32,0,14]]** (v15.936).

Physical `Q_x/a0²`: **[[0,0,16200],[0,31104,0],[16200,0,18144]]**.

The ratios in each nonzero block equal (45/2)², 24² and 36², respectively. These are ordinary hydrogen radial angular-momentum coefficients fixed by the Coulomb potential. The bicone SO(4) geometry fixes angular support and relative m-dependence *within* each channel, but does **not** fix the three independent reduced matrix elements from geometry alone. A cross-shell/beyond-n_H=3 comparison would need even more physical radial data and an actual SO(4,2)/KS representation.

This is an important **negative novelty result**: inserting the three factors into the bicone would *repackage* known Coulomb physics, not derive gravitational tidal response from Cone geometry. Conversely, taking the physical Fermi-normal `H_tidal=(m/2)E_ij x^i x^j` and the real hydrogen wavefunctions gives ordinary GR-plus-quantum-mechanics tidal spectroscopy. Neither n=2 rest/Casimir circle coincidence nor the formal quarter-gravity Casimir C_{2,L} supplies the missing gravitational field strength or a massless helicity-two mode.

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_hydrogen3_position_vs_bicone_quadrupole_v15_937.py`, additive commit **5d07d116d8f9d22d6df1d162ca4ed744ebbb297b**. Executed exact SymPy check locally before repository deposit: all normalized radial integrals, CG basis transformation, every one of the 81 matrix entries, block strengths and exact factors PASS. External Audit pending.

**NEXT:** Preserve the genuine distinction between physical position quadrupole and Runge–Lenz quadrupole. If seeking a predictive gravitational sector, construct an independently motivated `x_i x_j` image or tidal-field carrier on the *odd-quarter* Casimir module, compare its reduced elements to this fixed hydrogen benchmark without channel-by-channel fit, and require a dimensionless field-normalized residual beyond standard tidal E1/E2 selection. Otherwise record that the simpler bicone bridge is exhausted at angular structure.
