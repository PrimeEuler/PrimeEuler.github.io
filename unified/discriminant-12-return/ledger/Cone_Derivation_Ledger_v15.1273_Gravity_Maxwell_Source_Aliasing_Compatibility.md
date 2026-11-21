# Cone Derivation Ledger v15.1273 — Maxwell native/dealiased SVT source compatibility obstruction

**Date:** 2026-11-20 Eastern. **Lane:** Gravity/Cone. **Status:** [N] numerical compatibility of the historic v15.1267 native-grid Maxwell tidal source and a fully dealiased v15.1271 conserved source is *false at fixed resolution*, even though homogeneous energy agrees; [D] five-grid native/dealiased mode-by-mode comparison and fixed-low-mode refinement; [OPEN] new single-prescription full SVT metric, independent Einstein+K4 constraints, converged optical response and Cone-only physical interaction. **Immediately prewrite inspected HEAD:** 8e75d7aca9ed29efde2317ecaa136b9e0610d229. External Audit Round 621 has now independently executed and certified v15.1266–1271 at v15.1272 (SHA da27e843380893a7fc97e544c2b20d0326097918), including the original v15.1266 and nonlinear aliasing negative controls. The new target v15.1273 was checked absent before writing. All archived parent files, Audit, Suzuki, Muse and Sandbox remain unchanged.

## Gate 1221 — compare actual gravitational *source* coefficients, not merely homogeneous energy

For exactly the v15.1078 compact electric initial field, shared transverse projector and v15.1267 Nyquist-plane removal, evolve Maxwell `Ehat=h cos(k sqrt(3)log tau)` and `Bhat=-i(q cross h) sin(k sqrt(3)log tau)/k` to tau=1.08. Form Maxwell conformal `rho=(E²+B²)/2`, `F=E cross B`, `T_ij=rho delta_ij-E_iE_j-B_iB_j` from both (A) native N³ inverse FFT products (the original v15.1262/v15.1267 Fourier stress scheme) and (B) 2N³ zero-padded Fourier reconstruction/products (the conservation-consistent v15.1269/v15.1271 scheme). Fourier-transform with the relevant M^-3 normalization and compare coefficients at **matching signed physical wavevectors**, excluding ambiguous N-Nyquist component bins. This holds the Maxwell initial data, propagation and homogeneous energy fixed: it isolates **only product aliasing**, not different source models.

At every N, the *mean* conformal Maxwell energy agrees between A/B to <=5.5e-19 (expected, by Parseval for the common Hermitian source), but the nonzero Fourier coefficients can differ materially.

Define the sector relative discrepancy as `max_{|m_j|<N/3} |S_native(m)-S_dealiased(m)| / max_{|m_j|<N/2}|S_dealiased(m)|`, with component maxima for flux and tensor stress. This is a **largest coefficient error normalized by the sector's largest reference coefficient**, not a relative error per mode (which could be arbitrarily large near zeros).

| N³ | rho retained-band rel. | flux retained-band rel. | stress retained-band rel. |
|---|---:|---:|---:|
| 16³ | 0.1695088411 | 0.6556348279 | 0.3486002016 |
| 24³ | 0.0649588255 | 0.5769297633 | 0.2616471007 |
| 32³ | 0.0035453081 | 0.1515482159 | 0.0691478080 |
| 40³ | 0.0084994765 | 0.0938676583 | 0.0480207049 |
| 48³ | 0.0010909706 | 0.0036626615 | 0.0024600721 |

The discrepancy is not strictly monotone at every N, and spatial center tidal amplitudes previously varied even at N=32/40/48. Therefore do not claim continuum-converged tides based on these source convergence hints.

## Gate 1222 — fixed low modes and physical consequence

For the stricter fixed Fourier box `|m_j|<=2`, relative discrepancies (same denominator as above) at N=48 are rho 7.14e-6, flux 9.84e-7, stress 1.35e-5; at N=32 they are rho 4.03e-5, flux 3.10e-4, stress 1.67e-4. These smaller low-wavenumber errors suggest the source inconsistency is largely an ultraviolet spectral representation issue for the sampled compact packet, but are not a proof of a particular continuum rate.

**Negative integration gate:** the v15.1267 pointwise `tr E=9rho/tau^4` passes for its own native-grid stress assignment. The separately Audited Maxwell Ward test passes for the **dealiased** stress. It does not follow that the same full inhomogeneous metric solves both tests without recomputing P,V,T and lapse/shift with one common stress convention. The k=0 homogeneous energy can agree even when anisotropic/nonzero Fourier stress disagrees; it is an insufficient equivalence criterion. A trace-only Einstein assertion cannot replace independent Hamiltonian, momentum, and spatial equations.

**Local execution:** source comparison was actually run with Python/NumPy on 16³,24³,32³,40³,48³ with new self-contained implementation, including source Nyquist filter, Fourier normalization, signed-frequency matching, energy mean checks and low-band/fixed-mode diagnostics. Additive canonical reproducer `research-notes/k4_native_dealiased_source_comparison_v15_1273.py`, SHA 8e75d7aca9ed29efde2317ecaa136b9e0610d229, is staged for independent Audit execution; the quoted local numbers were obtained from an equivalent independently authored script rather than byte-original GitHub post-upload execution.

## Gate 1223 — next falsification-first solver

Select scheme (B) to **retain the existing physical Maxwell Fourier field** but exactly evaluate all quadratic sources on the 2N product grid. Retain the full stress modes on that 2N grid, or explicitly declare/verify a consistent Fourier low-pass projection if K4 metric evolution is run on N; never compare an aliased full-grid Riemann to an unaliased Maxwell stress as if it were one solution. Recompute the complete scalar/vector/tensor source histories and a common homogeneous pressure/shear/Friedmann history, exposing `Phi_N,Psi_N,B_i,gamma_ij,u,beta_i`. Independently construct Einstein+solid stress for full metric `G_mu_nu-kappa(T_EM+T_K4)_mu_nu`, with local Fourier Hamiltonian, momentum, and spatial residuals and time propagation. Only then integrate finite-distance causal photon/mirror/clock.

**Audit handoff:** verify the new reproducer's 2N FFT coefficient mapping and exact parent Maxwell source, check convergence at fixed low k, ensure comparator denominators are explicitly stated, and do not treat this negative compatibility finding as a physical Cone-only signal.

**Novelty boundary:** still exactly Einstein–Maxwell coupled to the stipulated K4 solid; arithmetic quarter-grid structure has not supplied an independently justified new interaction or G-free gravitational observable.
