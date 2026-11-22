# Cone Derivation Ledger v15.1318 — Evolved transverse-vector Einstein momentum and offdiagonal spatial closure

**Date:** 2026-11-22 Eastern. **Track:** Gravity/Cone. **Status:** [D] direct metric-to-Einstein vector 0y and yz operators for coasting FLRW; [D] independently varied original solid offdiagonal spatial stress; [D] both sourced time-dependent vector Einstein identities under the already archived K4 vector Euler equation and Maxwell transverse-momentum Ward; [O] exact newly committed combined reproducer has not been independently replayed by Audit, remaining TT gravitational closure and finite-time full metric, continuum convergence, causal optical experiment and independent physical quarter-grid coupling. **Immediately pre-ledger live HEAD:** 21850b9976a2ad8f8db6a38a801706e2260398a3. New v15.1318 ledger path checked absent. Strictly additive; preserve historical source assets, Audit-owned v15.1316, Suzuki, Sandbox/Muse.

## Gate 1247 — independent vector metric geometry

In the same (-+++) metric convention as v15.787, set `a=τ/sqrt3`, a nonzero Fourier mode along z and one transverse polarization `g0y=-a B_V(τ)e^(ikz)`; vector spatial gauge `F_i(metric)=0`. Perturb the inverse metric and compute the complete first-order Christoffels/Ricci/mixed Einstein tensor, retaining all FLRW background terms. The direct calculation gives

`delta G^0_y= sqrt3 k² B_V/(2τ)`,
`delta G^y_z= sqrt3 i k (τ B_V'+2 B_V)/(2τ²)`,
`R_background=6/τ²`.

The offdiagonal metric perturbation contributes to the mixed-index Einstein tensor through both `δg^{μν}G^(0)_{νρ}` and the perturbed Ricci tensor. A standalone independent local SymPy Christoffel calculation was actually run and produced the displayed operators; the latter are **not** inferred from the electric Weyl or local tidal Riemann channel. The other transverse polarization follows by rotational covariance about k, but its full-grid numerical source remains to be integrated.

## Gate 1248 — the original relativistic solid has a nonzero vector momentum and shear

Use the frozen physical material action
`F(B)=C(det B)^(1/3)[1+eta_s(tr B²/(tr B)²−1/3)]`,
`phi^I = x^I - f_V e^I e^(ikz)`, with `e = yhat`, and `g0y=-a B_V e^(ikz)`. The **minus sign** in `phi^y=y-f_V e^(ikz)` is the archived vector-displacement convention required to match v15.710/v15.721; do not silently substitute the scalar `phi^I=x^I+∂^I P` sign.

Linearizing `T^μ_ν=-F δ^μ_ν+2F_AB ∂^μ phi^A ∂_ν phi^B` gives the solid transverse momentum

`δT^0_y,solid=(2C/3)(f_V' - B_V/a)`,

and the **spatial offdiagonal solid stress**

`δT^y_z,solid= -4 eta_s C i k f_V/(9a²)`.

For `eta_s=3/4, κC=1`, the latter becomes `-ik f_V/τ²`. This sign and coefficient were independently computed from the full matrix material invariant including its offdiagonal B_yz strain, *not* inferred by subtracting Einstein geometry. The direct local SymPy calculation of the matrix derivative `∂F/∂B` gave `-4i C eta_s k f_V b/9`, where `b=a^-2`, and simplified the difference to exact zero.

The physical Maxwell source, with conformal transverse flux `F_perp` and stress `T_perp,n`, supplies `δT^0_y,EM=3sqrt3 F_perp/τ³`, `δT^y_z,EM=9 T_perp,n/τ⁴`. Its transverse momentum conservation is `F_perp'=-i sqrt3 k T_perp,n/τ`; the conservation-preserving dealiased Fourier stress of v15.1274 supplies this relation in the projected interior subspace.

## Gate 1249 — exact on-shell transverse momentum and spatial shear

The archived source-first vector shift and displacement equations, v15.710/721/v15.1235, at eta_s=3/4 are

`D=4+3k²`,
`B_V=4τ f_V'/[sqrt3 D]+18 F_perp/[τ² D]`,
`f_V''+3f_V'/τ+D f_V/(2τ²)=-18 i T_perp,n/(k τ⁴)`.

Substituting them into the independently reconstructed geometric operators gives both Einstein equations exactly:

`C_0y = sqrt3 k² B_V/(2τ) - 3sqrt3 F_perp/τ³ -(2/3)(f_V' -sqrt3 B_V/τ)=0`;

`C_yz = sqrt3 i k(τ B_V'+2B_V)/(2τ²) -9T_perp,n/τ⁴+ik f_V/τ²=0`.

The first cancellation is algebraic from the sourced ADM shift constraint and the solid momentum contribution. The second is algebraic from Maxwell transverse momentum Ward, the driven vector solid equation and material shear. In separate local SymPy tests each expression simplified *exactly* to zero. This is a nontrivial independent metric/source sign and normalization regression, but since we use the archived sourced equations it is **conditional on-shell closure**, not a new independent gravitational interaction nor the full numerical three-dimensional time-dependent metric.

**Reproducer:** additive `research-notes/k4_vector_einstein_closure_v15_1318.py`, committed SHA **21850b9976a2ad8f8db6a38a801706e2260398a3**. It packages direct Christoffel-to-Einstein geometry, independent F(B) offdiagonal stress variation, and both on-shell Einstein equations. The separate mathematical pieces were executed in local Python/SymPy and each returned zero residual. The exact uploaded combined file was **not** executed byte-for-byte after commit: direct raw-GitHub fetch into the local container failed due DNS/network restrictions. Audit must replay the exact commit and report any integration/script error as an additive correction, not assume its PASS from this ledger.

## Gate 1250 — next field-equation gate

Together with v15.1314–1317, the **linear scalar sector** and the transverse-vector momentum/shear equations now have conditional analytic closure in the specified coasting Einstein–Maxwell+K4 action. The critical remaining dynamical field equation is TT tensor evolution reconstructed independently from the spatial metric and original action. Derive direct `δG^i_j,TT` from `gij=a²(δij+γij)`, independently vary K4 solid TT stress, insert Maxwell TT stress on a common dealiased Fourier grid, and test both TT polarizations. Only then build the single **complete time-dependent four-metric**, check actual all-component `Gμν-κ(T_EM+T_K4)μν` residuals on common numerical time/spatial grids, and evaluate a finite-baseline causal photon/mirror/clock observable with identical-action GR comparator.

**Audit handoff:** independently run committed v15.1318 code, verify (-+++) mixed-index 0y signs and background inverse-metric contributions, differentiating the *unexpanded* F(B), physical vector displacement sign, and the dependence of the offdiagonal Einstein spatial operator on both `B_V'` and `2B_V/τ`. Keep the archived historical v15.1316 Audit number intact.

**Scientific boundary:** the mathematical 1/4-Casimir mesh has not supplied an independently justified Einstein-action modification or G-free observational prediction. All sourced identities here agree with ordinary Einstein–Maxwell and the *same* K4 solid, so the matched-action null remains exact.
