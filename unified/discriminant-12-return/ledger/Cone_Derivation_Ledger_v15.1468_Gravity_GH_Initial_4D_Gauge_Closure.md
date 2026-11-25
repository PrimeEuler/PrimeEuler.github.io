# Cone Derivation Ledger v15.1468 — Harmonic lapse and shift initial derivatives for 3+1 nonlinear Einstein–H² slices

**Date:** 2026-11-25. **Lane:** Gravity/Cone. **Status:** [EXACT] For arbitrary 3+1 ADM spatial metric γij and Kij, initial lapse α=1 and shift βi=0 with harmonic-coordinate gauge source Hμ=0, the harmonic coordinate conditions Γμ=0 require **nontrivial initial time derivatives** dotα=−K and dotβ^i=γ^{jk} Γ^i_jk[γ] (spatial metric Christoffel contraction). [NUMERICAL PASS] reconstruct the **complete 4-dimensional** spacetime Christoffels from all spacetime metric derivatives and verify Γ^μ=0 on a nontrivial 3D periodic conformal slice with nonzero traceless K perturbation, maximum residual 1.735×10^−18 on 12³/16³/24³. [OPEN] full nonlinear generalized-harmonic evolution, wave-gauge constraint propagation, coupling and physical quarter selector.

## Gate 1394 — derive actual gauge initialization, not assume unit lapse for all times

For lapse α=1, βi=0 on the initial slice, the 4-metric is g00=−1, g0i=0 and gij=γij. Its time derivatives are ∂t g00=−2 dotα, ∂t g0i=γij dotβ^j and ∂t gij=−2Kij (the **initial** relations, not a geodesic-lapse gauge imposed forever). With g−1=diag(−1,γ−1), directly contracting the spacetime Levi-Civita symbols gives

Γ^0=−dotα−K,
Γ^i=−dotβ^i+γ^{jk} {}³Γ^i_jk.

Thus harmonic gauge Γ^μ=0 requires dotα=−K and dotβ^i=γ^{jk}{}³Γ^i_jk. For γij=e^(2ψ)δij in three spatial dimensions, γ^{jk}{}³Γ^i_jk=−e^(−2ψ) ∂iψ. Importantly, the nonzero *initial* lapse/shift derivatives do not change the intrinsic ADM Hamiltonian/momentum initial constraints, which are separately determined by γij and Kij and the matter fields. They make the 4D coordinates harmonic at that slice. The second time derivatives and gauge constraint propagation require the Einstein field equations and remain separate.

**Actually executed standalone Python** with N=12,16,24 and ψ=3×10^−6[cos x+.7sin(2y)+.3sin(x+y)], Kij=−.005259956 γij plus symmetric nonzero offdiagonal Kxy=(1e−5 sin z) exp(2ψ). Recompute complete ∂μgαβ and all Γα_μν using FFT spatial differentiation; contract with true gμν inverse. Maximum |Γα|=1.734723475976807e−18 at all tested resolutions, average K=−.015779868 and |dotβ|≤5.1000306000918e−6. These fields are an **illustrative conformal ADM slice**, NOT the exact v15.1453 constrained data. Gauge initial prescription is algebraic and applies to v15.1453 too, once its γij/Kij are imported; this implementation has not imported them yet.

**Reproducer:** locally executed \`/mnt/data/cone_gate/gh_initial_gauge_v15_1468.py\`; exact same algorithm additive GitHub \`research-notes/k4_gh_initial_gauge_v15_1468.py\`, commit **2d73437c5b6dcbcc2259da62934de461bf205877**. Independent exact committed-byte Audit replay pending.

**AUDIT:** verify sign of K, all 4D metric time derivative expressions, contraction Γ^0=−dotα−K, Γ^i=−dotβ^i+³Γ^i and conformal −gradψ/e^(2ψ), and reproduce all grid checks. Distinguish this harmonic-gauge initial prescription from a numerically evolved GH gauge and from exact matter Einstein constraint satisfaction. Do not call this full strongly hyperbolic Einstein–H² evolution.

**NEXT MAIN:** construct nonlinear 3+1 GH metric and matter wave equations with gauge constraints and stress conservation, initialize from actual v15.1453 constrained γij/Kij, and run Fourier-filtered short- and long-time constraint convergence. The known v15.1420 Weyl–F–area high-frequency branch is still open. κ=8πG still prescribed rather than derived from Q=1/16.