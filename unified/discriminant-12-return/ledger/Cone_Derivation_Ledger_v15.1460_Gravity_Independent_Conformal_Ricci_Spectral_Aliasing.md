# Cone Derivation Ledger v15.1460 — Independent full-connection Ricci versus exact conformal-curvature aliasing diagnosis

**Date:** 2026-11-25 Eastern. **Gravity/Cone.** **Status:** [EXACT geometric identity / N PASS] independent computation of the complete 3D Christoffel/Ricci curvature and the exact conformal scalar curvature on identical smooth weak Einstein–H² sigma initial data, identifying the precise Fourier aliasing floor limiting short-time ADM evolution v15.1459; [NEGATIVE] coarse N=16 is WORSE than N=12 due to Nyquist and nonlinear harmonic aliasing, and N=24 still has ~1e−8 absolute curvature disagreement, so coarse-grid apparently small constraint residuals do not certify numerical convergence; [POSITIVE] error decreases to ~1e−12 by N40; [OPEN] explicit spectral 3/2 padding or exact dealiasing, gauge formulation for well-posed long-time nonlinear 3+1 metric evolution, full Weyl–F–H² action metric variation, EFT cutoff, quarter-grid-selected coupling. Strictly additive, Sandbox v15.1458 and certified Lane A preserved. Parent v15.1459 canonical short-time inhomogeneous ADM evolution.

## Gate 1385 — independent spatial geometric identity

For conformal 3D spatial metric `γij=e^(2ψ)δij`, the scalar intrinsic curvature is **exactly**

`³R_closed=e^(−2ψ)[−4Δψ−2|∇ψ|²]`.

Separately construct at every spectral grid point the **complete** 3D Christoffel symbols

`Γ^a_ij=½γ^al(∂iγ_lj+∂jγ_li−∂lγ_ij)`,

and the full Ricci tensor

`R_ij=∂kΓ^k_ij−∂jΓ^k_ik+Γ^k_ijΓ^l_kl−Γ^k_ilΓ^l_jk`,

then `³R_Christoffel=γ^ijR_ij`.

In the continuum these are mathematically IDENTICAL. On a finite FFT collocation grid, products `e^(2ψ)`, nonlinear metric inverses and products of Γ can fold unresolved harmonics back into retained modes, while the closed-form conformal formula has fewer nonlinear products. Their **difference** measures the numerical aliasing/truncation error of the full connection-based computation, not a physical Einstein constraint defect. Compute ψ from the leading positive curved-H² sigma energy/Poisson solution with illustrative fixed κ=.003 and the same smooth N³ periodic profiles of v15.1450. This gives an independent, purely spatial error comparator without any time integration or evolution-equation uncertainties.

**Actual executed local program** `/mnt/data/cone_gate/k4_conformal_ricci_fft_v15_1460.py`, pure NumPy FFT and pointwise 3D tensor algebra. Equivalent separately authored additive GitHub `research-notes/k4_conformal_ricci_alias_v15_1460.py`, SHA **ebe90eff31ab532f67c3741df7afa188db1bfc84**. Exact committed-byte independent Audit replay pending.

| N³ | max |ψ| | max absolute `|³R_Christoffel−³R_closed|` |
| ---:|---:|---:|
| 12³ | 4.1753780124e−6 | 3.0960006706e−7 |
| 16³ | 3.9572146084e−6 | **4.2170121349e−6** |
| 24³ | 4.0899940164e−6 | 1.1061443545e−8 |
| 32³ | 4.2325634971e−6 | 1.5048015801e−10 |
| 40³ | 4.2620957663e−6 | 1.0428732734e−12 |

The N24/N32/N40 curvature discrepancies agree in order of magnitude with the **initial Hamiltonian residual floors** of v15.1459: 1.10589e−8, 1.50105e−10 and 1.12291e−12 respectively. They are therefore traced to nonlinear spectral Ricci reconstruction, not time stepping or a genuine failure of the initial constraint equations. N16's spectacularly worse curvature disagreement than N12 is a **negative** and forbids extrapolating monotone convergence from underresolved grids. The high-resolution trend is strong evidence for smooth-spectrum truncation/aliasing, but no rigorous infinite-resolution bound or zero-padding implementation has been established.

## Gate 1386 — interpretation and Audit handoff

The first short-time full inhomogeneous ADM Einstein–H² evolution (v15.1459) exhibited initial metric Hamiltonian errors that could not be explained by v15.1453's exact conformal constraint solution alone. This independent purely spatial comparison establishes their origin to the same numerical level: **the fully general Ricci implementation is converging to the exact conformal initial-geometry result, but slowly at N24 and very poorly at N16**. It also provides a test harness for future de-aliasing: a correct 3/2-padded pseudospectral evaluation of nonlinear Γ products should lower this difference at fixed nominal N, which must be tested rather than asserted.

**AUDIT:** independently derive conformal ³R formula and full Christoffel/Ricci signs, execute committed v15.1460 exact bytes, compare N12/16/24/32/40 table, verify v15.1459 initial Hamiltonian floor agreement, examine de-aliasing and code's FFT product conventions. Critical: ensure the source's ψ is computed from correct nonlinear H² target positive energy but recognize **this is the leading Poisson conformal ψ, not the fully nonlinear v15.1453 ψ**; the leading and full ψ differ at O(κ²), small enough that the observed aliasing floor comparison is about numerical implementation, not a claim of identical Cauchy fields.

**NEXT:** implement explicit padded/dealiased Ricci and then adopt a strongly hyperbolic evolution gauge (BSSN/generalized harmonic/Z4) for longer inhomogeneous 3+1 time runs, monitoring both Einstein constraints and sigma Noether/Bianchi stress. A full Weyl–F–H² interaction needs the complete 4D metric variation and controlled EFT order reduction before being treated dynamically; no G-free quarter-specific new gravitational observable has been derived.
