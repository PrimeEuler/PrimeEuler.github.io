# Cone Derivation Ledger v15.630 — Lane A: Larmor/rotor coupling cannot implement the quarter-only geometric Casimir transition as an ordinary SU(2) tensor

**Date:** 2026-11-10. **Parents:** v14.700 and `research-notes/Gravity_Rotor_Response_Operators.md` (audited 3D spherical rotor rank-1/rank-2 response and G-free gradiometry null), v15.135 §5 (Casimir sector distinction), v15.602 (all-q geometry and separate refined-step SU2), v15.625–628 (recovered all-q Casimir spectrum, parity, actual cross-shell and odd-rung cover), v15.629 External Audit Round 524 (all v15.619–628 verified). **Status:** [D] exact angular-momentum representation/selection-rule obstruction; [C] auxiliary geometric inter-shell shift; [O] gravity-sector dynamical carrier, energy spectrum and coupling. **Prewrite live HEAD:** 9f226717e408499b90e0ac9978032bb3525997d4; v15.630 duplicate search empty. Additive only; no Suzuki/far-tail/certified artifacts modified.

## Gate 124 — Larmor / rank-1 / rank-2 standard selection rules

Existing `v14.700` gravity-rotor gate uses the conventional *3D spherical rotor* with \(E_j/B=j(j+1)\), rank-1 \(\cos\theta\), and rank-2 \(P_2(\cos\theta)\). That research correctly distinguished it from the separately treated planar/Mathieu rotor. The Larmor generator \(J_i\) commutes with \(J^2\) and has \(\Delta j=0\). Under a conventional SU2 tensor of integer rank k, Clebsch–Gordan selection requires \(j'\in\{|j-k|,|j-k|+1,\ldots,j+k\}\), thus \(j'-j\) is integer. Rank 1 or 2 cannot yield the needed geometric jump \(\Delta j=1/4\), independently of reduced matrix elements. For ordinary *orbital* rotor multiplication by \(\cos\theta\), additional parity makes \(\Delta l=\pm1\); \(P_2\) gives \(\Delta l=0,\pm2\). This is stricter than, and consistent with, the general tensor selection rule. Even a conventional half-integer-rank spinor tensor would have half-integer, not quarter-integer, changes of spin label.

## Gate 125 — odd-quarter j values are not genuine SU2 spin irreps

The all-mesh **geometric** q=2 shell assignment is \(j=L/4\), \(C_{\mathrm{geom}}=j(j+1)=L(L+4)/16\), and odd L represent the gravity-candidate shells. An actual unitary SU2 irrep permits j only in \(\tfrac12\mathbb Z_{\ge0}\). On a hypothesized highest-weight with odd L, a \(4\pi\) rotation would act by \(e^{-i4\pi j}=(-1)^L=-1\), contradicting that \(4\pi\) is the identity in SU2. Therefore these odd-quarter geometric labels cannot *simultaneously* be conventional physical SU2 total spin values. This is an exact no-go for an identity of representations, NOT a denial of the geometric Casimir formula or of other gravity-side symmetries/extended carriers.

## Gate 126 — the previously constructed closed refined-step SU2 has a different Casimir

At q=2 the refined nearest-neighbor lattice \(m_i=-L/4+i/2\), i=0,...,L, can carry an SU2 algebra after scaling the generators/weights by q=2, as v15.602 already explicitly showed. Its genuine SU2 representation spin is \(J=L/2\), so \(C_{SU2}=L(L+2)/4\), **not** \(C_{\mathrm{geom}}=L(L+4)/16\). For L>0 these differ, and the difference is L(3L+4)/16, not a constant shift. The earlier *original-unit-step projected* ladder's defective Casimir \(C_{\mathrm{def}}=C_{\mathrm{geom}}1-E\) is a third, distinct construction. None is substituted for the user's already-known geometric quarter spectrum.

## Gate 127 — odd shift algebra is possible but has no rotor-derived matrix element

On an auxiliary direct-sum tower \(|L\rangle\), define \(\chi=(-1)^L\), \(C_{\mathrm{geom}}=L(L+4)/16\), \(W|L\rangle=|L+1\rangle\) on allowed edges. Then \(\{\chi,W\}=0\) and \([\chi,W^2]=0\), but \([C_{\mathrm{geom}},W]\ne0\) and \([C_{\mathrm{geom}},W^2]\ne0\). Such a W need not transform as a rank-1 or rank-2 SO3 tensor. Its Hermitian interaction \(gW+g^*W^\dagger\) has a freely supplied coupling g, and an enlarged carrier would need explicit physical representation and dynamics. The dimensionless rank-1/rank-2 rotor response \(\Xi=(1-d\ln g_{field}/d\ln R)/3\) from v14.700 remains standard gradiometry, not a Cone-novel gravitational prediction. No G or quarter-rung energy splitting is derived here.

## Verification, conclusion, independent audit

An exact SymPy reproducer and REPORT.md are in the conversation artifact `cone_rotor_casimir_124_127.zip`. Direct checks verified (1) the SU2 4π obstruction over L=0..31, (2) integer spin differences of nonzero rank-1/rank-2 Clebsch–Gordan coefficients, (3) exact finite-shell parity commutators and noncommutation with C, and (4) mismatch between genuine closed refined-step SU2 and geometric C for L=1..8.

**Verdict:** the audited standard Larmor/rotor interactions do NOT supply the missing EM↔odd-quarter transition. The quarter-shell Casimir is an exact *formal geometric* spectrum, but not a conventional physical SU2 irrep spectrum on odd L. A gravity-specific dynamical realization remains an open target; the older rotor's dimensionless test is legitimate but equivalent to standard gravitational field-gradient measurement.

**HANDOFF:** external-audit, gravity, sandbox; verify all four gates and crucial distinction between formal \(C_{\mathrm{geom}}\), defective projected original step, and genuine closed refined-step SU2. Audit precise Clebsch–Gordan selection and 4π central-element obstruction, and confirm scope of earlier v14.700 null result. No Suzuki physical-quarter integration; frozen production untouched.

**Next gate:** test a *specified* non-SU2 or enlarged dynamical carrier (e.g. independent sector gauge/tensor algebra or physically justified holonomy) for an authentic odd-rung generator with normalization determined independently of any fitted force constant. Do not promote a formal C(j) to physical spin without a representation.
