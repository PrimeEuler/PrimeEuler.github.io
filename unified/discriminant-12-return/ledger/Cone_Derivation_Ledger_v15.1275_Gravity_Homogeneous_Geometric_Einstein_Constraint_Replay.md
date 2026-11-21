# Cone Derivation Ledger v15.1275 — Direct homogeneous Bianchi-I Einstein tensor versus Maxwell–K4 solid stress at five grids

**Date:** 2026-11-21 Eastern. **Gravity/Cone lane.** **Prewrite inspected HEAD:** 029df32696c1e89fd0265bc9adb01dbab0f63aaf. **Status:** [PASS] homogeneous linearized 00 and three spatial Einstein equation residuals for a common transverse/Nyquist-clean Maxwell source; [C] this is an independent *geometrical reconstruction* of the previously specified v15.1264 Bianchi-I solution, NOT independent discovery of its dynamical equations; [OPEN] inhomogeneous k>0 Hamiltonian/momentum and all spatial Einstein–K4 constraints, time-dependent complete SVT metric, finite-baseline optical detector, and new physical quarter-grid selection. Additive only; retain frozen parents, Suzuki, Sandbox/Muse and Audit.

## Gate 1227 — reconstruct geometry from homogeneous metric, not tidal trace

Let the metric be `ds²=-dτ²+Σ_i a_i(τ)² (dx^i)²`, `a_i=a(1+u)e^{β_i}`, `a=τ/√3`, `Σβ_i=0`. Directional expansion rates are `H_i=1/τ+u'+β_i'` at first order. The exact Bianchi-I geometrical identities, before perturbative truncation, are

`G_00=H_xH_y+H_yH_z+H_zH_x`,
`G^i_i=-(H_j'+H_k'+H_j²+H_k²+H_j H_k)` for complementary `j,k`.

Their **first-order** perturbations about the coasting K4 solid are
`δG_00=6u'/τ`,
`δG^i_i=-2u''-6u'/τ+β_i''+3β_i'/τ`.

The original frozen solid's energy/pressure variation and shear constitutive law give `δρ_s=-6u/τ²`, `δp_{s,i}=2u/τ²-(8η_s/3τ²)β_i`. For the conformal Maxwell cell mean `R=ρbar_conf`, `δρ_EM=9R/τ⁴`, `δp_EM,i=3R/τ⁴+9Π_i/τ⁴`, `Π_i=(2R/3)-M_ii` and `M_ij=<E_iE_j+B_iB_j>`. Set `η_s=3/4`, `κC=1`.

The independent metric-to-matter residuals are therefore:
`C_00=6u'/τ +6u/τ² -9R/τ⁴`,
`C_ii=-2u''-6u'/τ+β_i''+3β_i'/τ - 2u/τ²-3R/τ⁴-9Π_i/τ⁴+2β_i/τ²`.

The v15.1264 specified initial-value solution `u=(3R/2)(τ-1)/τ²`, `β_i''+3β_i'/τ+2β_i/τ²=9Π_i/τ⁴` is inserted *after* constructing the geometric expressions. Because those are the equations originally solved, passing is a nontrivial implementation/sign/normalization regression but **not independent physical closure of k>0 ADM constraints**.

## Gate 1228 — five-grid, 33-slice directly computed results

The Maxwell stream is the original v15.1078 compact sampled source, transverse Fourier projected, with common v15.1267 Nyquist-plane removal. Its source-free conformal evolution uses `ξ=√3 log τ`; the homogeneous electromagnetic `M_ij(τ)` is computed by complex Fourier Parseval, which matches the physical mean of the **same** real field on a 2N product grid because the common Nyquist/Hermitian condition is enforced. The same means drive both u and the three β_i. Source histories on 33 equal τ steps in [1,1.08] are spline-interpolated for adaptive ODE integration, evaluated on all 33 times.

| N³ | R | max |C00| | max_i,t |Cii| | max |Σβ_i| |
| --- | ---: | ---: | ---: | ---: |
| 16³ | 0.00036157226055914273 | 8.673617379884035e-19 | 1.3010426069826053e-18 | 8.470329472543003e-22 |
| 24³ | 0.0008184024500958875 | 1.734723475976807e-18 | 2.6020852139652106e-18 | 3.3881317890172014e-21 |
| 32³ | 0.0007676608970155845 | 2.6020852139652106e-18 | 4.336808689942018e-18 | 8.470329472543003e-21 |
| 40³ | 0.000782478551245894 | 1.734723475976807e-18 | 2.6020852139652106e-18 | 1.6940658945086007e-21 |
| 48³ | 0.0007786954245360617 | 2.6020852139652106e-18 | 2.6020852139652106e-18 | 3.3881317890172014e-21 |

The Maxwell mean-energy drift was <=1.3e-18 in absolute units in each run. The unusually low 16³ mean and 24³ overshoot highlight poor low-resolution spatial accuracy, not a failure of the algebraic constraint residual. At N=48 and τ=1.08, `u=8.011269799753727e-05`, `β=(4.864619067589825e-06,-1.625062804864408e-05,1.138600898105425e-05)`. All are dimensionless perturbative/model-normalized values.

**Local execution:** `/mnt/data/cone_gate/k4_bianchi_independent_einstein_constraints_v15_1275.py` was actually executed using local NumPy/SciPy, PASS all five grids. A functionally equivalent, separately authored canonical GitHub reproducer `research-notes/k4_bianchi_independent_einstein_constraints_v15_1275.py` committed SHA `029df32696c1e89fd0265bc9adb01dbab0f63aaf` requires an independent **exact-committed-byte** replay by Audit. No prior source was edited.

## Gate 1229 — next true inhomogeneous gravitational gate

The k=0 homogeneous metric now has both Hamiltonian and spatial Einstein-component regression across time. It was already derived in v15.1264; the incremental result here is independent reconstruction of `G^i_i` and five-grid replay with **the Nyquist-clean, dealiased-compatible** source convention, with stronger explicit spatial residual reporting. No independent k>0 Einstein momentum constraint has yet been tested. For full closure:

1. Use the identically conserved v15.1274 projected dealiased `ρ,F,T_ij` histories for every k>0 SVT source and match their k=0 mean and `Π_i` to the background.
2. Recover lapse `Φ_N`, scalar spatial potential `Ψ_N`, transverse shift `B_i`, and TT tensor `γ_ij` alongside dynamical solid P,V,T and background u,β; use archived v15.729 pressure-corrected gauge formulas and v15.787 metric-to-Riemann identities.
3. Derive the linearized `δG^0_0,δG^0_i,δG^i_j` **from the constructed four-metric** independently of the K4 mode evolution and assemble the full solid stress from its same original frozen material action, not from postulated tide/trace equality. Quantify all Fourier/time residuals, including off-diagonal spatial stress and constraint propagation.
4. Do not yet compute finite photon–mirror–clock observables from the still-unreconstructed causal metric. The matched Einstein–Maxwell plus identical K4 solid comparator remains null.

**AUDIT:** independently check Bianchi-I geometry, the isotropic solid pressure sign in `C_ii`, k=0 Maxwell Parseval/source equivalence after Nyquist cleaning, and exact committed Python replay. Distinguish the already-solved ODEs from a genuinely independent inhomogeneous gravitational constraint.

**Scientific boundary:** the quarter-grid / Casimir arithmetic has no independently justified new gravitational interaction or dimensionless Newton-G-free observable; this remains ordinary Einstein–Maxwell+K4 solid.
