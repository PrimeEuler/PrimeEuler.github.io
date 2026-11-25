# Cone Derivation Ledger v15.1464 — A constraint-satisfying longitudinal Jordan block obstructs strong hyperbolicity of raw geodesic ADM

**Date:** 2026-11-25 Eastern. **Lane:** Gravity/Cone. **Status:** [EXACT MATHEMATICAL NEGATIVE] unit-lapse, zero-shift *unmodified ADM* has a non-diagonalizable zero-speed longitudinal principal subsystem, despite **both linear vacuum Einstein constraints vanishing** on that subsystem. It admits arbitrarily large high-spatial-frequency growth in the natural first-derivative metric norm at fixed positive time, so it is NOT a satisfactory strongly hyperbolic long-time field-evolution formulation. [NOT CLAIMED] any physical GR instability or faster-than-light signalling. [NEXT] strongly hyperbolic generalized harmonic / Z4 / appropriately gauge-fixed BSSN formulation, fully coupled to curved-H² sigma fields. Strict additive; certified Lane A/Sandbox/Audit objects unchanged. Parents v15.1459 short-time 3D raw ADM evolution; v15.1460/1463 Ricci aliasing and oversampling; Audit Round 648 v15.1461 verified v15.1459–1460. v15.1462 Sandbox G trace confirms no independent G selector.

## Gate 1388 — a literal zero-speed gauge/Jordan block with zero constraints

Linearize vacuum Einstein ADM about a flat Minkowski spatial slice with lapse α=1 and shift β^i=0. Let Fourier wave vector p=(k,0,0), k>0, and take **only** longitudinal metric and extrinsic-curvature components `h_xx(t,x)=H(t) exp(ikx)`, `K_xx(t,x)=P(t) exp(ikx)`. All other tensor components vanish. The entire linearized spatial Ricci tensor `R_ij[h]` vanishes for this pure-longitudinal metric perturbation, as can be verified using

`R_ij=½(∂_k∂_i h_kj+∂_k∂_j h_ki−∂_i∂_j tr(h)−Δ h_ij)`.

Both linear vacuum constraints are **identically zero** at all times:

`H_constraint=∂i∂j h_ij−Δ tr h=0`,
`M_i=∂j(K_ij−δij tr K)=0`.

Nevertheless, linearized raw ADM evolution gives

`∂t H=−2P,quad ∂t P=0`.

Its 2×2 evolution matrix is the nontrivial nilpotent Jordan block `J=[[0,−2],[0,0]]`, with `J²=0` and double eigenvalue 0 but just one independent eigenvector. The exact propagator is `exp(tJ)=I+tJ`, so `H(t)=H(0)−2tP(0)`. This is a **zero-speed gauge-type sector**, not a radiating TT graviton mode. The finite-dimensional linear ODE itself is harmless at a fixed wave number.

## Gate 1389 — high-frequency loss of uniform derivative control

In the standard mixed-order-in-space ADM initial-value norm `||h||_(H¹)+||K||_(L²)`, take single-mode initial `H(0)=0,P(0)=1`, with L² amplitude normalized independently of k. At time t>0, `H(t)=−2t`, and the squared Fourier H¹×L² norm becomes

`||state(t)||²=1+4t²(1+k²)`.

Thus its amplification grows as `~2kt` for k→∞ at any fixed t>0, while the initial H¹×L² norm is 1. There is no frequency-independent energy estimate of that form for the raw fixed-lapse ADM formulation. This is the familiar weak-hyperbolicity gauge obstruction; it explains why the nice short-time RK4/FFT residuals of v15.1459 and the near-perfect oversampled Ricci evaluation of v15.1463 do **not** establish a long-time well-posed numerical Einstein system. A strongly hyperbolic gauge-fixed formulation supplies appropriate propagating/gauge constraints and a well-posed energy estimate.

**Actually executed exact SymPy local test:** `/mnt/data/cone_gate/k4_adm_geodesic_jordan_v15_1464.py` verified all Ricci components, both ADM constraints, the Jordan matrix and exponential, and positive-time Fourier norm amplification:

| k | normalized H¹×L² norm at t=1 |
|---:|---:|
| 1 | 3.000000 |
| 4 | 8.306624 |
| 16 | 32.078030 |
| 64 | 128.019530 |
| 256 | 512.004883 |

**Additive GitHub reproducible source:** `research-notes/k4_raw_adm_longitudinal_jordan_v15_1464.py`, commit **7fbe9f82c407790daf5bd1014d796ac82bc2ad18**, equivalent symbolic derivation, exact committed-byte Audit replay pending. The preliminary local SymPy program initially contained a misspelled double-index summation in an assertion, which failed; it was corrected **before** the mathematical test and commit, with no change to physical equations. That local coding mistake is not hidden or a failed physical consistency gate.

## Audit and physical interpretation

**AUDIT:** Independently calculate the complete linearized Ricci and both constraints on the longitudinal plane wave, prove the Jordan block non-diagonalizable, check H¹ metric versus L² curvature norm growth and distinguish physical TT characteristic speeds from nonpropagating gauge modes. Confirm the v15.1463 Fourier oversampling diagnostic and its separation from complete evolution. Independently test whether the generalized harmonic gauge-fixing and constraint-damping additions produce a strongly hyperbolic wave principal symbol for metric and the ordinary H² sigma system.

**NEXT:** Implement a **strongly hyperbolic generalized harmonic Einstein–H²** evolution with a precise gauge constraint, monitor the Einstein constraints and gauge constraints, and carry out longer T=.04 and larger time-window convergence tests on appropriately filtered/oversampled 3D grids. Only after that start the actual Einstein–Maxwell–Weyl–H² higher-derivative EFT through a covariant order-reduction/metric-stress calculation, including the local characteristic warning v15.1420. No metric-only or sigma-only calculation selects G from the quarter q2=1/16 carrier; the exact null-affine 3:1 and historical Dirac 45.31 are not parameter-free gravitational predictions.
